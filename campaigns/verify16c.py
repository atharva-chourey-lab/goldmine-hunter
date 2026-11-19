#!/usr/bin/env python3
"""Verify16c — Campaign 16 sunspot-drawings close-out.
The howard.astro.ucla.edu FTP drawing tree's Wayback captures
carry statuscode 226 (FTP transfer-complete), so the standing
statuscode:200 filter hid them in verify16; KSO CESAR drawing
files are images, not gh.is_data extensions. Sample both here,
with the 226-status fact recorded, not silently re-filtered.
Samples to gold/campaign16-verify/. Run from goldmine-hunter/.
"""
import collections, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import wb, UA, evidence

OUTDIR = "gold/campaign16-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=900_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def cdx_raw(prefix, limit=10000, extra=None):
    params = {"url": prefix, "output": "json", "fl": "timestamp,original,statuscode,length,mimetype",
              "collapse": "urlkey", "limit": limit}
    if extra:
        params.update(extra)
    try:
        r = requests.get("http://web.archive.org/cdx/search/cdx", params=params, headers=UA, timeout=120)
        r.raise_for_status()
        rows = r.json()
        return rows[1:] if len(rows) > 1 else []
    except Exception as e:
        print(f"  CDX raw failed {prefix}: {e}", flush=True)
        return []

def main():
    out = {}

    print("\n== 9c-i. howard FTP drawing tree — count + sample (status 226 captures) ==", flush=True)
    rows = cdx_raw("howard.astro.ucla.edu/pub/obs/drawings/*", limit=10000)
    statuses = collections.Counter(x[2] for x in rows)
    years = collections.Counter()
    for x in rows:
        m = re.search(r"/drawings/(\d{4})/", x[1])
        if m:
            years[m.group(1)] += 1
    print(f"  howard tree: {len(rows)} collapsed rows (cap 10000), statuses {dict(statuses)}, years {dict(sorted(years.items())[:8])}...", flush=True)
    out["howard_tree"] = {"collapsed_cap10000": len(rows), "statuses": dict(statuses),
                          "per_year_sample": dict(sorted(years.items())[:40]),
                          "sample_rows": [list(x) for x in rows[:10]]}
    cand = [x for x in rows if re.search(r"\.(gif|jpg|jpeg|png)$", x[1], re.I)] or rows[:1]
    if cand:
        ts, orig, sc, ln, mt = cand[0]
        out["howard_sample"] = evidence("MWO sunspot drawing via Wayback (howard FTP tree, status-226 capture)",
                                        wb(ts, orig), "mwo-drawing-" + orig.rsplit("/", 1)[-1], cap=4_000_000)

    print("\n== 9c-ii. KSO CESAR — one year directory + one drawing image ==", flush=True)
    rows = cdx_raw("cesar.kso.ac.at/sunspot_drawings/*", limit=3000)
    ok = [x for x in rows if x[2] == "200"]
    out["kso_cdx_detail"] = {"n": len(rows), "ok200": len(ok), "sample": [list(x) for x in ok[:12]]}
    print(f"  KSO sunspot_drawings CDX: {len(rows)} rows, {len(ok)} status-200", flush=True)
    st, html = get_text("https://cesar.kso.ac.at/sunspot_drawings/automatic/1999/", cap=900_000)
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    print(f"  KSO automatic/1999 {st}: {len(hrefs)} hrefs, sample {hrefs[:10]}", flush=True)
    out["kso_1999"] = {"status": st, "hrefs": hrefs[:30]}
    imgs = [h for h in hrefs if re.search(r"\.(jpg|jpeg|gif|png|dat|txt)$", h, re.I)]
    if imgs:
        url = imgs[0] if imgs[0].startswith("http") else "https://cesar.kso.ac.at/sunspot_drawings/automatic/1999/" + imgs[0].lstrip("./")
        out["kso_sample"] = evidence("KSO sunspot drawing file (1999)", url,
                                     "kso-" + url.rsplit("/", 1)[-1], cap=4_000_000)

    gh.save({"verify16c": out}, "verify16c")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
