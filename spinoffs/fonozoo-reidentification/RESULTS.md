# Fonozoo Re-identification — Results

**The minting of the Wave 1 GOLD (Fonoteca Zoológica stranded frog-call pile).**
Pre-registration: commit `d2700cf`, written before any name was resolved.
Backbone: GBIF Backbone Taxonomy via the species-match API, accessed 2026-11-18.
Full per-name table: `data/classifications.csv` (573 unique names resolved).

## Headline

Of **629 countable species-named recordings** (556 unique filed names) in the
stranded pile:

| Outcome | Recordings | % | Unique names | % |
|---|---|---|---|---|
| **Name changed** (MOVED + SYNONYM + SPLIT-ELEVATED) | **146** | 23.2 | 127 | 22.8 |
| **Split-ambiguous** (REQUIRES-LOCALITY, not guessable) | **6** | 1.0 | 5 | 0.9 |
| **Unchanged** (filed name is still the accepted name) | **469** | 74.6 | 416 | 74.8 |
| Unresolved (name not carried by the backbone) | 8 | 1.3 | 8 | 1.4 |

Changed, by kind: **MOVED 129 recordings / 112 names** (genus recombination
only) · **SYNONYM 15 / 13** (epithet replaced or combination sunk) ·
**SPLIT-ELEVATED 2 / 2** (filed subspecies is now a species; identity
determined). Split-ambiguous: 6 recordings under 5 filed names whose taxon
concept was partitioned by a named revision — the recording's true species
depends on its locality/voucher, which the filenames do not carry.

