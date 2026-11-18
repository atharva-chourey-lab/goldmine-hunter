# Goldmine Hunter — Campaign 6 / Wave 1 shortlist (2026-11-18)

The first **registry-generated** campaign: all 9 seeds from
`PROBE-CAMPAIGN6-SEEDS.md`, in probe order, heads of the eight
9/10 niches. Grades were fixed BEFORE digging in `GRADES.md`
(git commit `6d76541`) and are applied below exactly as written —
GOLD / DIAMOND / SILVER / INVENTORY / KILL, never awarded on raw
counts. Method: live crawl + Wayback inventory filtered to
statuscode:200 before counting (`campaign6_wave1.py`,
`outputs/campaign6-20261118-181409.json`), then two verify passes
(`verify6.py`, `verify6b.py`; `outputs/verify6-20261118-181716.json`,
`outputs/verify6b-20261118-181956.json`; samples in
`gold/campaign6-verify/`, 2.2 MB total new disk).

**Headline, plainly: Wave 1 found GOLD — one set, the campaign's
#1 seed — plus one SILVER. No diamond.** The registry's top seed
did what Campaigns 4 and 5's hand-picked hosts never did. The
other seven seeds produced one silver, two inventories and a run
of honest kills, detailed below; the registry's scores
over-predicted strandedness for interface-era collections, and
`CALIBRATION-2026-11-18.md` cuts five scores for it.

## GOLD — stranded, verified

**Fonoteca Zoológica sound pile (STRANDED, sample-verified) —
`fonozoo.com`, Museo Nacional de Ciencias Naturales (CSIC),
Madrid. Niche: frog-call-archives.**
Targeted CDX over `fonozoo.com/*`: 9,907 collapsed captures,
**1,013 status-200 data files** — one library's audio, in five
sub-piles:

| Sub-pile | status-200 files | What it is |
|---|---|---|
| `/sonidos/` | 751 mp3 | the published sound-guide tracks: 593 species-named (`0800 alytes muletensis.mp3`), 89 purely numbered, rest mixed |
| `/fnz_back/propios/files/` | 166 mp3 | the FZ Sound Collection's own accessions, filenames carrying date + subject + accession suffix |
| `/fnz_back/publicados/files/` | 29 mp3 | published-collection files |
| `/archivos/` | 23 mp3 | the 2006–2012 date-coded pile the probe first saw |
| `/audios/` + guide dirs | 44 mp3/wav | guide-page samples (Madagascar, Cuba, Bali…) |

Verification (Wayback `id_` downloads; the live origin answers
our client with an identical 403 / 34 B stub for every file path
while serving its homepage — see caveat):

| Sample | Evidence |
|---|---|
| `14650_web_1736941493.mp3` (propios, wb 2026-01-06) | 32,507 B, md5 `f65154f0c53f16bd283c4254e8e60872`; `file`: MPEG layer III 128 kbps; ffprobe: MP3 44.1 kHz mono, 2.69 s |
| `26 Pelodytes Punctatus…_1551687956.mp3` (publicados, wb 2022-06-15) | 140,015 B, md5 `1a29349bc7cd1634c7442515b180d781`; MPEG layer III, stereo |
| `2690.mp3` (/sonidos, wb 2015-09-27) | 85,680 B, md5 `444fcff1127224891c9fd465ce657cb7`; ffprobe: MP3 44.1 kHz mono 320 kb/s, 2.12 s (1,044 B leading junk skipped by the decoder — a real call clip, not a phantom) |
| `2677.mp3` (/sonidos, wb 2015-09-26) | 625,893 B, md5 `5f6994189179de22f7aaad504d73633f`; ffprobe: MP3 44.1 kHz mono, 15.62 s |
| `OadeModified.wav` (/audios, wb 2015-09-22) | RIFF/WAVE magic, 3,014,656 B downloaded at the 3 MB cap, md5 of head `800212208d615010e1853f35ae557bbe` |

