# Calibration — Campaign 6 / Wave 1 vs the niche registry (2026-11-18)

Registry scores were assigned on paper (fidelity + headline +
fragmentation tests) before any campaign fired. Wave 1 ran the
eight 9/10 niches. Score vs outcome, per niche:

| Niche | Registry score | Wave 1 outcome | Verdict on the score |
|---|---|---|---|
| frog-call-archives | 9 | **GOLD** (Fonozoo, seed 1) | Predicted. The one niche whose flagship was a file pile on an old site, exactly as carded. Score stands. |
| autopsy-cause-of-death-ledgers | 9 | **SILVER** (Barts registers) | Material predicted exactly; strandedness over-predicted — the flagship archive digitised and serves its ledgers openly. Score stands, grade ceiling at flagship = silver, noted in niches.json. |
| salmon-scale-archives | 9 | INVENTORY (NOAA spreadsheets; images internal) + KILL (Burrishoole web host) | Half-predicted: the data exists and the label gap is real, but the raw images are network-internal, not web-stranded. **9 → 8, applied.** |
| long-term-crop-plot-books | 9 | KILL (Sanborn: no file pile) | Single-host evidence; the flagship-curation logic held (Morrow) but the tail host keeps records off the web. **9 → 8, applied.** |
| fish-otoliths | 9 | KILL ×2 (AFORO + UNAM, both adapter-class; AFORO also GBIF-mirrored) | Over-predicted. The niche's collections are database products, not file piles — the fragmentation test was misapplied to interface-era collections. **9 → 7, applied.** |
| electric-fish-eod | 9 | KILL (mormyrids: deep crawl + audio CDX = 0) | Over-predicted at the flagship host: the recordings were never web files at all. **9 → 7, applied.** |
| longitudinal-growth-studies | 9 | KILL ×2 (Harpenden in formal archive; Nittedal no host; AAOF already consolidated at probe) | The niche is consolidating/archived wherever checked — fragmentation premise failing niche-wide. **9 → 7, applied.** |
| river-gauge-charts | 9 | KILL for charts (paper-only at OPW) + INVENTORY (live service) | The pattern repeated the Danube: the one basin checked in depth keeps charts on paper and publishes the rescue. **9 → 7, applied.** |

Adjustments were applied to `niches.json` (new `score`, old kept
as `score_pre_campaign6`, reason in `calibration_2026_11_18` per
niche). *Tooling debt, stated:* `build_niches.py` still carries
the pre-campaign scores — regenerating the registry from it
would revert these five cuts. The registry's source of truth is
now `niches.json` as amended; the builder needs the same edits
before its next run.

**Pattern in the misses:** every over-prediction shared one
shape — a collection that *looked* fragmented from its papers
turned out to be a database, an internal network, a formal
archive, or paper. The score's fragmentation test was being
passed on the *field's* fragmentation, when what pays is
fragmentation of the *files*: loose files on an old website,
which only frog-calls (and, in earlier campaigns, Brain
Catalogue and Maddison) actually had. Future scoring should
require evidence of loose-file hosting — a directory listing, a
files/ tree, guide pages linking raw files — before a niche
scores above 7.

## The tooling question: registry-generated vs hand-picked

| | GOLD | Other verified yield | Seeds/hosts |
|---|---|---|---|
| Campaign 4 (hand-picked) | 0 | 1 small DELETED set (HCA matrices, caveated) | 15 hosts |
| Campaign 5 (hand-picked) | 0 | 1 small DELETED set (SCOP) + 4 live vintage stacks (silver class) | 17 hosts |
| **Campaign 6 Wave 1 (registry-generated)** | **1 (Fonozoo, 1,013 files)** | 1 SILVER (Barts), 2 INVENTORY | 9 seeds / 11 hosts |

