#!/usr/bin/env python3
"""Verify15 — Campaign 15 (Broad Wave 3A) targeted verification.
Standing method (= verify6/10): targeted CDX prefix queries
filtered to statuscode:200, direct sample downloads of every
concrete pile (size + md5 + magic), custody checks documented
and never circumvented. Samples to gold/campaign15-verify/.
Run from goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence

OUTDIR = "gold/campaign15-verify"
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

def zenodo_files(record_id):
    try:
        r = requests.get(f"https://zenodo.org/api/records/{record_id}", headers=UA, timeout=60)
        if r.status_code != 200:
            return {"api_status": r.status_code, "files": []}
        d = r.json()
        return {"api_status": 200, "title": d.get("metadata", {}).get("title", "")[:120],
                "files": [{"name": f["key"], "size": f.get("size"),
                           "link": f.get("links", {}).get("self")} for f in d.get("files", [])]}
    except Exception as e:
        return {"api_status": None, "error": str(e)[:160], "files": []}

def main():
    out = {}

    print("\n== 1a. Avisoft batcalls — page wav links, batcalls.zip, CDX wav count ==", flush=True)
    st, html = get_text("http://www.avisoft.com/batcalls/")
    wavs = links_of(html, "wav|zip|flac")
    print(f"  avisoft batcalls page {st}: {len(wavs)} wav/zip refs", flush=True)
    out["avisoft"] = {"status": st, "refs": wavs[:30]}
    out["avisoft_zip"] = evidence("Avisoft batcalls.zip (playback pile, cap 6MB)",
                                   "https://www.avisoft.com/batcalls/europe/playback/batcalls.zip",
                                   "avisoft-batcalls.zip", cap=6_000_000)
    for w in wavs[:2]:
        url = w if w.startswith("http") else "http://www.avisoft.com" + (w if w.startswith("/") else "/batcalls/" + w)
        out.setdefault("avisoft_wav_samples", []).append(
            evidence("Avisoft wav sample", url, "avisoft-" + url.rsplit("/", 1)[-1].split("?")[0], cap=3_000_000))
    rows = cdx("avisoft.com/batcalls/*", limit=8000, extra={"filter": r"original:.*\.(wav|zip)"})
    ok = [x for x in rows if x[2] == "200"]
    print(f"  avisoft/batcalls CDX wav+zip: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
    out["avisoft_cdx"] = {"collapsed": len(rows), "ok200": len(ok),
                           "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:25]]}

    print("\n== 1b. Animal Sound Labs bat calls — wav/flac sample ==", flush=True)
    st, html = get_text("https://animalsoundlabs.pl/en/bat-calls/")
    wavs = links_of(html, "wav|flac|mp3")
    print(f"  animalsoundlabs page {st}: {len(wavs)} audio refs", flush=True)
    out["asl"] = {"status": st, "refs": wavs[:20]}
    if wavs:
        w = wavs[0]
        url = w if w.startswith("http") else "https://animalsoundlabs.pl" + (w if w.startswith("/") else "/" + w)
        out["asl_sample"] = evidence("Animal Sound Labs audio sample", url,
                                     "asl-" + url.rsplit("/", 1)[-1].split("?")[0], cap=3_000_000)

    print("\n== 1c. Morcegoteca — species/download links on Bat Library page ==", flush=True)
    st, html = get_text("https://ppbio.inpa.gov.br/en/Bat_Library")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    dl = [h for h in hrefs if re.search(r'\.(wav|zip|rar)$|download|ferramenta|tool', h, re.I)][:20]
    print(f"  Morcegoteca page {st}: {len(hrefs)} hrefs, download-ish {len(dl)}", flush=True)
    out["morcegoteca"] = {"status": st, "downloadish": dl, "hrefs_sample": hrefs[:25]}
    for h in dl[:2]:
        url = h if h.startswith("http") else "https://ppbio.inpa.gov.br" + (h if h.startswith("/") else "/" + h)
        out.setdefault("morcegoteca_samples", []).append(
            evidence("Morcegoteca download sample", url,
                     "morcegoteca-" + url.rsplit("/", 1)[-1].split("?")[0][:60], cap=4_000_000))

    print("\n== 1d. ChiroVox — browse page audio-link check (platform interface) ==", flush=True)
    st, html = get_text("https://www.chirovox.org/")
    wavs = links_of(html, "wav|zc|mp3")
    print(f"  chirovox home {st}: {len(wavs)} direct audio refs (interface expected: 0)", flush=True)
    out["chirovox"] = {"status": st, "direct_audio_refs": wavs[:10]}

    print("\n== 2a. BioCosmos Zenodo — file list + smallest file sample ==", flush=True)
    z = zenodo_files(23840624)
    out["biocosmos"] = z
    print(f"  BioCosmos API {z.get('api_status')}: {len(z['files'])} files", flush=True)
    for f in z["files"][:8]:
        print(f"    {f['size']} B  {f['name']}", flush=True)
    small = [f for f in z["files"] if f["link"]]
    if small:
        pick = sorted(small, key=lambda f: f["size"] or 0)[0]
        out["biocosmos_sample"] = evidence(f"BioCosmos smallest file ({pick['name']})",
                                           pick["link"], "biocosmos-" + pick["name"].replace("/", "_")[:60],
                                           cap=4_000_000)

    print("\n== 2b. BAMONA gallery — one gallery image sample (field photo check) ==", flush=True)
    st, html = get_text("https://www.butterfliesandmoths.org/gallery?species_type=0&stage=adult&page=58")
    imgs = links_of(html, "jpg|jpeg|png")
    print(f"  BAMONA gallery {st}: {len(imgs)} image refs", flush=True)
    out["bamona"] = {"status": st, "refs": imgs[:10]}
    if imgs:
        img = imgs[0]
        url = img if img.startswith("http") else "https://www.butterfliesandmoths.org" + (img if img.startswith("/") else "/" + img)
        out["bamona_sample"] = evidence("BAMONA gallery image", url,
                                        "bamona-" + url.rsplit("/", 1)[-1].split("?")[0], cap=3_000_000)

    print("\n== 3. Venom Zenodo deposits — file lists + smallest samples ==", flush=True)
    out["venom"] = {}
    for rid, tag in ((16418915, "berus"), (11103867, "monticola"), (11482457, "ammodytes")):
        z = zenodo_files(rid)
        out["venom"][tag] = z
        print(f"  Zenodo {rid} ({tag}) API {z.get('api_status')}: {len(z['files'])} files, "
              f"total {sum(f['size'] or 0 for f in z['files']):,} B", flush=True)
        small = [f for f in z["files"] if f["link"]]
        if small:
            pick = sorted(small, key=lambda f: f["size"] or 0)[0]
            out["venom"][tag + "_sample"] = evidence(f"Venom {tag} smallest file ({pick['name']})",
                                                     pick["link"],
                                                     f"venom-{tag}-" + pick["name"].replace("/", "_")[:50],
                                                     cap=3_000_000)
    out["pride_head"] = head("https://www.ebi.ac.uk/pride/archive/projects/PXD016503")
    print(f"  PRIDE PXD016503 live-status: {out['pride_head']}", flush=True)

    print("\n== 4a. Historic England dendro report PDF sample ==", flush=True)
    st, html = get_text("https://historicengland.org.uk/research/results/reports/96-2022")
    pdfs = links_of(html, "pdf")
    print(f"  HE report page {st}: {len(pdfs)} PDF refs", flush=True)
    out["historic_england"] = {"status": st, "pdf_refs": pdfs[:8]}
    if pdfs:
        p = pdfs[0]
        url = p if p.startswith("http") else "https://historicengland.org.uk" + (p if p.startswith("/") else "/" + p)
        out["he_sample"] = evidence("Historic England dendro report PDF", url,
                                    "he-dendro-" + url.rsplit("/", 1)[-1].split("?")[0], cap=6_000_000)
    print("\n== 4b. ADS VAG dendro — any .rwl/.txt data links on record pages? ==", flush=True)
    for rid in ("923", "1100"):
        st, html = get_text(f"https://archaeologydataservice.ac.uk/archives/view/vag_dendro/full_record.cfm?id={rid}")
        dat = links_of(html, "rwl|txt|csv|zip|xls|xlsx")
        print(f"  ADS record {rid} {st}: {len(dat)} data-file refs", flush=True)
        out.setdefault("ads", {})[rid] = {"status": st, "data_refs": dat[:10]}
    rows = cdx("archaeologydataservice.ac.uk/archives/view/vag_dendro/*", limit=3000,
               extra={"filter": r"original:.*\.(rwl|txt|csv|zip)"})
    ok = [x for x in rows if x[2] == "200"]
    print(f"  ADS vag_dendro CDX data-filter: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
    out["ads_cdx"] = {"collapsed": len(rows), "ok200": len(ok)}

    print("\n== 5a. phage.org — Table 2-5 host-range PDF + CDX data count ==", flush=True)
    out["phage_table_pdf"] = evidence("Bacteriophages Table 2-5 host range PDF (phage.org)",
                                      "http://www.phage.org/images/thebacteriophages/0020_table_005.pdf",
                                      "phage-table2-5-hostrange.pdf", cap=10_000_000)
    rows = cdx("phage.org/*", limit=8000)
    ok = [x for x in rows if x[2] == "200" and gh.is_data(x[1]) and " " not in x[1]]
    print(f"  phage.org CDX: {len(rows)} collapsed, {len(ok)} status-200 data files", flush=True)
    out["phage_cdx"] = {"collapsed": len(rows), "ok200_data": len(ok),
                        "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:25]]}
    print("\n== 5b. d'Herelle catalogue — interface check (file links?) ==", flush=True)
    st, html = get_text("https://www.phage.ulaval.ca/en/rechercher-catalogue-phages")
    dat = links_of(html, "csv|xls|xlsx|zip|pdf")
    print(f"  ulaval catalogue {st}: {len(dat)} downloadable-file refs", flush=True)
    out["ulaval"] = {"status": st, "file_refs": dat[:10]}

    print("\n== 6. AAOF Legacy — interface check (direct image/file links?) ==", flush=True)
    st, html = get_text("https://www.aaoflegacycollection.org/aaof_home.html")
    dat = links_of(html, "jpg|jpeg|zip|csv|dcm")
    print(f"  AAOF home {st}: {len(dat)} direct data/image refs", flush=True)
    out["aaof"] = {"status": st, "refs": dat[:10]}

    print("\n== 7a. VizieR VI/132C — CDS catalogue file sample (formal archive data) ==", flush=True)
    st, html = get_text("https://cdsarc.cds.unistra.fr/viz-bin/cat/VI/132C")
    ftps = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']*(?:ftp|VI/132)[^"\']*)["\']', html, re.I)))[:15]
    print(f"  CDS VI/132C page {st}: ftp-ish refs {len(ftps)}", flush=True)
    out["vizier132"] = {"status": st, "refs": ftps}
    out["vizier132_readme"] = evidence("VizieR VI/132C ReadMe (head)",
                                       "https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/VI/132C?format=txt",
                                       "vizier-vi132c-readme.txt", cap=500_000)
    print("\n== 7b. lunar-occultations.com — CDX data files on the section site ==", flush=True)
    rows = cdx("lunar-occultations.com/*", limit=8000)
    ok = [x for x in rows if x[2] == "200" and gh.is_data(x[1]) and " " not in x[1]]
    print(f"  lunar-occultations.com CDX: {len(rows)} collapsed, {len(ok)} status-200 data files", flush=True)
    out["lunar_cdx"] = {"collapsed": len(rows), "ok200_data": len(ok),
                        "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:25]]}
    if ok:
        ts, orig, sc, ln, mt = sorted(ok, key=lambda x: int(x[3] or 0))[0]
        out["lunar_sample"] = evidence(f"lunar-occultations smallest wb ({ln} B CDX)", wb(ts, orig),
                                       "lunar-" + orig.rsplit("/", 1)[-1][:60], cap=3_000_000)
    out["rasc_pdf"] = evidence("IOTA RASC 2026 lunar PDF (predictions, not timings)",
                               "https://occultations.org/publications/rasc/2026/lunar26.pdf",
                               "iota-rasc2026-lunar.pdf", cap=6_000_000)

    print("\n== 8a. APPLAUSE — DR3 page counts + WFPDB ReadMe sample ==", flush=True)
    out["wfpdb_readme"] = evidence("WFPDB VI/90 ReadMe (head)",
                                   "https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/VI/90?format=txt",
                                   "wfpdb-vi90-readme.txt", cap=500_000)
    st, html = get_text("https://www.plate-archive.org/cms/documentation/dr3/")
    print(f"  plate-archive DR3 docs {st}: {len(html):,} chars fetched", flush=True)
    out["applause_dr3"] = {"status": st,
                           "mentions": {k: html.count(k) for k in ("70276", "70,276", "logbook", "plate")}}
    print("\n== 8b. skyarchive.org (WFPDB home) — live status ==", flush=True)
    out["skyarchive_head"] = head("http://www.skyarchive.org/")
    print(f"  skyarchive.org live-status: {out['skyarchive_head']}", flush=True)

    print("\n== 9. Radio charts — Manchester logbooks page + narrative PDFs ==", flush=True)
    st, html = get_text("https://www.library.manchester.ac.uk/services/digitisation-services/projects/jodrell-bank-logbooks/")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    coll = [h for h in hrefs if re.search(r'digital|collection|logbook', h, re.I)][:12]
    print(f"  Manchester Jodrell logbooks page {st}: collection-ish links {len(coll)}", flush=True)
    out["manchester"] = {"status": st, "collection_links": coll}
    out["bigear_pdf"] = evidence("Cosmic Search 13 — Reber first radio maps (bigear.org)",
                                 "https://www.bigear.org/CSMO/PDF/CS13/cs13p14.pdf",
                                 "bigear-cs13-reber.pdf", cap=6_000_000)
    out["bell_pdf"] = evidence("Bell Burnell Cosmic Search — pen-chart pulsar account",
                               "https://magonia.com/wp-content/uploads/2016/10/cosmic-search-jocelyn-bell.pdf",
                               "bell-cosmic-search.pdf", cap=6_000_000)

    gh.save({"verify15": out}, "verify15")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
