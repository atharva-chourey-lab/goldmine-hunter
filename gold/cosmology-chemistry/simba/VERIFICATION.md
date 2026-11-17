# SIMBA (Davé et al. 2019) — Goldmine Hunter scouting verification, 2026-11-17

Source: Simba Simulation Repository, http://simba.roe.ac.uk/
No registration / no login — plain HTTP downloads verified with curl.

## Downloaded & verified in this directory
- m25n512_010.hdf5 — 2,241,946 bytes, md5 8773e0b6799b315666ccd0227ed0d140
  Caesar catalogue, snap 010, z=13.707 (simulation_attributes/redshift).
  ngalaxies=0 (only 18 star particles) — halo_data only; halo metallicities.* present.
- m25n512_020.hdf5 — 39,106,116 bytes, md5 aa1e2d6ecd71cd5fe66587d472075d28
  Caesar catalogue, snap 020, z=9.642. ngalaxies=46.
  galaxy_data/dicts verified: masses.stellar (unit Msun),
  metallicities.stellar / .mass_weighted / .sfr_weighted (unit dimensionless),
  galaxy_data/sfr, sfr_100.

## z=0 catalogue verified WITHOUT full download (HTTP range reads, h5py)
File: http://simba.roe.ac.uk/simdata/m25n512/s50/catalogs/m25n512_151.hdf5
Server Content-Length: 340,478,689 bytes. Range-read total fetched: ~12–23 MB per pass.
- simulation_attributes: redshift = 4.44e-16 (~0), basename snap_m25n512_151.hdf5
- root attrs: ngalaxies=5539, nhalos=275252
- galaxy_data/dicts: 668 datasets = 588 absmag/appmag photometry + 80 others.
  Non-photometry chemistry/mass fields (all shape (5539,), float64):
  masses.stellar, masses.star_30kpc, masses.gas, masses.gas_30kpc, masses.bh,
  masses.dm, masses.dust, masses.HI, masses.H2 (+_30kpc), masses.baryon, masses.total
  metallicities.mass_weighted, metallicities.sfr_weighted, metallicities.stellar,
  metallicities.mass_weighted_cgm, metallicities.temp_weighted_cgm
  Sample z=0 values: masses.stellar[0]=3.23e12 Msun; metallicities.stellar[0]=0.02836;
  metallicities.mass_weighted[0]=0.03349; metallicities.sfr_weighted[0]=0.03255.
- NO per-element datasets anywhere in galaxy_data/dicts.

## Other z=0 catalogue sizes (HEAD, Content-Length)
- m50n512/s50 (full physics): 218,785,515 bytes — smallest z=0 catalogue, still >200 MB cap
- m25n512/s50: 340,478,689 | m100n1024/s50 flagship: 2,828,044,459
- m100n1024/simba-c: 2,608,169,233 (catalogue listing exists; same Caesar format expected, NOT inspected)
- z=0 snapshot (element source) m25n512: snap_m25n512_151.hdf5 = 32,575,439,948 bytes — not downloaded

## Chemistry facts
- Caesar metallicities are TOTAL metal mass fractions, NOT solar-scaled
  (Caesar docs, catalog.html): from snapshot Metallicity[0]; Caesar holds no
  per-element info — elements must come from the snapshot's 11-element
  Metallicity array per particle (Caesar docs worked example: oxygen = index 4,
  5th element), combined with galaxy_data glist/slist particle lists.
- SIMBA tracks 11 elements: H, He, C, N, O, Ne, Mg, Si, S, Ca, Fe.
  Yields: SNII Nomoto et al. 2006; SNIa Iwamoto et al. 1999 (1.4 Msun metals each);
  AGB Oppenheimer & Davé 2006. SIMBA dropped MUFASA's ad-hoc factor-2 yield cut.
  Solar normalisation: Zsun = 0.0134, Asplund et al. 2009.
  (Note: yt unit registry embedded in the Caesar files lists Zsun=0.01295 — not SIMBA's value.)
- Feedback relevant to chemistry: two-phase decoupled FIRE-scaled stellar winds
  (metal-loaded in SIMBA), torque-limited+Bondi BH accretion, AGN radiative +
  bipolar jet + X-ray feedback, on-the-fly dust production/growth/destruction.
  Feedback-variant z=0 catalogues (s50nox / s50nojet / s50noagn / s50nofb, 50 Mpc/h)
  are on the same repository — a ready-made chemistry-vs-feedback control set.
