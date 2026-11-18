#!/usr/bin/env python3
"""Campaign 12 — Mammal Wave 4, GENERATED from the mammal-grain
registry's 7/10 batch (part 1), in registry order:
primate-palm-sole-dermatoglyphics, paw-pad-ridge-patterns,
bear-paw-mensuration, canid-track-size-archives,
snow-track-gait-archives, elephant-tusk-patterns,
cheetah-spot-patterns, snow-leopard-rosettes,
painted-dog-coat-patterns, pangolin-scale-patterns.
Grades are GRADES.md's, unchanged.

Hosts from the Campaign 12 discovery pass (2026-11-18 searches):
loose-file leads first (mjkelly.info personal site, journal PDFs,
Mara-Meru foundation reports), formal archives counted as such
(NASA ORNL DAAC snow-tracks, Luke wildlife triangles, Hokkaido
ERDP data paper), custody/sensitive systems documented, never
circumvented (Gorongosa Who's Who, snow-leopard PAWS locations,
painted-dog pack catalogues, pangolin programme marking systems).

Method (standing, = Campaigns 7-8): live crawl + Wayback inventory
FILTERED to statuscode:200 BEFORE counting; whole-domain Wayback
only for small hosts. Every promising pile sample-verified in
verify12.py. Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

SITES = [
    ("primate-palm-sole-dermatoglyphics", "Turkish J Pediatrics — Down syndrome dermatoglyphics PDF (journal site)",
     "https://turkjpediatr.org/article/download/4340/4948/48939", 0, 3, None),
    ("primate-palm-sole-dermatoglyphics", "Int J Biomedicine — Kosova atd comparison PDF",
     "https://www.ijbm.org/articles/i51/ijbm_13(3)_oa15.pdf", 0, 3, None),
    ("paw-pad-ridge-patterns", "Murie Peterson Field Guide full text (archive.org)",
     "https://dn720005.ca.archive.org/0/items/peterson-field-guide-animal-tracks/Peterson%20Field%20Guide%20Animal%20Tracks_djvu.txt", 0, 3, None),
    ("paw-pad-ridge-patterns", "Amherst — Tracks and Scat Identification sheet PDF",
     "https://cpb-us-w2.wpmucdn.com/wordpress.amherst.edu/dist/3/137/files/2020/03/Track-and-Scat-Identification-1.pdf", 0, 3, None),
    ("bear-paw-mensuration", "Virginia DWR — judging age/sex of black bears (paw-width rule)",
     "https://dwr.virginia.gov/blog/how-to-judge-the-age-and-sex-of-black-bears/", 1, 8, None),
    ("bear-paw-mensuration", "Ecological Research — Hokkaido brown bear 40yr field-sign data paper",
     "https://esj-journals.onlinelibrary.wiley.com/doi/10.1111/1440-1703.70054", 0, 3, None),
    ("canid-track-size-archives", "Wisconsin DNR wolf monitoring report PDF (preprod host)",
     "https://preprod-wpr-main.pantheonsite.io/wp-content/uploads/2026/09/2026-Annual-Wolf-Report_July2026.pdf", 0, 3, None),
    ("canid-track-size-archives", "NASA Snow Wildlife Tracks — data.gov catalogue page (ORNL DAAC 2188)",
     "https://catalog.data.gov/dataset/snow-properties-and-wildlife-tracks-in-washington-and-alaska", 1, 8, None),
    ("snow-track-gait-archives", "Natural Resources Institute Finland (Luke) — wildlife triangle host",
     "https://www.luke.fi/en", 1, 12, None),
    ("snow-track-gait-archives", "NASA Earthdata — Snow Wildlife Tracks AK/WA catalogue",
     "https://www.earthdata.nasa.gov/data/catalog/ornl-cloud-snow-wildlife-tracks-ak-wa-2188-1", 0, 3, None),
    ("elephant-tusk-patterns", "ElephantVoices (Gorongosa Who's Who custody surface)",
     "https://www.elephantvoices.org/", 1, 12, "elephantvoices.org"),
    ("elephant-tusk-patterns", "Pachyderm — Who's Who & Whereabouts system paper PDF (tusk attributes)",
     "https://Pachydermjournal.org/index.php/pachyderm/article/download/482/498", 0, 3, None),
    ("cheetah-spot-patterns", "Kelly personal site — Serengeti cheetah computer-aided ID paper PDF (mjkelly.info)",
     "http://mjkelly.info/ewExternalFiles/computeraid.pdf", 0, 3, "mjkelly.info"),
    ("cheetah-spot-patterns", "Mara-Meru Cheetah Project Annual Report 2022 PDF (Roman Wildlife Foundation)",
     "https://romanwildlifefoundation.com/files/uploads/annual-report-2022.pdf", 0, 3, None),
    ("snow-leopard-rosettes", "Snow Leopard Trust (snowleopard.org — PAWS / Ghost Trackers)",
     "https://snowleopard.org/the-ghost-trackers-how-indigenous-women-are-leading-snow-leopard-conservation-in-the-himalayas/", 1, 12, "snowleopard.org"),
    ("painted-dog-coat-patterns", "Endangered Wildlife Trust (Kruger wild-dog monitoring surface)",
     "https://ewt.org.za/", 1, 10, None),
    ("painted-dog-coat-patterns", "Painted Dog Conservation (painteddog.org)",
     "https://www.painteddog.org/", 1, 12, "painteddog.org"),
    ("pangolin-scale-patterns", "PUNS preprint PDF (EcoEvoRxiv — programme marking systems survey)",
     "https://ecoevorxiv.org/repository/object/6274/download/12204/", 0, 3, None),
    ("pangolin-scale-patterns", "CITES CoP18 — IUCN Pangolin SG monitoring methods PDF",
     "https://cites.org/sites/default/files/eng/cop/18/inf/P-CoP18-Inf-075.pdf", 0, 3, None),
    ("pangolin-scale-patterns", "WTI Wildlife ID & Post-Seizure Guide PDF (pangolin scale ID)",
     "https://www.wti.org.in/wp-content/uploads/2026/03/SPECIES-ID-POST-IDENTIFICATION-GUIDE.pdf", 0, 3, None),
]

def main():
    results = []
    for niche, label, url, depth, max_pages, wb_domain in SITES:
        print(f"\n#### [{niche}] {label} — {url}", flush=True)
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
              + (" [whole-domain skipped — targeted checks in verify12]" if not wb_domain else ""), flush=True)
        for f in ranked[:8]:
            print(f"    [gold {gh.gold_score(f['name'], False):2d}] {f['name']}  <- {f['url'][:110]}", flush=True)
        for k, n in sets.most_common(5):
            print(f"    wb200-set {n:4d}  {k}", flush=True)
        results.append({"niche": niche, "label": label, "url": url,
                        "pages": len(crawl["pages"]),
                        "unique_data_files": len(uniq),
                        "images": len(crawl["images"]),
                        "top": [{"name": f["name"], "url": f["url"], "score": gh.gold_score(f["name"], False)} for f in ranked[:25]],
                        "wayback_data_files_status200": len(wb_data),
                        "wayback_data_files_raw": len(wb_data_all),
                        "wayback_sets_status200": dict(sets.most_common(12)),
                        "wayback_top": [{"name": w["name"], "url": w["url"], "first_capture": w["first_capture"], "status": w["status"]} for w in sorted(wb_data, key=lambda x: -gh.gold_score(x["name"], False, True))[:25]]})
    gh.save({"campaign12_mammal4": results}, "campaign12")
    print("\n=== CAMPAIGN12 MAMMAL4 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
