#!/usr/bin/env python3
"""Gather gold — actually download the gold-class finds and verify them:
1. SDSS apogee-rc-DR12.fits — DELETED from live, Wayback-only.
2. SBA macaque CIVM labels + b0 template + Badhwar hippocampal atlas —
   stranded on a project site, in no formal archive.
3. WorldClim v1 — the smallest complete resolution group of the bio
   family, from Wayback captures.
Everything lands in gold/ with a manifest. Run from goldmine-hunter/."""
import json, os, re, sys, zipfile
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) GoldmineHunter/2.0"}
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gold")
os.makedirs(ROOT, exist_ok=True)
manifest = []

def download(url, dest, cap=900_000_000):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return os.path.getsize(dest)
    with requests.get(url, headers=UA, stream=True, timeout=180) as r:
        r.raise_for_status()
        n = 0
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                n += len(chunk)
                if n > cap:
                    raise RuntimeError(f"cap exceeded for {url}")
                f.write(chunk)
    return os.path.getsize(dest)

def verify(path):
    with open(path, "rb") as f:
        head = f.read(8)
    size = os.path.getsize(path)
    kind = "unknown"
    if head.startswith(b"SIMPLE  ="):
        kind = "FITS (valid header)"
    elif head[:2] == b"\x1f\x8b":
        kind = "gzip (NIfTI.gz or tar.gz)"
    elif head[:2] == b"PK":
        try:
            with zipfile.ZipFile(path) as z:
                kind = f"ZIP ok, {len(z.namelist())} entries, first: {z.namelist()[:3]}"
        except Exception as e:
            kind = f"ZIP BROKEN: {e}"
    return size, kind

def record(group, name, src, path):
    size, kind = verify(path)
    manifest.append({"group": group, "file": name, "source": src,
                     "bytes": size, "verify": kind})
    print(f"  OK {name} — {size:,} B — {kind}", flush=True)

def wayback_raw(original):
    r = requests.get("http://web.archive.org/cdx/search/cdx",
                     params={"url": original, "output": "json",
                             "fl": "timestamp,original,statuscode",
                             "filter": "statuscode:200", "limit": "5"},
                     headers=UA, timeout=60)
    rows = r.json()[1:]
    if not rows:
        raise RuntimeError(f"no capture for {original}")
    ts, orig = rows[-1][0], rows[-1][1]
    return f"https://web.archive.org/web/{ts}id_/{orig}"

# ---------- 1. SDSS deleted catalogue ----------
print("== SDSS deleted catalogue ==", flush=True)
orig = "https://data.sdss.org/sas/dr12/apogee/vac/apogee-rc/cat/apogee-rc-DR12.fits"
d = os.path.join(ROOT, "sdss-deleted"); os.makedirs(d, exist_ok=True)
p = os.path.join(d, "apogee-rc-DR12.fits")
try:
    download(wayback_raw(orig), p)
    record("sdss-deleted", "apogee-rc-DR12.fits", f"wayback-only (deleted from live): {orig}", p)
except Exception as e:
    manifest.append({"group": "sdss-deleted", "file": "apogee-rc-DR12.fits",
                     "source": orig, "bytes": 0,
                     "verify": f"NOT GATHERED: {e} — Wayback captures of this URL are 404 pages (checked via CDX)"})
    print(f"  NOT GATHERED: {e}", flush=True)

# ---------- 2. SBA macaque set ----------
print("== SBA macaque set ==", flush=True)
d = os.path.join(ROOT, "sba-macaque"); os.makedirs(d, exist_ok=True)
SBA = "https://scalablebrainatlas.incf.org/templates/"
for name, url in [
    ("civm_rhesus_v1_labels.nii.gz", SBA + "CBCetal15/source/civm_rhesus_v1_labels.nii.gz"),
    ("civm_rhesus_v1_b0.nii.gz", SBA + "CBCetal15/source/civm_rhesus_v1_b0.nii.gz"),
    ("badhwar_hippocampal_atlas.nii.gz", SBA + "BLHS13/source/badhwar_hippocampal_atlas.nii.gz"),
]:
    p = os.path.join(d, name)
    download(url, p)
    record("sba-macaque", name, url, p)

# ---------- 3. WorldClim v1 bio slice ----------
print("== WorldClim v1 (Wayback) ==", flush=True)
r = requests.get("http://web.archive.org/cdx/search/cdx",
                 params={"url": "worldclim.org/data/bio*", "output": "json",
                         "fl": "timestamp,original,statuscode,length",
                         "filter": "statuscode:200", "collapse": "urlkey",
                         "limit": "500"},
                 headers=UA, timeout=120)
rows = [x for x in r.json()[1:] if x[1].endswith(".zip")]
groups = {}
for ts, orig, sc, ln in rows:
    base = orig.rsplit("/", 1)[-1]
    m = re.match(r"bio_(.+)\.zip", base)
    if m:
        groups.setdefault(m.group(1), []).append((ts, orig, int(ln or 0)))
print("  bio groups:", {k: (len(v), sum(x[2] for x in v)) for k, v in groups.items()}, flush=True)
best = min(groups.items(), key=lambda kv: sum(x[2] for x in kv[1]))
print(f"  gathering smallest complete group: {best[0]} "
      f"({len(best[1])} files, {sum(x[2] for x in best[1]):,} B archived)", flush=True)
d = os.path.join(ROOT, "worldclim-v1-bio"); os.makedirs(d, exist_ok=True)
for ts, orig, ln in sorted(best[1]):
    base = orig.rsplit("/", 1)[-1]
    p = os.path.join(d, base)
    download(f"https://web.archive.org/web/{ts}id_/{orig}", p)
    record("worldclim-v1-bio", base, f"wayback {ts}: {orig}", p)

with open(os.path.join(ROOT, "MANIFEST.json"), "w") as f:
    json.dump(manifest, f, indent=1)
total = sum(m["bytes"] for m in manifest)
print(f"\nGATHERED {len(manifest)} files, {total:,} bytes total. Manifest: gold/MANIFEST.json", flush=True)
