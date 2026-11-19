# Goldmine Hunter — Campaign 14 shortlist: Mammal Wave 6, the registry tail (2026-11-18)

The **mammal-grain registry's** sixth and final campaign, generated
from the recalibrated queue: ranks 42–50, in registry order —
hair-medulla-cross-sections (7), sheep-goat-nose-prints,
cat-nose-leather-patterns, hoof-cloven-track-systems,
claw-mark-archives, bite-mark-records, vibrissae-follicle-maps,
tail-pattern-systems, lab-animal-marking-records (all 6). **This
campaign exhausts the mammal registry — all 50 niches have now
fired.** Grades are `GRADES.md`'s, unchanged. Method = Campaigns
7–8/12 exactly: live crawl + Wayback inventory filtered to
statuscode:200 before counting (`campaign14_mammal6.py`,
`outputs/campaign14-20261118-214039.json`), then targeted verify
(`verify14.py`, `outputs/verify14-20261118-214344.json`; samples
in `gold/campaign14-verify/`, 16 MB total new disk). Custody
classes are Custody Mapper classes assigned **post-probe**, from
probe evidence. Paper/custody systems (Indiana 4-H nose-print
cards, forensic reference casts, colony marking logs) were
documented, never circumvented.

**Headline, plainly: NO GOLD, NO DIAMOND, NO SILVER.** Three
INVENTORY and six KILL results. The 6-band (plus the last 7)
behaves exactly as the calibration law predicts, one step below
the 7-band: the material is real in most niches, but it lives in
journal PDFs, published guides and atlases, paper templates and
cards, or inside other catalogues — never as a loose working pile
on an old website, and in two niches (claw marks, tail patterns)
the card's own comparison was already run or the archive never
existed standalone. The wave's product is its custody/premise
map, stated as such. With no GOLD set there is no novelty scrub
and no pre-registration to write.

## Verdict table

| Niche (score) | Hosts probed | Verified files | Custody (post-probe) | Grade | One-line evidence |
|---|---|---|---|---|---|
| hair-medulla-cross-sections (7) | hairatlas.hu (+Wayback), zsi.gov.in, zenodo.org | 10 unique status-200 PDFs on hairatlas.hu (6 sample spreads + checklist/index/literature/museum-codes); 4 samples REAL (see below) | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | Tóth 2017's web surface is a deliberate *sample* of a 307-pp commercial book, not the atlas; the medulla tables otherwise live in journal PDFs (ZSI, BHL). |
| sheep-goat-nose-prints (6) | slideshare.net (JOE mirror), mdpi.com | 0 data files; JOE text check positive | PAPER_ONLY → KILL | **KILL** | The one systematic series — Indiana 4-H, 491 beef + 220 sheep — is ink prints on index cards held by county committees; modern work is face photos (Roboflow/Kaggle), not nose prints. |
| cat-nose-leather-patterns (6) | knau-bulletin.com, cfa.org | 0 data files; KNAU text checks positive (n=157, stamp pad) | PAPER_ONLY → KILL | **KILL** | The entire rigorous base is one 2025 paper: 157 cats printed with a Trodat stamp pad on paper, 14 re-printed; no print file, dataset or registry exists anywhere probed. |
| hoof-cloven-track-systems (6) | pubs.nmsu.edu, api.pageplace.de | NMSU guide REAL (below); field-guide preview is a commercial preview | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | Hoof measurement survives as published guides (NMSU Circular 561: deer 2⅜–3¼ in, elk 4–4¾ in); the forensic labs' reference cast/photo sets the card imagines surfaced on no host. |
| claw-mark-archives (6) | mdpi-res.com, conservancy.umn.edu | MDPI application paper REAL (below) | PAPER_ONLY → KILL | **KILL** | Records are paper templates pressed over marks; and the un-run comparison **was run** — Steinmetz & Garshelis 2008: captive known bears (n=43, 121 imprints), 95% classified, wild tests 91%/100%; thesis formally archived at UMN. |
| bite-mark-records (6) | scavengers.cat, pmc.ncbi.nlm.nih.gov | FSI taphonomy paper REAL (below) | PHYSICAL_OBJECTS / lab custody → KILL | **KILL** | Tooth-pit data lives as tables inside taphonomy papers and on lab-held bones; no reference bite archive — fossil or forensic — has a file surface. |
| vibrissae-follicle-maps (6) | e-space.mmu.ac.uk, pubmed.ncbi.nlm.nih.gov | 0 (MMU PDF unreachable from this client; search-indexed full text only, stated) | CUSTODY_RESTRICTED (lab/museum specimens) → KILL | **KILL** | Follicle maps are figures inside neuroscience papers; the arrangement is species-stereotyped (5 rows A–E + straddlers), not individual — the niche's ID premise fails, and the diceCT pads are museum/lab specimens. |
| tail-pattern-systems (6) | ielc.libguides.com, nre.tas.gov.au | 0 (Tasmanian PDF unreachable from this client; search-indexed text only, stated) | No standalone custody — field inside other catalogues → KILL | **KILL** | No tail-first archive exists: tail rings/notches are a column in cheetah/dolphin/lemur host catalogues (already hunted in C7/C12); the public surface is species fact sheets (lemur: 13–14 black / 12–13 white rings — a species trait, not an individual key). |
| lab-animal-marking-records (6) | informatics.jax.org, archive.org, ojs.utlib.ee | USDA 1949 manual REAL head sample (below); JAX chapter HTML 200 | FORMAL_OR_PLATFORM → CAUTION (charts) / CUSTODY_RESTRICTED → KILL (logs) | **INVENTORY** | The punch/toe-clip *charts* are published methods figures (JAX Green Book: one code to 12,999; USDA 1949 Fig. 3; rival charts never standardised); the colony *logs* themselves are institutional archives with no file surface. |

