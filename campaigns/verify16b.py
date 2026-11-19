#!/usr/bin/env python3
"""Verify16b — Campaign 16 follow-up pass: fixes the samples
verify16 missed (UCI file behind its landing page, IA playbill
PDF stub, JCU listing PDF, UNLV/NYPL menu surfaces, howard/KSO
CDX row detail, MWO drawings page). Same evidence discipline.
Samples to gold/campaign16-verify/. Run from goldmine-hunter/.
"""
import collections, hashlib, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence

OUTDIR = "gold/campaign16-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=900_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def hrefs_of(html):
    return sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))

def cdx_raw(prefix, limit=2000, extra=None):
    params = {"url": prefix, "output": "json", "fl": "timestamp,original,statuscode,length,mimetype",
              "collapse": "urlkey", "limit": limit}
    if extra:
        params.update(extra)
    try:
        r = requests.get("http://web.archive.org/cdx/search/cdx", params=params, headers=UA, timeout=120)
        r.raise_for_status()
        rows = r.json()
        return rows[1:] if len(rows) > 1 else []
    except Exception as e:
        print(f"  CDX raw failed {prefix}: {e}", flush=True)
        return []

def main():
    out = {}

    print("\n== 1b. UCI concrete dataset — real file behind the landing page ==", flush=True)
    st, html = get_text("https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength")
    hrefs = hrefs_of(html)
    zips = [h for h in hrefs if re.search(r'\.(zip|csv|xlsx?)(\?|$)', h, re.I)]
    print(f"  UCI page {st}: file links {zips[:5]}", flush=True)
    out["uci"] = {"status": st, "file_links": zips[:8]}
    if zips:
        url = zips[0] if zips[0].startswith("http") else "https://archive.ics.uci.edu" + zips[0]
        out["uci_sample"] = evidence("UCI concrete dataset file", url,
                                     "uci-" + url.rsplit("/", 1)[-1].split("?")[0], cap=6_000_000)

    print("\n== 3b. IA playbill — djvu text sample (PDF fetch returned a 172B stub) ==", flush=True)
    out["ia_playbill_djvu"] = evidence("IA playbill djvu text (Plymouth Theatre, The Happy Time, 1951)",
        "https://archive.org/download/playbill_the_plymouth_theatre_the_happy_time/playbill_the_plymouth_theatre_the_happy_time_djvu.txt",
        "ia-playbill-djvu.txt", cap=2_000_000)
    out["ia_playbill_pdf_retry"] = evidence("IA playbill PDF retry (cap 6MB)",
        "https://archive.org/download/playbill_the_plymouth_theatre_the_happy_time/playbill_the_plymouth_theatre_the_happy_time.pdf",
        cap=6_000_000)

    print("\n== 4b. JCU Pioneer — one series-listing PDF sample ==", flush=True)
    st, html = get_text("https://libserver.jcu.edu.au/specials/Archives/pioneer.html", cap=1_200_000)
    pdfs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+\.pdf)["\']', html, re.I)))
    print(f"  pioneer page {st}: pdf hrefs {pdfs[:8]}", flush=True)
    out["jcu_pdfs"] = pdfs[:10]
    if pdfs:
        from urllib.parse import quote
        url = "https://libserver.jcu.edu.au/specials/Archives/" + quote(pdfs[0])
        out["jcu_listing_sample"] = evidence("JCU Pioneer series listing PDF", url,
                                             "jcu-" + pdfs[0].replace(" ", "_"), cap=10_000_000)

    print("\n== 7b. Menus — UNLV retry + Wayback, curatingmenus CSVs, NYPL current data page ==", flush=True)
    st, html = get_text("https://special.library.unlv.edu/node/312816", cap=900_000)
    tifs = sorted(set(re.findall(r'(?:href|src)\s*=\s*["\']([^"\']+\.tiff?(?:\?[^"\']*)?)["\']', html, re.I)))
    print(f"  UNLV node/312816 (men000105) {st}: tif refs {tifs[:3]}", flush=True)
    out["unlv_node"] = {"status": st, "tif_refs": tifs[:5]}
    rows = cdx_raw("special.library.unlv.edu/*", limit=3000, extra={"filter": r"original:.*men000.*\.tif.*"})
    ok = [x for x in rows if x[2] == "200"]
    out["unlv_cdx_tif"] = {"collapsed": len(rows), "ok200": len(ok),
                           "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:10]]}
    print(f"  UNLV tif CDX: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
    if ok:
        ts, orig, sc, ln, mt = ok[0]
        f = verify6.fetch_bounded(wb(ts, orig), 3_000_000)
        raw = f["raw"]
        out["unlv_wb_tif_sample"] = {"url": wb(ts, orig), "http_status": f["status"], "bytes_downloaded": len(raw),
                                     "md5_head1mb": hashlib.md5(raw[:1_000_000]).hexdigest() if raw else None,
                                     "first_bytes_hex": raw[:8].hex() if raw else None,
                                     "verdict": "REAL — TIFF image (II/MM magic)" if raw[:4] in (b"II*\x00", b"MM\x00*") else "see bytes"}
        print(f"  UNLV wb tif sample: {out['unlv_wb_tif_sample']['verdict']} | {len(raw):,} B", flush=True)
    out["curatingmenus_samples"] = []
    for name in ("Dish.csv", "Menu.csv"):
        out["curatingmenus_samples"].append(evidence(f"curatingmenus data-dictionary {name}",
            f"http://curatingmenus.org/data_dictionary/{name}", "nypl-dict-" + name, cap=3_000_000))
    st, html = get_text("https://www.nypl.org/research/support/whats-on-the-menu", cap=600_000)
    hrefs = hrefs_of(html)
    dl = [h for h in hrefs if re.search(r'menus|data', h, re.I)][:15]
    out["nypl_support_page"] = {"status": st, "menu_data_links": dl}
    print(f"  NYPL support page {st}: links {dl[:5]}", flush=True)

    print("\n== 6b. Seed collection count, exact collection query ==", flush=True)
    try:
        r = requests.get("https://archive.org/advancedsearch.php",
                         params={"q": "collection:(usda-nurseryandseedcatalog)", "fl[]": "identifier",
                                 "rows": 1, "output": "json"}, headers=UA, timeout=60)
        out["ia_usda_seed_exact"] = r.json().get("response", {}).get("numFound") if r.status_code == 200 else None
        print(f"  exact collection numFound: {out['ia_usda_seed_exact']}", flush=True)
    except Exception as e:
        out["ia_usda_seed_exact"] = {"error": str(e)[:120]}

    print("\n== 9b. Sunspot drawings — howard/KSO CDX row detail + MWO drawings page ==", flush=True)
    for prefix in ("howard.astro.ucla.edu/pub/obs/drawings/1999/*",
                   "howard.astro.ucla.edu/pub/obs/drawings/*"):
        rows = cdx_raw(prefix, limit=3000)
        statuses = collections.Counter(x[2] for x in rows)
        print(f"  CDX {prefix}: {len(rows)} rows, statuses {dict(statuses)}", flush=True)
        out.setdefault("howard_detail", {})[prefix] = {"n": len(rows), "statuses": dict(statuses),
                                                       "sample": [list(x) for x in rows[:8]]}
        ok = [x for x in rows if x[2] == "200"]
        if ok and "howard_sample" not in out:
            ts, orig, sc, ln, mt = ok[0]
            out["howard_sample"] = evidence("MWO drawing via Wayback (howard tree)", wb(ts, orig),
                                            "mwo-drawing-" + orig.rsplit("/", 1)[-1], cap=4_000_000)
    rows = cdx_raw("cesar.kso.ac.at/sunspot_drawings/*", limit=3000)
    statuses = collections.Counter(x[2] for x in rows)
    print(f"  CDX cesar sunspot_drawings: {len(rows)} rows, statuses {dict(statuses)}", flush=True)
    out["kso_detail"] = {"n": len(rows), "statuses": dict(statuses), "sample": [list(x) for x in rows[:10]]}
    st, html = get_text("https://cesar.kso.ac.at/sunspot_drawings/automatic/", cap=900_000)
    hrefs = hrefs_of(html)
    out["kso_auto_hrefs"] = hrefs[:25]
    print(f"  KSO automatic index {st}: {len(hrefs)} hrefs, sample {hrefs[:8]}", flush=True)
    st, html = get_text("https://www.mtwilson.edu/sunspot-drawings", cap=900_000)
    hrefs = hrefs_of(html)
    imgs = sorted(set(re.findall(r'src\s*=\s*["\']([^"\']+\.(?:gif|jpg|jpeg|png))["\']', html, re.I)))
    out["mwo_drawings_page"] = {"status": st, "hrefs_sample": hrefs[:20], "images": imgs[:15]}
    print(f"  mtwilson.edu/sunspot-drawings {st}: {len(hrefs)} hrefs, {len(imgs)} images", flush=True)
    cand = [i for i in imgs if re.search(r'draw|sunspot|spot', i, re.I)] or imgs[:1]
    if cand:
        url = cand[0] if cand[0].startswith("http") else "https://www.mtwilson.edu" + cand[0]
        out["mwo_drawing_sample"] = evidence("MWO sunspot drawing image (mtwilson.edu)", url,
                                             "mwo-" + url.rsplit("/", 1)[-1].split("?")[0], cap=4_000_000)

    gh.save({"verify16b": out}, "verify16b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
