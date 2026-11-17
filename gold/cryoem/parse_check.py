import mrcfile, numpy as np, json, gzip
def parse_map(path, contour):
    with mrcfile.open(path, permissive=True) as m:
        h=m.header; d=m.data
        vox=tuple(float(x) for x in m.voxel_size.tolist()) if hasattr(m.voxel_size,'tolist') else m.voxel_size
        origin=(float(h.origin.x),float(h.origin.y),float(h.origin.z))
        stats=dict(shape=d.shape, dtype=str(d.dtype), voxel_A=[round(float(v),4) for v in m.voxel_size.tolist()],
                   origin=origin, min=float(d.min()), max=float(d.max()), mean=float(d.mean()), std=float(d.std()))
        above=d>contour
        stats["author_contour"]=contour
        stats["frac_voxels_above_contour"]=round(float(above.mean()),5)
        idx=np.argwhere(above)
        if len(idx):
            lo=idx.min(axis=0); hi=idx.max(axis=0)
            vs=np.array(m.voxel_size.tolist(),dtype=float)
            # data axes are (z,y,x); header dims col=x,row=y,sec=z
            ext_A=(hi-lo+1)*vs[::-1]
            stats["density_bbox_extent_A_zyx"]=[round(float(x),1) for x in ext_A]
            stats["density_volume_A3_at_contour"]=round(float(above.sum()*np.prod(vs)),0)
        return stats
def parse_pdb(path):
    coords=[]; bfac=[]; chains=set(); res=set()
    for line in open(path):
        if line.startswith(("ATOM  ","HETATM")):
            coords.append((float(line[30:38]),float(line[38:46]),float(line[46:54])))
            bfac.append(float(line[60:66])); chains.add(line[21]); res.add((line[21],line[22:26]))
    c=np.array(coords)
    return dict(atoms=len(c), chains=sorted(chains), residues=len(res),
                extent_A=[round(float(x),1) for x in (c.max(axis=0)-c.min(axis=0))],
                centroid=[round(float(x),1) for x in c.mean(axis=0)],
                coord_min=[round(float(x),1) for x in c.min(axis=0)], coord_max=[round(float(x),1) for x in c.max(axis=0)],
                bfactor_mean=round(float(np.mean(bfac)),2), bfactor_min=round(float(np.min(bfac)),2))
out={}
# contours from EMDB metadata
meta={10000:0.013, 76805:None, 22805:None}
for eid in ["10000","76805","22805"]:
    d=json.load(open(f"api/EMD-{eid}.json"))
    cl=d["map"].get("contour_list",{}).get("contour",[{}])
    meta[eid]=cl[0].get("level") if cl else None
    res=[ip.get("final_reconstruction",{}).get("resolution",{}).get("valueOf_") for s in d["structure_determination_list"]["structure_determination"] for ip in s.get("image_processing",[])]
    out[f"EMD-{eid}"]={"title":d["admin"]["title"],"reported_resolution_A":res,"pdb_list":(d.get("crossreferences",{}).get("pdb_list") or None)}
    out[f"EMD-{eid}"]["map_parse"]=parse_map(f"maps/emd_{eid}.map.gz", meta[eid] if meta[eid] is not None else 0.05)
out["PDB-7KC2"]={"deposited_model_for_EMD-22805": parse_pdb("models/7kc2.pdb")}
out["AF-S5RZC2"]={"alphafold_for_7KC2_uniprot": parse_pdb("alphafold/AF-S5RZC2-F1-model_v6.pdb")}
af=out["AF-S5RZC2"]["alphafold_for_7KC2_uniprot"]
out["AF-S5RZC2"]["plddt_note"]="B-factor column in AF PDB = pLDDT per residue/atom"
out["AF-P69905-HBA"]={"alphafold_human_hemoglobin_alpha": parse_pdb("alphafold/AF-P69905-F1-model_v6.pdb")}
print(json.dumps(out, indent=1))
json.dump(out, open("first_check_results.json","w"), indent=1)
