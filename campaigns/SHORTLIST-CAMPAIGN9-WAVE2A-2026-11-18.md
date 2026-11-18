# Goldmine Hunter — Campaign 9 shortlist: Broad Wave 2A (2026-11-18)

The **broad registry's** second campaign: all nine unfired 8/10
niches, in registry order — cephalopod-beaks, bivalve-shell-rings,
bird-egg-collections, seed-bank-germination-vintages,
diatom-type-slides, wood-anatomy-xylarium, blood-group-surveys,
pathology-museum-jars, tide-marigrams. Grades are `GRADES.md`'s,
fixed before digging and applied unchanged. Method = Campaigns
6–8 exactly: live crawl + Wayback inventory filtered to
statuscode:200 before counting (`campaign9_wave2a.py`,
`outputs/campaign9-20261118-200003.json`), then three verify
passes (`verify9.py`, `verify9b.py`, `verify9c.py` — see
Method notes for why there are three; samples in
`gold/campaign9-verify/`, 864 KB total new disk). Researcher-only / internal systems (Genesys/GGCE internals,
AFND, MIPS-class museum catalogues) were documented as custody
and **not** scraped or circumvented.

**Headline, plainly: NO GOLD and NO DIAMOND.** One small SILVER
(the WSL static wood-anatomy key), four INVENTORY, and a run of
honest kills — several of them custody findings. The 8-band of
the broad registry behaved exactly as the calibration law from
Campaigns 6–8 predicted: every niche in this wave has *some*
infrastructure — a formal archive (NOAA NCEI, PSMSL, GBIF), a
joined database (InsideWood, AFND, diatoms.org), a platform
(Genesys, OMERO), or a physical collection whose catalogue is
internal (WFVZ, Gordon, LABCOP) — and wherever infrastructure
exists, the loose-file pile does not. The two old-site leads
that looked most Fonozoo-shaped (woodanatomy.ch, BloodBook)
both turned out to have been absorbed or rebuilt: the wood key
is now a maintained WSL static publication, and BloodBook's
classic ABO table page no longer carries a table. With no GOLD
set there is no novelty scrub and no pre-registration to write,
and **no README verified-results entry is proposed** — flagged
here for the parent, per standing rule, as a nil return.

## SILVER — published-by-design, verified

**WSL static dendro tree — the Schoch et al. wood-anatomy key,
frozen in its web form (PUBLISHED-BY-DESIGN, live, verified).
Niche: wood-anatomy-xylarium.** `woodanatomy.ch` now 301-redirects
to `static.wsl.ch/land/products/dendro/` — WSL's own static tree
carrying the 2004 Schoch/Heller/Schweingruber/Kienast *Wood
Anatomy of Central European Species* web key: `welcome.html`
(200, 6,708 B), `ident_key.html` (200, 50,654 B, 91 refs),
`species_list.html` driven by `js/species_list.js` (sampled:
REAL text data, 4,132 B, md5 `0b178712b05eac0ce056f350c1757ffd`).
A complete published identification key with section imagery,
kept on a static tree while WSL's main site moved on — the
EBRWS class: a kept, published vintage surface, at most SILVER.
The cross-surface comparison it would enable (WSL key codings
vs InsideWood for shared Central European species) is blunted
by the fact that InsideWood already joined this tradition's
feature data (below), which caps the grade at SILVER (small).

## INVENTORY — verified real, published, no comparison completed

- **NOAA NCEI paleo — Butler *Arctica islandica* directories
  (PUBLISHED-BY-DESIGN formal archive). Niche:
  bivalve-shell-rings.** Two author directories of loose .txt
  files inside the formal NOAA paleo archive: Butler2013 —
  17 files (raw increment measurements, chronologies, lifetimes,
  isotope series); Butler2009 — 9 files. Samples verified:
  `butler2013-raw.txt` REAL data, 191,038 B, md5
  `8a7c9c3461300f91322278a8ae78dba5` (verify9b retry; verify9's
  first fetch returned EMPTY — corrected, see Method notes);
  `butler2013-stats-ne.txt` REAL text, 6,676 B, md5
  `696fa37503526112fe6307e40e5f4426`; `butler2009-deltaR.txt`
  REAL text, 10,494 B, md5 `c7e826a5903cf8662ae55effbe66fc6e`.
  Exactly the niche's raw material — deposited in the formal
  archive, with its papers. The image side of the niche (shell
  section photographs) appears in no directory probed.
  Inventory.
