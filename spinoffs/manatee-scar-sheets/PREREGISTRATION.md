# Manatee Scar Sheets — pre-registration

Written and git-committed 2026-11-18, BEFORE any transcription
or joining is run for this project. State at registration: the
set was recovered and sample-verified by Goldmine Hunter
Campaign 8 (provenance and evidence in
`~/workspace/goldmine-hunter/SHORTLIST-CAMPAIGN8-MAMMAL2-2026-11-18.md`);
the novelty scrub is done (`NOVELTY.md`, same commit). Three
pages of the sheet PDF (key, page 3, page 22) were visually
inspected during campaign verification — that inspection is
the only contact with the set's contents so far. No entry has
been transcribed, counted exactly, or joined to any record.

## The surviving claim (from the scrub)

The first persistence audit of a hand-drawn scar-ID
catalogue: Hartley's frozen April-2013 Blue Spring Practical
Scar Sheet set, transcribed and joined to post-2013 records,
measuring the re-identifiability curve of sketch-based scar
IDs and testing the sheet's own drop rules (3–5-year
Practical drop; 10-year drop for recognised animals) as
predictions. Priors that narrowed the claim: Langtimm et al.
(1998) and Reid et al. (1991) used the photographic ID
system for survival/distribution science; neither audits
the sketch system.

## The set

- `data/smc-scar-sheets-all-10-13.pdf` — the frozen set:
  1,599,152 B, md5 `79e2067c1ad29b6ca34227889141b50d`,
  22 pages (key + ~21 catalogue pages, ~10 animals/page,
  **≈200 individuals, exact count to be fixed by
  transcription and reported as the first result**). Each
  entry: tail sketch with scar marks in the key's vocabulary
  (white / healed-grey / cut / section-missing), flipper
  drawn only to show damage, size class (S/M/L), ID number
  (BS / Blue Spring series), name, year first ID'd (with the
  sheet's conventions: 70 = Blue Spring 1970, R81 = St Johns
  River 1981, B89 = born 1989, Y93 = first came as nursing
  yearling, etc.).
- `data/smc-scarsheet-mail.pdf` — companion adoptee sheet
  set (2016): 481,180 B, md5
  `c2abc9b134530d20e42aa2dc85c8783d`, 2 pages. Secondary;
  used only for the adoptee-subset checks.

## Outcome rulers (priority order, fixed)

1. **Public ruler (primary):** Hartley's *Genealogies of
   Blue Spring Manatees* (SMC, openly served) — life
   histories, last-seen years, deaths, calves for named
   individuals; SMC's published adoptee updates; FWC's
   published photo-ID material. Coverage bias is expected
   and is itself reported: the public ruler covers named,
   long-resident animals better than transients.
2. **MIPS (secondary, by request only):** the FWC/FWRI
   Manatee Individual Photo-ID System is researcher-only.
   A formal data request may be filed; the project does
   **not** assume it succeeds. If it fails or is unanswered,
   all results are reported as public-ruler results with
   their coverage stated — never silently upgraded.

## Registered method rules

1. Transcription is double-pass (two independent reads of
   every sheet entry; disagreements reconciled against the
   page image and logged). Fields per entry: page, name,
   ID number (as written), size class, year first ID'd
   (decoded per the key, raw string kept), scar inventory
   (count of distinct marks; presence of section-missing;
   presence of flipper damage), sex if marked.
2. The join key is ID number first, name second; name-only
   matches are flagged as weak joins and reported
   separately. Animals whose sheet entry lacks an ID number
   are transcribed but excluded from joined statistics.
3. Outcomes per joined animal, from the public ruler:
   resighted post-2013 (any dated record), last-record
   year, known death (with year), calf records. Aggregate
   roll-call counts (e.g. "400+ identified per winter") are
   **not** individual outcomes and are never used as such.
4. Persistence is measured from 2013 (the frozen edition):
   an animal is "persisting at year t" if it has any record
   in or after year t. The re-identifiability curve is the
   share of the joined set persisting at each t = 2014…
   latest public-ruler year, with known deaths treated as
   exits (not as identification failures) and reported both
   ways.
5. Scar-load groups are fixed from the 2013 sheet alone,
   before outcomes are looked up: HIGH = section-missing
   OR ≥3 distinct marks; LOW = exactly 1 mark AND no
   section-missing; MID = the rest.
6. If the public ruler joins < 40% of the transcribed set,
   the registered fallback fires: the project reports a
   coverage audit + the joined-subset results labelled as a
   non-representative case series, and the MIPS request
   becomes the main path. No silent re-scoping.

## Predictions (scorecard — falsifiable, thresholds fixed)

- **P1 — the set is joinable at scale.** ≥ 60% of
  transcribed, ID-bearing sheet individuals have at least
  one public post-2013 outcome record (resighting, death,
  or life-history entry).
- **P2 — the 3–5-year drop rule under-predicts persistence.**
  Among animals resighted post-2013, the median
  last-record year is ≥ 2019 (i.e. the typical persisting
  animal was still identifiable ≥ 6 years after the frozen
  edition — beyond the Practical sheet's drop window).
- **P3 — persistence is scar-load dependent.** The
  post-2013 resighting rate of the HIGH group exceeds the
  LOW group's by ≥ 20 percentage points.
- **P4 — the set is old enough to read mortality.** ≥ 15%
  of joined animals have a known death recorded in the
  public ruler by its latest edition.
- **P5 — cohort senescence.** Animals first ID'd before
  1990 have a post-2013 resighting rate ≥ 15 points below
  animals first ID'd in 2000–2013.
- **P6 — long gaps get bridged (conditional).** Among
  joined animals whose public life histories give
  year-by-year sighting records, ≥ 25% show a gap of ≥ 5
  consecutive unrecorded years followed by a later record —
  the behaviour the 10-year drop rule exists for. **P6 is
  void if fewer than 30 joined animals have year-by-year
  histories**; voiding is reported, not scored as a fail.

## Registered risks / honesty rules

- The public ruler is biased toward named, resident,
  adoptee animals; every headline number carries its join
  coverage beside it. A result that holds only inside the
  public ruler is reported as exactly that.
- The sheet count (≈200) is an estimate from page
  structure until transcription fixes it; if transcription
  finds materially fewer (< 120 ID-bearing entries), P1's
  denominator shrinks accordingly and the change is
  reported in RESULTS, not edited here.
- Hartley's living system continues and SMC/FWC hold the
  authoritative records; this project audits a frozen
  public snapshot and claims nothing about the living
  archive's quality.
- If persistence turns out near-total (the sketches simply
  work for decades), the headline is that positive —
  reported plainly, in the Maddison style.
