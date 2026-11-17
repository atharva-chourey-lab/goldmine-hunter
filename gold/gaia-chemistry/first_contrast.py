"""FIRST CONTRAST: Gaia mh_gspphot / mh_gspspec minus GALAH DR3 fe_h.
Sample: GALAH DR3 main allstar FIRST 16,120 rows in file order (NOT random),
quality = flag_sp==0 AND flag_fe_h==0 AND finite fe_h AND dr3_source_id>0 (n=7,698),
joined by dr3_source_id = Gaia DR3 source_id via Gaia TAP (31 batches x 250, all returned).
Declared mismatches: Gaia mh is [M/H] (global metallicity), GALAH fe_h is [Fe/H];
for alpha-enhanced stars [M/H] > [Fe/H] by ~ +0.1-0.2 dex at low [Fe/H] (alpha term),
so a positive offset at metal-poor end is PARTLY definitional, not pure bias. GSP-Spec values are
UNCALIBRATED as published (Recio-Blanco+2023 calibrations NOT applied). No extinction cut
in headline; extinction bins use Gaia's own ag_gspphot (same pipeline - circularity declared).
"""
import csv, json, os, statistics as st
BASE=os.path.expanduser("~/workspace/goldmine-hunter/gold/gaia-chemistry")
galah={r["dr3_source_id"]: r for r in csv.DictReader(open(os.path.join(BASE,"galah_sample.csv"))) if r["quality"]=="1"}
gaia=list(csv.DictReader(open(os.path.join(BASE,"gaia_for_galah_sample.csv"))))
def f(x):
    try: return float(x)
    except: return None
pairs=[]
for g in gaia:
    sid=g["source_id"]; gal=galah.get(sid)
    if not gal: continue
    pairs.append({
        "source_id": sid,
        "fe_h_galah": f(gal["fe_h"]), "teff_galah": f(gal["teff"]), "logg_galah": f(gal["logg"]),
        "alpha_fe_galah": f(gal["alpha_fe"]), "ebv_galah": f(gal["ebv"]),
        "mh_gspphot": f(g["mh_gspphot"]), "teff_gspphot": f(g["teff_gspphot"]), "logg_gspphot": f(g["logg_gspphot"]),
        "ag_gspphot": f(g["ag_gspphot"]), "mh_gspspec": f(g["mh_gspspec"]), "alphafe_gspspec": f(g["alphafe_gspspec"]),
        "phot_g": f(g["phot_g_mean_mag"]), "bp_rp": f(g["bp_rp"]),
    })
print("joined pairs:", len(pairs))
def med(vals): return round(st.median(vals),3) if vals else None
def summ(name, rows, key_gaia, key_ref="fe_h_galah"):
    d=[r[key_gaia]-r[key_ref] for r in rows if r[key_gaia] is not None and r[key_ref] is not None]
    return {"subset": name, "n": len(d), "median_diff": med(d),
            "p16": round(sorted(d)[len(d)//6],3) if d else None, "p84": round(sorted(d)[5*len(d)//6],3) if d else None}
out={"n_pairs": len(pairs)}
out["gspphot_all"]=summ("all quality", pairs, "mh_gspphot")
out["gspspec_all"]=summ("all quality (gspspec subset)", pairs, "mh_gspspec")
# bins by GALAH fe_h
bins=[(-3,-2),(-2,-1.5),(-1.5,-1),(-1,-0.5),(-0.5,0),(0,0.6)]
out["by_feh_gspphot"]=[{**summ(f"fe_h {a}..{b}", [r for r in pairs if r["fe_h_galah"] is not None and a<=r["fe_h_galah"]<b], "mh_gspphot"), "bin":f"{a}..{b}"} for a,b in bins]
out["by_feh_gspspec"]=[{**summ(f"fe_h {a}..{b}", [r for r in pairs if r["fe_h_galah"] is not None and a<=r["fe_h_galah"]<b], "mh_gspspec"), "bin":f"{a}..{b}"} for a,b in bins]
# giants vs dwarfs by GALAH logg
out["giants_logg_lt2.5_gspphot"]=summ("giants logg<2.5", [r for r in pairs if r["logg_galah"] is not None and r["logg_galah"]<2.5], "mh_gspphot")
out["subgiants_2.5_3.5_gspphot"]=summ("logg 2.5-3.5", [r for r in pairs if r["logg_galah"] is not None and 2.5<=r["logg_galah"]<3.5], "mh_gspphot")
out["dwarfs_logg_ge3.5_gspphot"]=summ("dwarfs logg>=3.5", [r for r in pairs if r["logg_galah"] is not None and r["logg_galah"]>=3.5], "mh_gspphot")
out["giants_gspspec"]=summ("giants logg<2.5 gspspec", [r for r in pairs if r["logg_galah"] is not None and r["logg_galah"]<2.5], "mh_gspspec")
out["dwarfs_gspspec"]=summ("dwarfs logg>=3.5 gspspec", [r for r in pairs if r["logg_galah"] is not None and r["logg_galah"]>=3.5], "mh_gspspec")
# teff bins (GALAH teff)
tbins=[(3500,4500),(4500,5500),(5500,6500),(6500,8000)]
out["by_teff_gspphot"]=[{**summ(f"teff {a}..{b}", [r for r in pairs if r["teff_galah"] is not None and a<=r["teff_galah"]<b], "mh_gspphot"), "bin":f"{a}..{b}"} for a,b in tbins]
# extinction bins by Gaia ag_gspphot
abins=[(0,0.5),(0.5,1),(1,2),(2,10)]
out["by_ag_gspphot"]=[{**summ(f"Ag {a}..{b}", [r for r in pairs if r["ag_gspphot"] is not None and a<=r["ag_gspphot"]<b], "mh_gspphot"), "bin":f"{a}..{b}"} for a,b in abins]
out["n_with_gspphot"]=sum(1 for r in pairs if r["mh_gspphot"] is not None)
out["n_with_gspspec"]=sum(1 for r in pairs if r["mh_gspspec"] is not None)
out["feh_range_galah"]=[min(r["fe_h_galah"] for r in pairs), max(r["fe_h_galah"] for r in pairs)]
out["n_vmp_feh_lt_-2"]=sum(1 for r in pairs if r["fe_h_galah"]<-2)
out["n_mp_feh_lt_-1"]=sum(1 for r in pairs if r["fe_h_galah"]<-1)
json.dump(out, open(os.path.join(BASE,"first_contrast_results.json"),"w"), indent=2)
print(json.dumps(out, indent=2))
