#!/usr/bin/env python3
"""Doctrine run — analysis-first. Takes the two big Wayback piles the
campaign flagged (WorldClim, SDSS) and classifies them the way the
doctrine requires: grouped into comparable SETS (by directory), and
each sampled file classed by provenance — still-live (published by
design) vs gone-from-live (deleted: Wayback-only, the gold class).
Run from goldmine-hunter/."""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from urllib.parse import urlparse

TARGETS = [
    ("WorldClim (geo/climate)", "worldclim.org"),
    ("SDSS data (astro)", "data.sdss.org"),
]
SAMPLE = 24

def classify(url):
    st = gh.head_info(url).get("status")
    if st == 200:
        return "still-live"
    if st in (404, 410):
        return "DELETED (wayback-only)"
    return f"unknown({st})"

def main():
    out = []
    for label, domain in TARGETS:
        print(f"\n#### {label} — {domain}", flush=True)
        wb = gh.wayback_inventory(domain)
        data = [w for w in wb if gh.is_data(w["url"])]
        uniq = {}
        for w in data:
            uniq.setdefault(w["url"], w)
        files = list(uniq.values())
        print(f"  wayback data files (unique): {len(files)}", flush=True)
        import re as _re
        sets = collections.Counter()
        for w in files:
            p = urlparse(w["url"]).path
            parent = p.rsplit("/", 1)[0] or "/"
            fam = _re.sub(r"\d+", "#", p.rsplit("/", 1)[-1])
            sets[f"{parent}/{fam}"] += 1
        print("  sets (by directory):", flush=True)
        for k, n in sets.most_common(10):
            print(f"    {n:5d}  {k}", flush=True)
        exts = collections.Counter(os.path.splitext(urlparse(w['url']).path)[1].lower() for w in files)
        print(f"  extensions: {dict(exts.most_common(8))}", flush=True)
        ranked = sorted(files, key=lambda w: -gh.gold_score(w["url"].rsplit('/', 1)[-1], False))
        sample = ranked[::max(1, len(ranked) // SAMPLE)][:SAMPLE]
        tally = collections.Counter()
        deleted_examples = []
        for w in sample:
            c = classify(w["url"])
            tally[c] += 1
            if c.startswith("DELETED") and len(deleted_examples) < 8:
                deleted_examples.append(w["url"])
        print(f"  provenance sample ({len(sample)} files): {dict(tally)}", flush=True)
        for u in deleted_examples:
            print(f"    deleted: {u}", flush=True)
        out.append({"label": label, "domain": domain, "unique_wayback_data": len(files),
                    "sets": dict(sets.most_common(12)), "extensions": dict(exts.most_common(10)),
                    "sample": dict(tally), "deleted_examples": deleted_examples,
                    "top_scored": [w["url"] for w in ranked[:10]]})
    gh.save({"doctrine_run": out}, "doctrine-run")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
