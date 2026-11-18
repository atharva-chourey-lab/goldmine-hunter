#!/usr/bin/env python3
"""Verify12 — Campaign 12 (Mammal Wave 4) targeted verification.
Standing method (= verify7/8): sample downloads (size + md5 +
magic), targeted text checks for custody statements, grades in
GRADES.md may only rest on this output. Samples to
gold/campaign12-verify/. Run from goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA

OUTDIR = "gold/campaign12-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR
evidence = verify6.evidence

def get_text(url, cap=900_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 1. Palm/sole dermatoglyphics — journal PDF samples ==", flush=True)
    out["turkish_atd"] = evidence("Turkish J Pediatr 1970 Down dermatoglyphics (atd tables)",
        "https://turkjpediatr.org/article/download/4340/4948/48939", "turkish-atd-1970.pdf", cap=15_000_000)
    out["ijbm_atd"] = evidence("IJBM 2023 Kosova atd comparison",
        "https://www.ijbm.org/articles/i51/ijbm_13(3)_oa15.pdf", "ijbm-atd-2023.pdf", cap=15_000_000)

    print("\n== 2. Paw-pad — Murie full text + Amherst sheet ==", flush=True)
    out["murie_text_head"] = evidence("Murie Peterson Field Guide djvu text (archive.org)",
        "https://dn720005.ca.archive.org/0/items/peterson-field-guide-animal-tracks/Peterson%20Field%20Guide%20Animal%20Tracks_djvu.txt",
        "murie-tracks-text-head.txt", cap=400_000)
    out["amherst_sheet"] = evidence("Amherst Tracks and Scat ID sheet",
        "https://cpb-us-w2.wpmucdn.com/wordpress.amherst.edu/dist/3/137/files/2020/03/Track-and-Scat-Identification-1.pdf",
        "amherst-tracks-scat.pdf", cap=10_000_000)

    print("\n== 3. Bear — Virginia rule page text + Hokkaido data-paper check ==", flush=True)
    st, html = get_text("https://dwr.virginia.gov/blog/how-to-judge-the-age-and-sex-of-black-bears/")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,120}front paw track of 4[^.]{0,160}\.", txt, re.I)
    print(f"  Virginia DWR {st}; paw rule snippet: {bool(m)}", flush=True)
    out["virginia"] = {"status": st, "paw_rule_snippet": (m.group(0)[:300] if m else None)}
    st, html = get_text("https://esj-journals.onlinelibrary.wiley.com/doi/10.1111/1440-1703.70054")
    txt = re.sub(r"<[^>]+>", " ", html)
    m2 = re.search(r"[^.]{0,100}ERDP-2026-01[^.]{0,100}", txt)
    m3 = re.search(r"[^.]{0,100}front paw width[^.]{0,140}", txt, re.I)
    print(f"  Hokkaido paper page {st}; ERDP id: {bool(m2)}; paw-width: {bool(m3)}", flush=True)
    out["hokkaido"] = {"status": st, "erdp_snippet": (m2.group(0)[:240] if m2 else None),
                       "paw_width_snippet": (m3.group(0)[:280] if m3 else None)}

    print("\n== 4/5. Canid + snow-track — NASA ORNL DAAC 2188 formal dataset ==", flush=True)
    out["nasa_pdf"] = evidence("NASA Snow Wildlife Tracks user guide PDF (ORNL DAAC 2188)",
        "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Wildlife_Tracks_AK_WA/comp/Snow_Wildlife_Tracks_AK_WA.pdf",
        "nasa-snow-tracks-guide.pdf", cap=15_000_000)
    out["nasa_zip_head"] = head("https://data.ornldaac.earthdata.nasa.gov/protected/bundle/Snow_Wildlife_Tracks_AK_WA_2188.zip")
    print(f"  NASA bundle HEAD: {out['nasa_zip_head']}", flush=True)
    st, html = get_text("https://catalog.data.gov/dataset/snow-properties-and-wildlife-tracks-in-washington-and-alaska")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,80}707 sites[^.]{0,120}", txt)
    print(f"  data.gov {st}; 707-sites snippet: {bool(m)}", flush=True)
    out["datagov"] = {"status": st, "snippet": (m.group(0)[:240] if m else None)}

    print("\n== 5b. Finland Luke wildlife triangles — open-file check ==", flush=True)
    st, html = get_text("https://www.luke.fi/en")
    print(f"  luke.fi/en {st}, {len(html)} B", flush=True)
    out["luke"] = {"status": st, "bytes": len(html)}

    print("\n== 6. Elephant tusk — Pachyderm Who's Who paper (custody + tusk fields) ==", flush=True)
    out["pachyderm"] = evidence("Pachyderm Who's Who & Whereabouts paper",
        "https://Pachydermjournal.org/index.php/pachyderm/article/download/482/498", "pachyderm-whoswho.pdf", cap=20_000_000)

    print("\n== 7. Cheetah — Kelly personal-site PDF + Mara-Meru report ==", flush=True)
    out["kelly"] = evidence("Kelly 2001 Serengeti cheetah computer-aided ID (mjkelly.info personal site)",
        "http://mjkelly.info/ewExternalFiles/computeraid.pdf", "kelly-cheetah-2001.pdf", cap=15_000_000)
    out["marameru"] = evidence("Mara-Meru Cheetah Project Annual Report 2022",
        "https://romanwildlifefoundation.com/files/uploads/annual-report-2022.pdf", "marameru-2022.pdf", cap=25_000_000)

    print("\n== 8. Snow leopard — SLT page text (PAWS custody, no file pile) ==", flush=True)
    st, html = get_text("https://snowleopard.org/the-ghost-trackers-how-indigenous-women-are-leading-snow-leopard-conservation-in-the-himalayas/")
    txt = re.sub(r"<[^>]+>", " ", html)
    m = re.search(r"[^.]{0,100}one million images[^.]{0,120}", txt, re.I)
    m2 = re.search(r"[^.]{0,100}rosette[^.]{0,120}", txt, re.I)
    print(f"  SLT ghost-trackers {st}; 1M-images: {bool(m)}; rosette: {bool(m2)}", flush=True)
    out["slt"] = {"status": st, "million_snippet": (m.group(0)[:260] if m else None),
                  "rosette_snippet": (m2.group(0)[:260] if m2 else None)}

    print("\n== 10. Pangolin — PUNS preprint + CITES methods + WTI guide ==", flush=True)
    out["puns"] = evidence("PUNS pangolin notching preprint (EcoEvoRxiv)",
        "https://ecoevorxiv.org/repository/object/6274/download/12204/", "puns-preprint.pdf", cap=15_000_000)
    out["cites_pangolin"] = evidence("CITES CoP18 IUCN pangolin monitoring methods",
        "https://cites.org/sites/default/files/eng/cop/18/inf/P-CoP18-Inf-075.pdf", "cites-pangolin-methods.pdf", cap=20_000_000)
    out["wti_guide"] = evidence("WTI Wildlife ID & Post-Seizure Guide",
        "https://www.wti.org.in/wp-content/uploads/2026/03/SPECIES-ID-POST-IDENTIFICATION-GUIDE.pdf", "wti-seizure-guide.pdf", cap=25_000_000)

    print("\n== Wisconsin wolf report sample ==", flush=True)
    out["wisconsin_wolf"] = evidence("Wisconsin Gray Wolf Monitoring Report 2025-26",
        "https://preprod-wpr-main.pantheonsite.io/wp-content/uploads/2026/09/2026-Annual-Wolf-Report_July2026.pdf",
        "wisconsin-wolf-2026.pdf", cap=20_000_000)

    gh.save({"verify12": out}, "verify12")
    print("\nverify12 saved", flush=True)

if __name__ == "__main__":
    main()
