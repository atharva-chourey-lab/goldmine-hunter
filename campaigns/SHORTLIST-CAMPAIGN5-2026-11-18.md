# Goldmine Hunter — Campaign 5 shortlist (2026-11-18)

Campaign 5 ("tons and tons of gold"): 17 fresh sites, none hunted in
Campaigns 1–4 — old lab / personal / university sites and vintage
edition stacks, per the pattern that actually pays (Maddison
vintages, Campaigns 2+3). Every site crawled live (depth 1, max 25
pages) + Wayback-inventoried with **statuscode:200 filtering before
counting**, then every promising pile sample-verified by download
(`verify5.py` + `verify5b.py`; `outputs/verify5-20261118-174328.json`,
`outputs/verify5b-20261118-174506.json`; samples in
`gold/campaign5-verify/`, 660 KB total new disk). Raw counts alone
counted nothing. One disclosure: the Penn World Table target sits on
rug.nl — ggdc.net was hunted in Campaign 2, but for *Maddison*; PWT
itself, on this host, was never hunted.

**Headline, plainly: Campaign 5 found no STRANDED set.** Tons of
files, yes — 511 live unique data files and 5,722 whole-domain
Wayback-200 files — but tons of *gold*, no. What survived
verification is one small DELETED set (SCOP release files) and four
large PUBLISHED-BY-DESIGN vintage stacks that are still live on
their own sites (CRU, Reptile Database, CLIO Infra, ATNF). The
vintage stacks are genuinely comparable sets and are ranked below
as inventory assets, not recoveries — the same honesty rule as
Campaign 4.

## The find — deleted, verified (small)

**SCOP 2020-02-28 release files (DELETED, Wayback-only, verified).**
The old MRC-LMB Cambridge host `scop.mrc-lmb.cam.ac.uk` served the
SCOP2 release under `/files/`. Those URLs now return **404 live on
both http and https** (HEAD-checked), and the release survives in
Dec-2020 Wayback captures — the comparable set is small:

| File | Capture | Evidence |
|---|---|---|
| `scop-cla-20200228.txt` | 2020-12-02 | real text, first line `# SCOP release 2020-02-28`, 8,687 lines in the capture as served |
| `scop-cla-latest.txt` | 2021-01-26 | same release lineage (not separately downloaded) |
| `scop_fa_represeq_lib20200228.fa` | 2020-12-02 | real FASTA, first header `>8072807 FA=4003632 FA-PDBID=3KCN_A FA-UNIID=Q7UJS6` |

Verification: `scop-cla-20200228.txt` downloads at exactly
1,048,576 B as served by Wayback (its HEAD Content-Length is also
1,048,576), md5 `1587ec3973a770b813cb5666d5b9e1a9` — *caveat,
plainly:* a round 1 MiB is suspicious and the capture may itself be
truncated; what is verified is ≥1 MiB of real classification text,
not a complete file. The represeq `.fa` head (bounded 1 MB sample)
is likewise real FASTA, md5 of sample
`914c0312a2919215e5a3e62f14f1615b`. *Second caveat:* SCOP2 is
distributed today through other channels — the recovery value is
this host's 2020 release vintage, not unique data. This is a
one-release, two-content-file set: deleted and verified, but it
does not complete a comparison the way Brain Catalogue or Maddison
did.

## The vintage stacks — published-by-design, still live, verified

**CRU UEA climate version stack (PUBLISHED-BY-DESIGN, live,
verified).** `crudata.uea.ac.uk/cru/data/` keeps superseded versions
openly beside current ones — CRUTEM3 next to CRUTEM4/5, CRU TS
3.23 → 4.06 with per-country files and release-vs-release comparison
folders. The campaign's live crawl found 0 files (the tree is not
navigable by the depth-1 crawler), but the files themselves are
live: `CRUTEM3-gl.dat` HEAD live size 30,855 B, and the Wayback
2016 capture downloads at 30,855 B, md5
`6b5990670a6f5a982de4c3d43c96afd7`, real anomaly-series text
(first row begins `1850 -1.757 -0.267 …`); `abstem3.zip` live 200
(52,215 B); `CRUTEM.4.2.0.0.anomalies.nc` live 200 (20,494,628 B,
netCDF). Targeted CDX: crutem3 subtree 36 status-200, temperature
subtree 169, hrg subtree 1,801 (incl. 290 status-200 CRU TS 3.23
per-country `tmp` files). *Caveat:* the live check on the
cru_ts_3.23 country subtree specifically failed through the proxy
(directory URL) and is **not** claimed either way; the crutem3 and
temperature trees are verified live. A Two-Rulers-shaped vintage
comparison (version-vs-version temperature series) is sitting here
in the open — inventory, not recovery.

