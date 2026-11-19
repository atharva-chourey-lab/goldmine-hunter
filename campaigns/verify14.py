#!/usr/bin/env python3
"""Verify14 — Campaign 14 (Mammal Wave 6) targeted verification.
Standing method (= verify12): sample downloads (size + md5 +
magic), targeted text checks for custody/comparison statements,
grades in GRADES.md may only rest on this output. Samples to
gold/campaign14-verify/. Run from goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA

OUTDIR = "gold/campaign14-verify"
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

    print("\n== 1. Hair medulla — hairatlas.hu pile count + samples ==", flush=True)
    rows = cdx("hairatlas.hu/pdf/*", limit=8000)
    ok200 = [r for r in rows if str(r[2]) == "200"]
    print(f"  hairatlas.hu/pdf/* CDX rows={len(rows)} status200={len(ok200)}", flush=True)
    out["hairatlas_cdx"] = {"rows": len(rows), "status200": len(ok200),
                            "sample_urls": [r[1] for r in ok200[:12]]}
    out["hair_atlas_spread"] = evidence("Hair Atlas Cervidae & Bovidae spread (medulla/cross-section)",
        "https://hairatlas.hu/pdf/Hair_atlas_212-213.pdf", "hair-atlas-212-213.pdf", cap=15_000_000)
    out["hair_atlas_soricomorpha"] = evidence("Hair Atlas Soricomorpha spread (medulla/cross-section)",
        "http://hairatlas.hu/pdf/Hair_atlas_90-91.pdf", "hair-atlas-90-91.pdf", cap=15_000_000)
    out["zsi_ratufa"] = evidence("ZSI Trichotaxonomy of Ratufa (medullary index + cross-section)",
        "https://zsi.gov.in/public/PDFVolumes/records/110/03/0037-0057.pdf", "zsi-ratufa-trichotaxonomy.pdf", cap=15_000_000)
    out["hyena_medulla"] = evidence("De & Chakraborty hyena guard hair (medullary index 0.57, Zenodo/BHL)",
        "https://zenodo.org/records/13475121/files/bhlpart155754.pdf?download=1", "hyena-medulla-bhl.pdf", cap=15_000_000)

    print("\n== 2. Sheep/goat nose prints — 4-H paper system text check ==", flush=True)
    st, html = get_text("https://www.slideshare.net/slideshow/2006-an-evaluation-of-retinal-imaging-technology-for-4h-beef-and-sheep-identification/3310171")
    txt = re.sub(r"<[^>]+>", " ", html or "")
    m = re.search(r"[^.]{0,100}nose print[^.]{0,140}", txt, re.I)
    print(f"  slideshare JOE mirror {st}; nose-print snippet: {bool(m)}", flush=True)
    out["joe_4h"] = {"status": st, "snippet": (m.group(0)[:280] if m else None),
                     "note": "Indiana 4-H: 491 beef + 220 sheep enrolled, nose prints on index cards by county committees (discovery-pass full text)"}

    print("\n== 3. Cat nose — Tentieva 2025 paper text check ==", flush=True)
    st, html = get_text("https://knau-bulletin.com/en/journals/tom-23-2-2025/kharakteristika-papillyarnogo-stroyeniya-nosogubnogo-zerkala-koshek")
    txt = re.sub(r"<[^>]+>", " ", html or "")
    m = re.search(r"[^.]{0,80}157 cats[^.]{0,140}", txt)
    m2 = re.search(r"[^.]{0,80}stamp pad[^.]{0,120}", txt, re.I)
    print(f"  KNAU page {st}; 157-cats: {bool(m)}; stamp-pad: {bool(m2)}", flush=True)
    out["tentieva"] = {"status": st, "n157_snippet": (m.group(0)[:260] if m else None),
                       "stamp_snippet": (m2.group(0)[:260] if m2 else None)}

    print("\n== 4. Hoof — NMSU guide sample ==", flush=True)
    out["nmsu_tracks"] = evidence("NMSU Circular 561 Identifying & Preserving Wildlife Tracks",
        "https://pubs.nmsu.edu/_circulars/CR561.pdf", "nmsu-tracks-561.pdf", cap=15_000_000)

    print("\n== 5. Claw marks — MDPI application paper sample (comparison already run) ==", flush=True)
    out["mdpi_claw"] = evidence("Diversity 2022 three bears NE India (claw-mark method)",
        "https://mdpi-res.com/d_attachment/diversity/diversity-14-00717/article_deploy/diversity-14-00717.pdf?version=1661778465",
        "mdpi-claw-bears-2022.pdf", cap=20_000_000)

    print("\n== 6. Bite marks — taphonomy paper sample ==", flush=True)
    out["fsi_bite"] = evidence("FSI Animals & Environments 2023 bear-attack taphonomy (tooth pits)",
        "https://scavengers.cat/wp-content/uploads/2023/12/1-s2.0-S2666937423000148-main.pdf",
        "fsi-bear-taphonomy-2023.pdf", cap=20_000_000)

    print("\n== 7. Vibrissae — diceCT methods sample ==", flush=True)
    out["mmu_dicect"] = evidence("Evans & Elder diceCT pinniped mystacial pad methods (MMU e-space)",
        "https://e-space.mmu.ac.uk/638064/8/EVANS_AND_ELDER_DiceCT_Methods_Pinnipeds_FINAL_SUBMISSION.pdf",
        "mmu-dicect-pinniped.pdf", cap=20_000_000)

    print("\n== 8. Tail — lemur risk assessment sample (species rings, not individual ID) ==", flush=True)
    out["lemur_risk"] = evidence("Tasmania DPIPWE ring-tailed lemur risk assessment",
        "https://nre.tas.gov.au/Documents/Ring%20tailed%20lemur%20risk%20assessment.pdf",
        "lemur-risk-assessment.pdf", cap=15_000_000)

    print("\n== 9. Lab-animal marking — JAX Green Book text + USDA manual sample ==", flush=True)
    st, html = get_text("http://www.informatics.jax.org/greenbook/chapters/chapter3.shtml")
    txt = re.sub(r"<[^>]+>", " ", html or "")
    m = re.search(r"[^.]{0,100}ear punch[^.]{0,140}", txt, re.I)
    m2 = re.search(r"[^.]{0,80}12,999|ear-marking system[^.]{0,120}", txt, re.I)
    print(f"  JAX Green Book ch3 {st}; ear-punch: {bool(m)}", flush=True)
    out["jax_greenbook"] = {"status": st, "ear_punch_snippet": (m.group(0)[:280] if m else None),
                            "code_snippet": (m2.group(0)[:240] if m2 else None)}
    out["usda_mice"] = evidence("USDA 1949 Raising Laboratory Mice and Rats (ear/toe Fig.3)",
        "https://ia903202.us.archive.org/7/items/raisinglaborator253eato/raisinglaborator253eato_bw.pdf",
        "usda-mice-rats-1949-head.pdf", cap=2_000_000)
    out["scand_marking"] = evidence("Scand J Lab Anim Sci 1988 identification-methods review",
        "https://ojs.utlib.ee/index.php/SJLAS/article/download/21751/16479/28642",
        "scand-lab-marking-1988.pdf", cap=15_000_000)

    gh.save({"verify14": out}, "verify14")
    print("\nverify14 saved", flush=True)

if __name__ == "__main__":
    main()
