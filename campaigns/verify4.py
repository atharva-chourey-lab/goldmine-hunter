#!/usr/bin/env python3
"""Verify4 — Campaign 4 verification pass (standing method upgrade).
For every promising Campaign-4 pile: sample-download 1-2 smallest
promising files (live URL, or Wayback snapshot id_ URL for deleted
ones), bounded, and record size / md5 / magic / zip-listing / line
count so a pile counts only if a member is REAL data, not an HTML
phantom or placeholder (the WorldClim lesson). Also HEAD-checks the
live status of Wayback-only files (deleted vs still-live), and runs
targeted CDX prefix queries where the campaign's whole-domain
Wayback inventory was misleading (GCVS: sai.msu.su is mostly an
Apache software mirror; the catalogue lives under /gcvs/gcvs/).
Run from goldmine-hunter/. Samples saved to gold/campaign4-verify/.
"""
import collections, hashlib, io, json, os, sys, zipfile
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh

UA = {"User-Agent": "goldmine-hunter/2.0 (open-science dataset recovery)"}
OUTDIR = "gold/campaign4-verify"
CAP = 40_000_000

def head(url):
    try:
        r = requests.head(url, headers=UA, timeout=30, allow_redirects=True)
        return {"status": r.status_code, "size": r.headers.get("Content-Length"),
                "type": r.headers.get("Content-Type")}
    except Exception as e:
        return {"status": None, "error": str(e)[:120]}

def fetch_bounded(url, cap=CAP):
    """Stream-download up to cap bytes. Returns dict with evidence."""
    try:
        r = requests.get(url, headers=UA, timeout=120, stream=True, allow_redirects=True)
        status = r.status_code
        buf = io.BytesIO()
        for chunk in r.iter_content(65536):
            buf.write(chunk)
            if buf.tell() > cap:
                break
        raw = buf.getvalue()
        truncated = len(raw) > cap or (r.headers.get("Content-Length") and int(r.headers["Content-Length"]) > len(raw))
        return {"status": status, "raw": raw, "truncated": bool(truncated),
                "content_type": r.headers.get("Content-Type")}
    except Exception as e:
        return {"status": None, "raw": b"", "error": str(e)[:160]}

def evidence(label, url, save_name=None):
    f = fetch_bounded(url)
    raw = f["raw"]
    ev = {"label": label, "url": url, "http_status": f["status"],
          "bytes_downloaded": len(raw), "truncated_at_cap": f.get("truncated", False),
          "content_type": f.get("content_type"), "error": f.get("error")}
    if not raw:
        ev["verdict"] = "UNREACHABLE / EMPTY"
        print(f"  [{label}] {ev['verdict']} {url[:100]}", flush=True)
        return ev
    ev["md5_full"] = hashlib.md5(raw).hexdigest() if not ev["truncated_at_cap"] else None
    ev["md5_head1mb"] = hashlib.md5(raw[:1_000_000]).hexdigest()
    head_bytes = raw[:512]
    low = url.lower().split("?")[0]
    is_html = head_bytes.lstrip().lower().startswith((b"<!doctype", b"<html", b"<!--"))
    ev["looks_html"] = bool(is_html)
    if is_html:
        ev["verdict"] = "PHANTOM — HTML page, not data"
    elif low.endswith(".zip") or raw[:2] == b"PK":
        try:
            z = zipfile.ZipFile(io.BytesIO(raw))
            ev["zip_entries"] = z.namelist()[:12]
            ev["zip_n_entries"] = len(z.namelist())
            ev["verdict"] = "REAL — valid zip"
        except Exception as e:
            ev["verdict"] = f"NOT A VALID ZIP: {e}"
    elif raw[:4] == b"\xd0\xcf\x11\xe0":
        ev["verdict"] = "REAL — OLE2 (legacy .xls)"
        ev["ole2"] = True
    elif raw[:8] == b"\x89HDF\r\n\x1a\n":
        ev["verdict"] = "REAL — HDF5 (loom/h5 family)"
        ev["hdf5"] = True
    elif raw[:6] == b"SIMPLE":
        ev["verdict"] = "REAL — FITS header SIMPLE"
        ev["fits"] = True
    elif raw[:2] == b"\x1f\x8b":
        ev["verdict"] = "REAL — gzip stream"
        ev["gzip"] = True
    elif low.endswith((".csv", ".tsv", ".txt", ".dat", ".json", ".xml", ".label", ".stm")):
        try:
            txt = raw.decode("utf-8", errors="strict")
            ev["lines_sampled"] = txt.count("\n")
            ev["first_line"] = txt.split("\n")[0][:160]
            ev["verdict"] = "REAL — decodable text data"
        except UnicodeDecodeError:
            ev["first_bytes_hex"] = head_bytes[:16].hex()
            ev["verdict"] = "BINARY — non-HTML, non-blank (fixed-width data?)"
    else:
        ev["first_bytes_hex"] = head_bytes[:16].hex()
        ev["all_blank"] = all(b in (0, 9, 10, 13, 32) for b in raw[:100000])
        ev["verdict"] = "EMPTY PLACEHOLDER — blank" if ev["all_blank"] else "BINARY — non-HTML, non-blank"
    if save_name and ev["verdict"].startswith("REAL") and not ev["truncated_at_cap"]:
        os.makedirs(OUTDIR, exist_ok=True)
        with open(os.path.join(OUTDIR, save_name), "wb") as fh:
            fh.write(raw)
        ev["saved_to"] = os.path.join(OUTDIR, save_name)
    print(f"  [{label}] {ev['verdict']} | {len(raw):,} B | md5={ev.get('md5_full') or ev['md5_head1mb']} | {url[:100]}", flush=True)
    return ev

