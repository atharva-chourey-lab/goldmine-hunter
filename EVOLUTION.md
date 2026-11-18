# Evolution — the tool, the campaigns, and the pain points

**Atharva Chourey Lab.** This document couples the Goldmine Hunter
campaign record (`campaigns/`) to the tooling paradigm that produced
it: how the tool changed, what each campaign actually found, and the
pain points — stated plainly, with the one-line law each one produced.
Nothing here is inflated: grades were fixed in writing before the
campaigns they grade (`campaigns/GRADES.md`), and every shortlist
leads with its honest headline, including the zeroes.

## The tooling paradigm

The hunter exists because of one find: Zenodo held only a lion's raw
MRI, while the Brain Catalogue project site quietly hosted the
hand-drawn hippocampus and telencephalon segmentations for a decade.
The paradigm generalises that shape into a loop:

1. **Hunt** — crawl the project/lab/author site, not the archive.
   Repositories hold the official deposit; the derived, older or
   extra files accumulate on the site, unindexed and unarchived, and
   old versions hold what was deleted.
2. **Verify** — Wayback inventories filtered to statuscode:200
   *before* counting, and a sample download (size + md5 + format
   check) for every pile before it is called a find.
3. **Classify** — provenance classes are never blurred: STRANDED
   (on the site, absent from the formal archive) is the gold class;
   DELETED (Wayback-only) is second; PUBLISHED-BY-DESIGN is
   inventory, useful but never reported as a recovery.
4. **Grade** — against criteria fixed before digging
   (`campaigns/GRADES.md`): GOLD = verified stranded/deleted
   comparable set + an identifiable un-run comparison + a local
   anchor; DIAMOND = gold plus a headline-class overturn visible in
   the set itself; SILVER = verified material on published data.
5. **Mint** — a surviving set is not the result; the comparison it
   enables is. Minted sets spin off into pre-registered projects
   (`spinoffs/`).
6. **Calibrate** — after each wave, registry scores are compared
   against outcomes and cut where they lied (`campaigns/
   CALIBRATION-2026-11-18.md`). The tool is expected to be wrong in
   recorded ways, and the record is part of the publication.

Two doctrines govern what the hunter is pointed at. The
**analysis-first doctrine** (2026-11-16): the unit of value is a
comparable set, not a file; the deliverable is an audited,
analysis-ready bundle. The **high-fidelity doctrine** (2026-11-17):
a system is fertile only if the raw capture was kept, one
instrument/protocol ran across many comparable units, the labels are
incomplete, stranded, or on a second ruler, and a local ground truth
exists to grade against — the four-line fidelity card
(RAW / UNIT / LABEL GAP / ANCHOR) must be filled before any file is
counted.

## The evolution, in order

- **v1, neuro-only (2026-11-16).** Built to re-find the Brain
  Catalogue pattern: audit a Zenodo record against its project site,
  flag empty-placeholder labels. It re-found the lion labels cold.
- **v2, cross-domain (2026-11-16).** Domain packs (neuro, genomics,
  ecology, astro, geo, linguistics, heritage, media), archive
  adapters beyond Zenodo, a generic placeholder validator, and an
  `articles` mode that diffs a page against its Wayback snapshots.
- **Campaigns 2+3 (2026-11-17) — the first deleted gold.**
  Science-first sweep of 16 sites. The find was Maddison's own
  2006–2010 GDP/population vintages: 18 status-200 files surviving
  only in Wayback, sample-verified as real, differing Excel files —
  a complete vintage set for a self-revision analysis (later minted:
  Maddison revised the recent and the national, never the ancient).
- **Fidelity campaign (2026-11-17).** The fidelity doctrine run as a
  campaign across nine seeded systems: rhino-5 landed (a
  centroid-profile separates all five living rhinos), Gaia×GALAH
  produced a measured +1.85 dex slope at the metal-poor end, the
  cryo-EM population was measured; a parallel cosmology×chemistry
  leg produced a comparison, not a recovery.
- **Campaigns 4+5 (2026-11-17/18) — zero gold, twice.** Hand-picked
  old lab/project sites, 15 + 17 hosts. Campaign 4: no stranded set;
  one small deleted set (HCA 2019–20 portal matrices). Campaign 5:
  no stranded set; one small deleted set (SCOP release files) and
  four live vintage stacks. The lesson that reshaped the programme:
  labs now *keep* their old versions instead of stranding them.
