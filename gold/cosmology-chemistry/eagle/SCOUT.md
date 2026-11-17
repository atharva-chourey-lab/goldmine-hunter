# EAGLE scout — cosmology-chemistry Goldmine Hunter
Scouted 2026-11-17. All URLs below copied verbatim from tool results / live-fetched pages. No catalogue data was downloaded — both data routes return 401 without an account (evidence files in this folder).

## Routes

### 1. EAGLE SQL galaxy database (the z=0 catalogue route — USE THIS)
- Landing / registration portal: https://virgodb.cosma.dur.ac.uk/
  - Page text fetched live: "To request an account please enter your email address below. We will send you a randomly generated user name and password"
- Public-data page (live-fetched, saved as eagle_database_page.html): https://astro.dur.ac.uk/ICC/Eagle/database.php
  - Redirect chain observed: http://icc.dur.ac.uk/Eagle/database.php -> https://icc.dur.ac.uk/Eagle/database.php -> https://astro.dur.ac.uk/ICC/Eagle/database.php
  - Page states: "Access to both the database and particle data require only a single account"
- SQL endpoint linked from that page: http://virgodb.dur.ac.uk:8080/Eagle/
  - TESTED unauthenticated 2026-11-17: HTTP 401, WWW-Authenticate: Basic realm="Note: accounts reset as of 21 July 2020.  New accounts can be requested at http://virgodb.dur.ac.uk ." (sql_endpoint_401_evidence.html)
- Newer SQL endpoint linked from the live virgodb.cosma portal (virgodb_cosma.html): https://virgoDB.cosma.dur.ac.uk:8443/Eagle/
- Format: SQL query -> CSV (browser "Query (stream)" returns CSV; browser queries time out after 90 s per McAlpine et al. 2016). Registered users also get a private MyDB.
- No file size: it is a query service, not a file. >1,000,000 galaxies across all runs/snapshots per the public-data page.
- z=0 = SnapNum 28 (McAlpine Table C.1: SnapNum 28, Redshift 0.00).
- Tables per run, prefixed e.g. RefL0100N1504_ : SubHalo, FOF, Sizes, Aperture, Magnitudes

### 2. EAGLE particle snapshots (HDF5) — only if per-particle chemistry is needed
- Listing/download base linked from public-data page: http://dataweb.cosma.dur.ac.uk:8080/eagle-snapshots/
  - Redirects to https://dataweb.cosma.dur.ac.uk:8443/eagle-snapshots/
  - TESTED unauthenticated: HTTP 401, realm="Eagle Database Authentication" (snapshots_listing_401_evidence.html, snapshot_download_401_evidence.html)
- Download pattern seen in third-party tutorials (MARTINI notebook): https://dataweb.cosma.dur.ac.uk:8443/eagle-snapshots//download?run=RefL0025N0376&snapnum=28 (same account as SQL)
- Sizes actually stated in fetched sources: RefL0025N0376 snapshot 28 alone = 8 GB tarball (~15 GB temp space while unpacking, MARTINI notebook); all 29 snapshots of RefL0025N0376 = 184 GB disk (Tangos tutorial). NO size for RefL0100N1504 was stated in any fetched source — do not assume one.
- Format: HDF5, split over multiple part-files, e.g. snap_028_z000p000.0.hdf5

## Exact field names — verified from the downloaded release papers in this folder
Source documents actually downloaded and text-extracted here:
- McAlpine2016_EAGLE_database_release_1510.01320.pdf (24 pp, 1,992,008 bytes) — Appendix B is the DB schema
- EAGLEteam2017_particle_data_release_1706.09899.pdf (20 pp, 728,647 bytes) — Tables 4/6 are the snapshot schema
These verify the SCHEMA. They are not catalogue data.

