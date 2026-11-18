# RESULTS — EXHAUSTED (Part 2, 2026-11-18)

Part 1 (`RESULTS.md`, pre-registration `d2700cf`, results `3084a88`) measured
the stranded Fonozoo web pile against one ruler: of 629 countable
species-named recordings, 146 (23.2%) no longer carry their filed name in the
GBIF Backbone, 6 recordings (5 names) were split-ambiguous, 469 unchanged.
This Part 2 exhausts the same set in three directions: a catalogue-metadata
join, a second-backbone cross-check, and a second-archive generalisation
probe. Stage commits: `e2dd403` (join), `f8fb2e0` (region), `b21330a` (FNJV),
`c0e9ea9` (second backbone).

## Stage 1 — Catalogue-metadata join

**Source reached.** The Fonoteca Zoológica's own-recordings amphibian
collection (FZ_AMPHIBIA) is published as a Darwin Core Archive via the GBIF.ES
IPT (GBIF dataset `836c3a66-f762-11e1-a439-00145eb45e9a`; 3,618 occurrence
records). The published/guides collection (PUB_AMPHIBIA) exists only as a
registry entry — no occurrence download exists for it anywhere we could reach,
and fonozoo.com's own catalogue interface returns 403 stubs to programmatic
clients (Campaign 6). The web pile derives largely from published guides, so
the joinable catalogue is the institution's *own-recordings* collection: an
envelope for a filed name, not the web track's own record.

**Coverage of the export itself.** catalogNumber 100%, recordedBy 97%,
country 89%, stateProvince 88%, locality 15% — and **dates 0%**: year and
eventDate are empty for all 3,618 records. The era analysis this stage was
meant to unlock is impossible from the catalogue; that blockage is documented,
not worked around.

**Accession join: tested and rejected.** The filenames' leading numbers are
not catalogue accessions. For species present in both sources, filename
numbers matched a same-species catalogNumber once, mismatched four times, and
were absent 113 times. The one hit (`0800` / *Alytes muletensis*, Mallorca) is
a coincidence of two independent numbering systems (guide track numbers vs
collection accessions).

**Name-level envelope join: stands.** 136 of 561 firm filed names (24%) and
**163 of 636 firm recordings (26%)** have a catalogue envelope: the countries,
provinces, localities and recordists under which the institution itself holds
that name. This is institutional-usage evidence about the filed name — it is
not the web track's own metadata, and is used only as such (split evidence,
§ below).

**Split resolutions (evidence per recording; analyst verdicts,
`results/split_resolutions.json`).** Of the 5 split-ambiguous names
(6 recordings):

- *Bufo viridis* (2 recordings) → **RESOLVED: *Bufotes balearicus*.**
  Envelope 3/3 Balearic (Mallorca, Cap Blanc; Islas Baleares); the pile's
  scope is the Spain & Portugal guide; *B. viridis* s.s. does not occur in
  Iberia or the Balearics.
- *Hyla arborea* (1) → **RESOLVED: *Hyla molleri*.** Envelope 118/118 Iberian
  (Salamanca 53, Portalegre 47, Coimbra 15, Ávila 3) — all inside *molleri*
  range, none in the NE-Iberian *arborea* s.s. zone.
- *Bufo granulosus* (1) → **RESOLVED: *Rhinella major*.** The track belongs to
  the Bolivia guide's *granulosus* series whose preceding track was filed as
  the subspecies *granulosus major* (→ *R. major*); *granulosa* s.s. is
  NE-Brazilian (Narvaes & Rodrigues 2009). Moderate strength — flagged as
  such.
- *Rana temporaria* (1) → **STAYS FLAGGED.** Zero catalogue records under the
  name; the guide spans both daughters' ranges (*parvipalmata* NW Iberia,
  *temporaria* s.s. Pyrenees/NE). No honest resolution without a province.
- *Mantidactylus betsileanus* (1) → **STAYS FLAGGED, with a documented lean
  to s.s.** (Stage 2 spot-check: the envelope localities Andasibe and
  Mandraka fall inside the *betsileanus* s.s. distribution as circumscribed
  by Scherz et al. 2022, but Glaw & Vences 2007 note an unnamed similar
  lineage at Andasibe — the lean is recorded, the flag stays.)

