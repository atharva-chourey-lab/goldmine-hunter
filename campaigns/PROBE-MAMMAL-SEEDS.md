# Probe — mammal-grain Campaign seeds (2026-11-18)

Generated FROM the mammal-grain registry (`mammal_niches.json`, top of
queue — this registry now sits AHEAD of the broad registry), per
Atharva's correction. This probe is **targeting and tooling
validation only, not a campaign**. For the top 6 niches: keyword web
searches to identify concrete hosts/collections, then — where a host
was concrete — a light hunter crawl (depth 1, ≤15 pages) and/or
Wayback status-200 inventory via `goldmine_hunter.py`
(`probe_mammal.py`; output `outputs/probe-mammal-20261118-182301.json`).

**No gold is claimed anywhere in this file.** A probe hit is a seed,
not a find. Gold requires a campaign: status-200-filtered counts and
sample-download verification, per the standing method (GRADES.md).

## Per niche — what the probe actually saw

### 1. primate-fingerprints-dermatoglyphics (9/10) — archive-shaped, catalogue-first
- **UCL Galton Papers, `archives.ucl.ac.uk`** — the catalogue itself
  is the evidence: file GALTON/2/9/6/3/4, "Indian Fingerprints,
  Chimpanzee Fingerprints and Analysis" (1892–1895), including a
  bundle of ~20 chimpanzee fingerprints sent by W. F. R. Weldon in
  1894 with photographic enlargements (also catalogued at Wellcome
  Collection, work n9q6q77r). Galton's "Finger Imprints Vol. I"
  (1890) is a 75-page album of annotated print sets. Access is
  reading-room, not download — this niche's campaign is an
  archive-digitisation hunt (what has Wellcome/UCL already imaged?),
  not a crawl.
- **Penrose Papers dermatoglyphics (PENROSE/2/42), Wellcome/UCL** —
  notebooks, patient dermatoglyphic analyses and print photographs
  from the Galton Laboratory era; several series are closed-store,
  stated plainly: the catalogue is public, the prints mostly are not
  (yet) digital.
- **Midlo & Cummins, *Palmar and Plantar Dermatoglyphics in
  Primates* (1942), full text on archive.org** — 602 figures, 36
  genera, with a source table depositing which prints came from
  where (Wistar Institute). The monograph is the published layer;
  the underlying print sets are the stranded layer it points to.
- **Smithsonian National Anthropological Archives** — American
  Dermatoglyphics Association records and T. D. Stewart's Maya
  fingerprint/palm-print manuscripts (1947–49, with Cummins
  correspondence) in the NAA subject guide.

### 2. cattle-muzzle-prints (9/10) — the biggest archive is paper, by design
- **Wagyu Registry Association (Kyoto)** — per Minagawa et al. 2002
  (via Farmers' Weekly's review): muzzle prints lifted in ink before
  4 months and again after 14 months; **more than 3 million beef
  cattle registered this way since 1948**. Every registered animal
  has a certificate carrying its nose print beside its pedigree
  (certificates surface commercially, e.g. Kobe-beef nose-print
  certificates reproduced by retailers). No public digital surface
  for the print archive was found by this probe — the seed is the
  institution and its card system; the campaign question is what, if
  anything, has been scanned, and what the pre-1948→present
  Petersen-tradition university series (350+ prints in 1922 alone)
  left behind.
- Second-ruler infrastructure is live and public: Japan's national
  cattle ID search (NLBC) keys animals by 10-digit ID with DNA
  sampled — the ruler the print archive was never joined to.

### 3. paw-track-morphometrics-fit (9/10) — front-end is a shell; the sets are per-project
- **WildTrack, `wildtrack.org`** — probe crawl: 15 pages, 4 unique
  data files (all site furniture: sitemaps/.label files), 89 images;
  Wayback-200: 7 data files (all sitemaps), 876 images. The FIT
  method is fully documented in the open (standardised photo
  protocol, 120+ measurements/print, algorithms for 13+ species —
  rhino, tiger, cheetah, puma, tapirs, polar bear), and WildTrack's
  own material says the reference data is built per species from
  **captive known-individual training sets**. Those training sets —
  the actual gold — live with the projects/zoos, not on wildtrack.org.
  Campaign shape: hunt the per-species project piles FIT was trained
  on, plus pre-FIT hand-measured track tables. Probe verdict: seed
  the *projects*, not the homepage.

### 4. whale-fluke-trailing-edge (9/10) — narrowed on contact, honestly
- **The narrowing:** the North Pacific humpback set has already been
  joined — Cheeseman et al. 2023 combined **39 catalogues, 27,956
  individuals**, into Happywhale. For that ocean/species the
  fragmentation test now FAILS; do not campaign there expecting
  stranded gold.
