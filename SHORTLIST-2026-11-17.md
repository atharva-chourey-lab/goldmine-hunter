# Goldmine Hunter — science-first shortlist (2026-11-17)

Campaigns 2+3: 16 new sites crawled + Wayback-inventoried, then every
promising pile re-audited with **statuscode:200-only counts + sample
downloads**. Raw Wayback counts overstate by 10–100×; nothing below
rests on a raw count.

## The find — historical statistics

**Maddison's own vintages, 2006–2010 (DELETED, Wayback-only, verified).**
18 status-200 files under `ggdc.net/maddison/Historical_Statistics/`:
horizontal + vertical files at vintages 2006, 10-2006, 03-2007, 09-2008,
03-2009, 02-2010, plus Background docs and Revised Population Estimates.
Three downloaded and verified as real Excel (OLE2), all different sizes
/ hashes (2006 horizontal: 1,607,680 B; 02-2010: 1,789,952 B) —
`gold/maddison-vintages/`.
*The set:* the same GDP/population series (country × year 1–2008 AD),
re-issued by Maddison himself five+ times before the Maddison Project
Database replaced him. *The analysis nobody has run:* the geometry of
his self-revisions — which countries/centuries moved, how far, which
way — then chained to the Project's 2013→2023 re-revisions. This is the
Revisions/Vintages pattern with a clean, small, complete vintage set.

**HMD v6 partial vintage (DELETED, verified counts).** 150 status-200
files across 50 country codes under `mortality.org/.../hmd.v6/` — but
only 2–8 files per country of a ~77-file set. Current HMD is
free-with-login, so this is a vintage-only, incomplete panel. Second.

## Science — what survived

**SBA primate atlases (STRANDED, in hand, re-verified today).**
Macaque CIVM labels + b0 (400×530×340, ~22M nonzero bytes) and the
Badhwar hippocampal atlas — real NIfTI, on the project site, in no
formal archive. Analysis: a declared cross-pipeline primate comparison
next to the Brain Catalogue set (never pooled undeclared).

Everything else science was inventory or dead:
- PHOIBLE, IDS, TimeTree 6, PaleoDB, exoplanet catalogue, Gapminder —
  published-by-design (GitHub / CLLD / API). The stranded pattern is
  dying on modern portals; it lives on old project/personal pages
  (the one small live example: binary-planet lists on Paris
  Observatory *perso* pages, linked from exoplanet.eu).
- FishBase, TRY — data behind forms/APIs; needs a dedicated adapter,
  same class as DigiMorph. Not faked.

## Kills (verified, with corrections to yesterday's record)

- **WorldClim v1: NOT recoverable via Wayback.** 1,122 collapsed
  captures under `/data/*` → exactly 1 status-200 zip → it downloads
  as HTML. Yesterday's `gold/worldclim-v1/tmean_30_tif.zip` is a
  38,691-byte HTML error page, not a zip — the earlier haul was a
  phantom. The 727-file pile was non-200 captures.
- **SILSO sunspot v1: not found.** Live datafiles serve only V2.0;
  V1 filenames 404 live and have zero CDX captures under every
  sidc.be / sidc.oma.be datafiles pattern tried.
- **SDSS deleted VAC:** the one named catalogue (apogee-rc-DR12) was
  already known unrecoverable (its captures are 404 pages); the rest
  of SDSS is still-live inventory.
- COW old versions (Alliance v3.03, MID v3.10) are real status-200
  Wayback files, and Polity's /inscr holds old .sav/.xls live — both
  deprioritised per the science-first instruction.

## Method upgrade (standing)

Filter every Wayback inventory to statuscode:200 *before* counting
sets, and sample-download one member of any set before calling it a
find. WorldClim went 727 → 1 → 0 under that rule; Maddison went
877 raw → 18 real — and the 18 are the gold.