Net effect on the Part 1 tally: 4 of 6 split-ambiguous recordings resolved by
evidence; 2 remain flagged. The headline rate is unchanged (splits were never
counted as changed): **146/629 = 23.2%**.

## Stage 1b — Region structure (era blocked; region by genus-realm proxy)

With dates absent, era structure is untestable for Fonozoo (the FNJV probe,
Stage 3, supplies the era axis for a maintained archive). Region is assigned
per recording from the accepted genus via an explicit genus→realm table
(`scripts/region_analysis.py`; 94% of recordings assigned; trans-realm genera
left unassigned). The 23.2% is strongly region-structured, and the *mechanism*
differs by region:

| Realm | Firm recordings | Changed | Split-ambiguous |
|---|---|---|---|
| Neotropical | 388 | **119 (30.7%)** | 1 |
| Palearctic | 25 | 4 (16.0%) | **4 (16.0%)** |
| Nearctic | 12 | 2 (16.7%) | 0 |
| Indomalayan | 10 | 3 (30.0%) | 0 |
| Madagascar | 175 | 10 (5.7%) | 1 |
| Afrotropical (mainland) | 4 | 0 | 0 |

Neotropical churn is genus-move churn (Hypsiboas→Boana, Bufo→Rhinella/
Peltophryne). Palearctic churn is split-driven: a further 16% of its
recordings cannot be carried forward under the filed name at all. Madagascar
is near-stable (5.7%) — its guide postdated the region's genus-level
reorganisation, so only species-level splits touch it. Small-n realms
(Nearctic, Indomalayan) are reported but not leaned on.

## Stage 2 — Second-backbone cross-check (COL/ASW lineage)

All 573 filed-name tokens were independently resolved against the Catalogue
of Life release 26.11 (ChecklistBank dataset 3LR; COL's amphibian taxonomy
derives from Amphibian Species of the World — ASW itself offers no API or
bulk export, verified directly). The resolver filters to exact-name,
species/subspecies-rank usages within Amphibia.

**Agreement.** The two rulers agree on **501 of 573 names (87.4%)**. Scored
disagreements: 64 DISAGREE-VERDICT + 1 DISAGREE-TARGET; 7 further names are
SPLIT-class under GBIF, which a backbone match cannot score. The aggregate
rate is ruler-robust: COL changes 125 of the 516 firm names it resolves
(24.2%), against GBIF's 128 of 561 (22.8%).

**But the 65 disagreements decompose into two very different kinds:**

1. **Matcher artefacts — 47 names.** COL's exact-name search does not rescue
   the pile's misspelt and truncated filename names (*diptyyx, brachychird,
   feonnysala, Trachicephalus, Pseudys…*) that GBIF's fuzzy matcher maps to
   the intended species: 33 firm names + all 14 hedged/junk-token
   disagreements are COL-UNRESOLVED for this reason alone. The
   literature-documented case, *Leptodactylus chaquensis macrosternum*
   (GBIF: synonym of *L. chaquensis*; ASW-side literature lumps the pair
   into *L. macrosternum*), also lands in this bucket operationally — the
   trinomial usage was not returned by the filtered COL search. A
   filename-based audit's yield depends on its ruler's spelling tolerance:
   an exact ruler silently drops ~8% of a real archive's names.
2. **Genuine taxonomic disagreement — 18 names** (both rulers resolve; the
   verdict or the target differs). Concentrated, not diffuse:
   - *Platypelis* vs *Cophyla* (5 names): GBIF sinks Platypelis into
     Cophyla; ASW/COL retains Platypelis.
   - The bullfrog (2 names): GBIF → *Lithobates catesbeianus*; COL →
     *Aquarana catesbeiana* — the same frog carries two different current
     names (the single DISAGREE-TARGET: *Rana catesbeiana*).
   - *Ptychohyla* → *Duellmanohyla* (2 names, COL ahead); *Lysapsus* vs
     *Pseudis* for *limellum* (2 spellings; the rulers place it in opposite
     genera — cf. FNJV, whose *Pseudis limellum* GBIF moves to *Lysapsus*);
     *Colostethus jacobuspetersi* → *Hyloxalus* (COL ahead); *Hylarana
     guentheri* (GBIF → *Sylvirana*; COL keeps Hylarana); *Hyla koechlini*
     (GBIF → *Dendropsophus koechlini*; COL → synonym of *D. pauiniensis* —
     a different species concept); three species sunk by COL that GBIF
     keeps (*Discoglossus jeanneae* → *D. galganoi*, *Gephyromantis
     ventrimaculatus* → *G. malagasius*, *Telmatobius vilamensis* →
     *T. halli*); one trinomial treated inversely (*Discoglossus pictus
     auritus*).

