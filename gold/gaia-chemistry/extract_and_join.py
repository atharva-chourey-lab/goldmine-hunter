"""Extract GALAH sample from truncated FITS, query Gaia TAP by dr3_source_id in batches,
compute first Gaia-GALAH metallicity contrast. Flags declared in output JSON."""
import warnings, json, io, csv, os, sys, time
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.expanduser("~/workspace/goldmine-hunter/tools-venv/lib/python3.12/site-packages"))
from astropy.io import fits
import numpy as np, requests

BASE=os.path.expanduser("~/workspace/goldmine-hunter/gold/gaia-chemistry")
# --- GALAH extraction ---
hdul=fits.open(os.path.join(BASE,"galah_dr3_first16120rows.fits"), ignore_missing_end=True)
data=hdul[1].data
print("rows readable from truncated file:", len(data))
cols=["dr3_source_id","teff","logg","fe_h","e_fe_h","flag_fe_h","flag_sp","alpha_fe","ebv"]
arr={c: np.array(data[c]) for c in cols}
# also ra/dec proxies? GALAH DR3 has ra_dr2/dec_dr2
arr["ra_dr2"]=np.array(data["ra_dr2"]); arr["dec_dr2"]=np.array(data["dec_dr2"])
n=len(data)
print("dr3_source_id null/zero:", int(np.sum(arr["dr3_source_id"]<=0)))
# quality sample: flag_sp==0 and flag_fe_h==0, fe_h finite
mask=(arr["flag_sp"]==0)&(arr["flag_fe_h"]==0)&np.isfinite(arr["fe_h"])&(arr["dr3_source_id"]>0)
print("quality GALAH rows (flag_sp==0, flag_fe_h==0):", int(mask.sum()), "of", n)
# save GALAH sample csv (all readable rows, quality flag marked)
with open(os.path.join(BASE,"galah_sample.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(cols+["ra_dr2","dec_dr2","quality"])
    for i in range(n):
        w.writerow([arr[c][i] for c in cols]+[arr["ra_dr2"][i],arr["dec_dr2"][i], int(mask[i])])
qids=[int(x) for x in arr["dr3_source_id"][mask]]
print("quality ids to query in Gaia:", len(qids), "unique:", len(set(qids)))
json.dump({"galah_rows_readable":int(n),"galah_quality":int(mask.sum()),"qids":qids}, open(os.path.join(BASE,"galah_sample_meta.json"),"w"))

# --- Gaia TAP join by source_id, batches of 400 ---
TAP="https://gea.esac.esa.int/tap-server/tap/sync"
def gaia_batch(ids):
    idlist=",".join(str(i) for i in ids)
    adql=("SELECT ap.source_id, ap.mh_gspphot, ap.teff_gspphot, ap.logg_gspphot, ap.ag_gspphot, ap.ebpminrp_gspphot, "
          "ap.mh_gspspec, ap.teff_gspspec, ap.logg_gspspec, ap.alphafe_gspspec, gs.phot_g_mean_mag, gs.bp_rp "
          "FROM gaiadr3.astrophysical_parameters AS ap JOIN gaiadr3.gaia_source AS gs ON ap.source_id=gs.source_id "
          f"WHERE ap.source_id IN ({idlist})")
    r=requests.post(TAP, data={"REQUEST":"doQuery","LANG":"ADQL","FORMAT":"csv","QUERY":adql}, timeout=180)
    if r.status_code!=200:
        print("Gaia batch FAILED", r.status_code, r.text[:500]); return []
    rows=list(csv.DictReader(io.StringIO(r.text)))
    return rows

allrows=[]
B=400
for i in range(0, len(qids), B):
    rows=gaia_batch(qids[i:i+B])
    allrows.extend(rows)
    print(f"batch {i//B+1}/{(len(qids)+B-1)//B}: +{len(rows)} cumulative {len(allrows)}", flush=True)
    time.sleep(0.5)
with open(os.path.join(BASE,"gaia_for_galah_sample.csv"),"w",newline="") as f:
    if allrows:
        w=csv.DictWriter(f, fieldnames=list(allrows[0].keys())); w.writeheader(); w.writerows(allrows)
print("Gaia rows returned:", len(allrows))
withgspphot=sum(1 for r in allrows if r.get("mh_gspphot") not in (None,""))
withgspspec=sum(1 for r in allrows if r.get("mh_gspspec") not in (None,""))
print("with mh_gspphot:", withgspphot, " with mh_gspspec:", withgspspec)