- **Juneau Flukes, `juneauflukes.org`** — probe crawl: 5 pages, 0 data
  files, 22 images; Wayback-200: 3 data files (robots/sitemap/one
  audio), 461 images. The catalogue itself is a **2025 PDF on the
  site (252 individual humpbacks, 2006–2024)** — a published local
  catalogue of exactly the classic shape, one of dozens of regional
  PDF/print catalogues (Glacier Bay, Gulf of Maine, Newfoundland…)
  that predate or sit beside the platforms.
- **What remains un-joined (the seed):** film/slide-era catalogues,
  Southern Ocean and Atlantic regional sets, and sperm-whale fluke
  catalogues — none of which the North Pacific consolidation touched.

### 5. dolphin-dorsal-fin-notches (9/10) — one gulf joined, the rest FinBase-era
- **Sarasota Dolphin Research Program, `sarasotadolphin.org`** —
  probe crawl: 15 pages, 1 data file (a site video), 107 images;
  Wayback-200: 18 data files (17 sitemaps + robots), 334 images.
  The site states the substance: a fin catalogue of **5,000+
  distinctive individuals**, and SDRP curates **GoMDIS — 35 Gulf of
  Mexico catalogues, 23,444 individuals, 41,492 images** — joined,
  but researcher-only. Outside the Gulf, the FinBase (Access-era)
  catalogue world — hundreds of bays, each a desktop database —
  was never networked. NOAA's InPort even serves individual
  catalogue extracts (e.g. the Beaufort catalog's dolphin-ID CSV)
  piecemeal.
- Campaign shape: inventory the non-Gulf FinBase-era catalogues and
  the piecemeal NOAA/agency extracts; Sarasota/GoMDIS is the anchor
  and the proof that joining pays, not the target.

### 6. elephant-ear-edge-veins (9/10) — card tradition, partly still physical
- **ElephantVoices, `elephantvoices.org`** — probe crawl: 15 pages,
  1 data file (a CDN video), 117 images; Wayback-200: 20 data files —
  all .mp3 (the *calls* database surfacing in 2012 captures), 751
  images. The ID system itself is documented in the open: Amboseli's
  method (ear tears, holes, vein patterns; **1,600+ elephants
  catalogued since 1972**, physical photographic ID cards in
  Amboseli, digital cards in Gorongosa/Mara), and the Gorongosa
  "Who's Who & Whereabouts" database is **password-protected**
  (poaching precaution, stated in the Science 2021 supplement).
- Campaign shape: the seed is the *card tradition across sites* —
  Amboseli (ATE), Gorongosa and Mara (ElephantVoices), Samburu
  (Save the Elephants) — and the question of what of the paper-card
  era is digitised, where, and in whose custody. Expect an
  access-and-inventory campaign, not a download campaign.

### 7. (bonus, search-evidence only) whisker-spot-patterns (9/10, rank 7)
Not crawled in this probe; search evidence alone: the lion method
(Pennycuick & Rudnai 1970) is live in Kruger (EWT whisker-spot
cataloguing), in India via the Wildlife Institute of India's "Lion"
software (wii.gov.in), and in Namibia's Desert Lion work; the
Australian sea-lion whisker validation set (53 individuals, 99%
pattern uniqueness at population 50) is published. Three literatures,
one point-pattern geometry, no joined archive — a first-class seed
for the mammal campaign's second wave.

## Ready-to-fire mammal Campaign seed list (in firing order)

1. **Juneau Flukes + regional fluke PDF catalogues** (Glacier Bay,
   Gulf of Maine, Newfoundland) — classic-shape local catalogues;
   campaign = inventory + sample-verify the PDFs/images, skipping
   the already-joined North Pacific platform set.
2. **Non-Gulf FinBase-era dolphin catalogues + NOAA InPort
   catalogue extracts** — desktop-database catalogues, piecemeal
   public extracts; Sarasota/GoMDIS as anchor only.
3. **Elephant ID-card sites** (ATE Amboseli; ElephantVoices
   Gorongosa/Mara; Save the Elephants Samburu) — inventory what of
   the card era is digital and where it is custodied.
4. **Galton/Penrose dermatoglyphics digitisation surface**
   (archives.ucl.ac.uk, Wellcome Collection) + Midlo & Cummins'
   deposited print sources (Wistar) — what is already imaged vs
   catalogue-only.
5. **Wagyu Registry muzzle-print system + Petersen-tradition
   university series** — establish what digital surface, if any,
   the 3M-print card archive has; NLBC as second ruler.
6. **FIT per-species project piles** (via WildTrack's species list:
   rhino, tiger, cheetah, tapir, polar bear projects) — hunt the
   captive training sets and pre-FIT measurement tables, not the
   homepage.
7. **Whisker-spot catalogues** (WII Lion software records, EWT
   Kruger, Desert Lion Conservation; sea-lion validation sets) —
   second wave, search-evidenced in this probe.

*Method note (standing): probe crawls are depth-1 front-end checks;
a 0-data-file crawl of a CMS homepage says nothing about the
catalogue behind it, and this file claims nothing more than it
shows. Every seed above needs a campaign — status-200-filtered
counts plus sample-download verification — before the word gold
is used.*
