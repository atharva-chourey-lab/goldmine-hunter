# Goldmine Hunter

**Atharva Chourey Lab — independent research lab.** A human–AI
collaboration: Atharva Chourey works with Lapis (Muse), an AI
research partner; all results are framed as the collaboration's.

Finds datasets stranded on project websites that never made it into the
formal archive — the exact pattern behind the Brain Catalogue find
(2026-11-16): Zenodo held only the lion's raw MRI, while
braincatalogue.org quietly hosted the hand-drawn `Hippocampus.nii.gz`
and `Telencephalon.nii.gz` segmentations for a decade.

**The full campaign record is published in `campaigns/`, and the
coupled narrative — the tooling paradigm, the document and campaign
evolution, and the pain points — is in [EVOLUTION.md](EVOLUTION.md).**
Grades were fixed in writing before the campaigns they grade
(`campaigns/GRADES.md`); minted sets spin off into pre-registered
projects under `spinoffs/`.

## Campaigns index

| Campaign | Date | Targets | Verdict |
|---|---|---|---|
| Campaign 1 (Brain Catalogue sweep) | 2026-11-16 | 37 species pages vs the local archive | Gold pattern re-found cold; 53 real / 18 empty-placeholder labels of 71 |
| Campaigns 2+3 | 2026-11-17 | 16 science + social-science sites | **DELETED gold** — Maddison's 2006–2010 vintages, Wayback-only, verified ([shortlist](campaigns/SHORTLIST-2026-11-17.md)) |
| Fidelity campaign | 2026-11-17 | 9 high-fidelity systems | Rhino-5 landed; Gaia×GALAH measured; cryo-EM set measured ([report](campaigns/FIDELITY_CAMPAIGN_2026-11-17.md)) |
| Cosmology × chemistry | 2026-11-17 | TNG/EAGLE/SIMBA × APOGEE/GALAH | A comparison, not a recovery — published-by-design ([report](campaigns/campaign-cosmology-chemistry.md)) |
| Campaign 4 | 2026-11-17 | 15 hosts (fidelity leftovers + old lab sites) | No stranded set; one small DELETED set (HCA matrices) ([shortlist](campaigns/SHORTLIST-CAMPAIGN4-2026-11-17.md)) |
| Campaign 5 | 2026-11-18 | 17 fresh old lab/personal sites | No stranded set; SCOP deleted + CRU/Reptile/CLIO/ATNF live stacks → CRU minted as SILVER ([shortlist](campaigns/SHORTLIST-CAMPAIGN5-2026-11-18.md), [spin-off](spinoffs/cru-vintages/)) |
| Campaign 6 / Wave 1 (registry) | 2026-11-18 | Broad niche registry top 8 niches, 9 seeds | **GOLD** — Fonoteca Zoológica frog-call pile, 1,013 files stranded; SILVER Barts ([shortlist](campaigns/SHORTLIST-CAMPAIGN6-WAVE1-2026-11-18.md), [spin-off](spinoffs/fonozoo-reidentification/)) |
| Campaign 7 / Mammal Wave 1 | 2026-11-18 | Mammal-grain registry top 7 seed groups | No gold; SILVER ×2 (Juneau flukes, Wellcome Galton IIIF); Wagyu custody finding ([shortlist](campaigns/SHORTLIST-CAMPAIGN7-MAMMAL-2026-11-18.md)) |
| Campaign 8 / Mammal Wave 2 | 2026-11-18 | Recalibrated mammal queue, 7 niches | **GOLD** — Blue Spring manatee scar sheets, ~200 individuals, frozen 2013; SILVER guard-hair atlases + EBRWS ([shortlist](campaigns/SHORTLIST-CAMPAIGN8-MAMMAL2-2026-11-18.md), [spin-off](spinoffs/manatee-scar-sheets/)) |

Campaign scripts, verify passes and output JSONs are in `campaigns/`
and `campaigns/outputs/`; the two niche registries are
`campaigns/NICHES-50.md` and `campaigns/MAMMAL-NICHES-50.md`;
score calibration is `campaigns/CALIBRATION-2026-11-18.md`; excluded
verification samples are listed, with sizes and md5s, in
`campaigns/SAMPLES-MANIFEST.md`.

