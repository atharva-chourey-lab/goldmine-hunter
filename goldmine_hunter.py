#!/usr/bin/env python3
"""
Goldmine Hunter — find datasets stranded on project websites that never
made it into the formal archive.

The pattern (from the Brain Catalogue find, 2026-11-16):
  - Formal archive (Zenodo/OSF/Dryad) holds only the raw deposit
    e.g. Zenodo 44855 = lion MRI.nii.gz, nothing else.
  - The project's own website hosts the *derived* gold alongside it:
    Hippocampus.nii.gz, Telencephalon.nii.gz, Atlas.nii.gz — hand-drawn
    segmentations, never archived, unindexed, one redesign away from gone.
  - Old versions of the site / articles (Wayback Machine) sometimes hold
    files and high-res images that the live site no longer links.

What this tool does:
  1. audit   — diff an archive record's file list against a project
               website's downloadable files. Website-only = gold candidate.
  2. crawl   — inventory every data file / image / article link on a site.
  3. wayback — list data files the Wayback Machine captured for a domain,
               including ones no longer live.
  4. sweep   — run audit+crawl+wayback over a seeds file of candidate
               projects and rank the finds.

Scoring: a file scores higher if its name looks like derived data
(segmentation, atlas, labels, parcellation, ROI, mask, table...), if it
is absent from the archive, and if it only exists in Wayback captures.

Stdlib + requests only. No keys, no logins, nothing bypassed.
Usage:
  python3 goldmine_hunter.py audit --zenodo 44855 --site https://braincatalogue.org/Lion
  python3 goldmine_hunter.py crawl --site https://braincatalogue.org --depth 2
  python3 goldmine_hunter.py wayback --domain braincatalogue.org
  python3 goldmine_hunter.py sweep --seeds seeds.json
"""
import argparse, gzip, hashlib, json, re, struct, sys, time
from collections import deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse, unquote

import requests

UA = {"User-Agent": "goldmine-hunter/1.0 (open-science dataset recovery; contact via repo)"}
TIMEOUT = 30

DATA_EXTS = (
    ".nii.gz", ".nii", ".dcm", ".img", ".hdr", ".gii", ".mgz", ".mgh",
    ".csv", ".tsv", ".xlsx", ".xls", ".json", ".xml", ".mat", ".h5", ".hdf5",
    ".zip", ".tar.gz", ".tgz", ".tar", ".7z",
    ".stl", ".obj", ".ply", ".vtk", ".label", ".annot", ".txt", ".dat",
    # v2 — cross-domain: the methodology is not neuro-specific
    ".fits", ".fit", ".fts",                       # astronomy
    ".fasta", ".fa", ".fastq", ".fq", ".bam", ".sam", ".vcf", ".gff", ".gtf",  # genomics
    ".shp", ".geojson", ".kml", ".gpkg",           # geospatial (tif in IMAGE_EXTS)
    ".wav", ".mp3", ".flac", ".ogg",               # audio corpora / field recordings
    ".mp4", ".mov", ".webm",                       # video
    ".npy", ".npz", ".parquet", ".feather", ".pkl", ".sqlite", ".db",  # data science
    ".rds", ".sav", ".dta",                        # stats packages
    ".eaf", ".cha", ".stm", ".trs",                # linguistics corpora / transcripts
    ".las", ".laz", ".e57",                        # lidar / 3D scanning (heritage, geo)
    ".nc", ".grib", ".mrc", ".map", ".ccp4", ".cif", ".h5ad", ".loom", ".mtx",  # climate / cryo-EM / single-cell (fidelity packs)
)
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp", ".svg")
# names that signal *derived* data — the gold, as opposed to raw deposits
GOLD_WORDS = (
    "segment", "atlas", "label", "parcellat", "hippocamp", "amygdal",
    "telenceph", "cerebell", "cortex", "cortical", "mask", "roi",
    "annotat", "template", "volum", "measure", "table", "supplement",
)
# v2 — domain packs: same hunt, different vocabularies. The pattern is
# universal (archive holds the deposit, the project site holds the
# derived/older/extra files); only the gold words and signature file
# types change by field.
DOMAIN_PACKS = {
    "neuro":      {"words": GOLD_WORDS, "exts": (".nii.gz", ".nii", ".gii", ".label", ".annot")},
    "genomics":   {"words": ("genome", "assembly", "annotation", "transcript", "variant",
                             "alignment", "phylogen", "sequence", "reads", "contig"),
                   "exts": (".fasta", ".fa", ".fastq", ".fq", ".bam", ".vcf", ".gff", ".gtf")},
    "ecology":    {"words": ("occurrence", "survey", "transect", "specimen", "trait",
                             "abundance", "checklist", "inventory", "observation"),
                   "exts": (".csv", ".tsv", ".xlsx", ".geojson", ".shp")},
    "astro":      {"words": ("catalog", "catalogue", "lightcurve", "spectrum", "spectra",
                             "photometr", "redshift", "observation", "calibrat"),
                   "exts": (".fits", ".fit", ".fts", ".csv", ".vot")},
    "geo":        {"words": ("dem", "elevation", "raster", "vector", "boundary",
                             "watershed", "landcover", "survey", "lidar"),
                   "exts": (".shp", ".geojson", ".tif", ".las", ".laz", ".gpkg")},
    "linguistics": {"words": ("corpus", "transcript", "lexicon", "dictionary", "gloss",
                              "interlinear", "recording", "elicitation", "wordlist"),
                    "exts": (".eaf", ".cha", ".stm", ".trs", ".wav", ".mp3", ".xml")},
    "heritage":   {"words": ("scan", "photogrammetr", "excavat", "artifact", "artefact",
                             "context", "finds", "survey", "reconstruction"),
                   "exts": (".ply", ".obj", ".stl", ".las", ".e57", ".tif")},
    "media":      {"words": ("original", "master", "uncompressed", "raw", "archive",
                             "restored", "transcript", "caption", "subtitle"),
                   "exts": (".wav", ".flac", ".mp4", ".mov", ".srt", ".vtt")},
}
ALL_GOLD_WORDS = tuple({w for p in DOMAIN_PACKS.values() for w in p["words"]} | set(GOLD_WORDS))