**Reptile Database checklist stack (PUBLISHED-BY-DESIGN, live,
verified).** `/data/` holds a dated checklist series —
**37 checklist files, 2013_03 → 2026_06** (`.xls.zip` to 2015_03,
`.xlsx` after, incl. the 2022_07 v2/v3 and 2024_08 v2 revisions) —
plus `reptile_synonyms_2023_04.xlsx`,
`originaldescriptions2009.xls` / `originaldescriptions2017.xlsx`,
and paper supplement tables (Garg 2019, Marshall 2020, type-catalogue
Tables S1–S3). 57 status-200 files under `/data/*`; **every one
HEADs 200 live** with spreadsheet content types. Verification:
`reptile_checklist_2013_12.xls.zip` — Wayback capture 253,165 B,
md5 `58169036be8fea12bb7e6815f9efd1b1`, valid zip; the **live file
is md5-identical**. `Genera_without_photos.xlsx` live verified
(23,261 B, md5 `4f087f269a3cd978c07218df93a5488d`, valid zip).
One catalogue, one pipeline, 13 years of vintages — a real
time-comparable set, openly published.

**CLIO Infra indicator stack (PUBLISHED-BY-DESIGN, live,
verified).** 356 live data files in the crawl (the `/data`
Compact/Broad indicator workbooks + `/docs` country files), and the
`/IndicatorsPerCountry/` tree — the same indicators sliced
per-country × territorial-reference — hits the CDX collapse cap:
9,998 status-200 at a 10,000 limit, so the true count is higher.
Verification kills any deleted reading: the smallest IPC file,
`Samoa_Workingweekinmanufacturing_TerritorialRef_1976_2012_CCode_882.xlsx`
(4,190 B), is **md5-identical live and in Wayback**:
`93bd3439c5ad8e338a3f91da72e68648`, valid zip.
`CompositeMeasureofWellbeing_Compact.xlsx` live verified
(377,874 B, md5 `867920e6b26b881e2bc73cfc8899914e`). The largest
pile of the campaign, and it is the site's own published database
in two slicings — inventory at scale, not a recovery.

**ATNF Pulsar Catalogue version stack (PUBLISHED-BY-DESIGN, live,
verified).** 92 live files, dominated by the `psrcat_pkg` download
series: every release from **v1.9 through v2.9.0** openly listed
(v2.9.0, v2.8.1, v2.8.0, v2.7.0, v2.6.x … v1.9 in the crawl's top
20). Verification: oldest crawled version `psrcat_pkg.v1.9.tar.gz`
downloads real gzip, 337,183 B, md5
`c9c80cbc0fe5fbf115de57e5964fbe89`; HEADs — current pkg 1,249,005 B,
v2.9.0 1,233,779 B, and even v1.45 (not in the crawl's top list)
still live at 533,577 B. A complete version lineage of one
catalogue, published by design.

## Inventory, verified real, published-by-design (say so plainly)

- **Bank of England research datasets.** Millennium of
  Macroeconomic Data v3.1 spreadsheet live (HEAD 27,533,690 B,
  spreadsheet content type; a bounded 2 MB head shows PK magic —
  the zip is unreadable at that bound because it is truncated,
  the same artefact Campaign 4 corrected on HCA, not a defect).
  The Wayback bank-liabilities-survey annexes that looked
  Wayback-only are still live: 2018-Q4 annex live size 166,324 B,
  exactly the Wayback download's size (wb copy verified valid zip,
  md5 `553012f8e9d3612569e7073681a0051b`).
- **PDG 2026 edition file.** `mass_width_2026.txt` live verified
  text (31,863 B, md5 `90d304f3df77266daf8ec3a3eef447a4`, header
  `MASSES, WIDTHS, AND MC ID NUMBERS FROM 2026 EDITION OF RPP`).
  Historical editions live under `/YYYY/` by design; the depth-1
  crawl reached only the current edition, so no edition stack is
  counted or claimed.
- **OEIS b-files.** Live verified: `b001006.txt` 1,062,369 B, md5
  `44ee15276b5e42654f6c0c400bbea21b`, real sequence text. The 379
  Wayback-200 files are the same live per-sequence files.
- **RUG / GGDC historical national accounts.** The live finds on
  rug.nl were GGDC `hna_*_09.xls` country files, not PWT:
  `hna_bel_09.xls` verified OLE2, 786,944 B, md5
  `553c05160a31130aeeef9774e719fee5`. Published lab-site data.
- **Starling / GLD.** `timestr.zip` live verified (261,439 B, md5
  `6e44e988c64bfa8065e1e7eec22dbcf0`, valid zip). The database
  itself sits behind the site's CGI query interface (the GLD
  pattern from the search-visible site: browse/search/build, PDF
  or Excel generated on demand) — no downloadable wordlist pile
  was found at depth 1, stated as a host result.
- **CATH old API derived data (Wayback, real, not claimed as a
  set).** The 2011 `/api/data/derived_data/…` alignment files are
  real FASTA in Wayback (sample: 512 B head, md5
  `db51d502c670432e548680f06015c2d5`, first header
  `>domain|1ft9A02|3_4_0`). Per-superfamily API output,
  published-by-design when served; the campaign did not verify the
  pile as a comparable set and does not claim it.

## Kills and corrections (plainly)

- **Reptile "Wayback-only checklists" was wrong on first look.**
  The /data files looked like a deleted vintage series; every one
  is still live and the sampled checklist is md5-identical to its
  Wayback capture. Published stack, not a recovery (see above).
