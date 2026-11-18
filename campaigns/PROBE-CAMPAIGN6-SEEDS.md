# Probe — Campaign 6 seeds (2026-11-18)

Generated FROM the niche registry (`niches.json`, top of queue), per
the niche-keyword doctrine: this probe is **tooling validation and
targeting only, not a research campaign**. The top 8 niches are
exactly the eight scoring 9/10. For each: keyword web searches to
identify concrete hosts, then — where a host was concrete — a light
hunter crawl (depth 1, ≤15 pages) and/or Wayback status-200
inventory via `goldmine_hunter.py` (`outputs/probe-campaign6.log`,
`outputs/probe-campaign6-20261118.json`).

**No gold is claimed anywhere in this file.** A probe hit is a seed,
not a find. Gold requires a campaign: status-200-filtered counts and
sample-download verification, per the standing method.

## Per niche — what the probe actually saw

### 1. frog-call-archives (9/10) — STRONGEST probe signal
- **Fonoteca Zoológica, `fonozoo.com`** (Museo Nacional de Ciencias
  Naturales, Madrid — the sound library frog-call papers deposit to,
  with accession numbers, e.g. #9844/#9845 in a 2016 Pristimantis
  paper). Probe crawl returned 0 pages, but a direct GET in the
  follow-up check returned **200 (68,512 B, index.html)** — the 0 is
  a crawler limit on its front end, stated plainly, not a dead site.
  **Wayback inventory: 201 status-200 data files, all .mp3**,
  date-coded filenames (e.g. `09-05-05-09-52-08.mp3`), first
  captures **2006–2012** — direct-file captures of the library's
  recordings, exactly the hunter's pattern. Whether they are still
  served live in that form is a campaign question, not a probe one.
- UCI Anuran Calls dataset: features (MFCCs) only, not raw audio —
  second-ruler material, not a host.

### 2. fish-otoliths (9/10) — two concrete collection hosts
- **AFORO, `aforo.cmima.csic.es`** (ICM-CSIC, Barcelona): the site
  itself reports **9,821 high-resolution sagitta images, 2,980
  species, 289 families**, still accreting named collections in
  2025. Old JSP-era site. Probe crawl: 15 pages, 0 data files,
  31 images; Wayback status-200 data files: 0 — the images sit
  behind the database interface, so this needs the dedicated-
  adapter treatment (the DigiMorph/FishBase class), stated as such.
- **Otolitos UNAM, `otolitos.unam.mx`**: Mexico's first digital
  otolith collection — 3,001 lots, ~2,600 optical/SEM images, 214
  species, with biometric + capture data per specimen. Probe crawl:
  5 pages, 1 data file (a site video), Wayback 0 — same
  behind-interface shape as AFORO.
- Marine Institute Burrishoole (Ireland): a 1928–2020 scale-and-
  otolith archive with an image library, described in a 2020
  *Ecological Informatics* paper — a named physical archive whose
  web surface is the institute catalogue (shared with niche 4).

### 3. salmon-scale-archives (9/10) — labels gapped exactly as carded
- **NOAA NEFSC Atlantic Salmon Scale Measurements**
  (`fisheries.noaa.gov`, InPort record 27493): scale images + age /
  origin / measurement data "to archive", two .xlsx files listed —
  and the record states the data may sit on an **internal NEFSC
  network** with access constrained. Probe crawl of the domain:
  15 pages, 0 data files, 249 images. The gap between "archived"
  and "reachable" is the niche in one record.
- The anchor already exists and is published: the 2025 PLOS ONE
  known-age validation set (254 PIT-tagged fish, scale images on
  Figshare) — proof the two-rulers comparison is runnable.