# --- High-fidelity scan doctrine (2026-11-17, Atharva's direction) ---
# A system is fertile only if: (1) raw high-fidelity capture is kept,
# (2) one instrument/protocol across many comparable units, (3) labels
# are incomplete/stranded/on a second ruler, (4) a local anchor exists.
# FIDELITY_PACKS encodes that per system so `fidelity` mode and scoring
# can test a candidate before any file counting.
FIDELITY_PACKS = {
    "morpho_ct": {
        "label": "Skeletal micro-CT (MorphoSource/DigiMorph)",
        "raw_exts": (".ply", ".stl", ".obj", ".nii", ".nii.gz", ".tif", ".tiff"),
        "raw_words": ("mesh", "surface", "ct", "microct", "scan", "specimen"),
        "label_words": ("landmark", "centroid", "measurement", "morphometr"),
        "unit": "specimen / species — same bone set across taxa",
        "anchor": "published landmarks / dissection measurements (e.g. Mallet 2019)",
        "second_ruler": "2D photos / few-landmark papers vs full 3D meshes",
    },
    "cosmology": {
        "label": "Cosmology hydro sims (TNG/EAGLE/SIMBA)",
        "raw_exts": (".hdf5", ".h5", ".fits"),
        "raw_words": ("subhalo", "snapshot", "catalog", "catalogue", "groupcat"),
        "label_words": ("metallicity", "abundance", "mzr", "element", "yield"),
        "unit": "galaxy — same mass bins across simulation suites",
        "anchor": "APOGEE / GALAH / MaNGA observed abundances + solar zero-point",
        "second_ruler": "each suite's yield/feedback tables and solar scale",
    },
    "gaia": {
        "label": "Gaia astrometry + XP spectra",
        "raw_exts": (".fits", ".csv", ".parquet", ".vot"),
        "raw_words": ("source", "xp", "spectrum", "astrometr", "parallax"),
        "label_words": ("metallicity", "photometric", "gspphot", "gspspec"),
        "unit": "star — 1.8B sources, one satellite instrument",
        "anchor": "APOGEE / GALAH high-resolution spectroscopy",
        "second_ruler": "photometric (XP/GSP-Phot) vs spectroscopic metallicity",
    },
    "connectome": {
        "label": "Diffusion / connectome MRI (DBB/HCP/MICrONS)",
        "raw_exts": (".nii", ".nii.gz", ".gii", ".hdf5", ".npy"),
        "raw_words": ("dwi", "diffusion", "tract", "connectome", "em", "volume"),
        "label_words": ("atlas", "parcellat", "label", "segment", "roi"),
        "unit": "brain — same diffusion protocol across primates / subjects",
        "anchor": "histology / tracer atlases; Brain Catalogue volumetry",
        "second_ruler": "atlas pipeline A vs pipeline B labels on same scan",
    },
    "cryoem": {
        "label": "Cryo-EM density maps (EMDB)",
        "raw_exts": (".map", ".mrc", ".ccp4", ".pdb", ".cif"),
        "raw_words": ("map", "density", "emdb", "emd-", "reconstruction"),
        "label_words": ("model", "fitted", "alphafold", "prediction"),
        "unit": "protein / complex — same imaging modality across families",
        "anchor": "deposited atomic models; AlphaFold DB as second ruler",
        "second_ruler": "experimental map vs predicted model (and vice versa)",
    },
    "lidar_earth": {
        "label": "Earth lidar + satellite stack (3DEP/GEDI/CORONA/Sentinel)",
        "raw_exts": (".las", ".laz", ".e57", ".tif", ".tiff"),
        "raw_words": ("lidar", "pointcloud", "dem", "corona", "gedi"),
        "label_words": ("landcover", "change", "classification", "canopy"),
        "unit": "site / tile — same geometry, decades apart",
        "anchor": "ground survey / toposheets; modern Sentinel-2 for CORONA",
        "second_ruler": "raster classifications vs raw point clouds",
    },
    "climate": {
        "label": "Climate ERA5 reanalysis x CMIP6 ensemble",
        "raw_exts": (".nc", ".grib", ".zarr"),
        "raw_words": ("era5", "reanalysis", "cmip", "tas", "pr"),
        "label_words": ("extreme", "index", "bias", "correction"),
        "unit": "grid cell x month — same diagnostics across 30+ models",
        "anchor": "ERA5 reanalysis + station records",
        "second_ruler": "each model's convection / parameterisation scheme",
    },
    "singlecell": {
        "label": "Single-cell RNA atlases (HCA/Tabula)",
        "raw_exts": (".h5ad", ".h5", ".loom", ".mtx", ".parquet"),
        "raw_words": ("counts", "expression", "cell", "atlas"),
        "label_words": ("celltype", "cell_type", "cluster", "annotation", "marker"),
        "unit": "cell — same chemistry across tissues and species",
        "anchor": "marker-gene panels; cross-lab consensus labels",
        "second_ruler": "lab A clustering/naming vs lab B on same tissue",
    },
    "lightcurve": {
        "label": "Kepler/TESS light curves",
        "raw_exts": (".fits", ".csv"),
        "raw_words": ("lightcurve", "light_curve", "flux", "cadence", "kepler", "tess"),
        "label_words": ("planet", "candidate", "threshold", "transit", "variable"),
        "unit": "star — 2-min cadence across 200k+ targets",
        "anchor": "confirmed planet / variable catalogues (partial by design)",
        "second_ruler": "threshold-crossing catalogue vs sub-threshold signal",
    },
}

