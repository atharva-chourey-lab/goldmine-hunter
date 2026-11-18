#!/usr/bin/env python3
"""Campaign 6 — Wave 1, GENERATED from the niche registry
(Atharva, 2026-11-18: "collect as much gold as possible").
The first registry-generated campaign: seeds are the 9 from
PROBE-CAMPAIGN6-SEEDS.md, in probe order, heads of the top-8
9/10 niches. Grades were fixed BEFORE this ran in GRADES.md
(git commit 6d76541) — GOLD / DIAMOND / SILVER / INVENTORY / KILL.

Concrete hosts named by this campaign for the class-level seeds:
 7 growth strays — Harpenden Growth Study (UK Data Service study
   9330, ukdataservice.ac.uk) + Nittedal Growth Study (University
   of Oslo, uio.no) as the non-US stray named in the literature;
   AAOF itself is NOT fired on (consolidated flagship, probe kill).
 8 crop tail — Sanborn Field, University of Missouri
   (cafnr.missouri.edu / extension.missouri.edu), est. 1888, the
   Sanborn-class peer of the curated Morrow Plots.
 9 river-gauge — Irish OPW hydrometric archive / ICARUS data
   rescue (waterlevel.ie, the OPW hydrometric service; basin =
   Ireland, non-Danube, non-USDA). The rescued 8-catchment output
   is PANGAEA 950792 (published); the chart archive itself is the
   paper archive at OPW Headford described in the rescue papers.

Method (standing): live crawl + Wayback inventory FILTERED to
statuscode:200 BEFORE counting. Whole-domain Wayback only for
small hosts; big institutional domains (qmul.ac.uk, noaa.gov,
missouri.edu, ukdataservice.ac.uk, marine.ie, uio.no) get targeted
CDX prefix queries in verify6.py instead — a whole-domain count
there would be cap-limited noise, stated as such.
Every promising pile is sample-verified in verify6.py.
Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (seed, niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    (1, "frog-call-archives", "Fonoteca Zoologica (fonozoo.com)",
     "https://www.fonozoo.com/", 1, 25, "fonozoo.com"),
    (1, "frog-call-archives", "Fonoteca Zoologica catalogue host (fonozoo.mncn.csic.es)",
     "http://www.fonozoo.mncn.csic.es/", 1, 25, "fonozoo.mncn.csic.es"),
    (2, "fish-otoliths", "AFORO otolith database (ICM-CSIC)",
     "http://aforo.cmima.csic.es/", 1, 25, "aforo.cmima.csic.es"),
    (3, "fish-otoliths", "Otolitos UNAM",
     "https://otolitos.unam.mx/", 1, 25, "otolitos.unam.mx"),
    (4, "autopsy-cause-of-death-ledgers", "QMUL Barts dissection registers page",
     "https://www.qmul.ac.uk/fmd/about/our-history/records-of-bodies-dissected-at-the-st-bartholomews-hospital-medical-college/",
     1, 10, None),
    (5, "electric-fish-eod", "Mormyrids EOD lab (Cornell/Hopkins lineage) — DEEP crawl",
     "https://mormyrids.efishgenomics.com/", 2, 60, "mormyrids.efishgenomics.com"),
    (6, "salmon-scale-archives", "NOAA fisheries root (NEFSC scale lab lives under this domain; targeted InPort check in verify6)",
     "https://www.fisheries.noaa.gov/", 1, 15, None),
    (6, "salmon-scale-archives", "Marine Institute data catalogue (Burrishoole IFBA record)",
     "https://data.marine.ie/", 1, 15, None),
    (7, "longitudinal-growth-studies", "UK Data Service (Harpenden Growth Study 9330 lives here)",
     "https://ukdataservice.ac.uk/", 1, 15, None),
    (8, "long-term-crop-plot-books", "Sanborn Field story page (MU CAFNR)",
     "https://cafnr.missouri.edu/stories/from-the-soil-medicine/", 1, 15, None),
    (9, "river-gauge-charts", "OPW hydrometric service (waterlevel.ie) — Irish basin",
     "https://waterlevel.ie/", 1, 15, "waterlevel.ie"),
]

def main():
    results = []
    for seed, niche, label, url, depth, max_pages, wb_domain in SITES:
        print(f"\n#### Seed {seed} [{niche}] {label} — {url}", flush=True)
        try:
            crawl = gh.crawl_site(url, depth=depth, max_pages=max_pages)
        except Exception as e:
            print(f"  crawl failed: {e}", flush=True)
            crawl = {"data_files": [], "images": [], "pages": []}
        uniq = {}
        for f in crawl["data_files"]:
            if f["name"].lower() in gh.IGNORE_NAMES or " " in f["name"]:
                continue
            uniq.setdefault(f["name"], f)
        ranked = sorted(uniq.values(), key=lambda x: -gh.gold_score(x["name"], False))
        wb_data, wb_data_all = [], []
        if wb_domain:
            wb_all = gh.wayback_inventory(wb_domain)
            wb_data = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"] and str(w.get("status")) == "200"]
            wb_data_all = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"]]
        sets = collections.Counter()
        for w in wb_data:
            p = urlparse(w["url"]).path
            sets[p.rsplit("/", 1)[0] or "/"] += 1
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files, {len(crawl['images'])} images | "
              f"wayback: {len(wb_data)} status-200 data files ({len(wb_data_all)} raw)"
              + (" [whole-domain skipped — targeted CDX in verify6]" if not wb_domain else ""), flush=True)
        for f in ranked[:8]:
            print(f"    [gold {gh.gold_score(f['name'], False):2d}] {f['name']}  <- {f['url'][:110]}", flush=True)
        for k, n in sets.most_common(5):
            print(f"    wb200-set {n:4d}  {k}", flush=True)
        results.append({"seed": seed, "niche": niche, "label": label, "url": url,
                        "pages": len(crawl["pages"]),
                        "unique_data_files": len(uniq),
                        "images": len(crawl["images"]),
                        "top": [{"name": f["name"], "url": f["url"], "score": gh.gold_score(f["name"], False)} for f in ranked[:25]],
                        "wayback_data_files_status200": len(wb_data),
                        "wayback_data_files_raw": len(wb_data_all),
                        "wayback_sets_status200": dict(sets.most_common(12)),
                        "wayback_top": [{"name": w["name"], "url": w["url"], "first_capture": w["first_capture"], "status": w["status"]} for w in sorted(wb_data, key=lambda x: -gh.gold_score(x["name"], False, True))[:25]]})
    gh.save({"campaign6_wave1": results}, "campaign6")
    print("\n=== CAMPAIGN6 WAVE1 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  seed {r['seed']} live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | {r['label']}", flush=True)

if __name__ == "__main__":
    main()
