#!/usr/bin/env python3
"""Verify9b — Campaign 9 completion + correction pass.
verify9.py hit its 280s timeout inside §7 (the nature.com PDF
fetch hung), so §§8-9 never ran and no JSON was saved. This pass:
(1) retries the Butler2013 raw file that returned EMPTY;
(2) re-samples a REAL diatoms.org species image (verify9's pick
was the favicon — corrected here, never counted);
(3) inspects the WSL static dendro tree structure directly
(verify9's species_list parse found only 3 hrefs);
(4) re-reads the BloodBook ABO page as text;
(5) HEAD-only for the Mourant Nature PDF (no body fetch);
(6) runs verify9's §§8-9 (Gordon, PSMSL) unchanged.
Samples to gold/campaign9-verify/. Run from goldmine-hunter/.
"""
import os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import head, evidence, UA

OUTDIR = "gold/campaign9-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=600_000, timeout=45):
    try:
        r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
        return r.status_code, r.url, r.text[:cap]
    except Exception as e:
        return None, url, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 2b. Butler2013 raw — retry both variants ==", flush=True)
    out["butler2013_raw_retry"] = evidence("Butler2013 raw measurements retry (NCEI)",
        "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/butler2013/butler2013-raw.txt",
        "butler2013-raw.txt", cap=5_000_000)
    out["butler2013_raw_noaa"] = evidence("Butler2013 raw measurements -noaa variant (NCEI)",
        "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/butler2013/butler2013-raw-noaa.txt",
        cap=5_000_000)

    print("\n== 5b. Diatoms — real species image (not favicon) ==", flush=True)
    st, furl, html = get_text("https://diatoms.org/species/49961/cymbella_hustedtii")
    imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png))["\']', html, re.I)))
    real = [i for i in imgs if "favicon" not in i.lower() and "icon" not in i.lower() and "logo" not in i.lower()]
    print(f"  species page {st}: {len(imgs)} image refs, {len(real)} non-furniture", flush=True)
    for i in real[:10]:
        print(f"    img: {i[:110]}", flush=True)
    out["diatoms_images"] = {"all": imgs[:20], "non_furniture": real[:10]}
    out["diatoms_sample"] = None
    for img in real[:1]:
        iurl = img if img.startswith("http") else "https://diatoms.org" + (img if img.startswith("/") else "/" + img)
        out["diatoms_sample"] = evidence("diatoms.org Cymbella hustedtii valve image", iurl,
                                          "diatoms-" + iurl.rsplit("/", 1)[-1].split("?")[0], cap=3_000_000)

    print("\n== 6b. WSL static dendro tree — structure ==", flush=True)
    for path in ("welcome.html", "species_list.html", "micro.html", "ident_key.html"):
        st, furl, html = get_text("https://static.wsl.ch/land/products/dendro/" + path)
        links = sorted(set(re.findall(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', html, re.I)))
        print(f"  {path}: {st}, {len(html)} B, {len(links)} refs; sample: {links[:6]}", flush=True)
        out.setdefault("wsl_tree", {})[path] = {"status": st, "bytes": len(html), "refs": links[:30]}
    # species pages pattern probe via CDX on the static tree
    from verify6 import cdx
    rows = cdx("static.wsl.ch/land/products/dendro/*", limit=8000)
    ok = [x for x in rows if x[2] == "200"]
    okimg = [x for x in ok if x[1].lower().split("?")[0].endswith((".jpg", ".jpeg", ".png", ".gif"))]
    okhtml = [x for x in ok if x[4] and "html" in x[4]]
    print(f"  static.wsl.ch dendro CDX: {len(rows)} collapsed, {len(ok)} status-200, {len(okhtml)} html, {len(okimg)} images", flush=True)
    out["wsl_cdx"] = {"collapsed": len(rows), "ok200": len(ok), "ok200_html": len(okhtml),
                       "ok200_images": len(okimg),
                       "sample_images": [{"ts": x[0], "url": x[1], "length": x[3]} for x in okimg[:10]]}
    if okimg:
        x = sorted(okimg, key=lambda r: int(r[3] or 0))
        mid = x[len(x)//2]
        out["wsl_image_sample_wb"] = evidence("WSL dendro image via Wayback",
            f"https://web.archive.org/web/{mid[0]}id_/{mid[1]}",
            "wsl-wb-" + mid[1].rsplit("/", 1)[-1], cap=3_000_000)

    print("\n== 7b. BloodBook — page as text + Mourant HEAD ==", flush=True)
    st, furl, html = get_text("https://www.bloodbook.com/world-abo-frequency.html", cap=1_500_000)
    txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))
    print(f"  BloodBook {st} final={furl[:70]}: {len(html)} B; text head: {txt[:300]!r}", flush=True)
    out["bloodbook"] = {"status": st, "final_url": furl, "bytes": len(html), "text_head": txt[:500],
                        "mentions_mourant": "mourant" in txt.lower(),
                        "mentions_populations": len(re.findall(r"population", txt, re.I))}
    out["mourant_head"] = head("https://www.nature.com/articles/hdy19522.pdf?origin=ppub")
    print(f"  Mourant Nature PDF HEAD: {out['mourant_head']}", flush=True)

    print("\n== 8. Pathology — Gordon page access/catalogue text ==", flush=True)
    st, furl, html = get_text("http://kcl.ac.uk/lsm/centre-for-education/museums/gordon-museum/the-collection")
    txt = re.sub(r"<[^>]+>", " ", html)
    spec = re.search(r"[^.]{0,100}8,000 pathological specimens[^.]{0,80}\.", txt)
    restr = re.search(r"[^.]{0,120}(only|restricted|not open|medical professionals)[^.]{0,120}\.", txt, re.I)
    print(f"  Gordon page {st}; specimens snippet: {bool(spec)}; restriction snippet: {bool(restr)}", flush=True)
    out["gordon"] = {"status": st, "specimens_snippet": (spec.group(0)[:260] if spec else None),
                     "restriction_snippet": (restr.group(0)[:260] if restr else None)}

    print("\n== 9. Tide — PSMSL catalogue + station-15 links + calibrations + Ireland paper ==", flush=True)
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

    gh.save({"verify9b": out}, "verify9b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
