# Dead names in a frozen archive: a name-by-name re-identification of the stranded Fonozoo frog-call pile, with a maintained-archive control

**Atharva Chourey Lab** — independent research lab
*Human–AI collaboration: fieldwork, resolution pipeline and analysis conducted jointly by the lab's researcher and an AI research partner (Muse).*

**Status: DRAFT — not submitted.**

---

## Abstract

Sound archives assembled before the molecular era are filed under the
taxonomy of their day. When such an archive is abandoned — its files stranded
on the web, its catalogue frozen — every subsequent taxonomic revision
silently falsifies a fraction of its labels, and no one re-counts them. We
recovered the complete stranded web pile of the Fonoteca Zoológica (MNCN,
Madrid): 1,013 frog-call audio files published as web companions to printed
sound guides, present in no formal archive. Of the 629 recordings filed under
firm species names, **146 (23.2%) no longer carry that name** in the GBIF
Backbone Taxonomy — predominantly genus recombinations (129 recordings), with
15 junior synonyms and 2 split elevations; a further 6 recordings (5 names)
are split-ambiguous, their filed name now denoting a complex of two or more
species. Joining the institution's own catalogue (3,618 Darwin Core records)
resolved 4 of the 6 ambiguous recordings on geographic evidence. The burden
is region-structured: Neotropical recordings changed at 30.7% (genus moves),
Palearctic recordings carry a further 16% split-ambiguity (splits, not
moves), and Malagasy recordings only 5.7%, their guide postdating the
region's genus reorganisation. A second ruler — the Catalogue of Life
(ASW lineage) — agrees with the GBIF Backbone on 87.4% of names and leaves
the aggregate rate nearly unchanged (24.2% vs 22.8%), yet genuinely
disagrees on 18 names (a whole genus, *Platypelis*, among them) and drops a
further 47 of the pile's misspelt filename names that GBIF's fuzzy matcher
rescues — so a re-identification is only as stable, and as complete, as the
backbone and matcher it is run against. As a control, we ran the identical instrument over the
maintained Fonoteca Neotropical Jacques Vielliard (5,793 firm-named
amphibian recordings): **1.1% changed**, its residue running in the opposite
direction (recent moves and newly described species the backbone has not yet
absorbed). The 23% figure is therefore not a property of an era but of a
*filing state*: the measured dead-name burden of a frozen archive, against a
living one. The method — recovery, two-ruler resolution, catalogue join — is
archive-agnostic and is released with the per-recording tables.

## 1. Introduction

Bioacoustic archives are identification infrastructure. A recording's value
is the name attached to it: the name is what a user searches, what a
distribution model ingests, what a conservation assessment cites. Anuran
taxonomy, however, has been in continuous rapid revision since the molecular
era began — genera split and recombined (Hyla sensu lato into Boana,
Dendropsophus, Dryophytes and others; Bufo sensu lato into Rhinella,
Peltophryne, Bufotes…), species complexes partitioned, synonyms sunk. Every
archive compiled before or during this churn inherits it.

Maintained archives absorb the churn invisibly: curators update names, and
the archive's history of dead names is erased as a side effect. Frozen
archives — abandoned web publications, superseded guide companions, stranded
institutional piles — absorb nothing. Their labels are exactly as falsifiable
as the day they were frozen, and increasingly false. Yet the size of this
effect has never, to our knowledge, been measured for any sound archive: no
published study re-identifies a pre-DNA sound archive name-by-name against a
current backbone and reports the rate (novelty scrub, `NOVELTY.md`).

The Fonoteca Zoológica pile is an ideal test case. The files were published
as companions to a series of printed regional sound guides (Spain & Portugal;
Madagascar; Bolivia; a world selection), then stranded: the pile sits on
institutional subdomains outside any formal archive, unmaintained, its
filenames frozen at guide-publication taxonomy. We ask four questions.
(1) What fraction of its species-named recordings are dead-named today?
(2) Can the institution's own catalogue resolve the recordings a backbone
alone cannot (the split-ambiguous residue)? (3) Is the rate structured — by
region, by mechanism? (4) Is the rate a property of the archive's era, or of
its frozen state — answered by running the identical instrument on a
maintained archive of the same era and class (FNJV, Brazil).

## 2. Methods

**Recovery.** The pile was enumerated from the fonozoo.com /sonidos surface
during a systematic stranded-dataset survey (Goldmine Hunter campaign,
2026-11-18): 1,013 audio files, each verified HTTP 200 with content length
and checksum at capture. Filenames encode guide, track number and filed
name; 636 recordings carry a firm (binomial/trinomial, non-hedged) species
name, 629 of them countable after exclusions pre-registered in
`PREREGISTRATION.md`.

