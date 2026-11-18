#!/usr/bin/env python3
"""Verify11 — Campaign 11 (Mammal Wave 3) targeted verification.
Standing method (= verify7/8): targeted CDX filtered to
statuscode:200, sample downloads with size + md5 + magic for
every graded claim, custody checks documented and never
circumvented. The ExtractCompare demo zips (22-73 MB) are
streamed to /tmp for a full md5 + entry listing; only ONE small
extracted image per zip is saved as the sample, keeping disk
small. Samples to gold/campaign11-verify/. Run from
goldmine-hunter/.

SAFETY: rhino/tiger systems are poaching-sensitive — custody
documentation only, no location data collected or reported.
"""
import hashlib, io, json, os, re, sys, zipfile
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA, evidence

OUTDIR = "gold/campaign11-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=600_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def zip_probe(label, url):
    """Stream a zip to /tmp: full md5, size, entry census; save
    the smallest image entry as the graded sample."""
    ev = {"label": label, "url": url}
    try:
        r = requests.get(url, headers=UA, timeout=300, stream=True, allow_redirects=True)
        ev["http_status"] = r.status_code
        h = hashlib.md5(); total = 0; path = "/tmp/c11-" + url.rsplit("/", 1)[-1]
        with open(path, "wb") as fh:
            for chunk in r.iter_content(262144):
                fh.write(chunk); h.update(chunk); total += len(chunk)
        ev["bytes"] = total; ev["md5_full"] = h.hexdigest()
        with open(path, "rb") as fh:
            ev["magic"] = fh.read(2).decode("latin1")
        z = zipfile.ZipFile(path)
        names = z.namelist()
        imgs = [n for n in names if n.lower().endswith((".jpg", ".jpeg", ".tif", ".tiff", ".png", ".bmp"))]
        mdbs = [n for n in names if n.lower().endswith((".mdb", ".accdb"))]
        ev["n_entries"] = len(names); ev["n_images"] = len(imgs); ev["mdb"] = mdbs[:3]
        ev["entries_sample"] = names[:12]
        if imgs:
            pick = min((z.getinfo(n) for n in imgs), key=lambda i: i.file_size)
            raw = z.read(pick.filename)
            sname = (label.split()[0].lower() + "-sample-" + pick.filename.rsplit("/", 1)[-1]).replace(" ", "_")
            with open(os.path.join(OUTDIR, sname), "wb") as fh:
                fh.write(raw)
            ev["sample"] = {"entry": pick.filename, "bytes": len(raw),
                            "md5": hashlib.md5(raw).hexdigest(),
                            "magic_hex": raw[:3].hex(), "saved_to": os.path.join(OUTDIR, sname)}
        os.remove(path)
        ev["verdict"] = "REAL — valid zip, listed + sampled"
    except Exception as e:
        ev["verdict"] = f"FAILED: {str(e)[:140]}"
    print(f"  [{label}] {ev['verdict']} | {ev.get('bytes','?')} B | md5={ev.get('md5_full')} | entries={ev.get('n_entries')} images={ev.get('n_images')} mdb={ev.get('mdb')}", flush=True)
    return ev

