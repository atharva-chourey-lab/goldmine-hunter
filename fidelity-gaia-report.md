# Goldmine Hunter — Fidelity Campaign: GAIA CHEMISTRY leg (2026-11-17)

**System:** Gaia DR3 (astrometry + XP spectra; GSP-Phot / GSP-Spec metallicities)
vs local anchor APOGEE DR17 / GALAH DR3 high-resolution spectroscopy.

**Fidelity card (hunter doctrine):**
- RAW: Gaia source catalogue + XP continuous spectra + RVS spectra — the scan
  itself is kept (1.812B sources). Catalogue-level APs are the derived layer.
- UNIT: star — one satellite instrument, one pipeline, 470,759,263 sources
  with `mh_gspphot` (counted live this run, see below).
- LABEL GAP: metallicity labels sit on a *second ruler* — synthetic-spectrum
  fitting of low-resolution XP (GSP-Phot) and RVS (GSP-Spec, published
  deliberately **uncalibrated**) vs high-resolution spectroscopic [Fe/H].
- ANCHOR: APOGEE DR17 (733,901 stars, R≈22,500, H-band) and GALAH DR3
  (588,571 stars, R≈28,000, optical) — independent pipelines, independent
  wavelength regimes, so their mutual systematics are also known (~0.1 dex).

**Provenance (honest classification):** everything in this leg is
**published-by-design** — Gaia Archive, GALAH/Data Central, SDSS are curated
open releases. This is **inventory / comparison gold, NOT a recovery**:
nothing stranded, nothing Wayback-only. The value is the Two Rulers
comparison, exactly as in the cosmology leg.

---

## LANDED (verified by actual data access / sample download today)

### 1. Gaia TAP — barrier-free, works from this VM
- Endpoint `https://gea.esac.esa.int/tap-server/tap/sync` (POST, ADQL, CSV),
  no account, no key. Capabilities URL returned HTTP 200; sync queries
  returned real CSV.
- Live counts run today:
  - `SELECT COUNT(*) FROM gaiadr3.astrophysical_parameters WHERE mh_gspphot IS NOT NULL`
    → **470,759,263**
  - same for `mh_gspspec` → **5,546,177**
- Sample probe verified columns parse: `gaiadr3.gaia_source` (source_id, ra,
  dec, phot_g_mean_mag) and `gaiadr3.astrophysical_parameters` (source_id,
  mh_gspphot, teff_gspphot, logg_gspphot, mh_gspspec, teff_gspspec, …).
- TAP_SCHEMA queries fail for anonymous users (HTTP 500, server-side SQL
  bug) and the DR3 cross-match tables are **not** under the names
  `gaiadr3.apogee_dr17_best_neighbour` / `gaiadr3.galah_dr3_best_neighbour`
  (HTTP 400 "unknown table" ×4 names tried). Workaround used instead: both
  anchor files carry Gaia source IDs internally (below), so no Gaia-side
  cross-match table is needed.

### 2. GALAH DR3 — barrier-free via Data Central range fetch (the working mirror)
- File: `https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits`
  (note: `.fits`, **not** `.fits.gz` — the `.gz` URL 404s).
- Range GET → **HTTP 206**, Content-Range total **873,518,400 B**,
  588,571 rows × 1,484 B/row, 197 columns (header parsed with astropy,
  installed into `tools-venv` this run: astropy 8.0.2).
- Downloaded bytes 0–23,999,999 (24 MB), header NAXIS2 patched in a copy to
  the 16,120 complete rows present → **16,120 GALAH rows parsed for real**,
  including `dr3_source_id` (= Gaia DR3 source_id, column 4), `teff`, `logg`,
  `fe_h`, `alpha_fe`, `flag_sp`, `flag_fe_h`, `ebv`, `ra_dr2/dec_dr2`.
- GALAH sample file: `gold/gaia-chemistry/galah_sample.csv` (16,120 rows).

### 3. The comparable set — measured on the sample, estimated for the full surveys
Sample definition (declared): GALAH **first 16,120 rows in file order**
(file order is observational/sobject order, *not* random — early GALAH
fields, incl. LMC-region stars; first row RA 53.22°, Dec −68.67°). Quality
cut = GALAH's own recommendation: `flag_sp==0 AND flag_fe_h==0`, finite
`fe_h`, `dr3_source_id>0` → **7,698 stars (47.8%)**.

