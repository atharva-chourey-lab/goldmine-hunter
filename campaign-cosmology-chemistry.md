# Campaign: Cosmology × Local Chemistry (commissioned 2026-11-17)

**Idea (Atharva's terms):** high-fidelity scans are the premium resource —
capitalize on them. Here the "scan" is a high-fidelity cosmological
simulation; the contrast is against known **local chemistry**.

**Interpretation worked under (correct if wrong):**
- Simulations = IllustrisTNG (TNG100/TNG300), EAGLE, SIMBA — the premium
  high-resolution "scans" of the universe; their galaxy catalogues are the
  derived "labels".
- Local chemistry = observed chemistry of the local universe: Milky Way /
  nearby-galaxy stellar and gas abundances from real surveys — APOGEE DR17,
  GALAH DR3/DR4, SDSS/MaNGA mass–metallicity data, solar abundances
  (Asplund et al.) as zero-point.
- Comparison = the SAME chemical diagnostics computed the SAME way across
  all suites, graded against local observed values. Diagnostics:
  (1) z=0 stellar MZR normalisation/scatter, (2) gas-phase MZR,
  (3) [α/Fe] vs [Fe/H] / element ratios (O, Mg, Si, Fe), (4) metallicity
  distributions / gradients.

**Provenance (doctrine):** all three simulation releases and all local
survey releases are **published-by-design** — inventory, not recoveries.
Nothing here is stranded or Wayback-only. The value is the comparison
nobody has run (see Novelty), not a file recovery. Say so plainly.

## Comparable set: z=0 galaxy chemistry catalogues × suite

| Suite | Stellar mass | Stellar Z | Gas Z | Elements (O, Mg, Si, Fe) | Status |
|---|---|---|---|---|---|
| IllustrisTNG (TNG100-1, snap 99) | REAL — via FlatHUB mirror, unauthenticated; 29,978-row random sample of the 95,417 subhalos with M*(2Rhalf) > 10⁷ M☉/h downloaded & computed | REAL (same sample) | REAL (same sample, all-gas fractions) | REAL — star/gas metal fractions for H, C, N, O, Ne, Mg, Si, Fe + catch-all "total" (S, Ca NOT individually tracked) | Official API = 403 without API key (free registration + admin approval). HDF5 header inspection still pending a key; field names corroborated by specs + live FlatHUB data |
| EAGLE (RefL0100N1504, SnapNum=28) | SCHEMA-VERIFIED, DATA BLOCKED — fields from McAlpine+2016 App. B (downloaded): `Mass_Star` (Aperture, 30 pkpc), join `GalaxyID` | `Stars_Metallicity` (SubHalo) | `SF_Metallicity` / `NSF_Metallicity` | Full per-element stellar fields: `Stars_Oxygen/Iron/Magnesium/Silicon/Carbon/…` + `IronFromSNIa` split | Both routes (SQL DB, snapshots) return **401** without a free registered account. No data row obtained |
| SIMBA (m25n512, snap 151) | REAL — full z=0 Caesar catalogue downloaded (340,478,689 B, exact HEAD match), 5,539 galaxies, fields read from the file | REAL — `metallicities.stellar` | REAL — `metallicities.mass_weighted` / `sfr_weighted` (total Z only) | ABSENT from all Caesar catalogues (by design, per Caesar docs). Elements exist only per-particle in snapshots; smallest z=0 snapshot = 32.6 GB | No barrier at all — plain HTTP from simba.roe.ac.uk |

Exact fields:
- **TNG** (official names; FlatHUB flattens to `Subhalo_…` and codes Fe as
  `Fi`): `SubhaloMassInRadType[:,4]` (stellar mass within 2× stellar
  half-mass radius, 10¹⁰ M☉/h, h=0.6774), `SubhaloStarMetallicity`,
  `SubhaloGasMetallicity`, `SubhaloStarMetalFractions` /
  `SubhaloGasMetalFractions` (N,10; order H, He, C, N, O, Ne, Mg, Si, Fe,
  total). Z is a raw mass fraction; specs: divide by **Z☉ = 0.0127** for
  solar units. Full groupcat sizes: TNG100-1 snap 99 = 4.1 GB,
  TNG300-1 = 13.0 GB, TNG100-3 = 104.6 MB (smallest first grab once a key
  exists).
- **EAGLE**: metal mass fraction Σ(mᵢZᵢ)/Σmᵢ per component; element field =
  element mass / component mass ("absolute abundances which do not depend
  on the solar abundance"). No Z☉ in the simulation; EAGLE-paper
  convention Z☉ = 0.0127 (Allende Prieto+2001 / Wiersma+2009a), some later
  papers 0.012 — declare which.
- **SIMBA** (HDF5 paths under `galaxy_data/dicts/`): `masses.stellar`
  (total bound; aperture variant spelled `masses.star_30kpc`),
  `metallicities.stellar`, `metallicities.mass_weighted`,
  `metallicities.sfr_weighted`, `metallicities.mass_weighted_cgm`.
  Total metal mass fractions, NOT solar-scaled. Model solar value
  **Z☉ = 0.0134 (Asplund+2009)** — note the yt registry embedded in the
  files says 0.01295; do not use it. Yields: SNII Nomoto+2006, SNIa
  Iwamoto+1999, AGB Oppenheimer & Davé 2006; SIMBA dropped MUFASA's
  ad-hoc ×2 yield reduction. Feedback-variant z=0 catalogues (s50nox /
  s50nojet / s50noagn / s50nofb) exist on the same site — a ready-made
  chemistry-vs-feedback control set.

## Local anchors

| Anchor | What it anchors | Fields (verified) | Status |
|---|---|---|---|
| APOGEE DR17 allStar (733,901 rows, 3.97 GB file) | [α/Fe]–[Fe/H] plane, element tracks, MDF — for MW-mass simulated galaxies. NOT an MZR anchor (no galaxy mass) | `FE_H`, `M_H`, `ALPHA_M`, `O_FE`, `MG_FE`, `SI_FE`, `C_FE`, `CA_FE`, … (234 columns) | VERIFIED by partial download (header parsed) via dr17.sdss.org mirror; data.sdss.org unreachable from this VM |
| GALAH DR3 (588,571 stars) / DR4 (917,588 stars) | Same class as APOGEE + neutron-capture ratios (Ba, Eu, La) | DR3: `fe_h`, `alpha_fe`, `O_fe`, `Mg_fe`, `Si_fe`, … (197 cols). DR4: `fe_h`, lowercase `o_fe/mg_fe/si_fe`, … (184 cols) — **DR4 has NO `alpha_fe` column**; build α from Mg/Si/Ca/Ti | VERIFIED by partial download (headers parsed), no registration |
| MaNGA DR17 Pipe3D VAC (10,243 galaxies) | **The MZR anchor** — stellar MZR (`log_Mass` vs `ZH_MW_Re_fit` / `ZH_LW_Re_fit`) AND gas MZR (`OH_Mar13_O3N2_Re_fit`), plus gradients (`alpha_ZH_…`, `OH_…_alpha_fit`) | From VizieR ReadMe J/ApJS/262/36 (fetched in full) | DOCUMENTED, NOT download-verified — SDSS host unreachable from VM; needs a live-browser or alternate-network fetch. Caveats: Pipe3D stellar Z is SSP-template Z; gas O/H is calibrator-dependent — fix the calibrator before contrasting |
| Solar zero-point | Conversion zero-point for every [Fe/H], [X/Fe], Z comparison | Asplund+2021: log ε O 8.69, Mg 7.55, Si 7.51, Fe 7.46; Z☉ = 0.0139, Z/X = 0.0187. Asplund+2009 (the simulation-era standard): O 8.69, Mg 7.60, Si 7.51, Fe 7.50; Z☉ = 0.0134 | Sourced from fetched pages (SIMBAD record, FastChem tables). 2009→2021 shifts [Fe/H] by 0.04 dex — declare the scale |

## Novelty scrub (full papers fetched, not snippets)

**The broad proposal is already published.** Garcia, Torrey et al. have run
the uniform same-method cross-suite comparison:
- Torrey+2019 — TNG gas MZR/FMR baseline (single suite).
- Garcia+2024 Paper I — FMR scatter, Illustris+TNG+EAGLE (no SIMBA).
- Garcia+2024 Paper II — gas MZR normalisation, **all four suites incl.
  SIMBA**. Method warning: their metallicity is total Z scaled to O/H with
  fixed f_O = 50% — they deliberately avoided directly-tracked oxygen to
  suppress yield-table differences.
- Garcia+2024 (stellar interplay) — stellar MZR for Illustris/TNG/EAGLE
  (**no SIMBA**), total Z⋆ only, vs Gallazzi+2005 / Panter+2008; simulated
  MZ⋆R found elevated vs observations.
- Garcia+2025 — **gas-phase** gradients, all four suites.
- Carnevale+2026 — FMR mass dependence, all four + SDSS (gas only).
- Element ratios exist only single-suite: Segers+2016 & Gebek &
  Matthee 2022 (EAGLE [α/Fe]); Naiman+2018 (TNG100 [Mg/Fe], [Eu/Fe] vs MW
  stars). Wright+2024 is the uniform cross-suite precedent but for the
  baryon cycle, not chemistry.

**The unclaimed combination (narrow — every qualifier matters):** at z=0
only, one common aperture/weighting/solar scale, TNG+EAGLE+SIMBA together:
(i) stellar element ratios [O/Fe], [Mg/Fe], [Si/Fe] as full distributions
in the [α/Fe]–[Fe/H] plane — not just median total Z⋆ — and (ii) stellar
MDFs and stellar (not gas) gradients, graded against APOGEE/GALAH
resolved-star abundances and MaNGA *stellar* abundances. Risks: yields and
solar scales genuinely differ per suite (EAGLE tracks 11 elements, TNG 9 +
catch-all, SIMBA 10 + Ca/S), so "same way" = same post-processing, not
same yields; Garcia+2025 is labelled "I" — a stellar/element sequel from
that group is a plausible in-preparation competitor.

## First contrast — COMPUTED 2026-11-17 (script: gold/cosmology-chemistry/first_contrast.py; numbers: first_contrast_results.json)

Method, declared: 0.5-dex stellar-mass bins. TNG = 29,978-row FlatHUB
random sample (of 95,417 subhalos above threshold), M⋆ within 2×Rhalf,
Z☉ = 0.0127. SIMBA = full m25n512 z=0 catalogue (5,539 galaxies; small
25 Mpc/h box — high-mass bins are thin), M⋆ total bound, Z☉ = 0.0134.
Apertures differ (2Rhalf vs total) — declared, not pooled. Medians over
galaxies with Z > 0.

**Stellar MZR — median log(Z⋆/Z☉):**

| log M⋆ bin | TNG100-1 (n) | SIMBA m25 (n) | Δ (TNG − SIMBA) |
|---|---|---|---|
| 8.5–9.0 | −0.153 (4,232) | −0.360 (783) | +0.21 |
| 9.0–9.5 | +0.011 (2,915) | −0.239 (584) | +0.25 |
| 9.5–10.0 | +0.130 (1,662) | −0.253 (501) | +0.38 |
| 10.0–10.5 | +0.245 (1,140) | −0.187 (138) | **+0.43** |
| 10.5–11.0 | +0.269 (526) | −0.029 (43) | +0.30 |
| 11.0–11.5 | +0.278 (105) | +0.081 (17) | +0.20 |

The two "rulers" disagree by 0.2–0.43 dex across the whole mass range;
the solar-scale difference (0.0127 vs 0.0134) explains only 0.023 dex.
SIMBA's stellar MZR is also much flatter. This is the yield/feedback
signature the campaign exists to measure. (Consistent in direction with
Garcia+2024's finding of large cross-suite stellar normalisation
differences — but SIMBA was not in their stellar comparison.)

**Gas-phase MZR — TNG median 12+log(O/H)** (all-gas mass fractions,
SFR > 0, aperture 2Rhalf; NOT SFR-weighted — declared mismatch vs
emission-line observations) **vs Tremonti+2004** (SDSS, ~53,000 SF
galaxies; polynomial −1.492 + 1.847 logM⋆ − 0.08026 (logM⋆)², verified
from the source paper):

| log M⋆ bin | TNG (n) | Tremonti+2004 | Δ |
|---|---|---|---|
| 8.5–9.0 | 8.589 (2,938) | 8.524 | +0.06 |
| 9.0–9.5 | 8.751 (2,260) | 8.726 | +0.03 |
| 9.5–10.0 | 8.894 (1,391) | 8.887 | +0.01 |
| 10.0–10.5 | 8.969 (812) | 9.007 | −0.04 |
| 10.5–11.0 | 8.831 (346) | 9.088 | −0.26 |
| 11.0–11.5 | 8.775 (96) | 9.129 | −0.35 |

TNG tracks the local gas MZR within ~0.05 dex up to 10^10.5 M☉, then
turns down (massive-galaxy gas dilution / AGN regime + the all-gas vs
emission-line weighting caveat). SIMBA gas O/H is not computable from
Caesar catalogues (total Z only) — its gas total-Z medians are in the
results JSON.

**TNG stellar element ratios, MW-mass galaxies (log M⋆ 10.5–11.0, n=526),
Asplund+2009 solar:** [O/Fe] = +0.40, [Mg/Fe] = +0.29, [Si/Fe] = +0.25
(medians; 16–84% spreads ≈ ±0.03–0.05). α-enhanced, in the regime APOGEE's
high-α sequence occupies — APOGEE/GALAH are verified anchors for exactly
this plane, but no APOGEE median was computed in this pass (header-level
verification only), so no numeric sim-vs-APOGEE offset is claimed yet.

## Blockers & smallest unblocking steps

1. **EAGLE data** — one free registration by Atharva at
   https://virgodb.cosma.dur.ac.uk/ (email + consent tick; username/
   password emailed). Unlocks SQL + snapshots. Then run the prepared
   z=0 query in gold/cosmology-chemistry/eagle/SCOUT.md.
2. **TNG full catalogue / HDF5 headers** — free registration at
   https://www.tng-project.org/users/register/ (admin approval, then API
   key). First grab: TNG100-3 groupcat-99 (104.6 MB) for a full header
   check, or single-field TNG100-1 subsets. FlatHUB already covers
   catalogue-level work unauthenticated in the meantime.
