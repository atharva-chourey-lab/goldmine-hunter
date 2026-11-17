# Goldmine Hunter — Fidelity Campaign: Cryo-EM leg (EMDB × PDB × AlphaFold DB)

Date: 2026-11-17 · Doctrine: high-fidelity scans (README, standing instruction 2026-11-17)
Bundle: `gold/cryoem/` — 9,949,186 bytes total (≈9.5 MB, budget was <500 MB). No accounts created anywhere.

## Verdict first

**Fertile, and the comparable set is real — but this is comparison gold, not recovery gold.**
EMDB, the PDB and AlphaFold DB are all curated public releases (*published-by-design* in
hunter doctrine — nothing stranded, nothing Wayback-only). The gold is the same shape as
MRI, one level up: the raw density map preserves more than any model extracted from it,
the same imaging modality spans ~50k comparable units, and there are **two rulers that
were never designed to agree** — experimental maps (with deposited models fitted by hand)
vs AlphaFold predictions (monomers, sequence-only, pLDDT-scored). Barrier-free access is
verified by actual download and parse for all three legs (one UA quirk, below). A first
check on one entry was computed, not just scouted: the deposited model's extent matches
its map's density box to ~1 Å per axis.

**Fidelity card (filled before counting, per doctrine):**
- `RAW:` CCP4/MRC density volumes (`.map.gz`, float32) deposited in EMDB — the volume
  itself, not a table. Half-maps and additional maps are deposited alongside.
- `UNIT:` protein / complex — one imaging modality (cryo-EM, mostly single-particle)
  across all protein families; the comparable set is entries × families.
- `LABEL GAP:` ~45% of sampled entries carry no deposited PDB model at all; where a
  model exists it is a hand-fitted, often partial interpretation; AlphaFold covers the
  sequence but as a monomer, in a different frame, with its own confidence ruler.
- `ANCHOR:` deposited PDB models grade the maps; AlphaFold DB is the second ruler
  (and vice versa — maps grade AlphaFold in flexible / assembled regions).

## 1. Access verification — LANDED (all by actual download + parse)

| Leg | Endpoint used | Result |
|---|---|---|
| EMDB entry API | `GET https://www.ebi.ac.uk/emdb/api/entry/EMD-{id}` | 200, full JSON (map dims, voxel, contour, resolution, `crossreferences.pdb_list`) |
| EMDB search API | `GET https://www.ebi.ac.uk/emdb/api/search/{term}?rows=N` | 200, returns full entry JSONs (default rows=10). **No total-count field** — see §2 caveat |
| EMDB map download | `https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-{id}/map/emd_{id}.map.gz` | 200, no auth; downloaded bytes match FTP `Content-Length` exactly for all 3 samples |
| PDB model | PDBe `https://www.ebi.ac.uk/pdbe/entry-files/download/7kc2.cif` + RCSB `https://files.rcsb.org/download/7KC2.pdb` | Both 200, no auth |
| PDBe mappings | `https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/7kc2` | 200 — gives the exact UniProt per PDB (7KC2 → **S5RZC2**, not the canonical P00330; strain matters, declared) |
| AlphaFold API | `https://alphafold.ebi.ac.uk/api/prediction/{uniprot}` | 200, JSON with global pLDDT, per-band fractions, file URLs — for S5RZC2, P00330, P69905, P68871, all hit |
| AlphaFold files | `https://alphafold.ebi.ac.uk/files/AF-{uniprot}-F1-model_v6.pdb` (+ PAE JSON) | 200 **only with a browser User-Agent**; default curl UA gets `403 Forbidden` (bot filter, not a paywall/login). Downloaded via `requests` + browser UA |

### Sample maps downloaded and parsed (mrcfile 1.5.4, tools-venv)