- **InsideWood coding sheets (PUBLISHED-BY-DESIGN). Niche:
  wood-anatomy-xylarium.** The joined database's own data-entry
  templates are loose files on the NCSU site:
  `ModernWoodDataSheet.xlsx` REAL xlsx, 14,558 B, md5
  `f3db9623dfc2374aba6b0ed1f4898dbe` (plus fossil/softwood
  sheets, .xls twins). Blank templates, not data — the database
  behind them is the field's central reconciliation product.
  Inventory as files; the niche's joined surface itself.
- **Bird-egg GBIF DwC-A sets (PUBLISHED-BY-DESIGN formal).
  Niche: bird-egg-collections.** The egg world publishes
  through GBIF/Arctos: MVZ's 12,800+ egg sets via Arctos/iDigBio,
  and the Nosachenko collection (1,611 clutches, 1907–1959) as a
  GBIF IPT Darwin Core Archive — resource page 200, archive
  download HEAD 200 (`application/zip`), discovered from the
  resource page at verify time. Real, integrated, published.
  Inventory.
- **diatoms.org species imagery (PUBLISHED-BY-DESIGN). Niche:
  diatom-type-slides.** The curated flora (1,144 species pages)
  serves its LM/SEM imagery openly; a *Cymbella hustedtii* LM
  valve image sampled REAL JPEG, 24,311 B, md5
  `ad4f5d12aed590fd2969147c0060a056` (verify9c; verify9's first
  sample was the site's favicon and verify9b's a habitat photo —
  both corrected and neither counted, see Method notes).
  Inventory.
- **PSMSL data service files (PUBLISHED-BY-DESIGN formal).
  Niche: tide-marigrams.** The consolidated service's loose
  files are exactly its product: `catalogue.dat` REAL text,
  703,499 B, md5 `70726f95da1d31dad29cb31aaf295685`; station
  15 (Liverpool, 1857–1983) monthly RLR file REAL text,
  39,468 B, md5 `691b090c7605e24cc38f3c3f423c6c01`; Aden
  calibrations .xls REAL OLE2, 401,920 B, md5
  `6a6291618011745e03b8acec6071a163`. Monthly means published
  by design for decades — the niche card said so itself.
  Inventory.

## KILLS & CUSTODY FINDINGS — probed, nothing claimable, evidence stated

- **Cephalopod beaks — KILL for recovery; the reference layer
  is published books, the collections are jars.** The field's
  beak-to-body ruler exists as published guides, verified:
  Xavier & Cherel's *Cephalopod Beak Guide for the Southern
  Ocean* (2021 rev. ed.) PDF on the NERC NORA repository —
  REAL PDF, 5,046,272 B downloaded at the 5 MB cap, md5 of
  head `2bacf226578794b1b277927ab03816a7`. The one collection
  paper with full curation detail (LABCOP, Brazil: 562 beaks,
  50 taxa, from predator stomachs) is a journal PDF — REAL
  PDF, 336,891 B, md5 `4ffb826da2bfa78424aa2f2d9561a880` —
  describing a physical liquid-preserved collection; no
  beak-by-beak measurement file was found on BAS, NORA, or
  any host crawled. The measurement piles the niche card
  hoped for live in the guides' printed tables and in thesis
  appendices, not in web files. INVENTORY for the guide
  itself is recorded under Kills here rather than above
  because the guide is a book, not a data surface.
- **sclerochronology.org — KILL, no surface.** The community
  domain returns nothing to this client live and its CDX
  inventory is 0 collapsed captures. Stated as a host result,
  not as a claim about the field.
- **WFVZ egg collection — KILL for recovery; custody finding.
  Niche: bird-egg-collections.** The world's largest egg
  collection (~250,000 sets, 1M+ eggs) serves a collections
  page (200) whose data sentence is a by-request offer —
  "Staff of the WFVZ provide data on eggs, including
  measurements and digital images, to researchers… contact
  us" (verified in the page text this campaign). The Alfred
  Denny (Sheffield) collection is the same shape one scale
  down: ~1,300 historic eggs photographed and "databased" in
  a 2024 student internship, served as a Google Sites page
  with 46 images and zero data files. Drawers and internal
  databases, not files.
- **Seed-bank germination vintages — KILL for recovery.** The
  niche's flagship modern dataset (Australian Grains Genebank:
  24,141 germination observations over ~40 years) exists only
  as its 2026 paper (Baum et al., *Plant Genetic Resources*
  24(4), doi `10.1017/S1479262125100488`); the one personal
  site analysing it (mariuscomper.uk) carries a 5,088 B
  `evidence.json` that is the blog's *citation file for that
  paper* — sampled REAL text, md5
  `54c47af31e70dd52732bd66b65d9a21b` — not accession data.
  Genesys is a platform (its 43 crawl "data files" are locale
  JSON furniture); GGCE is genebank *software* whose viability
  module keeps test records inside each bank's own system.
  The accession × year panel was never a web file surface.
