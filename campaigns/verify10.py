#!/usr/bin/env python3
"""Verify10 — Campaign 10 (Broad Wave 2B) targeted verification.
Standing method (= verify6-8): targeted CDX prefix queries filtered
to statuscode:200, direct sample downloads of every concrete pile
(size + md5 + magic), custody checks documented and never
circumvented. Samples to gold/campaign10-verify/. Run from
goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence

OUTDIR = "gold/campaign10-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=800_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def links_of(html, exts):
    return sorted(set(re.findall(r'(?:href|src)\s*=\s*["\']([^"\']+\.(?:' + exts + r')(?:\?[^"\']*)?)["\']', html, re.I)))

def main():
    out = {}

    print("\n== 1a. gletschervergleiche.ch — repeat-photo pages + image samples ==", flush=True)
    st, html = get_text("https://gletschervergleiche.ch/pages/ImageCompare.aspx?Id=6")
    imgs = links_of(html, "jpg|jpeg|png")
    print(f"  ImageCompare index {st}: {len(imgs)} image refs", flush=True)
    out["gletscher_index"] = {"status": st, "n_image_refs": len(imgs), "refs": imgs[:20]}
    out["gletscher_samples"] = []
    for img in imgs[:2]:
        url = img if img.startswith("http") else "https://gletschervergleiche.ch" + (img if img.startswith("/") else "/" + img)
        out["gletscher_samples"].append(evidence("gletschervergleiche image", url,
                                                 "gletscher-" + url.rsplit("/", 1)[-1].split("?")[0], cap=4_000_000))
    st2, html2 = get_text("https://gletschervergleiche.ch/PAGES/ImageCompareDet.aspx?Id=33")
    imgs2 = links_of(html2, "jpg|jpeg|png")
    print(f"  Rhone detail page {st2}: {len(imgs2)} image refs", flush=True)
    out["gletscher_rhone"] = {"status": st2, "n_image_refs": len(imgs2), "refs": imgs2[:12]}
    if imgs2:
        img = imgs2[0]
        url = img if img.startswith("http") else "https://gletschervergleiche.ch" + (img if img.startswith("/") else "/" + img)
        out["gletscher_rhone_sample"] = evidence("gletschervergleiche Rhone image", url,
                                                 "gletscher-rhone-" + url.rsplit("/", 1)[-1].split("?")[0], cap=4_000_000)

    print("\n== 1b. USGS repeat photography — one glacier page image sample ==", flush=True)
    st, html = get_text("https://www.usgs.gov/centers/norock/science/grinnell-glacier-north-moraine-1922-2008")
    imgs = [i for i in links_of(html, "jpg|jpeg|png") if "media" in i or "image" in i.lower()][:6]
    print(f"  USGS Grinnell page {st}: candidate images {len(imgs)}", flush=True)
    out["usgs"] = {"status": st, "candidates": imgs[:6]}
    if imgs:
        out["usgs_sample"] = evidence("USGS Grinnell repeat photo", imgs[0],
                                      "usgs-" + imgs[0].rsplit("/", 1)[-1].split("?")[0], cap=4_000_000)

    print("\n== 2a. storing.ingv.it EuroSeismos — station page preview images + CDX image count ==", flush=True)
    st, html = get_text("http://storing.ingv.it/es_web/Data/oss/PRA.html")
    imgs = links_of(html, "jpg|jpeg|gif|png|tif")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    print(f"  PRA page {st}: {len(imgs)} image refs, {len(hrefs)} hrefs", flush=True)
    out["ingv_pra"] = {"status": st, "image_refs": imgs[:15], "hrefs_sample": hrefs[:20]}
    out["ingv_samples"] = []
    for img in imgs[:2]:
        url = img if img.startswith("http") else "http://storing.ingv.it/es_web/Data/oss/" + img.lstrip("./")
        out["ingv_samples"].append(evidence("INGV EuroSeismos preview (PRA)", url,
                                            "ingv-" + url.rsplit("/", 1)[-1].split("?")[0], cap=4_000_000))
    rows = cdx("storing.ingv.it/*", limit=10000, extra={"filter": r"original:.*\.(jpg|jpeg|gif|tif|tiff|png)"})
    ok = [x for x in rows if x[2] == "200"]
    print(f"  storing.ingv.it image CDX: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
    out["ingv_cdx_images"] = {"collapsed": len(rows), "ok200": len(ok),
                              "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:25]]}
    if ok and not out["ingv_samples"]:
        ts, orig, sc, ln, mt = ok[0]
        out["ingv_wb_sample"] = evidence("INGV preview via Wayback", wb(ts, orig),
                                         "ingv-wb-" + orig.rsplit("/", 1)[-1], cap=4_000_000)

    print("\n== 2b. Mendeley Romanian seismograms — public API file list ==", flush=True)
    out["mendeley"] = {}
    try:
        r = requests.get("https://data.mendeley.com/public-api/datasets/gvxmng6644",
                         params={"version": 2}, headers=UA, timeout=60)
        out["mendeley"]["api_status"] = r.status_code
        files = r.json().get("files", []) if r.status_code == 200 else []
        out["mendeley"]["files"] = [{"name": f.get("filename"), "size": f.get("size"),
                                     "download_url": f.get("content_details", {}).get("download_url")} for f in files]
        print(f"  API {r.status_code}: {len(files)} files", flush=True)
        for f in out["mendeley"]["files"][:10]:
            print(f"    {f['size']} B  {f['name']}", flush=True)
        small = [f for f in out["mendeley"]["files"] if f["download_url"]]
        if small:
            pick = sorted(small, key=lambda f: f["size"] or 0)[0]
            out["mendeley_sample"] = evidence(f"Mendeley seismogram file ({pick['name']})",
                                              pick["download_url"], "mendeley-" + (pick["name"] or "file"), cap=6_000_000)
    except Exception as e:
        out["mendeley"]["error"] = str(e)[:160]
        print(f"  API failed: {e}", flush=True)

    print("\n== 3. Moonwatch — SIA finding aid PDF + IGY Satellite Report PDF ==", flush=True)
    out["moonwatch_finding_aid"] = evidence("SIA Moonwatch Division finding aid (RU 255)",
                                            "https://sirismm.si.edu/EADpdfs/SIA.FARU0255.pdf",
                                            "sia-moonwatch-ru255-finding-aid.pdf", cap=20_000_000)
    out["moonwatch_igy_report"] = evidence("IGY Satellite Report No.4 (Moonwatch Catalogue)",
                                           "https://noaadata.apps.nsidc.org/NOAA/G02201/IPY_Pub_017_20100728/DAHLI_IPY017_0387.pdf",
                                           "igy-satellite-report-4.pdf", cap=20_000_000)

    print("\n== 4a. Science Museum Group — indicator diagram object (API + page) ==", flush=True)
    out["smg"] = {}
    for u in ("https://collection.sciencemuseumgroup.org.uk/objects/co51466/indicator-diagram",
              "https://collection.sciencemuseumgroup.org.uk/objects/co84161"):
        st, html = get_text(u, cap=400_000)
        imgs = links_of(html, "jpg|jpeg|png")
        out["smg"][u] = {"status": st, "n_images": len(imgs), "refs": imgs[:5]}
        print(f"  SMG {u[-40:]}: {st}, {len(imgs)} images", flush=True)
    print("\n== 4b. Rolls-Royce archive — Box 52 scan images ==", flush=True)
    st, html = get_text("https://archive.rollsroyces.org/boxes/experimental/ExFiles_bck_Box_sp_52_bck_1/")
    imgs = links_of(html, "jpg|jpeg|png")
    print(f"  RR box page {st}: {len(imgs)} image refs", flush=True)
    out["rollsroyce"] = {"status": st, "image_refs": imgs[:10]}
    if imgs:
        img = imgs[0]
        url = img if img.startswith("http") else "https://archive.rollsroyces.org" + (img if img.startswith("/") else "/" + img)
        out["rollsroyce_sample"] = evidence("Rolls-Royce archive scan", url,
                                            "rr-" + url.rsplit("/", 1)[-1].split("?")[0], cap=4_000_000)

    print("\n== 5. Truempy catalog — item images ==", flush=True)
    st, html = get_text("https://truempy-druckmuster.ethz.ch/en")
    imgs = links_of(html, "jpg|jpeg|png")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    print(f"  Truempy home {st}: {len(imgs)} images, {len(hrefs)} hrefs", flush=True)
    out["truempy"] = {"status": st, "image_refs": imgs[:10],
                      "itemish_hrefs": [h for h in hrefs if re.search(r'volume|item|record|object|detail', h, re.I)][:12]}
    if imgs:
        img = imgs[0]
        url = img if img.startswith("http") else "https://truempy-druckmuster.ethz.ch" + (img if img.startswith("/") else "/" + img)
        out["truempy_sample"] = evidence("Truempy catalog image", url,
                                         "truempy-" + url.rsplit("/", 1)[-1].split("?")[0], cap=4_000_000)

    print("\n== 6. AIATSIS finding-aid PDFs (tape-shelf inventories) ==", flush=True)
    out["aiatsis"] = {}
    for key, u in (("hercus_l09", "https://aiatsis.gov.au/sites/default/files/catalogue_resources/hercus_l09_finding_aid.pdf"),
                   ("breen_g11", "https://aiatsis.gov.au/sites/default/files/catalogue_resources/breen_g11_finding_aid.pdf"),
                   ("oates_l02", "https://aiatsis.gov.au/sites/default/files/catalogue_resources/oates_l02_finding_aid.pdf")):
        out["aiatsis"][key] = evidence(f"AIATSIS finding aid {key}", u, f"aiatsis-{key}.pdf", cap=20_000_000)
    rows = cdx("aiatsis.gov.au/sites/default/files/catalogue_resources/*", limit=8000)
    ok = [x for x in rows if x[2] == "200" and x[1].lower().endswith(".pdf")]
    print(f"  AIATSIS catalogue_resources CDX: {len(rows)} collapsed, {len(ok)} status-200 PDFs", flush=True)
    out["aiatsis_cdx"] = {"collapsed": len(rows), "ok200_pdfs": len(ok),
                          "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:25]]}
    out["anla_xml"] = evidence("ANLA result.xml (interface check)",
                                "https://www.uaf.edu/anla/result.xml?searchId=&form.searchId;", cap=300_000)

    print("\n== 7. LAP (lap.uga.edu) — the dialect pile, counted + sampled ==", flush=True)
    out["lap"] = {}
    st, html = get_text("https://www.lap.uga.edu/Projects/")
    folders = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+/)["\']', html)))
    print(f"  Projects index {st}: {len(folders)} folder links", flush=True)
    out["lap"]["project_folders"] = folders
    st, html = get_text("https://www.lap.uga.edu/Projects/LAGS/Speakers/")
    spk = sorted(set(re.findall(r'href\s*=\s*["\'](LAGS\(INF[^"\']+\)/)["\']', html)))
    print(f"  LAGS Speakers index {st}: {len(spk)} informant folders", flush=True)
    out["lap"]["lags_speaker_folders"] = len(spk)
    out["lap"]["lags_sample_folder"] = spk[:3]
    base = "https://www.lap.uga.edu/Projects/LAGS/Speakers/LAGS(INF001)"
    out["lap"]["inf001_xlsx"] = evidence("LAGS INF001 informant spreadsheet",
                                         base + "/LAGS(INF001).xlsx", "lap-inf001.xlsx", cap=6_000_000)
    out["lap"]["inf001_xml"] = evidence("LAGS INF001 informant XML",
                                        base + "/LAGS(INF001).xml", "lap-inf001.xml", cap=6_000_000)
    mp3 = "https://www.lap.uga.edu/Projects/LAGS/Speakers/LAGS(INF001)/Audio/LAGS(INF001)1/LAGS(INF001)1%2001%20Wild%20Animals.mp3"
    out["lap"]["inf001_mp3"] = evidence("LAGS INF001 tape1 seg01 'Wild Animals' mp3 (cap 4MB)",
                                        mp3, cap=4_000_000)
    out["lap"]["inf001_meta"] = evidence("LAGS INF001 tape1 meta.txt",
                                         "https://www.lap.uga.edu/Projects/LAGS/Speakers/LAGS(INF001)/Audio/LAGS(INF001)1/LAGS(INF001)1meta.txt",
                                         "lap-inf001-tape1-meta.txt", cap=300_000)
    out["lap"]["dass_full_txt"] = evidence("DASS2019 full corpus txt (head, cap 2MB)",
                                           "https://www.lap.uga.edu/Projects/DASS2019/Full_Corpus/DASS_full.txt",
                                           cap=2_000_000)
    out["lap"]["sed_kindling_csv"] = evidence("LAP-hosted SED kindling full dataset csv",
                                              "https://www.lap.uga.edu/Projects/SED/SED_kindling_fulldataset.csv",
                                              "lap-sed-kindling-full.csv", cap=6_000_000)
    for pat, label in ((r"original:.*\.mp3", "mp3"), (r"original:.*\.xlsx", "xlsx")):
        rows = cdx("lap.uga.edu/Projects/*", limit=10000, extra={"filter": pat})
        ok = [x for x in rows if x[2] == "200"]
        print(f"  LAP Projects CDX {label}: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
        out["lap"][f"cdx_{label}"] = {"collapsed": len(rows), "ok200": len(ok),
                                      "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:20]]}

    print("\n== 8. Price currents — archive.org item files ==", flush=True)
    out["toronto_pdf"] = evidence("Toronto Trade Circular and Prices Current PDF (archive.org)",
                                  "https://archive.org/download/torontotradecirc00unse/torontotradecirc00unse.pdf",
                                  cap=20_000_000)
    out["toronto_djvu_txt"] = evidence("Toronto Prices Current djvu text (head)",
                                       "https://archive.org/download/torontotradecirc00unse/torontotradecirc00unse_djvu.txt",
                                       "toronto-prices-current-djvu.txt", cap=2_000_000)
    out["bna_pdf"] = evidence("British Packet 1845-10-04 text PDF (Prices Current inside, cap 6MB)",
                              "https://archive.org/download/BNA_S001219212_18451004N0998/BNA_S001219212_18451004N0998_text.pdf",
                              cap=6_000_000)

    print("\n== 9. Fire insurance — LAC ecopy sheet + UCalgary links ==", flush=True)
    out["lac"] = {}
    st, html = get_text("https://recherche-collection-search.bac-lac.gc.ca/eng/home/record?app=fonandcol&IdNumber=3821547", cap=1_200_000)
    imgs = links_of(html, "jpg|jpeg|png")
    eco = sorted(set(re.findall(r'[^"\']*ecopy[^"\']*', html, re.I)))[:8]
    print(f"  LAC Montreal record {st}: {len(imgs)} images, ecopy refs {len(eco)}", flush=True)
    out["lac"] = {"status": st, "image_refs": imgs[:10], "ecopy_refs": eco}
    cand = [i for i in imgs if re.search(r'ecopy|e0\d', i, re.I)] or imgs[:1]
    if cand:
        img = cand[0]
        url = img if img.startswith("http") else "https://recherche-collection-search.bac-lac.gc.ca" + (img if img.startswith("/") else "/" + img)
        out["lac_sample"] = evidence("LAC Goad sheet image", url,
                                     "lac-" + url.rsplit("/", 1)[-1].split("?")[0], cap=5_000_000)
    st, html = get_text("https://libguides.ucalgary.ca/c.php?g=740062&p=5339528", cap=800_000)
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    fip = [h for h in hrefs if re.search(r'digital|collection|fire|fip', h, re.I)][:15]
    print(f"  UCalgary libguide {st}: FIP-ish links {len(fip)}", flush=True)
    out["ucalgary"] = {"status": st, "fip_links": fip}

    print("\n== 10. Photo-finish — Weebly PDF + Substack finish frame ==", flush=True)
    out["weebly_pdf"] = evidence("Weebly 'Photo Finish' PDF",
                                 "https://licksmacenre.weebly.com/uploads/1/4/8/7/148708983/photo-finish.pdf",
                                 "weebly-photo-finish.pdf", cap=10_000_000)
    st, html = get_text("https://la32games.substack.com/p/the-first-olympic-photo-finish", cap=1_000_000)
    imgs = links_of(html, "jpg|jpeg|png")
    print(f"  LA32 Substack {st}: {len(imgs)} images", flush=True)
    out["la32"] = {"status": st, "image_refs": imgs[:8]}
    if imgs:
        out["la32_sample"] = evidence("LA32 1932 finish image", imgs[0],
                                      "la32-" + imgs[0].rsplit("/", 1)[-1].split("?")[0], cap=4_000_000)

    gh.save({"verify10": out}, "verify10")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
