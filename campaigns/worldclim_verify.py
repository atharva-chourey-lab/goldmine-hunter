#!/usr/bin/env python3
"""WorldClim v1 hard check — yesterday's doctrine run counted 727 Wayback
data files but sampled live-HEAD (all 403, uninformative). The only
question that matters: how many captures are statuscode:200 (the standing
lesson: only 200 captures hold recoverable data), grouped as the bio /
prec / tmean... comparable sets, and does one sampled zip actually
download and open? Run from goldmine-hunter/.
"""
import collections, io, json, os, sys, zipfile
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh

UA = {"User-Agent": "goldmine-hunter/2.0 (open-science dataset recovery)"}

def cdx(url_pattern, limit=2000):
    r = requests.get("http://web.archive.org/cdx/search/cdx",
                     params={"url": url_pattern, "output": "json",
                             "fl": "timestamp,original,statuscode,length",
                             "collapse": "urlkey", "limit": limit},
                     headers=UA, timeout=120)
    r.raise_for_status()
    return r.json()[1:]

def main():
    rows = cdx("worldclim.org/data/*.zip")
    print(f"total zip captures (collapsed): {len(rows)}", flush=True)
    ok = [x for x in rows if x[2] == "200"]
    print(f"statuscode:200: {len(ok)}", flush=True)
    sets = collections.Counter()
    members = collections.defaultdict(list)
    for ts, orig, sc, ln in ok:
        base = orig.rsplit("/", 1)[-1]
        fam = base.split("_")[0] if "_" in base else base
        sets[fam] += 1
        members[fam].append((ts, orig, int(ln or 0)))
    for k, n in sets.most_common(20):
        tot = sum(x[2] for x in members[k])
        print(f"  set {k:10s} {n:4d} files  {tot:,} archived bytes", flush=True)
    # sample: smallest 200-capture zip, download head of it via wayback and test zip
    verdict = None
    if ok:
        ts, orig, ln = min(ok, key=lambda x: int(x[3] or 10**12))
        url = f"https://web.archive.org/web/{ts}id_/{orig}"
        print(f"\nsampling smallest: {orig} ({ln:,} B archived, capture {ts})", flush=True)
        try:
            r = requests.get(url, headers=UA, timeout=180)
            print(f"  downloaded {len(r.content):,} B, http {r.status_code}", flush=True)
            try:
                z = zipfile.ZipFile(io.BytesIO(r.content))
                names = z.namelist()
                verdict = f"ZIP OPENS — {len(names)} entries, first: {names[:3]}"
            except Exception as e:
                verdict = f"NOT A VALID ZIP: {e} (first bytes: {r.content[:4]!r})"
        except Exception as e:
            verdict = f"DOWNLOAD FAILED: {e}"
        print(f"  verdict: {verdict}", flush=True)
    out = {"total_zip_captures": len(rows), "status200": len(ok),
           "sets": dict(sets.most_common(30)), "sample_verdict": verdict}
    gh.save({"worldclim_verify": out}, "worldclim-verify")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
