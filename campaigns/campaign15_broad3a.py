#!/usr/bin/env python3
"""Campaign 15 — Broad Wave 3A, GENERATED from the broad niche
registry (ranks 28-36, all score 7, all previously UNFIRED):
bat-echolocation-libraries, butterfly-wing-drawers,
snake-venom-spectra, heritage-tree-ring-cores,
phage-plaque-hostrange, orthodontic-dental-casts,
lunar-occultation-timings, observatory-plate-logbooks,
early-radio-astronomy-charts.
Grades are GRADES.md's, fixed before digging, unchanged.

Hosts from the Campaign 15 host-discovery pass (2026-11-18,
web searches using each niche's registry keywords):
loose-file leads first (avisoft.com/batcalls vendor lure
library, animalsoundlabs.pl mirror, phage.org — the old
Bacteriophage Ecology Group site carrying the 2nd-edition
book tables, lunar-occultations.com IOTA section site,
bat-sound-database.com personal site), formal/consolidated
systems documented as such (ChiroVox, TERN, Morcegoteca/
PPBio, LepiVerse/GBIF via Zenodo BioCosmos, BAMONA,
Zenodo/PRIDE/MassIVE venom deposits, Historic England +
ADS VAG dendro database, d'Hérelle Center catalogue,
AAOF Legacy Collection, VizieR VI/132C, APPLAUSE /
plate-archive.org, WFPDB VizieR VI/90, Manchester Library
Jodrell Bank logbook digitisation), custody never
circumvented (ChiroVox restricted-call permissions,
AAOF/VizieR/APPLAUSE are interfaces, not file piles).

Method (standing, = Campaigns 6-10): live crawl + Wayback
inventory FILTERED to statuscode:200 BEFORE counting;
whole-domain Wayback only for small hosts; big institutional
domains get crawl-only here + targeted CDX in verify15.py.
Every promising pile is sample-verified in verify15.py.
Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    # 1 — bat-echolocation-libraries (7)
    ("bat-echolocation-libraries", "Avisoft batcalls — European bat lure-call library (vendor site, wav + zip)",
     "http://www.avisoft.com/batcalls/", 1, 20, "avisoft.com"),
    ("bat-echolocation-libraries", "Animal Sound Labs — bat calls mirror/expanded table (animalsoundlabs.pl)",
     "https://animalsoundlabs.pl/en/bat-calls/", 1, 10, "animalsoundlabs.pl"),
    ("bat-echolocation-libraries", "ChiroVox — the bat call library (formal platform, help/access page)",
     "https://www.chirovox.org/help.php", 1, 10, None),
    ("bat-echolocation-libraries", "Morcegoteca — PPBio/INPA bat ultrasound library (formal programme site)",
     "https://ppbio.inpa.gov.br/en/Bat_Library", 1, 15, None),
    ("bat-echolocation-libraries", "Bat Sound Database — personal European social-call site",
     "https://www.bat-sound-database.com/about", 1, 10, "bat-sound-database.com"),
    ("bat-echolocation-libraries", "TERN — Australian Bat Acoustic Data Collection record (formal portal)",
     "https://portal.tern.org.au/metadata/TERN/9c47fe65-86c0-4cbd-bb28-73d30c3fd6c1", 1, 5, None),
    # 2 — butterfly-wing-drawers (7)
    ("butterfly-wing-drawers", "BioCosmos / LepiVerse image occurrences — Zenodo record (GBIF-aggregated, formal)",
     "http://zenodo.org/records/23840624", 1, 5, None),
    ("butterfly-wing-drawers", "AfricaMuseum — Lepidoptera digitisation / DoeDat transcription project page",
     "https://www.africamuseum.be/en/research/news/citizen_science_butterfly_collection", 1, 10, None),
    ("butterfly-wing-drawers", "BAMONA image gallery (field-photo platform, not specimen drawers)",
     "https://www.butterfliesandmoths.org/gallery?species_type=0&stage=adult&page=58", 1, 10, None),
    # 3 — snake-venom-spectra (7)
    ("snake-venom-spectra", "Zenodo — Vipera berus venom proteomics, sex variation (formal deposit)",
     "https://zenodo.org/records/16418915", 1, 5, None),
    ("snake-venom-spectra", "Zenodo — Vipera monticola 3 subspecies venom proteomics (formal deposit)",
     "https://zenodo.org/records/11103867", 1, 5, None),
    ("snake-venom-spectra", "Zenodo — V. ammodytes island/mainland populations venom proteomics (formal deposit)",
     "https://zenodo.org/records/11482457", 1, 5, None),
    ("snake-venom-spectra", "PRIDE PXD016503 — snake venom protein structures (formal archive)",
     "https://www.ebi.ac.uk/pride/archive/projects/PXD016503", 1, 5, None),
    ("snake-venom-spectra", "MassIVE — Vipera/Macrovipera/Daboia Turkiye venom dataset (formal archive)",
     "https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?task=f8872b47554a4e588fc0580dd4bda293", 1, 5, None),
    # 4 — heritage-tree-ring-cores (7)
    ("heritage-tree-ring-cores", "Historic England — tree-ring report 96/2022, Stratford timbers (formal report series)",
     "https://historicengland.org.uk/research/results/reports/96-2022", 1, 10, None),
    ("heritage-tree-ring-cores", "ADS VAG Dendrochronology Database — Stokesay Castle record (formal database)",
     "https://archaeologydataservice.ac.uk/archives/view/vag_dendro/full_record.cfm?id=923", 1, 10, None),
    ("heritage-tree-ring-cores", "ADS VAG Dendrochronology Database — Bodleian Library record (formal database)",
     "https://archaeologydataservice.ac.uk/archives/view/vag_dendro/full_record.cfm?id=1100", 1, 10, None),
    # 5 — phage-plaque-hostrange (7)
    ("phage-plaque-hostrange", "phage.org — Bacteriophage Names 2000 host list (old BEG site)",
     "http://www.phage.org/names/2000/names_host.htm", 1, 20, "phage.org"),
    ("phage-plaque-hostrange", "phage.org — Bacteriophages 2nd ed. Table 2-5 host range PDF (book table file)",
     "http://www.phage.org/images/thebacteriophages/0020_table_005.pdf", 0, 3, None),
    ("phage-plaque-hostrange", "Felix d'Herelle Reference Center catalogue — phage.ulaval.ca (formal DB interface)",
     "https://www.phage.ulaval.ca/en/rechercher-catalogue-phages", 1, 10, None),
    # 6 — orthodontic-dental-casts (7)
    ("orthodontic-dental-casts", "AAOF Craniofacial Growth Legacy Collection home (formal consolidated archive — the excluded growth centres)",
     "https://www.aaoflegacycollection.org/aaof_home.html", 1, 15, None),
    ("orthodontic-dental-casts", "CRIL — 2D Longitudinal Growth Study / CGCS page (formal consortium)",
     "https://www.cril.org/home/2d-longitudinal-growth-study-2/", 1, 10, None),
    # 7 — lunar-occultation-timings (7)
    ("lunar-occultation-timings", "lunar-occultations.com — IOTA 2008 archive format page (section site)",
     "http://www.lunar-occultations.com/iota/2008archiveformat.htm", 1, 20, "lunar-occultations.com"),
    ("lunar-occultation-timings", "VizieR VI/132C Lunar Occultation Archive — GAVO record (formal archive, re-reduced)",
     "https://dc.g-vo.org/rr/q/lp/custom/CDS.VizieR/VI/132C", 1, 5, None),
    ("lunar-occultation-timings", "IOTA RASC 2026 lunar section PDF (occultations.org, formal)",
     "https://occultations.org/publications/rasc/2026/lunar26.pdf", 0, 3, None),
    # 8 — observatory-plate-logbooks (7)
    ("observatory-plate-logbooks", "APPLAUSE DR3 metadata — plate-archive.org (formal plate archive)",
     "https://www.plate-archive.org/metadata/applause_dr3/", 1, 10, None),
    ("observatory-plate-logbooks", "APPLAUSE DR3 documentation — plate-archive.org (formal)",
     "https://www.plate-archive.org/cms/documentation/dr3/", 1, 10, None),
    ("observatory-plate-logbooks", "WFPDB VizieR VI/90 ReadMe (formal plate-metadata database)",
     "https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/VI/90?format=html&tex=true", 1, 5, None),
    ("observatory-plate-logbooks", "AIP APPLAUSE project page (formal)",
     "http://www.aip.de/en/research/projects/applause/", 1, 5, None),
    # 9 — early-radio-astronomy-charts (7)
    ("early-radio-astronomy-charts", "Manchester Library — Jodrell Bank logbooks digitisation project (formal)",
     "https://www.library.manchester.ac.uk/services/digitisation-services/projects/jodrell-bank-logbooks/", 1, 10, None),
    ("early-radio-astronomy-charts", "Jodrell Bank history — early space tracking (jb.man.ac.uk, published history)",
     "http://www.jb.man.ac.uk/history/tracking/part1.html", 1, 10, None),
    ("early-radio-astronomy-charts", "Big Ear / NAAPO — Cosmic Search 13, Reber first radio maps (bigear.org PDF)",
     "https://www.bigear.org/CSMO/PDF/CS13/cs13p14.pdf", 0, 3, None),
    ("early-radio-astronomy-charts", "Bell Burnell — Cosmic Search pulsar account, pen-chart analysis (magonia PDF)",
     "https://magonia.com/wp-content/uploads/2016/10/cosmic-search-jocelyn-bell.pdf", 0, 3, None),
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
              + (" [whole-domain skipped — targeted checks in verify15]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign15_broad3a": results}, "campaign15")
    print("\n=== CAMPAIGN15 BROAD3A SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