**Resolution (ruler 1).** Each unique filed name (573) was matched against
the GBIF Backbone Taxonomy (species-match API, accessed 2026-11-18) and
classified UNCHANGED / MOVED (name survives only as a synonym of a
recombination) / SYNONYM (junior synonym within the same genus) /
SPLIT-ELEVATED / UNRESOLVED. A split screen — filed name accepted today but
known to have been partitioned since the guide era — flagged
SPLIT-AMBIGUOUS cases, which a name match alone cannot see; the screen is a
verified lower bound (it cannot detect splits absent from the backbone's
synonymy or the literature consulted).

**Catalogue join.** The Fonoteca's own-recordings amphibian collection
(FZ_AMPHIBIA; GBIF dataset 836c3a66-f762-11e1-a439-00145eb45e9a; 3,618 Darwin
Core records) was joined at name level: for each filed name, the countries,
provinces, localities and recordists of the institution's own holdings. A
direct accession join (filename numbers vs catalogNumbers) was tested and
rejected (§3.2). Split-ambiguous names were resolved only where the envelope
and the guide's geographic scope jointly exclude all but one daughter;
verdicts are evidence-graded and unresolved cases stay flagged.

**Region structure.** Each recording's region was assigned from its accepted
genus via an explicit genus→realm table (realm-endemic genera only;
trans-realm genera unassigned; Madagascar separated from mainland
Afrotropical). This is a genus-level proxy, not recording locality, and is
reported with its coverage (94%).

**Resolution (ruler 2).** All 573 filed-name tokens were independently
resolved against the Catalogue of Life release 26.11 via the ChecklistBank
name-usage API (dataset 3LR), COL's amphibian taxonomy deriving from
Amphibian Species of the World (ASW offers no API or bulk export; its taxon
pages were additionally read directly for the split-residue spot-checks).
The COL resolver accepts exact-name, species/subspecies-rank usages within
Amphibia — deliberately no fuzzy matching, mirroring COL's own search
behaviour. Disagreements with ruler 1 are classified DISAGREE-VERDICT
(changed vs unchanged, or changed-kind differs), DISAGREE-TARGET (both
changed, different accepted name), or matcher artefacts (one ruler fails to
resolve a misspelt/truncated filename token the other rescues).

**Control archive.** FNJV's catalogue (GBIF dataset
ca2e422f-be48-42a5-bca5-a37cada435c8; 103,162 records; 11,130 amphibian
recordings; 5,793 firm-named) was classified with the identical code,
identical split screen and identical backbone. FNJV's exported names are its
catalogue's current names — the asymmetry against Fonozoo's frozen filenames
is the contrast under study, and is stated wherever the comparison is used.

## 3. Results

### 3.1 The headline rate (ruler 1)

Of 629 countable recordings: 146 changed (23.2%) — 129 MOVED, 15 SYNONYM,
2 SPLIT-ELEVATED — 6 split-ambiguous, 469 unchanged, 8 unresolved. At name
level: 128 of 561 firm names changed (22.8%). The dominant single flow is
the dismantling of Hyla and Bufo sensu lato: Hyla→Boana/Dendropsophus/
Dryophytes, Hypsiboas→Boana, Bufo→Rhinella/Peltophryne/Bufotes.

### 3.2 Catalogue join

The export carries no dates at all (year/eventDate empty, 3,618/3,618), so
no era analysis is possible for Fonozoo; we document the blockage rather
than substitute weaker proxies. The accession join failed (1 coincidental
hit, 4 mismatches, 113 absences in the overlap test) — guide track numbers
are not accessions. The name-level envelope join covers 163/636 firm
recordings (26%) and resolved 4 of 6 split-ambiguous recordings:
*Bufo viridis* → *Bufotes balearicus* (envelope 3/3 Balearic), *Hyla
arborea* → *Hyla molleri* (envelope 118/118 Iberian, all in molleri range),
*Bufo granulosus* → *Rhinella major* (guide-scope + series evidence,
moderate strength). *Rana temporaria* stays flagged (no envelope; guide
spans both daughters). *Mantidactylus betsileanus* stays flagged with a
documented lean to s.s. (envelope localities inside the s.s. range per
Scherz et al. 2022; an unnamed similar lineage at Andasibe per Glaw &
Vences 2007 prevents closure).

### 3.3 Region structure

Neotropical 30.7% changed (119/388, genus moves); Palearctic 16.0% changed
plus 16.0% split-ambiguous (4/25 each — split-driven); Madagascar 5.7%
(10/175); Nearctic 16.7% (2/12); Indomalayan 30.0% (3/10). One archive,
three churn mechanisms: where a genus-level reorganisation postdates the
guide, moves dominate; where the guide postdates it (Madagascar), only
species-level splits remain; Europe's burden is splits almost entirely.

### 3.4 Two rulers

