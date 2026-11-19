#!/usr/bin/env python3
"""Verify13b — Campaign 13 correction pass.
verify13's first PMC-instance xlsx URLs returned 1.8 KB HTML
stubs (PMC viewer phantoms) and the MDPI /pdf endpoint returned
a 408 B stub — both excluded, never counted. This pass samples
the Rice's-whale scar figures via their verbatim PLOS image URLs,
retries the two unreachable PDFs (https scheme / Wayback id_
form), lists the full Holekamp zip, and text-checks the bat
paper for a data repository. Run from goldmine-hunter/.
"""
import io, json, os, re, sys, zipfile
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, UA

OUTDIR = "gold/campaign13-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR
evidence = verify6.evidence

def get_text(url, cap=1_200_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== A. Holekamp zip — full entry list + hyenas.csv size (local sample) ==", flush=True)
    zp = os.path.join(OUTDIR, "msu-hyena-project-data.zip")
    z = zipfile.ZipFile(zp)
    entries = [{"name": i.filename, "bytes": i.file_size} for i in z.infolist()]
    out["holekamp_entries"] = entries
    for e in entries:
        print(f"    {e['bytes']:>10,} B  {e['name']}", flush=True)
    hy = [e for e in entries if e["name"].endswith("hyenas.csv")]
    if hy:
        raw = z.read(hy[0]["name"])
        out["hyenas_csv_lines"] = raw.count(b"\n")
        print(f"  hyenas.csv lines (incl header): {out['hyenas_csv_lines']}", flush=True)

    print("\n== B. Scar — Rice's whale PLOS scar-figure samples (verbatim image URLs) ==", flush=True)
    out["rices_fig3_scar"] = evidence("Rice's whale Fig 3 — whales matched by cookiecutter shark bite scars (PLOS)",
        "https://journals.plos.org/plosone/article/figure/image?size=medium&id=10.1371/journal.pone.0331010.g003",
        "rices-whale-fig3-scar.jpg", cap=5_000_000)
    out["rices_fig7_scar"] = evidence("Rice's whale Fig 7 — dorsal fin + peduncle scar matches 2007-2019 (PLOS)",
        "https://journals.plos.org/plosone/article/figure/image?size=medium&id=10.1371/journal.pone.0331010.g007",
        "rices-whale-fig7-scar.jpg", cap=5_000_000)
    st, html = get_text("https://pmc.ncbi.nlm.nih.gov/articles/PMC12416752/")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,80}Thirty-one whales were individually identified[^.]{0,160}", txt)
    m2 = re.search(r"[^.]{0,60}Cookiecutter shark bite scars were widely present[^.]{0,120}", txt)
    out["rices_pmc_text"] = {"status": st, "n31_snippet": (m.group(0)[:280] if m else None),
                             "cc_snippet": (m2.group(0)[:240] if m2 else None)}
    print(f"  Rice PMC text {st}; 31-whales: {bool(m)}; cookiecutter: {bool(m2)}", flush=True)

    print("\n== C. Dental — Swindler excerpt via https ==", flush=True)
    out["swindler_https"] = evidence("Swindler Primate Dentition excerpt (https)",
        "https://assets.cambridge.org/97805216/52896/excerpt/9780521652896_excerpt.pdf", "swindler-dental-cast-excerpt.pdf", cap=15_000_000)

    print("\n== D. Bat key — Antillean field key via Wayback (CDX-located) ==", flush=True)
    rows = cdx("ia902302.us.archive.org/23/items/fieldkeyantille94bake/fieldkeyantille94bake.pdf", limit=50)
    ok = [x for x in rows if x[2] == "200"]
    print(f"  CDX rows {len(rows)}, status-200 {len(ok)}", flush=True)
    out["antillean_cdx"] = {"rows": len(rows), "ok200": len(ok)}
    if ok:
        out["antillean_wb"] = evidence("Field Key to Antillean Bats PDF (Wayback)",
            wb(ok[0][0], ok[0][1]), "antillean-bat-key.pdf", cap=15_000_000)

    print("\n== E. Bat 2025 — repository / supplement text check ==", flush=True)
    st, html = get_text("https://pmc.ncbi.nlm.nih.gov/articles/PMC12527007/")
    txt = re.sub(r"<[^>]+>", " ", html)
    hits = {}
    for w in ("Dryad", "Zenodo", "figshare", "Supplementary Material", "supplementary data"):
        hits[w] = len(re.findall(w, txt, re.I))
    m = re.search(r"[^.]{0,60}1,212 photographs[^.]{0,100}", txt)
    out["bat_repo_check"] = {"status": st, "repo_hits": hits}
    print(f"  bat PMC repo hits: {hits}", flush=True)

    gh.save({"verify13b": out}, "verify13b")
    print("\nverify13b saved", flush=True)

if __name__ == "__main__":
    main()
