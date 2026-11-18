#!/usr/bin/env python3
"""Verify12b — NASA bundle contents + CITES via Wayback."""
import io, json, os, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA
verify6.OUTDIR = "gold/campaign12-verify"
evidence = verify6.evidence

def main():
    out = {}
    print("\n== NASA ORNL DAAC 2188 bundle — full download + zip listing ==", flush=True)
    ev = evidence("NASA Snow Wildlife Tracks bundle zip (ORNL DAAC 2188)",
                  "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/Snow_Wildlife_Tracks_AK_WA_2188.zip",
                  "nasa-snow-tracks-2188.zip", cap=5_000_000)
    out["nasa_bundle"] = ev
    p = "gold/campaign12-verify/nasa-snow-tracks-2188.zip"
    if os.path.exists(p):
        try:
            z = zipfile.ZipFile(p)
            infos = [{"name": i.filename, "size": i.file_size} for i in z.infolist()]
            out["nasa_bundle_contents"] = infos
            for i in infos: print(f"    {i['size']:>10}  {i['name']}", flush=True)
            # count CSV rows for the main data file
            for i in infos:
                if i["name"].lower().endswith(".csv"):
                    data = z.read(i["name"])
                    out.setdefault("nasa_csv_rows", {})[i["name"]] = data.count(b"\n")
                    print(f"    CSV {i['name']}: {data.count(bytes([10]))} lines", flush=True)
        except Exception as e:
            out["nasa_bundle_error"] = str(e)[:160]
    print("\n== CITES pangolin PDF via Wayback ==", flush=True)
    rows = cdx("cites.org/sites/default/files/eng/cop/18/inf/P-CoP18-Inf-075.pdf", limit=50)
    rows200 = [r for r in rows if r[2] == "200"]
    print(f"  CITES CDX rows: {len(rows)}, status-200: {len(rows200)}", flush=True)
    out["cites_cdx200"] = len(rows200)
    if rows200:
        ts, orig = rows200[0][0], rows200[0][1]
        out["cites_wb"] = evidence("CITES pangolin methods via Wayback", wb(orig, ts), "cites-pangolin-wb.pdf", cap=20_000_000)
    gh.save({"verify12b": out}, "verify12b")
    print("verify12b saved", flush=True)

if __name__ == "__main__":
    main()
