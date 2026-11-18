# Fonozoo re-identification — pre-registration

Written and git-committed 2026-11-18, BEFORE any name in the pile
is resolved against the backbone. State at registration: the
novelty scrub is done (`NOVELTY.md`, same commit); the inventory
source (Campaign 6's verify6 CDX list, 1,013 files) has been
inspected for *filename patterns only* — counts per pile, pattern
classes, and a handful of example filenames quoted in the campaign
shortlist. No filed name has been looked up in any taxonomy
backbone for this project, and no change rate has been estimated
from data.

## The comparison

Every species-named audio file in the recovered pile (1,013
status-200 files, Campaign 6 verify6 CDX inventory) is parsed to a
filed name, and each unique filed name is resolved against the
**GBIF Backbone Taxonomy via the GBIF species-match API, accessed
2026-11-18** (GBIF's backbone is built substantially on the
Catalogue of Life / Amphibian Species of the World lineage for
amphibians; the access date and API are the version statement).
Counts are reported at two levels: **unique filed names** and
**recordings (files)**.

## Registered parsing rules

1. Source = `goldmine-hunter/outputs/verify6-20261118-181716.json`
   (`fonozoo_cdx.files`: url, first-capture timestamp, CDX length)
   plus the campaign6 whole-domain list for cross-checking only.
   No live re-crawl of fonozoo.com (origin 403-stubs our client).
2. A file is **species-named** if its filename yields a genus and
   a species epithet under the parser: strip extension, leading
   guide/track numbers (incl. `14_2`-style take suffixes and
   concatenated `2634Name` forms), trailing take digits glued to
   the epithet, `_`/`-` separators, and trailing descriptive text
   after the epithet where separable. Trinomials (genus species
   subspecies) are filed names at subspecies rank and are kept as
   their own class. Filings marked `sp.`, `cf.` or `aff.` are
   **PROVISIONAL** identifications — counted, resolved at genus
   level where possible, but excluded from the firm-name
   denominator and reported separately. Genus-only and
   epithet-only fragments are **FRAGMENTARY** — reported, not
   resolved as names.
3. **Dedup rule:** the unit is the unique file (URL) in the CDX
   list; exact duplicates across piles — same normalised basename
   AND same CDX length — are counted once, with the dedup count
   stated. Takes (`_1`, `_2`, glued digits) are distinct
   recordings, not duplicates.

## Registered classification (per unique filed name)

From the GBIF match result for the filed name:

- **UNCHANGED** — match status ACCEPTED and the accepted canonical
  name is identical to the filed name (species rank; for a filed
  trinomial, the trinomial itself still accepted at subspecies
  rank, or its species name unchanged AND subspecies still
  recognised — otherwise see SPLIT).
- **MOVED** — the taxon is the same but the genus changed: the
  accepted name has the same species epithet under a different
  genus (recombination, e.g. recording-era catch-all genera
  dismantled). Includes trinomials whose subspecies was elevated
  within a new genus only if epithet path is unambiguous —
  otherwise SPLIT.
- **SYNONYM** — the filed name is a junior synonym: the accepted
  name differs in epithet (same or different genus), the taxon
  concept carried over (match status SYNONYM, or match returns a
  different accepted species with no split evidence).
- **SPLIT (REQUIRES-LOCALITY)** — the filed name's taxon has been
  partitioned into two or more currently accepted species such
  that which one a recording belongs to depends on its locality /
  voucher, not on the name. A name is SPLIT-flagged if ANY of:
  (a) it is a filed trinomial whose subspecies is now an accepted
  species distinct from the filed species; (b) it resolves
  ACCEPTED but appears on the project's split-complex screen —
  a documented list, built from the taxonomic literature for the
  faunas present (Iberian/European, Malagasy, Neotropical),
  where each entry names the splitting revision and the daughter
  species; (c) the backbone returns multiple equally-plausible
  accepted matches in different daughter taxa. SPLIT overrides
  UNCHANGED/MOVED for that name. **The screen is a lower bound:**
  absence of a flag does not prove a concept was never narrowed.
- **UNRESOLVED** — no backbone match at species level (including
  non-anuran names in the pile: cicadas, birds, mammals — the
  pile is mostly but not exclusively anuran; non-anuran matches
  in another class are reported as NON-ANURAN, not UNRESOLVED).

Recordings inherit their filed name's class. Headline counts are
given on **firm species-named recordings** (PROVISIONAL and
FRAGMENTARY reported alongside, never folded in silently).

## Predictions (scorecard — falsifiable, thresholds fixed)

- **P1 — churn is large.** ≥ 35% of unique firm filed names are
  no longer the accepted name for the same taxon
  (MOVED + SYNONYM, excluding SPLIT-flagged).
- **P2 — moves dominate.** MOVED is the largest change category
  and accounts for ≥ 60% of all name changes
  (MOVED / (MOVED + SYNONYM)).
- **P3 — splits are material but bounded.** SPLIT-flagged
  recordings are ≥ 5% and ≤ 20% of firm species-named recordings.
- **P4 — unchanged is a majority of names but not a landslide.**
  UNCHANGED share of unique firm filed names lies between 40%
  and 65%.
- **P5 — one catch-all donor genus dominates.** A single
  recording-era genus (candidates: Bufo, Hyla, Eleutherodactylus,
  Mantidactylus, Rana) accounts for ≥ 15% of all changed
  recordings (MOVED + SYNONYM + SPLIT recordings).
- **P6 — trinomials churn harder.** The change rate
  (MOVED + SYNONYM + SPLIT) among filed trinomials exceeds the
  rate among filed binomials by ≥ 15 percentage points.

## Registered risks / honesty rules

- GBIF's match is fuzzy: every match with confidence < 90 or
  matchType FUZZY is hand-checked before it is counted, and the
  hand-check count is reported. Misspellings in filenames are
  corrected only where the intended name is unambiguous, and
  each correction is logged.
- Filename locality: most /sonidos filenames carry no locality.
  The Fonozoo catalogue's per-recording pages (species, recordist,
  Fonozoo Ref.) are reachable only through the live site, which
  403-stubs our client; unless a catalogue record is actually
  retrieved for a recording, SPLIT recordings stay flagged —
  never guessed to a daughter species.
- If the backbone or inventory proves unreachable, the project
  reports the block instead of estimating.
