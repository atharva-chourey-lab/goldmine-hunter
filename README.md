# Goldmine Hunter

**A tool for finding datasets stranded on project websites that never made it
into the formal archive — the pattern behind the lab's Brain Catalogue find:
Zenodo held only a lion's raw MRI, while the project site quietly hosted the
hand-drawn hippocampus and telencephalon segmentations for a decade.**

## The doctrine

Every field has the same shape: a repository holds the official deposit (a
paper's data, a survey's release), while the project/lab/author site
accumulates the derived, older, or extra files — segmentations, catalogues,
supplementary tables — that were never deposited. Goldmine Hunter crawls the
project site, not the archive: it scans raw page text and embedded JSON for
data-file tokens, resolves them against embedded base URLs, HEAD-verifies
candidates, and ranks what it finds for human fidelity checks.

The methodology is domain-general (v2). This repository contains the hunter as
run across neuroscience, Gaia/GALAH stellar chemistry, cryo-EM, cosmological
simulations and morphology/CT.

## What is here

- `goldmine_hunter.py` — the hunter itself (crawl, token scan, resolution,
  verification).
- `campaign*.py`, `doctrine_run.py`, `gather_gold.py`, `set_report.py`,
  `species_sweep.py` — campaign drivers and reporting.
- `verify2.py`, `worldclim_verify.py` — independent verification passes.
- `seeds.json`, `seeds_fidelity.json` — the seed target lists the campaigns ran
  from.
- `gold/` — per-domain worked examples: the small analysis scripts and
  verification notes from each campaign (e.g. `gold/gaia-chemistry/`,
  `gold/cryoem/`, `gold/cosmology-chemistry/`, `gold/morpho-ct/`).
- Campaign and fidelity reports at the top level
  (`FIDELITY_CAMPAIGN_2026-11-17.md`, `fidelity-*.md`).

## How to run

```bash
python3 goldmine_hunter.py --help
```

Python 3 with requests (see imports); no API keys are required or used — the
hunter reads public web pages only.

## Data — not redistributed

The datasets the campaigns downloaded (~800 MB of atlases, simulation
snapshots, survey files) are **not** in this repository: they belong to their
source projects. Only the lab's own scripts, seed lists, result summaries and
verification notes are published.

## Status

Working tool, run in production campaigns by the lab. It is a research
instrument, not a polished crawler framework: campaign drivers encode the
specific hunts they ran.

## Authorship and licence

**Author:** Atharva Chourey, Atharva Chourey Lab (independent research lab)

The Atharva Chourey Lab is a human–AI collaboration: Atharva Chourey works with
Lapis (Muse), an AI research partner. All results are framed as the
collaboration's.

Code in this repository is released under the **MIT License** (see `LICENSE`).
The associated manuscripts are published separately under CC BY 4.0 — the code
licence and the paper licence are deliberately different.
