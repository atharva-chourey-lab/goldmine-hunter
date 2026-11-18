#!/usr/bin/env python3
"""Verify11b — Campaign 11 correction/completion pass (C8 pattern).
Fixes: (1) SealID paper sample — MDPI served a 410 B HTML phantom
to this client, so the arXiv version is sampled instead;
(2) monk-seal PDF integrity (page count / EOF) for the saved
Wayback sample, whose downloaded size (1,048,576 B) differs from
its CDX length (967,472 B); (3) MN Matson report — CDX retried
under the www host and as a filtered prefix, never reported as
zero on one failed query shape; (4) GiraffeSpotter platform
probe; (5) Matson Wayback file census from the campaign output.
Run from goldmine-hunter/.
"""
import json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence

OUTDIR = "gold/campaign11-verify"
verify6.OUTDIR = OUTDIR

def get_text(url, cap=600_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 1. SealID paper — arXiv version (MDPI was a phantom to this client) ==", flush=True)
    out["sealid_arxiv"] = evidence("SealID paper (arXiv 2206.02260, same work as Sensors 2022)",
                                   "https://arxiv.org/pdf/2206.02260",
                                   "sealid-arxiv-2206.02260.pdf", cap=15_000_000)

    print("\n== 2. Monk-seal saved PDF integrity ==", flush=True)
    p = os.path.join(OUTDIR, "monk-seal-report-2017-2018.pdf")
    info = {"path": p, "bytes_on_disk": os.path.getsize(p)}
    raw = open(p, "rb").read()
    info["has_eof_marker"] = b"%%EOF" in raw[-2048:]
    try:
        import PyPDF2
        r = PyPDF2.PdfReader(p)
        info["pages"] = len(r.pages)
        t = (r.pages[2].extract_text() or "")[:300] if len(r.pages) > 2 else ""
        info["page3_text_sample"] = t
        print(f"  monk PDF: {info['pages']} pages, EOF={info['has_eof_marker']}, page3: {t[:120]!r}", flush=True)
    except Exception as e:
        info["pypdf_error"] = str(e)[:140]
        print(f"  monk PDF pypdf failed: {e}", flush=True)
    out["monk_integrity"] = info

    print("\n== 3. MN Matson report — CDX under variant shapes ==", flush=True)
    out["mn_variants"] = {}
    for prefix in ("www.leg.mn.gov/docs/2013/other/C130010.pdf",
                   "leg.mn.gov/docs/2013/other/*"):
        rows = cdx(prefix, limit=3000)
        ok = [x for x in rows if x[2] == "200"]
        hits = [x for x in ok if "C130010" in x[1]] if "*" in prefix else ok
        print(f"  {prefix}: collapsed {len(rows)}, status-200 {len(ok)}, C130010 hits {len(hits)}", flush=True)
        out["mn_variants"][prefix] = {"collapsed": len(rows), "ok200": len(ok), "hits": len(hits),
                                      "rows": [{"ts": x[0], "url": x[1], "length": x[3]} for x in hits[:5]]}
        if hits and "mn_sample" not in out:
            ts, orig, sc, ln, mt = hits[0]
            out["mn_sample"] = evidence(f"Matson MN DNR cementum report wb ({ln} B CDX)", wb(ts, orig),
                                         "matson-mn-dnr-cementum-report-2006.pdf", cap=15_000_000)

    print("\n== 4. GiraffeSpotter — platform probe ==", flush=True)
    st, html = get_text("https://giraffespotter.org/")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,100}Wildbook[^.]{0,120}", txt)
    print(f"  giraffespotter {st}; Wildbook mention: {bool(m)}", flush=True)
    out["giraffespotter"] = {"status": st, "snippet": (m.group(0)[:260] if m else None)}

    print("\n== 5. Matson Wayback census (from campaign11 output) ==", flush=True)
    import glob
    f = sorted(glob.glob("outputs/campaign11-*.json"))[-1]
    d = json.load(open(f))["campaign11_mammal3"]
    for r in d:
        if "Matson" in r["label"]:
            out["matson_campaign"] = {"wayback200": r["wayback_data_files_status200"],
                                       "sets": r["wayback_sets_status200"],
                                       "top": [t["name"] for t in r["top"][:10]]}
            print(f"  matsonslab.com wayback200={r['wayback_data_files_status200']} sets={r['wayback_sets_status200']}", flush=True)

    gh.save({"verify11b": out}, "verify11b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
