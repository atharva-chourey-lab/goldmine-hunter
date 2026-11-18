#!/usr/bin/env python3
"""Verify5 — Campaign 5 verification pass (standing method upgrade).
For every promising Campaign-5 pile: sample-download 1-2 smallest
promising files (live URL, or Wayback snapshot id_ URL for deleted
ones), bounded, and record size / md5 / magic / zip-listing so a pile
counts only if a member is REAL data, not an HTML phantom. Also
HEAD-checks the live status of Wayback-only files (deleted vs
still-live), and runs targeted CDX prefix queries where the
campaign's whole-domain Wayback inventory was misleading or capped
(Reptile /data, CRU subtrees, CLIO IndicatorsPerCountry, Villanova
WDCatalog, SCOP /files).
Run from goldmine-hunter/. Samples saved to gold/campaign5-verify/.
Total new disk kept small: samples only, bounded caps.
"""
import collections, hashlib, io, json, os, sys, zipfile
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh

UA = {"User-Agent": "goldmine-hunter/2.0 (open-science dataset recovery)"}
OUTDIR = "gold/campaign5-verify"
CAP = 25_000_000

def head(url):
    try:
        r = requests.head(url, headers=UA, timeout=30, allow_redirects=True)
        return {"status": r.status_code, "size": r.headers.get("Content-Length"),
                "type": r.headers.get("Content-Type")}
    except Exception as e:
        return {"status": None, "error": str(e)[:120]}

def fetch_bounded(url, cap=CAP):
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

