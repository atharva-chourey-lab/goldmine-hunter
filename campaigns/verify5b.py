#!/usr/bin/env python3
"""Verify5b — Campaign 5 follow-up checks (same standing method).
Resolves the questions verify5 left open:
 1. CLIO IndicatorsPerCountry: is the Wayback file md5-identical to live?
 2. SCOP /files: full size of the wb scop-cla capture; a second member
    (represeq .fa); live status on http as well as https.
 3. CRU: live HEADs on actual crutem3 data files + a cru_ts_3.23
    country file; full wb sample of CRUTEM3-gl.dat.
 4. Villanova: CDX filtered to data extensions under WDCatalog/ and
    the /mccook/ FTP-mirror path HEASARC cites for WD*.txt files.
 5. Reptile: live download of reptile_checklist_2013_12.xls.zip —
    md5 vs the Wayback capture's 58169036be8fea12bb7e6815f9efd1b1.
Run from goldmine-hunter/.
"""
import hashlib, io, os, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from verify5 import evidence, head, cdx, wb

def md5_of(url, cap=30_000_000):
    r = requests.get(url, headers={"User-Agent": "goldmine-hunter/2.0"}, timeout=120, stream=True)
    h, n = hashlib.md5(), 0
    for chunk in r.iter_content(65536):
        h.update(chunk); n += len(chunk)
        if n > cap: break
    return {"status": r.status_code, "bytes": n, "md5": h.hexdigest()}

def main():
    out = {}

    print("\n== 1. CLIO IPC live vs wb md5 ==", flush=True)
    ipc = "https://clio-infra.eu/IndicatorsPerCountry/Samoa_Workingweekinmanufacturing_TerritorialRef_1976_2012_CCode_882.xlsx"
    out["clio_ipc_live_md5"] = md5_of(ipc)
    print(f"  live: {out['clio_ipc_live_md5']}", flush=True)

    print("\n== 2. SCOP full check ==", flush=True)
    scop_wb = wb("20201202220621", "http://scop.mrc-lmb.cam.ac.uk/files/scop-cla-20200228.txt")
    out["scop_wb_head"] = head(scop_wb)
    print(f"  wb scop-cla HEAD: {out['scop_wb_head']}", flush=True)
    out["scop_fa_wb"] = evidence("SCOP scop_fa_represeq_lib20200228.fa wb2020 (head 1MB via cap)",
                                 wb("20201202224826", "http://scop.mrc-lmb.cam.ac.uk/files/scop_fa_represeq_lib20200228.fa"),
                                 cap=1_000_000)
    out["scop_live_http"] = {"scop-cla-20200228.txt": head("http://scop.mrc-lmb.cam.ac.uk/files/scop-cla-20200228.txt"),
                             "scop-cla-latest.txt": head("http://scop.mrc-lmb.cam.ac.uk/files/scop-cla-latest.txt")}
    for k, v in out["scop_live_http"].items():
        print(f"  live-http {k}: {v}", flush=True)

    print("\n== 3. CRU live data-file HEADs + wb sample ==", flush=True)
    cru_files = [
        "https://crudata.uea.ac.uk/cru/data/crutem3/CRUTEM3-gl.dat",
        "https://crudata.uea.ac.uk/cru/data/crutem3/abstem3.zip",
        "https://crudata.uea.ac.uk/cru/data/temperature/CRUTEM.4.2.0.0.anomalies.nc",
    ]
    out["cru_live_heads"] = {u.rsplit("/", 1)[-1]: head(u) for u in cru_files}
    for k, v in out["cru_live_heads"].items():
        print(f"  HEAD {k}: {v}", flush=True)
    out["cru_gl_dat_wb"] = evidence("CRU CRUTEM3-gl.dat wb2016",
                                    wb("20161013064833", "https://crudata.uea.ac.uk/cru/data/crutem3/CRUTEM3-gl.dat"),
                                    "cru-CRUTEM3-gl.dat")
    rows = cdx("crudata.uea.ac.uk/cru/data/hrg/cru_ts_3.23/crucy.1506241137.v3.23/countries/tmp/*", limit=400)
    ok = [x for x in rows if x[2] == "200"]
    print(f"  cru_ts_3.23 tmp countries: collapsed {len(rows)}, status-200 {len(ok)}", flush=True)
    out["cru_ts323"] = {"collapsed": len(rows), "ok200": len(ok),
                        "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:20]]}
    if ok:
        ts, orig, sc, ln, mt = ok[0]
        out["cru_ts323_live_status_first"] = head(orig)
        print(f"  live-status {orig[:100]}: {out['cru_ts323_live_status_first']}", flush=True)

    print("\n== 4. Villanova data-extension CDX ==", flush=True)
    out["villanova_data"] = {}
    for prefix in ("astronomy.villanova.edu/WDCatalog/*", "astronomy.villanova.edu/mccook/*"):
        rows = cdx(prefix, limit=10000)
        ok = [x for x in rows if x[2] == "200" and gh.is_data(x[1])]
        print(f"  {prefix}: status-200 data-ext {len(ok)}", flush=True)
        for ts, orig, sc, ln, mt in ok[:15]:
            print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
        out["villanova_data"][prefix] = {"ok200_data": len(ok),
                                         "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:40]]}
        if ok:
            ts, orig, sc, ln, mt = sorted(ok, key=lambda x: int(x[3] or 0))[0]
            out["villanova_data"][prefix + " sample"] = evidence(f"Villanova smallest data wb ({ln} B CDX)", wb(ts, orig))

    print("\n== 5. Reptile live checklist md5 vs wb ==", flush=True)
    out["reptile_checklist_live_md5"] = md5_of("http://www.reptile-database.org/data/reptile_checklist_2013_12.xls.zip")
    print(f"  live: {out['reptile_checklist_live_md5']}  (wb md5 was 58169036be8fea12bb7e6815f9efd1b1)", flush=True)

    gh.save({"verify5b": out}, "verify5b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