def fidelity_score(name, system=None):
    """Score a filename/URL for raw-fidelity signal under the
    high-fidelity doctrine. Raw capture types outrank derived tables;
    a named system pack sharpens the signal. Returns 0..~12."""
    n = name.lower()
    s = 0
    packs = FIDELITY_PACKS.values() if system is None else [FIDELITY_PACKS[system]] if system in FIDELITY_PACKS else []
    for p in packs:
        if n.endswith(p["raw_exts"]):
            s += 4
        for w in p["raw_words"]:
            if w in n:
                s += 2
        for w in p["label_words"]:
            if w in n:
                s += 1  # label present is useful, but raw is the premium
    return min(s, 12)

def fidelity_card(system):
    """The four-line card the doctrine requires before counting files."""
    p = FIDELITY_PACKS.get(system)
    if not p:
        return None
    return {"system": system, "label": p["label"],
            "RAW": f"raw capture types {p['raw_exts']} / words {p['raw_words']}",
            "UNIT": p["unit"], "LABEL_GAP": p["second_ruler"], "ANCHOR": p["anchor"]}

# --- Niche-keyword registry (2026-11-18, Atharva's direction) ---
# 50 niche domains chosen by three tests — fidelity, headline,
# fragmentation (see README doctrine + NICHES-50.md). The registry in
# niches.json is the campaign-generation queue: campaigns are
# GENERATED from the top of it, not hand-picked. NICHE_PACKS mirrors
# the FIDELITY_PACKS shape so scoring works the same way.
import os as _os
def _load_niches():
    path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "niches.json")
    try:
        with open(path) as fh:
            doc = json.load(fh)
        return {e["slug"]: e for e in doc["niches"]}
    except Exception:
        return {}
NICHE_PACKS = _load_niches()

def niche_score(name, slug=None):
    """Score a filename/URL against a niche's gold words + signature
    extensions (all niches if slug is None). Raw-capture signature
    extensions outrank generic data files. Returns 0..~12."""
    n = name.lower()
    s = 0
    packs = NICHE_PACKS.values() if slug is None else [NICHE_PACKS[slug]] if slug in NICHE_PACKS else []
    for p in packs:
        if n.endswith(tuple(p["signature_exts"])):
            s += 3
        for w in p["gold_words"]:
            if w in n:
                s += 2
    return min(s, 12)

def niche_card(slug):
    """Registry entry as a printable card: fidelity 4-liner, keywords,
    headline shape, score."""
    e = NICHE_PACKS.get(slug)
    if not e:
        return None
    return {"slug": slug, "name": e["name"], "family": e["family"],
            "score": e["score"], "rank": e["rank_by_score"],
            "RAW": e["fidelity_card"]["RAW"], "UNIT": e["fidelity_card"]["UNIT"],
            "LABEL_GAP": e["fidelity_card"]["LABEL_GAP"], "ANCHOR": e["fidelity_card"]["ANCHOR"],
            "keywords": e["keywords"], "headline": e["headline_shape"],
            "why_niche": e["why_niche"], "score_justification": e["score_justification"],
            "signature_exts": e["signature_exts"], "gold_words": e["gold_words"]}

# --- Mammal-grain niche registry (2026-11-18, Atharva's correction) ---
# He meant niches at the grain of "paws and fingerprint analysis of
# mammals": ONE intuitive animal world, a niche = one body/trace/
# pattern system (prints, tracks, whisker spots, flukes, hair casts).
# This registry (mammal_niches.json, built by build_mammal_niches.py)
# sits AHEAD of the broad NICHE_PACKS registry in the campaign queue.
def _load_mammal_niches():
    path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "mammal_niches.json")
    try:
        with open(path) as fh:
            doc = json.load(fh)
        return {e["slug"]: e for e in doc["niches"]}
    except Exception:
        return {}
MAMMAL_NICHE_PACKS = _load_mammal_niches()

def mammal_niche_score(name, slug=None):
    """Score a filename/URL against a mammal niche's gold words +
    signature extensions (all mammal niches if slug is None).
    Mirrors niche_score(), except word matching normalises _ and -
    to spaces first (real files are named guard_hair_scale_cast.tif,
    not 'guard hair scale cast.tif'). Returns 0..~12."""
    n = name.lower()
    n_words = n.replace("_", " ").replace("-", " ")
    s = 0
    packs = MAMMAL_NICHE_PACKS.values() if slug is None else [MAMMAL_NICHE_PACKS[slug]] if slug in MAMMAL_NICHE_PACKS else []
    for p in packs:
        if n.endswith(tuple(p["signature_exts"])):
            s += 3
        for w in p["gold_words"]:
            if w in n_words:
                s += 2
    return min(s, 12)

def mammal_niche_card(slug):
    """Mammal registry entry as a printable card. Mirrors niche_card()."""
    e = MAMMAL_NICHE_PACKS.get(slug)
    if not e:
        return None
    return {"slug": slug, "name": e["name"], "family": e["family"],
            "score": e["score"], "rank": e["rank_by_score"],
            "RAW": e["fidelity_card"]["RAW"], "UNIT": e["fidelity_card"]["UNIT"],
            "LABEL_GAP": e["fidelity_card"]["LABEL_GAP"], "ANCHOR": e["fidelity_card"]["ANCHOR"],
            "keywords": e["keywords"], "headline": e["headline_shape"],
            "why_niche": e["why_niche"], "score_justification": e["score_justification"],
            "signature_exts": e["signature_exts"], "gold_words": e["gold_words"]}