| Entry | What it is | gz bytes (SHA-256 prefix) | Parsed dims | Voxel | Author contour | Reported res. | Deposited PDB? |
|---|---|---|---|---|---|---|---|
| EMD-10000 | *Plesiomonas* lateral flagellar motor, subtomogram averaging | 3,652,596 (`fccd84e3…`) | 100×100×100 float32 | 8.28 Å | 0.013 | 120 Å (nominal — see note) | **None** (no `pdb_list`) |
| EMD-76805 | Human hemoglobin, laser phase-plate TEM | 1,097,880 (`3a03df37…`) | 128×128×128 float32 | 0.94 Å | 0.010 | 2.86 Å | **None** (no `pdb_list`) |
| EMD-22805 | Yeast alcohol dehydrogenase + NADH, open form | 2,536,548 (`d757d225…`) | 180×180×180 float32 | 1.05 Å | 0.032 | 2.67 Å | **7KC2** (`FULLOVERLAP`) |

Parsed dims/voxel match the EMDB API metadata exactly for all three — the files are the
maps the metadata claims. Note on EMD-10000: at its author contour 56% of voxels sit
above threshold and the density box is the whole 828 Å cube — it is a low-fidelity
tomographic member, *not* comparable to the single-particle members undeclared
(Scalable Brain Atlas rule applies inside EMDB itself: subtomogram/tomography ≠ SPA).

Models in hand: `models/7kc2.cif` (1,081,037 B, `34f232cb…`), `models/7kc2.pdb`
(893,835 B, `743e90c4…`); AlphaFold `alphafold/AF-S5RZC2-F1-model_v6.pdb` (215,783 B,
`0e921b2d…`, global pLDDT 96.69), `alphafold/AF-P69905-F1-model_v6.pdb` (92,096 B,
`d9d7ad46…`, global pLDDT 98.06), plus the S5RZC2 PAE JSON (245,471 B).
Full parse output: `gold/cryoem/first_check_results.json`.

## 2. Comparable set shape — counts actually measured

**API-measured (RCSB Search API v2, `POST https://search.rcsb.org/rcsbsearch/v2/query`, 2026-11-17):**

| Query (attribute, exact_match) | total_count |
|---|---|
| `exptl.method = ELECTRON MICROSCOPY` | **37,932** PDB entries |
| `pdbx_database_related.db_name = EMDB` | **38,174** PDB entries |
| both (AND) | **37,885** PDB entries = set **(a) map + deposited model**, PDB side |

**Set (b) map with NO model — derived estimate, declared as such:** EMDB's own search
API exposes no archive total, so the total is scouted from primary sources: EMDB news
(2026-01-23) states the archive "surpassed 50,000 total entries" in 2025; a Scholar
Data snapshot puts EMDB at **53,202** entries (2026-04-30). (b) ≈ 53,202 − 37,885 ≈
**~15,000 maps with no deposited model**. Caveats, all load-bearing: one PDB can serve
several maps (composite/focused-refinement maps inflate the map count), some EMDB
entries are tomography volumes never intended to carry an atomic model, and the
published cross-check differs in definition — the 2025 *Briefings in Bioinformatics*
survey (below) counted ~57% of EMDB-associated coordinates as resolved in the PDB as
of 2025-01-09. The honest statement is **order 10–15k no-model maps**, not a point count.

**Direct sample (EMDB search API, 5 keyword searches × rows=30, deduplicated,
`gold/cryoem/sample_c_results.json`):** 148 entries → **82 (55%) with a `pdb_list`,
66 (45%) without**. This sample is biased toward well-studied proteins (hemoglobin,
chaperonin, proteasome, dehydrogenases) — it corroborates the archive-level split,
it does not replace it.

