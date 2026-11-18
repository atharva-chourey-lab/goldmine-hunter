#!/usr/bin/env python3
"""Campaign 2 — science + social science.
Doctrine: hunt COMPARABLE SETS that are out there but not integrated.
Each target chosen because (a) old project site, (b) formal archive/release
is partial or versioned, (c) a published benchmark / obvious comparison
is waiting if the set were completed.

Science:
 - PHOIBLE (phoible.org) — phoneme inventories x ~2,186 languages
 - IDS (ids.clld.org) — Intercontinental Dictionary Series wordlists x languages
 - TRY (try-db.org) — plant trait records x species
 - Human Mortality DB (mortality.org) — life tables x country x year x sex [bridge]
Social science:
 - Correlates of War (correlatesofwar.org) — dyad-year panels: war/trade/alliances/diplomacy
 - Polity / Systemic Peace (systemicpeace.org) — regime scores x country-year, versioned
 - Maddison Project (ggdc.net) — historical GDP/pop x country-year, multiple vintages
 - World Values Survey (worldvaluessurvey.org) — survey waves x country
 - UCDP (ucdp.uu.se) — conflict events/deaths x country-year, versioned
 - QoG (qog.pol.gu.se) — Quality of Government compilation x country-year
Run from goldmine-hunter/.
"""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# social-science gold words the v2 packs don't carry — score boost locally
SOC_WORDS = ("census","survey","panel","microdata","election","precinct","constituency",
             "district","polity","democracy","gdp","mortality","fertility","conflict",
             "war","trade","alliance","dyad","regime","governance","values","returns")
def score2(name, in_archive=False, only_wb=False):
    s = gh.gold_score(name, in_archive, only_wb)
    n = name.lower()
    for w in SOC_WORDS:
        if w in n:
            s += 3
    return s

SITES = [
    ("PHOIBLE phoneme inventories (linguistics)", "https://phoible.org"),
    ("IDS dictionary series (linguistics)", "https://ids.clld.org"),
    ("TRY plant traits (ecology)", "https://www.try-db.org"),
    ("Human Mortality Database (demography)", "https://www.mortality.org"),
    ("Correlates of War (IR / social sci)", "https://correlatesofwar.org"),
    ("Systemic Peace / Polity (social sci)", "https://www.systemicpeace.org"),
    ("Maddison Project via GGDC (econ history)", "https://www.ggdc.net"),
    ("World Values Survey (social sci)", "https://www.worldvaluessurvey.org"),
    ("UCDP conflict (social sci)", "https://ucdp.uu.se"),
    ("Quality of Government (social sci)", "https://www.qog.pol.gu.se"),
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
            if f["name"].lower() in gh.IGNORE_NAMES:
                continue
            # drop parser artefacts: names with spaces are text fragments, not files
            if " " in f["name"]:
                continue
            uniq.setdefault(f["name"], f)
        ranked = sorted(uniq.values(), key=lambda x: -score2(x["name"]))
        try:
            wb = gh.wayback_inventory(urlparse(url).netloc)
        except Exception as e:
            print(f"  wayback failed: {e}", flush=True)
            wb = []
        wb_data = [w for w in wb if gh.is_data(w["url"]) and " " not in w["name"]]
        # group wayback into sets by directory
        sets = collections.Counter()
        for w in wb_data:
            p = urlparse(w["url"]).path
            parent = p.rsplit("/", 1)[0] or "/"
            sets[parent] += 1
        print(f"  live: {len(crawl['pages'])} pages, {len(uniq)} unique data files, "
              f"{len(crawl['images'])} images | wayback: {len(wb_data)} archived data files", flush=True)
        for f in ranked[:8]:
            print(f"    [score {score2(f['name']):2d}] {f['name']}  <- {f['url'][:110]}", flush=True)
        for k, n in sets.most_common(5):
            print(f"    wb-set {n:4d}  {k}", flush=True)
        results.append({"label": label, "url": url, "pages": len(crawl["pages"]),
                        "unique_data_files": len(uniq),
                        "top": [{"name": f["name"], "url": f["url"], "score": score2(f["name"])} for f in ranked[:20]],
                        "wayback_data_files": len(wb_data),
                        "wayback_sets": dict(sets.most_common(12)),
                        "wayback_top": [{"name": w["name"], "url": w["url"], "first_capture": w["first_capture"], "status": w["status"]} for w in sorted(wb_data, key=lambda x: -score2(x["name"], False, True))[:20]]})
    gh.save({"campaign2_sci_soc": results}, "campaign2")
    print("\n=== CAMPAIGN2 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files"])):
        print(f"  live {r['unique_data_files']:4d} | wayback {r['wayback_data_files']:5d} | {r['label']}", flush=True)

if __name__ == "__main__":
    main()