## INVENTORY — verified real, published, no comparison completed

- **Hair medulla & cross-sections — hairatlas.hu sample pile +
  journal layer (PUBLISHED-BY-DESIGN).** Wayback status-200
  inventory of hairatlas.hu yields exactly **10 unique PDFs**:
  six sample spreads of Tóth (2017) *Hair and Fur Atlas of
  Central European Mammals* (123 species, 307 pp) plus the
  checklist, index, literature and museum-codes PDFs; the live
  site links only those samples. Two spreads sampled REAL:
  Cervidae & Bovidae (366,797 B, md5
  `ae85cf94a6b587d04b165d7af7fa7eda` — medulla + cross-section
  plates exactly as carded) and Soricomorpha (331,346 B, md5
  `f26160b28d560b5ddd1192352f538835`). The wider literature is
  journal PDFs: ZSI *Ratufa* trichotaxonomy REAL (826,447 B,
  md5 `3c6881dcd662aa22aa905db8ae1f81a6`) and De & Chakraborty
  hyena (medullary index 0.57, elliptical cross-section) REAL
  via Zenodo/BHL (2,977,512 B, md5
  `09d0f7cb51114e0738e6b90f8f9d5d56`). This is the guard-hair
  niche's second preparation arriving at the same ceiling one
  grade lower: the atlases publish samples and papers, never
  the working pile. Inventory.
- **Hoof & cloven tracks — the published guides
  (PUBLISHED-BY-DESIGN).** NMSU Circular 561 *Identifying and
  Preserving Wildlife Tracks* is REAL (2,380,760 B, md5
  `82ee64f0ebff7112fd6e1aafb4c3e82e`) and carries the niche's
  measurement layer in print (deer/elk/bighorn track lengths,
  cast-making protocol); the Stuart field guide's cloven-hoof
  section circulates as a publisher preview. Guides, not the
  forensic reference sets. Inventory.
- **Lab-animal marking charts (PUBLISHED-BY-DESIGN).** The
  JAX Green Book Ch. 3 (ear-punch code, ledgers, pedigree
  cards) is live HTML (200, ear-punch text verified) and the
  USDA 1949 manual's Fig. 3 toe-clip/ear-mark system is REAL
  as sampled (2,031,616 B head, md5-head
  `394049d4abfe368b3a70122ebce355e7`, truncated at cap —
  head sample only, stated). The 1988 Scandinavian review
  documents the rival-chart landscape (ear punch, toe clip,
  tail tattoo codes) — all published as methods literature.
  The charts are inventory; the logs are custody (below).

## KILLS & CUSTODY FINDINGS — probed, nothing claimable, evidence stated

- **Sheep & goat nose prints — KILL, paper custody (the cattle
  pattern at a tenth the scale).** The card's system was real:
  Indiana 4-H enrolled 491 beef and 220 sheep by nose print
  (ink on index card, county committees) plus retinal images;
  at re-check, sheep nose-print pairs matched visually 79.5%
  of the time (JOE 2006, text-verified this campaign). The
  cards were never digitised, and the modern sheep/goat ID
  literature has moved to face recognition on web/Kaggle
  photos — a different ruler entirely. No nose-print file
  exists to recover. Kill.
