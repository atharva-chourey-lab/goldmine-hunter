#!/usr/bin/env python3
"""Campaign: point Goldmine Hunter at a batch of candidate sites across
domains — old project/lab/atlas sites whose data may be stranded outside
any formal archive. Per site: live crawl inventory (deduped, scored)
+ Wayback inventory. Run from goldmine-hunter/."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

SITES = [
    ("SDSS data archive (astro)", "https://data.sdss.org"),
    ("Glottolog (linguistics)", "https://glottolog.org"),
    ("WALS language atlas (linguistics)", "https://wals.info"),
    ("WorldClim (geo/climate)", "https://www.worldclim.org"),
    ("Movebank animal tracking (ecology)", "https://www.movebank.org"),
    ("Open Heritage 3D (heritage)", "https://openheritage3d.org"),
    ("Marmoset Brain Atlas (neuro)", "https://www.marmosetbrain.org"),
    ("BrainInfo primate (neuro, old site)", "http://braininfo.rprc.washington.edu"),
    ("Xeno-canto bird audio (ecology/media)", "https://xeno-canto.org"),
]

def main():
    results = []
    for label, url in SITES:
        print(f"\n#### {label} — {url}", flush=True)
        try:
            crawl = gh.crawl_site(url, depth=1, max_pages=20)
        except Exception as e:
            print(f"  crawl failed: {e}", flush=True)
            crawl = {"data_files": [], "images": [], "pages": []}
        uniq = {}
        for f in crawl["data_files"]:
            if f["name"].lower() in gh.IGNORE_NAMES:
                continue
            uniq.setdefault(f["name"], f)
        ranked = sorted(uniq.values(), key=lambda x: -gh.gold_score(x["name"], False))
        wb = gh.wayback_inventory(urlparse(url).netloc)
        wb_data = [w for w in wb if gh.is_data(w["url"])]
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files, "
              f"{len(crawl['images'])} images | wayback: {len(wb_data)} archived data files", flush=True)
        for f in ranked[:6]:
            print(f"    [score {gh.gold_score(f['name'], False):2d}] {f['name']}", flush=True)
        results.append({"label": label, "url": url, "pages": len(crawl["pages"]),
                        "unique_data_files": len(uniq),
                        "top": [{"name": f["name"], "url": f["url"],
                                 "score": gh.gold_score(f["name"], False)} for f in ranked[:15]],
                        "wayback_data_files": len(wb_data)})
    gh.save({"campaign": results}, "campaign")
    print("\n=== CAMPAIGN SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -x["unique_data_files"]):
        print(f"  {r['unique_data_files']:5d} live data files | {r['wayback_data_files']:5d} wayback | {r['label']}", flush=True)

if __name__ == "__main__":
    main()
