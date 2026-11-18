# Results — Blue Spring Scar-Sheet Persistence Audit

*Pre-registration committed 2026-11-18 (795ac16) before any transcription or join.
Predictions and thresholds below are exactly as registered; nothing was revised after
seeing data.*

## Headline

**The sheet's drop rules cannot be tested for most of the catalogue from public data —
and for every animal the public record *can* see, the rules are far too pessimistic.**

The public ruler reaches only **45 of 209** ID-bearing sheet animals (21.5%), so the
pre-registered fallback (rule 6, <40% coverage) fires: what follows is a **coverage
audit plus a non-representative case series**, not a population estimate. Within that
visible subset, persistence is long: 34 of 45 joined animals were publicly recorded
again after 2013, the median last record is **2025 — twelve years after the April-2013
freeze** — and animals first identified in the 1970s (Lilly, BS4, 1974; Merlin, BS19,
1970) were still being individually recognised in the 2025–26 season. A 10-year
recognised-animal drop rule applied from the freeze would have retired both in 2023.
But the silent 78.5% is uninformative, not dead: the public ruler is a genealogy
booklet plus adoptee updates, not a sighting census, and absence from it proves
nothing about survival or recognisability. The decisive join sits in MIPS, which is
researcher-only — the formal request draft (`MIPS-REQUEST-DRAFT.md`) is therefore the
main path this audit produces.

## The two datasets

**The frozen catalogue (transcription).** All 22 pages of Hartley's April-2013
"Practical Scar Sheet" set were transcribed by two independent visual passes with
adjudication of contested entries (`transcription.csv`, `TRANSCRIPTION-METHODS.md`):
**210 entries, 209 with a BS ID** (sole exception: Nick, no legible ID). Scar groups
as registered (from the sheet alone): HIGH 151, MID 39, LOW 20. Transcription
confidence: high 141, medium 67, low 2. The two passes never disagreed on an ID
number, size, sex, or year code; scar counts disagreed by ±1 on 79 entries and
section-missing calls on 25, all resolved by stated rules with a logged sensitivity
(section-missing prevalence 11–23% depending on convention — group assignments use
the adjudicated rule throughout).

**The public ruler.** 165 sourced rows covering 91 distinct individuals
(`ruler.csv`), every row read from a named source: Hartley's *Genealogies of the
Blue Spring Manatees* (newest edition; booklet footer dated 11/2023) and five Save
the Manatee Club articles/updates (Jan 2025 – Feb 2026). Events: resightings 61,
calves born to identified mothers 51, deaths 37, last-seen statements 13, births 3.
The genealogy covers matriarchy members only, and the SMC updates cover adoptees —
the ruler is structurally biased toward named resident females and famous adoptees,
which is precisely the bias the joined subset shows (below).

## Scorecard (as registered)

| # | Prediction | Verdict | Numbers |
|---|---|---|---|
| P1 | ≥60% of transcribed ID-bearing individuals have ≥1 public post-2013 outcome record | **FAIL** | 45/209 = **21.5%** |
| P2 | Among post-2013-resighted animals, median last-record year ≥2019 | **PASS** (joined subset) | median **2025** (n=34) |
| P3 | HIGH-group resighting rate exceeds LOW by ≥20 points | **FAIL** | HIGH 69.7% (23/33) vs LOW 66.7% (2/3); diff **+3.0 pts**; MID 100% (9/9) |
| P4 | ≥15% of joined animals have a known death in the ruler by its latest edition | **PASS** | 11/45 = **24.4%** (deaths in 2014×2, 2015×2, 2016×2, 2017, 2020, 2022, 2023, 2025) |
| P5 | Pre-1990 first-ID cohort resighting ≥15 pts below the 2000–2013 cohort | **FAIL** (wrong direction) | pre-1990 **86.7%** (13/15) vs 2000–13 **82.4%** (14/17); diff **−4.3 pts** |
| P6 | ≥25% of joined animals with year-by-year histories show a ≥5-year unrecorded gap followed by a later record | **VOID** (as registered) | only **5** joined animals have ≥4 distinct presence years (<30 required); none of the 5 shows a bridged ≥5-year gap |

**Scorecard: 2 pass, 3 fail, 1 void** — all scored on the joined subset under the
fallback rule, i.e. as a case series. 17 of the 45 joins are additionally confirmed
by ID number via the companion adoptee sheet; the rest are name joins within
Hartley's own naming system (no name is duplicated in the sheet set). No join rests
on a birth row alone, and no joined animal carries an impossible (pre-2014) death.

## Re-identifiability in the joined subset

