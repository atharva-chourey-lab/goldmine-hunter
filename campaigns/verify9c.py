#!/usr/bin/env python3
"""Verify9c — Campaign 9 final correction pass.
Fixes three verify9/9b sample defects, recorded as corrections:
(1) diatoms sample was a favicon (9) then a habitat photo (9b) —
    here a real LM valve image from the species page's own refs;
(2) WSL wb sample was a 236 B flag gif (furniture) — here the
    species_list.js data file itself, counted live;
(3) BloodBook text extraction in 9b hit the Astro CSS head —
    here raw-HTML term counts + embedded-data hunt.
Plus: PSMSL station-15 monthly RLR data sample (the actual
series file behind the station page). Samples to
gold/campaign9-verify/. Run from goldmine-hunter/.
"""
import os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import evidence, UA

OUTDIR = "gold/campaign9-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=900_000, timeout=45):
    try:
        r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
        return r.status_code, r.url, r.text[:cap]
    except Exception as e:
        return None, url, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 5c. Diatom LM valve image (gumlet CDN, species page ref) ==", flush=True)
    out["diatom_lm"] = evidence("diatoms.org Cymbella hustedtii LM image 1",
        "https://diatoms.gumlet.io/images/species_lm_images/Cymbella_hustedtii1.jpg",
        "diatoms-Cymbella_hustedtii1.jpg", cap=3_000_000)

    print("\n== 6c. WSL species_list.js — the dendro key's data file ==", flush=True)
    out["wsl_species_js"] = evidence("WSL dendro species_list.js",
        "https://static.wsl.ch/land/products/dendro/js/species_list.js",
        "wsl-species_list.js", cap=3_000_000)
    p = os.path.join(OUTDIR, "wsl-species_list.js")
    if os.path.exists(p):
        js = open(p, encoding="utf-8", errors="ignore").read()
        out["wsl_js_stats"] = {"bytes": len(js),
                               "latin_name_like": len(re.findall(r"[A-Z][a-z]+ [a-z]{3,}", js)),
                               "sample": js[:300]}
        print(f"  species_list.js: {len(js)} B, ~{out['wsl_js_stats']['latin_name_like']} binomial-like strings", flush=True)

    print("\n== 7c. BloodBook raw-HTML term counts ==", flush=True)
    st, furl, html = get_text("https://www.bloodbook.com/world-abo-frequency.html", cap=1_500_000)
    low = html.lower()
    out["bloodbook_raw"] = {"status": st, "bytes": len(html),
                            "count_ABO": low.count("abo"), "count_percent_sign": html.count("%"),
                            "json_refs": sorted(set(re.findall(r'["\']([^"\']+\.json)["\']', html)))[:8],
                            "has_table_tag": "<table" in low}
    print(f"  BloodBook raw: {out['bloodbook_raw']}", flush=True)

    print("\n== 9c. PSMSL station 15 monthly RLR data file ==", flush=True)
    out["psmsl_15_rlr"] = evidence("PSMSL 15.rlrdata monthly (Liverpool)",
        "https://psmsl.org/data/obtaining/rlr.monthly.data/15.rlrdata",
        "psmsl-15.rlrdata", cap=3_000_000)

    gh.save({"verify9c": out}, "verify9c")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