**The methodology is domain-general (v2).** Every field has the same
shape: a repository holds the official deposit (a paper's data, a
survey's release), while the project/lab/author site accumulates the
derived, older, or extra files — segmentations, catalogues, corpora,
spectra, scans — unindexed and unarchived, and article pages quietly
swap out their original images and links over the years. v2 therefore
ships **domain packs** (neuro, genomics, ecology, astro, geo,
linguistics, heritage, media — each with its own gold words and
signature file types), archive adapters beyond Zenodo (any archive
landing page — Figshare/OSF/Dryad/journal supplements — plus GitHub
release assets), a generic placeholder validator for any file type,
and an `articles` mode that diffs a page's images/data links against
its Wayback snapshots to surface what vanished.

Cross-domain proof (2026-11-16): crawling the IllustrisTNG
astrophysics site (tng-project.org) inventoried **946 data files** —
the FITS cluster catalogue top-scored by the astro pack, hundreds of
HDF5 spectra beneath it. Articles mode on NASA's APOD page recovered
image files from its 2006 and 2019 versions that the live page no
longer carries.

## The pattern it hunts

1. **Archive ≠ website.** A repository record (Zenodo/OSF/Dryad) holds
   the raw deposit; the lab/project site holds the derived gold —
   segmentations, atlases, labels, tables — unindexed and unarchived.
2. **The gold hides in scripts, not links.** On Brain Catalogue the
   filenames live inside an embedded JSON blob in a `<script>` tag
   (`var info = JSON.parse('{... "url":"/data/Lion/", "atlas":[...] }')`),
   invisible to a normal link crawler. The hunter scans raw page text
   for data-file tokens and resolves them against embedded base URLs.
3. **Old versions hold deleted files.** Wayback Machine captures keep
   files and article/image versions the live site no longer links.

## Design doctrine — analysis-first (standing instruction, 2026-11-16)

The hunter is not a file collector. It exists to feed comparative
analyses like the brain project it was born in — recover a stranded
derived dataset, audit it, and run one clean comparison across many
comparable units, graded against the field's published benchmark.
Every design decision must serve that end:

1. **The unit of value is a comparable set, not a file.** A find
   matters as a member of a comparison class — the same derived data
   type across species, simulation runs, sites, or timepoints. Always
   group finds into sets and report *completeness per set* (real /
   empty-placeholder / absent across the units), the way
   `set_report.py` does. "Hippocampus labels × 37 species: 13 real,
   17 empty, 7 absent" is an analysis-ready statement; a file list
   is not.
2. **Classify every find by provenance, and never blur the classes.**
   *Stranded* (on the project site, absent from the formal archive)
   is the gold class. *Deleted* (only in Wayback/old versions) is
   the second. *Published by design* (a curated release a site lists
   openly — e.g. IllustrisTNG's data files) is inventory: useful,
   sometimes the raw material for a cross-suite comparison nobody
   has run, but never reported as a recovery.
3. **The deliverable is an audited, analysis-ready bundle.** Empty
   placeholders are flagged, never silently dropped; members from
   different pipelines are declared, never pooled undeclared (the
   Scalable Brain Atlas rule). A set is done when an analyst can run
   the comparison from the bundle alone and state exactly what each
   number rests on.
4. **Judge hauls by the analysis they enable.** A smaller stranded
   set that completes a comparison outranks a thousand inventoried
   files that answer no question. When a sweep finds only inventory,
   say so plainly — the next move is choosing the comparison nobody
   has run, not collecting more files.

## Design doctrine — high-fidelity scans (standing instruction, 2026-11-17)

Added at Atharva's direction: *"high fidelity scans, that's our most
premium resource, and we capitalize on that"* — and *"integrate this
particular approach in the gold mine hunter."* The MRI / Brain
Catalogue win was not a file-recovery accident. It was a fidelity
arbitrage, and it generalises:

**Why MRI paid:** the raw scan preserved more information than any
paper extracted from it, the same scanner protocol ran across many
comparable units (37 species), the derived labels were incomplete /
stranded / on a different ruler (histology ran ~1.6× the MRI line —
Two Rulers), and a local benchmark existed to grade a new measurement
against.

**The fidelity test — a system is fertile only if all four hold:**

1. **Raw capture kept, not just the summary.** The deposit holds the
   high-resolution artefact itself (volume, mesh, spectrum, light
   curve, density map, point cloud), not only the table the paper
   published. If only summaries survive, there is nothing to
   re-derive — kill it.
2. **One instrument / protocol, many comparable units.** Same scanner,
   survey, simulation code family, or chemistry across species /
   galaxies / stars / specimens / sites / cells. The comparable set
   *is* the asset; a single exquisite scan with no siblings is a
   portrait, not a pattern.
3. **Labels incomplete, stranded, or on a second ruler.** Segmentations
   missing or empty-placeholder, catalogues threshold-cut, cell-type /
   metallicity / model labels assigned by a different pipeline than
   the ground truth. The gap between scan and label is where the
   finding lives.
4. **A local ground truth to grade against.** APOGEE for Gaia and for
   cosmology sims, histology for MRI, landmarks / dissection for CT,
   AlphaFold vs experimental maps (and vice versa), reanalysis for
   climate models. Without an anchor, a cross-scan gap is
   uninterpretable — declare it scouted, not landed.

**Hunter behaviour under this doctrine:**

- Score *fidelity* before volume: file types and names signalling raw
  capture (`.nii/.nii.gz`, `.ply/.stl` meshes + `.las/.laz` point
  clouds, `.fits` spectra/cubes, EMDB maps, Gaia-style catalogues with
  per-source spectra) outrank derived tables. See `FIDELITY_PACKS`
  and `fidelity_score()` in `goldmine_hunter.py`, and the `fidelity`
  subcommand.
- For every candidate system, fill the four-line card *before*
  counting files: `RAW: / UNIT: / LABEL GAP: / ANCHOR:` — a system
  missing any line does not enter a campaign, however large its pile.
- Never pool scans from different instruments/pipelines undeclared —
  the Scalable Brain Atlas rule, generalised: TNG ≠ SIMBA apertures,
  Gaia XP ≠ APOGEE, histology ≠ MRI. Declare the ruler per member.
- The deliverable is a *re-derivation-ready bundle*: raw scans +
  completeness per comparable unit (real / placeholder / absent) +
  the anchor set, so the comparison can be run from the bundle alone.

## Design doctrine — niche keywords (standing instruction, 2026-11-18)

Added at Atharva's direction: *"come up with ~50 different domain
keywords … niche, not touched as much, but with the potential —
especially headlines, like mammals: intuitive to anyone, yet full of
hunter-level scope. Work on the tooling, not the research itself."*

The registry — `NICHES-50.md` + machine-readable `niches.json`,
loaded by the hunter as `NICHE_PACKS` with a `niches` subcommand and
per-niche `niche_score()` — is **the campaign-generation queue:
campaigns are now GENERATED from the top of this registry, not
hand-picked.** Hand-picking is what produced Campaigns 4–5's lesson:
the obvious old-site vein now runs to kept vintages and
published-by-design stacks, because mature fields make
reconciliation their central product. The registry exists to aim
the hunter only where that has *not* happened.

**Every niche in the registry passed three selection tests on
paper before it was scored:**

1. **Fidelity test** (the 2026-11-17 doctrine, applied per niche):
   raw capture kept, not just summaries; one instrument/protocol
   over dozens+ comparable units; labels incomplete, stranded, or
   on a second ruler; a local anchor to grade against. Each entry
   carries its filled four-line card (RAW / UNIT / LABEL GAP /
   ANCHOR) — a niche missing a line does not enter the registry,
   however evocative it sounds.
2. **Headline test:** the comparison the niche would yield must be
   sayable in one sentence a non-specialist instantly gets — the
   mammals shape ("a newborn's X is bigger than an adult Y's").
   Each entry carries its headline-shape sentence. A niche whose
   payoff needs a paragraph of setup is a paper, not a headline,
   and scores down.
3. **Fragmentation test:** the field must NOT be mature-and-
   consolidated — if reconciliation is already the field's central
   product, its data publishes by design and there is no gold
   (CRU, Reptile Database, ATNF psrcat — Campaign 5). Fertile
   niches are fragmented corners: regional collections, single-lab
   piles, society and personal sites, pre-digital archives whose
   keepers never joined a central product.

Scoring (0–10 per niche) weighs the three tests together; the
ranked order in `niches.json` is the firing order. Already hunted,
landed or killed ground (Campaigns 1–5, the fidelity campaign) is
excluded; adjacent-but-distinct niches must say why they are
genuinely separate. A probe hit from the registry is a *seed*, not
a find — gold is still only what a campaign verifies by sample
download, per the analysis-first doctrine.

## Design doctrine — mammal-grain niches (2026-11-18, Atharva's correction)

Atharva's correction to the broad registry above: he meant niche
domains **at the grain of "paws and fingerprint analysis of
mammals and all that"** — the broad 50 spanned whole fields and
was the wrong grain. **The grain rule: one intuitive animal world;
a niche is ONE body part, trace, print or pattern system in it.**

The mammal registry — `MAMMAL-NICHES-50.md` + `mammal_niches.json`,
loaded as `MAMMAL_NICHE_PACKS` with a `mammal-niches` subcommand and
`mammal_niche_score()` — holds exactly 50 such systems: primate and
koala fingerprints, dog nose prints, cattle muzzle-print
registration, paw-track morphometrics (FIT) and plaster cast
collections, whale flukes, dolphin fins, elephant ears, whisker-spot
maps, coat patterns, tooth-wear and cementum archives, guard-hair
scale-cast atlases, and their kin. **This registry now sits AHEAD
of the broad registry in the campaign queue**: when the two
disagree on where to hunt next, the mammal queue fires first.

Why the grain pays — the shared pattern of all 50: (a) a raw
capture (print, cast, photo, scan, hair cast) taken the same way
across many individuals/species; (b) used for individual ID or
age/sex/species reading, so labels exist but live in old
catalogues, forensic atlases, photo-ID archives and museum cast
collections — often on a second ruler (DNA, tags, dissection,
known-age animals); (c) instantly headline-shaped. The canonical
headline is the koala's fingerprint, and it is carried in its
*verified* form (Henneberg, Lambert & Leigh 1997: ~20 koalas, ink
prints + SEM, ridges nearly identical to human; the authors called
a crime-scene mix-up "extremely unlikely" and none is documented).

The same three selection tests (fidelity / headline /
fragmentation) gate entry, and the same honesty rule applies: a
probe hit is a seed, not gold. Excluded as already landed: mammal
brains and the rhino forearm centroid work — rhino ear-notch/horn
ID is a genuinely different system and is in the registry on its
own merits.

```
python3 goldmine_hunter.py mammal-niches            # all 50, ranked
python3 goldmine_hunter.py mammal-niches --top 6    # head of queue
python3 goldmine_hunter.py mammal-niches --niche koala-fingerprints
```

**Seeded fidelity systems (v1, 2026-11-17 — `seeds_fidelity.json`):**
morpho-CT (MorphoSource/DigiMorph), cosmology sims (TNG/EAGLE/SIMBA
× APOGEE/GALAH), Gaia × APOGEE, connectome MRI (Digital Brain Bank /
HCP / MICrONS), cryo-EM (EMDB × AlphaFold DB), Earth lidar + CORONA
× Sentinel-2, climate ERA5 × CMIP6, single-cell atlases (HCA/Tabula),
Kepler/TESS light curves. Ranking and first campaign:
`FIDELITY_CAMPAIGN_2026-11-17.md`.

## Use

```
python3 goldmine_hunter.py audit --zenodo 44855 --site https://braincatalogue.org/Lion --deep
python3 goldmine_hunter.py audit --archive-page <figshare/osf/dryad URL> --site <project site> --deep
python3 goldmine_hunter.py audit --github owner/repo --site <project site>
python3 goldmine_hunter.py crawl  --site https://braincatalogue.org --depth 2
python3 goldmine_hunter.py wayback --domain braincatalogue.org
python3 goldmine_hunter.py articles --url <article page>   # images/data that vanished from old versions
python3 goldmine_hunter.py sweep  --seeds seeds.json
python3 goldmine_hunter.py niches            # all 50 niches, ranked by score
python3 goldmine_hunter.py niches --top 8    # the next campaign's head of queue
python3 goldmine_hunter.py niches --niche frog-call-archives   # one niche's full card
python3 set_report.py outputs/species-sweep-<ts>.json --audit outputs/audit-<id>-<ts>.json
```

- `set_report.py` turns a sweep into comparison sets: per file type,
  real / empty-placeholder / absent across all units, with provenance
  class — the analysis-ready view the doctrine above requires.

- `audit` diffs the archive file list against the site's files,
  HEAD-verifies each candidate, scores it (derived-data names +
  absence from archive rank highest), and with `--deep` parses each
  NIfTI header and flags empty placeholders (correct grid, zero data —
  ~half the Brain Catalogue hippocampus files were exactly that).
- Reports land in `outputs/` as JSON.

## Verified results (2026-11-16)

- **Fonoteca Zoológica (Campaign 6 / Wave 1, 2026-11-18) — GOLD,
  stranded:** 1,013 status-200 audio files on fonozoo.com in five
  sub-piles (751 mp3 in `/sonidos/`, 593 of them species-named), the
  collection's own site only, in no formal archive; sample-verified
  from Wayback (real MP3/WAV, md5s in
  `SHORTLIST-CAMPAIGN6-WAVE1-2026-11-18.md`). The registry-generated
  campaign's first gold — frog-call-archives was its #1 seed. Un-run
  comparison: re-identify the accessioned calls against today's
  DNA-split anuran taxonomy and count how many change species.
- **Manatee scar sheets (Campaign 8 / Mammal Wave 2, 2026-11-18) —
  GOLD, stranded:** the complete frozen April-2013 edition of Wayne
  Hartley's hand-drawn Blue Spring scar catalogue (~200 individuals,
  22 pp., verified PDF, md5 in
  `SHORTLIST-CAMPAIGN8-MAMMAL2-2026-11-18.md`), stranded on Save the
  Manatee Club's old-site subdomains and never ingested by MIPS (the
  formal system is photographic; the sketches are a medium it does
  not ingest). Comparison pre-registered in
  `~/workspace/manatee-scar-sheets/`: join the 2013 sheets to
  post-2013 records and test the sheet's own 3–5-year drop rules as
  predictions of re-identifiability.
