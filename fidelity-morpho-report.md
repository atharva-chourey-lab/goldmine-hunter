# Fidelity Campaign — Morpho-CT leg: the NEXT gold after the rhino pair

Date: 2026-11-17 · Doctrine: RAW kept + one protocol across many comparable
units + labels incomplete/stranded/second-ruler + local anchor.
Provenance classes used honestly throughout. No accounts created.
Total new downloads this leg: ~24 KB (well under the 500 MB cap) — the
winning set was already on disk from the rhino computation.

## Verdict first

**The next gold is not a new repository. It is the other three species
inside the dataset we already proved.** Mallet et al. 2019 Supp. 9 —
downloaded barrier-free via Europe PMC for the rhino pair — contains
landmarks for **all five living rhinos**, same Gravibone protocol, same
six long bones, identical landmark configurations per bone. The pair
computation used two species and left three on the table. I ran the
pre-registered profile metric across all five today: **all 10 pairwise
profile distances are significant** (permutation p ≤ 0.04), and the
largest separation is a pair nobody has touched —
*Diceros bicornis* vs *Rhinoceros unicornis* (0.0566 log₁₀, p=0.0014).
Everything else in this system is either free-account-gated, n=1,
mismatched, or (CrocBase) currently missing its scans. Ranked detail below.

---

## 1. Access routes — verified today (LANDED evidence)

| Route | Status today | Evidence |
|---|---|---|
| **Europe PMC supplementary files** | **BARRIER-FREE, landed** | Rhino Supp. 9 `.pts` files (3,057,122 B, MD5 `0cae2df77ef81f06ea9e5b68076fc30c`, ex 51 MB EPMC zip MD5 `f07575f66b1af99ea0c1123613c2edd6`) re-parsed this leg: **308 files, every header/count asserted in code**. This is the route that bypasses MorphoSource entirely for Gravibone. |
| **OSF API (CrocBase)** | **BARRIER-FREE for metadata/list; scans ABSENT (see §3D)** | Specimen list downloaded unauthenticated: `gold/morpho-ct/osf-crocbase/specimen_list.xlsx`, 17,208 B, MD5 `f14960f51c6930394096568fdcdc0f2f` / SHA256 `02ae0453…e47` — **byte-identical to the hashes the OSF API itself publishes** for the file. Parses clean (openpyxl). |
| **DigiMorph direct files** | **BARRIER-FREE (where links live); one dead link found** | *Camelus dromedarius* page links `DICOM_Cranium.zip` directly on the DigiMorph host: HEAD = **200, Content-Length 188,810,442 B** — no account, no Box. *Elephas maximus* skull CT routes via a Box shared-static zip that now returns **404** — that file is currently unrecoverable by its published link (not downloaded; elephant remains a NON-pair, not revived). Pages saved: `gold/morpho-ct/digimorph/{camel,elephas}_page.html`. |
| **MorphoSource media download** | **FREE-ACCOUNT, not barrier-free** | Official membership doc + pyMorphoSource docs agree: guests may browse/search and use the 3D viewer; **downloading Open media requires a registered account + terms agreement + intended-use statement + captcha**; API download requires an account API key; Restricted media needs manager approval. Scripted access from this VM is additionally stopped by an **Anubis bot wall** — both the project page and a catalog `.csv` export returned the 7,435 B Anubis challenge page (`gold/morpho-ct/morphosource/gravibone_project.html`), not data. No bypass attempted, no account created. |
| **Phenome10k** | **BLOCKED from this VM (network)** | `phenome10k.org` returned curl code 000 (unreachable) from here. Literature (PNAS 2019 squamate paper) states its meshes are "freely available for download on Phenome10k and MorphoSource" — treat as scouted, needs a live-browser/alternate-network check. |

**Fidelity card — the system as a whole:**
RAW: CT/microCT DICOM stacks + surface meshes (.ply/.stl) + landmark
files · UNIT: specimen, same element set across taxa · LABEL GAP: papers
compute per-element shape from a fraction of each scan; cross-element
size allocation, endocast/labyrinth volumes, and full-mesh geometry are
mostly uncomputed · ANCHOR: published landmarks (Mallet 2019),
physical-caliper distances (baboon, below), dissection/literature values.

---

## 2. LANDED + COMPUTED — Candidate A: Gravibone, all five rhinos ★ #1

- **Comparable set:** same project (MorphoSource 000366286 / Gravibone),
  same Artec Eva surface protocol + 250k-vertex decimation, same 6 long
  bones (humerus, radius, ulna, femur, tibia, fibula), five taxa:
  *Ceratotherium simum* (Africa, savanna, ~2,300 kg), *Diceros bicornis*
  (Africa, savanna/clear forest, ~1,050 kg), *Rhinoceros unicornis*
  (Asia, floodplain, ~2,000 kg), *R. sondaicus* (Asia, dense forest,
  ~1,350 kg), *Dicerorhinus sumatrensis* (Asia, dense forest, ~775 kg).
