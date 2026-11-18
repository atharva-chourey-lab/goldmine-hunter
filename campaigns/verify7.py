#!/usr/bin/env python3
"""Verify7 — Campaign 7 (Mammal Wave) targeted verification.
The crawl pass (campaign7_mammal.py) confirmed the probe's
shape: CMS front-ends, sitemaps and furniture. This pass does
the targeted work per seed group: CDX prefix queries filtered
to real data extensions, direct sample downloads of every
concrete catalogue/extract found (size + md5 + magic), the
Wellcome IIIF surface, the archive.org Midlo & Cummins deposit,
and custody checks for the protected systems (documented, never
scraped). Samples to gold/campaign7-verify/. Run from
goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA

OUTDIR = "gold/campaign7-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR
evidence = verify6.evidence

def cdx_filter(prefix, pattern, limit=6000):
    rows = cdx(prefix, limit=limit, extra={"filter": f"original:.*{pattern}.*"})
    return [x for x in rows if x[2] == "200"]

def get_text(url, cap=400_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 1a. Juneau Flukes — find the catalogue PDF ==", flush=True)
    rows = cdx_filter("juneauflukes.org/*", r"\.pdf")
    print(f"  CDX pdf-filtered: {len(rows)} status-200 PDFs", flush=True)
    for ts, orig, sc, ln, mt in rows[:10]:
        print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
    out["juneau_pdfs"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in rows]
    st, html = get_text("https://www.juneauflukes.org/")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    pdf_links = [h for h in hrefs if ".pdf" in h.lower()]
    upl = [h for h in hrefs if "uploads" in h][:15]
    print(f"  homepage {st}: {len(hrefs)} hrefs, pdf links: {pdf_links[:5]}", flush=True)
    out["juneau_home"] = {"status": st, "pdf_links": pdf_links, "upload_links": upl}
    out["juneau_samples"] = []
    cand = [x for x in rows if "catalog" in x[1].lower() or "fluke" in x[1].lower()] or rows
    for ts, orig, sc, ln, mt in cand[:2]:
        out["juneau_samples"].append(evidence(f"Juneau wb PDF ({ln} B CDX)", wb(ts, orig),
                                              "juneau-" + orig.rsplit("/", 1)[-1], cap=30_000_000))
    for link in pdf_links[:1]:
        url = link if link.startswith("http") else "https://www.juneauflukes.org" + link
        out["juneau_samples"].append(evidence("Juneau live PDF", url,
                                              "juneau-live-" + url.rsplit("/", 1)[-1], cap=30_000_000))

    print("\n== 1b. Whitehead Lab — Dominica sperm-whale Flukebook PDF ==", flush=True)
    out["flukebook"] = evidence("Dominica Flukebook 2016 (whitelab live)",
                                "http://whitelab.biology.dal.ca/sge/Flukebook2016.pdf",
                                "dominica-flukebook2016.pdf", cap=30_000_000)

    print("\n== 1c. Southern Ocean — CCAMLR Danco Coast catalogue PDF ==", flush=True)
    out["ccamlr_danco"] = evidence("CCAMLR Danco Coast humpback catalogue (meeting doc)",
                                   "https://meetings.uat.ccamlr.org/es/system/files?file=meeting-documents/2026-06/WG-EMM-2026-67.pdf",
                                   None, cap=8_000_000)

    print("\n== 1d. Coastal Studies (Gulf of Maine) — targeted CDX pdf/csv ==", flush=True)
    out["ccs_cdx"] = {}
    for pat in (r"\.pdf", r"\.csv", r"\.xlsx?"):
        rows = cdx_filter("coastalstudies.org/*", pat)
        out["ccs_cdx"][pat] = len(rows)
        print(f"  coastalstudies {pat}: {len(rows)} status-200", flush=True)

    print("\n== 2. NOAA Beaufort dolphin catalogue — NCEI formal-archive extracts ==", flush=True)
    base = "https://www.ncei.noaa.gov/archive/accession/0254384/1.1/data/0-data/67350/"
    out["beaufort_csv1"] = evidence("Beaufort 2018_match_to_master_catalog.csv (NCEI)",
                                    base + "2018_match_to_master_catalog.csv",
                                    "beaufort-2018_match_to_master_catalog.csv")
    out["beaufort_csv2"] = evidence("Beaufort 2018_SNCES_id_dolphins.csv (NCEI)",
                                    base + "2018_SNCES_id_dolphins.csv",
                                    "beaufort-2018_SNCES_id_dolphins.csv")
    zip_url = "https://www.nodc.noaa.gov/archive/arc0204/0254384/1.1/data/0-data/67350/Photos%20from%20NC%20patterns.zip"
    out["beaufort_photos_zip_head"] = head(zip_url)
    print(f"  photos zip HEAD: {out['beaufort_photos_zip_head']}", flush=True)
    f = verify6.fetch_bounded(zip_url, cap=200_000)
    raw = f["raw"]
    out["beaufort_photos_zip_probe"] = {"status": f["status"], "bytes_sampled": len(raw),
                                        "pk_magic": raw[:2] == b"PK",
                                        "md5_head": hashlib.md5(raw).hexdigest() if raw else None,
                                        "content_length_header": out["beaufort_photos_zip_head"].get("size")}
    print(f"  photos zip probe: {out['beaufort_photos_zip_probe']}", flush=True)

    print("\n== 3a. elephant.se — live database record (published-by-design check) ==", flush=True)
    st, html = get_text("https://www.elephant.se/database2.php?elephant_id=7894")
    has_aerp = "AERP" in html and "Amboseli" in html
    print(f"  elephant.se record page: status {st}, {len(html)} B, AERP/Amboseli fields present: {has_aerp}", flush=True)
    out["elephant_se"] = {"status": st, "bytes": len(html), "aerp_fields": has_aerp,
                          "md5": hashlib.md5(html.encode()).hexdigest() if st else None}
    rows = cdx_filter("elephant.se/*", r"\.(pdf|csv|xlsx?|zip)")
    print(f"  elephant.se CDX data-ext: {len(rows)} status-200", flush=True)
    out["elephant_se_cdx_data"] = len(rows)

    print("\n== 3b. ATE (amboseliephants.org) — reachability + targeted CDX ==", flush=True)
    out["ate_head"] = head("https://www.amboseliephants.org/")
    rows = cdx_filter("amboseliephants.org/*", r"\.(pdf|csv|xlsx?|zip)")
    print(f"  ATE head: {out['ate_head']}; CDX data-ext status-200: {len(rows)}", flush=True)
    for ts, orig, sc, ln, mt in rows[:8]:
        print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
    out["ate_cdx"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in rows[:20]]
    out["ate_samples"] = []
    for ts, orig, sc, ln, mt in rows[:2]:
        out["ate_samples"].append(evidence(f"ATE wb sample ({ln} B CDX)", wb(ts, orig),
                                           "ate-" + orig.rsplit("/", 1)[-1], cap=15_000_000))

    print("\n== 4a. Wellcome Collection — Galton works + IIIF surface ==", flush=True)
    out["wellcome"] = {}
    for wid, label in (("n9q6q77r", "Chimpanzee Fingerprints"), ("dnzrn3kb", "Fingerprints (3,022 images)")):
        try:
            r = requests.get(f"https://api.wellcomecollection.org/catalogue/v2/works/{wid}",
                             headers=UA, timeout=60)
            j = r.json()
            items = j.get("items", [])
            out["wellcome"][wid] = {"api_status": r.status_code, "title": j.get("title"),
                                    "n_items_api": len(items),
                                    "items_sample": [it.get("id") for it in items[:5]]}
            print(f"  work {wid} ({label}): API {r.status_code}, title={j.get('title')!r}, items in API page: {len(items)}", flush=True)
        except Exception as e:
            out["wellcome"][wid] = {"error": str(e)[:140]}
            print(f"  work {wid}: API failed {e}", flush=True)
    # one IIIF image sample from the chimp work's page images (via the work page HTML)
    st, html = get_text("https://wellcomecollection.org/works/n9q6q77r")
    iiif = sorted(set(re.findall(r'(https://iiif\.wellcomecollection\.org/[^"\']+)', html)))
    print(f"  chimp work page {st}: {len(iiif)} IIIF refs in HTML", flush=True)
    out["wellcome"]["iiif_refs_on_chimp_page"] = iiif[:5]
    if iiif:
        img_url = iiif[0]
        if "/info.json" not in img_url and not img_url.endswith((".jpg", ".png")):
            img_url = img_url.rstrip("/") + "/full/800,/0/default.jpg"
        out["wellcome_image_sample"] = evidence("Wellcome IIIF image (Galton work)", img_url,
                                                "wellcome-galton-iiif-sample.jpg", cap=5_000_000)

    print("\n== 4b. Midlo & Cummins 1942 — archive.org deposit ==", flush=True)
    out["midlo"] = {}
    try:
        q = "title:(Palmar and plantar dermatoglyphics in primates)"
        r = requests.get("https://archive.org/advancedsearch.php",
                         params={"q": q, "fl[]": ["identifier", "title", "date"], "output": "json"},
                         headers=UA, timeout=60)
        docs = r.json()["response"]["docs"]
        print(f"  archive.org search: {len(docs)} hits", flush=True)
        for d in docs[:5]:
            print(f"    {d.get('identifier')} — {str(d.get('title'))[:80]}", flush=True)
        out["midlo"]["hits"] = docs[:5]
        if docs:
            ident = docs[0]["identifier"]
            m = requests.get(f"https://archive.org/metadata/{ident}", headers=UA, timeout=60).json()
            files = [{"name": f["name"], "size": f.get("size")} for f in m.get("files", [])
                     if f["name"].lower().endswith((".pdf", ".txt", ".djvu"))][:12]
            out["midlo"]["identifier"] = ident
            out["midlo"]["files"] = files
            print(f"  {ident}: {len(m.get('files', []))} files; doc files: {files[:6]}", flush=True)
            txt_file = next((f for f in m.get("files", []) if f["name"].endswith("_djvu.txt")), None)
            if txt_file:
                out["midlo_text_sample"] = evidence("Midlo & Cummins full text (archive.org)",
                                                     f"https://archive.org/download/{ident}/{txt_file['name']}",
                                                     None, cap=300_000)
    except Exception as e:
        out["midlo"]["error"] = str(e)[:160]
        print(f"  archive.org check failed: {e}", flush=True)

    print("\n== 5. Wagyu / NLBC — targeted CDX for any print-image or data surface ==", flush=True)
    out["wagyu_cdx"] = {}
    for pat in (r"\.(pdf|csv|xlsx?|zip|jpg|jpeg|png)"):
        rows = cdx_filter("wagyu.or.jp/*", pat, limit=4000)
        out["wagyu_cdx"][pat] = len(rows)
        print(f"  wagyu.or.jp {pat}: {len(rows)} status-200", flush=True)
        for ts, orig, sc, ln, mt in rows[:5]:
            print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)

    print("\n== 6. FIT — PeerJ tapir training-set: where the library lives ==", flush=True)
    st, html = get_text("https://pmc.ncbi.nlm.nih.gov/articles/PMC5878928/")
    m = re.search(r"training[- ]set[^<]{0,220}", html, re.I)
    m2 = re.search(r"426 images[^<]{0,160}", html)
    print(f"  PMC tapir paper {st}; training-set mention: {bool(m)}; 426-images mention: {bool(m2)}", flush=True)
    out["fit_pmc"] = {"status": st,
                      "training_set_snippet": (m.group(0)[:220] if m else None),
                      "images426_snippet": (m2.group(0)[:160] if m2 else None)}

    print("\n== 7. Desert Lion — individual-lion pages + Kunene survey PDF ==", flush=True)
    st, html = get_text("http://www.desertlion.info/")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    lion_links = [h for h in hrefs if re.search(r"lion|id|profile|gallery", h, re.I)][:20]
    print(f"  desertlion.info home {st}: {len(hrefs)} hrefs; lion-ish links: {lion_links[:8]}", flush=True)
    out["desertlion_home"] = {"status": st, "n_hrefs": len(hrefs), "lion_links": lion_links}
    out["kunene_survey_pdf"] = evidence("Kunene lion survey 2023 (Conservation Namibia PDF)",
                                        "https://mail.conservationnamibia.com/pdfs/lion-survey-2023.pdf",
                                        None, cap=6_000_000)
    rows = cdx_filter("desertlion.info/*", r"\.(pdf|csv|xlsx?|zip)")
    print(f"  desertlion.info CDX data-ext: {len(rows)} status-200", flush=True)
    out["desertlion_cdx_data"] = len(rows)

    gh.save({"verify7": out}, "verify7")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
