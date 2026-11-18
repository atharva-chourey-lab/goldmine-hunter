#!/usr/bin/env python3
"""Verify8b — Campaign 8 correction/completion pass.
Fixes verify8's weak spots: (1) scar-sheet PDF page + individual
count via pdfinfo/text; (2) CMU full-size (non-thumbnail) image
sample; (3) Adelaide koala CDX redone with plain regex (verify8's
(?i) inline flags made CDX return 500 — same class of error as
Campaign 7's malformed filters, corrected here); (4) NPDD
microfiche evidence on tag-stripped text; (5) Parker handbook via
Wayback after the live UFDC host returned empty; (6) Utah record
page retry. Samples to gold/campaign8-verify/. Run from
goldmine-hunter/.
"""
import hashlib, io, json, os, re, subprocess, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import cdx, wb, head, UA

OUTDIR = "gold/campaign8-verify"
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

    print("\n== 1. Scar-sheet PDF — pages + individual count ==", flush=True)
    p = os.path.join(OUTDIR, "smc-scar-sheets-all-10-13.pdf")
    info = {}
    try:
        r = subprocess.run(["pdfinfo", p], capture_output=True, text=True, timeout=60)
        info["pdfinfo"] = r.stdout[:500]
        print(f"  pdfinfo: {r.stdout[:300]!r}", flush=True)
    except Exception as e:
        info["pdfinfo_error"] = str(e)[:120]
    try:
        r = subprocess.run(["pdftotext", p, "-"], capture_output=True, text=True, timeout=120)
        txt = r.stdout
        info["text_chars"] = len(txt)
        # scar sheets carry an alphabetical index of named individuals + BS numbers
        bs = sorted(set(re.findall(r"\bBS\s?\d{2,4}\b", txt)))
        info["n_BS_numbers"] = len(bs)
        info["bs_sample"] = bs[:15]
        named = re.findall(r"(?m)^([A-Z][a-zA-Z' ]{2,24})\s+BS\s?\d", txt)
        info["n_named_index_entries"] = len(named)
        print(f"  pdftotext: {len(txt)} chars; BS numbers found: {len(bs)}; named entries: {len(named)}", flush=True)
        m = re.search(r"[^.]{0,120}drop[^.]{0,160}", txt, re.I)
        info["drop_rule_snippet"] = (m.group(0)[:280] if m else None)
    except Exception as e:
        info["pdftotext_error"] = str(e)[:120]
    out["scar_pdf_structure"] = info
    p2 = os.path.join(OUTDIR, "smc-scarsheet-mail.pdf")
    try:
        r = subprocess.run(["pdfinfo", p2], capture_output=True, text=True, timeout=60)
        out["scar_mail_pdfinfo"] = r.stdout[:300]
        print(f"  mail scar pdfinfo: {r.stdout[:200]!r}", flush=True)
    except Exception as e:
        out["scar_mail_pdfinfo"] = f"error {str(e)[:100]}"

    print("\n== 2. CMU — one full-size hair image ==", flush=True)
    st, page = get_text("http://people.se.cmich.edu/swans1bj/hair%20id/Canis/Canis.html")
    imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|gif|png))["\']', page, re.I)))
    full = [i for i in imgs if "humbnail" not in i]
    print(f"  Canis page {st}: {len(imgs)} image refs, {len(full)} non-thumbnail", flush=True)
    out["cmu_full_imgs"] = full[:8]
    out["cmu_full_sample"] = None
    for img in full[:1]:
        iurl = img if img.startswith("http") else "http://people.se.cmich.edu/swans1bj/hair%20id/Canis/" + img
        out["cmu_full_sample"] = evidence("CMU Canis full-size hair image", iurl,
                                           "cmu-canis-full-" + iurl.rsplit("/", 1)[-1], cap=4_000_000)

    print("\n== 3. Adelaide koala CDX — plain regex redo ==", flush=True)
    out["koala_cdx_redo"] = {}
    try:
        rows = cdx_filter("adelaide.edu.au/*", r"koala", limit=3000)
        out["koala_cdx_redo"]["koala_any"] = len(rows)
        print(f"  adelaide.edu.au 'koala': {len(rows)} status-200", flush=True)
        fp = [x for x in rows if re.search(r"finger|dermato|print", x[1], re.I)]
        out["koala_cdx_redo"]["koala_fingerprint"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in fp[:10]]
        print(f"  of which fingerprint/dermato/print: {len(fp)}", flush=True)
    except Exception as e:
        out["koala_cdx_redo"]["error"] = str(e)[:160]
        print(f"  CDX redo failed: {e}", flush=True)

    print("\n== 4. NPDD — microfiche evidence, tag-stripped ==", flush=True)
    st, html = get_text("https://nationalpurebreddogday.com/the-dogs-version-of-the-fingerprint/")
    txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or ""))
    mf = re.search(r"[^.]{0,180}microfiche[^.]{0,180}\.", txt, re.I)
    yrs = re.search(r"[^.]{0,120}1938[^.]{0,200}", txt)
    print(f"  NPDD {st}; microfiche: {bool(mf)}; 1938 span: {bool(yrs)}", flush=True)
    out["ckc_redo"] = {"status": st, "microfiche_snippet": (mf.group(0)[:360] if mf else None),
                       "span_snippet": (yrs.group(0)[:320] if yrs else None)}

    print("\n== 5. Parker handbook — Wayback fallback ==", flush=True)
    out["parker_wb"] = None
    try:
        rows = cdx_filter("ufdcimages.uflib.ufl.edu/IR/00/00/42/09/*", r"Parker", limit=500)
        print(f"  UFDC Parker CDX status-200: {len(rows)}", flush=True)
        out["parker_cdx"] = [{"ts": x[0], "url": x[1], "length": x[3]} for x in rows[:6]]
        for ts, orig, sc, ln, mt in rows[:1]:
            out["parker_wb"] = evidence(f"Parker handbook via Wayback ({ln} B CDX)", wb(ts, orig),
                                        "parker-elephant-handbook-wb.pdf", cap=15_000_000)
    except Exception as e:
        out["parker_cdx_error"] = str(e)[:160]
        print(f"  Parker CDX failed: {e}", flush=True)

    print("\n== 6. Utah RWC — retry record page ==", flush=True)
    st, html = get_text("https://collections.lib.utah.edu/details?id=2148813")
    print(f"  Utah details retry: {st}, {len(html or '')} B", flush=True)
    out["utah_retry"] = {"status": st, "bytes": len(html or "")}
    if html:
        imgs = sorted(set(re.findall(r'(https?://[^"\']+\.(?:jpg|jpeg))', html, re.I)))
        out["utah_retry"]["n_jpg_refs"] = len(imgs)
        out["utah_retry"]["refs"] = imgs[:4]
        wid = re.search(r"(Whale ID|0729|uum_rwc)", html)
        out["utah_retry"]["rwc_meta"] = bool(wid)

    gh.save({"verify8b": out}, "verify8b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
