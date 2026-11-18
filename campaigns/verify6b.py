#!/usr/bin/env python3
"""Verify6b — Fonozoo live-vs-deleted resolution + UNAM catalogue
probe + Sanborn CDX. Verify6's HEAD checks all returned 403
(bot/hotlink protection rejects HEAD on these CSIC hosts), which
proves nothing about existence. This pass uses bounded GETs.
Also establishes whether the Fonozoo guide pages in Wayback map
species names to the mp3 files (the labels question for grading).
Run from goldmine-hunter/.
"""
import hashlib, io, json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
from verify6 import evidence, cdx, wb, OUTDIR

UA = {"User-Agent": "goldmine-hunter/2.0 (open-science dataset recovery)"}

def get_probe(url, nbytes=4096):
    """Bounded GET of the first bytes; status + magic, no full file."""
    try:
        r = requests.get(url, headers={**UA, "Range": f"bytes=0-{nbytes-1}"},
                         timeout=60, stream=True, allow_redirects=True)
        buf = io.BytesIO()
        for chunk in r.iter_content(8192):
            buf.write(chunk)
            if buf.tell() >= nbytes:
                break
        raw = buf.getvalue()[:nbytes]
        kind = ("MP3" if raw[:3] == b"ID3" or raw[:2] in (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2")
                else "HTML" if raw.lstrip().lower().startswith((b"<!doctype", b"<html"))
                else "OTHER")
        return {"url": url, "status": r.status_code, "content_type": r.headers.get("Content-Type"),
                "content_length": r.headers.get("Content-Length"), "first_bytes_kind": kind,
                "first16_hex": raw[:16].hex()}
    except Exception as e:
        return {"url": url, "status": None, "error": str(e)[:140]}

def main():
    out = {}

    print("\n== Fonozoo live GET probes (Range, first bytes) ==", flush=True)
    probes = [
        "https://www.fonozoo.com/",
        "https://www.fonozoo.com/sonidos/0720.mp3",
        "http://www.fonozoo.com/sonidos/0800%20alytes%20muletensis.mp3",
        "http://www.fonozoo.com/archivos/03-07-08-14-49-11.mp3",
        "https://www.fonozoo.com/fnz_back/propios/files/14650_web_1736941493.mp3",
        "https://www.fonozoo.com/fnz_publicaciones/files/madagascar/fnz_madagascar_eng.php",
    ]
    out["live_get_probes"] = []
    for u in probes:
        p = get_probe(u)
        out["live_get_probes"].append(p)
        print(f"  GET {p['status']} kind={p.get('first_bytes_kind')} len={p.get('content_length')} {u[:95]}", flush=True)

    print("\n== Fonozoo /sonidos Wayback samples (numbered + species-named + oldest) ==", flush=True)
    rows = cdx("fonozoo.com/sonidos/*", limit=5000)
    ok = [x for x in rows if x[2] == "200" and x[1].lower().endswith(".mp3")]
    print(f"  /sonidos CDX: {len(rows)} collapsed, {len(ok)} status-200 mp3", flush=True)
    named = [x for x in ok if re.search(r"[a-z]{4,}", x[1].lower().rsplit("/", 1)[-1]) and "%20" in x[1]]
    numbered = [x for x in ok if re.fullmatch(r"\d+\.mp3", x[1].rsplit("/", 1)[-1].lower())]
    print(f"  species-named: {len(named)}, purely numbered: {len(numbered)}", flush=True)
    out["sonidos"] = {"collapsed": len(rows), "ok200_mp3": len(ok),
                      "species_named": len(named), "numbered": len(numbered),
                      "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok[:50]]}
    picks = []
    if numbered:
        picks.append(("numbered smallest", sorted(numbered, key=lambda x: int(x[3] or 0))[0]))
        picks.append(("numbered oldest", sorted(numbered)[0]))
    if named:
        picks.append(("species-named smallest", sorted(named, key=lambda x: int(x[3] or 0))[0]))
    out["sonidos_samples"] = []
    for label, (ts, orig, sc, ln, mt) in picks:
        out["sonidos_samples"].append(evidence(f"Fonozoo /sonidos {label} wb ({ln} B CDX)",
                                               wb(ts, orig), "fonozoo-sonidos-" + orig.rsplit("/", 1)[-1].replace("%20", "_")))

    print("\n== Fonozoo guide page in Wayback — species->file mapping ==", flush=True)
    rows = cdx("fonozoo.com/fnz_publicaciones/files/madagascar/fnz_madagascar_eng.php", limit=50,
               fl="timestamp,original,statuscode")
    print(f"  guide page captures: {len(rows)}", flush=True)
    out["guide_captures"] = len(rows)
    if rows:
        ts = sorted(x[0] for x in rows if x[2] == "200")[0]
        f_url = wb(ts, "https://www.fonozoo.com/fnz_publicaciones/files/madagascar/fnz_madagascar_eng.php")
        try:
            r = requests.get(f_url, headers=UA, timeout=90)
            txt = r.text
            mp3s = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+\.mp3)["\']', txt, re.I)))
            species = sorted(set(re.findall(r'<i>([A-Z][a-z]+ [a-z]+)</i>', txt)))
            out["guide_snapshot"] = {"ts": ts, "bytes": len(txt), "mp3_links": mp3s[:20],
                                     "n_mp3_links": len(mp3s), "species_italic_sample": species[:15],
                                     "n_species": len(species)}
            print(f"  snapshot {ts}: {len(txt):,} B, {len(mp3s)} mp3 links, {len(species)} italic species names", flush=True)
            for m in mp3s[:8]:
                print(f"    mp3 link: {m[:110]}", flush=True)
            for s in species[:8]:
                print(f"    species: {s}", flush=True)
        except Exception as e:
            out["guide_snapshot"] = {"error": str(e)[:140]}
            print(f"  guide snapshot fetch failed: {e}", flush=True)

    print("\n== UNAM catalogue pages — image refs ==", flush=True)
    out["unam_catalogo"] = {}
    for page in ("Catalogo_Otolitos.php", "Busqueda_Otolitos.php"):
        try:
            r = requests.get("https://otolitos.unam.mx/" + page, headers=UA, timeout=60)
            txt = r.text
            imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png))', txt, re.I)))
            out["unam_catalogo"][page] = {"status": r.status_code, "bytes": len(txt),
                                          "image_refs": imgs[:12], "n_image_refs": len(imgs)}
            print(f"  {page}: {r.status_code}, {len(txt):,} B, {len(imgs)} image refs", flush=True)
            for i in imgs[:5]:
                print(f"    img: {i[:110]}", flush=True)
        except Exception as e:
            out["unam_catalogo"][page] = {"error": str(e)[:140]}
            print(f"  {page} failed: {e}", flush=True)

    print("\n== Sanborn — targeted CDX on MU hosts ==", flush=True)
    out["sanborn_cdx"] = {}
    for prefix in ("cafnr.missouri.edu/*", "extension.missouri.edu/*"):
        rows = cdx(prefix, limit=6000, extra={"filter": r"original:.*[Ss]anborn.*"})
        ok6 = [x for x in rows if x[2] == "200"]
        print(f"  {prefix} (sanborn filter): {len(rows)} collapsed, {len(ok6)} status-200", flush=True)
        for ts, orig, sc, ln, mt in ok6[:10]:
            print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
        out["sanborn_cdx"][prefix] = {"collapsed": len(rows), "ok200": len(ok6),
                                      "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok6[:30]]}

    gh.save({"verify6b": out}, "verify6b")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
