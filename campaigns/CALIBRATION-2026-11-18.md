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