- **Starling `bsh.xls` / `bshet.xls` are NOT deleted.** Wayback
  copies verified real OLE2 (49,664 B, md5
  `381b4d300ea2f067fae06c33f3e975f8`; 338,944 B, md5
  `75416e4925190dc6cbf24e845a4c6309`) — and both HEAD **200 live
  at identical sizes**. Inventory.
- **CLIO's 2,901 campaign Wayback count understates the pile and
  overstates nothing else.** The whole-domain inventory was
  cap-limited; the targeted IPC count is ≥9,998 status-200 — and
  the sampled file is md5-identical live, so the bigger number
  changes the inventory size, not the class.
- **CATH live "data files" are phantoms.** The crawl's top hits
  (`text.label`, `/path/to/file.fasta`, `-.atom.fa` variants) are
  documentation example URLs; they download as the site's HTML app
  page (10,520 B, md5 `a5b3b57b59695ee0b2e2f3697084b725`). Zero real
  live data files from those links.
- **Villanova White Dwarf Catalog: no data pile.** Targeted CDX
  over `WDCatalog/*` (2,698 status-200 captures) contains **zero
  data-extension files** — the catalogue was HTML tables — and
  `mccook/*` likewise zero. The `WD*.txt` files HEASARC cites were
  FTP-served and are not in the http captures. The catalogue's data
  survives as HTML pages plus the HEASARC/VizieR subsets, which are
  published. Kill.
- **UCSC pile is contamination for goldenPath purposes.** The 342
  Wayback-200 files are `/admin` software archives and `/gbdb`
  browser-backend FASTA (e.g. `Group1.fa` live 200, 22,730,493 B —
  the genome browser's own backend, live by design). goldenPath
  assembly downloads proper contributed ~0 at this crawl. Not an
  assemblies recovery.
- **PWT on rug.nl: no vintage pile.** rug.nl's 5 Wayback-200 "data
  files" are CMS metadata XMLs (`newsarticle.xml`, `published.xml`,
  a pgp key) — phantoms for this hunt. PWT's current release is
  Dataverse-hosted and its earlier releases are linked from the
  release pages as published downloads; nothing stranded or
  deleted was found on this host.
- **Tree of Life: phantom.** Its 2 live "data files" are external
  BBC News `.stm` article links, not ToL data. Zero found.
- **D-PLACE: app responses, not a pile.** The 71 Wayback-200 files
  are the web app's geojson parameter responses; D-PLACE data is
  published via its project repositories by design. Nothing
  stranded found at depth 1.
- **Minor Planet Center: one visualisation file, not the
  catalogue.** Sole Wayback data file of note:
  `asteroid_data.json` (2015) verified real text/JSON, 3,703,427 B,
  md5 `b0ed1d30bf7eb0c7103a4aa563f910c2` — the asteroid-explorers
  web visualisation's data, trivial against the MPC catalogue,
  which sits behind its data services.
- **Pfam: zero.** Host unreachable from here and 0 Wayback-200 data
  files on the domain — a host result, not a claim about where
  Pfam releases live by design (InterPro/EBI).
- **CRU "0 live files" was a crawler limit, not a deletion.** The
  depth-1 crawl could not navigate the crudata tree; direct HEADs
  prove the version stack is live (above). Corrected here so the
  1,532 whole-domain Wayback-200 count is never read as a deleted
  pile.

## Ranking

1. **SCOP 2020 release files** — the campaign's only DELETED,
   verified set; ranked first by provenance class, with its size
   (two content files, one possibly-truncated capture) and
   caveats stated, not buried.
2. **CRU version stack** — live and published, but the most
   analysis-ready inventory of the campaign: one instrument
   family, many versions, per-country and per-release-comparison
   files, verified identical across Wayback and live.
3. **Reptile checklist stack** — 37 dated vintages of one
   catalogue, md5-verified, openly live; a species-count /
   taxonomy-churn time series waiting to be run.
4. **CLIO Infra stack** — the largest pile (356 live + ≥10k
   per-country slices), verified real and md5-stable, but it is
   one published database in two slicings.
5. **ATNF psrcat lineage** — complete v1.9→v2.9.0 version stack,
   verified; published-by-design.

No stranded set, and no pile here completes a comparison the way
the Brain Catalogue or Maddison sets did. Campaign 5's honest
yield is one small deleted vintage (SCOP) plus confirmation that
the vintage-edition vein, on these 17 fresh hosts, now runs mostly
to *kept* old versions — labs that never deleted their stacks
(CRU, Reptile, ATNF, CLIO) rather than stranded files. That is
itself a finding about where the pattern still lives: the gold
is no longer deletion, it is un-run comparisons across stacks
nobody deleted.

*Method note (standing): Wayback counts status-200-filtered before
counting; every claimed set has ≥1 sample download with size + md5
in `outputs/verify5-20261118-174328.json` /
`outputs/verify5b-20261118-174506.json`. README verified-results
not updated — no find in this campaign meets the stranded-gold bar
those entries set.*