- **Persistence curve** (share of the 45 joined animals with a public record in or
  after year *t*): 2014: 75.6% → 2017: 62.2% → 2020: 60.0% → 2023: 48.9% → 2025:
  44.4%. With known deaths treated as exits rather than identification failures
  (registered rule 4, second form): 2014: 91.1% → 2020: 78.9% → 2025: 60.0%. The
  2026 point (22.2% / 29.4%) is censored — the ruler's latest source is a February
  2026 update covering a partial season — and should not be read as a drop.
- **Duration past the freeze** (last record year − 2013, n=34 resighted): median
  **12 years**, max 13. The distribution is bimodal: an early-exit bloc (≤4 years:
  7 animals) and a large bloc still recorded in 2025–26 (12–13 years: 20 animals),
  with few in between.
- **Span since first identification** (last record − year first ID'd): median
  **28 years**, max **56 years** (Merlin, first ID'd 1970, recorded Jan 2026).
- **Sensitivity:** counting "last seen" statements dated ≥2014 as presence (Lucille
  2022, Michelle 2014) raises resighted to 36/45 and HIGH to 25/33; no verdict
  changes.

## Five worked examples (sheet → post-2013 record)

1. **Lilly (BS4, first ID'd 1974, HIGH — 7 marks).** The catalogue's "Lilly" is the
   genealogy's and adoptee programme's "Lily" (BS4/1974 in both the sheet set and
   the companion adoptee sheet — an ID-confirmed join). SMC updates record her in
   the November 2024, January 2025 and January 2026 aggregations: individually
   recognised **52 years after first identification**, 13 years past the freeze.
2. **Merlin (BS19, first ID'd 1970, HIGH — 5 marks).** ID-confirmed join. SMC
   season updates record him in Dec 2024, through the 2024–25 season, and on
   1 and 21 January 2026 — the longest first-ID-to-last-record span in the set
   (56 years).
3. **Ann (BS189, first ID'd 1996, HIGH — 5 marks).** The genealogy records calves
   in 2014, 2017, 2021 and 2023: a breeding resident still being identified a
   decade after the freeze, on the strength of the same scar pattern the 2013
   sheet froze.
4. **Amber (BS286, born 2000, MID — brand/pattern animal, 0 counted scars).**
   Calved in 2015 (with her twin Amanda, as in 2011 and 2013), then died of
   unknown causes in February 2020: a complete post-2013 arc — resighted, then a
   known death — and a MID-group animal, which is part of why P3's scar-load
   gradient fails.
5. **Calista (BS260, first ID'd 1999, HIGH — 4 marks).** Never resighted in the
   ruler; found dead of unknown causes in 2014. One of 7 joined animals whose only
   post-2013 outcome is a death record, and one of 11 known deaths overall (24.4%
   of joined — P4).

## What the drop rules verdict actually is

The Practical sheet's 3–5-year drop and the 10-year recognised-animal drop are
*visibility* rules: they retire animals a field team stops seeing. Tested as
predictions about re-identifiability, they fail in both directions at once in the
public data. For visible animals they are far too short — recognised animals
routinely remain identifiable 12+ years past the freeze, scar load does not predict
who persists (P3), and the oldest cohort persists best (P5, wrong direction) —
because the public ruler sees exactly the site-faithful residents the rules were
designed to keep. For the other 164 animals the rules are simply untested: public
silence mixes death, emigration, missed seasons and non-publication in unknown
proportions. **The honest headline is a coverage result, not a survival result:
a hand-drawn catalogue frozen in 2013 can still be joined to a living public record
for a fifth of its animals a decade later — and resolving the rest requires the
MIPS join this project now requests.**

## Limits

- The ruler is not a census. Genealogy coverage requires ≥3-generation matriarchies;
  SMC coverage requires adoptee status or newsworthiness. All rates are conditional
  on joining and are labelled a case series per the fallback rule.
- Presence years from the genealogy are *notable-event* years (calves, deaths), not
  sighting logs; the persistence curve is therefore a floor, and P6's year-by-year
  test could not be run (void, as registered).
- Scar groups derive from sketches read by eye; the ±1 count error and the
  section-missing convention (11–23% prevalence range) are documented in
  `TRANSCRIPTION-METHODS.md`. Group-level conclusions (P3) are robust to the count
  error only at the HIGH/MID/LOW granularity used.
- One site, one freeze date, one (exceptional) observer's naming system. Nothing
  here generalises to other manatee aggregations without their own frozen sets.

*Analysis code: `hidden/analyse.py`; full join table: `hidden/analysis.json`;
ruler build notes: `hidden/ruler_notes.md`.*