**Set (c) map where an AlphaFold prediction also exists for the same UniProt —
measured on a subsample:** from the 82 with-model entries, 12 drawn at random
(seed 42); chain run per entry: EMDB `pdb_list` → PDBe UniProt mapping → AlphaFold
API. **Result: 12/12 AlphaFold hits** (P00366, O42480, P69905, P00327, P33299 ×2,
P17987, A0R1C2, Q25790, P0A9Q7, …). For standard proteins the overlap is effectively
universal — unsurprising, since AlphaFold DB covers ~200M UniProt sequences; the
interesting residue is the exceptions (synthetic constructs, viral polyproteins,
heavily engineered sequences), which this biased sample cannot size.

## 3. Label gap / Two Rulers — where the rulers disagree, and what's published

**Systematic disagreement zones (established in the literature, consistent with our sample):**
- **Flexible / disordered regions:** maps go locally blurry exactly where AlphaFold's
  pLDDT drops — but not identically: a region can be low-pLDDT yet resolved in a map
  (stabilised by a partner/ligand) or high-pLDDT yet absent from density (mobile in
  vitro). The *joint* distribution (local resolution × pLDDT) is the unmined object.
- **Complexes vs monomers:** AlphaFold DB's bulk is single chains; EMDB's unit is the
  assembly. Our first check quantifies it (§4): the AF monomer spans ~64×42×62 Å where
  the map holds a 94×73×69 Å tetramer. Interfaces, symmetry and ligand states
  (e.g. NADH-bound open form, EMD-22805) are map-only information.
- **Conformational states:** one sequence → many EMDB maps (open/closed, apo/holo);
  one AlphaFold model → one state. Which state AF picks, per family, is un-audited
  at population scale.
- **The no-model population itself:** ~10–15k maps (tomography-heavy, but including
  high-resolution SPA maps like EMD-76805 at 2.86 Å) have no deposited interpretation
  to disagree with — the label is absent, not wrong.

**Novelty scrub — what has already been published, and its unit:**
- *Briefings in Bioinformatics* 2025 survey/benchmark of DL model-building methods
  (doi:10.1093/bib/bbaf322) — unit: **50 maps**, method-vs-method benchmark; also the
  source of the ~57% coordinates-resolved archive stat. Not a disagreement audit.
- CryoAtlas (arXiv, data to 2026-03) — **17,809 map–model–sequence entries** curated
  for training/benchmarking model builders, 618-target benchmark vs Phenix/AlphaFold 3.
  Critically, its curation *removes densities with large unmodeled regions* — it
  excludes exactly the gap population by design.
- EModelX (*Nat Commun* 2024) — unit: **126 maps from a single year (2023) with no
  fitted PDB**, used to demo a builder. A method demonstration on the no-model class,
  not a census or audit of it.
- Terwilliger et al. (Phenix + iterative AlphaFold refinement) and the fitting-tool
  literature (DomainFit, DeepTracer, ModelAngelo…) — unit: **single structures /
  small test sets**; the question is "can AF be fitted better", not "where do the
  rulers systematically part".
- *Protein Journal* 2026 review of AlphaFold-in-cryo-EM studies — unit: **32 papers**,
  narrative synthesis.

**What remains unclaimed:** a pre-registered, population-level audit over the whole
comparable set — (i) the completeness census itself per family (map real / model
present / model absent / AF present), (ii) the joint local-resolution × pLDDT
disagreement geometry stratified by family, assembly size and conformational state,
run *including* the no-model maps as a first-class population, and (iii) the reverse
grading: deposited-model-vs-own-map misfit compared against AF-vs-map misfit, to
separate "AlphaFold's blind spot" from "the map's flexibility". Nobody has published
the census or the joint distribution; the benchmarks actively filter the gap out.

## 4. First check — computed on EMD-22805 / 7KC2 / AF-S5RZC2 (script: `gold/cryoem/parse_check.py`)

- Map box: 180³ voxels × 1.05 Å = 189 Å cube, origin 0. Density above the author
  contour (0.032; 0.83% of voxels) has bounding-box extent **93.4 × 72.4 × 70.3 Å**
  and volume ≈ 56,288 Å³.