def main():
    out = {}
    CR = "https://www.conservationresearch.org.uk/Home/ExtractCompare"

    print("\n== 1. ExtractCompare demo zips — the wave's only loose-file piles ==", flush=True)
    out["tiger_zip"] = zip_probe("Tiger demo folders zip", f"{CR}/tiger/tiger_demo_folders.zip")
    out["leopard_zip"] = zip_probe("Leopard demo folders zip", f"{CR}/leopard/leopard_demo_folders.zip")
    out["zebra_zip"] = zip_probe("Zebra demo folders zip", f"{CR}/zebra/zebra_demo_folders.zip")
    out["giraffe_zip"] = zip_probe("Giraffe demo folders zip", f"{CR}/giraffe/giraffe_demo_folders.zip")
    out["clouded_zip"] = zip_probe("Clouded leopard demo zip", f"{CR}/clouded_leopard/clouded_leopard_demo.zip")
    out["extractcompare_install_head"] = head("https://www.conservationresearch.org.uk/onewebmedia/ExtractCompare_install.zip")
    print(f"  install zip HEAD: {out['extractcompare_install_head']}", flush=True)

    print("\n== 2. SealID — DOI landing (Etsin/Fairdata) + paper PDF ==", flush=True)
    st, html = get_text("https://etsin.fairdata.fi/dataset/22b5191e-f24b-4457-93d3-95797c900fc0")
    txt = re.sub(r"<[^>]+>", " ", html)
    print(f"  Etsin dataset page {st}, {len(html)} B", flush=True)
    out["sealid_etsin"] = {"status": st, "bytes": len(html),
                           "snippet": (re.search(r"[^.]{0,120}Saimaa[^.]{0,160}", txt).group(0)[:280] if re.search(r"Saimaa", txt) else None)}
    out["sealid_paper"] = evidence("SealID paper PDF (MDPI Sensors 2022)",
                                   "https://www.mdpi.com/1424-8220/22/19/7602/pdf",
                                   "sealid-sensors-2022.pdf", cap=12_000_000)

    print("\n== 3. Monk seal Cabo Blanco report — Wayback for the unreachable host ==", flush=True)
    rows = cdx("freqstats.marineland.fr/dl/*", limit=2000)
    ok = [x for x in rows if x[2] == "200"]
    print(f"  freqstats /dl CDX: {len(rows)} collapsed, {len(ok)} status-200", flush=True)
    for ts, orig, sc, ln, mt in ok[:8]:
        print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
    out["monk_cdx"] = {"collapsed": len(rows), "ok200": len(ok),
                       "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:15]]}
    out["monk_sample"] = None
    monk = [x for x in ok if "monk" in x[1].lower() and x[1].lower().endswith(".pdf")]
    if monk:
        ts, orig, sc, ln, mt = monk[0]
        out["monk_sample"] = evidence(f"Monk seal annual report wb ({ln} B CDX)", wb(ts, orig),
                                      "monk-seal-report-2017-2018.pdf", cap=20_000_000)
    out["noaa_inport_head"] = head("https://www.fisheries.noaa.gov/inport/item/28581")
    st, html = get_text("https://www.fisheries.noaa.gov/inport/item/28581")
    m = re.search(r"No Distributions[^<]{0,60}", html)
    print(f"  NOAA InPort {st}; 'No Distributions' present: {bool(m)}", flush=True)
    out["noaa_inport"] = {"status": st, "no_distributions_snippet": (m.group(0)[:120] if m else None)}

    print("\n== 4. Tooth-wear charts — agency PDFs + the published known-age comparison ==", flush=True)
    out["tpwd_pdf"] = evidence("TPWD White-tailed Deer Harvest Records / age bulletin (official)",
                                "https://tpwd.texas.gov/publications/pwdpubs/media/pwd_rp_w7000_1135.pdf",
                                "tpwd-deer-age-bulletin.pdf", cap=5_000_000)
    out["east_paper"] = evidence("East Foundation — Foley et al. TRW vs CA vs known-age (Wildlife Research 2021)",
                                  "https://eastfoundation.net/wp-content/uploads/2024/09/wr21050.pdf",
                                  "foley-trw-ca-known-age-2021.pdf", cap=5_000_000)
    out["boone_pdf"] = evidence("Boone & Crockett Fair Chase Summer 2008 — Deer Ages (Severinghaus tradition)",
                                 "https://aws.boone-crockett.org/s3fs-public/atoms/files/FC_Summer2008_DeerAges.pdf",
                                 "boone-crockett-deer-ages-2008.pdf", cap=10_000_000)

    print("\n== 5. Cementum — Matson order form, the deleted MN report, lab surface ==", flush=True)
    out["matson_xlsx"] = evidence("Matson's Laboratory — Biologist Order Form xlsx (live uploads)",
                                   "https://matsonslab.com/wp-content/uploads/2025/02/Biologist-Order-Form.xlsx",
                                   "matson-order-form.xlsx", cap=2_000_000)
    rows = cdx("leg.mn.gov/docs/2013/other/C130010.pdf", limit=100)
    ok5 = [x for x in rows if x[2] == "200"]
    print(f"  leg.mn.gov C130010 CDX: {len(rows)} collapsed, {len(ok5)} status-200", flush=True)
    out["mn_cdx"] = {"collapsed": len(rows), "ok200": len(ok5),
                     "rows": [{"ts": x[0], "length": x[3]} for x in ok5[:5]]}
    out["mn_sample"] = None
    if ok5:
        ts, orig, sc, ln, mt = ok5[0]
        out["mn_sample"] = evidence(f"Matson MN DNR cementum report wb ({ln} B CDX)", wb(ts, orig),
                                    "matson-mn-dnr-cementum-report-2006.pdf", cap=15_000_000)
    out["mn_live_head"] = head("https://www.leg.mn.gov/docs/2013/other/C130010.pdf")
    print(f"  leg.mn.gov live HEAD (expect 404): {out['mn_live_head']}", flush=True)

    print("\n== 6. Rhino custody — RhODIS scale + notch-system text probes (no files, no locations) ==", flush=True)
    st, html = get_text("https://rhinos.org/blog/genetic-factors-to-improve-rhino-management/")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,100}180,000 samples[^.]{0,80}", txt)
    print(f"  IRF RhODIS page {st}; 180k-samples mention: {bool(m)}", flush=True)
    out["rhodis_irf"] = {"status": st, "snippet": (m.group(0)[:260] if m else None)}
    st, html = get_text("https://www.savetherhino.org/africa/south-africa/how-do-you-identify-black-rhinos/")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,100}personal rhino file[^.]{0,120}", txt)
    print(f"  SaveTheRhino page {st}; 'personal rhino file' mention: {bool(m)}", flush=True)
    out["savetherhino"] = {"status": st, "snippet": (m.group(0)[:280] if m else None)}

    print("\n== 7. Primate faces — PrimNet/ChimpFace paper + JGI archive probe ==", flush=True)
    out["primnet_paper"] = evidence("PrimNet — Face Recognition: Primates in the Wild (arXiv 1804.08790)",
                                     "https://arxiv.org/pdf/1804.08790",
                                     "primnet-primates-in-the-wild.pdf", cap=12_000_000)
    st, html = get_text("https://news.janegoodall.org/2018/07/29/the-future-using-ai-in-gombe/")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,120}most comprehensive[^.]{0,120}", txt, re.I)
    print(f"  JGI news {st}; archive-comprehensive mention: {bool(m)}", flush=True)
    out["jgi"] = {"status": st, "snippet": (m.group(0)[:280] if m else None)}

    print("\n== 8. GZGC — LILA page census + GCP tarball HEAD (10.4 GB, never downloaded) ==", flush=True)
    out["gzgc_head"] = head("https://storage.googleapis.com/public-datasets-lila/wild-me/gzgc.coco.tar.gz")
    print(f"  GZGC tar HEAD: {out['gzgc_head']}", flush=True)
    st, html = get_text("https://lila.science/datasets/great-zebra-giraffe-id")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,80}2,056 combined names[^.]{0,120}", txt)
    print(f"  LILA GZGC page {st}; census mention: {bool(m)}", flush=True)
    out["gzgc_page"] = {"status": st, "snippet": (m.group(0)[:260] if m else None)}

    gh.save({"verify11": out}, "verify11")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
