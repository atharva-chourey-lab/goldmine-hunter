#!/usr/bin/env python3
"""Verify6 — Campaign 6 (Wave 1) verification pass.
Standing method: every promising pile gets sample downloads
(size + md5 + magic) and live-status HEADs; grades in GRADES.md
may only rest on this output. Samples to gold/campaign6-verify/,
total kept small. Run from goldmine-hunter/.
"""
import collections, hashlib, io, json, os, re, sys, zipfile
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh

UA = {"User-Agent": "goldmine-hunter/2.0 (open-science dataset recovery)"}
OUTDIR = "gold/campaign6-verify"
CAP = 25_000_000

def head(url):
    try:
        r = requests.head(url, headers=UA, timeout=30, allow_redirects=True)
        return {"status": r.status_code, "size": r.headers.get("Content-Length"),
                "type": r.headers.get("Content-Type")}
    except Exception as e:
        return {"status": None, "error": str(e)[:120]}

def fetch_bounded(url, cap=CAP):
    try:
        r = requests.get(url, headers=UA, timeout=120, stream=True, allow_redirects=True)
        status = r.status_code
        buf = io.BytesIO()
        for chunk in r.iter_content(65536):
            buf.write(chunk)
            if buf.tell() > cap:
                break
        raw = buf.getvalue()
        truncated = len(raw) > cap or (r.headers.get("Content-Length") and
                                        int(r.headers["Content-Length"]) > len(raw))
        return {"status": status, "raw": raw, "truncated": bool(truncated),
                "content_type": r.headers.get("Content-Type")}
    except Exception as e:
        return {"status": None, "raw": b"", "error": str(e)[:160]}

