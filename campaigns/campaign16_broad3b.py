#!/usr/bin/env python3
"""Campaign 16 — Broad Wave 3B, GENERATED from the broad niche
registry, ranks 37-45 in registry order, all previously UNFIRED:
concrete-test-ledgers (7), pigment-cross-sections (7),
playbill-programme-archives (7), factory-payroll-wage-books (7),
booth-level-election-gazettes (7), seed-catalogue-varieties (7),
regional-menu-collections (7), borehole-well-logs (6),
sunspot-drawings (6, DRAWINGS angle only — SILSO sunspot-number
v1 was hunted in Campaigns 2-3 and not found; this niche is the
observatory drawing piles, distinct from the SILSO version stack).
Grades are GRADES.md's, fixed before digging, unchanged.

Factory-payroll note: research-tools CUSTODY-1 KILLed this niche
prospectively from its fidelity card (CUSTODY_RESTRICTED cue).
That is treated here as a prior to test against probe evidence,
not as a verdict.

Hosts from the Campaign 16 host-discovery pass (2026-11-18, web
searches using each niche's registry keywords): loose-file leads
first (UCLA obs.astro.ucla.edu sunspot-drawing pages / howard
FTP tree cited in the literature, Clowes Collection technical-
report PDF tree, blplaybills.org independent BL-playbill site,
JCU Pioneer Sugar Mill archive listing), formal/consolidated
systems documented as such (UCI concrete dataset via Datadory,
British Library Research Repository playbill OCR dataset, USDA
Henry G. Gilbert seed catalogues on archive.org, NYBG Mertz,
NYPL What's on the Menu, UNLV Menus: The Art of Dining, USGS
Geolog Locator, Washington Geologic Information Portal, BGS
AGS borehole index, Mount Wilson / KSO CESAR sunspot-drawing
archives, Indian gazettes on archive.org), custody never
circumvented (OPD cross-sections access-on-request, Tate CHSA
in-person, Derbyshire Record Office catalogue-only volumes,
Fulton Bag personnel records restricted for confidentiality).

Method (standing, = Campaigns 6-10): live crawl + Wayback
inventory FILTERED to statuscode:200 BEFORE counting;
whole-domain Wayback only for small hosts; big institutional
domains get crawl-only here + targeted CDX in verify16.py.
Every promising pile is sample-verified in verify16.py.
Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    # 1 — concrete-test-ledgers (7)
    ("concrete-test-ledgers", "Datadory — UCI Concrete Compressive Strength dataset page (1,030 lab records, published)",
     "https://www.datadory.com/datasets/construction-materials/concrete-compressive-strength-dataset", 1, 10, None),
    ("concrete-test-ledgers", "archive.org — Concrete journal 1930-10 (published test tables inside a journal issue, not a lab ledger)",
     "https://archive.org/download/concrete_1930-10_37_4/concrete_1930-10_37_4.pdf", 0, 3, None),
    # 2 — pigment-cross-sections (7)
    ("pigment-cross-sections", "ICCROM Sample Archives — OPD Collection of Cross- and Thin-Sections (15,400 sections, access on request)",
     "https://samplearchives.iccrom.org/oggetti/41651-opd-collection-of-cross-and-thin-sections?i=2", 1, 10, None),
    ("pigment-cross-sections", "Clowes Collection — Notes to the User (technical reports with cross-sections, published catalogue)",
     "https://paintings.theclowescollection.org/notes-to-the-user/", 1, 20, "paintings.theclowescollection.org"),
    ("pigment-cross-sections", "Rijksmuseum Paint Sample Database — MW2016 description (psa.rijksmuseum.nl, login-gated interface)",
     "https://mw2016.museumsandtheweb.com/glami/rijksmuseum-paint-sample-database-2/index.html", 1, 5, None),
    ("pigment-cross-sections", "Tate CHSA — RICHeS page (16,000+ cross-sections, physical+digital, in-person/request access)",
     "https://www.riches.ukri.org/funding/riches-investments/tranche-1-collections/establishing-tates-conservation-and-heritage-science-archive-chsa/", 1, 5, None),
    # 3 — playbill-programme-archives (7)
    ("playbill-programme-archives", "British Library Research Repository — Theatrical playbills OCR dataset (264 vols, DOI 10.21250/pb2)",
     "https://bl.iro.bl.uk/entities/product/3876be77-0625-4234-a6bd-2fac173a0712", 1, 10, None),
    ("playbill-programme-archives", "blplaybills.org — independent site over BL open playbill data (84,000+ bills)",
     "https://www.blplaybills.org/", 1, 20, "blplaybills.org"),
    ("playbill-programme-archives", "archive.org — Playbill, Plymouth Theatre 'The Happy Time' 1951 (single item)",
     "https://archive.org/details/playbill_the_plymouth_theatre_the_happy_time", 1, 5, None),
    ("playbill-programme-archives", "British Library libguide — Rare Books: Playbills (digitised set + microfilm note)",
     "https://bl.libguides.com/reference-services/rare-books/playbills", 1, 5, None),
    # 4 — factory-payroll-wage-books (7) — CUSTODY-1 prior: KILL / CUSTODY_RESTRICTED (card text only)
    ("factory-payroll-wage-books", "JCU Library Archives — Pioneer Sugar Mill Archive (wages books PMR/WB/1-13 listed, physical location)",
     "https://libserver.jcu.edu.au/specials/Archives/pioneer.html", 1, 10, "libserver.jcu.edu.au"),
    ("factory-payroll-wage-books", "Derbyshire Record Office CalmView — Mill hands weekly wages book D6948/E/9/4 (catalogue record, 1 volume)",
     "https://calmview.derbyshire.gov.uk/calmview/Record.aspx?src=CalmView.Catalog&id=D6948%2FE%2F9%2F4", 1, 5, None),
    ("factory-payroll-wage-books", "Georgia Tech — Fulton Bag and Cotton Mills history/records (payroll + 50k personnel cards, restricted)",
     "https://exhibit-archive.library.gatech.edu/fulton_bag/history.html", 1, 10, "exhibit-archive.library.gatech.edu"),
    # 5 — booth-level-election-gazettes (7)
    ("booth-level-election-gazettes", "archive.org — Mysore Gazette 1948 text PDF (polling stations/booths statement inside)",
     "https://archive.org/download/karnataka-state-archives-2026-348623/362_PART_2_5_3_JULY_DEC_1948_409_text.pdf", 0, 3, None),
    ("booth-level-election-gazettes", "archive.org — Himachal Pradesh Gazette 1986-09-13 text PDF (election petition, constituency totals)",
     "https://archive.org/download/in.gazette.himachalarchive.1986-09-13.3691/3691_text.pdf", 0, 3, None),
    ("booth-level-election-gazettes", "archive.org — Gazette of India 1953 election notification PDF",
     "https://archive.org/download/in.gazette.e.1953.219/E-2260-1953-0009-104687.pdf", 0, 3, None),
    # 6 — seed-catalogue-varieties (7)
    ("seed-catalogue-varieties", "NYBG Mertz Library — Nursery and Seed Catalogs guide (58,000 items catalogued, 1,400 pre-1923 digitised)",
     "https://libguides.nybg.org/c.php?g=655017&", 1, 10, None),
    ("seed-catalogue-varieties", "archive.org — 1926 catalogue, Northern Seed & Nursery Co. (USDA Gilbert collection item)",
     "https://archive.org/download/CAT31322813/CAT31322813_bw.pdf", 0, 3, None),
    ("seed-catalogue-varieties", "archive.org — 1906 seed catalogue, Nebraska Seed Co. (USDA Gilbert collection item)",
     "https://archive.org/download/CAT31288032/CAT31288032_bw.pdf", 0, 3, None),
    # 7 — regional-menu-collections (7)
    ("regional-menu-collections", "UNLV Special Collections — Bohn-Bettoni menu item (men000606, Menus: The Art of Dining)",
     "https://special.library.unlv.edu/ark%3A/62930/d1br8mz4h", 1, 10, None),
    ("regional-menu-collections", "UNLV — Bohn-Bettoni Menu Collection finding aid PDF (MS-00793, 12.68 cu ft physical)",
     "https://special.library.unlv.edu/sites/default/files/finding-aids/MS-00793.pdf", 0, 3, None),
    ("regional-menu-collections", "Curating Menus — NYPL What's on the Menu data dictionary (CSV export at menus.nypl.org/data)",
     "http://curatingmenus.org/data_dictionary/", 1, 10, None),
    # 8 — borehole-well-logs (6)
    ("borehole-well-logs", "USGS Geolog Locator page (7,000+ digital borehole geophysical logs, formal database)",
     "https://www.USGS.gov/centers/oklahoma-texas-water-science-center/science/geolog-locator", 1, 10, None),
    ("borehole-well-logs", "Washington Geologic Information Portal (subsurface database, formal portal)",
     "https://dnr.wa.gov/washington-geological-survey/publications-and-data/geologic-information-portal", 1, 10, None),
    ("borehole-well-logs", "TechnicalGIS — BGS AGS borehole index worked example (OGC API + AGS export, formal BGS service)",
     "https://ns2.technicalgis.com/tutorials/read-validate-ags4-python/", 1, 5, None),
    # 9 — sunspot-drawings (6) — DRAWINGS angle only, NOT the SILSO number series
    ("sunspot-drawings", "Mount Wilson Observatory — Solar Observing (daily sunspot drawing archive since 1917)",
     "https://www.mtwilson.edu/solar-observing/", 1, 10, None),
    ("sunspot-drawings", "UCLA obs.astro.ucla.edu — Historical Sunspot Drawing Resource Page (20th-century observers)",
     "http://obs.astro.ucla.edu/resource3.html", 1, 15, "obs.astro.ucla.edu"),
    ("sunspot-drawings", "UCLA obs.astro.ucla.edu — Mt Wilson 150-Foot Tower Sunspot Drawing page",
     "http://obs.astro.ucla.edu/150_draw.html", 1, 10, None),
    ("sunspot-drawings", "Carnegie Science — Object 26 Sunspot Drawings (Plate Archives, digitised via MWO site)",
     "https://carnegiescience.edu/news/object-26-sunspot-drawings", 1, 5, None),
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
              + (" [whole-domain skipped — targeted checks in verify16]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign16_broad3b": results}, "campaign16")
    print("\n=== CAMPAIGN16 BROAD3B SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