Why GOLD, element by element (per `GRADES.md`): *comparable
set* — 1,013 files, one library, one accession system (Fonozoo
Ref. numbers), hundreds of species, overwhelmingly anuran
advertisement calls; *stranded* — the audio lives on the
collection's own site and in **no formal archive** (no Zenodo /
GBIF / repository deposit of the audio exists; the institution's
catalogue is an index, not an audio archive); *anchor* — the
catalogue's own accession records, voucher specimens and
type-locality recordings (the library's detail pages carry
species, recordist and Fonozoo Ref. per recording); *un-run
comparison* — below. **Not DIAMOND:** nothing in the verified set
itself yet shows two rulers disagreeing — that is what the
comparison would test, and a diamond may not be awarded on hope.

*Caveats, plainly:* (1) live retrievability — Wayback's crawler
received 200s from the origin as recently as 2025-10-07
(`/sonidos/0721.mp3`) and 2026-01-06 (propios files), so the
files exist server-side; our own client gets the 403 stub, so
today the openly retrievable copies are Wayback's. (2) Two
recent-capture samples (Sep 2025) downloaded as 4.6 KB HTML
block pages despite CDX status 200 — those captures are
phantoms and were excluded; grading rests only on the
audio-verified samples above. (3) Only a handful of files were
sampled, per method — the pile's count is a CDX count of
captures, each graded file is one of the verified samples.

**The un-run comparison this enables (the minting step, queued,
not run):** re-identify the Fonoteca's accessioned advertisement
calls — filed under the species names of their recording era —
against today's DNA-split anuran taxonomy, anchored on the
catalogue's voucher and type-locality accessions, and count how
many recordings change species.

## SILVER — published-by-design, verified

**Barts dissection registers (PUBLISHED-BY-DESIGN, live,
verified) — QMUL / Barts Health NHS Trust Archives. Niche:
autopsy-cause-of-death-ledgers.** The registers page links five
digitised volumes directly: `SBHMS-E-12-1.pdf` … `-5.pdf` under
`qmul.ac.uk/fmd/media/smd/archives/`. Sample verified: vol. 1
downloads live at **30,015,488 B, md5
`1e5ff76f3290366fd0c1d79e18f007cb`, %PDF magic** — case-level
entries (name, age, sex, abode, date/place of death, cause of
death, burial) for the 19th–early-20th-century dissected dead of
St Bartholomew's Hospital Medical College. Exactly the niche
card's material, served openly by its own archive: SILVER, not
gold — a recovery of nothing. The cross-hospital case-level
panel (Barts × the other digitised registers) remains un-built
and is the comparison this stack waits for.

## INVENTORY — verified real, published, no comparison completed

- **NOAA NEFSC Atlantic salmon scale measurements
  (PUBLISHED-BY-DESIGN).** InPort record 27493's two spreadsheets
  are publicly downloadable from NOAA's open-data GCS bucket
  (`nmfs_odp_nefsc/PARR/READ/PSB/NEST/27493/`): the SALSEA
  2009–2011 file verified — **1,043,189 B, md5
  `7097ea91ca3c9557630fc45e210c7c1c`, valid xlsx** (second file:
  `2016 nefsc-salmoscale-Feb2017.xlsx`, 8,685,316 B, listed not
  sampled). Measurements only: the scale *images* — the niche's
  raw capture — remain, per the record itself, on an internal
  NEFSC network. Inventory.
- **Waterlevel.ie station CSVs (PUBLISHED-BY-DESIGN).** The OPW
  hydrometric service serves per-station CSVs live (sample:
  `25017_0001.csv`, 77,318 B, md5
  `a0ba67fe80e06c0bbb824d37a8114857`, real CSV text; the 2019
  Wayback station download is likewise real, 20,776 B, md5
  `138799f3ea1f74a22f915df525bf1b42`, and the same endpoint
  answers 200 live today). A working data service, not an
  archive recovery. Inventory.

## KILLS — probed, nothing claimable, evidence stated