def cdx(prefix, limit=8000):
    try:
        r = requests.get("http://web.archive.org/cdx/search/cdx",
                         params={"url": prefix, "output": "json",
                                 "fl": "timestamp,original,statuscode,length,mimetype",
                                 "collapse": "urlkey", "limit": limit},
                         headers=UA, timeout=120)
        r.raise_for_status()
        rows = r.json()
        return rows[1:] if len(rows) > 1 else []
    except Exception as e:
        print(f"  CDX failed {prefix}: {e}", flush=True)
        return []

def wb(ts, orig):
    return f"https://web.archive.org/web/{ts}id_/{orig}"

def main():
    out = {}

    print("\n== 1. STScI / Kepler-HLSP live (657 files) ==", flush=True)
    stsci = [
        "https://archive.stsci.edu/hlsps/agnsedatlas/hlsp_agnsedatlas_multi_photometry_all_multi_v1_obs-cat.csv",
        "https://archive.stsci.edu/hlsps/agnsedatlas/hlsp_agnsedatlas_multi_photometry_all_multi_v1_cat.fits",
        "https://archive.stsci.edu/hlsps/atlas-var/hlsp_atlas-var_atlas_ccd_all_cyan-orange_dr1_observation.fits",
    ]
    out["stsci_head"] = {u.rsplit("/", 1)[-1]: head(u) for u in stsci}
    for k, v in out["stsci_head"].items():
        print(f"  HEAD {k}: {v}", flush=True)
    out["stsci_sample"] = evidence("STScI obs-cat.csv live", stsci[0])

    print("\n== 2. AnAge / Senescence.info live ==", flush=True)
    out["anage_live"] = [
        evidence("AnAge cellAge.zip live", "https://genomics.senescence.info/cells/cellAge.zip", "anage-cellAge-live.zip"),
        evidence("AnAge diet dataset.zip live", "https://genomics.senescence.info/diet/dataset.zip"),
        evidence("AnAge TableS2.xls live", "https://genomics.senescence.info/diet/TableS2.xls"),
    ]
    print("== 2b. AnAge Wayback-only evolution supplements ==", flush=True)
    anage_wb = [
        ("supplemental_tables.zip", "20171022094929", "http://genomics.senescence.info/evolution/supplemental_tables.zip"),
        ("mammalian_supplement.zip", "20171022121512", "http://genomics.senescence.info/evolution/mammalian_supplement.zip"),
        ("animals_aln.zip", "20060101044930", "http://genomics.senescence.info:80/evolution/animals_aln.zip"),
        ("overall_stats.txt", "20050224184957", "http://genomics.senescence.info:80/evolution/overall_stats.txt"),
    ]
    out["anage_wb"] = [evidence(f"AnAge wb {n}", wb(ts, u), f"anage-{n}" if n.endswith(".zip") else None) for n, ts, u in anage_wb]
    out["anage_wb_live_status"] = {n: head(u.replace(":80", "")) for n, ts, u in anage_wb}
    for k, v in out["anage_wb_live_status"].items():
        print(f"  live-status {k}: {v}", flush=True)

    print("\n== 3. NOW fossil mammals live + wayback ==", flush=True)
    out["now_live"] = [
        evidence("NOW dental csv live", "https://www.nowdatabase.org/static/now/datasets/data_dental_modern_public_10.b63c3f89c38d.csv"),
        evidence("NOW Fortelius 2003 zip live", "https://www.nowdatabase.org/static/now/datasets/Fortelius_2003_ICZ2000.338638644ed3.zip", "now-Fortelius_2003_ICZ2000.zip"),
        evidence("NOW Sinap txt live", "https://www.nowdatabase.org/static/now/field_cat/SinapFC95.252b351538d0.txt"),
    ]
    out["now_wb"] = [
        evidence("NOW dental csv wb2023 (unhashed name)", wb("20230805032843", "https://www.nowdatabase.org/static/now/datasets/data_dental_modern_public_10.csv")),
    ]

    print("\n== 4. Neotoma live snapshots ==", flush=True)
    neo = [
        "https://www.neotomadb.org/apps/data/taxa_changes.json",
        "https://www.neotomadb.org/assets/uploads/documents/snapshots/neotoma_schema_only_2022-03-17.tar",
        "https://www.neotomadb.org/assets/uploads/documents/snapshots/NeotomaSnapshot_2016-05-13.zip",
        "https://www.neotomadb.org/assets/uploads/documents/snapshots/neotoma_ndb_only_2024-03-18.tar",
        "https://neotoma-remote-store.s3.us-east-2.amazonaws.com/neotoma_clean_latest.tar.gz",
    ]
    out["neotoma_head"] = {u.rsplit("/", 1)[-1]: head(u) for u in neo}
    for k, v in out["neotoma_head"].items():
        print(f"  HEAD {k}: {v}", flush=True)
    out["neotoma_sample"] = evidence("Neotoma taxa_changes.json live", neo[0])

    print("\n== 5. Human Protein Atlas live ==", flush=True)
    out["hpa"] = [
        evidence("HPA d.data.label live", "https://www.proteinatlas.org/humanproteome/d.data.label"),
        {"label": "HPA cell_proteome_movie.mp4 HEAD", **head("https://www.proteinatlas.org/download/cell_proteome_movie.mp4")},
    ]
    print(f"  HPA movie HEAD: {out['hpa'][1]}", flush=True)

    print("\n== 6. Rosetta Project live (archive.org streams) ==", flush=True)
    out["rosetta"] = [
        evidence("Rosetta cat.txt live", "http://www.archive.org/stream/rosettaproject_cat_swadesh-1/cat.txt"),
        evidence("Rosetta English_Swadesh_list.txt live", "http://www.archive.org/stream/rosettaproject_eng_swadesh-1/English_Swadesh_list.txt"),
    ]

    print("\n== 7. HyperLEDA live + wayback ==", flush=True)
    out["hyperleda"] = [
        evidence("HyperLEDA opensearch xml live", "http://leda.univ-lyon1.fr/opensearch_description.xml"),
        evidence("HyperLEDA line_code.txt wb2003", wb("20030510221348", "http://leda.univ-lyon1.fr:80/05/line_code.txt")),
    ]

    print("\n== 8. HCA project matrices (Wayback) ==", flush=True)
    rows = cdx("data.humancellatlas.org/project-assets/*")
    ok = [x for x in rows if x[2] == "200"]
    mats = [x for x in ok if "/project-matrices/" in x[1]]
    metas = [x for x in ok if "/project-metadata/" in x[1]]
    print(f"  project-assets status-200: matrices {len(mats)}, metadata {len(metas)}", flush=True)
    for ts, orig, sc, ln, mt in sorted(mats, key=lambda x: int(x[3] or 0)):
        print(f"    mat {ln:>10} B  {orig.rsplit('/',1)[-1]}  ({ts})", flush=True)
    out["hca_cdx"] = {"matrices200": [{"ts": x[0], "url": x[1], "length": x[3]} for x in mats],
                      "metadata200": [{"ts": x[0], "url": x[1], "length": x[3]} for x in metas]}
    # sample the smallest matrix zip + one loom header + one metadata tsv
    zips = sorted([x for x in mats if x[1].endswith(".zip")], key=lambda x: int(x[3] or 0))
    looms = sorted([x for x in mats if x[1].endswith(".loom")], key=lambda x: int(x[3] or 0))
    out["hca_sample"] = []
    if zips:
        ts, orig, sc, ln, mt = zips[0]
        out["hca_sample"].append(evidence(f"HCA smallest matrix zip ({ln} B CDX)", wb(ts, orig),
                                          "hca-" + orig.rsplit("/", 1)[-1]))
    if looms:
        ts, orig, sc, ln, mt = looms[0]
        out["hca_sample"].append(evidence(f"HCA smallest loom ({ln} B CDX, header check)", wb(ts, orig)))
    if metas:
        ts, orig, sc, ln, mt = sorted(metas, key=lambda x: int(x[3] or 0))[0]
        out["hca_sample"].append(evidence("HCA metadata tsv", wb(ts, orig)))
    if mats:
        ts, orig, sc, ln, mt = mats[0]
        out["hca_live_status_first_matrix"] = head(orig)
        print(f"  live-status of a matrix URL today: {out['hca_live_status_first_matrix']}", flush=True)

    print("\n== 9. GCVS targeted CDX (/gcvs/gcvs/) ==", flush=True)
    rows = cdx("www.sai.msu.su/gcvs/gcvs/*", limit=10000)
    ok = [x for x in rows if x[2] == "200"]
    data = [x for x in ok if x[1].lower().split("?")[0].endswith((".dat", ".txt", ".csv", ".zip", ".gz"))]
    sets = collections.Counter("/" + "/".join(x[1].split("/")[3:-1]) for x in data)
    print(f"  /gcvs/gcvs/* collapsed {len(rows)}, status-200 {len(ok)}, data-ext {len(data)}", flush=True)
    for k, v in sets.most_common(15):
        print(f"    set {v:4d}  {k}", flush=True)
    out["gcvs_cdx"] = {"collapsed": len(rows), "ok200": len(ok), "data_ext200": len(data),
                       "sets": dict(sets.most_common(20)),
                       "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in data[:80]]}
    out["gcvs_sample"] = [
        evidence("GCVS iii.dat wb2011", wb("20110520055841", "http://www.sai.msu.su:80/gcvs/gcvs/iii/iii.dat")),
        evidence("GCVS cep/cat_3.dat wb2006", wb("20060716113202", "http://www.sai.msu.su:80/gcvs/gcvs/cep/cat_3.dat")),
        evidence("GCVS glcl_var.dat wb2022", wb("20220706230406", "http://www.sai.msu.su/gcvs/gcvs/glcl_var/glcl_var.dat")),
    ]
    out["gcvs_live_status"] = head("http://www.sai.msu.su/gcvs/gcvs/iii/iii.dat")
    print(f"  live-status iii.dat: {out['gcvs_live_status']}", flush=True)
    # digitised light-curve pile spotted in the whole-gcvs filter
    rowsd = cdx("www.sai.msu.su/gcvs/digit/*", limit=10000)
    okd = [x for x in rowsd if x[2] == "200"]
    print(f"  /gcvs/digit/* collapsed {len(rowsd)}, status-200 {len(okd)}", flush=True)
    for x in okd[:10]:
        print(f"    digit {x[3]} B  {x[1]}  ({x[0]})", flush=True)
    out["gcvs_digit"] = {"collapsed": len(rowsd), "ok200": len(okd),
                          "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in okd[:40]]}
    if okd:
        ts, orig, sc, ln, mt = sorted(okd, key=lambda x: int(x[3] or 0))[0]
        out["gcvs_digit_sample"] = evidence(f"GCVS digit smallest ({ln} B CDX)", wb(ts, orig))

    print("\n== 10. Harvard Whole Brain Atlas (Wayback) ==", flush=True)
    out["wba"] = [
        evidence("WBA case.txt wb2001", wb("20010507153114", "http://www.med.harvard.edu:80/AANLIB/cases/case1/case.txt")),
        evidence("WBA jnavcd.txt wb2001", wb("20010507153710", "http://www.med.harvard.edu:80/AANLIB/cases/case1/jnavcd.txt")),
    ]

    print("\n== 11. TreeBASE (Wayback) ==", flush=True)
    out["treebase"] = [evidence("TreeBASE kmltreeserver.zip wb2007", wb("20071027075101", "http://www.treebase.org/getrees/kmltreeserver.zip"))]

    print("\n== 12. Fidelity leftovers with ~zero piles ==", flush=True)
    out["dbb"] = [evidence("DBB robots.txt wb2021 (only wb200 file)", wb("20211129181902", "http://digitalbrainbank.org/robots.txt"))]
    out["tabula"] = [evidence("Tabula Muris manifest.json wb2018 (only wb200 file)", wb("20180525073344", "http://tabula-muris.ds.czbiohub.org:80/manifest.json"))]

    gh.save({"verify4": out}, "verify4")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
