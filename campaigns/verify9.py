#!/usr/bin/env python3
"""Verify9 — Campaign 9 (Broad Wave 2A) targeted verification.
Standing method (= verify6/8): targeted CDX prefix queries
filtered to statuscode:200, direct sample downloads of every
concrete pile (size + md5 + magic), custody checks documented
and never circumvented. Samples to gold/campaign9-verify/.
Run from goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, evidence, UA

OUTDIR = "gold/campaign9-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=600_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.url, r.text[:cap]
    except Exception as e:
        return None, url, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 1. Cephalopod beaks — BAS guide PDF (NORA) + LABCOP collection paper ==", flush=True)
    out["bas_guide_pdf"] = evidence("Xavier & Cherel Cephalopod Beak Guide 2021 (NORA PDF, cap 5MB)",
        "http://nora.nerc.ac.uk/id/eprint/529835/15/CephalopodBeakGuide_5march2021.pdf",
        cap=5_000_000)
    out["labcop_paper"] = evidence("LABCOP beak collection paper PDF (562 beaks, 50 taxa)",
        "https://periodicos.univali.br/index.php/bjast/article/download/17226/11015",
        "labcop-beaks-2022.pdf", cap=10_000_000)

    print("\n== 2. Bivalve — NCEI Butler raw/chron samples (formal paleo archive) ==", flush=True)
    out["butler2013_raw"] = evidence("Butler2013 raw increment measurements (NCEI)",
        "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/butler2013/butler2013-raw.txt",
        "butler2013-raw.txt", cap=5_000_000)
    out["butler2013_stats_ne"] = evidence("Butler2013 NE chronology statistics (NCEI)",
        "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/butler2013/butler2013-stats-ne.txt",
        cap=2_000_000)
    out["butler2009_deltaR"] = evidence("Butler2009 delta-R file (NCEI)",
        "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/butler2009/butler2009-deltaR.txt",
        cap=2_000_000)
    rows = cdx("sclerochronology.org/*", limit=4000)
    ok = [x for x in rows if x[2] == "200" and gh.is_data(x[1])]
    print(f"  sclerochronology.org CDX: {len(rows)} collapsed, {len(ok)} status-200 data files", flush=True)
    out["sclero_cdx"] = {"collapsed": len(rows), "ok200_data": len(ok)}

    print("\n== 3. Bird eggs — MVZ/Nosachenko GBIF surfaces + WFVZ/Denny custody text ==", flush=True)
    st, furl, html = get_text("https://ukraine.ipt.gbif.no/resource?r=nosachenko_bird_breeding_records")
    arch = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']*archive\.do[^"\']*)["\']', html, re.I)))
    print(f"  Nosachenko IPT resource {st}: archive links {arch[:3]}", flush=True)
    out["nosachenko"] = {"status": st, "archive_links": arch[:3]}
    if arch:
        u = arch[0] if arch[0].startswith("http") else "https://ukraine.ipt.gbif.no/" + arch[0].lstrip("/")
        out["nosachenko_head"] = head(u)
        print(f"  Nosachenko DwC-A HEAD: {out['nosachenko_head']}", flush=True)
    st, furl, html = get_text("https://wfvz.org/collections/")
    m = re.search(r"[^.]{0,140}(Staff of the WFVZ provide data|contact us)[^.]{0,140}\.", re.sub(r"<[^>]+>", " ", html), re.I)
    print(f"  WFVZ collections {st} (final {furl[:60]}); by-request snippet: {bool(m)}", flush=True)
    out["wfvz"] = {"status": st, "final_url": furl, "by_request_snippet": (m.group(0)[:280] if m else None)}
    st, furl, html = get_text("https://sites.google.com/sheffield.ac.uk/admuseum/collections/eggs")
    m2 = re.search(r"[^.]{0,120}databased[^.]{0,120}\.", re.sub(r"<[^>]+>", " ", html), re.I)
    print(f"  Denny eggs page {st}; 'databased' snippet: {bool(m2)}", flush=True)
    out["denny"] = {"status": st, "databased_snippet": (m2.group(0)[:260] if m2 else None)}

    print("\n== 4. Seed bank — Comper blog evidence.json + page data-source links ==", flush=True)
    out["comper_evidence_json"] = evidence("Comper seed-vault page evidence.json",
        "https://mariuscomper.uk/how-long-do-seeds-last-seed-vault/assets/evidence.json",
        "comper-evidence.json", cap=2_000_000)
    st, furl, html = get_text("https://mariuscomper.uk/how-long-do-seeds-last-seed-vault/")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    dataish = [h for h in hrefs if re.search(r'data|supplement|doi|csiro|cambridge|figshare|zenodo', h, re.I)]
    print(f"  Comper page {st}: {len(hrefs)} hrefs, data-source-ish: {dataish[:8]}", flush=True)
    out["comper_page"] = {"status": st, "data_source_links": dataish[:8]}

    print("\n== 5. Diatom — diatoms.org species image sample + legacy ANSP CDX ==", flush=True)
    st, furl, html = get_text("https://diatoms.org/species/49961/cymbella_hustedtii")
    imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png))["\']', html, re.I)))
    print(f"  Cymbella hustedtii page {st}: {len(imgs)} image refs", flush=True)
    out["diatoms_species"] = {"status": st, "n_images": len(imgs), "images": imgs[:8]}
    out["diatoms_sample"] = None
    for img in imgs[:1]:
        iurl = img if img.startswith("http") else "https://diatoms.org" + (img if img.startswith("/") else "/" + img)
        out["diatoms_sample"] = evidence("diatoms.org species image", iurl,
                                          "diatoms-" + iurl.rsplit("/", 1)[-1].split("?")[0], cap=3_000_000)
    rows = cdx("diatom.ansp.org/*", limit=8000)
    okd = [x for x in rows if x[2] == "200"]
    okdata = [x for x in okd if gh.is_data(x[1])]
    print(f"  diatom.ansp.org CDX: {len(rows)} collapsed, {len(okd)} status-200 all, {len(okdata)} status-200 data", flush=True)
    out["ansp_legacy_cdx"] = {"collapsed": len(rows), "ok200_all": len(okd), "ok200_data": len(okdata),
                              "data_files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in okdata[:20]]}

    print("\n== 6. Wood — WSL static dendro tree (woodanatomy.ch successor) + InsideWood sheet ==", flush=True)
    st, furl, html = get_text("https://static.wsl.ch/land/products/dendro/species_list.html")
    links = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    sp_links = [h for h in links if h.lower().endswith((".html", ".htm")) and "species_list" not in h.lower()]
    print(f"  WSL dendro species_list {st}: {len(links)} hrefs, {len(sp_links)} species-page links", flush=True)
    out["wsl_dendro"] = {"status": st, "n_species_links": len(sp_links), "species_links": sp_links[:40]}
    out["wsl_species_sample"] = None
    if sp_links:
        base = "https://static.wsl.ch/land/products/dendro/"
        surl = sp_links[0] if sp_links[0].startswith("http") else base + sp_links[0].lstrip("./")
        st2, furl2, page = get_text(surl)
        simgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png|gif))["\']', page, re.I)))
        print(f"  species page {sp_links[0]}: {st2}, {len(simgs)} image refs", flush=True)
        out["wsl_species_page"] = {"url": surl, "status": st2, "n_images": len(simgs), "images": simgs[:10]}
        for img in simgs[:1]:
            iurl = img if img.startswith("http") else surl.rsplit("/", 1)[0] + "/" + img
            out["wsl_species_sample"] = evidence("WSL dendro species image", iurl,
                                                 "wsl-" + iurl.rsplit("/", 1)[-1], cap=3_000_000)
    out["insidewood_xlsx"] = evidence("InsideWood ModernWoodDataSheet.xlsx",
        "https://insidewood.lib.ncsu.edu/extras/insidewood/ModernWoodDataSheet.xlsx",
        "insidewood-ModernWoodDataSheet.xlsx", cap=5_000_000)

    print("\n== 7. Blood groups — BloodBook ABO page analysis + Mourant Nature PDF ==", flush=True)
    st, furl, html = get_text("http://www.bloodbook.com/world-abo-frequency.html", cap=1_500_000)
    txt = re.sub(r"<[^>]+>", " ", html)
    rows_n = html.lower().count("<tr")
    pops = len(re.findall(r"(19|20)\d\d", txt))
    print(f"  BloodBook ABO page {st} final={furl[:70]}: {len(html)} B, ~{rows_n} table rows", flush=True)
    out["bloodbook"] = {"status": st, "final_url": furl, "bytes": len(html), "table_rows": rows_n,
                        "sample_text": re.sub(r"\s+", " ", txt)[:400]}
    out["mourant_pdf"] = evidence("Mourant & Watkin 1948 Nature paper PDF (cap 3MB)",
        "https://www.nature.com/articles/hdy19522.pdf?origin=ppub", cap=3_000_000)

    print("\n== 8. Pathology — Gordon page access/catalogue text ==", flush=True)
    st, furl, html = get_text("http://kcl.ac.uk/lsm/centre-for-education/museums/gordon-museum/the-collection")
    txt = re.sub(r"<[^>]+>", " ", html)
    spec = re.search(r"[^.]{0,100}8,000 pathological specimens[^.]{0,80}\.", txt)
    restr = re.search(r"[^.]{0,120}(only|restricted|not open|medical professionals)[^.]{0,120}\.", txt, re.I)
    print(f"  Gordon page {st}; specimens snippet: {bool(spec)}; restriction snippet: {bool(restr)}", flush=True)
    out["gordon"] = {"status": st, "specimens_snippet": (spec.group(0)[:260] if spec else None),
                     "restriction_snippet": (restr.group(0)[:260] if restr else None)}

    print("\n== 9. Tide — PSMSL catalogue + station-15 data link + Ireland marigram paper ==", flush=True)
    out["psmsl_catalogue"] = evidence("PSMSL catalogue.dat (cap 3MB)",
        "https://psmsl.org/data/obtaining/catalogue.dat", cap=3_000_000)
    st, furl, html = get_text("https://psmsl.org/data/obtaining/stations/15.php")
    dlinks = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']*(?:\.dat|\.rlrdata|data)[^"\']*)["\']', html, re.I)))
    print(f"  PSMSL station15 {st}: data-ish links {dlinks[:8]}", flush=True)
    out["psmsl_station15"] = {"status": st, "data_links": dlinks[:10]}
    out["aden_calib"] = evidence("PSMSL Aden calibrations xls",
        "https://psmsl.org/data/calibrations/aden/aden_calibrations.xls",
        "psmsl-aden_calibrations.xls", cap=3_000_000)
    out["ireland_marigram_paper"] = evidence("McLoughlin et al. Ireland sea-level preprint PDF (cap 3MB)",
        "https://egusphere.copernicus.org/preprints/2026/egusphere-2025-6404/egusphere-2025-6404.pdf",
        cap=3_000_000)

    gh.save({"verify9": out}, "verify9")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
