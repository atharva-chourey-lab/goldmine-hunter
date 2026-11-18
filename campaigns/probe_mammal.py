#!/usr/bin/env python3
"""Light probe — mammal-grain registry top 6 (2026-11-18).
Targeting/tooling validation only: light crawl (depth 1, <=15 pages)
+ Wayback status-200 inventory per concrete host. NO bulk downloads,
NO gold claimed — outputs feed PROBE-MAMMAL-SEEDS.md.
"""
import collections, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

HOSTS = [
    ("whale-fluke-trailing-edge", "Juneau Flukes catalog", "https://www.juneauflukes.org"),
    ("paw-track-morphometrics-fit", "WildTrack / ConservationFIT", "https://www.wildtrack.org"),
    ("dolphin-dorsal-fin-notches", "Sarasota Dolphin Research Program / GoMDIS", "https://sarasotadolphin.org"),
    ("elephant-ear-edge-veins", "ElephantVoices", "https://www.elephantvoices.org"),
]

def main():
    results = []
    for slug, label, url in HOSTS:
        print(f"\n#### {slug} — {label} — {url}", flush=True)
        try:
            crawl = gh.crawl_site(url, depth=1, max_pages=15)
        except Exception as e:
            print(f"  crawl failed: {e}", flush=True)
            crawl = {"data_files": [], "images": [], "pages": []}
        uniq = {}
        for f in crawl["data_files"]:
            if f["name"].lower() in gh.IGNORE_NAMES or " " in f["name"]:
                continue
            uniq.setdefault(f["name"], f)
        ranked = sorted(uniq.values(), key=lambda x: -gh.mammal_niche_score(x["name"], slug))
        wb_all = gh.wayback_inventory(urlparse(url).netloc)
        wb200 = [w for w in wb_all if str(w.get("status")) == "200" and " " not in w["name"]]
        wb_data = [w for w in wb200 if gh.is_data(w["url"])]
        wb_img = [w for w in wb200 if gh.is_image(w["url"])]
        exts = collections.Counter(os.path.splitext(w["name"].lower())[1] for w in wb_data)
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files, {len(crawl['images'])} images", flush=True)
        print(f"  wayback-200: {len(wb_data)} data files, {len(wb_img)} images | data exts: {dict(exts.most_common(6))}", flush=True)
        for f in ranked[:6]:
            print(f"    [mammal {gh.mammal_niche_score(f['name'], slug):2d}] {f['name']} <- {f['url'][:100]}", flush=True)
        for w in sorted(wb_data, key=lambda x: -gh.mammal_niche_score(x["name"], slug))[:6]:
            print(f"    wb200 [{w['first_capture'][:4]}] {w['name']} <- {w['url'][:100]}", flush=True)
        results.append({"niche": slug, "host": label, "url": url,
                        "pages": len(crawl["pages"]), "unique_data_files": len(uniq),
                        "live_top": [{"name": f["name"], "url": f["url"], "mammal_score": gh.mammal_niche_score(f["name"], slug)} for f in ranked[:12]],
                        "wayback200_data": len(wb_data), "wayback200_images": len(wb_img),
                        "wayback_data_exts": dict(exts.most_common(10)),
                        "wayback_top": [{"name": w["name"], "url": w["url"], "first_capture": w["first_capture"]} for w in sorted(wb_data, key=lambda x: -gh.mammal_niche_score(x["name"], slug))[:12]]})
    gh.save({"probe_mammal_top6": results}, "probe-mammal")
    print("\n=== PROBE-MAMMAL SUMMARY ===", flush=True)
    for r in results:
        print(f"  live {r['unique_data_files']:3d} | wb200 data {r['wayback200_data']:4d} | wb200 img {r['wayback200_images']:4d} | {r['niche']} @ {r['host']}", flush=True)

if __name__ == "__main__":
    main()