Gaia join (query in §5): all **7,698 / 7,698** quality IDs returned a
`gaiadr3.astrophysical_parameters` row joined to `gaia_source`. Of those:
- **5,834 (75.8%) have `mh_gspphot`**
- **1,834 (23.8%) have `mh_gspspec`**

Scaled to the full GALAH DR3 (588,571 stars) *if* the first-rows sample
were representative (it is not — treat as order-of-magnitude):
quality ≈ 281k stars; quality + mh_gspphot ≈ **213k**; quality +
mh_gspspec ≈ **67k**. That is the Gaia×GALAH comparable set.
For APOGEE: the allStar file itself carries `GAIAEDR3_SOURCE_ID`
(verified in the header parsed in the cosmology leg, 234 columns,
733,901 rows), so the Gaia×APOGEE set is file-internal — Andrae et al.'s
XP training set alone used ~500k APOGEE stars, i.e. the APOGEE comparable
set is larger and giant-richer than GALAH's.

### 4. FIRST CONTRAST — computed today (script + JSON in bundle)
`gold/gaia-chemistry/first_contrast.py` → `first_contrast_results.json`.
Differences are **Gaia [M/H] − GALAH [Fe/H]**, medians, on the sample above.
Declared mismatches: (a) [M/H] ≠ [Fe/H] — for α-enhanced stars [M/H]
exceeds [Fe/H] by ≲ +0.1–0.3 dex, so a *small* positive metal-poor offset
is definitional; the effects below are far larger. (b) GSP-Spec values are
**uncalibrated as published** (Recio-Blanco calibrations NOT applied).
(c) Extinction bins use Gaia's own `ag_gspphot` — same pipeline, circularity
declared.

**Headline (n = 5,834 GSP-Phot / 1,834 GSP-Spec pairs):**
- GSP-Phot overall median **−0.062 dex** (p16 −0.307, p84 +0.288) — the
  global median hides everything below.
- GSP-Spec (uncalibrated) overall median **+0.108 dex**, tight-ish
  (p16 −0.072, p84 +0.289).

**By GALAH [Fe/H] — the bias is a metallicity function, not an offset:**
| GALAH [Fe/H] bin | GSP-Phot Δ (n) | GSP-Spec Δ (n) |
|---|---|---|
| −3 … −2 | **+1.849** (15) | +0.509 (4) |
| −2 … −1.5 | **+1.447** (66) | −0.001 (4) |
| −1.5 … −1 | **+0.932** (149) | +0.243 (14) |
| −1 … −0.5 | +0.337 (722) | +0.159 (196) |
| −0.5 … 0 | −0.075 (3,506) | +0.103 (1,226) |
| 0 … +0.6 | −0.177 (1,369) | +0.101 (389) |

GSP-Phot catastrophically overestimates metal-poor stars (XP spectra lose
[M/H] sensitivity; the pipeline floors them near −1) and slightly
underestimates metal-rich ones — a slope, crossing zero near [Fe/H] ≈ −0.4.

**By gravity (GALAH log g), GSP-Phot:** giants (log g < 2.5) **+0.167**
(n=1,101); log g 2.5–3.5 +0.147 (988); dwarfs (log g ≥ 3.5) **−0.154**
(3,745) — a sign flip across gravity at fixed survey. GSP-Spec shows no
such flip in this sample (giants +0.105, dwarfs +0.096).

**By GALAH Teff, GSP-Phot:** 3500–4500 K **+0.320** (337); 4500–5500 K
+0.062 (3,071); 5500–6500 K **−0.234** (2,144); 6500–8000 K +0.006 (282).

**By Gaia A_G, GSP-Phot:** A_G 0–0.5 **−0.112** (4,778); 0.5–1 **+0.282**
(872); 1–2 **+0.323** (177); 2–10 +0.551 (7 — anecdotal n). The
temperature–extinction degeneracy signature, visible even in this
low-extinction GALAH sample.

Sample [Fe/H] span: −3.62 … +0.87; only 19 stars below −2 and 330 below
−1 — the corner where the bias is largest is the corner where this anchor
is thinnest (see novelty).

---

## SCOUTED (documented / schema-verified, no new sample rows today)

- **APOGEE DR17 allStar** — header-level only, and that header is *reused
  from earlier today*: the cosmology leg range-fetched bytes 0–2 MB from
  the dr17.sdss.org SAS mirror (HTTP 206, total 3,970,621,440 B, 733,901
  rows, 234 TTYPEs incl. `FE_H`, `M_H`, `ALPHA_M`, `GAIAEDR3_SOURCE_ID`;
  partial file still on disk at
  `gold/cosmology-chemistry/local/apogee_allStar_dr17_synspec_rev1.HEADER_partial.fits`).
  No APOGEE data rows were downloaded in *this* leg.
