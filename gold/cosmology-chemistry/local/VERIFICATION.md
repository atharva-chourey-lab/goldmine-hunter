# Local observed-chemistry anchors — verification log (2026-11-17)

Method: HTTP Range partial fetches (headers only, 2–3 MB each), FITS TTYPEn cards parsed
with pure Python (astropy NOT installed in this VM). Total downloaded: ~7.8 MB.

## Files in this directory
- `apogee_allStar_dr17_synspec_rev1.HEADER_partial.fits` — bytes 0–2,000,000 of
  allStar-dr17-synspec_rev1.fits, fetched from the dr17.sdss.org SAS mirror.
  Response: HTTP 206, Content-Range total = 3,970,621,440 bytes.
  Parsed: TFIELDS=234, NAXIS2=733,901 rows (first table HDU).
  Chemistry columns present: FE_H, M_H, ALPHA_M, O_FE, MG_FE, SI_FE, C_FE, CI_FE, N_FE,
  NA_FE, AL_FE, P_FE, S_FE, K_FE, CA_FE, TI_FE, TIII_FE, V_FE, CR_FE, MN_FE, CO_FE, NI_FE,
  CU_FE, CE_FE, YB_FE (each with _SPEC/_ERR/_FLAG), plus X_H, X_M arrays, TEFF, LOGG.
  `apogee_ttype_list_partial.json` = full parsed list. `apogee_headers.txt` = response headers.
  NOTE: official host data.sdss.org returned empty replies from this VM on every attempt;
  the mirror host worked.
- `GALAH_DR3_main_allstar_v2.HEADER_partial.fits` — bytes 0–3,000,000.
  HEAD: Content-Length 873,518,400, Accept-Ranges: bytes.
  Parsed: 197 TTYPEs. Chemistry: fe_h, alpha_fe, O_fe, Mg_fe, Si_fe, C_fe, Li_fe, Na_fe,
  Al_fe, K_fe, Ca_fe, Ti_fe, Ti2_fe, Sc_fe, V_fe, Cr_fe, Mn_fe, Co_fe, Ni_fe, Cu_fe, Zn_fe,
  Rb_fe, Sr_fe, Y_fe, Ba_fe, La_fe, Ce_fe, Nd_fe, Sm_fe, Eu_fe (+ e_/nr_/flag_ per element).
- `galah_dr4_allstar_240705.HEADER_partial.fits` — bytes 0–3,000,000.
  HEAD: Content-Length 757,998,720, Accept-Ranges: bytes.
  Parsed: 184 TTYPEs. Chemistry: fe_h; o_fe, mg_fe, si_fe, c_fe, n_fe, na_fe, al_fe, k_fe,
  ca_fe, sc_fe, ti_fe, v_fe, cr_fe, mn_fe, co_fe, ni_fe, cu_fe, zn_fe, rb_fe, sr_fe, y_fe,
  zr_fe, mo_fe, ru_fe, ba_fe, la_fe, ce_fe, nd_fe, sm_fe, eu_fe (lowercase, + e_/flag_).
  IMPORTANT: NO alpha_fe column in DR4 main allstar (DR3 has one). DR4 main file DOES
  carry per-star `mass`, `age`, `lbol` (individual stellar, not galaxy, mass).
  `galah_ttype_lists.json` = full parsed lists for both GALAH files.

## NOT downloaded
- MaNGA Pipe3D catalogue: fields documented byte-by-byte in the VizieR ReadMe for
  J/ApJS/262/36 (fetched in full). Data-file sample download FAILED: data.sdss.org
  unreachable from this VM; VizieR nao.ac.jp mirror returned 404 for catalog.dat;
  CDS attempt returned nothing. Fields are therefore ReadMe-documented, not download-verified.
- APOGEE astroNN VAC: SDSS VAC page fetched; its text extraction exposed no direct file
  URL, so no sample download was attempted. Page-claim only.
