#!/usr/bin/env python3
"""Verify8 — Campaign 8 (Mammal Wave 2) targeted verification.
Standing method (= verify7): targeted CDX prefix queries filtered
to statuscode:200, direct sample downloads of every concrete pile
(size + md5 + magic), custody checks documented and never
circumvented. Samples to gold/campaign8-verify/. Run from
goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA

OUTDIR = "gold/campaign8-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR
evidence = verify6.evidence

def cdx_filter(prefix, pattern, limit=6000):
    rows = cdx(prefix, limit=limit, extra={"filter": f"original:.*{pattern}.*"})
    return [x for x in rows if x[2] == "200"]

def get_text(url, cap=600_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 1a. CMU hair-ID pages — species index + image samples ==", flush=True)
    st, html = get_text("http://people.se.cmich.edu/swans1bj/hair%20id/species.html")
    links = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    sp_links = [h for h in links if h.lower().endswith((".html", ".htm")) and "species" not in h.lower()]
    print(f"  species index {st}: {len(links)} hrefs, {len(sp_links)} species-page links", flush=True)
    out["cmu"] = {"index_status": st, "n_species_links": len(sp_links), "species_links": sp_links[:70]}
    out["cmu_samples"] = []
    base = "http://people.se.cmich.edu/swans1bj/hair%20id/"
    for link in sp_links[:3]:
        url = link if link.startswith("http") else base + link.lstrip("./")
        st2, page = get_text(url)
        imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|gif|png|tif))["\']', page, re.I)))
        print(f"  species page {link}: {st2}, {len(imgs)} image refs", flush=True)
        out["cmu_samples"].append({"page": link, "status": st2, "n_images": len(imgs), "images": imgs[:10]})
        for img in imgs[:2]:
            iurl = img if img.startswith("http") else (url.rsplit("/", 1)[0] + "/" + img)
            out["cmu_samples"].append(evidence(f"CMU hair image ({link})", iurl,
                                               "cmu-" + img.rsplit("/", 1)[-1], cap=3_000_000))

    print("\n== 1b. Texas Tech NSRL — SP-055 hair atlas PDF ==", flush=True)
    st, html = get_text("https://www.depts.ttu.edu/nsrl/publications/special-publications.php")
    pdfs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']*\.pdf)["\']', html, re.I)))
    hair_pdfs = [p for p in pdfs if "55" in p or "hair" in p.lower()]
    print(f"  NSRL page {st}: {len(pdfs)} pdf links, hair/SP55 candidates: {hair_pdfs[:5]}", flush=True)
    out["nsrl"] = {"status": st, "n_pdf_links": len(pdfs), "hair_candidates": hair_pdfs[:5]}
    out["nsrl_sample"] = None
    for p in hair_pdfs[:1]:
        url = p if p.startswith("http") else "https://www.depts.ttu.edu" + (p if p.startswith("/") else "/nsrl/publications/" + p)
        out["nsrl_sample"] = evidence("NSRL SP-055 hair atlas PDF", url,
                                      "nsrl-" + url.rsplit("/", 1)[-1], cap=30_000_000)

    print("\n== 1c. ZSI PDFVolumes — targeted CDX for hair/trichotaxonomy papers ==", flush=True)
    out["zsi"] = {}
    rows = cdx_filter("zsi.gov.in/public/PDFVolumes/*", r"(?i)hair|tricho", limit=8000)
    print(f"  ZSI hair-pattern CDX status-200: {len(rows)}", flush=True)
    for ts, orig, sc, ln, mt in rows[:8]:
        print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
    out["zsi"]["hair_rows"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in rows[:20]]
    out["zsi_sample"] = evidence("ZSI guard-hair paper (discovery-pass URL)",
                                  "https://zsi.gov.in/public/PDFVolumes/records/112/02/0039-0052.pdf",
                                  "zsi-hair-records-112-02.pdf", cap=15_000_000)

    print("\n== 1d. Landcare NZ hair factsheets — species page + image sample ==", flush=True)
    st, html = get_text("https://www.landcareresearch.co.nz/tools-and-resources/identification/hair-sample-identification-and-factsheets")
    hrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)))
    sp = [h for h in hrefs if "hair" in h.lower() and h != hrefs[0]][:20]
    print(f"  Landcare index {st}: {len(hrefs)} hrefs, hair sub-links: {len(sp)}", flush=True)
    out["landcare"] = {"status": st, "sub_links": sp[:20]}
    out["landcare_sample"] = None
    for h in sp[:1]:
        url = h if h.startswith("http") else "https://www.landcareresearch.co.nz" + h
        st2, page = get_text(url)
        imgs = sorted(set(re.findall(r'(?:src)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png))["\']', page, re.I)))
        print(f"  factsheet {url[:90]}: {st2}, {len(imgs)} images", flush=True)
        out["landcare"]["fact_sample"] = {"url": url, "status": st2, "n_images": len(imgs)}
        for img in imgs[:1]:
            iurl = img if img.startswith("http") else "https://www.landcareresearch.co.nz" + img
            out["landcare_sample"] = evidence("Landcare hair factsheet image", iurl,
                                              "landcare-" + iurl.rsplit("/", 1)[-1].split("?")[0], cap=3_000_000)

    print("\n== 2. Koala — is there ANY Adelaide / collection surface? targeted CDX ==", flush=True)
    out["koala_cdx"] = {}
    for pat in (r"(?i)koala.*(finger|dermato|print)", r"(?i)(finger|dermato).*koala"):
        rows = cdx_filter("adelaide.edu.au/*", pat, limit=2000)
        out["koala_cdx"][pat] = len(rows)
        print(f"  adelaide.edu.au {pat}: {len(rows)} status-200", flush=True)

    print("\n== 3. Dog nose — CKC microfiche evidence + PMC dataset-deposit check ==", flush=True)
    st, html = get_text("https://nationalpurebreddogday.com/the-dogs-version-of-the-fingerprint/")
    mf = re.search(r"[^.]{0,160}microfiche[^.]{0,120}\.", html, re.I)
    ckc = re.search(r"[^.]{0,120}Canadian Kennel Club[^.]{0,200}", re.sub(r"<[^>]+>", " ", html), re.I)
    print(f"  NPDD page {st}; microfiche mention: {bool(mf)}", flush=True)
    out["ckc"] = {"status": st, "microfiche_snippet": (mf.group(0)[:280] if mf else None),
                  "ckc_snippet": (ckc.group(0)[:300] if ckc else None)}
    st, html = get_text("https://pmc.ncbi.nlm.nih.gov/articles/PMC8697952/")
    ds = re.search(r"[^.]{0,140}278 images[^.]{0,140}", re.sub(r"<[^>]+>", " ", html), re.I)
    avail = re.search(r"(Data Availability|data availability)[^<]{0,300}", html, re.I)
    print(f"  PMC8697952 {st}; 278-images mention: {bool(ds)}; availability stmt: {bool(avail)}", flush=True)
    out["pmc_nose"] = {"status": st, "dataset_snippet": (ds.group(0)[:280] if ds else None),
                       "availability_snippet": (avail.group(0)[:300] if avail else None)}

    print("\n== 4a. Idaho Virtual Museum — footprint virtualization surface ==", flush=True)
    st, html = get_text("https://virtual.imnh.iri.isu.edu/Home/Sources")
    txt = re.sub(r"<[^>]+>", " ", html)
    appr = re.search(r"[^.]{0,140}approval[^.]{0,140}", txt, re.I)
    print(f"  VMI sources {st}, {len(html)} B; approval-gated mention: {bool(appr)}", flush=True)
    out["idaho_vm"] = {"status": st, "bytes": len(html),
                       "approval_snippet": (appr.group(0)[:280] if appr else None)}

    print("\n== 4b. Murie cast collection — the book is online; is the collection? ==", flush=True)
    out["murie_text"] = evidence("Murie Field Guide to Animal Tracks, full text (archive.org)",
                                  "https://dn720005.ca.archive.org/0/items/peterson-field-guide-animal-tracks/Peterson%20Field%20Guide%20Animal%20Tracks_djvu.txt",
                                  None, cap=300_000)

    print("\n== 5a. Parker elephant dataset handbook (UF formal IR) ==", flush=True)
    out["parker"] = evidence("Parker Elephant Data Set Handbook (UFDC PDF)",
                              "https://ufdcimages.uflib.ufl.edu/IR/00/00/42/09/00001/ParkerElephantDataSetHandbook15.pdf",
                              "parker-elephant-handbook.pdf", cap=15_000_000)

    print("\n== 5b. Elephants for Africa FIT PDF ==", flush=True)
    out["efa_fit"] = evidence("Elephants for Africa FIT project PDF",
                               "https://www.elephantsforafrica.org/wp-content/uploads/2014/07/FootprintIdentificationTechnique.pdf",
                               "efa-fit.pdf", cap=10_000_000)

    print("\n== 6a. EBRWS — uploads inventory + catalogue brochure ==", flush=True)
    rows = cdx_filter("ebrws.com.au/*", r"\.pdf", limit=4000)
    print(f"  ebrws.com.au CDX pdf status-200: {len(rows)}", flush=True)
    for ts, orig, sc, ln, mt in rows[:10]:
        print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
    out["ebrws_cdx_pdfs"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in rows[:25]]
    out["ebrws_brochure"] = evidence("EBRWS 2019 brochure / Photo-ID catalogue (live)",
                                     "https://www.ebrws.com.au/wp-content/uploads/2021/07/Encounter-Bay-Right-Whale-Study-2019-Brochure-edited-2021.pdf",
                                     "ebrws-brochure-2019.pdf", cap=20_000_000)

    print("\n== 6b. Utah Right Whale Collection — one record + its image ==", flush=True)
    st, html = get_text("https://collections.lib.utah.edu/details?id=2148813&facet_setname_s=%22uum_rwc%22")
    imgs = sorted(set(re.findall(r'(https://collections\.lib\.utah\.edu/[^"\']+\.(?:jpg|jpeg))', html, re.I)))
    meta = re.search(r"(19770913_0437_0015|Whale ID|uum_rwc)", html)
    print(f"  Utah record page {st}: {len(imgs)} jpg refs; rwc meta present: {bool(meta)}", flush=True)
    out["utah"] = {"status": st, "n_jpg_refs": len(imgs), "sample_refs": imgs[:4]}
    out["utah_sample"] = None
    for img in imgs[:1]:
        out["utah_sample"] = evidence("Utah RWC whale image", img,
                                       "utah-rwc-" + img.rsplit("/", 1)[-1], cap=4_000_000)

    print("\n== 6c. NARWC custody — access protocol PDF (researcher-only evidence) ==", flush=True)
    out["narwc_access_head"] = head("https://www.narwc.org/uploads/1/1/6/6/116623219/consortium_database_accessfinal04-2025.pdf")
    print(f"  NARWC access PDF HEAD: {out['narwc_access_head']}", flush=True)

    print("\n== 7a. Save the Manatee Club archive — scar-sheet PDFs ==", flush=True)
    out["manatee_scar_main"] = evidence("SMC Blue Spring scar sheets, ALL 10-13 (archive subdomain)",
                                        "https://www.savethemanatee-archive.org/cam_scar_sheets_all_10-13.pdf",
                                        "smc-scar-sheets-all-10-13.pdf", cap=40_000_000)
    out["manatee_scar_mail"] = evidence("SMC scar sheet (mail subdomain)",
                                        "https://mail.savethemanatee-archive.org/ScarSheet.pdf",
                                        "smc-scarsheet-mail.pdf", cap=40_000_000)
    rows = cdx_filter("savethemanatee-archive.org/*", r"\.(pdf|jpg|jpeg|png|csv)", limit=6000)
    print(f"  savethemanatee-archive.org CDX data-ext status-200: {len(rows)}", flush=True)
    for ts, orig, sc, ln, mt in rows[:12]:
        print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
    out["manatee_archive_cdx"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in rows[:30]]
    # page count + text probe of the main scar PDF if it downloaded
    p = os.path.join(OUTDIR, "smc-scar-sheets-all-10-13.pdf")
    if os.path.exists(p):
        try:
            import PyPDF2
            r = PyPDF2.PdfReader(p)
            out["manatee_scar_main_pages"] = len(r.pages)
            t0 = (r.pages[0].extract_text() or "")[:400]
            out["manatee_scar_main_text0"] = t0
            print(f"  scar PDF pages: {len(r.pages)}; page0 text: {t0[:160]!r}", flush=True)
        except Exception as e:
            out["manatee_scar_main_pages"] = f"pypdf failed: {str(e)[:120]}"
            print(f"  pypdf failed: {e}", flush=True)

    print("\n== 7b. FWS manatee documents folder — guidelines only? ==", flush=True)
    out["fws_guidelines"] = evidence("FWS Guidelines for Photography (MIPS intake doc)",
                                      "https://apps.fws.gov/sites/manatee/files/documents/Guidelines%20for%20Photography.pdf",
                                      None, cap=2_000_000)

    gh.save({"verify8": out}, "verify8")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