3. **MaNGA Pipe3D download-verification** — needs a live-browser or
   alternate-network fetch (data.sdss.org unreachable from this VM;
   VizieR mirrors failed). The catalogue is the stellar-MZR grading
   anchor, so this is the highest-value unblock after EAGLE.
4. **SIMBA elements** — blocked by design, not access: needs the 32.6 GB
   z=0 snapshot (m25n512 snap 151) + Caesar glist/slist cross-match.
   Deliberate decision, not a scout step.
5. Local tooling: h5py lives in ~/workspace/goldmine-hunter/tools-venv
   (system python has none). Total campaign downloads ≈ 386 MB.

## Files

- gold/cosmology-chemistry/tng/ — FlatHUB samples (29,978-row MZR +
  gas samples, CSV+NPY), VERIFICATION_LOG.txt (403 evidence)
- gold/cosmology-chemistry/simba/ — m25n512_151.hdf5 (full z=0
  catalogue), m25n512_010/020.hdf5, VERIFICATION.md
- gold/cosmology-chemistry/eagle/ — SCOUT.md (schema + ready z=0 query),
  release papers, 401 evidence
- gold/cosmology-chemistry/local/ — APOGEE/GALAH partial FITS headers +
  parsed field lists, VERIFICATION.md
- gold/cosmology-chemistry/first_contrast.py + first_contrast_results.json

*Pointer: this campaign file is the record; README.md's verified-results
history is untouched, per instructions.*
