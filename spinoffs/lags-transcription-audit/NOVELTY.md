# Novelty scrub — the full-LAGS transcription audit (2026-11-18)

**The set (Campaign 10 GOLD):** the Linguistic Atlas Project's
loose file pile on its former host institution's site,
`lap.uga.edu/Projects/` — a live directory tree of 23 project
folders. Inside LAGS (Linguistic Atlas of the Gulf States,
914 interviews, 1968–83): **1,082 informant folders** counted
from the live Speakers index, each holding per-informant
transcription files (.xml + .xls/.xlsx), a biography text, and
an Audio/ tree of tape folders whose files are
topic-segmented MP3s with a per-tape meta.txt. Sample-verified
in Campaign 10 (xlsx / xml / mp3 / meta.txt / full-corpus txt,
md5s in `goldmine-hunter/outputs/verify10-*.json`).

## What is already published / deposited (the narrowing)

- **The published LAGS atlas** (Pederson et al.) — the product
  these interviews were collected for; it prints responses, it
  does not audit the transcriptions against the audio.
- **DASS (2012)** — a 64-informant sample of LAGS, distributed
  as an LDC catalogue release (LDC2016S05 documentation).
- **DASS2019 (2019, NSF)** — the same 64 informants, manually
  transcribed and time-aligned; 344 hours. Served from the
  same UGA pile (61 speaker folders + Full_Corpus txt/xml
  counted and sampled in Campaign 10).
- **DASS2019_NLP (LREC 2026)** — a cleaned, curated version of
  DASS2019 plus six Whisper ASR models fine-tuned on it. This
  **closes the 64-informant seam**: for those informants, a
  modern re-transcription comparison now exists.
- **UK successor** — LAP moved to the University of Kentucky
  in 2018; UK's pages say materials are being transferred and
  a LAP website is "forthcoming". No UK file archive of the
  full pile was found live at scrub time.

## What has NOT been done (the open seam)

No publication, dataset, or treatment found that audits the
**full** LAGS pile — the ~850 informants outside the curated
64 — name-by-name / file-by-file: whether every informant's
audio survives complete beside its transcription, and whether
the original field transcriptions (the .xml/.xls layer the
atlas was built from) agree with the surviving audio when
re-heard by a modern, non-fine-tuned ASR ruler. The pile's
own structure (one folder per informant, audio + transcription
+ biography side by side) is exactly the comparable-set shape
the comparison needs, and it exists only as loose files on
the old site.

**Verdict: NARROWED BUT OPEN.** The claim survives only in
its full-pile form: *the first complete transcription-vs-audio
audit of the LAGS informant pile beyond the curated
DASS/DASS2019 sample.* Any write-up must state the narrowing
plainly — DASS2019_NLP owns the 64-informant seam.