- **GALAH DR4** — header verified in the cosmology leg (917,588-star file,
  184 cols, `gaiadr3_source_id`, **no `alpha_fe` column** — α must be built
  from Mg/Si/Ca/Ti). Not sampled here; DR3 was the working anchor.
- **XP spectra themselves** — `gaiadr3.xp_continuous_mean_spectrum` /
  `xp_sampled_mean_spectrum` are **not TAP tables** (HTTP 400, unknown
  table ×2). XP spectra are served via DataLink / bulk download, a
  different route; not needed for this catalogue-level contrast, not
  download-tested.
- **astroquery route** — not installed in the VM; astroquery wraps the
  same ESA TAP endpoint verified above, so the TAP result stands for it.

## BLOCKED (exact block points, tested today — do not assume from the cosmology leg)

- **APOGEE data rows, three routes all failed today:**
  1. `data.sdss.org` — proxy disconnect (HTTPSConnectionPool ProxyError,
     "Remote end closed connection"), same as the cosmology leg.
  2. `dr17.sdss.org` — host *answers* but returns **404** for the SAS
     directory and for every guessed allStar path tried (4 variants).
     This **differs from earlier today**, when the cosmology leg recorded
     a 206 range fetch from this host. Either the SAS tree moved or the
     earlier URL was a path not recovered in this leg — the exact
     earlier URL was not recorded in the campaign files, only the host.
  3. VizieR TAP (`tapvizier.cds.unistra.fr` and `tapvizier.cfa.harvard.edu`,
     catalogue III/286) — proxy disconnect on both mirrors.
  Smallest unblock: one working allStar URL (live-browser fetch of the
  SDSS DR17 APOGEE data-access page would find it), then the same
  range-fetch trick as GALAH works — the file carries its own Gaia IDs.
- **GSP-Spec VMP corner via GALAH** — not an access block, a population
  block: GALAH quality sample gives n=4–15 per VMP bin for GSP-Spec.
  No download fixes that; the anchor itself is thin there.

---

## Novelty scrub — what is already published, and where it stops

**Already published (do not re-claim):**
- Gaia DR3 documentation Ch. 11 + Creevey/Andrae (GSP-Phot paper):
  GSP-Phot [M/H] median absolute error 0.14 dex vs a literature
  compilation; sensitivity collapses below [M/H] ≈ −1.5 with
  overestimation of very-metal-poor stars; hot stars (Teff > 7500 K)
  assigned solar metallicity; Teff–extinction degeneracy for A_0 ≳ 2.
- Recio-Blanco et al. 2023 (GSP-Spec paper): vs APOGEE DR17 / GALAH DR3 /
  RAVE DR6, best-quality sample median offsets ≈ −17 K, −0.3 dex (log g,
  removed by their calibration), **0.00 dex [M/H]**; a log g-dependent
  [M/H] trend (giants underestimated, dwarfs overestimated) with
  published polynomial calibrations; [α/Fe] log g-dependent bias,
  calibration derived in the solar neighbourhood. DR3 GSP-Spec ships
  uncalibrated *by design*.
- Andrae et al. 2023 (XGBoost, 175M stars, trained on ~500k APOGEE DR17 +
  Li et al. VMP stars) and Zhang et al. 2023 (LAMOST forward model, 220M):
  the community has already *routed around* GSP-Phot [M/H] with
  data-driven re-derivations (~0.1 dex, degrading at faint G and at the
  metal-poor end). Any new GSP-Phot bias paper competes with these
  catalogues, not with GSP-Phot alone.
- VMP GSP-Spec reanalyses: recommended quality cuts discard ~80% of
  [Fe/H] < −2 stars (hot-star confusion, grid-border, cool-giant
  molecular bands); CaT-equivalent-width reanalysis halves the scatter
  at [Fe/H] < −1.5.
- GSP-Spec [α/Fe] is Ca-triplet-dominated: a 2026 reassessment finds the
  Gaia low-α massive-star sequence is **not** reproduced by APOGEE or
  GALAH — the RVS α ruler measures mostly calcium.