The rulers agree on 501/573 names (87.4%), and the headline rate barely
moves (COL: 125/516 resolved firm names changed, 24.2%; GBIF: 22.8%). The
65 scored disagreements decompose sharply. **47 are matcher artefacts**:
the pile's filenames misspell or truncate names (*diptyyx, brachychird,
Trachicephalus*), GBIF's fuzzy matcher rescues them, COL's exact search
leaves them unresolved — an exact ruler silently drops ~8% of a real
archive's names. **18 are genuine taxonomic disagreements**, concentrated
in a few decisions: *Platypelis* sunk into *Cophyla* by GBIF, retained by
ASW/COL (5 names); the bullfrog as *Lithobates catesbeianus* (GBIF) vs
*Aquarana catesbeiana* (COL); *Ptychohyla* split into *Duellmanohyla* by
COL only (2); *Lysapsus limellum* vs *Pseudis limellum* in opposite
directions; three species sunk by COL that GBIF keeps (*Discoglossus
jeanneae*, *Gephyromantis ventrimaculatus*, *Telmatobius vilamensis*);
*Hyla koechlini* assigned to different species concepts by the two rulers.
Two-ruler disagreement — ~3% of names genuine, ~8% matcher-dependent — is
the honest error bar on any single-backbone re-identification.

### 3.5 The control: FNJV

Changed: 11/694 names (1.6%), 61/5,793 recordings (1.1%). The residue is
directionally opposite to Fonozoo's: un-absorbed *recent* recombinations and
species too new for the backbone snapshot. By recording decade, FNJV's
changed share never exceeds 2.0% (2010s) and is 0.0% for 1960s–70s material:
a maintained archive has no frozen layer at any age.

## 4. Discussion

The dead-name burden of a sound archive is a function of its filing state,
not its age. Fonozoo and FNJV span the same decades and the same taxonomic
churn; one froze, one didn't; the measured burdens differ twenty-fold. Three
consequences follow. First, stranded piles — of which institutional web
space holds many — are not merely unmaintained but *increasingly wrong*, at
a rate set by the revision intensity of their fauna and region; a Neotropical
pile freezes worse than a Malagasy one. Second, re-identification is cheap
relative to the asset: the entire audit is filenames, a backbone and a
catalogue join — no re-listening — and recovered 96% of the pile to a
current name or an honestly flagged residue. Third, the rulers themselves
move: two authoritative backbones genuinely disagree on 3% of this pile's
names — including which genus a whole Malagasy radiation sits in — and
differ on a further 8% purely through spelling tolerance. A
re-identification should therefore always name its backbone and version,
and ideally report the second-ruler disagreement as its error bar.

For archive holders, the FNJV control carries the practical lesson: the
difference between 23% and 1% is not budget or era but the existence of any
curation pass at all. A single name-refresh against a current backbone,
repeated at intervals, keeps a catalogue's dead-name burden at the
backbone-lag floor (~1–2%).

## 5. Limitations

Declared, in order of weight. (1) **Names only**: no audio was re-listened;
a recording filed under a correct name may still be misidentified, and a
renamed recording is not thereby verified — this audit measures label
currency, not identification truth. (2) The split screen is a lower bound:
splits invisible to the backbone's synonymy and the consulted literature are
missed, so 23.2% understates the true dead-name share. (3) The catalogue
join is name-level institutional evidence, not the web tracks' own metadata;
the guides' own per-track data (PUB_AMPHIBIA) has no public occurrence
export. (4) Region is a genus-level proxy. (5) FNJV's export does not reveal
whether its names were curated continuously or in passes. (6) Backbone
results are versioned snapshots (GBIF Backbone and COL 26.11, accessed
2026-11-18); rates will drift as backbones move.

## 6. Data availability

All per-recording and per-name tables (inventory, classifications,
resolutions, catalogue join, split verdicts, region assignments, FNJV
classifications) are released with the recovery tooling in the lab's public
repository: https://github.com/atharva-chourey-lab/goldmine-hunter
(campaign record and spin-off project), with the analysis code in this
project's `scripts/`. The recovered audio files themselves remain the
Fonoteca Zoológica's (MNCN-CSIC) and are not redistributed; the inventory
records their URLs, sizes and checksums at capture.

## Acknowledgements

The Fonoteca Zoológica (MNCN-CSIC) and its recordists created and published
the recordings and catalogue this audit re-identifies; FNJV (UNICAMP) and
the GBIF.ES and CRIA IPT teams publish the Darwin Core Archives that made
the join and the control possible. This work is a human–AI collaboration of
the Atharva Chourey Lab.

## References (selection)

- Frost, D.R. Amphibian Species of the World (online reference, AMNH) —
  amphibian source taxonomy of the Catalogue of Life.
- GBIF Backbone Taxonomy; GBIF species-match API (accessed 2026-11-18).
- Catalogue of Life release 26.11 via ChecklistBank (accessed 2026-11-18).
- Scherz, M.D. et al. 2022. Megataxa 7: 113–311 (Mantidactylus revision).
- Glaw, F. & Vences, M. 2007. A Field Guide to the Amphibians and Reptiles
  of Madagascar, 3rd ed.
- Narvaes, P. & Rodrigues, M.T. 2009. Zootaxa 2134 (Rhinella granulosus
  group revision).