def is_data(url):
    p = unquote(urlparse(url).path.lower())
    return any(p.endswith(e) for e in DATA_EXTS)

def is_image(url):
    p = unquote(urlparse(url).path.lower())
    return any(p.endswith(e) for e in IMAGE_EXTS)

def basename(url):
    return unquote(urlparse(url).path.rsplit("/", 1)[-1])

def gold_score(name, in_archive, only_wayback=False, pack=None):
    n = name.lower()
    s = 0
    words = ALL_GOLD_WORDS if pack is None else DOMAIN_PACKS.get(pack, {}).get("words", ALL_GOLD_WORDS)
    for w in words:
        if w in n:
            s += 3
    if not in_archive:
        s += 4          # stranded outside the archive — the core signal
    if only_wayback:
        s += 3          # deleted from live site, survives only in captures
    sig_exts = (".nii.gz", ".nii", ".gii", ".label", ".annot") if pack is None \
        else DOMAIN_PACKS.get(pack, {}).get("exts", ())
    if n.endswith(sig_exts):
        s += 2          # a signature data file for the field, not just a document
    if pack is None and any(n.endswith(e) for p in DOMAIN_PACKS.values() for e in p["exts"]):
        s += 2
    return s

# ---------------------------------------------------------------- Zenodo
def zenodo_record(record_id):
    r = requests.get(f"https://zenodo.org/api/records/{record_id}",
                     headers=UA, timeout=TIMEOUT)
    r.raise_for_status()
    d = r.json()
    files = [{"name": f["key"], "size": f.get("size"),
              "link": f.get("links", {}).get("self")} for f in d.get("files", [])]
    return {"id": record_id, "title": d.get("metadata", {}).get("title", ""),
            "doi": d.get("doi"), "files": files}

def zenodo_search(query, size=10):
    r = requests.get("https://zenodo.org/api/records",
                     params={"q": query, "size": size}, headers=UA, timeout=TIMEOUT)
    r.raise_for_status()
    out = []
    for h in r.json().get("hits", {}).get("hits", []):
        out.append({"id": h["id"], "title": h.get("metadata", {}).get("title", ""),
                    "files": [f["key"] for f in h.get("files", [])]})
    return out

# ---------------------------------------------------------------- crawl
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.images = [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.images.append(a["src"])
        if tag in ("source", "video") and a.get("src"):
            self.images.append(a["src"])

FILE_TOKEN_RE = re.compile(
    r'[\w\-./ ]+?\.(?:nii\.gz|fastq\.gz|tar\.gz|nii|ply|stl|obj|csv|tsv|json|mat|h5|gii|label|annot|mgz|mgh|'
    r'fits|fasta|fa|fastq|fq|bam|vcf|gff|gtf|shp|geojson|kml|gpkg|wav|flac|mp4|mov|npy|npz|parquet|'
    r'eaf|cha|stm|las|laz|e57|fits|xml|xlsx|zip)\b',
    re.IGNORECASE)
BASE_URL_RE = re.compile(r'"url"\s*:\s*"([^"]+)"')
IGNORE_NAMES = {"feed.xml", "sitemap.xml", "robots.txt", "package.json", "manifest.json"}

def extract_embedded_files(html_text, page_url):
    """The Brain Catalogue lesson: the gold is often NOT in <a href> links.
    Species pages embed a JSON blob in a <script> —
      var info = JSON.parse('{... "url":"/data/Lion/",
        "mri":{"brain":"MRI-n4.nii.gz",
               "atlas":[{"filename":"Hippocampus.nii.gz"}, ...]},
        "mesh":"mesh.ply"}')
    So scan the raw page text for data-file tokens and resolve them
    against any embedded base "url" as well as the page URL itself."""
    clean = html_text.replace("\\\"", '"').replace("\\/", "/")
    # pages also unicode-escape characters in the JSON blob — the Galago
    # page's base is /data/Demidoff\u0027s_dwarf_Galago/ (literal backslash-u),
    # which 404s until decoded
    clean = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), clean)
    bases = [page_url]
    for b in BASE_URL_RE.findall(clean):
        bases.append(urljoin(page_url, b))
        bases.append(urljoin(page_url, b.rstrip("/") + "/"))
    found = {}
    for m in FILE_TOKEN_RE.finditer(clean):
        token = m.group(0).strip().strip('",\'')
        name = token.rsplit("/", 1)[-1]
        if name.lower() in IGNORE_NAMES or len(name) < 4:
            continue
        # keep every base variant — audit HEAD-checks them and keeps the
        # one that actually exists (embedded base /data/<Species>/ usually wins)
        for base in bases:
            full = urljoin(base, token)
            if full.startswith("http"):
                found[full] = {"url": full, "name": name,
                               "found_on": page_url, "via": "embedded"}
    return found

def fetch(url):
    try:
        r = requests.get(url, headers=UA, timeout=TIMEOUT, allow_redirects=True)
        return r
    except requests.RequestException as e:
        print(f"  ! fetch failed {url}: {e}", file=sys.stderr)
        return None

def head_info(url):
    try:
        r = requests.head(url, headers=UA, timeout=TIMEOUT, allow_redirects=True)
        return {"status": r.status_code,
                "size": r.headers.get("Content-Length"),
                "last_modified": r.headers.get("Last-Modified"),
                "content_type": r.headers.get("Content-Type")}
    except requests.RequestException:
        return {"status": None}