- **Lion audit re-found the gold cold:** Hippocampus.nii.gz (42,043 B,
  dims 276×334×209 = the MRI's grid) and Telencephalon.nii.gz
  (272,280 B), both website-only; Zenodo 44855 holds only MRI-n4.nii.gz.
- **Wayback sweep of braincatalogue.org:** 90 archived data files,
  including a label type the manual pass missed — Ferret `Neocortex.nii.gz`.
- **brainmuseum.org:** 156 images, 0 data files (photos/histology only —
  consistent with the manual survey).
- **digimorph.org:** Wayback noise mostly; its CT data sits behind
  specimen-page viewers and needs a dedicated adapter (noted, not faked).

## Follow-on runs (2026-11-16, later)

- **Full 37-species sweep** (`species_sweep.py`): every Brain Catalogue
  species page crawled and diffed against the local holdings in
  `brain-scan-comparison/data/brain_catalogue_full/` — site and local
  match for all 37; zero unheld files. Label census: **53 real,
  18 empty placeholders** of 71 label files deep-checked. Bug found
  en route: the Galago page unicode-escapes its data path
  (`Demidoff\u0027s_dwarf_Galago`) — hunter now decodes `\uXXXX`
  escapes in embedded JSON before resolving.
- **Scalable Brain Atlas** (scalablebrainatlas.incf.org): 61 unique
  data files / **44 NIfTI atlases** in the first 30 pages — macaque
  CIVM rhesus labels + DWI, F99 parcellations, mouse P56 Allen
  annotation, Waxholm labels, Badhwar hippocampal atlas
  (`outputs/sba-inventory.json`). A candidate primate-label source,
  different pipeline — never pool with catalogue numbers undeclared.
- **BrainMaps** (brainmaps.org): dead end — parked domain.

## Where to point it next

Old lab/project sites paired with a partial repository deposit:
university atlas pages, NITRC project pages, MorphoSource project
pages, journal supplementary-material pages hosted on author sites,
and news/article pages whose early Wayback versions embedded
higher-resolution figures or dataset links than the live page.

## Published output

The morpho-CT campaign's rhino computation — the dataset this tool
located (Mallet et al. 2019's Supplemental Information 9 landmarks,
obtained barrier-free via Europe PMC) — is published as a manuscript
in its own right: **[The Forearm Splits the
Rhinos](https://github.com/atharva-chourey-lab/rhino-forearm)**, a
within-specimen centroid-size profile analysis separating all five
living rhinoceros species. The computation itself lives here, under
`gold/morpho-ct/epmc-rhino5/`.

## Data — not redistributed

The datasets the campaigns downloaded are **not** in this repository:
they belong to their source projects. Verification sample files are
excluded and listed, with size and md5, in
`campaigns/SAMPLES-MANIFEST.md`, so every verification claim remains
reproducible from the source. Only the lab's own scripts, registries,
result summaries, tables and verification notes are published.

## Authorship and licence

**Author:** Atharva Chourey, Atharva Chourey Lab (independent
research lab). Code in this repository is released under the **MIT
License** (see `LICENSE`). The associated manuscripts are published
separately under CC BY 4.0 — the code licence and the paper licence
are deliberately different.
