#!/usr/bin/env python3
"""Verify13 — Campaign 13 (Mammal Wave 5) targeted verification.
Standing method (= verify12): sample downloads (size + md5 +
magic), targeted text checks for custody statements, grades in
GRADES.md may only rest on this output. Samples to
gold/campaign13-verify/. Run from goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA

OUTDIR = "gold/campaign13-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR
evidence = verify6.evidence

def get_text(url, cap=900_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def find(txt, pat):
    m = re.search(pat, txt, re.I)
    return m.group(0)[:280] if m else None

def main():
    out = {}

    print("\n== 1. Dental casts — Swindler excerpt + RCS catalogue text ==", flush=True)
    out["swindler"] = evidence("Swindler Primate Dentition excerpt (dental cast collection)",
        "http://assets.cambridge.org/97805216/52896/excerpt/9780521652896_excerpt.pdf", "swindler-dental-cast-excerpt.pdf", cap=15_000_000)
    out["rcs_text_head"] = evidence("RCS Descriptive Catalogue fossil Mammalia djvu text head",
        "https://archive.org/stream/descriptiveillus00roya/descriptiveillus00roya_djvu.txt", "rcs-catalogue-head.txt", cap=400_000)

    print("\n== 2. Antler — B&C sample sheet + S3 chart + subscription text ==", flush=True)
    out["fortcarson_bc"] = evidence("Fort Carson sample B&C score sheet PDF",
        "https://fortcarson.isportsman.net/files/Documents%2FPCMS%20Files%2Fsample-b-c-sheet.pdf", "fortcarson-bc-sample-sheet.pdf", cap=15_000_000)
    out["bc_s3_chart"] = evidence("B&C S3 non-typical mule deer score chart PDF",
        "https://prod10-boone-crockett.s3.amazonaws.com/s3fs-public/2025-01/sc_muledeernt.pdf?VersionId=TMi1cAGz5kz7TQwLBQ_O1hGr6d9YhUm7", "bc-muledeer-chart.pdf", cap=15_000_000)
    st, html = get_text("https://www.boone-crockett.org/boone-and-crockett-club-launches-ai-powered-big-game-records-live-20")
    txt = re.sub(r"<[^>]+>", " ", html)
    out["bc_records_live"] = {"status": st,
        "subscription_snippet": find(txt, r"[^.]{0,80}subscription-based platform[^.]{0,120}"),
        "entries_snippet": find(txt, r"[^.]{0,80}50,000 official trophy entries[^.]{0,80}")}
    print(f"  B&C Records Live page {st}; subscription: {bool(out['bc_records_live']['subscription_snippet'])}", flush=True)
    st, html = get_text("https://magazine.outdoornebraska.gov/blogs/in-the-wild/shed-antler-hunting-in-nebraska/")
    txt = re.sub(r"<[^>]+>", " ", html)
    out["unk_sheds"] = {"status": st,
        "snippet": find(txt, r"[^.]{0,100}cast antler collections[^.]{0,160}")}
    print(f"  UNK magazine {st}; cast-antler snippet: {bool(out['unk_sheds']['snippet'])}", flush=True)

    print("\n== 3. Horn annuli — Montana FWP summaries (3 years) + NWSGC proceedings ==", flush=True)
    out["mt1999"] = evidence("Montana FWP 1999 Bighorn Ram Measurements summary",
        "http://myfwp.mt.gov/getRepositoryFile?objectID=64293", "mt-fwp-bighorn-1999.pdf", cap=15_000_000)
    out["mt2001"] = evidence("Montana FWP 2001 Bighorn Ram Measurements summary",
        "https://myfwp.mt.gov/getRepositoryFile?objectID=64275", "mt-fwp-bighorn-2001.pdf", cap=15_000_000)
    out["mt2006"] = evidence("Montana FWP 2006 Bighorn Ram Measurements summary",
        "https://myfwp.mt.gov/getRepositoryFile?objectID=64295", "mt-fwp-bighorn-2006.pdf", cap=15_000_000)
    out["nwsgc2012"] = evidence("NWSGC 2012 Proceedings (goat horn increments vs cementum)",
        "https://www.nwsgc.net/proceedings/NWSGC_2012/2012Proceedings_complete.pdf", "nwsgc-2012-proceedings.pdf", cap=25_000_000)

    print("\n== 4. Bat wing — PMC 2025 CE paper text (data availability) + Antillean key ==", flush=True)
    st, html = get_text("https://pmc.ncbi.nlm.nih.gov/articles/PMC12527007/")
    txt = re.sub(r"<[^>]+>", " ", html)
    out["bat_pmc"] = {"status": st,
        "photos_snippet": find(txt, r"[^.]{0,80}192 photos[^.]{0,120}"),
        "data_avail_snippet": find(txt, r"Data Availability[^.]{0,220}")}
    print(f"  bat PMC {st}; 192-photos: {bool(out['bat_pmc']['photos_snippet'])}; data-avail: {out['bat_pmc']['data_avail_snippet']}", flush=True)
    out["antillean_key"] = evidence("Field Key to Antillean Bats PDF (archive.org)",
        "https://ia902302.us.archive.org/23/items/fieldkeyantille94bake/fieldkeyantille94bake.pdf", "antillean-bat-key.pdf", cap=15_000_000)

    print("\n== 5. Livestock iris/retinal — IntechOpen protocol + MDPI horse iris ==", flush=True)
    out["intech_retinal"] = evidence("IntechOpen RFID + Optibrand retinal protocol chapter PDF",
        "https://cdn.intechopen.com/pdfs/8497.pdf", "intech-retinal-protocol.pdf", cap=20_000_000)
    out["mdpi_horse_iris"] = evidence("MDPI HIEN horse iris paper (Zhaosu 54-horse dataset)",
        "https://mdpi-res.com/d_attachment/applsci/applsci-15-07191/article_deploy/applsci-15-07191.pdf?version=1750933868", "mdpi-horse-iris.pdf", cap=20_000_000)

    print("\n== 6. Ear notch — Illinois 4-H sheet + Minnesota handbook + UNL text ==", flush=True)
    out["il_4h"] = evidence("Illinois 4-H Notches Not Names spark sheet download",
        "https://4h.extension.illinois.edu/media/1636/download?inline", "illinois4h-notch-sheet.pdf", cap=10_000_000)
    out["mn_handbook"] = evidence("Minnesota Livestock Exhibition Handbook PDF",
        "https://www.bah.state.mn.us/sites/default/files/documents/Livestock-Exhibition-Handbook.pdf", "mn-livestock-handbook.pdf", cap=20_000_000)
    st, html = get_text("https://extensionpubs.unl.edu/publication/g1880/2008/html/view")
    txt = re.sub(r"<[^>]+>", " ", html)
    out["unl_notch"] = {"status": st, "snippet": find(txt, r"[^.]{0,80}Universal Ear-notching System[^.]{0,140}")}
    print(f"  UNL notch page {st}; universal snippet: {bool(out['unl_notch']['snippet'])}", flush=True)

    print("\n== 7. Hyena — Holekamp zip (entries!) + database page text + NSF review PDF ==", flush=True)
    out["holekamp_zip"] = evidence("Holekamp Lab MSU hyena project data files ZIP (live)",
        "https://www.holekamplab.org/uploads/8/7/7/8/87789204/msu_hyena_project_data_files.zip", "msu-hyena-project-data.zip", cap=25_000_000)
    st, html = get_text("https://www.holekamplab.org/project-database.html")
    txt = re.sub(r"<[^>]+>", " ", html)
    out["holekamp_page"] = {"status": st,
        "csv_snippet": find(txt, r"[^.]{0,80}available for download[^.]{0,140}"),
        "sessions_snippet": find(txt, r"[^.]{0,60}61,000 session records[^.]{0,100}")}
    print(f"  Holekamp db page {st}; csv: {bool(out['holekamp_page']['csv_snippet'])}; 61k: {bool(out['holekamp_page']['sessions_snippet'])}", flush=True)
    out["hyena_review"] = evidence("Spagnuolo et al hyena ID review PDF (NSF PAR)",
        "https://par.nsf.gov/servlets/purl/10388664", "hyena-id-review.pdf", cap=20_000_000)

    print("\n== 8. Scar — Rice's whale supplements (xlsx) + MDPI dolphin healing PDF ==", flush=True)
    out["rices_s002"] = evidence("Rice's whale catalog supplement s002 xlsx (PMC)",
        "https://pmc.ncbi.nlm.nih.gov/articles/instance/12416752/bin/pone.0331010.s002.xlsx", "rices-whale-s002.xlsx", cap=10_000_000)
    out["rices_s003"] = evidence("Rice's whale catalog supplement s003 xlsx (PMC)",
        "https://pmc.ncbi.nlm.nih.gov/articles/instance/12416752/bin/pone.0331010.s003.xlsx", "rices-whale-s003.xlsx", cap=10_000_000)
    out["mdpi_dolphin_scar"] = evidence("MDPI dolphin wound-healing scar markers PDF",
        "https://www.mdpi.com/2076-2615/16/2/305/pdf", "mdpi-dolphin-scar.pdf", cap=25_000_000)

    gh.save({"verify13": out}, "verify13")
    print("\nverify13 saved", flush=True)

if __name__ == "__main__":
    main()