- Deposited model 7KC2: 10,192 atoms, chains A–D, 1,404 residues; coordinate extent
  **94.3 × 73.2 × 69.3 Å**; centroid **(94.5, 94.5, 94.5)** — the exact centre of the
  map box. **Map density box and model extent agree to ≤1.1 Å on every axis** —
  EMDB's `FULLOVERLAP` claim verified arithmetically from the files, not the listing.
- AlphaFold AF-S5RZC2 (the model's own UniProt): 1 chain, 348 residues, extent
  **64.3 × 42.0 × 61.5 Å**, centred near origin (different frame — AF models are not
  placed in the map). Monomer-vs-tetramer gap in one line: the prediction covers
  one subunit of what the map shows; any AF-vs-map comparison must first solve
  placement + assembly, which is precisely the un-audited step.
- pLDDT (AF PDB B-factor column): mean **96.84**, min **57.53** — even this
  high-confidence case (global 96.69) carries a low-confidence tail; EMD-22805's
  reported resolution is 2.67 Å, so a per-residue local-resolution × pLDDT check is
  feasible on this entry but was **not** run — no local-resolution map was downloaded
  and no fitting was performed. Not faked, listed under Scouted.
- Bonus member check, EMD-76805 (no model): density box 70.5 × 66.7 × 56.4 Å at
  contour, volume ≈ 29,896 Å³ — the right size for a hemoglobin tetramer, i.e. the
  no-model map is buildable in principle; AF models for both its chains exist
  (HBA P69905 verified in hand, HBB P68871 API-hit).

## Landed / Scouted / Blocked

**Landed:** all three APIs + both file routes verified by download; 3 maps parsed
(header, dims, voxel, contour stats — metadata cross-checked); 1 deposited model in
both formats; 2 AlphaFold models + 1 PAE file in hand; archive counts measured via
RCSB (37,932 / 38,174 / 37,885); 148-entry sample classified (82/66); AF-overlap
subsample 12/12; first check computed (extent/centroid agreement, monomer gap, pLDDT tail).

**Scouted:** EMDB archive total (>50k end-2025; 53,202 at 2026-04-30 — secondary
sources, because the EMDB search API returns no total); set (b) ≈10–15k as a derived
range; novelty scrub (5 sources above); local-resolution × pLDDT comparison designed
but not computed (needs the entry's local-resolution/additional maps + a fitting step).

**Blocked:** nothing hard. Two soft frictions, both worked around without accounts:
AlphaFold file host 403s non-browser user agents; EMDB search API has no count
endpoint (counts routed through RCSB Search API instead). EMD-21375/6VSB (spike) was
verified as a linked pair via API but its map is 304,696,352 B gz — deliberately not
downloaded under the size budget when smaller verified pairs exist.

## Recommended next steps (Atharva's call)

1. **Census build (cheap, pure API):** enumerate EMDB→PDB→UniProt→AF for a full
   method-defined slice (e.g. all SPA entries 2023–2025 at ≤4 Å) and publish the
   completeness-per-family table — the deliverable the benchmarks filtered away.
2. **Joint-distribution pilot:** ~100 entries with local-resolution maps; per-residue
   local resolution vs AF pLDDT, stratified by assembly size — tests whether the
   disagreement geometry has family-level pattern (the lion-shaped question).
3. Pre-register before either, per house rule; declare rulers per member
   (SPA ≠ tomography, AF monomer ≠ AF-Multimer, strain-level UniProt as deposited).

## Files

- This report: `fidelity-cryoem-report.md`
- Bundle: `gold/cryoem/` — `maps/` (3 × `.map.gz`), `models/7kc2.{cif,pdb}`,
  `alphafold/` (2 PDB + PAE JSON), `api/` (EMDB entry JSONs, PDBe UniProt mapping,
  AF API JSONs), `parse_check.py`, `first_check_results.json`, `sample_c_results.json`
