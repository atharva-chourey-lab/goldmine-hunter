import numpy as np, h5py, json

H_TNG = 0.6774
ZSUN_TNG = 0.0127      # TNG specs: divide by 0.0127
ZSUN_SIMBA = 0.0134    # Asplund 2009, SIMBA model value
bins = [(8.5,9.0),(9.0,9.5),(9.5,10.0),(10.0,10.5),(10.5,11.0),(11.0,11.5)]

def med_stats(x):
    if len(x)==0: return None
    return dict(n=int(len(x)), median=float(np.median(x)),
                p16=float(np.percentile(x,16)), p84=float(np.percentile(x,84)))

out = {}

# ---------- TNG100-1 via FlatHUB sample ----------
d = np.load('/home/hatch/workspace/goldmine-hunter/gold/cosmology-chemistry/tng/flathub_tng100-1_snap99_mzr_sample.npy')
mstar = d['Subhalo_MassInRadType_stars']*1e10/H_TNG   # Msun, within 2x half-mass radius
logm = np.log10(np.where(mstar>0, mstar, np.nan))
zstar = d['Subhalo_StarMetallicity']                   # mass fraction, same aperture
logz_tng = np.log10(np.where(zstar>0, zstar/ZSUN_TNG, np.nan))
# gas O/H (number) from mass fractions, all-gas aperture 2Rhalf
dg = np.load('/home/hatch/workspace/goldmine-hunter/gold/cosmology-chemistry/tng/flathub_tng100-1_snap99_gas_sample.npy')
fO = dg['Subhalo_GasMetalFractions_O']; fH = dg['Subhalo_GasMetalFractions_H']
sfr = dg['Subhalo_SFR']
logm_g = np.log10(np.where(dg['Subhalo_MassInRadType_stars']*1e10/H_TNG>0, dg['Subhalo_MassInRadType_stars']*1e10/H_TNG, np.nan))
oh = np.where((fO>0)&(fH>0), 12+np.log10((fO/15.999)/(fH/1.008)), np.nan)
tng_star, tng_gas = [], []
for lo,hi in bins:
    sel = (logm>=lo)&(logm<hi)
    tng_star.append(med_stats(logz_tng[sel & np.isfinite(logz_tng)]))
    selg = (logm_g>=lo)&(logm_g<hi) & (sfr>0) & np.isfinite(oh)
    tng_gas.append(med_stats(oh[selg]))
out['TNG100-1'] = dict(n_sample=int(len(d)), stellar_logZ_over_Zsun_0127=tng_star, gas_12logOH_sfr_gt_0=tng_gas)

# TNG stellar element ratios for Milky-Way-mass galaxies (logM 10.5-11.0)
sel = (logm>=10.5)&(logm<11.0)
eps = {'O':8.69,'Mg':7.60,'Si':7.51,'Fe':7.50}  # Asplund 2009
A = {'O':15.999,'Mg':24.305,'Si':28.085,'Fe':55.845}
ratios = {}
for el in ['O','Mg','Si']:
    fx = d[f'Subhalo_StarMetalFractions_{el}'] if el!='Fe' else None
    ffe = d['Subhalo_StarMetalFractions_Fi']
    fx = d['Subhalo_StarMetalFractions_'+el]
    ok = sel & (fx>0) & (ffe>0)
    num = (fx[ok]/A[el])/(ffe[ok]/A['Fe'])
    xfe = np.log10(num) - (eps[el]-eps['Fe'])
    ratios[el] = med_stats(xfe)
out['TNG100-1']['MWmass_logM10.5-11.0_[X/Fe]_stellar'] = ratios

# ---------- SIMBA m25n512 z=0 full catalogue ----------
f = h5py.File('/home/hatch/workspace/goldmine-hunter/gold/cosmology-chemistry/simba/m25n512_151.hdf5','r')
gd = f['galaxy_data/dicts']
ms = gd['masses.stellar'][:]; zs = gd['metallicities.stellar'][:]
zg = gd['metallicities.mass_weighted'][:]; zgs = gd['metallicities.sfr_weighted'][:]
print('SIMBA ngalaxies:', len(ms), 'redshift attr:', f.attrs.get('redshift') if 'redshift' in f.attrs else gd.attrs.get('redshift'))
logm_s = np.log10(np.where(ms>0, ms, np.nan))
logz_s = np.log10(np.where(zs>0, zs/ZSUN_SIMBA, np.nan))
logzg_s = np.log10(np.where(zg>0, zg/ZSUN_SIMBA, np.nan))
sim_star, sim_gas = [], []
for lo,hi in bins:
    sel = (logm_s>=lo)&(logm_s<hi)
    sim_star.append(med_stats(logz_s[sel & np.isfinite(logz_s)]))
    sim_gas.append(med_stats(logzg_s[sel & np.isfinite(logzg_s)]))
out['SIMBA_m25n512'] = dict(n_galaxies=int(len(ms)), stellar_logZ_over_Zsun_0134=sim_star, gas_totalZ_logZ_over_Zsun_0134=sim_gas)
f.close()

# ---------- Tremonti et al. 2004 observed gas MZR ----------
def tremonti(logM): return -1.492 + 1.847*logM - 0.08026*logM**2
out['Tremonti2004_gas_12logOH'] = [round(tremonti((lo+hi)/2),3) for lo,hi in bins]

print(json.dumps(out, indent=1))
with open('/home/hatch/workspace/goldmine-hunter/gold/cosmology-chemistry/first_contrast_results.json','w') as fh:
    json.dump(out, fh, indent=1)
