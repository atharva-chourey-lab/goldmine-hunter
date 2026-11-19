#!/usr/bin/env python3
"""Campaign 14 — Mammal Wave 6, GENERATED from the mammal-grain
registry's tail (ranks 42-50 by current score, registry order):
hair-medulla-cross-sections (7), sheep-goat-nose-prints,
cat-nose-leather-patterns, hoof-cloven-track-systems,
claw-mark-archives, bite-mark-records, vibrissae-follicle-maps,
tail-pattern-systems, lab-animal-marking-records (all 6).
This campaign exhausts the mammal registry. Grades are
GRADES.md's, unchanged.

Hosts from the Campaign 14 discovery pass (2026-11-18 searches):
loose-file leads first (hairatlas.hu — Toth 2017 book served as
per-page PDFs on its own old site; JAX Green Book chapter;
journal PDFs), formal archives counted as such (UMN Conservancy
thesis, MDPI/PMC papers, archive.org manuals), custody systems
documented, never circumvented (Indiana 4-H nose-print cards,
wildlife-forensic reference casts, colony marking logs).

Method (standing, = Campaigns 7-8/12): live crawl + Wayback
inventory FILTERED to statuscode:200 BEFORE counting; whole-domain
Wayback only for small hosts. Every promising pile sample-verified
in verify14.py. Run from goldmine-hunter/.
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

SITES = [
    ("hair-medulla-cross-sections", "Hair Atlas home/species index (hairatlas.hu — Toth 2017)",
     "https://www.hairatlas.hu/index.php?m2=species", 1, 12, "hairatlas.hu"),
    ("hair-medulla-cross-sections", "Hair Atlas — Cervidae & Bovidae spread PDF (medulla + cross-section)",
     "https://hairatlas.hu/pdf/Hair_atlas_212-213.pdf", 0, 3, None),
    ("hair-medulla-cross-sections", "ZSI Trichotaxonomy of Ratufa PDF (medulla + cross-section tables)",
     "https://zsi.gov.in/public/PDFVolumes/records/110/03/0037-0057.pdf", 0, 3, None),
    ("sheep-goat-nose-prints", "JOE 2006 — Retinal imaging vs nose prints, Indiana 4-H beef & sheep (slideshare mirror)",
     "https://www.slideshare.net/slideshow/2006-an-evaluation-of-retinal-imaging-technology-for-4h-beef-and-sheep-identification/3310171", 0, 3, None),
    ("sheep-goat-nose-prints", "MDPI — Sheep & goat face classifier (muzzle/coat/ear, Roboflow/YOLOv8)",
     "https://www.mdpi.com/2624-7402/6/4/204", 0, 3, None),
    ("cat-nose-leather-patterns", "KNAU Bulletin — Tentieva & Arbaev 2025 cat nasolabial mirror (n=157)",
     "https://knau-bulletin.com/en/journals/tom-23-2-2025/kharakteristika-papillyarnogo-stroyeniya-nosogubnogo-zerkala-koshek", 0, 3, None),
    ("cat-nose-leather-patterns", "CFA — Inside the Cat's Nose (nose-print summary)",
     "https://cfa.org/cat-talk/inside-the-cats-nose/", 0, 3, None),
    ("hoof-cloven-track-systems", "NMSU Circular 561 — Identifying & Preserving Wildlife Tracks PDF (hoof measurements)",
     "https://pubs.nmsu.edu/_circulars/CR561.pdf", 0, 3, None),
    ("hoof-cloven-track-systems", "Stuart Field Guide to Tracks & Signs — preview PDF (cloven-hoof reference)",
     "https://api.pageplace.de/preview/DT0400.9781775840305_A20871588/preview-9781775840305_A20871588.pdf", 0, 3, None),
    ("claw-mark-archives", "Diversity 2022 — Three bears NE India, claw-mark method applied (MDPI PDF)",
     "https://mdpi-res.com/d_attachment/diversity/diversity-14-00717/article_deploy/diversity-14-00717.pdf?version=1661778465", 0, 3, None),
    ("claw-mark-archives", "UMN Conservancy — Steinmetz 2009 thesis (claw-mark discriminant, captive n=43)",
     "https://conservancy.umn.edu/items/7df0f099-e63b-49c7-beb7-c61f85cf85ee", 0, 3, None),
    ("bite-mark-records", "FSI Animals & Environments 2023 — bear attack taphonomy PDF (scavengers.cat)",
     "https://scavengers.cat/wp-content/uploads/2023/12/1-s2.0-S2666937423000148-main.pdf", 0, 3, None),
    ("bite-mark-records", "PMC — Purussaurus bite marks on sloth tibia (46 tooth marks, figshare supplement)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC7480153/", 0, 3, None),
    ("vibrissae-follicle-maps", "MMU e-space — Evans & Elder diceCT pinniped mystacial pad methods PDF",
     "https://e-space.mmu.ac.uk/638064/8/EVANS_AND_ELDER_DiceCT_Methods_Pinnipeds_FINAL_SUBMISSION.pdf", 0, 3, None),
    ("vibrissae-follicle-maps", "PubMed — Harbour seal mystacial pad diceCT paper record",
     "https://pubmed.ncbi.nlm.nih.gov/39404176/", 0, 3, None),
    ("tail-pattern-systems", "San Diego Zoo Library — Ring-tailed lemur fact sheet (tail-ring counts)",
     "https://ielc.libguides.com/sdzg/factsheets/ringtailedlemur/characteristics", 0, 3, None),
    ("tail-pattern-systems", "Tasmania DPIPWE — Ring-tailed lemur pest risk assessment PDF",
     "https://nre.tas.gov.au/Documents/Ring%20tailed%20lemur%20risk%20assessment.pdf", 0, 3, None),
    ("lab-animal-marking-records", "Jackson Laboratory Green Book Ch.3 — Keeping Records (ear-punch code, ledgers)",
     "http://www.informatics.jax.org/greenbook/chapters/chapter3.shtml", 1, 8, None),
    ("lab-animal-marking-records", "USDA 1949 — Raising Laboratory Mice and Rats (toe-clip/ear-mark Fig.3, archive.org)",
     "https://ia903202.us.archive.org/7/items/raisinglaborator253eato/raisinglaborator253eato_bw.pdf", 0, 3, None),
    ("lab-animal-marking-records", "Scand J Lab Anim Sci 1988 — Review of lab-animal identification methods PDF",
     "https://ojs.utlib.ee/index.php/SJLAS/article/download/21751/16479/28642", 0, 3, None),
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
              + (" [whole-domain skipped — targeted checks in verify14]" if not wb_domain else ""), flush=True)
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
    gh.save({"campaign14_mammal6": results}, "campaign14")
    print("\n=== CAMPAIGN14 MAMMAL6 SUMMARY ===", flush=True)
    for r in sorted(results, key=lambda x: -(x["unique_data_files"] + x["wayback_data_files_status200"])):
        print(f"  live {r['unique_data_files']:4d} | wayback200 {r['wayback_data_files_status200']:5d} | [{r['niche']}] {r['label']}", flush=True)

if __name__ == "__main__":
    main()
