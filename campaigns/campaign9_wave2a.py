#!/usr/bin/env python3
"""Campaign 9 — Broad Wave 2A, GENERATED from the broad niche
registry (Atharva, 2026-11-18: "run a ton of more waves").
Fires the unfired broad-registry 8/10 band, in registry order:
cephalopod-beaks, bivalve-shell-rings, bird-egg-collections,
seed-bank-germination-vintages, diatom-type-slides,
wood-anatomy-xylarium, blood-group-surveys,
pathology-museum-jars, tide-marigrams.
Grades are GRADES.md's, fixed before digging, unchanged.

Hosts from the Campaign 9 host-discovery pass (2026-11-18):
loose-file leads first (woodanatomy.ch — the Schoch et al.
2004 personal/institute atlas; bloodbook.com — a one-person
Mourant-derived ABO compilation; the dead legacy host
diatom.ansp.org, Wayback-only; NOAA NCEI paleo author
directories), formal systems documented as such, never
circumvented (Genesys/GGCE, AFND, PSMSL, InsideWood, MVZ
Arctos/GBIF, Gordon Museum restricted access).

Method (standing, = Campaigns 6-8): live crawl + Wayback
inventory FILTERED to statuscode:200 BEFORE counting;
whole-domain Wayback only for small hosts; big institutional
domains get crawl-only here + targeted CDX in verify9.py.
Every promising pile is sample-verified in verify9.py.
Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    # 1 — cephalopod-beaks (8)
    ("cephalopod-beaks", "BAS Cephalopod Beak Guide page (Xavier & Cherel)",
     "https://www.bas.ac.uk/news/cephalopod-beak-guide-for-the-southern-ocean/", 1, 10, None),
    ("cephalopod-beaks", "NERC NORA eprint record 529835 (2021 guide PDF)",
     "https://nora.nerc.ac.uk/id/eprint/529835/", 1, 10, None),
    # 2 — bivalve-shell-rings (8)
    ("bivalve-shell-rings", "NOAA NCEI paleo Butler2013 author directory (Arctica increments)",
     "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/butler2013/", 1, 15, None),
    ("bivalve-shell-rings", "NOAA NCEI paleo Butler2009 author directory (Irish Sea chronology)",
     "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/butler2009/", 1, 15, None),
    ("bivalve-shell-rings", "sclerochronology.org (community site — live status check)",
     "https://www.sclerochronology.org/", 1, 10, "sclerochronology.org"),
    # 3 — bird-egg-collections (8)
    ("bird-egg-collections", "WFVZ collections page (world's largest egg collection)",
     "https://wfvz.org/collections/", 1, 15, "wfvz.org"),
    ("bird-egg-collections", "Alfred Denny Museum egg collection (Google Sites)",
     "https://sites.google.com/sheffield.ac.uk/admuseum/collections/eggs", 1, 5, None),
    ("bird-egg-collections", "MVZ Egg & Nest Collection page (Arctos/GBIF surface)",
     "http://mvz.berkeley.edu/Egg_Nest_Collection.html", 1, 10, None),
    # 4 — seed-bank-germination-vintages (8)
    ("seed-bank-germination-vintages", "Genesys PGR portal (formal genebank platform)",
     "https://www.genesys-pgr.org/", 1, 10, None),
    ("seed-bank-germination-vintages", "Marius Comper blog — 40-yr Australian Grains Genebank analysis (personal site)",
     "https://mariuscomper.uk/how-long-do-seeds-last-seed-vault/", 1, 5, "mariuscomper.uk"),
    # 5 — diatom-type-slides (8)
    ("diatom-type-slides", "Diatoms of North America (diatoms.org)",
     "https://diatoms.org/", 1, 20, None),
    ("diatom-type-slides", "ANSP Diatom Herbarium page",
     "https://ansp.org/research/systematics-evolution/diatom-herbarium/", 1, 10, None),
    ("diatom-type-slides", "Legacy ANSP diatom host diatom.ansp.org (dead live — Wayback check)",
     "http://diatom.ansp.org/", 1, 10, "diatom.ansp.org"),
    # 6 — wood-anatomy-xylarium (8)
    ("wood-anatomy-xylarium", "woodanatomy.ch — Schoch et al. Central European wood anatomy (old institute site)",
     "https://www.woodanatomy.ch/", 1, 25, "woodanatomy.ch"),
    ("wood-anatomy-xylarium", "InsideWood (NCSU — formal joined database)",
     "https://insidewood.lib.ncsu.edu/", 1, 15, None),
    ("wood-anatomy-xylarium", "WSL Xylem Database page",
     "https://www.wsl.ch/en/services-produkte/xylem-database/", 1, 10, None),
    # 7 — blood-group-surveys (8)
    ("blood-group-surveys", "BloodBook — world ABO frequency page (one-person compilation)",
     "http://www.bloodbook.com/world-abo-frequency.html", 1, 15, "bloodbook.com"),
    ("blood-group-surveys", "Allele Frequency Net Database (formal database)",
     "https://www.allelefrequencies.net/", 1, 10, None),
    # 8 — pathology-museum-jars (8)
    ("pathology-museum-jars", "Gordon Museum collection page (KCL — restricted-access museum)",
     "http://kcl.ac.uk/lsm/centre-for-education/museums/gordon-museum/the-collection", 1, 10, None),
    ("pathology-museum-jars", "Anatomical Theatre museum list (secondary index)",
     "http://www.astropop.com/anatomical/museums.html", 1, 5, None),
    # 9 — tide-marigrams (8)
    ("tide-marigrams", "PSMSL data obtaining index (formal service)",
     "https://psmsl.org/data/obtaining/", 1, 15, None),
    ("tide-marigrams", "PSMSL station 15 — Liverpool Georges/Princes Piers (1857-1983)",
     "https://psmsl.org/data/obtaining/stations/15.php", 1, 5, None),
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
              + (" [whole-domain skipped — targeted checks in verify9]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign9_wave2a": results}, "campaign9")
    print("\n=== CAMPAIGN9 WAVE2A SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
