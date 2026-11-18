# Pre-registration — LAGS full-pile transcription-vs-audio audit

*Registered 2026-11-18, after Campaign 10's verification and
the novelty scrub (`NOVELTY.md`), BEFORE any informant beyond
the Campaign-10 samples (INF001) is resolved or compared.
Nothing below may be revised after seeing comparison data;
amendments require their own dated commit before the affected
run.*

## The set and the denominator

- Source: `https://www.lap.uga.edu/Projects/LAGS/Speakers/` —
  1,082 informant folders counted from the live index on
  2026-11-18. The folder count is NOT assumed to equal the
  published interview count (914): variant folders (e.g.
  INF011A) are counted and reported as their own line before
  any rate is computed.
- Denominator: informant folders holding BOTH an Audio/ tree
  with ≥1 MP3 AND a transcription file (.xml). Folders missing
  either are counted as completeness failures, never dropped
  silently.

## The comparison (one sentence)

For every informant in the denominator, re-transcribe the
surviving audio with a modern ASR ruler and measure its
agreement with the original per-informant transcription file
the LAGS atlas was built from — across the whole pile, not
the curated 64-informant sample.

## Ruler discipline

- ASR ruler: a general Whisper large-v3 model, **not** any
  DASS-fine-tuned variant (the fine-tuned models were trained
  on DASS2019 — using them on the pile would grade the
  transcriptions with a ruler fitted to a subset of them).
- Calibration first: the ruler is run on the DASS2019
  informants, whose manual time-aligned transcriptions are
  the anchor. The pile-wide run proceeds only if the ruler's
  agreement on the anchor subset is reported alongside every
  pile number; the anchor agreement is the measurement's
  error bar, not a result.

## Registered predictions

- **P1 (completeness):** ≥90% of the 1,082 folders hold both
  audio and a transcription file. Below 90%, the headline
  becomes the completeness census itself.
- **P2 (calibration):** on the DASS2019-overlap informants,
  ASR-vs-original word agreement will be ≥85% — if it is not,
  the ruler is declared unfit and no pile-wide fidelity claim
  is made (the census in P1/P3 still stands).
- **P3 (the gap):** outside the curated sample, agreement
  will run measurably below the anchor subset (≥3 points),
  because the non-sample transcriptions were never re-checked
  by the DASS/DASS2019 curation passes.
- **P4 (concentration):** disagreement will concentrate by
  questionnaire topic segment (the MP3s are topic-segmented;
  segments are the unit), not distribute uniformly — reported
  as the top-5 segments' share of total disagreement.

## Anchor

DASS2019's manual, time-aligned transcriptions (64 informants,
344 h) for calibration; the published LAGS atlas as the
downstream product whose inputs are being audited.

## Exclusions and honesty rules

- DASS/DASS2019 informants are reported separately in every
  table (they are the curated subset, not pile evidence).
- Split/variant folders (INF011A class) are never merged into
  their parent informant.
- No bulk download is authorised by this registration beyond
  what the comparison run itself needs, staged informant by
  informant; the Campaign-10 samples stay the only files held
  until the run is separately commissioned.