**ASW spot-checks** (`results/asw_spotchecks.md`): ASW taxon pages (full
synonymy + distribution) were read directly for the Stage 1 residue. The
*Mantidactylus betsileanus* page places the catalogue envelope's localities
(Andasibe, Mandraka) inside the s.s. distribution per Scherz et al. 2022,
while recording Glaw & Vences 2007's unnamed similar lineage at Andasibe —
hence flagged-with-lean, as recorded in Stage 1.

Two-ruler disagreement is therefore a real but bounded error bar on any
re-identification: ~3% of names (18/573) are genuinely ruler-dependent,
and a further ~8% are matcher-dependent. A re-identification that does not
name its backbone — and its match tolerance — is under-specified.

## Stage 3 — Generalisation probe: FNJV (Fonoteca Neotropical Jacques Vielliard)

FNJV's complete catalogue is a Darwin Core Archive on GBIF (dataset
`ca2e422f-be48-42a5-bca5-a37cada435c8`): 103,162 records, of which 11,130
amphibian recordings, 5,793 under firm species names (694 unique). The SAME
classifier and split screen as Part 1, unchanged, against the same GBIF
Backbone:

- **Changed: 11 of 694 names (1.6%); 61 of 5,793 recordings (1.1%)** —
  against Fonozoo's 22.8% of names / 23.2% of recordings.
- The residual runs the *other way*: FNJV's un-absorbed names are recent
  recombinations (e.g. *Nyctimantis brunoi* → *Aparasphenodon brunoi*) and
  its unresolved names are mostly species described too recently for the
  backbone snapshot (*Brachycephalus dacnis*, *Pseudopaludicola javae*,
  *Rhinella marianae*…). The archive is ahead of the ruler as often as behind
  it.
- Era axis (FNJV carries recording years, ~99% coverage): changed share by
  recording decade is 0.0% (1960s–70s) rising only to 2.0% in the 2010s —
  curation residue, not era structure. A maintained catalogue shows no frozen
  layer at any age.
- One export quirk recorded: 11 recordings under a bird name (*Paraclaravis
  geoffroyi*) sit inside the amphibian class slice.

**Verdict.** ~23% is not an archive-era constant. It is a *frozen-filing*
rate: FNJV, continuously curated, has absorbed the same decades of taxonomic
churn invisibly (its exported names are current combinations — *Boana*,
*Dendropsophus* — where Fonozoo's frozen filenames still say *Hypsiboas*,
*Hyla*). The contrast is the control that identifies the Fonozoo number: the
difference between a maintained catalogue and a stranded one, measured with
one instrument on both.

Registered caveat (stated, not hidden): FNJV's exported names are its
catalogue's *current* names; whether they were updated continuously or in a
re-identification pass, the export does not say. The Fonozoo filenames, by
contrast, are frozen at guide publication. The comparison therefore measures
exactly the quantity of interest — the dead-name burden a frozen filing
carries that a living one does not.

## Updated headline

Across both archives, one instrument: a frozen pre-DNA sound archive carries
**23.2%** dead names; a maintained one carries **1.1%**. Within the frozen
archive the burden is region-structured (Neotropical genus moves 30.7%;
Palearctic splits; Madagascar 5.7%), 4 of its 6 unresolvable recordings yield
to catalogue evidence, and the two taxonomic rulers themselves genuinely
disagree on 18 of 573 names (3.1%) — with a further 47 names (8.2%) decided
only by the ruler's spelling tolerance.
