# Goldmine Hunter — Campaign 4 shortlist (2026-11-17)

Campaign 4 ("fire for more"): 15 sites — 4 Fidelity-Campaign leftovers
(Digital Brain Bank, Tabula Muris, Kepler/STScI, Human Cell Atlas) plus
11 old lab/project/personal sites. Every site crawled live + Wayback-
inventoried with **statuscode:200 filtering before counting**, then
every promising pile sample-verified by download (`verify4.py`,
`outputs/verify4-20261118-012052.json`; samples in
`gold/campaign4-verify/`). Raw counts alone counted nothing.

**Headline, plainly: Campaign 4 found no STRANDED set.** The stranded
pattern did not appear on any of these 15 hosts. What survived
verification is one DELETED set (HCA matrices), one historical-edition
catalogue stack that is published-by-design (GCVS), and a tail of
honest inventory. Totals: 720 live unique data files (657 of them one
site's published archive — STScI HLSP), 1,049 whole-domain
Wayback-200 files (916 of them contamination — see the GCVS kill).

## The find — deleted, verified

**Human Cell Atlas 2019–20 portal project matrices (DELETED,
Wayback-only, verified).** The old `data.humancellatlas.org` portal
served one generated expression matrix per project under
`/project-assets/project-matrices/`. The portal was redesigned, the
URLs now return **404 live** (HEAD-checked), and the matrices survive
only in Jan-2020 Wayback captures: **12 matrix files across 6 projects,
in up to 3 generated formats each** — the comparable set:

| Project | csv.zip | loom | mtx.zip | metadata TSV |
|---|---|---|---|---|
| 4d6f6c96 | ✓ | ✓ | ✓ | — |
| cc95ff89 | ✓ | ✓ | ✓ | ✓ |
| 005d611a | — | ✓ | ✓ | — |
| 4a95101c | — | ✓ | ✓ | — |
| 8185730f | ✓ | — | — | — |
| c4077b3c | — | — | ✓ | ✓ |
| 8c3c290d | — | — | — | ✓ |

Verification: the smallest `.loom` (4d6f6c96, CDX length
276,345,172 B) downloads with a real **HDF5 magic header**
(head-1 MB md5 `676dba1096b17104bbc2edbac66f8364`); the smallest
`.csv.zip` (8185730f) returns **PK zip magic** on a range request
(the full file is ~75 MB CDX-compressed — an earlier "not a valid
zip" line in the verify log was my own 40 MB download cap cutting
off the zip's central directory, corrected here); a project-metadata
TSV is real decodable text (1,048,576 B, md5
`3456d5e3afddb242131620061fce40df`, proper HCA file-core header).
*Caveat, plainly:* these were published-by-design when served, and
the current HCA portal re-serves HCA project data in new form — the
recovery value is the 2019–20 pipeline's own 3-format vintage, not
unique data. Files are large (75 MB–2.1 GB per CDX record); nothing
was bulk-downloaded.

## Science — what else survived verification

**GCVS historical-edition stack (PUBLISHED-BY-DESIGN, Wayback copies
verified real).** Under the catalogue's own directory
`/gcvs/gcvs/`: 663 collapsed captures, 603 status-200, **160
data-extension files** grouped as editions — GCVS III (14 files),
GCVS 5 (4), the NL74–NL88 name-list series (~5 per part), vol1, nsv,
cep, v, glcl_var. Sample-verified real text data: `iii.dat`
6,651,562 B, md5 `fa0366fe4b74a9dd3c54899be702f849` (GCVS III main
catalogue, 2011 capture); `cep/cat_3.dat` 95,316 B, md5
`5c612d0f40f7958ff22670e6c07c2189`; `glcl_var.dat` 253,163 B, md5
`4b6579bbd9d389dd38765e0c1717de42`. GCVS is a published catalogue of
record (CDS/VizieR) — this is the old-edition stack in one place,
**not a recovery**, and it is ranked here only because the editions
form one comparable historical set.

**NOW fossil-mammal static compilations (PUBLISHED-BY-DESIGN,
live, verified).** 14 live files in two comparable groups:
`/static/now/datasets/` — 7 literature-compilation zips
(Alroy 1998 → Fortelius 2003) + the modern dental-measurements CSV;
`/static/now/field_cat/` — Sinap and Lantian field catalogues
(.xls + .txt) and 2 journal-supplement .xlsx. The site content-
addresses its files, and the downloads prove it: dental CSV
42,576 B, md5 `b63c3f89c38d2391b9202217359f8060` — the md5 *is* the
hash embedded in its filename; Fortelius 2003 zip 554,327 B, md5
`338638644ed31f6036e3f02751b5201f`, valid zip. The 2023 Wayback copy
of the dental CSV is md5-identical to live — same published file,
not a deleted vintage.

**Inventory, verified real, published-by-design (say so plainly):**

- **STScI HLSP (657 live files).** MAST's High Level Science Products
  archive, openly listed. Verified: AGN SED atlas obs-cat CSV
  17,963 B, md5 `9b029b3e3e3947ca8ddae95d75297ed1`; its catalogue
  FITS 54,720 B, md5 `bac715c31aae043f78d64455c7286d48`, header
  `SIMPLE = T`. Real archive, zero recovery content.
- **Neotoma snapshot series (live).** ~15 dated database dumps,
  2015→2024, openly listed on the site — a time-comparable set of
  one database's vintages. Verified: schema-only tar 1,085,440 B,
  md5 `05cc1338fd5c4ddfe4a2638f7b0f2a43`, opens, 2 entries (dump +
  README). HEAD sizes: 2016 snapshot zip 29,919,107 B; 2024
  ndb-only tar 104,448,000 B; latest clean dump (S3) 2,553,350,161 B.
- **AnAge / Senescence.info (live).** CellAge zip verified
  (21,540 B, md5 `a0543f64ca6574a7b6ffb5bc0bfe1418`, contains
  `cellage3.tsv`); diet dataset zip verified (8,209 B, md5
  `dae6d10f7efd893477d3911c61f4a2be`); TableS2.xls verified OLE2
  (49,152 B, md5 `01d5f6647e7210863d3fa931d62476eb`). These are the
  site's own published databases (GenAge/CellAge family).
- **Rosetta Project Swadesh lists (PUBLISHED-BY-DESIGN via
  archive.org — its formal archive).** Verified via the download
  path: Catalan `cat.txt` 1,781 B, md5
  `5b720c29871b990d7e1053f5b06e8252`, real wordlist text.

## Fidelity Lane A — the 4-line card verdicts on what was found

The seeded cards hold *on paper* for all four systems. On the data
this campaign actually found:

**Digital Brain Bank — connectome: card FAILS on found data.**
RAW ✗ (0 live files; the domain's only Wayback-200 data file is
`robots.txt`, 137 B, verified — not data). UNIT / LABEL GAP /
ANCHOR: untestable, no units or labels found. Not landed via this
host.

**Tabula Muris — singlecell: card FAILS on found data.**
RAW ✗ (0 live data files; sole Wayback-200 file is the web-app
`manifest.json`, 317 B, verified). UNIT / LABEL GAP / ANCHOR:
untestable on found data. The atlas's real data lives off-host by
design (Biohub channels); it was not hunted there in this campaign.

**Kepler/STScI — lightcurve: card FAILS on found data.**
RAW ~ (real FITS/CSV verified — but they are HST HLSP photometric
catalogues; **zero Kepler/TESS light-curve files** in the crawl).
UNIT ✗ as specified (HLSP is many instruments/protocols, not one
2-min cadence across 200k stars). LABEL GAP / ANCHOR: untestable —
no threshold-crossing vs sub-threshold pair found. Crawling the
archive root inventories MAST, not the Kepler mission archive.

**Human Cell Atlas — singlecell: card PARTIALLY holds.**
RAW ✓ (count matrices kept in 3 generated formats; HDF5/PK/TSV
verified above). UNIT ✓ (cells across 6 projects, one portal
pipeline — completeness table above). LABEL GAP ~ (metadata TSVs
survive for only 3 of 7 project UUIDs; no second-ruler cell-type
labels inside the pile — the matrices are one pipeline's output).
ANCHOR ✗ on found data (no marker-panel or consensus-label set in
the pile). Two lines hold, one partial, one fails — the deleted
pile alone is not a re-derivation-ready bundle.

## Kills and corrections (plainly)

- **GCVS "916 Wayback files" was contamination.** sai.msu.su is
  mostly an Apache software mirror; the campaign's whole-domain
  inventory counted Apache release zips. Path-scoped, the real
  catalogue is the 160-file stack above. (Same whole-domain caveat
  applies to every campaign number; GCVS is where it bit.)
- **AnAge evolution supplements are NOT deleted.** The Wayback
  copies looked Wayback-only because the live crawl's evolution
  pages failed through the proxy. Live re-downloads are
  **md5-identical** to the Wayback captures:
  `supplemental_tables.zip` 144,136 B, md5
  `fffb45c0a31a8463368e93bd6bcb09bf` (contains
  `supplemental_tables.xls`); `mammalian_supplement.zip` 105,639 B,
  md5 `920664d32bf3a36cd5330d3c3f67eaf0` (contains `data.xls`,
  `gene_pairs.xls`, `methods.pdf`); `animals_aln.zip` is a real zip
  of mitochondrial alignments (12S/16S/COX/CYTB/ND…) and is also
  still live. Published inventory, not a vintage recovery.
  (`overall_stats.txt` differs live vs its 2005 capture — a changed
  reference text, not a dataset find.)
- **Human Protein Atlas: phantom.** The top "data" hit
  `d.data.label` downloads as a 157,046 B HTML app page; the other
  hit is a promo movie. Zero real data files found by this crawl —
  HPA's real download bundles were not surfaced at depth 1, which
  is a crawl limit, not proof they don't exist.
- **Neotoma `taxa_changes.json`: phantom** — returns the site's
  HTML (HEAD 404). The snapshot tars beside it are real (above).
- **Rosetta crawler URLs were phantoms, the data is not.** The
  `/stream/` URLs return archive.org viewer HTML (151,495 B of it);
  the same files via `/download/` are real (Catalan list above).
- **Harvard Whole Brain Atlas: no data.** 0 live data files; the
  only 2 Wayback-200 files are tiny texts — `case.txt` is actually
  an HTML case description (1,076 B) and `jnavcd.txt` a 649 B
  navigation file. The atlas is images behind a viewer; nothing
  recoverable as data here.
- **HyperLEDA: no catalogue pile.** Data sits behind its query
  interface. Sole Wayback file `line_code.txt` (2,594 B, md5
  `13dd876b25e0af13296dd5c485b12cce`, 2003) is a spectral-line code
  reference table — real, trivial, not the catalogue.
- **TreeBASE: no pile.** Data sits behind the web app. Sole
  Wayback-200 file `kmltreeserver.zip` is a valid 443 B zip
  containing one KML server file — not alignments.
- **Animal Diversity Web, Seshat: zero.** ADW: 0 live data files,
  0 Wayback-200 (data behind its API/accounts). Seshat: site
  unreachable from here and 0 Wayback data captures on the domain.
  Nothing found on either host — stated as a host result, not a
  claim about where their data lives by design.
- **GCVS `/gcvs/digit/` (935 status-200 captures)** is mostly
  project-page images and documents; the `mdv/` per-star subdirs
  were not verified as a set in this pass and are **not** claimed.

## Ranking

1. **HCA matrices** — the campaign's only DELETED, verified set;
   ranked first by provenance class, with its caveats (huge files,
   current portal re-serves HCA data) stated, not buried.
2. **GCVS edition stack** — verified real and genuinely comparable
   across editions, but published-by-design; an inventory asset,
   not a recovery.
3. **NOW static compilations** — live, hash-verified, comparable
   literature compilations; published-by-design.

No stranded set, and no inventory pile here completes a comparison
the way the Brain Catalogue or Maddison sets did. Campaign 4's
honest yield is one deleted vintage (HCA) plus confirmation that
the old-lab-site vein, on these 11 fresh hosts, now runs mostly to
published-by-design or behind-interface data.

*Method note (standing): Wayback counts status-200-filtered before
counting; every claimed set has ≥1 sample download with size + md5
in `outputs/verify4-20261118-012052.json`. README verified-results
not updated — no find in this campaign meets the stranded-gold bar
those entries set.*
