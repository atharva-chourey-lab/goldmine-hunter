#!/usr/bin/env python3
"""Campaign 8 — Mammal Wave 2, GENERATED from the recalibrated
mammal-grain registry (Atharva, 2026-11-18: autonomous). Fires the
effective head of the mammal queue after Campaign 7's cuts:
guard-hair-scale-casts (9), then the 8s — koala-fingerprints,
dog-nose-prints, plaster-track-cast-collections,
elephant-footprint-age, right-whale-callosity-patterns,
manatee-photo-id-scars. Grades are GRADES.md's, unchanged.

Hosts come from the Campaign 8 host-discovery pass (three parallel
searches, 2026-11-18): loose-file leads first (CMU personal hair
pages, Save the Manatee Club archive subdomain, EBRWS uploads,
Utah Valdés records), custody/platform/paper systems documented
as such, never circumvented (MIPS, NARWC consortium, ARWPIC,
ATE Access databases, commercial nose-ID apps).

Method (standing, = Campaign 7): live crawl + Wayback inventory
FILTERED to statuscode:200 BEFORE counting; whole-domain Wayback
only for small hosts; big institutional domains get crawl-only
here + targeted CDX in verify8.py. Every promising pile is
sample-verified in verify8.py. Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

# (niche, label, url, depth, max_pages, wayback_domain_or_None)
SITES = [
    # 1 — guard-hair-scale-casts (9)
    ("guard-hair-scale-casts", "CMU personal faculty hair-ID pages (Swanson)",
     "http://people.se.cmich.edu/swans1bj/hair%20id/species.html", 1, 25, None),
    ("guard-hair-scale-casts", "Texas Tech NSRL Special Publications (Texas hair atlas SP-055)",
     "https://www.depts.ttu.edu/nsrl/publications/special-publications.php", 1, 10, None),
    ("guard-hair-scale-casts", "Landcare Research NZ hair factsheets (Brunner & Coman web afterlife)",
     "https://www.landcareresearch.co.nz/tools-and-resources/identification/hair-sample-identification-and-factsheets", 1, 15, None),
    ("guard-hair-scale-casts", "Hair Atlas HU (Toth Central European atlas companion)",
     "http://www.hairatlas.hu/index.php?m2=species", 1, 10, "hairatlas.hu"),
    # 2 — koala-fingerprints (8)
    ("koala-fingerprints", "Academia.edu — Henneberg et al. fingerprinting paper (platform)",
     "https://www.academia.edu/27860920/Fingerprinting_a_chimpanzee_and_a_koala_Animal_dermatoglyphics_can_resemble_human_ones_w_", 1, 5, None),
    ("koala-fingerprints", "Hawkeye Forensic — koala fingerprint summary (secondary)",
     "https://hawkeyeforensic.com/fingerprint-similarity-human-koala-and-chimpanze/", 1, 5, None),
    # 3 — dog-nose-prints (8)
    ("dog-nose-prints", "National Purebred Dog Day — CKC nose-print history (microfiche evidence)",
     "https://nationalpurebreddogday.com/the-dogs-version-of-the-fingerprint/", 1, 5, None),
    ("dog-nose-prints", "PMC — Korean dog nose-pattern viability study (dataset described, not deposited)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC8697952/", 1, 5, None),
    # 4 — plaster-track-cast-collections (8)
    ("plaster-track-cast-collections", "Idaho Virtual Museum (IMNH footprint virtualization)",
     "https://virtual.imnh.iri.isu.edu/Home/Sources", 1, 15, None),
    ("plaster-track-cast-collections", "Smithsonian NMNH Paleobiology IPT (database/formal archive check)",
     "https://collections.nmnh.si.edu/ipt/eml.do?r=nmnh_paleo_dwc-a", 1, 5, None),
    # 5 — elephant-footprint-age (8)
    ("elephant-footprint-age", "ElephantVoices — ATE science/ethogram (Amboseli custody surface)",
     "https://www.elephantvoices.org/the-science-behind-the-elephant-ethogram", 1, 10, None),
    ("elephant-footprint-age", "Elephants for Africa — FIT project (Botswana)",
     "https://www.elephantsforafrica.org/", 1, 10, "elephantsforafrica.org"),
    # 6 — right-whale-callosity-patterns (8)
    ("right-whale-callosity-patterns", "Encounter Bay Right Whale Study (small-project catalogue PDFs)",
     "https://www.ebrws.com.au/", 1, 15, "ebrws.com.au"),
    ("right-whale-callosity-patterns", "Univ. of Utah Marriott Library — Right Whale Collection (Valdes 1970-2004)",
     "https://collections.lib.utah.edu/search?facet_setname_s=%22uum_rwc%22", 1, 10, None),
    ("right-whale-callosity-patterns", "NARWC — photo-identification page (consortium custody)",
     "https://www.narwc.org/photo-identification.html", 1, 5, None),
    ("right-whale-callosity-patterns", "ARWPIC — Australasian catalogue platform",
     "https://data.marinemammals.gov.au/arwpic/index.php?route=common/home", 1, 5, None),
    # 7 — manatee-photo-id-scars (8)
    ("manatee-photo-id-scars", "Save the Manatee Club ARCHIVE subdomain (scar sheets)",
     "https://www.savethemanatee-archive.org/", 1, 15, "savethemanatee-archive.org"),
    ("manatee-photo-id-scars", "Save the Manatee Club main site",
     "https://savethemanatee.org/", 1, 10, "savethemanatee.org"),
    ("manatee-photo-id-scars", "FWC manatee research page (MIPS agency surface)",
     "https://myfwc.com/research/manatee/research/", 1, 5, None),
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
              + (" [whole-domain skipped — targeted checks in verify8]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign8_mammal2": results}, "campaign8")
    print("\n=== CAMPAIGN8 MAMMAL2 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
