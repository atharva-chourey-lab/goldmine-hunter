# Transcription — methods and error structure

Output: `transcription.csv` (210 rows). Source:
`data/smc-scar-sheets-all-10-13.pdf`, rendered at 200 dpi
(`pages/p-01.png` … `p-22.png`; page 1 is the KEY). The PDF's
text layer is negligible (2,537 characters — captions only);
all content was read visually from the page images.

## Result first

**210 entries exactly** — 21 catalogue pages × 10, no page
deviating from the 2×5 layout. 209 entries carry a BS ID
number; the sole exception is Nick (p16 s8), whose sketch
carries no legible number anywhere (both passes, and a third
targeted read, agree). Per the pre-registration (rule 2) Nick
is transcribed but excluded from joined statistics. Three
entries carry no year code as written: B.J., Chekov, Micanopy.
No BS ID and no name is duplicated anywhere in the set.

## Double-pass protocol

As registered: two independent visual reads of every entry
(passes A and B, produced by different readers working only
from the images), disagreements reconciled against the page
image and logged (`hidden/reconciliation_log.txt`, 42
adjudicated entries + the ±1 count resolutions).

Agreement structure, stated plainly:

- **Identity fields (name, BS ID, size, sex, year code):
  near-perfect agreement.** Across 210 entries the passes
  disagreed on *no* ID number, *no* size, *no* sex marker and
  *no* year code. The only name disagreements were 5 spacing
  variants (ChadII/Chad II etc.); spaced forms adopted.
- **Scar counts: the soft field.** 116/210 entries agreed
  exactly; 79 differed, almost all by ±1 (what counts as one
  "feature" when a strike leaves a fading series is a
  judgement call). 42 entries were adjudicated by a third
  read of cropped, labelled sketch images: all cases where
  the passes implied different scar-load groups, all
  section-missing and flipper disagreements, and all count
  differences ≥3.
- **Remaining ±1 disagreements** (same scar-load group under
  both readings) were resolved by rule: take the count from
  the pass with the higher stated confidence for that entry;
  on a tie take the lower count. Every resolution is in the
  reconciliation log.

## Counting rules (fixed before reconciliation)

- A scar **feature** = a spatially discrete mark; a tight
  linear series/cluster from one strike (propeller rake,
  column of cuts) counts as 1 feature.
- **Freeze brands are not scars.** Alphanumeric brands
  (A1/A3, A5, A6, A7, R5, 35, 47, 95 …) were excluded from
  scar counts by both passes; brand-only animals (Amber,
  Annie, Bock, Doom, Rocket, Turtle, Una …) have scar
  counts of 0–2 and sit in MID, never LOW — LOW requires
  exactly one *scar*.
- **Section-missing adjudication rule:** scored 1 only when
  a filled black region interrupts the fluke outline itself
  (a missing chunk, as drawn in the KEY) — not for black
  marks sitting on an intact outline. Rim triangles/wedges
  that scallop the edge were scored 1 (e.g. Nato, Nick,
  Nyx, Wanda); rim ticks on an intact outline were scored
  0 (e.g. Broz, Doc, Eris, Flash). This was the single most
  contested field (25 pass disagreements) and the rule is
  stated here so the grouping can be re-run under the
  opposite convention: doing so moves section-missing
  prevalence from 24/210 (11%) to at most 49/210 (23%) and
  does not change any identity field.
- Flipper damage: 1 only when the drawn flipper itself
  bears marks (7 entries in the final table).

## Cross-validation against the companion adoptee sheet

The companion set (`data/smc-scarsheet-mail.pdf`, 2016) was
transcribed separately (`hidden/adoptee_companion_read.csv`,
21 unique animals). 19 of the 21 appear in the 2013
catalogue; **BS IDs and first-ID years agree for 18 of 19**
— the exception is Nick (no ID on the catalogue sketch;
companion gives BS1, noted but *not* imported, per
registered rule 2). "Lilly" (catalogue) = "Lily"
(companion), BS4/1974 in both. Elaine (BS72) and Howie
(BS14) are absent from the 2013 Practical catalogue —
consistent with the sheet's own drop rules, not a
transcription miss (all 210 slots were read twice; the
alphabetical E and H pages contain no such entries).

## Confidence summary (final table)

- high: 141 entries — both passes high, no adjudication
  needed on any field that affects grouping.
- medium: 67 — an adjudicated scar field, or one pass
  medium (illegible year: Icarus; overwritten ID: Plum,
  best read 674; overwritten years: Rollo, Snorty).
- low: 2 — Nick (no ID) and Icarus (year illegible in both
  passes; recorded as 06/2006, best reading).

Error risk, honestly: names/IDs/years — the fields the join
and the cohort tests rest on — carry the lowest risk (zero
pass disagreement, 18/19 external cross-check). Scar
counts carry real judgement noise (±1 on ~38% of entries
before adjudication); the scar-load analysis (P3) is
therefore run on groups (HIGH/MID/LOW) rather than raw
counts, and group membership was the explicit target of
every adjudication. One process note: a transcription
worker reported finding a stray draft script from another
pass in /tmp *after* completing its own reads, stated it
did not use it, and its readings differ from that draft in
multiple places — the passes are treated as independent,
with this disclosed.