def evidence(label, url, save_name=None, cap=CAP):
    f = fetch_bounded(url, cap)
    raw = f["raw"]
    ev = {"label": label, "url": url, "http_status": f["status"],
          "bytes_downloaded": len(raw), "truncated_at_cap": f.get("truncated", False),
          "content_type": f.get("content_type"), "error": f.get("error")}
    if not raw:
        ev["verdict"] = "UNREACHABLE / EMPTY"
        print(f"  [{label}] {ev['verdict']} {url[:100]}", flush=True)
        return ev
    ev["md5_full"] = hashlib.md5(raw).hexdigest() if not ev["truncated_at_cap"] else None
    ev["md5_head1mb"] = hashlib.md5(raw[:1_000_000]).hexdigest()
    hb = raw[:512]
    low = url.lower().split("?")[0]
    is_html = hb.lstrip().lower().startswith((b"<!doctype", b"<html", b"<!--"))
    ev["looks_html"] = bool(is_html)
    if is_html:
        ev["verdict"] = "PHANTOM — HTML page, not data"
    elif raw[:3] == b"ID3" or raw[:2] in (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2"):
        ev["verdict"] = "REAL — MP3 audio (ID3/frame-sync magic)"
        ev["mp3"] = True
    elif raw[:4] == b"RIFF" and raw[8:12] == b"WAVE":
        ev["verdict"] = "REAL — WAV audio (RIFF/WAVE)"
        ev["wav"] = True
    elif raw[:4] == b"%PDF":
        ev["verdict"] = "REAL — PDF"
        ev["pdf"] = True
    elif raw[:3] == b"\xff\xd8\xff":
        ev["verdict"] = "REAL — JPEG image"
        ev["jpeg"] = True
    elif raw[:8] == b"\x89PNG\r\n\x1a\n":
        ev["verdict"] = "REAL — PNG image"
        ev["png"] = True
    elif low.endswith(".zip") or raw[:2] == b"PK":
        try:
            z = zipfile.ZipFile(io.BytesIO(raw))
            ev["zip_entries"] = z.namelist()[:12]
            ev["zip_n_entries"] = len(z.namelist())
            ev["verdict"] = "REAL — valid zip (xlsx/zip family)"
        except Exception as e:
            ev["verdict"] = f"PK MAGIC but zip unreadable (truncated?): {e}"
            ev["pk_magic"] = True
    elif raw[:4] == b"\xd0\xcf\x11\xe0":
        ev["verdict"] = "REAL — OLE2 (legacy .xls)"
        ev["ole2"] = True
    elif raw[:2] == b"\x1f\x8b":
        ev["verdict"] = "REAL — gzip stream"
        ev["gzip"] = True
    else:
        try:
            txt = raw.decode("utf-8", errors="strict")
            ev["lines_sampled"] = txt.count("\n")
            ev["first_line"] = txt.split("\n")[0][:160]
            ev["verdict"] = "REAL — decodable text data"
        except UnicodeDecodeError:
            ev["first_bytes_hex"] = hb[:16].hex()
            ev["all_blank"] = all(b in (0, 9, 10, 13, 32) for b in raw[:100000])
            ev["verdict"] = "EMPTY PLACEHOLDER — blank" if ev["all_blank"] else "BINARY — non-HTML, non-blank"
    if save_name and ev["verdict"].startswith("REAL") and not ev["truncated_at_cap"]:
        os.makedirs(OUTDIR, exist_ok=True)
        with open(os.path.join(OUTDIR, save_name), "wb") as fh:
            fh.write(raw)
        ev["saved_to"] = os.path.join(OUTDIR, save_name)
    print(f"  [{label}] {ev['verdict']} | {len(raw):,} B | md5={ev.get('md5_full') or ev['md5_head1mb']} | {url[:100]}", flush=True)
    return ev

def cdx(prefix, limit=8000, fl="timestamp,original,statuscode,length,mimetype", extra=None):
    params = {"url": prefix, "output": "json", "fl": fl, "collapse": "urlkey", "limit": limit}
    if extra:
        params.update(extra)
    try:
        r = requests.get("http://web.archive.org/cdx/search/cdx", params=params,
                         headers=UA, timeout=120)
        r.raise_for_status()
        rows = r.json()
        return rows[1:] if len(rows) > 1 else []
    except Exception as e:
        print(f"  CDX failed {prefix}: {e}", flush=True)
        return []

def wb(ts, orig):
    return f"https://web.archive.org/web/{ts}id_/{orig}"

def main():
    out = {}

    print("\n== 1. Fonozoo (fonozoo.com) — full targeted CDX, live status, samples ==", flush=True)
    rows = cdx("fonozoo.com/*", limit=10000)
    ok = [x for x in rows if x[2] == "200" and gh.is_data(x[1]) and " " not in x[1]]
    sets = collections.Counter("/" + "/".join(x[1].split("/")[3:-1]) for x in ok)
    print(f"  fonozoo.com targeted CDX: {len(rows)} collapsed, {len(ok)} status-200 data files", flush=True)
    for k, v in sets.most_common(10):
        print(f"    set {v:4d}  {k}", flush=True)
    out["fonozoo_cdx"] = {"collapsed": len(rows), "ok200_data": len(ok),
                          "sets": dict(sets.most_common(12)),
                          "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok]}
    # live status of a spread of originals
    def by_set(s):
        return [x for x in ok if s in x[1]]
    picks = []
    for s in ("/fnz_back/propios/files", "/fnz_back/publicados/files", "/archivos", "/audios"):
        g = by_set(s)
        if g:
            picks.append(sorted(g)[0]); picks.append(sorted(g)[-1])
    out["fonozoo_live_status"] = {x[1]: head(x[1]) for x in picks[:8]}
    for k, v in out["fonozoo_live_status"].items():
        print(f"  live-status {k[:95]}: {v}", flush=True)
    # samples: spread across sets and years, smallest in each set first
    samples = []
    for s in ("/archivos", "/fnz_back/propios/files", "/fnz_back/publicados/files"):
        g = [x for x in by_set(s) if x[1].lower().endswith(".mp3")]
        if g:
            samples.append(sorted(g, key=lambda x: int(x[3] or 0))[0])
            samples.append(sorted(g)[-1])
    out["fonozoo_samples_wb"] = []
    for ts, orig, sc, ln, mt in samples[:6]:
        out["fonozoo_samples_wb"].append(evidence(
            f"Fonozoo wb sample ({ln} B CDX)", wb(ts, orig),
            "fonozoo-" + orig.rsplit("/", 1)[-1]))
    wavs = [x for x in by_set("/audios") if x[1].lower().endswith(".wav")]
    if wavs:
        ts, orig, sc, ln, mt = sorted(wavs, key=lambda x: int(x[3] or 0))[0]
        out["fonozoo_wav_sample_wb"] = evidence(f"Fonozoo /audios wav wb ({ln} B CDX, cap 3MB)",
                                                wb(ts, orig), cap=3_000_000)
    # does a live guide page still link species -> mp3? (labels question)
    out["fonozoo_guide_live"] = evidence("Fonozoo Madagascar guide page live",
                                         "https://www.fonozoo.com/fnz_publicaciones/files/madagascar/fnz_madagascar_eng.php",
                                         cap=500_000)

    print("\n== 2. Fonozoo catalogue host (fonozoo.mncn.csic.es) — /sonidos CDX + live detail ==", flush=True)
    out["mncn"] = {}
    for prefix in ("fonozoo.mncn.csic.es/sonidos/*", "fonozoo.mncn.csic.es/*"):
        rows = cdx(prefix, limit=5000)
        ok2 = [x for x in rows if x[2] == "200" and gh.is_data(x[1])]
        print(f"  {prefix}: collapsed {len(rows)}, status-200 data {len(ok2)}", flush=True)
        for ts, orig, sc, ln, mt in ok2[:10]:
            print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
        out["mncn"][prefix] = {"collapsed": len(rows), "ok200_data": len(ok2),
                               "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok2[:40]]}
        if ok2:
            ts, orig, sc, ln, mt = sorted(ok2, key=lambda x: int(x[3] or 0))[0]
            out["mncn"][prefix + "_sample"] = evidence(f"MNCN smallest wb ({ln} B CDX)", wb(ts, orig))
            out["mncn"][prefix + "_live"] = head(orig)
            print(f"  live-status {orig[:95]}: {out['mncn'][prefix + '_live']}", flush=True)
    out["mncn_sonidos_example_live"] = evidence(
        "MNCN /sonidos/ '12 Leptodactylus Elenae.mp3' live",
        "http://www.fonozoo.mncn.csic.es/sonidos/12%20Leptodactylus%20Elenae.mp3", cap=3_000_000)

    print("\n== 3. AFORO — adapter probe (JSP app hosts) ==", flush=True)
    out["aforo"] = {}
    for u in ("http://isis.cmima.csic.es/startDB_en.jsp",
              "http://aforo.cmima.csic.es/upload_img_en.jsp"):
        f = fetch_bounded(u, cap=300_000)
        txt = f["raw"].decode("utf-8", errors="ignore")
        imgs = sorted(set(re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png))', txt, re.I)))
        out["aforo"][u] = {"status": f["status"], "bytes": len(f["raw"]),
                           "image_refs": imgs[:15], "n_image_refs": len(imgs)}
        print(f"  {u}: status {f['status']}, {len(f['raw']):,} B, {len(imgs)} image refs", flush=True)
        for i in imgs[:6]:
            print(f"    img: {i[:110]}", flush=True)
    out["aforo_dist_zip"] = evidence("AFORO dist.zip live (crawl find)",
                                      "http://www.cmima.csic.es/aforo-result/DOCS/dist.zip", cap=5_000_000)

    print("\n== 4. Otolitos UNAM — page links + targeted CDX ==", flush=True)
    f = fetch_bounded("https://otolitos.unam.mx/", cap=300_000)
    txt = f["raw"].decode("utf-8", errors="ignore")
    links = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)', txt, re.I)))
    out["unam_home"] = {"status": f["status"], "links_sample": [l for l in links if not l.startswith("#")][:40]}
    print(f"  home: status {f['status']}, {len(links)} hrefs", flush=True)
    for l in out["unam_home"]["links_sample"][:20]:
        print(f"    link: {l[:110]}", flush=True)
    rows = cdx("otolitos.unam.mx/*", limit=5000)
    ok3 = [x for x in rows if x[2] == "200"]
    print(f"  UNAM CDX: {len(rows)} collapsed, {len(ok3)} status-200 (all types)", flush=True)
    out["unam_cdx"] = {"collapsed": len(rows), "ok200": len(ok3),
                       "files": [{"ts": x[0], "url": x[1], "length": x[3], "mime": x[4]} for x in ok3[:40]]}

    print("\n== 5. QMUL Barts registers — page PDF hunt + targeted CDX ==", flush=True)
    page = "https://www.qmul.ac.uk/fmd/about/our-history/records-of-bodies-dissected-at-the-st-bartholomews-hospital-medical-college/"
    f = fetch_bounded(page, cap=500_000)
    txt = f["raw"].decode("utf-8", errors="ignore")
    pdfs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+\.pdf[^"\']*)', txt, re.I)))
    allhrefs = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+)', txt, re.I)))
    out["qmul_page"] = {"status": f["status"], "pdf_links": pdfs,
                        "registerish_links": [h for h in allhrefs if re.search(r'register|dissect|digital|archive', h, re.I)][:25]}
    print(f"  page status {f['status']}, {len(pdfs)} PDF links, register-ish links:", flush=True)
    for h in out["qmul_page"]["registerish_links"][:12]:
        print(f"    {h[:120]}", flush=True)
    rows = cdx("qmul.ac.uk/fmd/about/our-history/*", limit=5000)
    ok4 = [x for x in rows if x[2] == "200" and gh.is_data(x[1])]
    print(f"  QMUL history-tree CDX: {len(rows)} collapsed, {len(ok4)} status-200 data files", flush=True)
    out["qmul_cdx"] = {"collapsed": len(rows), "ok200_data": len(ok4),
                       "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok4[:40]]}
    cand = pdfs or [x[1] for x in ok4 if x[1].lower().endswith(".pdf")]
    if cand:
        u = cand[0] if cand[0].startswith("http") else "https://www.qmul.ac.uk" + cand[0]
        out["qmul_sample_pdf"] = evidence("QMUL Barts register PDF live", u,
                                          "qmul-barts-" + u.rsplit("/", 1)[-1].split("?")[0], cap=30_000_000)

    print("\n== 6. Mormyrids — targeted CDX audio filter ==", flush=True)
    rows = cdx("mormyrids.efishgenomics.com/*", limit=8000,
               extra={"filter": r"original:.*\.(wav|mp3|zip|wma|aif|aiff)"})
    ok5 = [x for x in rows if x[2] == "200"]
    print(f"  audio-filter CDX: {len(rows)} collapsed, {len(ok5)} status-200", flush=True)
    for ts, orig, sc, ln, mt in ok5[:15]:
        print(f"    {ln} B  {orig[:110]}  ({ts})", flush=True)
    out["mormyrid_cdx_audio"] = {"collapsed": len(rows), "ok200": len(ok5),
                                 "files": [{"ts": x[0], "url": x[1], "length": x[3]} for x in ok5[:30]]}
    out["mormyrid_robots"] = evidence("Mormyrids robots.txt", "https://mormyrids.efishgenomics.com/robots.txt", cap=50_000)

    print("\n== 7. NOAA NEFSC scales — GCS bucket listing + sample ==", flush=True)
    out["noaa"] = {}
    try:
        r = requests.get("https://storage.googleapis.com/storage/v1/b/nmfs_odp_nefsc/o",
                         params={"prefix": "PARR/READ/PSB/NEST/27493",
                                 "fields": "items(name,size,md5Hash)"},
                         headers=UA, timeout=60)
        out["noaa"]["gcs_list_status"] = r.status_code
        items = r.json().get("items", []) if r.status_code == 200 else []
        out["noaa"]["gcs_items"] = [{"name": i["name"], "size": i.get("size")} for i in items]
        print(f"  GCS list status {r.status_code}, {len(items)} objects", flush=True)
        for i in items:
            print(f"    {i.get('size')} B  {i['name'][:110]}", flush=True)
        xlsx = [i for i in items if i["name"].lower().endswith(".xlsx")]
        if xlsx:
            pick = sorted(xlsx, key=lambda i: int(i.get("size") or 0))[0]
            url = "https://storage.googleapis.com/nmfs_odp_nefsc/" + requests.utils.quote(pick["name"], safe="/")
            out["noaa"]["sample_xlsx"] = evidence(f"NOAA scales xlsx ({pick['name'].rsplit('/',1)[-1]})",
                                                  url, "noaa-" + pick["name"].rsplit("/", 1)[-1].replace(" ", "_"))
    except Exception as e:
        out["noaa"]["gcs_error"] = str(e)[:160]
        print(f"  GCS list failed: {e}", flush=True)
    out["noaa"]["inport_head"] = head("https://www.fisheries.noaa.gov/inport/item/27493")
    print(f"  InPort 27493 live-status: {out['noaa']['inport_head']}", flush=True)

    print("\n== 8. Burrishoole IFBA — GeoNetwork record ==", flush=True)
    f = fetch_bounded("https://data.marine.ie/geonetwork/srv/api/records/ie.marine.data:dataset.4067", cap=500_000)
    txt = f["raw"].decode("utf-8", errors="ignore")
    urls = sorted(set(re.findall(r'https?://[^\s"\'<>]+', txt)))
    out["ifba_record"] = {"status": f["status"], "bytes": len(f["raw"]),
                          "urls_found": [u for u in urls if re.search(r'download|\.zip|\.csv|dist', u, re.I)][:15],
                          "n_urls": len(urls)}
    print(f"  record status {f['status']}, {len(f['raw']):,} B, {len(urls)} urls, download-ish: {out['ifba_record']['urls_found'][:5]}", flush=True)

    print("\n== 9. Growth strays — Harpenden (UKDS) evidence; Nittedal note ==", flush=True)
    out["harpenden_dict_pdf"] = evidence("Harpenden Growth Study data dictionary (UK Data Service doc)",
                                         "https://doc.ukdataservice.ac.uk/doc/9330/mrdoc/pdf/9330_data_dictionary_2.pdf",
                                         "harpenden-9330-data-dictionary.pdf", cap=10_000_000)

    print("\n== 10. Sanborn Field — MU Extension summary PDF ==", flush=True)
    out["sanborn_pdf"] = evidence("Sanborn Field sulfur-history summary (MU Extension mp0939)",
                                  "https://extension.missouri.edu/sites/default/files/legacy_media/wysiwyg/Extensiondata/Pub/pdf/miscpubs/mp0939.pdf",
                                  "sanborn-mp0939.pdf", cap=10_000_000)

    print("\n== 11. Waterlevel.ie — live CSV + Wayback CSV samples ==", flush=True)
    out["waterlevel_live_csv"] = evidence("Waterlevel 25017_0001.csv live",
                                           "https://waterlevel.ie/data/month/25017_0001.csv",
                                           "waterlevel-25017_0001.csv", cap=2_000_000)
    out["waterlevel_wb_csv"] = evidence("Waterlevel station data.csv wb2019",
                                         wb("20191117235502", "http://waterlevel.ie/0000007037/0002/download/data.csv?1571470724"),
                                         cap=2_000_000)
    out["waterlevel_live_station_status"] = head("http://waterlevel.ie/0000007037/0002/download/data.csv")
    print(f"  live station-download status: {out['waterlevel_live_station_status']}", flush=True)

    gh.save({"verify6": out}, "verify6")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