- **Legacy ANSP diatom host — KILL; platform custody for the
  herbarium. Niche: diatom-type-slides.** `diatom.ansp.org`
  is dead live; its Wayback inventory is cap-limited at 8,000
  collapsed captures, 7,964 status-200, and **zero** carry a
  data-file extension — the legacy site was HTML/ASP pages
  with images behind scripts (the NADED/algae-image database
  class). The herbarium itself (~220,000 slides, ~5,000 types)
  is being served through a virtual-microscopy platform
  (OMERO) — a database surface, not a pile.
- **Blood-group surveys — KILL; the loose compilation's table
  is gone, the rest is books and a database.** BloodBook, the
  one-person Mourant-derived compilation, has been rebuilt as
  a modern site: its world-ABO page today is 26,084 B with
  **no `<table>` element, 6 "abo" strings and no data JSON**
  (verify9c raw counts) — the classic population table no
  longer exists in that form, and the domain's whole Wayback
  inventory (707 collapsed, 432 status-200) contains no data
  files, only HTML/GIF furniture. AFND is a formal database
  (HLA-centred; the ABO-era tables are not its product).
  Mourant's own compilations remain books; the 1948 Nature
  paper's PDF was unreachable from this client (HEAD failed —
  stated as unrun, not as absence).
- **Pathology museum jars — KILL for recovery; custody
  finding.** The Gordon Museum (KCL) page verifies the
  collection ("approximately 8,000 pathological specimens,
  all are catalogued") and offers no catalogue file — the
  crawl's only "data file" was a browserconfig.xml. The
  catalogue is an internal teaching system; the museum
  itself is a restricted teaching collection (per its own
  institutional descriptions in the discovery pass). Every
  museum surface probed this wave (Gordon, Surgeons' Hall
  via the Anatomical Theatre index) is the same shape:
  specimens and internal catalogues, no files. (Correction
  recorded: verify9b's "restriction snippet" was a false
  positive — it matched the word "restricted" in a biographical
  text about a curator's sleep habits, and no claim above
  rests on it.)
- **Tide marigrams — KILL for the scans as a loose pile.**
  The raw ink rolls are being digitised *by the field itself*,
  station by station, and published: the Ireland century
  study (McLoughlin et al., preprint sampled REAL PDF,
  2,542,402 B at cap, md5 of head
  `9c2a38c74dff680092b03bafed190be4`) documents marigram
  digitisation for Dún Laoghaire, Belfast, Cork and Tarbert
  as completed data archaeology with the series deposited in
  the formal services. What a hunter would recover here has
  already been recovered, by its owners.

## Ranking

1. **WSL static wood-anatomy key — SILVER (small).** The
   wave's only kept vintage surface: a complete published
   2004 web key, frozen on a static tree, sample-verified.
2. **NOAA NCEI Butler directories + PSMSL service files +
   GBIF egg sets + diatoms.org imagery — INVENTORY.** Real,
   verified, formally published; nothing to recover.
3. **WFVZ + Gordon + LABCOP + AGG — the wave's custody map.**
   Four major collections whose data exist and matter and
   are not files: the digitisation-with-institutions list
   grows by four.

*Method notes (standing + this wave's corrections): Wayback
counts status-200-filtered before counting; every grade rests
on ≥1 sample download with size + md5 + magic in
`outputs/verify9b-20261118-200924.json` /
`outputs/verify9c-20261118-201100.json` and `verify9.log`
(verify9 hit its timeout inside §7 on a hanging nature.com
fetch before its own JSON saved, so §§8–9 and three defective
samples were re-run in verify9b/9c rather than silently
dropped; verify9's §§1–6 evidence stands in its log). Corrections made and recorded:
verify9's Butler2013-raw EMPTY was a transient fetch failure —
the retry returned 191,038 B of real data (its `-noaa` twin
stayed unreachable and is claimed as nothing); verify9's
diatom sample was the site favicon (2,219 B PNG, deleted) and
verify9b's a habitat photograph — the counted sample is
verify9c's LM valve image; verify9b's WSL Wayback sample was
a 236 B flag gif (furniture) and is not counted — the WSL
claim rests on the live tree + species_list.js sample;
verify9b's Gordon "restriction" snippet was a false-positive
match, flagged in place above. Hosts that blocked or failed
this client are stated as host results (sclerochronology.org,
diatom.ansp.org live, nature.com, WFVZ crawl timeout — its
collections page was fetched successfully in verify9).
README verified-results NOT updated — no find in this wave
meets the stranded bar those entries set.*
