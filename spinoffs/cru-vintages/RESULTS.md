# CRU Vintages — results (2026-11-18)

Pre-registration: `PREREGISTRATION.md`, git commit `9e1606f`, frozen
before any data download. Novelty scrub: `NOVELTY.md` (same commit).
Analysis: `scripts/analyse.py` → `results.json` + `revision_series.csv`.
Completion note: the analysis script and downloads were finished in
the originating session; `analyse.py` was run and this report written
in the delivery session, against the frozen registration — no
prediction, threshold or method rule was changed after the run.

## Novelty verdict (from the scrub)

"First comparison of CRUTEM versions" is **dead** — killed by the
release papers themselves: Jones et al. (2012) published an extensive
CRUTEM4-vs-3 comparison, and Osborn et al. (2021) summarised
CRUTEM5-vs-4 ("only slightly modified"). What survived, narrowed but
open: **a uniform revision-geometry accounting of the full 3→4→5
lineage** — all three pairwise steps, decade/period structure and
revision-mass concentration, computed identically for harmonised
global, NH and SH. That is what was run. No stronger "first" is
claimed.

## The set

Nine series, latest minor of each major version, anomalies vs
1961–1990. Verified empirically: every version's own 1961–1990 mean
sits within 0.002–0.008 °C of zero, cross-version differences
< 0.003 °C — no re-baselining triggered (registered rule 4).
CRUTEM3's hosted series ends 2014, so **LCY = 2014** and the
"latest decade" throughout is 2005–2014, the latest decade all
three versions cover. Global is the harmonised (2·NH + SH)/3 —
CRUTEM3's published global used equal hemisphere weights, 4/5 use
land-area weights, so the published-global step mixes a convention
change into the data revision (quantified below).

| File | md5 |
|---|---|
| CRUTEM3-gl.dat | `6b5990670a6f5a982de4c3d43c96afd7` |
| CRUTEM3-nh.dat | `c21ea4693019ab67ffcf551b9694cf1f` |
| CRUTEM3-sh.dat | `0d627cbc3ed410d895237f64f4c671dd` |
| CRUTEM4-gl.dat | `b2f9c92e53ffed302bddb806044b0943` |
| CRUTEM4-nh.dat | `2b0905e7e826c59f654416461ce062cf` |
| CRUTEM4-sh.dat | `1800b9719e95d16e1531488b575d64e3` |
| CRUTEM5.2_gl.txt | `f173baf7ff25dc9b1d269ad6f9401be6` |
| CRUTEM5.2_nh.txt | `1be154b05e4b9fb5583eb2724d44ff08` |
| CRUTEM5.2_sh.txt | `8b8ea3f4b35bb992cc6f55e0d2e80f83` |

Phase 2 (CRU TS) skipped as pre-registered: no light global summary
series exists — per-country files and multi-GB grids only.

## Scorecard — 6 passed, 2 failed

- **P1 PASS — the 4−3 step lives in the recent NH.** Mean NH revision
  2001–2014 = **+0.067 °C** vs +0.001 °C over 1951–2000.
- **P2 PASS — the 4−3 step cools the early record.** Mean harmonised-GL
  revision 1850–1900 = **−0.105 °C** (threshold was ≤ −0.03).
- **P3 PASS — the 5−4 step is small everywhere.** Harmonised GL mean
  |revision| 0.015 °C, largest single year 0.143 °C (1860).
- **P4 PASS — endpoint warming grows at every step.** 2005–2014 minus
  1850–1900, harmonised GL: **V3 1.089 → V4 1.263 → V5 1.319 °C**;
  V5−V3 = +0.230 °C (threshold ≥ +0.10).
- **P5 PASS — revisions dodge the well-observed middle.** Of the total
  |5−3| mass (harmonised GL): 1850–1900 holds **68.4%**, 1951–2000
  only **7.9%**, 2001–2014 11.4%.
- **P6 FAIL — the NH is NOT revised more than the SH; the SH is
  revised more, both steps.** Mean |revision| 4−3: SH 0.098 vs NH
  0.042 °C; 5−4: SH 0.036 vs NH 0.018 °C. The prediction had the
  hemispheres backwards — the sparse-coverage SH early record is
  where the big revisions live (SH 1870s decade mean revision −0.39 °C
  in the 4−3 step; single-year SH 1850 revision +0.87 °C, a
  few-station year, flagged not leaned on).
- **P7 PASS — each step is quieter than the last**, all three regions
  (harmonised GL mean |revision|: 4−3 0.052 → 5−4 0.015 °C).
- **P8 FAIL, by a hair — trend revision is not quite the registered
  recent-era size.** 1979–2014 trend change (V5−V3, harmonised GL) =
  **+0.029 °C/decade** vs the ≥ +0.03 threshold — a 0.001 miss, scored
  fail as registered. The other half held: 1901–1950 trend change
  −0.007 °C/decade, inside ±0.02.

## The pattern

The CRUTEM lineage revised the record mostly by **cooling the
nineteenth century**, not by warming the present:

- The 5−3 revision (harmonised GL) averages **−0.131 °C over
  1850–1900** (SH: −0.221 °C) against **+0.065 °C over 2001–2014** and
  −0.001 °C over 1951–2000. Decade means tell the same story: 1850s
  −0.24, 1860s −0.17, 1870s −0.18 °C, fading to ~0.000 by the 1960s–
  1990s, then +0.05 (2000s) and +0.09 (2010–2014).
- Because the past cooled more than the present warmed, the
  1850–1900 period's own trend **flips sign** across the lineage:
  −0.035 °C/decade (V3) → +0.025 °C/decade (V5), while the
  1951–2000 trend is essentially untouched (0.132 → 0.134).
- The endpoint-warming growth (+0.230 °C, V3→V5) is therefore mostly
  a *baseline* effect — the early reference period moved down —
  plus a smaller recent warming (+0.065 °C period mean).
- **Convention effect, separated as registered:** of the
  *published-global* 4−3 revision over 2001–2014, **+0.073 °C is the
  hemisphere-weighting change alone** (published minus harmonised) —
  i.e. a large share of the headline "CRUTEM4 warmed the recent
  global record" is arithmetic convention, not new station data.
  The 5−4 convention effect is ~0.000.
- Mirror image of Maddison: Maddison revised the recent and the
  national, never the ancient; **CRU revised the ancient and the
  sparse, barely touching the well-observed middle.**

One-liner: *Three versions of the land record agree about the
twentieth century almost to the third decimal — nearly everything
they ever changed their minds about happened before 1900, in the
hemisphere with the fewest thermometers.*