def crawl_site(start_url, depth=2, max_pages=60, delay=0.4):
    """BFS same-domain crawl. Returns pages, data files, images."""
    domain = urlparse(start_url).netloc
    seen, queue = set(), deque([(start_url, 0)])
    pages, data_files, images = [], {}, {}
    while queue and len(pages) < max_pages:
        url, d = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        r = fetch(url)
        if r is None or r.status_code != 200:
            continue
        ctype = r.headers.get("Content-Type", "")
        if is_data(url):
            data_files[url] = {"url": url, "name": basename(url), "found_on": url}
            continue
        if "html" not in ctype:
            continue
        pages.append(url)
        p = LinkParser()
        try:
            p.feed(r.text)
        except Exception:
            pass
        for href in p.links:
            full = urljoin(url, href).split("#")[0]
            if not full.startswith("http"):
                continue
            if is_data(full):
                data_files.setdefault(full, {"url": full, "name": basename(full),
                                             "found_on": url})
            elif urlparse(full).netloc == domain and d < depth:
                queue.append((full, d + 1))
        for src in p.images:
            full = urljoin(url, src).split("#")[0]
            if full.startswith("http"):
                images.setdefault(full, {"url": full, "name": basename(full),
                                         "found_on": url})
        # embedded-JSON / script tokens — where stranded files usually hide
        for full, entry in extract_embedded_files(r.text, url).items():
            if is_data(full):
                data_files.setdefault(full, entry)
        time.sleep(delay)
    return {"start": start_url, "pages": pages,
            "data_files": list(data_files.values()),
            "images": list(images.values())}

# ---------------------------------------------------------------- Wayback
def wayback_inventory(domain, limit=5000):
    """All data/image files Wayback captured for a domain (live or deleted)."""
    url = "http://web.archive.org/cdx/search/cdx"
    params = {"url": f"{domain}/*", "output": "json", "fl": "timestamp,original,statuscode",
              "collapse": "urlkey", "limit": limit}
    try:
        r = requests.get(url, params=params, headers=UA, timeout=60)
        r.raise_for_status()
        rows = r.json()
    except Exception as e:
        print(f"  ! wayback failed for {domain}: {e}", file=sys.stderr)
        return []
    out = []
    for row in rows[1:]:
        ts, original, status = row[0], row[1], row[2]
        if is_data(original) or is_image(original):
            out.append({"url": original, "name": basename(original),
                        "first_capture": ts, "status": status,
                        "snapshot": f"https://web.archive.org/web/{ts}id_/{original}"})
    return out

def wayback_page_versions(url):
    """Timestamps of every capture of one page/article — for old-version diffs."""
    try:
        r = requests.get("http://web.archive.org/cdx/search/cdx",
                         params={"url": url, "output": "json",
                                 "fl": "timestamp,statuscode", "collapse": "timestamp:8"},
                         headers=UA, timeout=TIMEOUT)
        r.raise_for_status()
        return [row[0] for row in r.json()[1:]]
    except Exception:
        return []

# ---------------------------------------------------------------- NIfTI check
def check_nifti(url, deep=False):
    """Parse a NIfTI-1 header from a .nii/.nii.gz URL. Flags the two failure
    modes we actually hit on Brain Catalogue: empty placeholders (correct
    grid, no data — needs deep voxel count) and header/grid mismatches."""
    r = fetch(url)
    if r is None:
        return {"ok": False, "reason": "unreachable"}
    raw = r.content
    if url.lower().endswith(".gz"):
        try:
            raw = gzip.decompress(raw)
        except Exception as e:
            return {"ok": False, "reason": f"gzip: {e}"}
    if len(raw) < 348:
        return {"ok": False, "reason": "too small for a NIfTI header"}
    sizeof_hdr = struct.unpack("<i", raw[0:4])[0]
    if sizeof_hdr != 348:
        return {"ok": False, "reason": f"bad header size {sizeof_hdr}"}
    dims = struct.unpack("<8h", raw[40:56])
    ndim, nx, ny, nz = dims[0], dims[1], dims[2], dims[3]
    pixdim = struct.unpack("<8f", raw[76:108])
    vox_offset = struct.unpack("<f", raw[108:112])[0]
    result = {"ok": True, "dims": [nx, ny, nz], "pixdim_mm": [round(p, 4) for p in pixdim[1:4]],
              "voxels": nx * ny * nz, "bytes": len(raw),
              "md5": hashlib.md5(r.content).hexdigest()}
    if deep:
        data = raw[int(vox_offset):]
        result["all_zero"] = all(b == 0 for b in data)
        if result["all_zero"]:
            result["verdict"] = "EMPTY PLACEHOLDER — correct grid, zero data"
    return result

# ------------------------------------------------------- generic checks
def check_file_generic(url, max_bytes=25_000_000):
    """Domain-free version of the NIfTI check: is this file real or a
    placeholder? Downloads (bounded), then reports size, hash, whether
    the content is all-zero/whitespace, and a kind-specific peek —
    zip listing, text line count, PNG dimensions, FITS header card."""
    import io, zipfile
    r = fetch(url)
    if r is None:
        return {"ok": False, "reason": "unreachable"}
    raw = r.content[:max_bytes]
    out = {"ok": True, "bytes": len(r.content), "md5": hashlib.md5(r.content).hexdigest()}
    body = raw
    if url.lower().endswith(".gz") and not url.lower().endswith((".nii.gz", ".fastq.gz")):
        try:
            body = gzip.decompress(raw)
        except Exception:
            body = raw
    out["all_zero"] = len(body) > 0 and all(b in (0, 9, 10, 13, 32) for b in body)
    if out["all_zero"]:
        out["verdict"] = "EMPTY PLACEHOLDER — file exists, content is blank"
    low = url.lower()
    try:
        if low.endswith(".zip"):
            z = zipfile.ZipFile(io.BytesIO(r.content))
            out["zip_entries"] = z.namelist()[:20]
        elif low.endswith((".csv", ".tsv", ".txt", ".stm", ".cha")) and len(body) < max_bytes:
            out["lines"] = body.count(b"\n")
        elif low.endswith(".png") and len(body) > 24:
            out["png_dims"] = list(struct.unpack(">2I", body[16:24]))
        elif low.endswith((".fits", ".fit", ".fts")):
            out["fits_header_ok"] = body[:6] == b"SIMPLE"
    except Exception as e:
        out["peek_error"] = str(e)
    return out