- **Completeness (real, from the parsed files — not listings):**
  landmark counts are **constant within each bone across all species**
  (Humerus 674, Femur 639, Radius 416, Tibia 408, Ulna 364, Fibula 281),
  so centroid size is on identical configurations.

  | Species | specimens (any bone) | ≥5 of 6 bones | complete-6 |
  |---|---|---|---|
  | *C. simum* | 16 | 12 | 10 |
  | *D. sumatrensis* | 14 | 9 | 9 |
  | *D. bicornis* | 14 | 7 | **5** |
  | *R. sondaicus* | 8 | 7 | 7 |
  | *R. unicornis* | 11 | 9 | 7 |

  Total: 308 specimen-bone files. *D. bicornis* complete-6 n=5 is the
  weakest cell — declared, not hidden.
- **Label gap:** Mallet 2019 computed per-bone shape GMM, species mean
  shapes, NJ trees, and shape~centroid-size allometry per bone; Mallet
  2020 added cross-bone *shape* integration; Mallet 2022 extended
  per-bone shape vs mass to 69 rhinocerotoid taxa. **No CS value was
  ever tabulated and no within-specimen cross-bone size comparison was
  ever made** (rhino NOVELTY.md: full-text "integration"/"covariation"
  = 0 hits in the 2019 paper; this leg's searches found no later
  CS-profile/cross-element-ratio publication either).
- **Anchor:** Mallet's own landmark configurations + published per-bone
  results — the profile is graded inside the same ruler that produced
  the shape papers.
- **First computation (this leg, pipeline end-to-end, seed 42,
  10,000 permutations, complete-6 specimens):** script
  `gold/morpho-ct/epmc-rhino5/compute_rhino5.py`; outputs
  `centroid_sizes_all5.csv` (MD5 `18cdffe0…9c5`),
  `profiles_all5_complete6.csv`, `pairwise_profile_tests.csv`
  (MD5 `67e82c13…42d`), `rhino5_results.json`.

  | Pair | dist (log₁₀) | perm p |
  |---|---|---|
  | **D. bicornis – R. unicornis** | **0.0566** | 0.0014 |
  | D. bicornis – R. sondaicus | 0.0556 | 0.0017 |
  | C. simum – R. sondaicus | 0.0469 | 0.0002 |
  | R. sondaicus – R. unicornis | 0.0458 | 0.0011 |
  | D. sumatrensis – D. bicornis | 0.0376 | 0.0009 |
  | C. simum – R. unicornis (the proven pair, reproduced) | 0.0355 | 0.0001 |
  | D. sumatrensis – R. sondaicus | 0.0276 | 0.0002 |
  | D. sumatrensis – R. unicornis | 0.0263 | 0.0002 |
  | C. simum – D. bicornis | 0.0232 | 0.0400 |
  | C. simum – D. sumatrensis | 0.0223 | 0.0092 |

  Mean-profile shape: the forearm split found in the pair **generalises
  and sharpens** — *R. unicornis* has the most distal-light forelimb
  (Radius+Ulna profile, ≥5-bone specimens: −0.0450), *D. bicornis* the
  most distal-heavy (−0.0072), with *C. simum* (−0.0143),
  *D. sumatrensis* (−0.0243) and *R. sondaicus* (−0.0258) between.
  *R. sondaicus* vs *R. unicornis* is the cleanest single new contrast:
  **same genus, same continent, different habitat/mass — and they still
  separate by 0.0458 (p=0.0011)**, driven largely by humerus profile
  (+0.1586 vs +0.1296). That kills a pure-phylogeny reading of the pair
  result and is the headline the 5-species set buys.
