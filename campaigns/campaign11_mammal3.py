#!/usr/bin/env python3
"""Campaign 11 — Mammal Wave 3, GENERATED from the mammal-grain
registry (Atharva, 2026-11-18: "run a ton of more waves").
Fires the unfired 8/10 band in registry order:
rhino-ear-notch-horn-profiles, pinniped-pelage-patterns,
tiger-stripe-catalogues, leopard-jaguar-rosettes,
zebra-stripe-patterns, giraffe-coat-patterns,
tooth-wear-age-charts, cementum-annuli-tooth-archives,
primate-face-pattern-archives. Grades are GRADES.md's, unchanged.

Hosts from the Campaign 11 discovery pass (2026-11-18 searches):
loose-file leads first (Conservation Research Ltd's ExtractCompare
demo zips — tiger/leopard/zebra/giraffe pages untouched since
2010-12; a monk-seal programme report PDF on an unrelated
freqstats host; agency tooth-wear PDFs; a Matson cementum report
PDF on a legislature host), custody/platform systems documented
as such, never circumvented (RhODIS forensic law-enforcement
database, India's NTCA/WII national tiger archive + MSTrIPES,
Wildbook/GiraffeSpotter, Matson's commercial lab, NOAA InPort
monk-seal database with "No Distributions available", JGI's
Gombe archive).

SAFETY (standing, this wave especially): rhino and tiger are
poaching-sensitive. No sensitive location data is collected or
published; researcher-only / restricted systems are documented
as custody only, never scraped or circumvented.

Method (standing, = Campaigns 7-8): live crawl + Wayback
inventory FILTERED to statuscode:200 BEFORE counting; whole-
domain Wayback only for small hosts; big institutional domains
get crawl-only here + targeted checks in verify11.py. Every
promising pile is sample-verified in verify11.py. Run from
goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    # 1 — rhino-ear-notch-horn-profiles (8) — custody-sensitive
    ("rhino-ear-notch-horn-profiles", "Save the Rhino — how do you identify black rhinos? (Ezemvelo notch system explainer)",
     "https://www.savetherhino.org/africa/south-africa/how-do-you-identify-black-rhinos/", 1, 5, None),
    ("rhino-ear-notch-horn-profiles", "International Rhino Foundation — RhODIS genetics page (forensic anchor, custody)",
     "https://rhinos.org/blog/genetic-factors-to-improve-rhino-management/", 1, 5, None),
    ("rhino-ear-notch-horn-profiles", "RhODIS home (rhodis.co.za — forensic system surface check)",
     "http://rhodis.co.za/", 1, 5, "rhodis.co.za"),
    # 2 — pinniped-pelage-patterns (8)
    ("pinniped-pelage-patterns", "MDPI Sensors — SealID paper (Saimaa, 57 seals / 2,080 images, DOI dataset)",
     "https://www.mdpi.com/1424-8220/22/19/7602", 1, 5, None),
    ("pinniped-pelage-patterns", "Monk Seal Conservation Program Cabo Blanco — annual report PDF host (freqstats.marineland.fr)",
     "http://freqstats.marineland.fr/dl/Annual-Report-2017-2018-Mediterranean-monk-seal-Program.pdf", 0, 3, "freqstats.marineland.fr"),
    ("pinniped-pelage-patterns", "NOAA InPort — Hawaiian Monk Seal Photo ID Database (custody; no distributions)",
     "https://www.fisheries.noaa.gov/inport/item/28581", 1, 5, None),
    # 3 — tiger-stripe-catalogues (8) — poaching-sensitive, custody
    ("tiger-stripe-catalogues", "Conservation Research Ltd — ExtractCompare Tigers page (demo folders + Access DB, 2010)",
     "https://www.conservationresearch.org.uk/Home/ExtractCompare/Tigers.html", 1, 10, "conservationresearch.org.uk"),
    ("tiger-stripe-catalogues", "Wildlife Institute of India — MSTrIPES page (national system, custody)",
     "https://wii.gov.in/mstripes", 1, 5, None),
    # 4 — leopard-jaguar-rosettes (8)
    ("leopard-jaguar-rosettes", "Conservation Research Ltd — ExtractCompare leopard page (demo folders, 2010)",
     "https://www.conservationresearch.org.uk/Home/ExtractCompare/leopard.html", 1, 10, None),
    ("leopard-jaguar-rosettes", "Conservation Research Ltd — ExtractCompare clouded leopard page (demo, 2012)",
     "https://www.conservationresearch.org.uk/Home/ExtractCompare/cloudedLeopard.html", 1, 10, None),
    # 5 — zebra-stripe-patterns (8)
    ("zebra-stripe-patterns", "LILA BC — Great Zebra and Giraffe Count and ID dataset page (formal repository)",
     "https://lila.science/datasets/great-zebra-giraffe-id", 1, 10, None),
    ("zebra-stripe-patterns", "Conservation Research Ltd — ExtractCompare index (zebra system listed)",
     "https://www.conservationresearch.org.uk/Home/ExtractCompare/index.html", 1, 10, None),
    # 6 — giraffe-coat-patterns (8)
    ("giraffe-coat-patterns", "GiraffeSpotter (Wildbook platform — custody by design)",
     "https://giraffespotter.org/", 1, 10, "giraffespotter.org"),
    ("giraffe-coat-patterns", "Conservation Research Ltd — ExtractCompare giraffe page if present (via index crawl)",
     "https://www.conservationresearch.org.uk/Home/ExtractCompare/Giraffe.html", 1, 5, None),
    # 7 — tooth-wear-age-charts (8)
    ("tooth-wear-age-charts", "Vista Mountain WMA — TPWD Age Determination guide, HTML afterlife (Cain & Wallace 2003)",
     "http://vistamountainwma.org/news/age-determination-of-white-tailed-deer/", 1, 10, "vistamountainwma.org"),
    ("tooth-wear-age-charts", "East Foundation — Foley et al. known-age accuracy paper (the comparison, published)",
     "https://eastfoundation.net/wp-content/uploads/2024/09/wr21050.pdf", 0, 3, None),
    ("tooth-wear-age-charts", "Boone & Crockett Fair Chase — Deer Ages / dentition article PDF (Severinghaus tradition)",
     "https://aws.boone-crockett.org/s3fs-public/atoms/files/FC_Summer2008_DeerAges.pdf", 0, 3, None),
    # 8 — cementum-annuli-tooth-archives (8)
    ("cementum-annuli-tooth-archives", "Matson's Laboratory home (commercial ageing lab, since 1969)",
     "https://www.matsonslab.com/", 1, 15, "matsonslab.com"),
    ("cementum-annuli-tooth-archives", "Minnesota Legislature host — Matson cementum age report PDF for MN DNR (2,448 deer teeth, 2006)",
     "https://www.leg.mn.gov/docs/2013/other/C130010.pdf", 0, 3, None),
    ("cementum-annuli-tooth-archives", "ADF&G — How old is my bear? cementum explainer (agency lab history)",
     "https://www.adfg.alaska.gov/index.cfm?adfg=wildlifenews.view_article&articles_id=4137", 1, 5, None),
    # 9 — primate-face-pattern-archives (8)
    ("primate-face-pattern-archives", "Jane Goodall Institute news — ChimpFace / Gombe AI archive article (site custody surface)",
     "https://news.janegoodall.org/2018/07/29/the-future-using-ai-in-gombe/", 1, 5, None),
    ("primate-face-pattern-archives", "arXiv — Face Recognition: Primates in the Wild (ChimpFace 5,559 imgs / 90 indiv. dataset paper)",
     "https://arxiv.org/abs/1804.08790", 1, 5, None),
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
              + (" [whole-domain skipped — targeted checks in verify11]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign11_mammal3": results}, "campaign11")
    print("\n=== CAMPAIGN11 MAMMAL3 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