def page_inventory(url):
    """Inventory of data files on ANY archive landing page (Figshare,
    OSF, Dryad, a GitHub repo page, a journal supplement page...) —
    links plus embedded tokens, HEAD-verified. This is the archive
    side of an audit when the archive isn't Zenodo."""
    crawl = crawl_site(url, depth=0, max_pages=3)
    by_name = {}
    for f in crawl["data_files"]:
        if f["name"].lower() in IGNORE_NAMES:
            continue
        by_name.setdefault(f["name"].lower(), []).append(f)
    files = []
    for lname, variants in by_name.items():
        for v in variants:
            h = head_info(v["url"])
            if h.get("status") == 200:
                files.append({"name": v["name"], "size": h.get("size"), "link": v["url"]})
                break
    return {"title": url, "files": files}

def github_inventory(repo):
    """Release assets + repo file listing via the public GitHub API."""
    out = {"title": f"github:{repo}", "files": []}
    try:
        r = requests.get(f"https://api.github.com/repos/{repo}/releases",
                         headers=UA, timeout=TIMEOUT)
        for rel in r.json() if r.status_code == 200 else []:
            for a in rel.get("assets", []):
                out["files"].append({"name": a["name"], "size": a.get("size"),
                                     "link": a.get("browser_download_url")})
    except Exception as e:
        out["error"] = str(e)
    return out