- **Caveats (declared):** this extension was computed under the pair's
  pre-registered metric but was **not itself separately pre-registered**
  — treat pairwise p's as a strong scout result; register before any
  publication claim. CS is a landmark-configuration proxy (identical
  per bone, valid for profiles/ratios, not comparable as absolutes to
  mesh-based sizes). Sex unknown ~half the sample (Mallet's own limit).
- **Provenance:** published-by-design supplements, barrier-free via
  Europe PMC — a comparison gold, not a recovery. Say so plainly.

## 3. SCOUTED candidates

### B. SNPRC baboon crania — MorphoSource Project 00000C475 (n=985)
One protocol family (Siemens Biograph medical CT; slice spacing 0.60 /
0.75 mm in two tranches), one pedigreed hybrid colony
(*Papio hamadryas × anubis × cynocephalus*). **Not a two-taxon pair** —
its asset is n=985 within one population, with pedigree as anchor.
Label gap / second ruler, already partly claimed: Modesto-Mata et al.
2025 (PeerJ 13:e20172) found **182/985 scans (18.5%) carry inconsistent
slice-spacing metadata**, and validated the rest against physical
caliper Prosthion–Basion distances — so a naive GMM on the raw DICOMs
inherits a corrupted ruler for ~1 in 5 specimens. The slice-spacing
audit itself is **published — do not re-claim it**. What remains open:
a full cranial GMM run only on the validated subset, graded against the
caliper anchor. Access: free-account (above). **Scouted, not landed.**

### C. Copes et al. 2016 primate skulls — MorphoSource (MCZ)
The best *protocol* story after Gravibone: **489 scans / 431 specimens /
59 species, one scanner** (X-Tek HMXST225, Harvard CNS), crania +
mandibles, CC BY-NC, data paper (Sci Data 3:160001) that itself
computes **no comparative morphology** — the label gap is the whole
field's subsequent per-clade papers. But as a *matched pair* it fails
the n≥8 test on the obvious contrast: rhesus macaque n=3 in Copes
(baboon *Papio anubis* n=9 clears it, macaque does not). Viable shapes
instead: multi-species clade-level contrasts where several genera clear
n≥8, or Copes-as-one-ruler vs the SNPRC baboon DICOMs (different
scanner/resolution — declare, never pool undeclared). Access:
free-account only; no barrier-free route found this leg. **Scouted.**

### D. CrocBase crocodiles — OSF x38nh — specimen list landed, SCANS BLOCKED
Fidelity card promised gold: whole-body CT+MRI, one lab protocol, five
species. Reality today: the OSF node holds **only the About component
and the specimen list** — API children = [], storage = 1 file (the list,
hash-verified in §1). The list itself documents *C. niloticus* sections
(blog claim: 24 individuals, 0.127–298 kg — an ontogenetic series, the
real asset), *C. moreletii* (5), *Osteolaemus tetraspis* (3), plus
*Caiman crocodilus*, *Melanosuchus niger*, *Paleosuchus palpebrosus*
sections. **C. porosus is NOT in CrocBase** — the paired-report's
Nile-vs-saltwater contrast rests on WitmerLab's restricted MorphoSource
heads (OUVC 10899/11470, n=2, juveniles) on the porosus side, so it is
**not a matched set and is not ranked**. Papers as recent as 2024 cite
downloading CrocBase DICOMs (osf.io/x38nh; list at osf.io/6zamj), so the
scans existed — where they live now (linked node? Wayback? RVC site?)
is a recovery hunt, not a download. **Blocked pending that hunt.**

### E. DigiMorph singletons (camel, gharial, etc.)
Barrier-free route proven (§1), but the catalogue is n=1 per species
with mismatched modalities across any pair (camel DICOM cranium vs
Bactrian surface mesh of a mounted skeleton). Computable as
single-specimen endocast/sinus work, **not** as matched sets. **Scouted.**

### F. Squamate skulls — Phenome10k / MorphoSource (~200 species, PNAS 2019)
High-density skull meshes across ~200 modern + extinct squamates, one
GeoMagic Wrap protocol; the paper already computed cranial integration
at scale, so the obvious label gap is claimed. Site unreachable from
this VM (§1). **Scouted, access unverified.**

## 4. BLOCKED — plainly
- All MorphoSource media downloads: free account + API key / captcha
  (official), plus Anubis wall for scripted access. User's step only.
- CrocBase DICOMs: absent from the cited OSF node today (see §3D).
- Elephas DigiMorph CT: published Box link 404. (Elephant pair: dead,
  per standing instruction not revived.)
- Phenome10k: unreachable from this VM's network.

## 5. Ranked recommendation
1. **Rhino-5 (Candidate A) — do this next.** Barrier-free, already
   computed end-to-end, all 10 pairs significant, with two publishable
   framings: (i) *R. sondaicus vs R. unicornis* same-genus control, and
   (ii) *D. bicornis* as the distal-heavy outlier. Next step is cheap:
   pre-register the 5-species profile test, then run the ≥5-bone
   sensitivity + fore/hind ratios exactly as for the pair.
2. **Baboon validated-subset GMM (B)** — the strongest *new-system*
   option, but it needs the free MorphoSource account (user's step)
   and must cite Modesto-Mata 2025 as the ruler audit it builds on.
3. **Copes clade contrasts (C)** — same account unlock as B; pick the
   contrast by the Table-1 n's, not by the macaque/baboon headline.
4. **CrocBase recovery hunt (D)** — one hunter pass (Wayback + OSF
   linked nodes + RVC pages) to find where the DICOMs went; if found,
   the *niloticus* ontogenetic series outranks any croc pair.

Files: this report; bundle `gold/morpho-ct/` (EPMC rhino-5 outputs +
script, OSF specimen list, DigiMorph pages, MorphoSource Anubis
evidence). No accounts created; nothing pooled across pipelines.
