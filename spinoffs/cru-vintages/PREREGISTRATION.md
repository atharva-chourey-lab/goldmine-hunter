# CRU Vintages — pre-registration

Written and git-committed 2026-11-18, BEFORE any series file is
downloaded or parsed for this project. State at registration: the
novelty scrub is done (`NOVELTY.md`, same commit); the only data
values in hand are Campaign 5's sample of `CRUTEM3-gl.dat`
(30,855 B, md5 `6b5990670a6f5a982de4c3d43c96afd7`) and file-existence
HEAD probes. Disclosure: the CRUTEM5.2 global page text was fetched
by the browser tool while locating the file URL; no value from it
(or any series) has been parsed, averaged or differenced.

## The surviving claim (from the scrub)

A uniform revision-geometry accounting of the full CRUTEM 3→4→5
lineage — all three pairwise revision series (4−3, 5−4, 5−3),
decade means, period-trend revisions and revision-mass
concentration, computed identically for global, NH and SH annual
land series. The pairwise steps individually are already documented
by the release papers (Jones et al. 2012 for 4−3; Osborn et al. 2021
for 5−4); the chained, uniform geometry is the open seam. No
stronger "first" is claimed.

## The set

Nine text series, latest minor of each major version, all in CRU
format (year, 12 monthly anomalies, annual anomaly; coverage row
follows each year row), anomalies vs **1961–1990** in all three
versions (Brohan et al. 2006; Jones et al. 2012; Osborn et al. 2021;
CRU FAQ) — to be verified empirically from the files' own
1961–1990 means and reported, not assumed:

- CRUTEM3: `cru/data/crutem3/CRUTEM3-{gl,nh,sh}.dat`
- CRUTEM4: `cru/data/crutem4/CRUTEM4-{gl,nh,sh}.dat`
- CRUTEM5: `cru/data/temperature/CRUTEM5.2_{gl,nh,sh}.txt` (v5.2.0.0)

## Registered method rules

1. **Global-averaging convention changed between versions** —
   CRUTEM3's published global is the equal-weighted mean of the
   hemispheres; CRUTEM4/5 use land-area weighting (CRU FAQ: NH:SH
   weights 2:1). Therefore the **primary global series is a
   harmonised global, (2·NH + SH)/3, computed identically from each
   version's own hemispheric series**. The as-published global files
   are analysed secondarily and the convention effect reported
   (published-GL revision minus harmonised-GL revision). Hemispheric
   series are convention-clean and co-primary.
2. Pairwise alignment on common years only; a year enters a step's
   statistics only if both versions carry a non-missing annual value
   (missing = −9.999 sentinel or absent). LCY = latest common year
   across all three versions.
3. Periods (fixed in advance): 1850–1900, 1901–1950, 1951–2000,
   2001–LCY. Trends are OLS slopes in °C/decade. Endpoint warming =
   mean of the latest complete common decade minus mean 1850–1900.
4. No re-baselining is expected (all versions are 1961–1990
   anomalies); if the files' 1961–1990 means differ across versions
   by >0.02 °C for any series, that fact is reported and a
   common-period (1961–1990) re-baselined copy is used for
   differencing, with the change declared.
5. Phase 2 (CRU TS) is OUT unless a comparably light global/regional
   summary series exists. Known state at registration: CRU TS offers
   per-country text files and multi-GB grids, no light global
   summary — Phase 2 is expected to be skipped, with the reason
   stated in RESULTS.md.

## Predictions (scorecard — falsifiable, thresholds fixed)

- **P1 — the 4−3 step lives in the recent NH.** Mean NH revision
  (4−3) over 2001–LCY is ≥ +0.05 °C, and at least twice the mean NH
  revision over 1951–2000. (Jones et al. 2012 prior: NH ~+0.1 °C
  since 2001 from added Arctic/Russian stations.)
- **P2 — the 4−3 step cools the early record.** Mean harmonised-GL
  revision (4−3) over 1850–1900 is ≤ −0.03 °C.
- **P3 — the 5−4 step is small everywhere.** Harmonised-GL: mean
  |annual revision| over all common years < 0.05 °C AND the largest
  single-year |revision| < 0.15 °C. (Osborn et al. 2021 prior:
  "only slightly modified".)
- **P4 — endpoint warming grows at every step.** Harmonised-GL
  endpoint warming (latest complete common decade − 1850–1900):
  V5 > V4 > V3, strictly, and V5 − V3 ≥ +0.10 °C.
- **P5 — revisions dodge the well-observed middle.** Of the total
  Σ|5−3| revision mass (harmonised GL), the share falling in
  1951–2000 is < 25%, and the combined share of 1850–1900 plus
  2001–LCY is ≥ 45%.
- **P6 — the NH is revised more than the SH, both steps.** Mean
  |revision| NH > mean |revision| SH for 4−3 AND for 5−4.
- **P7 — each successive step is quieter than the last.** Mean
  |5−4| < mean |4−3| for harmonised GL, NH and SH — all three.
- **P8 — trend revision is a recent-era phenomenon.** Harmonised
  GL: the OLS trend change (V5 trend − V3 trend) over 1979–LCY is
  ≥ +0.03 °C/decade, while over 1901–1950 it lies within
  ±0.02 °C/decade.

## Registered risks / honesty rules

- CRUTEM3's frozen series ends years before CRUTEM5's; all
  cross-version statistics are on common years only — the "latest
  decade" is the latest decade all three versions cover, not the
  latest decade of CRUTEM5 alone.
- CRUTEM5.2 is a moving monthly-updated file; the downloaded copy is
  frozen by md5 in the provenance table and the analysis does not
  silently refresh it.
- If revisions turn out tiny everywhere, the headline is the
  negative — "the lineage barely moved" — reported plainly, in the
  Maddison style.