**Where the published validation stops (the unaudited corners):**
1. **Joint corner map, GALAH-anchored.** Validations are global medians
   or 1-D trends, mostly APOGEE-anchored or against a mixed literature
   compilation. A joint (Teff × log g × A_G × [Fe/H]) bias map against
   GALAH specifically — optical, southern, dwarf-rich, with systematics
   independent of APOGEE's — has not been published. Our sample already
   shows structure the globals hide: at fixed GALAH truth, GSP-Phot Δ
   flips sign with log g (+0.17 giants / −0.15 dwarfs) and with Teff
   (+0.32 cool / −0.23 at 5500–6500 K).
2. **The VMP tail is validated where the anchors are thinnest.** The
   largest bias in the system (+1.4 … +1.9 dex, this run) sits at
   [Fe/H] < −1.5, where GALAH gives tens of stars and APOGEE is also
   sparse. The honest anchor there is a dedicated VMP compilation
   (Li et al. / PASTEL / SAGA), not either survey alone — nobody has
   published the GSP-Phot *and* GSP-Spec bias curves on that anchor
   jointly.
3. **High extinction (A_G ≳ 2).** GALAH avoids the plane (our n = 7);
   GSP-Phot's own docs flag the degeneracy but the corner is effectively
   APOGEE-only territory — and APOGEE is the blocked leg today.
4. **Magellanic / zero-parallax populations.** GSP-Phot consumes
   parallax as an input; GALAH's early fields include LMC stars whose
   parallaxes are ~0 and whose metallicities are systematically
   sub-solar. No published validation isolates this out-of-distribution
   corner. (Flagged as a hypothesis, not a finding: our first-rows
   sample is LMC-contaminated by construction.)
5. **GSP-Spec calibrations outside their derivation regime.** The
   Recio-Blanco polynomials were fit on a literature compilation;
   their residual behaviour in GALAH's dwarf regime and at
   [Fe/H] < −1.5 (where the quality cuts remove most stars before
   calibration is even applied) remains thinly audited. In our sample
   the *uncalibrated* GSP-Spec offset is a near-constant +0.10 dex
   across −0.5 … +0.6 — i.e. most of what the calibration must remove
   here is a zero-point, not the published log g trend.

**Verdict:** comparison gold, narrow niche — the same shape as the
cosmology leg. The publishable unit is not "GSP-Phot is biased" (known,
and already routed around by XGBoost catalogues) but the **joint-corner
bias map on an independent optical anchor + the VMP/high-A_G corners
graded on anchors that actually live there**.

---

## Queries used (verbatim templates)

Gaia counts:
```sql
SELECT COUNT(*) AS n FROM gaiadr3.astrophysical_parameters WHERE mh_gspphot IS NOT NULL
SELECT COUNT(*) AS n FROM gaiadr3.astrophysical_parameters WHERE mh_gspspec IS NOT NULL
```
Gaia join (per batch of 250 GALAH `dr3_source_id`s; 31 batches, all returned):
```sql
SELECT ap.source_id, ap.mh_gspphot, ap.teff_gspphot, ap.logg_gspphot,
       ap.ag_gspphot, ap.ebpminrp_gspphot, ap.mh_gspspec, ap.teff_gspspec,
       ap.logg_gspspec, ap.alphafe_gspspec, gs.phot_g_mean_mag, gs.bp_rp
FROM gaiadr3.astrophysical_parameters AS ap
JOIN gaiadr3.gaia_source AS gs ON ap.source_id = gs.source_id
WHERE ap.source_id IN (<250 comma-separated GALAH dr3_source_ids>)
```
GALAH access: HTTP `Range: bytes=0-23999999` GET on the Data Central
`.fits` URL in §2 (HTTP 206).

## Files (bundle: `gold/gaia-chemistry/`, 26 MB total — budget < 500 MB)
- `fetch_galah_sample.py` — range download (24 MB) of GALAH DR3 allstar
- `galah_dr3_first16120rows.fits` — patched-header copy, 16,120 real rows
- `extract_and_join.py` — GALAH extraction (first, interrupted run;
  superseded by the two scripts below — kept for provenance)
- `galah_sample.csv` + `galah_sample_meta.json` — 16,120 GALAH rows;
  7,698 quality IDs
- `gaia_join.py` — resumable TAP join (progress: `join_progress.json`)
- `gaia_for_galah_sample.csv` — 7,698 Gaia rows for the quality IDs
- `first_contrast.py` + `first_contrast_results.json` — the contrast in §4
- Tooling note: astropy 8.0.2 was pip-installed into `tools-venv` this
  run (system python has numpy/pandas only). No accounts created anywhere.
