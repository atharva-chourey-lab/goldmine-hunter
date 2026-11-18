#!/usr/bin/env python3
"""Campaign 5 — "tons and tons of gold" (Atharva, 2026-11-18).

Doctrine (README, standing): the pattern that actually pays is old
lab / personal / university sites and vintage edition stacks, NOT
modern portals. Campaigns 2+3 gold was Maddison vintages (deleted,
Wayback-only, verified). Campaign 4 found NO stranded set on its 15
hosts; its only deleted verified set was HCA 2019-20 matrices.

Fresh targets only — none hunted in Campaigns 1-4:
 C1 SDSS, Glottolog, WALS, WorldClim, Movebank, OpenHeritage3D,
    Marmoset Brain, BrainInfo, Xeno-canto
 C2 PHOIBLE, IDS, TRY, HMD, CoW, Systemic Peace, Maddison/GGDC
    (ggdc.net), WVS, UCDP, QoG
 C3 SILSO, FishBase, TimeTree, Exoplanet, PaleobioDB, Gapminder
 C4 DBB, Tabula Muris, STScI, HCA, AnAge, Harvard WBA, HyperLEDA,
    GCVS, NOW, HPA, Neotoma, Rosetta, ADW, TreeBASE, Seshat

Note on PWT: ggdc.net was hunted in C2 for *Maddison*; the Penn World
Table itself, on its rug.nl host, was never hunted. Distinct dataset,
distinct host — included and disclosed as such in the shortlist.

Method (standing upgrade): live crawl depth 1, max 25 pages/site +
Wayback inventory FILTERED to statuscode:200 BEFORE counting any
set. Raw counts count for nothing. Every promising pile gets a
sample-download verification in verify5.py (size + md5 + magic).

Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

SITES = [
    ("Penn World Table old vintages (econ history, RUG/GGDC — rug.nl host, PWT never hunted; Maddison on ggdc.net was C2)", "https://www.rug.nl/ggdc/productivity/pwt/"),
    ("Starling / Global Lexicostatistical Database (linguistics, Moscow school, old CGI site)", "https://starlingdb.org"),
    ("CRU UEA climate data files (climate, university unit site)", "https://crudata.uea.ac.uk/cru/data/"),
    ("ATNF Pulsar Catalogue old versions (astro, CSIRO lab site)", "https://www.atnf.csiro.au/research/pulsar/psrcat/"),
    ("Villanova White Dwarf Catalog (astro, university personal/lab site)", "http://www.astronomy.villanova.edu/WDCatalog/index.html"),
    ("CATH protein structure classification old releases (UCL lab site)", "https://www.cathdb.info"),
    ("SCOP protein classification old releases (MRC-LMB Cambridge lab site)", "https://scop.mrc-lmb.cam.ac.uk"),
    ("Pfam old releases (protein families, ex-Xfam lab site)", "https://pfam.xfam.org"),
    ("Particle Data Group historical editions (physics, LBL lab site)", "https://pdg.lbl.gov"),
    ("CLIO Infra historical statistics (social/econ history, IISH project site)", "https://clio-infra.eu"),
    ("Bank of England research datasets / Millennium of Macroeconomic Data vintages (econ history)", "https://www.bankofengland.co.uk/statistics/research-datasets"),
    ("UCSC Genome Browser goldenPath old assemblies (genomics, university lab downloads)", "https://hgdownload.soe.ucsc.edu/goldenPath/"),
    ("Tree of Life Web Project (evolution, old university project site)", "http://tolweb.org"),
    ("Reptile Database old exports (ecology/herpetology, personal-project site)", "https://reptile-database.org"),
    ("OEIS integer sequences catalogue stack (maths catalogue, foundation site)", "https://oeis.org"),
    ("D-PLACE cross-cultural database (anthropology/linguistics project site)", "https://d-place.org"),
    ("Minor Planet Center data (astro catalogue, observatory site)", "https://www.minorplanetcenter.net/data"),
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
        wb_all = gh.wayback_inventory(urlparse(url).netloc)
        wb_data = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"] and str(w.get("status")) == "200"]
        wb_data_all = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"]]
        sets = collections.Counter()
        for w in wb_data:
            p = urlparse(w["url"]).path
            sets[p.rsplit("/", 1)[0] or "/"] += 1
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files | "
              f"wayback: {len(wb_data)} status-200 data files ({len(wb_data_all)} raw)", flush=True)
        for f in ranked[:8]:
            print(f"    [gold {gh.gold_score(f['name'], False):2d}] {f['name']}  <- {f['url'][:110]}", flush=True)
        for k, n in sets.most_common(5):
            print(f"    wb200-set {n:4d}  {k}", flush=True)
        results.append({"label": label, "url": url,
                        "pages": len(crawl["pages"]),
                        "unique_data_files": len(uniq),
                        "top": [{"name": f["name"], "url": f["url"], "score": gh.gold_score(f["name"], False)} for f in ranked[:20]],
                        "wayback_data_files_status200": len(wb_data),
                        "wayback_data_files_raw": len(wb_data_all),
                        "wayback_sets_status200": dict(sets.most_common(12)),
                        "wayback_top": [{"name": w["name"], "url": w["url"], "first_capture": w["first_capture"], "status": w["status"]} for w in sorted(wb_data, key=lambda x: -gh.gold_score(x["name"], False, True))[:20]]})
    gh.save({"campaign5_gold": results}, "campaign5")
    print("\n=== CAMPAIGN5 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | {r['label']}", flush=True)

if __name__ == "__main__":
    main()
