#!/usr/bin/env python3
"""Campaign 13 — Mammal Wave 5, GENERATED from the mammal-grain
registry's 7/10 batch (part 2), in registry order (ranks 34-41):
dental-casts-mammal, antler-tine-records, horn-annuli-age-records,
bat-wing-venation, livestock-iris-patterns,
ear-notch-punch-registries, hyena-ear-notch-id, scar-based-photo-id.
Grades are GRADES.md's, unchanged.

Hosts from the Campaign 13 discovery pass (2026-11-18 searches):
loose-file leads first (Montana FWP getRepositoryFile bighorn
summaries, NWSGC proceedings, Swindler dental-cast book excerpt,
UNK shed-antler magazine piece), formal/platform surfaces counted
as such (Boone & Crockett Big Game Records LIVE subscription
database, PMC journal articles, Holekamp Lab project-database
page), custody/sensitive systems documented, never circumvented
(Mara Hyena Project vehicle photo albums, Rice's whale NOAA
catalogue, breed-association books of record).

Method (standing, = Campaigns 7-8/12): live crawl + Wayback
inventory FILTERED to statuscode:200 BEFORE counting; whole-domain
Wayback only for small hosts. Every promising pile sample-verified
in verify13.py. Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

SITES = [
    ("dental-casts-mammal", "Swindler Primate Dentition excerpt — dental cast collection (Cambridge assets)",
     "http://assets.cambridge.org/97805216/52896/excerpt/9780521652896_excerpt.pdf", 0, 3, None),
    ("dental-casts-mammal", "RCS Descriptive Catalogue of Fossil Mammalia full text (archive.org)",
     "https://archive.org/stream/descriptiveillus00roya/descriptiveillus00roya_djvu.txt", 0, 3, None),
    ("antler-tine-records", "Boone & Crockett — biggest whitetail stories / score charts (registration-gated)",
     "https://www.boone-crockett.org/stories-behind-biggest-whitetail-deer-ever", 1, 8, None),
    ("antler-tine-records", "Boone & Crockett — trophy entry requirements (64,000+ records, database)",
     "https://www.boone-crockett.org/trophy-entry-requirements?ref=sidebar", 0, 3, None),
    ("antler-tine-records", "Fort Carson — sample B&C score sheet PDF (loose agency file)",
     "https://fortcarson.isportsman.net/files/Documents%2FPCMS%20Files%2Fsample-b-c-sheet.pdf", 0, 3, None),
    ("antler-tine-records", "Nebraskaland Magazine — UNK cast-antler collection research (Peterson)",
     "https://magazine.outdoornebraska.gov/blogs/in-the-wild/shed-antler-hunting-in-nebraska/", 1, 8, None),
    ("horn-annuli-age-records", "Montana FWP — 1999 Summary of Bighorn Ram Measurements (repository PDF)",
     "http://myfwp.mt.gov/getRepositoryFile?objectID=64293", 0, 3, None),
    ("horn-annuli-age-records", "Montana FWP — 2001 Summary of Bighorn Ram Measurements (repository PDF)",
     "https://myfwp.mt.gov/getRepositoryFile?objectID=64275", 0, 3, None),
    ("horn-annuli-age-records", "Montana FWP — 2006 Summary of Bighorn Ram Measurements (repository PDF)",
     "https://myfwp.mt.gov/getRepositoryFile?objectID=64295", 0, 3, None),
    ("horn-annuli-age-records", "NWSGC 2012 Proceedings — mountain goat horn increments vs cementum (nwsgc.net PDF)",
     "https://www.nwsgc.net/proceedings/NWSGC_2012/2012Proceedings_complete.pdf", 0, 3, None),
    ("horn-annuli-age-records", "Midwest Wild Sheep — how to accurately age bighorn sheep (annuli guide page)",
     "https://www.midwestwildsheep.com/how-to-accurately-age-bighorn-sheep/", 0, 3, None),
    ("bat-wing-venation", "PMC — Seheult et al 2025 CE-pattern individual ID, big brown bats (PMC12527007)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC12527007/", 1, 8, None),
    ("bat-wing-venation", "BioOne — Amelon et al 2017 bat wing biometrics (1,212 photos, 230 bats)",
     "https://complete.bioone.org/journals/journal-of-mammalogy/volume-98/issue-3/gyx018/Bat-wing-biometrics--using-collagen-elastin-bundles-in-bat/10.1093/jmammal/gyx018.full", 0, 3, None),
    ("bat-wing-venation", "Field Key to Antillean Bats PDF (archive.org)",
     "https://ia902302.us.archive.org/23/items/fieldkeyantille94bake/fieldkeyantille94bake.pdf", 0, 3, None),
    ("livestock-iris-patterns", "IntechOpen — RFID + biometric (Optibrand retinal) Irish bovine protocol PDF",
     "https://cdn.intechopen.com/pdfs/8497.pdf", 0, 3, None),
    ("livestock-iris-patterns", "MDPI — HIEN horse iris super-resolution, Zhaosu dataset 54 horses (PDF)",
     "https://mdpi-res.com/d_attachment/applsci/applsci-15-07191/article_deploy/applsci-15-07191.pdf?version=1750933868", 0, 3, None),
    ("livestock-iris-patterns", "MATR — Optibrand OptiReader retinal ID news piece (2003, defunct vendor)",
     "https://matr.net/news/high-tech-device-could-be-the-future-of-livestock-id/", 1, 8, None),
    ("ear-notch-punch-registries", "UNL Extension — Proper Way to Ear Notch Pigs (Universal system chart)",
     "https://extensionpubs.unl.edu/publication/g1880/2008/html/view", 1, 8, None),
    ("ear-notch-punch-registries", "Illinois 4-H — Notches Not Names spark sheet download",
     "https://4h.extension.illinois.edu/media/1636/download?inline", 0, 3, None),
    ("ear-notch-punch-registries", "Minnesota Livestock Exhibition Handbook PDF (ear notch + breed registration rule)",
     "https://www.bah.state.mn.us/sites/default/files/documents/Livestock-Exhibition-Handbook.pdf", 0, 3, None),
    ("hyena-ear-notch-id", "Holekamp Lab — Project Database page (Mara CSV downloads claimed)",
     "https://www.holekamplab.org/project-database.html", 1, 12, "holekamplab.org"),
    ("hyena-ear-notch-id", "PMC — Spagnuolo et al 2022 hyena individual ID review (PMC9744671)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC9744671/", 0, 3, None),
    ("hyena-ear-notch-id", "MSU Hyenas blog (Mara Hyena Project field blog, small host)",
     "https://msuhyenas.blogspot.com/", 1, 12, "msuhyenas.blogspot.com"),
    ("scar-based-photo-id", "PMC — Rice's whale photo-ID catalog 2025 (PMC12416752, NOAA SEFSC)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC12416752/", 1, 8, None),
    ("scar-based-photo-id", "PLOS ONE — Rice's whale catalog figures page",
     "https://journals.plos.org/plosone/article/figures?id=10.1371/journal.pone.0331010", 0, 3, None),
    ("scar-based-photo-id", "MDPI Animals — dolphin wound-healing / scar markers, 106 histories (PDF)",
     "https://www.mdpi.com/2076-2615/16/2/305/pdf", 0, 3, None),
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
              + (" [whole-domain skipped — targeted checks in verify13]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign13_mammal5": results}, "campaign13")
    print("\n=== CAMPAIGN13 MAMMAL5 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
