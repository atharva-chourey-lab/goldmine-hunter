#!/usr/bin/env python3
"""Verify10b — Campaign 10 completion pass. Fixes verify10's
misses: INGV preview samples via Wayback (live preview host
unreachable from this client), AIATSIS finding aids via Wayback
(live host breaks this client's downloads), Truempy + Rolls-Royce
real content images (10's first picks were favicon/logo), Mendeley
API variants, LAC via its central redirect surface, DASS text
decode. Samples to gold/campaign10-verify/. Run from
goldmine-hunter/.
"""
import os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence

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

    print("\n== 1. INGV previews — what are storing's 378 CDX images? + Wayback preview sample ==", flush=True)
    rows = cdx("storing.ingv.it/*", limit=10000, extra={"filter": r"original:.*\.(jpg|jpeg|gif|tif|tiff|png)"})
    ok = [x for x in rows if x[2] == "200"]
    import collections
    dirs = collections.Counter("/" + "/".join(x[1].split("/")[3:-1]) for x in ok)
    print(f"  storing images ok200: {len(ok)}; top dirs: {dirs.most_common(6)}", flush=True)
    out["ingv_storing_img_dirs"] = dict(dirs.most_common(10))
    rows2 = cdx("sismos.rm.ingv.it/*", limit=10000, extra={"filter": r"original:.*\.jpg"})
    ok2 = [x for x in rows2 if x[2] == "200"]
    print(f"  sismos.rm.ingv.it jpg CDX: {len(rows2)} collapsed, {len(ok2)} status-200", flush=True)
    out["ingv_sismos_cdx"] = {"collapsed": len(rows2), "ok200": len(ok2),
                              "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok2[:20]]}
    pra = [x for x in ok2 if "PRA" in x[1]]
    pick = (pra or ok2)[:1]
    if pick:
        ts, orig, sc, ln, mt = pick[0]
        out["ingv_preview_wb_sample"] = evidence(f"INGV seismogram preview via Wayback ({orig.rsplit('/',1)[-1]})",
                                                 wb(ts, orig), "ingv-preview-" + orig.rsplit("/", 1)[-1], cap=5_000_000)

    print("\n== 2. AIATSIS finding aids via Wayback ==", flush=True)
    out["aiatsis_wb"] = {}
    rows = cdx("aiatsis.gov.au/sites/default/files/catalogue_resources/*", limit=8000)
    okp = [x for x in rows if x[2] == "200" and x[1].lower().endswith(".pdf")]
    for key in ("hercus_l09_finding_aid.pdf", "breen_g11_finding_aid.pdf"):
        cand = [x for x in okp if key in x[1].lower()]
        print(f"  {key}: {len(cand)} wb captures status-200", flush=True)
        if cand:
            ts, orig, sc, ln, mt = cand[0]
            out["aiatsis_wb"][key] = evidence(f"AIATSIS {key} via Wayback", wb(ts, orig),
                                              "aiatsis-" + key, cap=20_000_000)

    print("\n== 3. Mendeley API variants ==", flush=True)
    out["mendeley_variants"] = {}
    for u in ("https://data.mendeley.com/public-api/datasets/gvxmng6644",
              "https://data.mendeley.com/public-api/datasets/gvxmng6644/versions/2"):
        try:
            r = requests.get(u, headers=UA, timeout=60)
            files = []
            if r.status_code == 200:
                j = r.json()
                files = j.get("files", []) if isinstance(j, dict) else []
            out["mendeley_variants"][u] = {"status": r.status_code, "n_files": len(files),
                                           "names": [f.get("filename") for f in files[:12]]}
            print(f"  {u[-45:]}: {r.status_code}, {len(files)} files", flush=True)
            if files:
                pick = sorted(files, key=lambda f: f.get("size") or 0)[0]
                dl = pick.get("content_details", {}).get("download_url")
                if dl:
                    out["mendeley_sample"] = evidence(f"Mendeley file ({pick.get('filename')})", dl,
                                                      "mendeley-" + (pick.get("filename") or "file"), cap=6_000_000)
                break
        except Exception as e:
            out["mendeley_variants"][u] = {"error": str(e)[:140]}
            print(f"  {u[-45:]}: ERROR {e}", flush=True)

    print("\n== 4. Truempy — follow an item/volume link to a real page image ==", flush=True)
    st, html = get_text("https://truempy-druckmuster.ethz.ch/en")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    print(f"  home {st}: hrefs sample {[h for h in hrefs if 'en/' in h][:10]}", flush=True)
    out["truempy_hrefs"] = hrefs[:40]
    tried = 0
    for h in hrefs:
        if tried >= 3:
            break
        if re.search(r'band|volume|muster|sample|page', h, re.I) and not h.endswith((".css", ".js")):
            url = h if h.startswith("http") else "https://truempy-druckmuster.ethz.ch" + (h if h.startswith("/") else "/" + h)
            st2, page = get_text(url)
            imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png)(?:\?[^"\']*)?)["\']', page, re.I)))
            real = [i for i in imgs if not re.search(r'favicon|logo|icon', i, re.I)]
            print(f"  item page {url[:95]}: {st2}, {len(imgs)} imgs, {len(real)} non-icon", flush=True)
            out.setdefault("truempy_items", []).append({"url": url, "status": st2, "imgs": real[:6]})
            if real:
                img = real[0]
                iurl = img if img.startswith("http") else "https://truempy-druckmuster.ethz.ch" + (img if img.startswith("/") else "/" + img)
                out["truempy_item_sample"] = evidence("Truempy sample-book page image", iurl,
                                                      "truempy-page-" + iurl.rsplit("/", 1)[-1].split("?")[0], cap=5_000_000)
                break
            tried += 1

    print("\n== 5. Rolls-Royce — follow a record link to its scan ==", flush=True)
    st, html = get_text("https://archive.rollsroyces.org/boxes/experimental/ExFiles_bck_Box_sp_52_bck_1/")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    recs = [h for h in hrefs if re.search(r'record|scan|image|view', h, re.I)][:10]
    print(f"  box {st}: {len(hrefs)} hrefs, record-ish {recs[:5]}", flush=True)
    out["rr_hrefs"] = hrefs[:30]
    for h in recs[:3]:
        url = h if h.startswith("http") else "https://archive.rollsroyces.org" + (h if h.startswith("/") else "/" + h)
        st2, page = get_text(url)
        imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png)(?:\?[^"\']*)?)["\']', page, re.I)))
        real = [i for i in imgs if not re.search(r'logo|icon|RR-512', i, re.I)]
        print(f"  record {url[:95]}: {st2}, {len(real)} content imgs", flush=True)
        if real:
            img = real[0]
            iurl = img if img.startswith("http") else "https://archive.rollsroyces.org" + (img if img.startswith("/") else "/" + img)
            out["rr_scan_sample"] = evidence("Rolls-Royce archive record scan", iurl,
                                             "rr-scan-" + iurl.rsplit("/", 1)[-1].split("?")[0], cap=5_000_000)
            break

    print("\n== 6. LAC via central redirect (search-result URL) ==", flush=True)
    out["lac_central_head"] = head("http://central.bac-lac.gc.ca/.redirect?app=FonAndCol&id=3805542&lang=eng")
    print(f"  central redirect HEAD: {out['lac_central_head']}", flush=True)
    st, html = get_text("http://central.bac-lac.gc.ca/.redirect?app=FonAndCol&id=3805542&lang=eng", cap=1_000_000)
    imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png)(?:\?[^"\']*)?)["\']', html, re.I))) if isinstance(html, str) else []
    print(f"  central page {st}: {len(imgs)} images", flush=True)
    out["lac_central"] = {"status": st, "image_refs": imgs[:10]}
    if imgs:
        img = imgs[0]
        url = img if img.startswith("http") else "http://central.bac-lac.gc.ca" + (img if img.startswith("/") else "/" + img)
        out["lac_sample"] = evidence("LAC Goad sheet image (central)", url,
                                     "lac-" + url.rsplit("/", 1)[-1].split("?")[0], cap=5_000_000)

    print("\n== 7. DASS_full.txt decode check (first 200KB, latin-1 tolerant) ==", flush=True)
    try:
        r = requests.get("https://www.lap.uga.edu/Projects/DASS2019/Full_Corpus/DASS_full.txt",
                         headers=UA, timeout=60, stream=True)
        buf = next(r.iter_content(200_000))
        txt = buf.decode("utf-8", errors="ignore")
        out["dass_txt_head"] = {"status": r.status_code, "lines_in_200kb": txt.count("\n"),
                                "first_line": txt.split("\n")[0][:160]}
        print(f"  DASS txt {r.status_code}: {txt.count(chr(10))} lines in 200KB; first: {txt.split(chr(10))[0][:100]!r}", flush=True)
    except Exception as e:
        out["dass_txt_head"] = {"error": str(e)[:140]}

    gh.save({"verify10b": out}, "verify10b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