- **CRU spin-off (2026-11-18) — SILVER, minted.** Campaign 5's CRU
  stack was published-by-design, but the un-run comparison across it
  was real: a pre-registered (6/8) revision-geometry accounting of
  CRUTEM 3→4→5 — CRU revised the ancient, not the recent (68% of
  revision mass in 1850–1900; endpoint warming 1.09→1.32 °C, mostly
  a baseline effect). See `spinoffs/cru-vintages/`.
- **The niche registry (2026-11-18) — and the grain correction.**
  Atharva's direction: stop working the research, work the tooling —
  generate 50 niche keyword domains with fidelity cards and
  mammals-style headline shapes, and generate campaigns from the
  registry instead of hand-picking. The first registry was built at
  field grain (fish otoliths, frog calls, river gauges…). Atharva
  corrected the grain: a niche is one body/trace system inside one
  intuitive animal world — "paws and fingerprint analysis of
  mammals". The mammal-grain registry (50 niches: primate
  fingerprints, cattle muzzle prints, paw tracks, whale flukes,
  whisker spots, guard-hair casts…) was built the same day and sits
  ahead of the broad registry in the queue.
- **Grades fixed (2026-11-18).** `campaigns/GRADES.md` committed
  before Campaign 6 dug anything, so gold could not be redefined to
  fit a haul.
- **Campaign 6 / Wave 1 (2026-11-18) — registry GOLD.** The broad
  registry's #1 seed, frog-call archives, produced the Fonoteca
  Zoológica pile: 1,013 status-200 audio files stranded on
  fonozoo.com, in no formal archive, sample-verified. Plus one
  SILVER (Barts dissection registers). Registry-generated beat
  hand-picked on its first wave — Campaigns 4+5 had produced zero
  gold between them. Minted the same day: 146 of 629 species-named
  recordings (23.2%) are filed under names that no longer stand
  (`spinoffs/fonozoo-reidentification/`).
- **Campaign 7 / Mammal Wave 1 (2026-11-18) — zero gold.** Two
  SILVER (Juneau fluke edition stack; Wellcome's Galton fingerprint
  digitisation, 3,022 IIIF canvases) and the wave's biggest result,
  a custody finding: the Wagyu registry's 3M+ ink muzzle prints,
  kept since 1948 with a join key (animal ID + DNA) already
  existing, have zero digital surface anywhere. All seven 9/10
  mammal scores were cut.
- **Campaign 8 / Mammal Wave 2 (2026-11-18) — mammal GOLD.** From
  the recalibrated queue's last seed: Wayne Hartley's hand-drawn
  Blue Spring manatee scar-sheet catalogue (~200 individuals,
  frozen April 2013), stranded on a charity's archive subdomain and
  absent from the formal MIPS system — GOLD, with a comparison
  pre-registered (the first persistence audit of a sketch-based ID
  catalogue; `spinoffs/manatee-scar-sheets/`). One SILVER stack
  (guard-hair forensic atlases), one small SILVER (EBRWS right-whale
  catalogue editions).

## Pain points — and the law each one produced

- **Raw Wayback counts overstate by 10–100×.** WorldClim v1 went
  727 counted files → 1 status-200 capture → 0 real data (the
  "zip" was a 38,691-byte HTML error page — a phantom that had been
  carried as a haul). *Law: filter to statuscode:200 before
  counting, and sample-download before calling anything a find.*
- **Phantom files everywhere.** HTML app pages wearing data
  extensions (Human Protein Atlas, CATH), viewer URLs that are not
  files (Rosetta `/stream/`), HTML captures inside audio piles
  (Fonozoo, two excluded). *Law: magic bytes and md5, or it didn't
  happen.*
- **Crawler limits masquerade as absences.** CRU's version stack
  was invisible to the depth-1 crawler (0 live files) while being
  fully live to direct HEADs; fonozoo's live site 403-stubs file
  requests from our client while Wayback holds origin 200s as
  recent as 2026-01. *Law: a crawl result is a statement about the
  crawl, not the site — verify by direct request before killing.*
- **Databases behind interfaces are not file piles.** AFORO's
  9,821 otolith images and Otolitos UNAM sit behind JSP/PHP query
  interfaces with zero downloadable files; HyperL
...[truncated 3396 chars]