def evidence(label, url, save_name=None, cap=CAP):
    f = fetch_bounded(url, cap)
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
            ev["verdict"] = "REAL — valid zip (xlsx/zip family)"
        except Exception as e:
            ev["verdict"] = f"PK MAGIC but zip unreadable (truncated?): {e}"
            ev["pk_magic"] = True
    elif raw[:4] == b"\xd0\xcf\x11\xe0":
        ev["verdict"] = "REAL — OLE2 (legacy .xls)"
        ev["ole2"] = True
    elif raw[:8] == b"\x89HDF\r\n\x1a\n":
        ev["verdict"] = "REAL — HDF5"
        ev["hdf5"] = True
    elif raw[:6] == b"SIMPLE":
        ev["verdict"] = "REAL — FITS header SIMPLE"
        ev["fits"] = True
    elif raw[:2] == b"\x1f\x8b":
        ev["verdict"] = "REAL — gzip stream"
        ev["gzip"] = True
        # peek inside tar.gz if small enough
        if low.endswith((".tar.gz", ".tgz")) and not ev["truncated_at_cap"]:
            import tarfile
            try:
                t = tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz")
                ev["tar_entries"] = t.getnames()[:12]
                ev["tar_n_entries"] = len(t.getnames())
            except Exception as e:
                ev["tar_error"] = str(e)[:100]
    elif low.endswith((".csv", ".tsv", ".txt", ".dat", ".json", ".xml", ".fa", ".fasta", ".geojson", ".stm")) or raw[:1] == b">":
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

    print("\n== 1. Reptile Database /data/* targeted CDX ==", flush=True)
    rows = cdx("reptile-database.org/data/*")
    ok = [x for x in rows if x[2] == "200"]
    print(f"  /data/* collapsed {len(rows)}, status-200 {len(ok)}", flush=True)
    for ts, orig, sc, ln, mt in sorted(ok, key=lambda x: x[1]):
        print(f"    {ln:>10} B  {orig.rsplit('/',1)[-1]}  ({ts})", flush=True)
    out["reptile_cdx"] = {"collapsed": len(rows), "ok200": len(ok),
                          "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok]}
    out["reptile_live_status"] = {x[1].rsplit("/", 1)[-1]: head(x[1]) for x in ok}
    for k, v in out["reptile_live_status"].items():
        print(f"  live-status {k}: {v}", flush=True)
    if ok:
        ts, orig, sc, ln, mt = sorted(ok, key=lambda x: int(x[3] or 0))[0]
        out["reptile_sample_smallest_wb"] = evidence(f"Reptile smallest /data wb ({ln} B CDX)", wb(ts, orig),
                                                     "reptile-" + orig.rsplit("/", 1)[-1])
    checks = [x for x in ok if "checklist" in x[1].lower()]
    if checks:
        ts, orig, sc, ln, mt = sorted(checks, key=lambda x: int(x[3] or 0))[0]
        out["reptile_sample_checklist_wb"] = evidence(f"Reptile checklist wb ({ln} B CDX)", wb(ts, orig),
                                                      "reptile-" + orig.rsplit("/", 1)[-1])
    out["reptile_live_sample"] = evidence("Reptile Genera_without_photos.xlsx live",
                                           "http://www.reptile-database.org/db-info/Genera_without_photos.xlsx")

    print("\n== 2. CRU targeted CDX (crutem3, temperature, cru_ts code_archives) ==", flush=True)
    out["cru"] = {}
    for prefix in ("crudata.uea.ac.uk/cru/data/crutem3/*",
                   "crudata.uea.ac.uk/cru/data/temperature/*",
                   "crudata.uea.ac.uk/cru/data/hrg/*"):
        rows = cdx(prefix)
        ok = [x for x in rows if x[2] == "200"]
        sets = collections.Counter("/" + "/".join(x[1].split("/")[3:-1]) for x in ok)
        print(f"  {prefix}: collapsed {len(rows)}, status-200 {len(ok)}", flush=True)
        for k, v in sets.most_common(8):
            print(f"    set {v:4d}  {k}", flush=True)
        key = prefix.split("/cru/data/")[1].strip("/*").replace("/", "_")
        out["cru"][key] = {"collapsed": len(rows), "ok200": len(ok), "sets": dict(sets.most_common(10)),
                           "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:60]]}
        if ok:
            ts, orig, sc, ln, mt = sorted(ok, key=lambda x: int(x[3] or 0))[0]
            out["cru"][key + "_sample_wb"] = evidence(f"CRU {key} smallest wb ({ln} B CDX)", wb(ts, orig))
            out["cru"][key + "_live_status"] = head(orig)
            print(f"  live-status {orig[:90]}: {out['cru'][key + '_live_status']}", flush=True)

    print("\n== 3. CLIO Infra IndicatorsPerCountry targeted CDX + live ==", flush=True)
    rows = cdx("clio-infra.eu/IndicatorsPerCountry/*", limit=10000)
    ok = [x for x in rows if x[2] == "200"]
    print(f"  IndicatorsPerCountry collapsed {len(rows)}, status-200 {len(ok)}", flush=True)
    out["clio_ipc"] = {"collapsed": len(rows), "ok200": len(ok),
                       "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:40]]}
    if ok:
        ts, orig, sc, ln, mt = sorted(ok, key=lambda x: int(x[3] or 0))[0]
        out["clio_ipc_sample_wb"] = evidence(f"CLIO IPC smallest wb ({ln} B CDX)", wb(ts, orig),
                                             "clio-" + orig.rsplit("/", 1)[-1])
        out["clio_ipc_live_status"] = head(orig)
        print(f"  live-status {orig[:90]}: {out['clio_ipc_live_status']}", flush=True)
    out["clio_live_sample"] = evidence("CLIO CompositeMeasureofWellbeing_Compact.xlsx live",
                                       "https://clio-infra.eu/data/CompositeMeasureofWellbeing_Compact.xlsx",
                                       "clio-CompositeMeasureofWellbeing_Compact.xlsx")

    print("\n== 4. ATNF psrcat version stack (live) ==", flush=True)
    out["atnf_head"] = {}
    for v in ("psrcat_pkg.tar.gz", "psrcat_pkg.v2.9.0.tar.gz", "psrcat_pkg.v1.45.tar.gz"):
        u = f"https://www.atnf.csiro.au/research/pulsar/psrcat/downloads/{v}"
        out["atnf_head"][v] = head(u)
        print(f"  HEAD {v}: {out['atnf_head'][v]}", flush=True)
    # sample an old version if present in the campaign JSON top list
    camp = json.load(open(sorted(__import__("glob").glob("outputs/campaign5-*.json"))[-1]))
    atnf = [r for r in camp["campaign5_gold"] if "ATNF" in r["label"]][0]
    vers = sorted([t["url"] for t in atnf["top"] if "psrcat_pkg.v" in t["url"]])
    if vers:
        out["atnf_sample_oldest_crawled"] = evidence(f"ATNF oldest crawled version {vers[0].rsplit('/',1)[-1]}",
                                                     vers[0], cap=10_000_000)

    print("\n== 5. Bank of England Millennium + wb annex ==", flush=True)
    mill = "https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/a-millennium-of-macroeconomic-data-for-the-uk.xlsx"
    out["boe_millennium_head"] = head(mill)
    print(f"  HEAD millennium: {out['boe_millennium_head']}", flush=True)
    out["boe_millennium_range"] = evidence("BoE millennium xlsx live (bounded 2MB head)", mill, cap=2_000_000)
    annex = "https://www.bankofengland.co.uk/-/media/boe/files/bank-liabilities-survey/2018/bank-liabilities-survey-annex---2018-q4.xlsx"
    out["boe_annex_live_status"] = head(annex)
    print(f"  live-status 2018-q4 annex: {out['boe_annex_live_status']}", flush=True)
    out["boe_annex_wb"] = evidence("BoE annex 2018-q4 wb2022", wb("20221224155757", annex))

    print("\n== 6. SCOP /files ==", flush=True)
    out["scop"] = [
        evidence("SCOP scop-cla-20200228.txt wb2020", wb("20201202220621", "http://scop.mrc-lmb.cam.ac.uk/files/scop-cla-20200228.txt")),
    ]
    out["scop_live_status"] = {
        "scop-cla-20200228.txt": head("https://scop.mrc-lmb.cam.ac.uk/files/scop-cla-20200228.txt"),
        "scop-cla-latest.txt": head("https://scop.mrc-lmb.cam.ac.uk/files/scop-cla-latest.txt"),
    }
    for k, v in out["scop_live_status"].items():
        print(f"  live-status {k}: {v}", flush=True)

    print("\n== 7. Starling wb xls + live timestr ==", flush=True)
    out["starling_wb"] = [
        evidence("Starling bsh.xls wb2022", wb("20220308004146", "https://starlingdb.org/bsh.xls")),
        evidence("Starling bshet.xls wb2022", wb("20220308004544", "https://starlingdb.org/bshet.xls")),
    ]
    out["starling_live_status"] = {"bsh.xls": head("https://starlingdb.org/bsh.xls"),
                                   "bshet.xls": head("https://starlingdb.org/bshet.xls")}
    for k, v in out["starling_live_status"].items():
        print(f"  live-status {k}: {v}", flush=True)
    out["starling_live"] = [evidence("Starling timestr.zip live", "https://starlingdb.org/timestr.zip")]

    print("\n== 8. Villanova WDCatalog targeted CDX ==", flush=True)
    out["villanova"] = {}
    for prefix in ("astronomy.villanova.edu/WDCatalog/*", "www.astronomy.villanova.edu/WDCatalog/*"):
        rows = cdx(prefix)
        ok = [x for x in rows if x[2] == "200"]
        print(f"  {prefix}: collapsed {len(rows)}, status-200 {len(ok)}", flush=True)
        for ts, orig, sc, ln, mt in ok[:15]:
            print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
        out["villanova"][prefix] = {"collapsed": len(rows), "ok200": len(ok),
                                    "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:40]]}

    print("\n== 9. CATH live phantoms + wb API sample ==", flush=True)
    out["cath_live"] = [
        evidence("CATH text.label live", "https://www.cathdb.info/browse/text.label"),
        evidence("CATH file.fasta live (docs example path)", "https://www.cathdb.info/path/to/file.fasta"),
    ]
    out["cath_wb_sample"] = evidence(
        "CATH API derived .fa wb2011",
        wb("20111217094726", "http://www.cathdb.info:80/api/data/derived_data/00001.00010.00010.00010/SSG5/11/00001.00010.00010.00010__SSG5__11.aln_reps.cora.fa"))

    print("\n== 10. PWT / RUG live sample + PDG + OEIS + UCSC + D-PLACE + MPC ==", flush=True)
    out["rug_live"] = [evidence("RUG hna_bel_09.xls live", "https://www.rug.nl/ggdc/docs/hna_bel_09.xls")]
    out["pdg_live"] = [evidence("PDG mass_width_2026.txt live", "https://pdg.lbl.gov/2026/mcdata/mass_width_2026.txt")]
    out["oeis_live"] = [evidence("OEIS b001006.txt live", "https://oeis.org/A001006/b001006.txt")]
    out["ucsc_gbdb_live_status"] = head("https://hgdownload.soe.ucsc.edu/gbdb/apiMel2/scaffolds/Group1.fa")
    print(f"  UCSC gbdb Group1.fa live-status: {out['ucsc_gbdb_live_status']}", flush=True)
    out["mpc_wb"] = [evidence("MPC asteroid_data.json wb2015", wb("20151026125757", "http://www.minorplanetcenter.net:80/asteroid_explorers/asteroid_data.json"))]

    gh.save({"verify5": out}, "verify5")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
