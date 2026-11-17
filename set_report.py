#!/usr/bin/env python3
"""set_report.py — the analysis-first layer of Goldmine Hunter.

Doctrine (see README, "Design doctrine"): the unit of value is a COMPARABLE
SET, not a file. A find becomes science when the same derived data type is
assembled across many comparable units (species, simulation runs, sites,
timepoints), audited member by member, and handed over as one harmonized
bundle the comparative analysis can run on. This script reads a
species-sweep JSON (per-unit file lists + deep-check verdicts) and reports,
per comparison class (file type):

  - coverage: how many units hold the file at all
  - real vs EMPTY PLACEHOLDER (deep-check all_zero verdicts)
  - absent: units that do not hold it
  - completeness: real / total units — the number an analysis can stand on

Provenance classes are kept distinct in the output: site-held files are
`stranded` candidates (gold class: on the project site, not in the formal
archive — pass an audit JSON with --audit to mark which are confirmed
website-only vs shared with the archive). Files a site publishes by design
are inventory, not recovery, and are never reported as gold.

File-level census only: plausibility QC (a non-empty file can still be a
junk sliver or a mislabel) is the analysis layer's job, as in the brain
project's table v2 exclusions.

Usage:
  python3 set_report.py outputs/species-sweep-<ts>.json [--audit outputs/audit-*.json]
"""
import json, sys, glob, collections

def load(p):
    with open(p) as f: return json.load(f)

def main():
    args = sys.argv[1:]
    sweep_path = next(a for a in args if "sweep" in a)
    audit_paths = []
    if "--audit" in args:
        audit_paths = args[args.index("--audit") + 1:]
        if not audit_paths: audit_paths = sorted(glob.glob("outputs/audit-*.json"))
    sweep = load(sweep_path)
    species = sweep["species"]
    units = sorted(species.keys())

    website_only = set()
    for ap in audit_paths:
        a = load(ap)
        for c in a.get("gold_candidates_website_only", []):
            website_only.add(c.get("name", ""))

    # two passes, so 'absent' is counted against ALL units for every class,
    # including classes that only appear in later units
    all_types = set()
    for u in units:
        rec = species[u]
        all_types |= set(rec.get("labels_real", [])) | set(rec.get("labels_empty", [])) | set(rec.get("site_files", {}).keys())
    classes = {t: {"real": [], "empty": [], "absent": []} for t in all_types}
    for u in units:
        rec = species[u]
        real = set(rec.get("labels_real", [])); empty = set(rec.get("labels_empty", []))
        held = set(rec.get("site_files", {}).keys())
        for t in all_types:
            if t in real or (t in held and t not in empty): classes[t]["real"].append(u)
            elif t in empty: classes[t]["empty"].append(u)
            else: classes[t]["absent"].append(u)

    print(f"COMPARISON-SET REPORT — {len(units)} units from {sweep_path}\n")
    rows = []
    for t, d in sorted(classes.items(), key=lambda kv: -len(kv[1]["real"])):
        n_real, n_empty, n_abs = len(d["real"]), len(d["empty"]), len(d["absent"])
        prov = "STRANDED (confirmed website-only)" if t in website_only else "site-held"
        rows.append({"class": t, "real": d["real"], "empty_placeholder": d["empty"],
                     "absent": d["absent"], "provenance": prov})
        print(f"{t:28s} real {n_real:3d} | empty {n_empty:3d} | absent {n_abs:3d} "
              f"| completeness {n_real}/{len(units)} | {prov}")
    out = {"source": sweep_path, "units": units, "sets": rows}
    op = "outputs/set-report-from-" + sweep_path.split("/")[-1]
    with open(op, "w") as f: json.dump(out, f, indent=1)
    print(f"\nwrote {op}")
    print("Reading: a set is analysis-ready when its REAL members span the comparison")
    print("the analysis needs; empty placeholders and absences are reported, never")
    print("silently dropped — they are what the completeness number is made of.")

if __name__ == "__main__":
    main()
