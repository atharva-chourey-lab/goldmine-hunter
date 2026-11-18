#!/usr/bin/env python3
"""Campaign 7 — the Mammal Wave, GENERATED from the mammal-grain
registry (Atharva, 2026-11-18: "Get this going. Be autonomous
today"). Seeds are the 7 groups in PROBE-MAMMAL-SEEDS.md firing
order. Grades were fixed BEFORE Campaign 6 in GRADES.md and
govern here unchanged — GOLD / DIAMOND / SILVER / INVENTORY /
KILL, never awarded on raw counts.

Exclusions honoured: NO North Pacific humpback platform set
(Happywhale already joined it — film-era / Southern / Atlantic /
sperm-whale sets only); password-protected / researcher-only
systems (Gorongosa Who's Who, GoMDIS) are custody questions,
documented, never scraped or circumvented.

Method (standing): live crawl + Wayback inventory FILTERED to
statuscode:200 BEFORE counting. Whole-domain Wayback only for
small hosts; big institutional domains (wellcomecollection.org,
archives.ucl.ac.uk, wii.gov.in, ewt.org.za, coastalstudies.org,
id.nlbc.go.jp) get crawl-only here + targeted checks in
verify7.py. Every promising pile is sample-verified in
verify7.py. Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (seed, niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    # 1 — regional fluke PDF catalogues (film-era / Southern / Atlantic / sperm)
    (1, "whale-fluke-trailing-edge", "Juneau Flukes (regional catalogue PDF)",
     "https://www.juneauflukes.org/", 1, 25, "juneauflukes.org"),
    (1, "whale-fluke-trailing-edge", "Whitehead Lab, Dalhousie (sperm-whale Flukebook + papers)",
     "http://whitelab.biology.dal.ca/", 1, 25, "whitelab.biology.dal.ca"),
    (1, "whale-fluke-trailing-edge", "The Sperm Whale Project (Dominica)",
     "https://www.thespermwhaleproject.org/", 1, 15, "thespermwhaleproject.org"),
    (1, "whale-fluke-trailing-edge", "Center for Coastal Studies (Gulf of Maine catalogue)",
     "https://coastalstudies.org/", 1, 15, None),
    # 2 — non-Gulf FinBase-era dolphin catalogues + NOAA extracts
    (2, "dolphin-dorsal-fin-notches", "Sarasota Dolphin Research Program (anchor; GoMDIS custody)",
     "https://sarasotadolphin.org/", 1, 15, "sarasotadolphin.org"),
    # 3 — elephant ID-card sites (public surface only)
    (3, "elephant-ear-edge-veins", "Elephant Encyclopedia & Database (elephant.se, incl. Amboseli records)",
     "https://www.elephant.se/", 1, 15, "elephant.se"),
    (3, "elephant-ear-edge-veins", "ElephantVoices (Gorongosa/Mara; Who's Who is password-protected — custody only)",
     "https://www.elephantvoices.org/", 1, 15, "elephantvoices.org"),
    (3, "elephant-ear-edge-veins", "Amboseli Trust for Elephants (ATE)",
     "https://www.amboseliephants.org/", 1, 15, "amboseliephants.org"),
    (3, "elephant-ear-edge-veins", "Save the Elephants (Samburu)",
     "https://www.savetheelephants.org/", 1, 15, None),
    # 4 — Galton/Penrose dermatoglyphics digitisation surface
    (4, "primate-fingerprints-dermatoglyphics", "Wellcome Collection — Chimpanzee Fingerprints work page",
     "https://wellcomecollection.org/works/n9q6q77r", 1, 10, None),
    (4, "primate-fingerprints-dermatoglyphics", "UCL Archives catalogue (Galton Papers)",
     "https://archives.ucl.ac.uk/", 1, 10, None),
    # 5 — Wagyu muzzle prints + Petersen tradition
    (5, "cattle-muzzle-prints", "National Wagyu Registry Association (wagyu.or.jp)",
     "https://www.wagyu.or.jp/", 1, 10, "wagyu.or.jp"),
    (5, "cattle-muzzle-prints", "NLBC cattle ID search (second ruler; interface)",
     "https://www.id.nlbc.go.jp/", 1, 10, None),
    # 6 — FIT per-species project piles
    (6, "paw-track-morphometrics-fit", "WildTrack (FIT) — projects, not just homepage",
     "https://www.wildtrack.org/", 1, 25, "wildtrack.org"),
    # 7 — whisker-spot catalogues
    (7, "whisker-spot-patterns", "Desert Lion Conservation (desertlion.info)",
     "http://www.desertlion.info/", 1, 20, "desertlion.info"),
    (7, "whisker-spot-patterns", "Endangered Wildlife Trust (Kruger lion whisker cataloguing)",
     "https://ewt.org.za/", 1, 10, None),
    (7, "whisker-spot-patterns", "Wildlife Institute of India (Lion software)",
     "https://www.wii.gov.in/", 1, 10, None),
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
            try:
                wb_all = gh.wayback_inventory(wb_domain)
            except Exception as e:
                print(f"  wayback failed: {e}", flush=True)
                wb_all = []
            wb_data = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"] and str(w.get("status")) == "200"]
            wb_data_all = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"]]
        sets = collections.Counter()
        for w in wb_data:
            p = urlparse(w["url"]).path
            sets[p.rsplit("/", 1)[0] or "/"] += 1
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files, {len(crawl['images'])} images | "
              f"wayback: {len(wb_data)} status-200 data files ({len(wb_data_all)} raw)"
              + (" [whole-domain skipped — targeted checks in verify7]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign7_mammal": results}, "campaign7")
    print("\n=== CAMPAIGN7 MAMMAL SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  seed {r['seed']} live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | {r['label']}", flush=True)

if __name__ == "__main__":
    main()
