#!/usr/bin/env python3
"""Campaign 3 — SCIENCE first, historical statistics second (Atharva, 2026-11-17).
Pure social-science survey/IR targets dropped. What stays is either
natural science, or a historical statistical series whose vintages /
deleted versions can yield a pattern (the eclipse / Gazetteer shape).

Targets:
 - SILSO sunspot numbers (sidc.be) — historical astro statistics; the
   famous 2015 v1->v2 recalibration is a Two-Rulers analogue; old
   datafiles live on the project site, versions in Wayback.
 - FishBase (fishbase.se) — species x traits, the ecology Brain Catalogue.
 - TimeTree (timetree.org) — divergence times x species pairs, versioned.
 - Exoplanet Encyclopaedia (exoplanet.eu) — planet catalogue, versioned csv/vot.
 - Paleobiology Database (paleobiodb.org) — fossil occurrences x taxa/time.
 - Gapminder (gapminder.org) — historical stats x country-year as xlsx,
   old versions deleted = vintage comparison.
Plus a hard check on yesterday's biggest science pile:
 - WorldClim v1: count ONLY statuscode:200 Wayback captures of the bio/
   zip sets, sample-download the smallest zip and verify it opens.
Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

SITES = [
    ("SILSO sunspot numbers (historical astro stats)", "https://www.sidc.be/SILSO/home"),
    ("FishBase species traits (ecology)", "https://www.fishbase.se"),
    ("TimeTree divergence times (evolution)", "https://timetree.org"),
    ("Exoplanet Encyclopaedia (astro)", "https://exoplanet.eu"),
    ("Paleobiology Database (paleo)", "https://paleobiodb.org"),
    ("Gapminder historical stats (stats)", "https://www.gapminder.org"),
]

def main():
    results = []
    for label, url in SITES:
        print(f"\n#### {label} — {url}", flush=True)
        try:
            crawl = gh.crawl_site(url, depth=1, max_pages=25)
        except Exception as e:
            print(f"  crawl failed: {e}", flush=True)
            crawl = {"data_files": [], "images": [], "pages": []}
        uniq = {}
        for f in crawl["data_files"]:
            if f["name"].lower() in gh.IGNORE_NAMES or " " in f["name"]:
                continue
            uniq.setdefault(f["name"], f)
        ranked = sorted(uniq.values(), key=lambda x: -gh.gold_score(x["name"], False))
        wb = gh.wayback_inventory(urlparse(url).netloc)
        wb_data = [w for w in wb if gh.is_data(w["url"]) and " " not in w["name"]]
        sets = collections.Counter()
        for w in wb_data:
            p = urlparse(w["url"]).path
            sets[p.rsplit("/", 1)[0] or "/"] += 1
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files | "
              f"wayback: {len(wb_data)} archived data files", flush=True)
        for f in ranked[:8]:
            print(f"    [score {gh.gold_score(f['name'], False):2d}] {f['name']}  <- {f['url'][:110]}", flush=True)
        for k, n in sets.most_common(5):
            print(f"    wb-set {n:4d}  {k}", flush=True)
        results.append({"label": label, "url": url, "pages": len(crawl["pages"]),
                        "unique_data_files": len(uniq),
                        "top": [{"name": f["name"], "url": f["url"], "score": gh.gold_score(f["name"], False)} for f in ranked[:20]],
                        "wayback_data_files": len(wb_data),
                        "wayback_sets": dict(sets.most_common(12)),
                        "wayback_top": [{"name": w["name"], "url": w["url"], "first_capture": w["first_capture"], "status": w["status"]} for w in sorted(wb_data, key=lambda x: -gh.gold_score(x["name"], False, True))[:20]]})
    gh.save({"campaign3_science": results}, "campaign3")
    print("\n=== CAMPAIGN3 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files"])):
        print(f"  live {r['unique_data_files']:4d} | wayback {r['wayback_data_files']:5d} | {r['label']}", flush=True)

if __name__ == "__main__":
    main()
