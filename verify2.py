#!/usr/bin/env python3
"""Verify2 — statuscode:200-only audits for the four piles that matter.
The standing lesson: only 200 captures hold recoverable data, and a CDX
wildcard only works as a trailing prefix. Each check: CDX prefix query,
filter in code, group into comparable sets, report real counts.

1. WorldClim v1 — worldclim.org/data/* and www.worldclim.org/data/*, .zip only,
   + sample-download smallest 200-zip and test it opens.
2. SILSO — sidc.be/SILSO/datafiles*, sidc.oma.be/silso/datafiles*, plus the
   live datafiles index page crawl.
3. HMD v6 — mortality.org/File/GetDocument/hmd.v6/* — per-country set completeness.
4. Maddison — ggdc.net/maddison/Historical_Statistics/* — original Maddison files.
Run from goldmine-hunter/.
"""
import collections, io, sys, zipfile
import requests
sys.path.insert(0, ".")
import goldmine_hunter as gh

UA = {"User-Agent": "goldmine-hunter/2.0 (open-science dataset recovery)"}

def cdx(prefix, limit=8000):
    try:
        r = requests.get("http://web.archive.org/cdx/search/cdx",
                         params={"url": prefix, "output": "json",
                                 "fl": "timestamp,original,statuscode,length",
                                 "collapse": "urlkey", "limit": limit},
                         headers=UA, timeout=120)
        r.raise_for_status()
        rows = r.json()
        return rows[1:] if len(rows) > 1 else []
    except Exception as e:
        print(f"  CDX failed {prefix}: {e}", flush=True)
        return []

def report(label, rows, exts=None):
    ok = [x for x in rows if x[2] == "200"]
    if exts:
        ok = [x for x in ok if any(x[1].lower().split("?")[0].endswith(e) for e in exts)]
    print(f"{label}: {len(rows)} captures collapsed, {len(ok)} status-200 data files", flush=True)
    return ok

def main():
    out = {}

    # 1. WorldClim
    print("\n== WorldClim v1 ==", flush=True)
    rows = cdx("worldclim.org/data/*") + cdx("www.worldclim.org/data/*")
    seen = {}
    for x in rows:
        seen.setdefault(x[1], x)
    rows = list(seen.values())
    ok = report("worldclim /data zips", rows, exts=(".zip",))
    sets = collections.Counter()
    members = collections.defaultdict(list)
    for ts, orig, sc, ln in ok:
        base = orig.rsplit("/", 1)[-1]
        fam = base.split("_")[0] if "_" in base else base
        sets[fam] += 1
        members[fam].append((ts, orig, int(ln or 0)))
    for k, n in sets.most_common(15):
        print(f"  set {k:10s} {n:4d} files  {sum(x[2] for x in members[k]):,} archived B", flush=True)
    verdict = None
    flat = [m for v in members.values() for m in v if m[2] > 0]
    if flat:
        ts, orig, ln = min(flat, key=lambda x: x[2])
        print(f"  sampling smallest: {orig} ({ln:,} B, {ts})", flush=True)
        try:
            r = requests.get(f"https://web.archive.org/web/{ts}id_/{orig}", headers=UA, timeout=180)
            try:
                z = zipfile.ZipFile(io.BytesIO(r.content))
                verdict = f"ZIP OPENS — {len(z.namelist())} entries, first {z.namelist()[:3]}"
            except Exception as e:
                verdict = f"NOT A VALID ZIP: {e} (downloaded {len(r.content):,} B, head {r.content[:4]!r})"
        except Exception as e:
            verdict = f"DOWNLOAD FAILED: {e}"
        print(f"  verdict: {verdict}", flush=True)
    out["worldclim"] = {"captures": len(rows), "ok200_zips": len(ok), "sets": dict(sets.most_common(20)), "sample_verdict": verdict}

    # 2. SILSO
    print("\n== SILSO datafiles ==", flush=True)
    rows = []
    for p in ("sidc.be/SILSO/datafiles/*", "www.sidc.be/SILSO/datafiles/*",
              "sidc.oma.be/silso/datafiles/*", "www.sidc.be/silso/datafiles/*"):
        rows += cdx(p, limit=3000)
    seen = {}
    for x in rows:
        seen.setdefault(x[1], x)
    rows = list(seen.values())
    ok = report("silso datafiles", rows)
    names = collections.Counter(x[1].rsplit("/", 1)[-1].split("?")[0] for x in ok)
    for k, n in names.most_common(20):
        print(f"  {n:3d} captures  {k}", flush=True)
    out["silso"] = {"captures": len(rows), "ok200": len(ok), "files": dict(names.most_common(30))}
    try:
        crawl = gh.crawl_site("https://www.sidc.be/SILSO/datafiles", depth=0, max_pages=3)
        live = sorted({f["name"] for f in crawl["data_files"] if " " not in f["name"]})
        print(f"  live datafiles page: {len(live)} data files linked", flush=True)
        for n in live[:20]:
            print(f"    live: {n}", flush=True)
        out["silso"]["live_linked"] = live
    except Exception as e:
        print(f"  live crawl failed: {e}", flush=True)

    # 3. HMD v6
    print("\n== HMD v6 ==", flush=True)
    rows = cdx("mortality.org/File/GetDocument/hmd.v6/*")
    ok = report("hmd.v6", rows)
    per_country = collections.Counter()
    for ts, orig, sc, ln in ok:
        parts = orig.split("/hmd.v6/")
        if len(parts) > 1:
            per_country[parts[1].split("/")[0]] += 1
    print(f"  countries with 200-captures: {len(per_country)}", flush=True)
    for k, n in per_country.most_common(40):
        print(f"  {k:10s} {n}", flush=True)
    out["hmd_v6"] = {"captures": len(rows), "ok200": len(ok), "per_country": dict(per_country)}

    # 4. Maddison Historical Statistics
    print("\n== Maddison Historical_Statistics ==", flush=True)
    rows = cdx("ggdc.net/maddison/Historical_Statistics/*") + cdx("www.ggdc.net/maddison/Historical_Statistics/*")
    seen = {}
    for x in rows:
        seen.setdefault(x[1], x)
    rows = list(seen.values())
    ok = report("maddison HS", rows)
    for ts, orig, sc, ln in sorted(ok)[:30]:
        print(f"  200 {ts} {orig.rsplit('/',1)[-1]} ({ln} B)", flush=True)
    out["maddison"] = {"captures": len(rows), "ok200": len(ok),
                       "files": [x[1] for x in ok[:60]]}

    gh.save({"verify2": out}, "verify2")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