- **AFORO (fish-otoliths) — adapter class, as the probe
  predicted.** The JSP app (`isis.cmima.csic.es/startDB_en.jsp`,
  200, 302,808 B) serves only interface chrome and logos at file
  level; the 9,821 images sit behind its database queries. The
  one crawl-found file (`aforo-result/DOCS/dist.zip` on the
  legacy cmima host) is now unreachable. And the collection is
  mirrored to GBIF as a formal occurrence dataset
  (doi:10.15468/wdwxid) — the images' home is a published
  catalogue, not a stranded pile. Kill as a hunter target.
- **Otolitos UNAM (fish-otoliths) — adapter class.** Catalogue
  and search are PHP endpoints (`Catalogo_Otolitos.php`,
  `Busqueda_Otolitos.php`, both 200); their HTML carries no
  specimen-image files (logos and one diagram only) — the ~2,600
  images sit behind the search interface. Wayback: 84 status-200
  captures, zero data files. Kill as a hunter target.
- **Mormyrids EOD lab (electric-fish-eod) — no pile.** The
  campaign's deepest crawl (60 pages, depth 2) surfaced 2 data
  files, both RSS feeds; a Wayback CDX query filtered to
  wav/mp3/zip/wma/aif across the whole domain returns **zero**.
  The lab's expedition recordings are not on its website in any
  captured form. Kill.
- **Burrishoole IFBA (salmon-scale-archives) — catalogue only.**
  The GeoNetwork record (data.marine.ie, dataset 4067) is live
  metadata (49,681 B, 27 URLs, none a download); per the 2020
  *Ecological Informatics* paper the image library lives in a
  collaborative online space, not public files. The physical
  1928–2020 archive is real; as a web host, kill.
- **Harpenden Growth Study (longitudinal-growth-studies) — in
  the formal archive.** UK Data Service study 9330; its data
  dictionary verified live (260,994 B PDF, md5
  `c27cb7f54c0024d912a84486871c6590`). The flagship pattern
  repeats: AAOF consolidated 9 of 11 US/Canada collections, and
  the named non-US stray turns out to be properly archived too.
  Kill for strandedness.
- **Nittedal Growth Study (longitudinal-growth-studies) — no
  host.** Named in the literature as a separate University of
  Oslo collection used by collaboration; no public file host
  exists to hunt. Kill as a seed (stated, not faked).
- **Sanborn Field (long-term-crop-plot-books) — no file pile.**
  Crawl of the MU CAFNR pages plus a sanborn-filtered CDX over
  cafnr.missouri.edu (69 collapsed, 42 status-200) yields pages,
  timeline entries and images — zero data files; the
  extension.missouri.edu CDX query timed out and is reported as
  unrun, not as zero. Sanborn's plot-level records circulate as
  published summaries and by request. Kill as a hunter target.
  (Correction to verify6's raw output: the MU Extension mp0939
  "PDF" fetch returned a 425 B HTML stub — it is **not** a
  verified PDF and nothing above rests on it.)
- **Irish river-gauge charts (river-gauge-charts) — paper
  only.** The autographic charts themselves are physical records
  at OPW Headford (per the ICARUS/OPW rescue papers); the rescued
  8-catchment series is published (PANGAEA 950792), and
  waterlevel.ie serves current data (inventory above). No chart
  scans exist on any host probed. Kill for this basin.

## Ranking

1. **Fonozoo audio pile — GOLD.** The wave's find: 1,013
   status-200 audio files, sample-verified as real recordings,
   in no formal archive, with an anchor and an un-run comparison.
2. **Barts dissection registers — SILVER.** Five case-level
   volumes, live and verified; published by design.
3. **NOAA scale spreadsheets + waterlevel.ie CSVs —
   INVENTORY.** Real, useful, openly published; nothing to
   recover.

*Method note (standing): Wayback counts status-200-filtered
before counting; every grade above GOLD-or-below rests on ≥1
sample download with size + md5 + magic in
`outputs/verify6-20261118-181716.json` /
`outputs/verify6b-20261118-181956.json`. Total new disk this
wave: ~2.2 MB of samples. README verified-results: the Fonozoo
set meets the stranded bar those entries set — flagged here for
the parent to update, not silently edited by this campaign.*
