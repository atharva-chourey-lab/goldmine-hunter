"""Resumable Gaia TAP join for the GALAH quality IDs. Progress in join_progress.json; rows appended to gaia_for_galah_sample.csv."""
import json, io, csv, os, time, requests
BASE=os.path.expanduser("~/workspace/goldmine-hunter/gold/gaia-chemistry")
meta=json.load(open(os.path.join(BASE,"galah_sample_meta.json")))
qids=meta["qids"]
OUT=os.path.join(BASE,"gaia_for_galah_sample.csv")
PROG=os.path.join(BASE,"join_progress.json")
done=0
if os.path.exists(PROG):
    done=json.load(open(PROG)).get("next_batch",0)
B=250
nb=(len(qids)+B-1)//B
print(f"total ids {len(qids)} batches {nb} resuming at batch {done}", flush=True)
TAP="https://gea.esac.esa.int/tap-server/tap/sync"
def gaia_batch(ids):
    idlist=",".join(str(i) for i in ids)
    adql=("SELECT ap.source_id, ap.mh_gspphot, ap.teff_gspphot, ap.logg_gspphot, ap.ag_gspphot, ap.ebpminrp_gspphot, "
          "ap.mh_gspspec, ap.teff_gspspec, ap.logg_gspspec, ap.alphafe_gspspec, gs.phot_g_mean_mag, gs.bp_rp "
          "FROM gaiadr3.astrophysical_parameters AS ap JOIN gaiadr3.gaia_source AS gs ON ap.source_id=gs.source_id "
          f"WHERE ap.source_id IN ({idlist})")
    r=requests.post(TAP, data={"REQUEST":"doQuery","LANG":"ADQL","FORMAT":"csv","QUERY":adql}, timeout=120)
    if r.status_code!=200:
        raise RuntimeError(f"Gaia batch failed {r.status_code}: {r.text[:400]}")
    return list(csv.DictReader(io.StringIO(r.text))), adql

fieldnames=None
mode="a" if done>0 and os.path.exists(OUT) else "w"
with open(OUT, mode, newline="") as f:
    w=None
    if mode=="w":
        pass
    for b in range(done, nb):
        rows, adql = gaia_batch(qids[b*B:(b+1)*B])
        if w is None:
            if mode=="w":
                fieldnames=list(rows[0].keys()) if rows else ["source_id","mh_gspphot","teff_gspphot","logg_gspphot","ag_gspphot","ebpminrp_gspphot","mh_gspspec","teff_gspspec","logg_gspspec","alphafe_gspspec","phot_g_mean_mag","bp_rp"]
                w=csv.DictWriter(f, fieldnames=fieldnames); w.writeheader()
            else:
                # read header from existing file
                with open(OUT) as hf: fieldnames=next(csv.reader(hf))
                w=csv.DictWriter(f, fieldnames=fieldnames)
        w.writerows(rows); f.flush()
        json.dump({"next_batch":b+1,"query_template":"see gaia_join.py gaia_batch()","last_adql_example":adql[:300]}, open(PROG,"w"))
        print(f"batch {b+1}/{nb} +{len(rows)}", flush=True)
        time.sleep(0.3)
print("DONE")