# ------------------------------------------------------------- articles
def articles_diff(url, max_versions=3):
    """The news/article angle: an article page's images and data links
    change over its life — early versions often embed the original
    high-res image or a dataset link that later edits remove. Diff the
    live page against its Wayback snapshots and surface what vanished."""
    def inventory(page_url):
        r = fetch(page_url)
        if r is None:
            return {"images": set(), "data": set()}
        p = LinkParser()
        try:
            p.feed(r.text)
        except Exception:
            pass
        imgs = {urljoin(page_url, s).split("#")[0] for s in p.images}
        data = {urljoin(page_url, h).split("#")[0] for h in p.links if is_data(urljoin(page_url, h))}
        for full in extract_embedded_files(r.text, page_url):
            (data if is_data(full) else imgs).add(full)
        return {"images": imgs, "data": data}
    live = inventory(url)
    versions = wayback_page_versions(url)
    report = {"url": url, "live_images": sorted(live["images"]),
              "live_data": sorted(live["data"]), "snapshots_checked": [],
              "vanished_images": [], "vanished_data": []}
    picks = []
    if versions:
        picks = [versions[0], versions[len(versions) // 2], versions[-1]]
    for ts in dict.fromkeys(picks):
        snap = f"https://web.archive.org/web/{ts}id_/{url}"
        inv = inventory(snap)
        report["snapshots_checked"].append(ts)
        report["vanished_images"] += sorted(inv["images"] - live["images"])
        report["vanished_data"] += sorted(inv["data"] - live["data"])
    report["vanished_images"] = sorted(set(report["vanished_images"]))
    report["vanished_data"] = sorted(set(report["vanished_data"]))
    return report

# ---------------------------------------------------------------- audit
def audit(zenodo_id, site_url, depth=1, deep=False, archive_page=None, github=None):
    if github:
        print(f"Auditing GitHub {github} vs {site_url} ...")
        rec = github_inventory(github)
    elif archive_page:
        print(f"Auditing archive page {archive_page} vs {site_url} ...")
        rec = page_inventory(archive_page)
    else:
        print(f"Auditing Zenodo {zenodo_id} vs {site_url} ...")
        rec = zenodo_record(zenodo_id)
    archive_names = {f["name"].lower() for f in rec["files"]}
    print(f"  archive: {rec['title'][:70]} — {len(rec['files'])} file(s): "
          f"{sorted(archive_names)}")
    crawl = crawl_site(site_url, depth=depth)
    print(f"  site: {len(crawl['pages'])} page(s), {len(crawl['data_files'])} data file(s), "
          f"{len(crawl['images'])} image(s)")
    # group by filename: embedded tokens yield several candidate URLs per
    # name — HEAD-check all and keep the live one (status 200)
    by_name = {}
    for f in crawl["data_files"]:
        if f["name"].lower() in IGNORE_NAMES:
            continue
        by_name.setdefault(f["name"].lower(), []).append(f)
    gold, shared = [], []
    for lname, variants in by_name.items():
        best = None
        for f in variants:
            entry = dict(f)
            entry["head"] = head_info(f["url"])
            if entry["head"].get("status") == 200:
                best = entry
                break
            best = best or entry
        if best is None or best["head"].get("status") != 200:
            continue  # no live variant — not a real candidate
        in_arch = lname in archive_names
        best["in_archive"] = in_arch
        best["score"] = gold_score(best["name"], in_arch)
        if deep and not in_arch:
            if lname.endswith((".nii", ".nii.gz")):
                best["nifti"] = check_nifti(best["url"], deep=True)
            else:
                best["check"] = check_file_generic(best["url"])
        (shared if in_arch else gold).append(best)
    gold.sort(key=lambda e: -e["score"])
    report = {"generated": datetime.now(timezone.utc).isoformat(),
              "zenodo": rec, "site": site_url, "crawl_pages": crawl["pages"],
              "images": crawl["images"],
              "gold_candidates_website_only": gold, "shared_files": shared}
    return report

def print_audit(report):
    gold = report["gold_candidates_website_only"]
    print(f"\n=== GOLD CANDIDATES (on website, NOT in archive): {len(gold)} ===")
    for g in gold:
        nifti = g.get("nifti", {})
        verdict = f" | {nifti.get('verdict', '')}" if nifti.get("verdict") else ""
        chk = g.get("check", {})
        if chk.get("verdict"):
            verdict += f" | {chk['verdict']}"
        dims = f" | dims {nifti['dims']}" if nifti.get("ok") else ""
        print(f"  [score {g['score']:2d}] {g['name']}  ({g['head'].get('size')} B){dims}{verdict}")
        print(f"           {g['url']}")
    if not gold:
        print("  none — site and archive match, or crawl found no data files.")

def save(report, name):
    import os
    os.makedirs("outputs", exist_ok=True)
    path = f"outputs/{name}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    with open(path, "w") as fh:
        json.dump(report, fh, indent=2)
    print(f"\nSaved: {path}")
    return path

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("audit", help="diff an archive record/page against a project website")
    a.add_argument("--zenodo", help="Zenodo record id")
    a.add_argument("--archive-page", help="any archive landing page (Figshare/OSF/Dryad/journal supplement)")
    a.add_argument("--github", help="GitHub owner/repo — diff its release assets against the site")
    a.add_argument("--site", required=True, help="project page/site URL")
    a.add_argument("--depth", type=int, default=1)
    a.add_argument("--deep", action="store_true", help="download candidates and check for empty placeholders")

    ar = sub.add_parser("articles", help="diff an article page's images/data links against its Wayback snapshots")
    ar.add_argument("--url", required=True)

    c = sub.add_parser("crawl", help="inventory data files + images on a site")
    c.add_argument("--site", required=True)
    c.add_argument("--depth", type=int, default=2)
    c.add_argument("--max-pages", type=int, default=60)

    w = sub.add_parser("wayback", help="list archived data files for a domain")
    w.add_argument("--domain", required=True)

    s = sub.add_parser("sweep", help="run audit/crawl/wayback over a seeds file")
    s.add_argument("--seeds", required=True,
                   help='JSON list: [{"name":..., "zenodo": id-or-null, "site": url}]')

    f = sub.add_parser("fidelity", help="high-fidelity doctrine: list systems, show a system's 4-line card, or score a site's files by fidelity")
    f.add_argument("--system", choices=sorted(FIDELITY_PACKS), help="one seeded fidelity system")
    f.add_argument("--site", help="optional site to crawl and fidelity-score")
    f.add_argument("--depth", type=int, default=1)
    f.add_argument("--max-pages", type=int, default=30)

    ni = sub.add_parser("niches", help="niche-keyword registry (NICHES-50.md / niches.json): list all 50 ranked by score, top N, or one niche's full card — the campaign-generation queue")
    ni.add_argument("--niche", choices=sorted(NICHE_PACKS), help="one niche slug — print its card, keywords and headline shape")
    ni.add_argument("--top", type=int, metavar="N", help="print only the top N niches by score")

    mn = sub.add_parser("mammal-niches", help="MAMMAL-GRAIN niche registry (MAMMAL-NICHES-50.md / mammal_niches.json): 50 print/trace/pattern systems inside one animal world — sits AHEAD of the broad registry in the campaign queue")
    mn.add_argument("--niche", choices=sorted(MAMMAL_NICHE_PACKS), help="one mammal niche slug — print its card, keywords and headline shape")
    mn.add_argument("--top", type=int, metavar="N", help="print only the top N mammal niches by score")

    args = ap.parse_args()

    if args.cmd == "audit":
        if not (args.zenodo or args.archive_page or args.github):
            ap.error("audit needs one of --zenodo, --archive-page, --github")
        report = audit(args.zenodo, args.site, depth=args.depth, deep=args.deep,
                       archive_page=args.archive_page, github=args.github)
        print_audit(report)
        save(report, f"audit-{args.zenodo or 'page'}")
    elif args.cmd == "articles":
        rep = articles_diff(args.url)
        print(f"Live: {len(rep['live_images'])} image(s), {len(rep['live_data'])} data link(s); "
              f"snapshots checked: {rep['snapshots_checked']}")
        print(f"Vanished since (in old versions, not live): {len(rep['vanished_images'])} image(s), "
              f"{len(rep['vanished_data'])} data file(s)")
        for u in rep["vanished_data"] + rep["vanished_images"][:20]:
            print(f"  {u}")
        save(rep, "articles")
    elif args.cmd == "crawl":
        r = crawl_site(args.site, depth=args.depth, max_pages=args.max_pages)
        print(f"Pages: {len(r['pages'])}  Data files: {len(r['data_files'])}  Images: {len(r['images'])}")
        for f in sorted(r["data_files"], key=lambda x: -gold_score(x["name"], False)):
            print(f"  [score {gold_score(f['name'], False):2d}] {f['name']}  <- {f['found_on']}")
        save(r, "crawl")
    elif args.cmd == "wayback":
        files = wayback_inventory(args.domain)
        data = [f for f in files if is_data(f["url"])]
        imgs = [f for f in files if is_image(f["url"])]
        print(f"Wayback captures for {args.domain}: {len(data)} data file(s), {len(imgs)} image(s)")
        for f in sorted(data, key=lambda x: -gold_score(x["name"], False, True)):
            print(f"  {f['first_capture']}  {f['name']}  {f['snapshot']}")
        save({"domain": args.domain, "data_files": data, "images": imgs}, "wayback")
    elif args.cmd == "sweep":
        seeds = json.load(open(args.seeds))
        all_reports = []
        for seed in seeds:
            print(f"\n######## {seed.get('name', seed.get('site'))} ########")
            rep = {"seed": seed}
            if seed.get("zenodo") and seed.get("site"):
                rep["audit"] = audit(str(seed["zenodo"]), seed["site"])
                print_audit(rep["audit"])
            elif seed.get("site"):
                rep["crawl"] = crawl_site(seed["site"], depth=2)
                print(f"  crawl: {len(rep['crawl']['data_files'])} data file(s)")
            if seed.get("site"):
                domain = urlparse(seed["site"]).netloc
                rep["wayback"] = wayback_inventory(domain)
                print(f"  wayback: {len(rep['wayback'])} archived data/image file(s)")
            all_reports.append(rep)
            time.sleep(1)
        save({"sweep": all_reports}, "sweep")
        print("\nSweep done. Rank gold candidates across reports by 'score'.")
    elif args.cmd == "fidelity":
        if args.system and not args.site:
            card = fidelity_card(args.system)
            print(f"\n=== {card['label']} ===")
            for k in ("RAW", "UNIT", "LABEL_GAP", "ANCHOR"):
                print(f"  {k}: {card[k]}")
            save({"fidelity_card": card}, f"fidelity-{args.system}")
        elif args.site:
            r = crawl_site(args.site, depth=args.depth, max_pages=args.max_pages)
            scored = sorted(r["data_files"], key=lambda x: -fidelity_score(x["name"], args.system))
            print(f"Pages: {len(r['pages'])}  Data files: {len(scored)}  (fidelity-ranked, system={args.system or 'any'})")
            for fi in scored:
                print(f"  [fidelity {fidelity_score(fi['name'], args.system):2d} / gold {gold_score(fi['name'], False):2d}] {fi['name']}  <- {fi['found_on']}")
            cards = [fidelity_card(args.system)] if args.system else [fidelity_card(k) for k in FIDELITY_PACKS]
            save({"site": args.site, "system": args.system, "cards": cards,
                  "data_files_fidelity_ranked": [{**fi, "fidelity": fidelity_score(fi["name"], args.system)} for fi in scored]}, "fidelity")
        else:
            print("Seeded high-fidelity systems (all pass the 4-line test on paper; verify before campaigning):")
            for k in sorted(FIDELITY_PACKS):
                c = fidelity_card(k)
                print(f"\n  {k}: {c['label']}\n    UNIT: {c['UNIT']}\n    ANCHOR: {c['ANCHOR']}")
    elif args.cmd == "niches":
        ranked = sorted(NICHE_PACKS.values(), key=lambda e: e["rank_by_score"])
        if args.niche:
            c = niche_card(args.niche)
            print(f"\n=== {c['name']} (`{c['slug']}`) — score {c['score']}/10, rank {c['rank']} of {len(ranked)} ===")
            print(f"  Family: {c['family']}")
            for k in ("RAW", "UNIT", "LABEL_GAP", "ANCHOR"):
                print(f"  {k}: {c[k]}")
            print(f"  HEADLINE: {c['headline']}")
            print(f"  Keywords: {'; '.join(c['keywords'])}")
            print(f"  Signature files: {', '.join(c['signature_exts'])} | Gold words: {', '.join(c['gold_words'])}")
            print(f"  Why niche: {c['why_niche']}")
            print(f"  Score justification: {c['score_justification']}")
            save({"niche_card": c}, f"niches-{args.niche}")
        else:
            show = ranked[:args.top] if args.top else ranked
            print(f"Niche-keyword registry — {len(ranked)} niches, ranked by score (campaign-generation queue; --top N / --niche <slug>):")
            for e in show:
                print(f"  {e['rank_by_score']:2d}. [{e['score']}/10] {e['slug']} — {e['name']}")
                print(f"      {e['headline_shape']}")
            if args.top:
                save({"niches_top": show}, f"niches-top{args.top}")
    elif args.cmd == "mammal-niches":
        # Sort by CURRENT score (calibration amends scores in
        # mammal_niches.json; rank_by_score is the stale pre-campaign
        # order and is kept only as a tiebreak) — patched 2026-11-18
        # before Campaign 8, per CALIBRATION-2026-11-18 tooling note.
        ranked = sorted(MAMMAL_NICHE_PACKS.values(), key=lambda e: (-e["score"], e["rank_by_score"]))
        if args.niche:
            c = mammal_niche_card(args.niche)
            print(f"\n=== {c['name']} (`{c['slug']}`) — score {c['score']}/10, rank {c['rank']} of {len(ranked)} ===")
            print(f"  Family: {c['family']}")
            for k in ("RAW", "UNIT", "LABEL_GAP", "ANCHOR"):
                print(f"  {k}: {c[k]}")
            print(f"  HEADLINE: {c['headline']}")
            print(f"  Keywords: {'; '.join(c['keywords'])}")
            print(f"  Signature files: {', '.join(c['signature_exts'])} | Gold words: {', '.join(c['gold_words'])}")
            print(f"  Why niche: {c['why_niche']}")
            print(f"  Score justification: {c['score_justification']}")
            save({"mammal_niche_card": c}, f"mammal-niches-{args.niche}")
        else:
            show = ranked[:args.top] if args.top else ranked
            print(f"Mammal-grain niche registry — {len(ranked)} niches, ranked by score (campaign queue, AHEAD of the broad registry; --top N / --niche <slug>):")
            for i, e in enumerate(show, 1):
                print(f"  {i:2d}. [{e['score']}/10] {e['slug']} — {e['name']}")
                print(f"      {e['headline_shape']}")
            if args.top:
                save({"mammal_niches_top": show}, f"mammal-niches-top{args.top}")

if __name__ == "__main__":
    main()