- **Cat nose leather — KILL, premise thin to a single paper.**
  Before 2025 the claim was folklore (1920s vet literature,
  per CFA's own summary); Tentieva & Arbaev (2025) supplied
  the first rigorous base — 157 cats, stamp-pad prints on
  paper, individuality/invariability/regeneration, 14 cats
  re-printed — as a journal article with no dataset, no
  registry, no clinic file surface. There is no archive to
  hunt because none was ever built. Kill.
- **Claw marks — KILL, paper templates + comparison already
  run (the C12 palm/sole shape).** Steinmetz & Garshelis
  (2008) built the discriminant on 121 imprints from 43 known
  (mainly captive) bears — the card's exact anchor — and
  classified 95% of captive and 91–100% of wild marks; the
  2022 NE-India application is REAL (1,511,530 B, md5
  `1128dafabbcbde822a4ce878ff6667af`) and already reports the
  method *failing* for sun bears where presence was unknown.
  Field records are paper templates punched over gouges.
  Nothing un-run, nothing filed. Kill.
- **Bite marks — KILL, lab-local bones and paper tables.**
  The taphonomy literature measures pits/punctures/scores
  case by case (FSI 2023 bear-attack foal REAL, 8,129,153 B,
  md5 `cf324f33b567f7a9431fcd4176074877`; the *Purussaurus*
  sloth tibia's 46 marks live in a paper + figshare
  supplement). Feeding-trial reference sets stay in the labs
  that made them; no cross-lab bite archive surfaced. Kill.
- **Vibrissae follicle maps — KILL, and distinct from C7's
  whisker-spot niche.** C7 hunted whisker *spot patterns* for
  individual ID (lions/pinnipeds); this niche is the follicle
  *anatomy* map. That map is stereotyped per species (rows
  A–E + α–δ straddlers across rodents; 7-row grids in harbour
  seals) — it keys species, not individuals, so the card's
  label gap has no individual-level signal to join. The
  primary material (diceCT mystacial pads, MMU/Manchester and
  Journal of Anatomy 2024) is museum/lab specimen work; the
  MMU methods PDF was unreachable from this client and is
  claimed only as search-indexed evidence. Kill.
- **Tail patterns — KILL, no standalone archive by the card's
  own construction.** Every tail record found is a field
  inside a host catalogue already hunted (cheetah tail tips,
  C12; dolphin tail stocks, C7) or a species-level fact-sheet
  trait (ring-tailed lemur ring counts). A tail-first pass
  would be a re-slice of other niches' custody, not a set.
  Kill.

## Pair-Hunter flags (checked, none viable)

- **Hair medulla × guard-hair scale casts** — the card's
  two-rulers pair (same vouchered hairs, two preparations).
  Checked: both preparations were *jointly published* in the
  same atlases (Texas TTU SP-055 keys medulla + scales
  together for 150+ species; Tóth likewise) — the join the
  pair would test was run by the atlases themselves. Closed.
- **Vibrissae follicle maps × whisker-spot photo ID (C7)** —
  same pads, two readings. Not viable: follicle arrangement
  is species-stereotyped, spot patterns are individual; there
  is no shared individual key to join on. Closed.

## Ranking

1. **Hair Atlas sample pile + ZSI layer — INVENTORY.** The
   wave's most complete verified surface: 10 status-200 PDFs,
   four REAL samples, medulla/cross-section data exactly as
   carded — published by design, sample-fraction only.
2. **Lab-animal marking charts — INVENTORY.** A century of
   rival punch/clip/tattoo codes, all in print; the cleanest
   methods-literature set in the wave.
3. **NMSU hoof/track guides — INVENTORY.** The measurement
   layer of the hoof niche, in extension-service print.
4. **The custody/premise map — the wave's real product.**
   4-H nose-print cards, claw-mark paper templates, Tentieva's
   157 paper prints, taphonomy lab bones, diceCT specimens,
   and two premises closed on evidence (claw comparison
   already run; tail archive never standalone).

## Score cuts recommended (parent to apply; reasons stated)

| Niche | Cut | Reason |
|---|---|---|
| hair-medulla-cross-sections | 7 → 6 | Same ceiling as guard-hair, one notch lower yield: flagship surface is a 6-spread sample, not a stack. |
| sheep-goat-nose-prints | 6 → 5 | Paper-card custody confirmed at its one systematic series (4-H); modern field moved rulers. |
| cat-nose-leather-patterns | 6 → 5 | Premise rests on a single 2025 paper; no archive ever built. |
| hoof-cloven-track-systems | 6 → 5 | Guides real; forensic reference sets have no surface anywhere probed. |
| claw-mark-archives | 6 → 5 | Already-run comparison + paper templates (C12 palm/sole shape). |
| bite-mark-records | 6 → 5 | Lab-local physical custody; data only as paper tables. |
| vibrissae-follicle-maps | 6 → 5 | Species-stereotyped, not individual — ID premise fails; specimen custody. |
| tail-pattern-systems | 6 → 4 | Thinnest card in the registry: no standalone archive exists even in principle; wholly a field inside hunted catalogues. |
| lab-animal-marking-records | 6 → 5 | Charts published (inventory), logs institutional — split outcome, net one-step cut. |

*Method notes (standing + this wave's corrections): Wayback
counts status-200-filtered before counting; the hairatlas pile
was enumerated by unique filename across the whole-domain CDX
(10 PDFs), correcting verify14's prefix query which returned
rows=10/status200=10 by coincidence of collapse. Every grade
rests on ≥1 sample download with size + md5 + magic in
`outputs/verify14-20261118-214344.json`, except where a host
was unreachable from this client and the shortlist says so
(MMU e-space PDF, Tasmania DPIPWE PDF, Scand J LAS PDF —
all claimed only as search-indexed evidence; the USDA manual
sample is a 2 MB head sample, md5 of head only). README
verified-results NOT updated — no find in this wave meets the
stranded bar those entries set. The mammal registry is now
fully fired: 50/50 niches; the mammal registry's career GOLD
tally stands at one (Manatee scar sheets, C8), with the
remaining yield in silvers, inventories and the custody map.*
