#!/usr/bin/env python3
"""Verify15b — Campaign 15 gap-closers: a clean bat .wav sample
(ASL's own upload + smallest Avisoft /batcalls Wayback wav),
and retries on the client-unreachable HE/ADS/CDS pages.
Samples to gold/campaign15-verify/. Run from goldmine-hunter/.
"""
import json, os, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence

OUTDIR = "gold/campaign15-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def main():
    out = {}

    print("\n== B1. ASL own-upload wav (live) ==", flush=True)
    out["asl_bb1"] = evidence("ASL bb1_x3.wav (own wp-content upload)",
                              "https://animalsoundlabs.pl/wp-content/uploads/2018/07/bb1_x3.wav",
                              "asl-bb1_x3.wav", cap=3_000_000)

    print("\n== B2. Avisoft /batcalls smallest Wayback wav ==", flush=True)
    rows = cdx("avisoft.com/batcalls/*", limit=8000, extra={"filter": r"original:.*\.wav"})
    ok = [x for x in rows if x[2] == "200"]
    ok_sorted = sorted(ok, key=lambda x: int(x[3] or 0))
    print(f"  avisoft/batcalls wav CDX: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
    out["avisoft_wav_cdx"] = {"collapsed": len(rows), "ok200": len(ok),
                              "smallest": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok_sorted[:10]]}
    if ok_sorted:
        ts, orig, sc, ln, mt = ok_sorted[0]
        out["avisoft_wav_sample"] = evidence(f"Avisoft batcalls wb wav ({ln} B CDX)", wb(ts, orig),
                                             "avisoft-wb-" + orig.rsplit("/", 1)[-1], cap=3_000_000)
    out["batcalls_live_head"] = head("http://batcalls.com/europe/playback/Barbastella_barbastellus_1_n.wav")
    print(f"  batcalls.com live wav head: {out['batcalls_live_head']}", flush=True)

    print("\n== B3. Historic England / ADS retries ==", flush=True)
    for tag, u in (("he_report", "https://historicengland.org.uk/research/results/reports/96-2022"),
                   ("ads_record", "https://archaeologydataservice.ac.uk/archives/view/vag_dendro/full_record.cfm?id=923")):
        try:
            r = requests.get(u, headers=UA, timeout=45, allow_redirects=True)
            out[tag] = {"status": r.status_code, "bytes": len(r.content),
                        "has_pdf_link": ".pdf" in r.text.lower(), "has_rwl": ".rwl" in r.text.lower()}
        except Exception as e:
            out[tag] = {"status": None, "error": str(e)[:140]}
        print(f"  {tag}: {out[tag]}", flush=True)

    print("\n== B4. CDS ReadMe retry over http ==", flush=True)
    out["vizier_readme_http"] = evidence("VizieR VI/132C ReadMe via http (head)",
                                         "http://cdsarc.cds.unistra.fr/viz-bin/ReadMe/VI/132C?format=txt",
                                         "vizier-vi132c-readme.txt", cap=400_000)

    gh.save({"verify15b": out}, "verify15b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