**Verdict: the registry beat hand-picking on its first wave** —
the only GOLD-class set of the last three campaigns came from
the registry's #1 seed, and it came with its comparison and
anchor already named by the niche card. Two honest caveats:
(1) the wave's gold came from its single strongest probe signal,
so this is one draw, not a rate — Waves 2+ will show whether
registry order keeps paying below the head of the queue;
(2) the registry's *scores* were badly calibrated below the top
seed (five of eight 9s cut) — the registry's value so far is in
its *target generation* (concrete hosts, named comparisons),
not in its numbers. Both caveats argue for continuing the waves
with the calibration loop running, which is what the registry
was built for.

---

# Calibration — Campaign 7 (Mammal Wave) vs the mammal-grain registry (2026-11-18)

The mammal registry's seven 9/10 niches were all fired on.
Score vs outcome, per niche:

| Niche | Registry score | Campaign 7 outcome | Verdict on the score |
|---|---|---|---|
| whale-fluke-trailing-edge | 9 | **SILVER** (Juneau edition stack) + INVENTORY (Dominica Fluke Book) + KILL (CCS catalogue = database; NAMSC = CD-era) | Material and stack predicted; strandedness over-predicted — the field professionalised into Happywhale/Flukebook/curated databases. **9 → 7, applied.** |
| primate-fingerprints-dermatoglyphics | 9 | **SILVER** (Wellcome Galton IIIF, 3,022 canvases — mostly human) + KILL for the primate sets (chimp bundle closed-stores; Wistar sets no digital surface) | The digitisation surface exists exactly where institutions did it, and the niche's own quarry is pointedly not in it. **9 → 7, applied.** |
| cattle-muzzle-prints | 9 | **KILL for recovery — major custody finding** (3M+ prints, paper only, zero digital surface) | The fidelity card was right about the archive and wrong about its surface: it was never scanned at all. **9 → 6, applied** — the cut prices hunter-recoverable gold only; as a digitisation target this niche is now the registry's most valuable negative. |
| paw-track-morphometrics-fit | 9 | KILL (training libraries project-held; software by request; supplements carry documents, not images) | Fragmentation of *projects* again failed to mean fragmentation of *files*. **9 → 7, applied.** |
| dolphin-dorsal-fin-notches | 9 | INVENTORY (Beaufort formal-archive subset, DOI) + KILL/custody (GoMDIS researcher-only; FinBase piles never surfaced) | The one public extract had been formally archived — the flagship pattern from Wave 1's Harpenden kill, repeated. **9 → 7, applied.** |
| elephant-ear-edge-veins | 9 | INVENTORY (elephant.se database) + KILL/custody (Who's Who protected; ATE unreachable from this client) | Cards stay in custody by deliberate design (poaching). A niche can be scientifically rich and hunter-proof. **9 → 7, applied.** |
| whisker-spot-patterns | 9 | KILL (galleries + reports only) + INVENTORY (Kunene/Stander PDFs) | The records live inside project systems that publish reports, not files. **9 → 7, applied.** |

Adjustments applied to `mammal_niches.json` (new `score`, old
kept as `score_pre_campaign7`, reason in
`calibration_2026_11_18_campaign7` per niche). *Tooling notes:*
(1) `build_mammal_niches.py` still carries the pre-campaign
scores — same debt as the broad builder; `mammal_niches.json`
as amended is the source of truth. (2) The `mammal-niches`
listing preserves registry order rather than re-sorting by
amended score — after these cuts the effective head of the
queue is **guard-hair-scale-casts (9, unfired)**, followed by
the 8-band (koala-fingerprints, dog-nose-prints,
plaster-track-cast-collections, elephant-footprint-age,
right-whale-callosity-patterns, manatee-photo-id-scars,
rhino-ear-notch-horn-profiles); the listing should re-sort
before Wave 2 fires.

**Pattern across both waves, now stated at both grains:** the
registry's scores over-predict strandedness wherever a field
has *any* professional infrastructure — a platform, a database,
a formal archive, a card room. What has actually paid, three
times now (Brain Catalogue, Maddison, Fonozoo), is a field
whose practitioners posted loose files on an old website
because no infrastructure existed. The mammal wave's seven
niches all had infrastructure. Its one great product is a
custody map: Wagyu's unscanned 3M prints, the closed-store
chimp bundle, GoMDIS and Who's Who behind their walls — the
places where a future *digitisation* campaign, run with
institutions rather than crawlers, would go.

---

# Calibration — Campaign 8 (Mammal Wave 2) vs the mammal-grain registry (2026-11-18)

The recalibrated head of the mammal queue was fired: the one
remaining 9 (guard-hair) and six of the 8s. Score vs outcome:

| Niche | Score (pre-C8) | Campaign 8 outcome | Verdict on the score |
|---|---|---|---|
| manatee-photo-id-scars | 8 | **GOLD** (Hartley scar-sheet set, stranded, ~200 individuals) | Under-predicted — the one niche whose working catalogue was a loose file on an old subdomain because its keeper is one observer with a pencil, not an institution. **8 → 9, applied.** |
| guard-hair-scale-casts | 9 | **SILVER** (four published atlas surfaces: TTU SP-055, CMU, ZSI, Landcare) | Material and loose-file hosting predicted exactly; strandedness over-predicted — every surface is a deliberate publication. Silver ceiling at the surfaces checked. **9 → 8, applied.** |
| right-whale-callosity-patterns | 8 | **SILVER (small)** (EBRWS live brochure stack) + custody (NARWC protocol, ARWPIC, ICB/Flukebook) | The Juneau pattern repeated: the small project publishes its catalogue and the big systems are consortia. **8 → 7, applied.** |
| elephant-footprint-age | 8 | INVENTORY (Parker, already formally published) + KILL/custody (ATE Access databases) | The niche's data layer is integrated or custodial wherever checked. **8 → 7, applied.** |
| dog-nose-prints | 8 | KILL for recovery — custody (CKC microfiche; Korean set by-request; Ant Group platform gone) | The registry form (paper → microfiche) was never a file surface at any era. **8 → 6, applied.** |
| plaster-track-cast-collections | 8 | KILL for recovery — custody (museum drawers; Smithsonian formal DwC-A; Idaho VM approval-gated) | Physical-custody niche: digitisation is a platform with a gate, not a pile. **8 → 6, applied.** |
| koala-fingerprints | 8 | KILL — paper-only (two small papers; no collection exists online) | Decisively falsified as a file hunt; the premise (a print collection) is false on the web. **8 → 5, applied.** |

Adjustments applied to `mammal_niches.json` (new `score`, old
kept as `score_pre_campaign8`, reason in
`calibration_2026_11_18_campaign8` per niche). The
`mammal-niches` listing-sort patch (sort by current score,
stale `rank_by_score` as tiebreak only) landed before this
wave fired, so the queue now re-sorts itself after every
calibration; the unfired head is now the coat-pattern block
(rhino-ear-notch, pinniped pelage, tiger stripes, leopard
rosettes, zebra, giraffe — all 8, all platform-era photo-ID,
which this wave's pattern says to discount before firing).

**Pattern update, third wave:** the one GOLD came from the
queue's *last* seed and its smallest institution — a single
observer's working files, posted by a small NGO on an old
subdomain, in a field whose formal system (MIPS) is a
*different medium* (photographs) that never absorbed the
sketch record. That refines the standing rule: what pays is
not just loose files, but loose files **whose medium the
formal archive does not ingest**. Where the formal system
ingests the same medium (photo-ID → Flukebook/ARWPIC,
specimens → DwC-A), the loose copy is a reconciliation
waiting to happen, and it happens. Where it cannot ingest
it (sketches, ink prints on cards, audio on a fonoteca's
own site), the copy stays stranded. Future scoring should
add a medium-mismatch test beside the loose-file test.

---

# Calibration — Campaign 12 (Mammal Wave 4, 7/10 batch part 1) vs the mammal-grain registry (2026-11-18)

The first ten unfired 7s were fired. Score vs outcome:

| Niche | Score (pre-C12) | Campaign 12 outcome | Verdict on the score |
|---|---|---|---|
| primate-palm-sole-dermatoglyphics | 7 | KILL — paper-only (journal PDFs verified; comparison already published 1970 + 2023) | Premise false: no archive, and the un-run comparison had in fact been run. **7 → 5, applied.** |
| paw-pad-ridge-patterns | 7 | INVENTORY (Murie full text + Amherst sheet, published) | Guides predicted; archive never existed as files. **7 → 6, applied.** |
| bear-paw-mensuration | 7 | INVENTORY (Hokkaido formal data paper) + KILL (harvest ledgers) | The designed series is formal; the ledger half is paper. **7 → 6, applied.** |
| canid-track-size-archives | 7 | INVENTORY (NASA ORNL DAAC 2188) + KILL (agency tables) | Measurement-level data exists — in the formal archive. **7 → 6, applied.** |
| snow-track-gait-archives | 7 | INVENTORY (same NASA deposit) + KILL/custody (Luke triangles) | Flagship is an institute programme publishing counts, not gait files. **7 → 6, applied.** |
| elephant-tusk-patterns | 7 | KILL — custody (Who's Who database field) | A field inside a database is not a file archive. **7 → 6, applied.** |
| cheetah-spot-patterns | 7 | INVENTORY (Kelly 2001, Mara-Meru 2022) + custody (photo albums) | Literature public, albums custodial — the C7 pattern at 7. **7 → 6, applied.** |
| snow-leopard-rosettes | 7 | KILL — custody (PAWS programme libraries, location-sensitive) | Rich and hunter-proof by design. **7 → 6, applied.** |
| painted-dog-coat-patterns | 7 | KILL — custody (park name-books) | Exactly as carded, which is the problem: carded custody is still custody. **7 → 6, applied.** |
| pangolin-scale-patterns | 7 | KILL — premise falsified (PUNS: notching, not pattern archives) | No individual pattern archive is kept. **7 → 5, applied.** |

Adjustments applied to `mammal_niches.json` (new `score`, old
kept as `score_pre_campaign12`, reason in
`calibration_2026_11_18_campaign12` per niche).

**Pattern update, fourth mammal wave:** the 7-band adds a
third failure shape beside infrastructure and custody — the
*already-run comparison* (palm/sole atd was graded against
karyotypes by its own literature in 1970) and the *formal
deposit of exactly the imagined data* (NASA's snow-track
CSVs). At 7, a niche can be scientifically real, measurably
comparable, and still worth zero to the hunter because
someone — the field itself, or an archive — already did the
join. The medium-mismatch test from Campaign 8 stands: none
of these ten had a medium the formal system cannot ingest.

---

# Calibration — Campaign 11 (Mammal Wave 3) vs the mammal-grain registry (2026-11-18)

(Appended after Campaign 12's section — the parallel waves
landed out of numeric order; nothing above was altered.)

All nine unfired 8s were fired. Score vs outcome:

| Niche | Score (pre-C11) | Campaign 11 outcome | Verdict on the score |
|---|---|---|---|
| rhino-ear-notch-horn-profiles | 8 | KILL for recovery — custody (per-reserve personal files; RhODIS forensic, 180,000+ samples) | Anti-poaching custody by design; the niche is hunter-proof exactly as the elephant-ear niche was. **8 → 6, applied.** |
| pinniped-pelage-patterns | 8 | **SILVER** (SealID, DOI dataset) + INVENTORY (monk-seal report) + custody (NOAA, Cap Blanc slides) | Flagship published itself whole; the rest is custody. Silver ceiling. **8 → 7, applied.** |
| tiger-stripe-catalogues | 8 | KILL for recovery — national custody (NTCA/WII) + INVENTORY (ExtractCompare demo) | Counts published, stripes sealed; the card said so and the wave confirmed it at full price. **8 → 6, applied.** |
| leopard-jaguar-rosettes | 8 | KILL (field catalogues) + INVENTORY (demos) + Wildbook custody fraction | Study-shaped custody as carded; long-tail thesis sets remain unprobed one by one. **8 → 7, applied.** |
| zebra-stripe-patterns | 8 | **SILVER** (GZGC) + INVENTORY (demo) + KILL (drawn-code era = paper) | Public layer is two deliberate releases; the historical layer is paper. **8 → 7, applied.** |
| giraffe-coat-patterns | 8 | **SILVER** (GZGC subset) + INVENTORY (demo) + platform custody (GiraffeSpotter) | The Juneau/Wildbook pattern, third coat niche running. **8 → 7, applied.** |
| tooth-wear-age-charts | 8 | **SILVER** (agency chart stack) — comparison already published (Foley et al. 2021) | The two-rulers audit the card imagines was run by the field itself, on known-age animals. **8 → 7, applied.** |
| cementum-annuli-tooth-archives | 8 | KILL for recovery — service-industry custody (Matson's) + INVENTORY (lab web surface) | A lab that sells ages files nothing; the one loose report is 404 and unarchived. **8 → 6, applied.** |
| primate-face-pattern-archives | 8 | INVENTORY (ChimpFace paper/dataset) + custody (Gombe/JGI site archives) | ML scraped its own set rather than joining the sites' portraits — the card's sentence, confirmed. **8 → 7, applied.** |

Adjustments applied to `mammal_niches.json` (new `score`, old
kept as `score_pre_campaign11`, reason in
`calibration_2026_11_18_campaign11` per niche).

**Pattern update, this wave:** Campaign 8's closing note
discounted this whole block in advance ("all platform-era
photo-ID") and Wave 3 paid a full wave to confirm it — the
coat-pattern world professionalised earliest and most
completely of any mammal system yet hunted (Wildbook,
national archives, forensic law-enforcement custody). Two
refinements worth keeping: (1) the ExtractCompare demos are a
new provenance shade — the Fonozoo *shape* (loose files, old
site, one small keeper) carrying deliberate-publication
*intent*, and under the fixed grades intent is the line:
same shape, INVENTORY not GOLD. Future scoring should ask
not only "loose files?" but "loose *working* files, or a
showcase?" (2) The teeth niches repeat Campaign 12's
already-run-comparison shape from the other side: tooth-wear
vs cementum vs known age is a *settled* two-rulers literature
(Foley 2021), so both teeth niches' headline comparisons
were dead before firing — a pre-flight literature check for
"has the comparison been run?" would have killed both cards
on paper.


---

# Calibration — Campaign 10 (Broad Wave 2B) vs the broad registry (2026-11-18)

| Niche | Score (pre-C10) | Campaign 10 outcome | Verdict on the score |
|---|---|---|---|
| glacier-repeat-photos | 8 | **SILVER** — 61 glaciers of verified repeat pairs on a living personal site; USGS (58 pairs) + NSIDC (45 sets) formal; terminus-vs-GLAMOS comparison un-run but on published-by-design data | **8 → 7.** The material was exactly as scored; the strandedness was not — the field publishes its pairs where its owners keep them. |
| paper-seismograms | 8 | **INVENTORY** — SISMOS/EuroSeismos is a formal archive (registration tiers); previews verified, preview tree uncaptured by Wayback and its host unreachable; Romanian set a 9.4 GB formal deposit | **8 → 7.** What looked like a static loose pile was the free tier of a running archive. |
| moonwatch-satellite-cards | 8 | **KILL** — ~400,000 cards are 24 cu ft of paper in Smithsonian custody; only the finding aid + a 1958 published catalogue exist as files | **8 → 5.** The koala class again: a perfect fidelity card whose population never became files. |
| steam-engine-indicator-cards | 8 | **KILL** — single-object museum records; the one scan archive's "indicator cards" are orders for blank card stock; measured populations are paper bundles | **8 → 6.** Cards survive as objects, not as a population with a surface. |
| dye-sample-books | 8 | **SILVER** — Trümpy: 17 volumes digitised + transcribed in ETH's own online catalog; Yale's recipe books catalogue-only | **8 → 7.** Best object real, and published by design — silver ceiling. |
| endangered-language-tape-shelves | 8 | **SILVER** — 1,384 status-200 AIATSIS finding-aid PDFs (the shelf list itself) sample-verified; tapes community-restricted custody via PARADISEC | **8 stands, ceiling silver.** The register is the data (Barts class) — scored right, capped by design. |
| dialect-survey-recordings | 8 | **GOLD** — 1,082 LAGS informant folders (audio + transcription + bio per folder) loose on the project's former-host site; every formal product covers 64 of 914 informants; full-pile audit un-run; minted as lags-transcription-audit | **8 → 9.** Under-scored: a complete comparable set whose medium no formal archive ingests beyond a 7% curated sample. |
| commodity-price-currents | 8 | **INVENTORY** — real Prices Current pages verified inside formal archive.org newspaper deposits; single issues, no port pile | **8 → 7.** The unit is everywhere; the comparable set is behind newspaper-corpus walls. |
| fire-insurance-plans | 8 | **INVENTORY (unsampled)** — LAC/UCalgary digitisation documented (64–81 objects per Goad volume) but every sheet surface blocked this client; authoritative catalogue itself undigitised | **8 → 7.** Probably a silver the client couldn't reach; graded on what was verified. |
| photo-finish-film-strips | 8 | **KILL** — no strip archive on the web; the niche-named PDF is a school compilation of Wikipedia text; strips are federation/timing custody | **8 → 6.** A niche whose web presence is writing about the objects. |

**Wave verdict: 1 GOLD, 3 SILVER, 3 INVENTORY, 3 KILL from
ten 8s.** The 8-band is behaving like the 9-band did: most
scores are one notch optimistic, and the gold came from the
niche whose score was one notch *pessimistic*.

**The refinement this wave adds:** the two archive-shaped
outcomes split on *coverage*, not custody. SISMOS covers
its whole seismogram population (formal archive → no gold),
while LAP's formal products cover 64 of 914 interviews —
**a formal archive that ingests only a sample leaves the
rest of the pile stranded**, and the sample's existence is
camouflage: DASS2019's polish made the full pile look
"done" for a decade. Test for future cards: *what fraction
of the population did the formal product actually take?*

Second instance of the camouflage pattern, inverted:
Trümpy's catalog and the glacier site are complete
publications (silver ceilings, honestly), while Moonwatch
and the steam cards repeat the standing law — a fidelity
card can be perfect and the population still paper.

---

# Calibration — Campaign 9 (Broad Wave 2A) vs the broad registry (2026-11-18)

The broad registry's unfired 8/10 band was fired, all nine
niches. Score vs outcome, per niche:

| Niche | Registry score | Campaign 9 outcome | Verdict on the score |
|---|---|---|---|
| cephalopod-beaks | 8 | KILL for recovery (BAS guide = published book, INVENTORY; LABCOP 562-beak collection = physical, paper-described) | The measurement piles are printed guide tables and thesis appendices, never web files; the collections are jars. **8 → 6, applied.** |
| bivalve-shell-rings | 8 | INVENTORY (Butler Arctica directories in NOAA NCEI formal paleo archive; sclerochronology.org no surface) | Material and loose-.txt hosting predicted, but the host is the formal archive itself — the Harpenden pattern. **8 → 7, applied.** |
| bird-egg-collections | 8 | INVENTORY (GBIF/Arctos DwC-A sets) + KILL/custody (WFVZ by-request; Denny internal database) | The field publishes through GBIF by design; the largest collection is custody. **8 → 7, applied.** |
| seed-bank-germination-vintages | 8 | KILL (AGG 24k-observation panel exists only as its 2026 paper; Genesys = platform; GGCE = internal software) | The built-in time series is real and entirely internal — genebank infrastructure is the niche's story. **8 → 6, applied.** |
| diatom-type-slides | 8 | INVENTORY (diatoms.org curated imagery) + KILL (legacy diatom.ansp.org: 7,964 status-200 captures, zero data files; herbarium on OMERO platform) | The personal-database era ended in platforms and a curated flora. **8 → 7, applied.** |
| wood-anatomy-xylarium | 8 | **SILVER (small)** (WSL static dendro key, frozen published surface) + INVENTORY (InsideWood templates; the joined DB itself) | The one niche whose old-site lead was real — and it is a maintained publication, silver ceiling, exactly as the guard-hair stack priced it. **8 → 7, applied.** |
| blood-group-surveys | 8 | KILL (BloodBook rebuilt — its ABO page carries no table today; AFND formal; Mourant = books) | The loose compilation existed and was rebuilt away; the underlying tables were never files. **8 → 6, applied.** |
| pathology-museum-jars | 8 | KILL/custody (Gordon: 8,000 specimens, internal catalogue, no file surface) | Teaching-museum catalogues are internal systems by design. **8 → 6, applied.** |
| tide-marigrams | 8 | INVENTORY (PSMSL service files) + KILL for scans (field's own data archaeology, published 2026) | PSMSL consolidated the numbers *and* the owners are digitising the rolls themselves. **8 → 7, applied.** |

Adjustments applied to `niches.json` (new `score`, old kept
as `score_pre_campaign9`, reason in
`calibration_2026_11_18_campaign9` per niche). Same tooling
debt as before: `build_niches.py` still carries pre-campaign
scores; `niches.json` as amended is the source of truth.

**Pattern update, fourth registry wave:** the 8-band went
0-for-9 on gold, and the reason is uniform — at this score
level every niche has already acquired its infrastructure
(formal archive, joined database, platform, internal
catalogue, or the field's own digitisation programme). The
two leads that looked loose-file-shaped at discovery
(woodanatomy.ch, BloodBook) had both been *absorbed* —
redirected into a maintained static publication, rebuilt
into a modern site that dropped the table. That adds a
third test beside loose-file hosting and medium-mismatch:
**absorption** — an old site that still resolves may have
been quietly adopted by its institution, and an adopted
site publishes by design. What has paid, four times now
(Brain Catalogue, Maddison, Fonozoo, Manatee), is a site
nobody adopted: still on its original host, in its original
form, in a medium the formal system does not ingest.

## Addendum — Campaigns 13–16 (2026-11-18, registry-generated, mammal first)

35 niches fired (mammal ranks 34–50 — the mammal registry is now
EXHAUSTED at 50/50; broad ranks 28–45). Result: **NO GOLD, NO
DIAMOND. 1 small SILVER (UNLV menus, C16), 18 INVENTORY, 16 KILL.**
Running tally after C1–16: **3 GOLD (Fonozoo C6, Manatee C8, LAGS
C10), 0 DIAMOND.**

New calibration laws from this block:
- **Completion is the new failure shape at score 7 (broad):** the
  field hasn't just built infrastructure, it has already RUN the
  registry card's headline comparison (lunar occultations re-reduced
  by VizieR itself; APPLAUSE plate-solving applied). Add a
  pre-flight "has the comparison been run?" check to niche scoring.
- **Premise errors are a real class:** livestock-iris was retinal
  (Optibrand, vendor-defunct custody); vibrissae follicle maps are
  species-stereotyped, not individual — the niche's ID premise was
  false, not just its custody bad. Score premise risk explicitly.
- **Custody Mapper post-probe confirmation:** CUSTODY-1's only
  prospective KILL (factory-payroll) was confirmed by probe at all
  three hosts — the mapper's hard-custody signals in card text are
  trustworthy; its PROBE class remains the honest default elsewhere.
- **Wayback statuscode 226 blind spot:** the dead UCLA FTP sunspot
  tree holds ≥10k captures, ALL status 226 (FTP transfer-complete);
  the standing 200-filter reads zero. Still not gold there (deleted
  mirror of a formally digitised set), but the filter needs a 226
  exception for FTP-mirror domains before it costs a real find.
- Mammal 6–7 band confirmed again: everything exists, nothing is
  loose files. The registry's remaining broad tail (ranks 46–50,
  all 6) should be expected to behave the same; the queue's centre
  of gravity shifts to minting the pairs already found (LAGS×DASS,
  Burger×Dembitzer) rather than more registry waves.
