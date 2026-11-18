#!/usr/bin/env python3
"""Verify7b — Campaign 7 corrections and second pass.
Fixes verify7's broken CDX alternation filters (per-extension
queries + local filtering), retries the NCEI CSVs on the working
nodc path, the CCAMLR document on the production meetings host,
the Wellcome items API, the archive.org Midlo & Cummins search,
and inventories the Coastal Studies PDF pile by name.
Run from goldmine-hunter/.
"""
import hashlib, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA

verify6.OUTDIR = "gold/campaign7-verify"
evidence = verify6.evidence
DATA_EXTS = (".pdf", ".csv", ".tsv", ".zip", ".xls", ".xlsx", ".doc", ".docx",
             ".wav", ".mp3", ".mp4", ".mov", ".jpg", ".jpeg", ".png", ".tif", ".tiff")
FURNITURE = ("sitemap", "robots.txt", "favicon", ".css", ".js", "feed", "wlwmanifest")

def ext_counts(domain):
    rows = cdx(f"{domain}/*", limit=9000)
    ok = [x for x in rows if x[2] == "200"]
    data = [x for x in ok if x[1].lower().split("?")[0].endswith(DATA_EXTS)
            and not any(f in x[1].lower() for f in FURNITURE)]
    return ok, data

def main():
    out = {}

    print("\n== Coastal Studies PDF pile — catalogue-shaped names? ==", flush=True)
    rows = cdx("coastalstudies.org/*", limit=9000, extra={"filter": r"original:.*\.pdf"})
    ok = [x for x in rows if x[2] == "200"]
    cat = [x for x in ok if re.search(r"whale|catalog|humpback|fluke|annual|report", x[1], re.I)]
    print(f"  pdf status-200: {len(ok)}; whale/catalog/report-named: {len(cat)}", flush=True)
    for ts, orig, sc, ln, mt in cat[:12]:
        print(f"    {ln} B  {orig[:115]}  ({ts})", flush=True)
    out["ccs"] = {"pdf200": len(ok), "catalog_named": len(cat),
                  "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in cat[:20]]}
    out["ccs_samples"] = []
    for ts, orig, sc, ln, mt in cat[:2]:
        out["ccs_samples"].append(evidence(f"CCS wb PDF ({ln} B CDX)", wb(ts, orig),
                                           "ccs-" + orig.rsplit("/", 1)[-1], cap=15_000_000))

    print("\n== NCEI Beaufort CSVs via nodc path ==", flush=True)
    base = "https://www.nodc.noaa.gov/archive/arc0204/0254384/1.1/data/0-data/67350/"
    out["beaufort_csv1_nodc"] = evidence("Beaufort match-to-master CSV (nodc)",
                                         base + "2018_match_to_master_catalog.csv",
                                         "beaufort-2018_match_to_master_catalog.csv")
    out["beaufort_csv2_nodc"] = evidence("Beaufort SNCES id dolphins CSV (nodc)",
                                         base + "2018_SNCES_id_dolphins.csv",
                                         "beaufort-2018_SNCES_id_dolphins.csv")

    print("\n== CCAMLR Danco catalogue — production meetings host ==", flush=True)
    for host_path in ("https://meetings.ccamlr.org/en/system/files?file=meeting-documents/2026-06/WG-EMM-2026-67.pdf",
                      "https://meetings.ccamlr.org/es/system/files?file=meeting-documents/2026-06/WG-EMM-2026-67.pdf"):
        ev = evidence("CCAMLR Danco PDF (production host)", host_path, None, cap=8_000_000)
        out.setdefault("ccamlr_prod", []).append(ev)
        if ev["verdict"].startswith("REAL"):
            break

    print("\n== Per-extension CDX redo: elephant.se / desertlion.info / wagyu.or.jp / amboseliephants.org ==", flush=True)
    out["ext_redo"] = {}
    for domain in ("elephant.se", "desertlion.info", "wagyu.or.jp", "amboseliephants.org"):
        ok, data = ext_counts(domain)
        interesting = [x for x in data if x[1].lower().split("?")[0].endswith((".pdf", ".csv", ".zip", ".xls", ".xlsx"))]
        print(f"  {domain}: {len(ok)} status-200 collapsed, {len(data)} data-ext (excl. furniture), "
              f"{len(interesting)} doc-type", flush=True)
        for ts, orig, sc, ln, mt in interesting[:8]:
            print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
        out["ext_redo"][domain] = {"ok200": len(ok), "data_ext": len(data),
                                   "doc_type": [{"ts": x[0], "url": x[1], "length": x[3]} for x in interesting[:20]]}

    print("\n== Wellcome items API (include=items) ==", flush=True)
    out["wellcome_items"] = {}
    for wid in ("n9q6q77r", "dnzrn3kb"):
        try:
            r = requests.get(f"https://api.wellcomecollection.org/catalogue/v2/works/{wid}",
                             params={"include": "items"}, headers=UA, timeout=60)
            j = r.json()
            items = j.get("items", [])
            locs = []
            for it in items[:3]:
                for loc in it.get("locations", []):
                    locs.append({"type": loc.get("locationType", {}).get("id"),
                                 "url": loc.get("url")})
            out["wellcome_items"][wid] = {"status": r.status_code, "n_items": len(items), "locations": locs}
            print(f"  {wid}: {r.status_code}, {len(items)} items, locations: {locs[:2]}", flush=True)
        except Exception as e:
            out["wellcome_items"][wid] = {"error": str(e)[:140]}
            print(f"  {wid}: failed {e}", flush=True)
    # sample one IIIF image if a manifest/image location surfaced
    urls = []
    for wid, v in out["wellcome_items"].items():
        for loc in v.get("locations", []) or []:
            if loc.get("url"):
                urls.append(loc["url"])
    out["wellcome_manifest_probe"] = urls[:4]
    for u in urls[:2]:
        try:
            r = requests.get(u, headers=UA, timeout=60)
            print(f"  location fetch {r.status_code} {r.headers.get('Content-Type')} {len(r.content)} B  {u[:100]}", flush=True)
            if "json" in (r.headers.get("Content-Type") or ""):
                mj = r.json()
                canvases = mj.get("sequences", [{}])[0].get("canvases", []) if mj.get("sequences") else mj.get("items", [])
                print(f"    manifest canvases/items: {len(canvases)}", flush=True)
                out["wellcome_manifest"] = {"url": u, "n_canvases": len(canvases)}
                if canvases:
                    img = canvases[0].get("images", [{}])[0].get("resource", {}).get("@id") or \
                          canvases[0].get("items", [{}])[0].get("items", [{}])[0].get("body", {}).get("id")
                    if img:
                        out["wellcome_image_sample"] = evidence("Wellcome IIIF canvas image", img,
                                                                 "wellcome-galton-canvas0.jpg", cap=5_000_000)
                break
        except Exception as e:
            print(f"  location fetch failed: {e}", flush=True)

    print("\n== Midlo & Cummins — archive.org search, corrected queries ==", flush=True)
    out["midlo"] = {}
    for q in ('creator:(Cummins) AND title:(dermatoglyphics)',
              'title:(dermatoglyphics) AND year:1942',
              '"Palmar and plantar dermatoglyphics"'):
        try:
            r = requests.get("https://archive.org/advancedsearch.php",
                             params={"q": q, "fl": "identifier,title,date,creator", "rows": 10, "output": "json"},
                             headers=UA, timeout=60)
            docs = r.json()["response"]["docs"]
            print(f"  q={q!r}: {len(docs)} hits", flush=True)
            for d in docs[:4]:
                print(f"    {d.get('identifier')} — {str(d.get('title'))[:80]}", flush=True)
            out["midlo"][q] = docs[:4]
            if docs:
                ident = docs[0]["identifier"]
                m = requests.get(f"https://archive.org/metadata/{ident}", headers=UA, timeout=60).json()
                files = [{"name": f["name"], "size": f.get("size")} for f in m.get("files", [])
                         if f["name"].lower().endswith((".pdf", ".txt", ".djvu", ".jp2.zip"))][:12]
                out["midlo"]["identifier"] = ident
                out["midlo"]["files"] = files
                print(f"  {ident}: doc files: {files[:6]}", flush=True)
                djvu = next((f for f in m.get("files", []) if f["name"].endswith("_djvu.txt")), None)
                if djvu:
                    out["midlo_text_sample"] = evidence("Midlo & Cummins full text (archive.org)",
                                                         f"https://archive.org/download/{ident}/{djvu['name']}",
                                                         None, cap=300_000)
                break
        except Exception as e:
            print(f"  query failed: {e}", flush=True)
            out["midlo"][q] = {"error": str(e)[:140]}

    gh.save({"verify7b": out}, "verify7b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