The pile behind the headline: 1,013 verified audio files → 636 recordings
with a parseable species name (631 binomials, 5 trinomials), 30 provisional
(aff./cf./sp., reported separately), 47 genus-only, 1 fragmentary, 299
unnamed. Five firm-looking filings (7 recordings) proved not to be
scientific names at all (a place + "slow", a Portuguese vernacular name, a
person's name…) and were excluded from the denominator, listed in the data.

## Novelty verdict

**OPEN — the claim survives, shrunk to its honest scope** (full scrub in
`NOVELTY.md`). The Fonoteca's own publications document the collection's
history and catalogue (62,424 records), and GBIF.ES registered collection
metadata in 2008 — but no publication, dataset, or treatment has ever
re-identified the collection's recordings name-by-name against current
taxonomy, and the stranded web audio pile itself sits in no formal archive.
Surviving claim: **the first name-by-name taxonomic re-identification of
the Fonoteca Zoológica's stranded web audio pile (filenames only), resolved
against the GBIF Backbone (accessed 2026-11-18), counted at unique-name and
recording level.** It does not cover the Fonoteca's full internal catalogue.

## Scorecard (pre-registered, thresholds fixed before resolution)

| # | Prediction | Result | Verdict |
|---|---|---|---|
| P1 | ≥35% of unique firm names MOVED+SYNONYM | 22.5% (125/556) | **FAIL** |
| P2 | MOVED ≥60% of (MOVED+SYNONYM), and the largest | 89.6% (112/125) | **PASS** |
| P3 | SPLIT recordings 5–20% of firm recordings | 1.3% (8/629) | **FAIL** |
| P4 | UNCHANGED share of unique names in 40–65% | 74.8% (416/556) | **FAIL** |
| P5 | One catch-all donor genus ≥15% of changed recordings | Hyla, 26.3% (40/152) | **PASS** |
| P6 | Trinomial change rate exceeds binomial by ≥15 pts | 80.0% vs 23.2% (n = 5 trinomials) | **PASS** |

**3 of 6.** The misses are informative, not noise: the pile is far more
name-stable than predicted (P1, P4), because the guides are mostly
Neotropical, where the last two decades of churn took the form of genus
recombinations (P2, overwhelming) rather than name replacements — and the
famous European cryptic splits (P3) touch only a handful of tracks in a
pile dominated by the Neotropics and Madagascar. Where splits do bite, they
bite exactly as predicted (P5, P6).

## The splits (REQUIRES-LOCALITY — never guessed)

| Filed name | Recordings | Partitioned by | Daughters include |
|---|---|---|---|
| Bufo viridis | 2 | Dufresnes et al. 2019 (15 Bufotes spp.) | Bufotes viridis s.s., B. sitibundus, B. boulengeri, B. cypriensis… |
| Hyla arborea | 1 | Stöck et al. 2008 | H. arborea s.s., H. molleri (Iberia), H. orientalis |
| Rana temporaria | 1 | Vences et al. 2017 / Dufresnes et al. 2020 | R. temporaria s.s., R. parvipalmata (NW Iberia) |
| Bufo granulosus | 1 | Narvaes & Rodrigues 2009 (12 spp.) | Rhinella granulosa s.s. (NE Brazil only), R. major, R. bergi… |
| Mantidactylus betsileanus | 1 | Scherz et al. 2022 (8+ spp.) | M. betsileanus s.s., M. noralottae, M. tripunctatus… |

Split-elevated (identity determined, counted as changed): **Bufo granulosus
major → Rhinella major**; **Discoglossus pictus scovazzi → Discoglossus
scovazzi**. Screen candidates checked and *excluded* with reasons in
`scripts/analyse.py`: Scinax ruber (no single formal partition), Mantella
ebenaui (resurrected, not partitioned), Boophis luteus (group-level
additions only), Boophis albilabris, Physalaemus cuvieri. The screen is a
documented lower bound, not a census of all splits.

## Biggest donor genera (changed recordings)

**Hyla 40** (→ Boana, Dendropsophus, Dryophytes, Hyloscirtus…) · **Bufo 29**
(→ Rhinella, Peltophryne, Bufotes…) · **Hypsiboas 15** (→ Boana, wholesale)
· **Eleutherodactylus 10** (→ Pristimantis) · Platypelis 6 · Rana 5 ·
Epipedobates 4 · Phyllomedusa 4 · Phrynopus 4 · Phrynohyas 3.

## Worked examples (filed → current, traced end to end)

1. **`0800 alytes muletensis.mp3`** (/sonidos, captured 2015-09-26) →
   **UNCHANGED.** *Alytes muletensis* is still the accepted name (GBIF
   EXACT, ACCEPTED). The campaign's own sample file stands.
2. **`4 Bufo Granulosus Major.mp3`** (Bolivia guide) → **SPLIT-ELEVATED.**
   The filed trinomial is a synonym of the species **Rhinella major**:
   Narvaes & Rodrigues (2009) raised Gallardo's subspecies of the
   granulosus complex to species; Bolivia is inside R. major's range.
3. **`17 Discoglossus Pictus Scovazzi.mp3`** → **SPLIT-ELEVATED.**
   Now the species **Discoglossus scovazzi** (backbone: filed trinomial is
   its synonym at subspecies rank). Its sibling filing *D. pictus auritus*
   went the other way — sunk into *D. pictus* (SYNONYM).
4. **`39 Hyla Arborea .mp3`** → **SPLIT-AMBIGUOUS.** The backbone still
   accepts *Hyla arborea* unchanged — but Stöck et al. (2008) partitioned
   the concept: an Iberian recording under this name is *H. molleri*. The
   filename carries no locality, so the recording is flagged
   REQUIRES-LOCALITY, not reassigned.
5. **`36Bufo Viridis.mp3`** → **SPLIT-AMBIGUOUS.** Filed name is a synonym
   of *Bufotes viridis* — and Dufresnes et al. (2019) resolved the old
   *Bufo viridis* sensu lato into 15 Bufotes species. Genus move *and*
   partition; locality decides.
6. **`Eleuthe atkinsi_48.mp3`** (Cuba guide) → **UNCHANGED, after a logged
   correction.** The guide truncates the genus to "Eleuthe" in all 47 of
   its Eleutherodactylus filings; expanded (uniquely, pile-internally),
   *Eleutherodactylus atkinsi* is accepted as filed.
7. **`30 Bufo Calamita.mp3`** → **MOVED.** Synonym of **Epidalea calamita**
   — same epithet, new genus.
8. **`6999Hyla  eximia.mp3`** → **MOVED.** Now **Dryophytes eximius**
   (genus recombination + gender agreement).
9. **`Leptodactylus chaquensis macrosternum`** (combined guide filing) →
   **SYNONYM per the backbone** (combination sunk into *L. chaquensis*) —
   with a documented divergence: Magalhães et al. (2020) lump the whole
   chaquensis–macrosternum pair into *L. macrosternum*. The backbone is the
   registered arbiter; the disagreement is on the record, not hidden.

## Hand-check log (summary)

All 93 non-EXACT / low-confidence matches were eyeballed. Twelve filed
names needed a correction query (`results/corrections.json`): misspelled
genera (Gubermantis→Guibemantis, Hpsiboas→Hypsiboas, Tlacohyla→
Tlalocohyla), Cuba-guide truncations completed only where the completion
is unique in the Cuban fauna (Eleuthe plani→E. planirostris, gund→
gundlachi, guana→guanahacabibes, klini→klinikowskii, Osteopilus sept→
septentrionalis), and two real era combinations missing from the backbone
(Colosthetus brunneus→Allobates brunneus MOVED; Eleutherodactylus
reichlei→Pristimantis reichlei MOVED). Thirty further filings are pure
orthographic variants of the accepted name (diptyyx→diptyx, goudoti→
goudotii…) and count as UNCHANGED. The 8 UNRESOLVED names are Madagascar
guide candidate/manuscript names the backbone carries at genus rank only
(Mantidactylus andranofotsy, M. toamasina, M. tolagnaro, M. tsaratanana,
M. "park", Platypelis antsirasira, P. vevembe) plus Pleurodema ufonina.

## Method limits (plain)

- **Filenames only.** The unit is the name as filed in the web filename,
  not the Fonoteca's internal catalogue record; no audio was re-listened
  to, and no voucher was inspected. A recording whose filed name stands
  can still be a misidentified animal — that audit needs ears and
  vouchers, and is the natural next study.
- **Backbone ≠ truth.** GBIF Backbone (accessed 2026-11-18) arbitrates
  every class; where the primary literature disagrees with it (the
  Leptodactylus lump), the disagreement is flagged, not resolved.
- **The split screen is a lower bound.** It contains only partitions
  verified against a named revision for names present in this pile;
  unscreened complexes (e.g. Scinax ruber) stay unflagged by design.
- **Dedup rule:** same normalised basename + same CDX length counted once
  (0 exact duplicates found); distinct takes are distinct recordings, so
  recording-level percentages weight prolific species more than
  name-level ones. Both levels are reported throughout.
- The pile is mostly anuran but not exclusively; the few non-anuran files
  carry no parseable binomial (concatenated or vernacular filenames) and
  never entered the firm set.
