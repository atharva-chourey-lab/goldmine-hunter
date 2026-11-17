import os, re, json
import numpy as np, pandas as pd
from scipy import stats
DATA=os.path.expanduser("~/workspace/rhino-pair-first-computation/data/pts")
OUT=os.path.expanduser("~/workspace/goldmine-hunter/gold/morpho-ct/epmc-rhino5")
os.makedirs(OUT, exist_ok=True)
BONES=["Humerus","Radius","Ulna","Femur","Tibia","Fibula"]
def read_pts(p):
    lines=[l.strip() for l in open(p) if l.strip()]
    n=int(lines[1]); pts=[]
    for l in lines[2:]:
        s=l.split(); pts.append([float(s[1]),float(s[2]),float(s[3])])
    a=np.array(pts); assert a.shape[0]==n; return a
def cs(a):
    c=a.mean(axis=0); return float(np.sqrt(((a-c)**2).sum()))
rows=[]
pat=re.compile(r"([A-Z][a-z]+_[a-z]+)_(.+)_(Humerus|Radius|Ulna|Femur|Tibia|Fibula)(_miroir)?\.pts")
for bone in BONES:
    d=os.path.join(DATA,bone)
    for fn in sorted(os.listdir(d)):
        if "LM_surface" in fn or not fn.endswith(".pts"): continue
        m=pat.match(fn)
        if not m: print("NOMATCH",fn); continue
        a=read_pts(os.path.join(d,fn))
        rows.append(dict(species=m.group(1),specimen=m.group(2),bone=bone,n_points=len(a),CS=cs(a)))
df=pd.DataFrame(rows); df.to_csv(os.path.join(OUT,"centroid_sizes_all5.csv"),index=False)
print(df.groupby(["species","bone"]).size().unstack(fill_value=0))
print("point counts per bone:", df.groupby(["bone","n_points"]).size().to_dict())
wide=df.pivot_table(index=["species","specimen"],columns="bone",values="CS")
print("\nspecimens total per species:", wide.reset_index().groupby("species").size().to_dict())
ge5=wide.dropna(thresh=5); print(">=5 bones:", ge5.reset_index().groupby("species").size().to_dict())
complete=wide.dropna(); print("complete 6:", complete.reset_index().groupby("species").size().to_dict())
logw=np.log10(ge5); prof=logw.sub(logw.mean(axis=1),axis=0)
prof.to_csv(os.path.join(OUT,"profiles_all5_ge5.csv"))
# complete-6 profiles for primary pairwise tests
logc=np.log10(complete); profc=logc.sub(logc.mean(axis=1),axis=0)
profc.to_csv(os.path.join(OUT,"profiles_all5_complete6.csv"))
print("\nMean profiles (complete-6):")
print(profc.groupby(level=0).mean().round(4).to_string())
rng=np.random.default_rng(42)
def perm_dist(a,b,nperm=10000):
    obs=float(np.linalg.norm(a.mean(0)-b.mean(0))); pooled=np.vstack([a,b]); n1=len(a); cnt=0
    for _ in range(nperm):
        idx=rng.permutation(len(pooled))
        if np.linalg.norm(pooled[idx[:n1]].mean(0)-pooled[idx[n1:]].mean(0))>=obs-1e-12: cnt+=1
    return obs,(cnt+1)/(nperm+1)
pairs=[]
sp_list=list(profc.index.get_level_values(0).unique())
for i in range(len(sp_list)):
    for j in range(i+1,len(sp_list)):
        a=profc.loc[sp_list[i]].to_numpy(); b=profc.loc[sp_list[j]].to_numpy()
        d,p=perm_dist(a,b)
        pairs.append(dict(sp1=sp_list[i],sp2=sp_list[j],n1=len(a),n2=len(b),dist=round(d,4),perm_p=p))
pairs_df=pd.DataFrame(pairs); pairs_df.to_csv(os.path.join(OUT,"pairwise_profile_tests.csv"),index=False)
print("\nPairwise complete-6 profile distances:")
print(pairs_df.to_string(index=False))
# Forearm focus: radius+ulna profile mean per species (ge5)
fore=prof[["Radius","Ulna"]].mean(axis=1)
print("\nForearm (Radius+Ulna profile, >=5):")
print(fore.groupby(level=0).agg(["count","mean","std"]).round(4).to_string())
json.dump({"ge5":ge5.reset_index().groupby("species").size().to_dict(),"complete6":complete.reset_index().groupby("species").size().to_dict(),"pairwise":pairs},open(os.path.join(OUT,"rhino5_results.json"),"w"),indent=2)
