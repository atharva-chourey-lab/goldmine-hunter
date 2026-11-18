#!/usr/bin/env python3
"""Campaign 4 — MORE (Atharva, 2026-11-17: "Fire goldmine hunter for more").

Two lanes, science-first, per the standing doctrine:

Lane A — Fidelity leftovers. The Fidelity Campaign catalogued 9 systems;
only morpho-CT, Gaia and cosmology were actually pulled. These four were
catalogued fertile, never downloaded — run them now with fidelity scoring
and a filled 4-line card (RAW / UNIT / LABEL GAP / ANCHOR) per system:
 - Digital Brain Bank (connectome)
 - Tabula Muris (singlecell)
 - Kepler/STScI archive (lightcurve)
 - Human Cell Atlas data portal (singlecell)

Lane B — Old project / lab / personal pages. Campaigns 2+3's lesson:
modern portals are published-by-design; the stranded pattern now lives
on old project/personal pages (Maddison vintages were the gold there).
Fresh old-site targets, none hunted before:
 - AnAge / Senescence.info (ageing genomics, classic lab site, vintages)
 - Whole Brain Atlas, Harvard AANLIB (1990s neuro atlas site)
 - HyperLEDA (Lyon galaxy catalogue, old lab site)
 - GCVS variable stars (Sternberg, old site)
 - NOW Database of fossil mammals (Helsinki)
 - Human Protein Atlas
 - Neotoma Paleoecology Database
 - Rosetta Project (linguistics/heritage)
 - Animal Diversity Web (Michigan)
 - TreeBASE (phylogenetics alignments)
 - Seshat Databank (historical statistics — in scope per science-first
   correction: historical stats to derive patterns)

Method upgrade (standing, from Campaigns 2+3): Wayback counts filtered
to statuscode:200 BEFORE counting sets; any promising set gets a
sample-download verification in the follow-up pass — raw counts alone
never count as a find (WorldClim 727 -> 1 -> 0 is the cautionary tale).

Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

SITES = [
    # Lane A — fidelity leftovers (label, url, fidelity system or None)
    ("Digital Brain Bank diffusion MRI [fidelity:connectome]", "https://www.digitalbrainbank.org", "connectome"),
    ("Tabula Muris single-cell [fidelity:singlecell]", "https://tabula-muris.ds.czbiohub.org", "singlecell"),
    ("Kepler archive light curves [fidelity:lightcurve]", "https://archive.stsci.edu", "lightcurve"),
    ("Human Cell Atlas data portal [fidelity:singlecell]", "https://data.humancellatlas.org", "singlecell"),
    # Lane B — old project/lab/personal pages
    ("AnAge / Senescence.info ageing (genomics)", "https://genomics.senescence.info", None),
    ("Whole Brain Atlas Harvard AANLIB (neuro, old)", "https://www.med.harvard.edu/aanlib/", None),
    ("HyperLEDA galaxy catalogue (astro, Lyon)", "http://leda.univ-lyon1.fr", None),
    ("GCVS variable stars (astro, Sternberg)", "https://www.sai.msu.su/gcvs/gcvs/", None),
    ("NOW fossil mammals (paleo, Helsinki)", "https://www.nowdatabase.org", None),
    ("Human Protein Atlas (genomics)", "https://www.proteinatlas.org", None),
    ("Neotoma Paleoecology (paleo/geo)", "https://www.neotomadb.org", None),
    ("Rosetta Project (linguistics/heritage)", "https://rosettaproject.org", None),
    ("Animal Diversity Web (ecology, Michigan)", "https://animaldiversity.org", None),
    ("TreeBASE phylogenetics (evolution)", "https://treebase.org", None),
    ("Seshat Databank (historical stats)", "https://seshatdatabank.org", None),
]

def main():
    results = []
    for label, url, system in SITES:
        print(f"\n#### {label} — {url}", flush=True)
        if system:
            card = gh.fidelity_card(system)
            if card:
                print(f"  FIDELITY CARD {system}: RAW={card['RAW']} | UNIT={card['UNIT']} | LABEL_GAP={card['LABEL_GAP']} | ANCHOR={card['ANCHOR']}", flush=True)
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
        ranked = sorted(uniq.values(), key=lambda x: -(gh.gold_score(x["name"], False) + gh.fidelity_score(x["name"], system)))
        wb_all = gh.wayback_inventory(urlparse(url).netloc)
        # standing method upgrade: status-200 only before counting
        wb_data = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"] and str(w.get("status")) == "200"]
        wb_data_all = [w for w in wb_all if gh.is_data(w["url"]) and " " not in w["name"]]
        sets = collections.Counter()
        for w in wb_data:
            p = urlparse(w["url"]).path
            sets[p.rsplit("/", 1)[0] or "/"] += 1
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files | "
              f"wayback: {len(wb_data)} status-200 data files ({len(wb_data_all)} raw)", flush=True)
        for f in ranked[:8]:
            print(f"    [gold {gh.gold_score(f['name'], False):2d} fid {gh.fidelity_score(f['name'], system):2d}] {f['name']}  <- {f['url'][:110]}", flush=True)
        for k, n in sets.most_common(5):
            print(f"    wb200-set {n:4d}  {k}", flush=True)
        results.append({"label": label, "url": url, "system": system,
                        "fidelity_card": gh.fidelity_card(system) if system else None,
                        "pages": len(crawl["pages"]),
                        "unique_data_files": len(uniq),
                        "top": [{"name": f["name"], "url": f["url"], "score": gh.gold_score(f["name"], False), "fidelity": gh.fidelity_score(f["name"], system)} for f in ranked[:20]],
                        "wayback_data_files_status200": len(wb_data),
                        "wayback_data_files_raw": len(wb_data_all),
                        "wayback_sets_status200": dict(sets.most_common(12)),
                        "wayback_top": [{"name": w["name"], "url": w["url"], "first_capture": w["first_capture"], "status": w["status"]} for w in sorted(wb_data, key=lambda x: -gh.gold_score(x["name"], False, True))[:20]]})
    gh.save({"campaign4_more": results}, "campaign4")
    print("\n=== CAMPAIGN4 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | {r['label']}", flush=True)

if __name__ == "__main__":
    main()
