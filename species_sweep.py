#!/usr/bin/env python3
"""Run Goldmine Hunter over every Brain Catalogue species page and diff
the live site's file inventory against what we already hold locally in
brain-scan-comparison/data/brain_catalogue_full/. Deep-checks every
label file for the empty-placeholder trap. Run from goldmine-hunter/."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh

LOCAL = os.path.expanduser("~/workspace/brain-scan-comparison/data/brain_catalogue_full")
LABEL_HINTS = ("hippocampus", "telencephalon", "atlas", "neocortex", "cerebellum")

def main():
    species = sorted(os.listdir(LOCAL))
    print(f"{len(species)} species folders locally")
    results, new_finds = {}, []
    for sp in species:
        local_files = {f for f in os.listdir(os.path.join(LOCAL, sp))}
        crawl = gh.crawl_site(f"https://braincatalogue.org/{sp}", depth=0, max_pages=3)
        # HEAD-verify variants per filename, keep live ones
        by_name = {}
        for f in crawl["data_files"]:
            if f["name"].lower() in gh.IGNORE_NAMES:
                continue
            by_name.setdefault(f["name"], []).append(f)
        live = {}
        for name, variants in by_name.items():
            for v in variants:
                h = gh.head_info(v["url"])
                if h.get("status") == 200:
                    live[name] = {"url": v["url"], "size": h.get("size")}
                    break
        site_files = set(live)
        new = sorted(site_files - local_files)
        gone = sorted(local_files - site_files)
        # deep-check labels (skip the big MRIs)
        checks = {}
        for name in sorted(site_files):
            if any(k in name.lower() for k in LABEL_HINTS):
                checks[name] = gh.check_nifti(live[name]["url"], deep=True)
        empties = [n for n, c in checks.items() if c.get("all_zero")]
        real = [n for n, c in checks.items() if c.get("ok") and not c.get("all_zero")]
        results[sp] = {"site_files": live, "new_vs_local": new, "local_not_on_site": gone,
                       "labels_real": real, "labels_empty": empties, "checks": checks}
        flag = f"  NEW: {new}" if new else ""
        print(f"{sp:28s} site={len(site_files)} local={len(local_files)} "
              f"labels real={len(real)} empty={len(empties)}{flag}")
        if new:
            new_finds.append((sp, new))
    out = {"species": results, "new_finds": new_finds}
    path = gh.save(out, "species-sweep")
    print(f"\nNEW FINDS (on site, not held locally): {new_finds or 'none'}")
    tot_real = sum(len(r["labels_real"]) for r in results.values())
    tot_empty = sum(len(r["labels_empty"]) for r in results.values())
    print(f"Label census across sweep: {tot_real} real, {tot_empty} empty placeholders")

if __name__ == "__main__":
    main()
