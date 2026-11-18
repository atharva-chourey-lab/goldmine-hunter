#!/usr/bin/env python3
"""Verify10c — Campaign 10 final small pass: INGV seismogram
thumbnail via Wayback, Mendeley file sizes, ETH e-heritage content
image (Truempy catalog evidence), UCalgary FIP asset image attempt,
LAP/gletschervergleiche counts for the shortlist. Samples to
gold/campaign10-verify/. Run from goldmine-hunter/.
"""
import os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, UA, evidence

OUTDIR = "gold/campaign10-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=900_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 1. INGV seismogram thumbnail via Wayback ==", flush=True)
    rows = cdx("sismos.rm.ingv.it/images/regridart/*", limit=2000)
    ok = [x for x in rows if x[2] == "200" and "DBN" in x[1]]
    print(f"  regridart DBN rows ok200: {len(ok)}", flush=True)
    out["ingv_dbn_rows"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:5]]
    if ok:
        ts, orig, sc, ln, mt = ok[0]
        out["ingv_dbn_sample"] = evidence("INGV seismogram crop DBN_E_1908122708361A (via Wayback)",
                                          wb(ts, orig), "ingv-dbn-seismogram-crop.jpg", cap=3_000_000)

    print("\n== 2. Mendeley file sizes ==", flush=True)
    try:
        r = requests.get("https://data.mendeley.com/public-api/datasets/gvxmng6644", headers=UA, timeout=60)
        files = r.json().get("files", [])
        out["mendeley_files"] = [{"name": f.get("filename"), "size": f.get("size")} for f in files]
        print(f"  files: {out['mendeley_files']}", flush=True)
    except Exception as e:
        out["mendeley_files"] = {"error": str(e)[:140]}

    print("\n== 3. ETH e-heritage Truempy content image ==", flush=True)
    st, html = get_text("https://etheritage.ethz.ch/2024/11/15/chemische-farbenpracht-a-j-truempys-stoffmuster-als-onlinekatalog/?lang=en", cap=1_200_000)
    imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png)(?:\?[^"\']*)?)["\']', html, re.I)))
    real = [i for i in imgs if not re.search(r'logo|icon|favicon|avatar', i, re.I)]
    print(f"  e-heritage {st}: {len(imgs)} imgs, {len(real)} content", flush=True)
    out["etheritage"] = {"status": st, "content_imgs": real[:8]}
    if real:
        out["etheritage_sample"] = evidence("ETH e-heritage Truempy sample-book image", real[0],
                                            "truempy-etheritage-" + real[0].rsplit("/", 1)[-1].split("?")[0], cap=5_000_000)

    print("\n== 4. UCalgary FIP asset page — image attempt ==", flush=True)
    st, html = get_text("https://digitalcollections.ucalgary.ca/asset-management/2R3BF1R1NHI4M", cap=1_200_000)
    imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png)(?:\?[^"\']*)?)["\']', html, re.I))) if isinstance(html, str) else []
    print(f"  asset page {st}: {len(imgs)} image refs", flush=True)
    out["ucalgary_asset"] = {"status": st, "image_refs": imgs[:10]}
    real = [i for i in imgs if not re.search(r'logo|icon|favicon|sprite', i, re.I)]
    if real:
        img = real[0]
        url = img if img.startswith("http") else "https://digitalcollections.ucalgary.ca" + (img if img.startswith("/") else "/" + img)
        out["ucalgary_sample"] = evidence("UCalgary digital collections image", url,
                                          "ucalgary-" + url.rsplit("/", 1)[-1].split("?")[0], cap=5_000_000)

    print("\n== 5. Counts for the shortlist ==", flush=True)
    st, html = get_text("https://www.lap.uga.edu/Projects/DASS2019/Speakers/")
    spk = sorted(set(re.findall(r'href\s*=\s*["\'](\d+/)["\']', html)))
    print(f"  DASS2019 speaker folders: {len(spk)}", flush=True)
    out["dass2019_speakers"] = len(spk)
    st, html = get_text("https://www.lap.uga.edu/Projects/LAMSAS/Speakers/")
    spk2 = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+/)["\']', html)))
    print(f"  LAMSAS Speakers index {st}: {len(spk2)} links", flush=True)
    out["lamsas_speakers_links"] = len(spk2)
    st, html = get_text("https://gletschervergleiche.ch/sitemap.xml", cap=2_000_000)
    det = len(re.findall(r'ImageCompareDet', html)) if isinstance(html, str) else 0
    print(f"  gletschervergleiche sitemap {st}: ImageCompareDet refs {det}", flush=True)
    out["gletscher_sitemap_det_refs"] = det

    gh.save({"verify10c": out}, "verify10c")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