### SubHalo table ([run]_SubHalo) — main galaxy table
- Stellar mass (total, all bound star particles): MassType_Star [Msun]; also MassType_Gas, MassType_DM, MassType_BH, Mass, StellarInitialMass
- NOTE: there is NO "Metallicity_Star" field. Metallicity fields use the component as a PREFIX.
- Repeated component block: every field below exists as SF_<field> (star-forming gas), NSF_<field> (non-star-forming gas) and Stars_<field> (stars):
  Metallicity, Hydrogen, Helium, Carbon, Nitrogen, Oxygen, Neon, Magnesium, Silicon, Sulphur, Calcium, Iron, IronFromSNIa, Mass, MassFromAGB, MassFromSNII, MassFromSNIa, MetalsFromAGB, MetalsFromSNII, MetalsFromSNIa, KineticEnergy, ThermalEnergy, TotalEnergy, Spin_x/y/z (+ MassWeightedTemperature / MassWeightedEntropy, gas components only)
  - Stellar metallicity = Stars_Metallicity
  - Gas metallicity = SF_Metallicity (star-forming gas; the usual "gas-phase" Z) and NSF_Metallicity
  - Individual stellar elements = Stars_Carbon, Stars_Nitrogen, Stars_Oxygen, Stars_Neon, Stars_Magnesium, Stars_Silicon, Stars_Sulphur, Stars_Calcium, Stars_Iron, Stars_Hydrogen, Stars_Helium, Stars_IronFromSNIa (same pattern for SF_/NSF_)
- Other useful: GalaxyID, GroupID, Redshift, SnapNum, SubGroupNumber (=0 centrals), Spurious (=1 artefact, discard), StarFormationRate, BlackHoleMass

### Aperture table ([run]_Aperture) — RECOMMENDED stellar mass
- Mass_Star [Msun], Mass_Gas, Mass_DM, Mass_BH, SFR, VelDisp, GalaxyID, ApertureSize
- ApertureSize values: 1, 3, 5, 10, 20, 30, 40, 50, 70, 100 pkpc. Use 30 (EAGLE-team standard, avoids intracluster light).
- Aperture has NO metallicity columns — join to SubHalo on GalaxyID for chemistry.

### Snapshot HDF5 (PartType0 gas / PartType4 stars)
- ElementAbundance — array, order as printed in manual Tables 4/6: [Carbon, Helium, Hydrogen, Iron, Magnesium, Neon, Nitrogen, Oxygen, Silicon], each = element mass / particle mass
- SmoothedElementAbundance — SPH-kernel-weighted version of the above
- Metallicity, SmoothedMetallicity, IronMassFracFromSNIa, SmoothedIronMassFracFromSNIa, MetalMassFracFromAGB, MetalMassFracFromSNIa, MetalMassFracFromSNII
- Stars also: Mass, InitialMass, StellarFormationTime, BirthDensity. Groups: PartType0/1/4/5, Header, Parameters (initial + solar abundances used in the run)

## Metallicity definition / solar normalisation
- DB Metallicity (per component): metal mass fraction, sum_i(m_i Z_i)/sum_i(m_i). Element field: total mass in that element / total mass of that component. Paper wording: "absolute abundances which do not depend on the solar abundance."
- Particle Metallicity: mass fraction in all elements heavier than He, INCLUDING elements not tracked individually — so Z > sum of the individually tracked metals.
- The simulation itself uses no Z_solar / solar pattern (definitions independent of it). Analysis convention in EAGLE papers: Z_sun = 0.0127 (Allende Prieto, Lambert & Asplund 2001), adopted for consistency with Wiersma et al. 2009a. Some later EAGLE papers use 0.012 / Asplund et al. 2009 (12+log(O/H)=8.69) — state which you use.

## Ready z=0 query (once account exists)
SELECT SH.GalaxyID, AP.Mass_Star, SH.MassType_Star, SH.Stars_Metallicity, SH.SF_Metallicity, SH.NSF_Metallicity, SH.Stars_Oxygen, SH.Stars_Iron, SH.Stars_Carbon, SH.Stars_Magnesium
FROM RefL0100N1504_SubHalo AS SH, RefL0100N1504_Aperture AS AP
WHERE SH.SnapNum = 28 AND SH.Spurious = 0 AND AP.ApertureSize = 30 AND SH.GalaxyID = AP.GalaxyID

## Blocker / smallest unblocking step
Free registration only: enter an email on https://virgodb.cosma.dur.ac.uk/ (tick the consent box) -> username/password emailed. One account unlocks BOTH the SQL DB and snapshot downloads. A third-party tutorial says it "typically takes a business day" — that timing is not an official statement. No anonymous CSV, sample catalogue, or Zenodo mirror was found.