- Rivers-trust scale reading (e.g. Ayrshire Rivers Trust) shows the
  reader-disagreement pattern in the open ("two or three different
  opinions in the office") — anecdote, not a host.

### 4. autopsy-cause-of-death-ledgers (9/10) — one live host, honest negatives
- **Barts Health / QMUL dissection registers** (`qmul.ac.uk`):
  digitised register volumes served as PDFs from the page (the page
  itself warns of 30–60 s downloads); fields include age, sex,
  cause of death, place of death — a concrete, live, case-level
  host, 19th–20th century.
- Columbia Presbyterian autopsy reports 1872–1919: **finding aid
  only, not digitised** (staff will search by exact date only) —
  probe negative, stated.
- JJ Hospital Mumbai 1884–1966: 13,024 autopsies analysed in a
  published paper; the underlying records are not online — paper-
  only, not a web host.
- NY State Archives Middletown autopsy record book 1891–1905:
  catalogue entry exists, access restricted — not a probe host.

### 5. electric-fish-eod (9/10) — lab host found, recordings not yet surfaced
- **Mormyrids, `mormyrids.efishgenomics.com`** (the Cornell/Hopkins-
  lineage lab site): detailed EOD recording protocol pages (96 kHz
  .wav practice, Mormyroscope), i.e. the lab that holds expedition
  recordings. Probe crawl: 15 pages, 1 data file (rss.xml),
  96 images; Wayback status-200 data files: 2 (rss.xml only). The
  .wav piles themselves did **not** surface at depth 1 — a deeper
  crawl / embedded-token pass is Campaign 6 work, not done here.

### 6. longitudinal-growth-studies (9/10) — probe NARROWS the niche
- **AAOF Craniofacial Growth Legacy Collection**
  (`aaoflegacycollection.org`): nine of the eleven US collections
  (Bolton-Brush, Fels, Burlington, Denver…) already consolidated —
  13,000–16,000+ images, ~750 children, records 1930–1985, free to
  researchers, and a 2025 consortium paper integrates them further.
  Probe crawl: 0 pages; Wayback status-200 data files: 2 (demo
  videos only — images move by request, not direct files).
  **Fragmentation verdict on contact: the flagship level of this
  niche is consolidated.** The niche survives only in its strays —
  the 2 un-joined US collections, non-US studies, and the
  non-craniofacial series — and the Campaign 6 seed below is aimed
  there, not at AAOF.

### 7. river-gauge-charts (9/10) — probe NARROWS the flagship basin
- Bavarian Danube gauge charts 1826–1894 were **already rescued**
  (ESSD 2025; versioned dataset on Zenodo) — that basin is done;
  do not fire there.
- Irish OPW / ICARUS hydrometric data rescue: autographic chart
  archives from 1939/40 exist and rescue is an active PhD-scale
  effort, but the rescued series are not a public host yet.
- USDA Fernow: strip charts were digitised into a published daily
  series — done, by the book.
- The niche stands (chart rooms in every basin authority), but the
  Campaign 6 seed must name a **non-Danube, non-USDA basin**; the
  probe did not verify one, and says so.

### 8. long-term-crop-plot-books (9/10) — flagship curated, tail open
- Morrow Plots (Illinois): **curated and published 2022–2024**
  (Illinois Data Bank, CC-BY; *Scientific Data* paper) — the
  flagship is consolidated, exactly the outcome the niche card
  anticipated. Rothamsted likewise has its own archive (eRA).
- The niche's tail — the dozens of other long-term stations whose
  plot-level data still lives in station reports — was not crawled
  in this probe; naming and checking the next stations (Sanborn
  Field and its peers) is the first Campaign 6 task for this niche.

## Campaign 6 seed list — ready to fire, ordered by probe promise

| # | Host / target | Niche | Why this order |
|---|---|---|---|
| 1 | `fonozoo.com` (Fonoteca Zoológica) | frog-call-archives | Only probe host with a real Wayback data pile already visible: 201 status-200 .mp3s, 2006–2012 |
| 2 | `aforo.cmima.csic.es` (AFORO) | fish-otoliths | 9,821 images / 2,980 species on an old JSP site; needs an adapter pass, pile size is stated by the host itself |
| 3 | `otolitos.unam.mx` | fish-otoliths | 2,600 images / 214 species with per-specimen data; same adapter class as #2, second collection for the comparable set |
| 4 | `qmul.ac.uk` Barts dissection registers | autopsy-cause-of-death-ledgers | Digitised case-level PDFs live now; the only autopsy host that survived the probe |
| 5 | `mormyrids.efishgenomics.com` | electric-fish-eod | The recording lab's own site; deep crawl + embedded-token hunt for .wav is the campaign step |
| 6 | `fisheries.noaa.gov` NEFSC scale lab + Marine Institute Burrishoole catalogue | salmon-scale-archives (+ otoliths) | "Archived but internal" is the exact label gap; Burrishoole is one physical archive behind both niches |
| 7 | The 2 un-joined US growth collections + non-US growth studies (to be named by the campaign) | longitudinal-growth-studies | AAOF is consolidated; only the strays pass the fragmentation test |
| 8 | Non-flagship long-term stations — Sanborn Field class (to be named by the campaign) | long-term-crop-plot-books | Morrow/Rothamsted are curated; the tail stations are the niche |
| 9 | A non-Danube basin-authority chart archive (to be named by the campaign) | river-gauge-charts | Danube is rescued and published; the seed is the *class*, with the basin still to be picked |

Seeds 7–9 are honestly class-level, not host-level: the probe
narrowed those niches by killing their flagships, and naming the
replacement hosts is Campaign 6's first job — not something this
probe fakes.

*Probe method note: searches run 2026-11-18 from the niches'
registered keywords; crawls depth 1 / ≤15 pages; Wayback counts
status-200-filtered before counting, per standing method. Total new
disk for the whole niche build (registry + tooling + probe): well
under 1 MB of outputs — no data files were downloaded.*
