#!/usr/bin/env python3
"""Verify16d — Campaign 16 playbill sample hunt (last gap).
verify16/16b got no playbill file: the BL repository product
page is a JS app (no static download href) and the archive.org
playbill item is access-restricted (patron-library collection).
Try: (1) the BL repository's Samvera concern page for /downloads/
links; (2) Sceneweb (National Library of Norway) playbill PDF;
(3) blplaybills.org sitemap/API for a direct image.
Samples to gold/campaign16-verify/. Run from goldmine-hunter/.
"""
import json, os, re, sys
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import goldmine_hunter as gh
import verify6
from verify6 import UA, evidence

OUTDIR = "gold/campaign16-verify"
os.makedirs(OUTDIR, exist_ok=True)
verify6.OUTDIR = OUTDIR

def get_text(url, cap=900_000):
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        return r.status_code, r.text[:cap]
    except Exception as e:
        return None, f"ERROR {e}"[:160]

def main():
    out = {}

    print("\n== 3c-i. BL repository concern page — download links ==", flush=True)
    for u in ("https://bl.iro.bl.uk/concern/datasets/807f0563-025e-46be-a251-1ad1ba477981",
              "https://doi.org/10.21250/pb2"):
        st, html = get_text(u, cap=900_000)
        dls = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']*(?:downloads|files)[^"\']*)["\']', html, re.I)))
        print(f"  {u[:60]} -> {st}: {len(dls)} download-ish links {dls[:4]}", flush=True)
        out.setdefault("bl_pages", []).append({"url": u, "status": st, "links": dls[:8]})
        for h in dls[:2]:
            url = h if h.startswith("http") else "https://bl.iro.bl.uk" + h
            if re.search(r'\.(zip|txt|xlsx?)(\?|$)', url, re.I):
                out.setdefault("bl_samples", []).append(
                    evidence("BL playbills dataset file", url, "bl-" + url.rsplit("/", 1)[-1].split("?")[0], cap=6_000_000))
                break

    print("\n== 3c-ii. Sceneweb — Norwegian Theatre playbill 1939 (National Library of Norway) ==", flush=True)
    st, html = get_text("https://sceneweb.no/en/multimedia/78865", cap=900_000)
    dls = sorted(set(re.findall(r'href\s*=\s*["\']([^"\']+\.(?:pdf|jpg|jpeg)(?:\?[^"\']*)?)["\']', html, re.I)))
    print(f"  sceneweb item {st}: file links {dls[:6]}", flush=True)
    out["sceneweb"] = {"status": st, "file_links": dls[:8]}
    if dls:
        url = dls[0] if dls[0].startswith("http") else "https://sceneweb.no" + dls[0]
        out["sceneweb_sample"] = evidence("Sceneweb playbill file (Golden Boy, 1939)", url,
                                          "sceneweb-" + url.rsplit("/", 1)[-1].split("?")[0], cap=10_000_000)

    print("\n== 3c-iii. blplaybills.org — sitemap / direct image ==", flush=True)
    st, txt = get_text("https://www.blplaybills.org/sitemap.xml", cap=900_000)
    urls = re.findall(r"<loc>([^<]+)</loc>", txt)
    print(f"  blplaybills sitemap {st}: {len(urls)} urls, sample {urls[:5]}", flush=True)
    out["blplaybills_sitemap"] = {"status": st, "n_urls": len(urls), "sample": urls[:10]}

    gh.save({"verify16d": out}, "verify16d")
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()
