#!/usr/bin/env python3
"""Verify16 — Campaign 16 (Broad Wave 3B) targeted verification.
Standing method (= verify6/10): targeted CDX prefix queries filtered
to statuscode:200, direct sample downloads of every concrete pile
(size + md5 + magic), custody checks documented and never
circumvented. Samples to gold/campaign16-verify/. Run from
goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence, fetch_bounded

OUTDIR = "gold/campaign16-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=800_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def links_of(html, exts):
    return sorted(set(re.findall(r'(?:href|src)\s*=\s*["\']([^"\']+\.(?:' + exts + r')(?:\?[^"\']*)?)["\']', html, re.I)))

def hrefs_of(html):
    return sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))

def tiff_evidence(label, url, cap=3_000_000):
    f = fetch_bounded(url, cap)
    raw = f["raw"]
    ev = {"label": label, "url": url, "http_status": f["status"],
          "bytes_downloaded": len(raw), "truncated_at_cap": f.get("truncated", False),
          "content_type": f.get("content_type"),
          "md5_head1mb": hashlib.md5(raw[:1_000_000]).hexdigest() if raw else None,
          "first_bytes_hex": raw[:8].hex() if raw else None}
    if raw[:4] in (b"II*\x00", b"MM\x00*"):
        ev["verdict"] = "REAL — TIFF image (II/MM magic)"
    elif raw.lstrip().lower().startswith((b"<!doctype", b"<html")):
        ev["verdict"] = "PHANTOM — HTML page, not data"
    else:
        ev["verdict"] = "BINARY — non-HTML, non-blank" if raw else "UNREACHABLE / EMPTY"
    print(f"  [{label}] {ev['verdict']} | {len(raw):,} B | {url[:100]}", flush=True)
    return ev

def main():
    out = {}

    print("\n== 1. concrete-test-ledgers — UCI dataset links + journal PDF ==", flush=True)
    st, html = get_text("https://www.datadory.com/datasets/construction-materials/concrete-compressive-strength-dataset")
    hrefs = hrefs_of(html)
    data_links = [h for h in hrefs if re.search(r'\.(csv|zip|xlsx?|txt)(\?|$)', h, re.I) or "ics.uci.edu" in h or "archive.ics" in h]
    print(f"  datadory page {st}: {len(data_links)} data-ish links", flush=True)
    out["concrete_datadory"] = {"status": st, "data_links": data_links[:15]}
    for h in data_links[:2]:
        url = h if h.startswith("http") else "https://www.datadory.com" + (h if h.startswith("/") else "/" + h)
        out.setdefault("concrete_samples", []).append(
            evidence("concrete dataset file", url, "concrete-" + url.rsplit("/", 1)[-1].split("?")[0], cap=6_000_000))
    out["concrete_journal_pdf"] = evidence("Concrete journal 1930-10 PDF (archive.org, cap 6MB)",
                                           "https://archive.org/download/concrete_1930-10_37_4/concrete_1930-10_37_4.pdf",
                                           cap=6_000_000)

    print("\n== 2. pigment-cross-sections — Clowes technical-report PDFs (cross-sections inside) ==", flush=True)
    out["clowes_reports"] = []
    for name in ("c10042a-d.pdf", "c10057.pdf", "c10028.pdf"):
        out["clowes_reports"].append(evidence(f"Clowes technical report {name}",
                                              f"https://paintings.theclowescollection.org/downloads/technical-reports/{name}",
                                              "clowes-" + name, cap=20_000_000))
    st, txt = get_text("https://samplearchives.iccrom.org/oggetti/41651-opd-collection-of-cross-and-thin-sections?i=2")
    out["opd"] = {"status": st, "access_on_request": "upon request" in txt or "opd@cultura.gov.it" in txt,
                  "n_sections_stated": "15 400" in txt or "15400" in txt, "part_not_digital": "not" in txt and "digital form" in txt}
    print(f"  OPD page {st}: access-on-request={out['opd']['access_on_request']}", flush=True)
    out["psa_head"] = head("https://psa.rijksmuseum.nl/")
    print(f"  psa.rijksmuseum.nl HEAD: {out['psa_head']}", flush=True)

    print("\n== 3. playbill-programme-archives — BL OCR zip head + archive.org item files ==", flush=True)
    st, html = get_text("https://bl.iro.bl.uk/entities/product/3876be77-0625-4234-a6bd-2fac173a0712", cap=400_000)
    dl = [h for h in hrefs_of(html) if "playbills-ocr" in h or h.endswith(".zip")]
    print(f"  BL repository page {st}: download links {dl[:3]}", flush=True)
    out["bl_repo"] = {"status": st, "download_links": dl[:5]}
    if dl:
        url = dl[0] if dl[0].startswith("http") else "https://bl.iro.bl.uk" + dl[0]
        out["bl_ocr_zip_head"] = evidence("BL playbills OCR zip (head, cap 6MB of 87.68MB)", url, cap=6_000_000)
    try:
        r = requests.get("https://archive.org/metadata/playbill_the_plymouth_theatre_the_happy_time", headers=UA, timeout=60)
        files = r.json().get("files", []) if r.status_code == 200 else []
        out["ia_playbill_item"] = {"n_files": len(files),
                                    "files": [{"name": f.get("name"), "size": f.get("size")} for f in files[:20]]}
        print(f"  archive.org playbill item: {len(files)} files", flush=True)
        pdfs = [f for f in files if (f.get("name") or "").lower().endswith(".pdf")]
        if pdfs:
            out["ia_playbill_sample"] = evidence("archive.org playbill PDF",
                "https://archive.org/download/playbill_the_plymouth_theatre_the_happy_time/" + pdfs[0]["name"],
                "ia-playbill-" + pdfs[0]["name"], cap=10_000_000)
    except Exception as e:
        out["ia_playbill_item"] = {"error": str(e)[:160]}

    print("\n== 4. factory-payroll-wage-books — CUSTODY-1 prior test ==", flush=True)
    st, html = get_text("https://libserver.jcu.edu.au/specials/Archives/pioneer.html", cap=1_200_000)
    wages_refs = len(re.findall(r"wages book", html, re.I))
    pdf_links = links_of(html, "pdf")
    out["jcu_pioneer"] = {"status": st, "wages_book_refs": wages_refs, "pdf_links": pdf_links[:10],
                          "archive_location_stated": "Archive Location" in html}
    print(f"  JCU Pioneer page {st}: {wages_refs} 'wages book' refs, {len(pdf_links)} PDF links (series listings)", flush=True)
    st, html = get_text("https://calmview.derbyshire.gov.uk/calmview/Record.aspx?src=CalmView.Catalog&id=D6948%2FE%2F9%2F4", cap=400_000)
    out["derbyshire"] = {"status": st, "extent_one_volume": "1 outsize volume" in html,
                         "repository": "Derbyshire Record Office" in html, "has_image_or_file": len(links_of(html, "jpg|pdf"))}
    print(f"  Derbyshire record {st}: 1-volume={out['derbyshire']['extent_one_volume']}, file links={out['derbyshire']['has_image_or_file']}", flush=True)
    st, html = get_text("https://exhibit-archive.library.gatech.edu/fulton_bag/history.html", cap=800_000)
    out["fulton"] = {"status": st, "payroll_mentioned": "payroll" in html.lower(),
                     "personnel_restricted": "restricted" in html.lower() and "confidentiality" in html.lower()}
    print(f"  Fulton page {st}: payroll={out['fulton']['payroll_mentioned']}, personnel-restricted={out['fulton']['personnel_restricted']}", flush=True)

    print("\n== 5. booth-level-election-gazettes — gazette PDF samples (archive.org) ==", flush=True)
    out["mysore_gazette"] = evidence("Mysore Gazette 1948 text PDF (booth statement inside, cap 6MB)",
                                     "https://archive.org/download/karnataka-state-archives-2026-348623/362_PART_2_5_3_JULY_DEC_1948_409_text.pdf",
                                     cap=6_000_000)
    out["himachal_gazette"] = evidence("Himachal Gazette 1986 text PDF (cap 6MB)",
                                       "https://archive.org/download/in.gazette.himachalarchive.1986-09-13.3691/3691_text.pdf",
                                       cap=6_000_000)
    out["india_gazette_1953"] = evidence("Gazette of India 1953 election PDF",
                                         "https://archive.org/download/in.gazette.e.1953.219/E-2260-1953-0009-104687.pdf",
                                         "gazette-india-1953-election.pdf", cap=20_000_000)

    print("\n== 6. seed-catalogue-varieties — USDA Gilbert catalogue PDFs on archive.org ==", flush=True)
    out["seed_1926"] = evidence("1926 Northern Seed catalogue PDF (cap 6MB)",
                                 "https://archive.org/download/CAT31322813/CAT31322813_bw.pdf", cap=6_000_000)
    out["seed_1906"] = evidence("1906 Nebraska Seed catalogue PDF (cap 6MB)",
                                 "https://archive.org/download/CAT31288032/CAT31288032_bw.pdf", cap=6_000_000)
    try:
        r = requests.get("https://archive.org/advancedsearch.php",
                         params={"q": "collection:usda-nurseryandseedcatalog", "fl[]": "identifier", "rows": 1,
                                 "output": "json"}, headers=UA, timeout=60)
        out["ia_usda_seed_collection_count"] = r.json().get("response", {}).get("numFound") if r.status_code == 200 else None
        print(f"  archive.org USDA nursery/seed collection items: {out['ia_usda_seed_collection_count']}", flush=True)
    except Exception as e:
        out["ia_usda_seed_collection_count"] = {"error": str(e)[:120]}

    print("\n== 7. regional-menu-collections — UNLV menu TIFF + NYPL data export ==", flush=True)
    st, html = get_text("https://special.library.unlv.edu/ark%3A/62930/d1br8mz4h", cap=800_000)
    tifs = links_of(html, "tif|tiff")
    print(f"  UNLV men000606 page {st}: tif refs {tifs[:3]}", flush=True)
    out["unlv_item"] = {"status": st, "tif_refs": tifs[:5]}
    if tifs:
        url = tifs[0] if tifs[0].startswith("http") else "https://special.library.unlv.edu" + (tifs[0] if tifs[0].startswith("/") else "/" + tifs[0])
        out["unlv_tif_sample"] = tiff_evidence("UNLV menu men000606 TIFF (cap 3MB)", url, cap=3_000_000)
    st, html = get_text("http://menus.nypl.org/data", cap=800_000)
    hrefs = hrefs_of(html)
    exports = [h for h in hrefs if re.search(r'\.(zip|tgz|tar|csv)', h, re.I)]
    print(f"  menus.nypl.org/data {st}: export links {exports[:5]}", flush=True)
    out["nypl_data"] = {"status": st, "export_links": exports[:8]}
    if exports:
        url = exports[0] if exports[0].startswith("http") else "http://menus.nypl.org" + exports[0]
        out["nypl_export_head"] = evidence("NYPL menus data export (head, cap 6MB)", url, cap=6_000_000)

    print("\n== 8. borehole-well-logs — BGS AGS OGC API sample + USGS Geolog ==", flush=True)
    try:
        r = requests.get("https://ogcapi.bgs.ac.uk/collections/agsboreholeindex/items",
                         params={"limit": 5}, headers=UA, timeout=60)
        j = r.json() if r.status_code == 200 else {}
        feats = j.get("features", [])
        out["bgs_ags_api"] = {"status": r.status_code, "n_features_sample": len(feats),
                              "number_matched": j.get("numberMatched"),
                              "first_props": (feats[0].get("properties") if feats else None)}
        print(f"  BGS AGS OGC API {r.status_code}: sample {len(feats)} features, numberMatched={j.get('numberMatched')}", flush=True)
        if feats:
            with open(os.path.join(OUTDIR, "bgs-ags-api-sample.geojson"), "w") as fh:
                json.dump(j, fh, indent=1)
            out["bgs_ags_api"]["saved_to"] = os.path.join(OUTDIR, "bgs-ags-api-sample.geojson")
            out["bgs_ags_api"]["md5_full"] = hashlib.md5(json.dumps(j, sort_keys=True).encode()).hexdigest()
    except Exception as e:
        out["bgs_ags_api"] = {"error": str(e)[:160]}
    st, txt = get_text("https://www.USGS.gov/centers/oklahoma-texas-water-science-center/science/geolog-locator", cap=400_000)
    out["usgs_geolog"] = {"status": st, "logs_stated_7000": "7,000" in txt, "downloadable": "download" in txt.lower()}
    print(f"  USGS Geolog page {st}: 7000-logs stated={out['usgs_geolog']['logs_stated_7000']}", flush=True)

    print("\n== 9. sunspot-drawings (DRAWINGS angle only) — UCLA/KSO/MWO drawing surfaces ==", flush=True)
    rows = cdx("howard.astro.ucla.edu/pub/obs/drawings/*", limit=10000)
    ok = [x for x in rows if x[2] == "200"]
    out["howard_cdx"] = {"collapsed": len(rows), "ok200": len(ok),
                         "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:25]]}
    print(f"  howard.astro.ucla.edu/pub/obs/drawings CDX: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
    if ok:
        ts, orig, sc, ln, mt = ok[0]
        out["howard_sample"] = evidence("MWO sunspot drawing via Wayback (howard tree)", wb(ts, orig),
                                        "mwo-drawing-" + orig.rsplit("/", 1)[-1], cap=4_000_000)
    out["howard_live_head"] = head("http://howard.astro.ucla.edu/pub/obs/drawings/")
    print(f"  howard live HEAD: {out['howard_live_head']}", flush=True)
    st, html = get_text("https://cesar.kso.ac.at/sunspot_drawings/automatic/", cap=800_000)
    dats = links_of(html, "dat|txt|fits")
    print(f"  KSO CESAR automatic drawings index {st}: {len(dats)} dat/txt/fits refs", flush=True)
    out["kso_automatic"] = {"status": st, "refs": dats[:15]}
    if dats:
        url = dats[0] if dats[0].startswith("http") else "https://cesar.kso.ac.at/sunspot_drawings/automatic/" + dats[0].lstrip("./")
        out["kso_sample"] = evidence("KSO sunspot-drawing DAT", url,
                                     "kso-" + url.rsplit("/", 1)[-1], cap=2_000_000)
    rows = cdx("cesar.kso.ac.at/sunspot_drawings/*", limit=10000)
    ok = [x for x in rows if x[2] == "200" and gh.is_data(x[1])]
    out["kso_cdx"] = {"collapsed": len(rows), "ok200_data": len(ok),
                      "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:20]]}
    print(f"  KSO sunspot_drawings CDX: {len(rows)} collapsed, {len(ok)} status-200 data files", flush=True)
    st, html = get_text("https://www.mtwilson.edu/solar-observing/", cap=800_000)
    hrefs = hrefs_of(html)
    draw = [h for h in hrefs if re.search(r'drawing|sunspot', h, re.I)]
    out["mtwilson"] = {"status": st, "drawing_links": draw[:10]}
    print(f"  mtwilson.edu solar page {st}: drawing links {draw[:5]}", flush=True)

    gh.save({"verify16": out}, "verify16")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
