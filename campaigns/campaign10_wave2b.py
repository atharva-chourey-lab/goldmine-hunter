#!/usr/bin/env python3
"""Campaign 10 — Broad Wave 2B, GENERATED from the broad niche
registry (Atharva, 2026-11-18: "run a ton of more waves").
Fires the next ten unfired broad-registry 8/10 niches, in the
order given: glacier-repeat-photos, paper-seismograms,
moonwatch-satellite-cards, steam-engine-indicator-cards,
dye-sample-books, endangered-language-tape-shelves,
dialect-survey-recordings, commodity-price-currents,
fire-insurance-plans, photo-finish-film-strips.
Grades are GRADES.md's, fixed before digging, unchanged.

Hosts from the Campaign 10 host-discovery pass (2026-11-18,
web searches): loose-file leads first (gletschervergleiche.ch
personal repeat-photo site, LAP's old UGA Data Download Center
directory listing, INGV storing.ingv.it EuroSeismos static
pages, AIATSIS finding-aid PDF tree, archive.org price-current
items, Rolls-Royce experimental archive), formal/consolidated
systems documented as such (NSIDC/USGS glacier collections,
SISMOS registration service, PARADISEC, BL Sounds, LAC Goad
digitisation), custody never circumvented (SISMOS 600-dpi
registration tiers, AIATSIS community permissions).

Method (standing, = Campaigns 6-8): live crawl + Wayback
inventory FILTERED to statuscode:200 BEFORE counting;
whole-domain Wayback only for small hosts; big institutional
domains get crawl-only here + targeted CDX in verify10.py.
Every promising pile is sample-verified in verify10.py.
Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    # 1 — glacier-repeat-photos (8)
    ("glacier-repeat-photos", "SwissGlaciers / gletschervergleiche.ch (personal repeat-photo site)",
     "https://gletschervergleiche.ch/pages/ImageCompare.aspx?Id=6", 1, 25, "gletschervergleiche.ch"),
    ("glacier-repeat-photos", "NSIDC glacier photographs announcement (formal collection surface)",
     "https://nsidc.org/data/user-resources/data-announcements/glacier-photographs-past-and-present", 1, 10, None),
    ("glacier-repeat-photos", "USGS Repeat Photography Project (formal)",
     "https://www.usgs.gov/centers/norock/science/repeat-photography-project?qt-science_center_objects=0", 1, 10, None),
    # 2 — paper-seismograms (8)
    ("paper-seismograms", "INGV EuroSeismos static collection pages (storing.ingv.it)",
     "http://storing.ingv.it/es_web/Data/Collection.htm", 1, 25, "storing.ingv.it"),
    ("paper-seismograms", "INGV SISMOS Seismogram Request 2.0 (registration-tier custody surface)",
     "http://seismogramrequest.rm.ingv.it", 1, 5, None),
    ("paper-seismograms", "Mendeley Data — Romanian EUROSEISMOS seismograms (formal deposit)",
     "https://data.mendeley.com/datasets/gvxmng6644/2", 1, 5, None),
    # 3 — moonwatch-satellite-cards (8)
    ("moonwatch-satellite-cards", "Smithsonian Archives — Moonwatch Division records page (RU 255)",
     "https://siarchives.si.edu/collections/siris_arc_216819", 1, 10, None),
    ("moonwatch-satellite-cards", "NSIDC NOAA IGY Satellite Report No.4 PDF (Moonwatch Catalogue inside)",
     "https://noaadata.apps.nsidc.org/NOAA/G02201/IPY_Pub_017_20100728/DAHLI_IPY017_0387.pdf", 0, 3, None),
    # 4 — steam-engine-indicator-cards (8)
    ("steam-engine-indicator-cards", "Science Museum Group — indicator diagram object",
     "https://collection.sciencemuseumgroup.org.uk/objects/co51466/indicator-diagram", 1, 10, None),
    ("steam-engine-indicator-cards", "Rolls-Royce Experimental Archives — Box 52 (indicator-card orders/scans)",
     "https://archive.rollsroyces.org/boxes/experimental/ExFiles_bck_Box_sp_52_bck_1/", 1, 10, None),
    ("steam-engine-indicator-cards", "Smithsonian NMAH — Lippincott indicator (record cards in box)",
     "https://americanhistory.si.edu/collections/object/nmah_847439", 1, 5, None),
    # 5 — dye-sample-books (8)
    ("dye-sample-books", "ETH Truempy print-sample catalog (truempy-druckmuster.ethz.ch)",
     "https://truempy-druckmuster.ethz.ch/en", 1, 20, "truempy-druckmuster.ethz.ch"),
    ("dye-sample-books", "ETH e-heritage — Truempy online catalog announcement",
     "https://etheritage.ethz.ch/2024/11/15/chemische-farbenpracht-a-j-truempys-stoffmuster-als-onlinekatalog/?lang=en", 1, 5, None),
    ("dye-sample-books", "Yale — Koechlin & Freres sample books catalogue record (2 vols, thousands of swatches)",
     "https://search.library.yale.edu/archives/13876265", 1, 5, None),
    # 6 — endangered-language-tape-shelves (8)
    ("endangered-language-tape-shelves", "AIATSIS collection finding aids index",
     "https://aiatsis.gov.au/research/guides-and-resources/collection-finding-aids", 1, 15, None),
    ("endangered-language-tape-shelves", "PARADISEC catalog (formal archive surface)",
     "https://catalog.paradisec.org.au/", 1, 10, None),
    ("endangered-language-tape-shelves", "Alaska Native Language Archive (UAF)",
     "https://www.uaf.edu/anla/", 1, 10, None),
    # 7 — dialect-survey-recordings (8)
    ("dialect-survey-recordings", "Linguistic Atlas Project Data Download Center (lap.uga.edu old site)",
     "https://www.lap.uga.edu/Site/DDC.html", 1, 25, "lap.uga.edu"),
    ("dialect-survey-recordings", "British Library Sound and Vision (SED surface, formal)",
     "https://www.bl.uk/collection/sound-and-vision", 1, 10, None),
    ("dialect-survey-recordings", "Leeds LAVC — SED gramophone disc recordings record",
     "https://explore.library.leeds.ac.uk/special-collections-explore/414940", 1, 5, None),
    # 8 — commodity-price-currents (8)
    ("commodity-price-currents", "archive.org — Toronto Trade Circular and Prices Current (item files)",
     "https://archive.org/details/torontotradecirc00unse", 1, 5, None),
    ("commodity-price-currents", "archive.org — British Packet and Argentine News 1845-10-04 (Prices Current inside)",
     "https://archive.org/details/BNA_S001219212_18451004N0998", 1, 5, None),
    # 9 — fire-insurance-plans (8)
    ("fire-insurance-plans", "Library and Archives Canada — Goad Montreal Vol V record (digitised sheets)",
     "https://recherche-collection-search.bac-lac.gc.ca/eng/home/record?app=fonandcol&IdNumber=3821547", 1, 5, None),
    ("fire-insurance-plans", "UCalgary libguide — Calgary Fire Insurance Plans inventory",
     "https://libguides.ucalgary.ca/c.php?g=740062&p=5339528", 1, 10, None),
    ("fire-insurance-plans", "Goad's Guide — collections & copyright page (househistories.ca)",
     "https://www.househistories.ca/goads-guide-collections", 1, 5, None),
    # 10 — photo-finish-film-strips (8)
    ("photo-finish-film-strips", "LA32 Games — First Olympic Photo Finish (1932 Kirby camera account)",
     "https://la32games.substack.com/p/the-first-olympic-photo-finish", 1, 5, None),
    ("photo-finish-film-strips", "Weebly — Photo Finish PDF (secondary compilation)",
     "https://licksmacenre.weebly.com/uploads/1/4/8/7/148708983/photo-finish.pdf", 0, 3, None),
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
              + (" [whole-domain skipped — targeted checks in verify10]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign10_wave2b": results}, "campaign10")
    print("\n=== CAMPAIGN10 WAVE2B SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
