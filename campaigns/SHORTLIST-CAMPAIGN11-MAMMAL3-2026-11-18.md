# Goldmine Hunter — Campaign 11 shortlist: Mammal Wave 3 (2026-11-18)

The **mammal-grain registry's** third campaign, generated from
the recalibrated queue: all nine unfired 8/10 niches, in
registry order — rhino-ear-notch-horn-profiles,
pinniped-pelage-patterns, tiger-stripe-catalogues,
leopard-jaguar-rosettes, zebra-stripe-patterns,
giraffe-coat-patterns, tooth-wear-age-charts,
cementum-annuli-tooth-archives, primate-face-pattern-archives.
Grades are `GRADES.md`'s, unchanged. Method = Campaigns 7–8
exactly: live crawl + Wayback inventory filtered to
statuscode:200 before counting (`campaign11_mammal3.py`,
`outputs/campaign11-20261118-195724.json`), then targeted
verify passes (`verify11.py`, `verify11b.py`;
`outputs/verify11-20261118-200047.json`,
`outputs/verify11b-20261118-200117.json`; samples in
`gold/campaign11-verify/`, 25 MB total new disk — the two
large items are paper PDFs sampled as the graded evidence for
their niches). Poaching-sensitive systems (rhino, tiger) were
documented as custody only and **not** scraped or
circumvented; no sensitive location data was collected or is
reported anywhere in this campaign.

**Headline, plainly: NO GOLD and NO DIAMOND.** Two SILVER,
five INVENTORY, and the wave's real product — a custody map
of the entire coat-pattern world. The one loose-file surface
in nine niches, Conservation Research Ltd's ExtractCompare
demo zips, is a deliberate software demo: real pattern
catalogues in miniature, published by design in 2010–12, and
the working catalogues behind them are national, platform or
commercial custody everywhere. The calibration file predicted
exactly this for the coat-pattern block ("all platform-era
photo-ID, which this wave's pattern says to discount before
firing") — Wave 3 is that prediction's confirmation, at the
cost of a wave. The autonomous chain therefore stops here:
with no GOLD set there is no novelty scrub and no
pre-registration to write.

## SILVER — published-by-design, verified

**SealID — the Saimaa ringed seal re-identification dataset
(PUBLISHED-BY-DESIGN, formal repository, verified). Niche:
pinniped-pelage-patterns.** The niche's anchor set is a
deliberate public release: **57 individuals, 2,080 expert-
matched images** (2010–2019, boat + camera-trap), plus a
4,599-patch pelage dataset, served from Finland's Fairdata
repository under DOI `10.23729/0f4a3296-3b10-40c8-9ad3-
0cf00a5a4a53` (Etsin landing fetched live, 200). The dataset
paper (*Sensors* 2022, *22*, 7602) was sample-verified via
its arXiv version (2206.02260): **REAL PDF, 10,746,065 B,
md5 `73638285fea3f4a3226947bbab179c35`** — MDPI's own PDF
endpoint served this campaign's client a 410 B HTML phantom
(403), recorded as a client result, not as absence. Exactly
what the niche card promised, published by its own authors:
SILVER. The comparison it enables (pelage ID vs the colony's
tag/telemetry record) runs on public data, which is what
silver means.

**GZGC — Great Zebra and Giraffe Count and ID
(PUBLISHED-BY-DESIGN, formal repository, verified). Niches:
zebra-stripe-patterns + giraffe-coat-patterns.** LILA BC
serves the 2015 Nairobi National Park citizen census as a
finished dataset: **4,948 images, 2,056 combined individual
names released for 6,286 zebra sightings and 639 giraffe
sightings** (page fetched live; census text verified). The
data tarball itself is **10,433,199,738 B** (GCP HEAD 200,
`application/x-tar`) — inventoried by HEAD only, never
downloaded, per method. A two-day, two-species, one-park
census, published whole by Wild Me: SILVER for both niches
it serves, and the ceiling for both — the long-run ecosystem
catalogues the cards actually want (Grevy's in Kenya,
Serengeti/Murchison giraffe) are not in it and did not
surface anywhere else probed.

**Tooth-wear chart stack — the Severinghaus tradition in
print (PUBLISHED-BY-DESIGN, live, verified). Niche:
tooth-wear-age-charts.** The chart literature exists exactly
as carded, and every surface is an agency publication:

| Surface | Evidence |
|---|---|
| TPWD deer-age / harvest bulletin (PWD RP W7000-1135; the Texas chart tradition, in use since 1965) | REAL PDF live, 53,033 B, md5 `e820f394e3568399ac27529d830356c3` |
| Boone & Crockett *Fair Chase* Summer 2008, "Deer Ages" (Cowan → Severinghaus 1949 lineage) | REAL PDF live, 3,155,455 B, md5 `6caceddbc2d2805c23e7c8a1391566de` |
| Cain & Wallace (TPWD) *Guide to Age Determination*, HTML afterlife on a small WMA site (jaw photo per age class, fawn → 8½ yr) | crawl: 33 jaw images, 0 data files; 2 status-200 Wayback data files (site furniture) |

SILVER as a stack — and a ceiling, because the niche's
headline comparison **has already been run and published**:
Foley et al. (*Wildlife Research* 2021; sample-verified,
REAL PDF, 825,781 B, md5 `0403094e47b1b9f905edef95b66e9284`)
aged 5,117 harvested + 134 known-age south-Texas deer and
found both rulers biased (TRW exact-age 43–51% on known-age
adults; CA 87–93% within one year). The two-rulers audit the
card imagines is, for Texas whitetails, a published result.
What remains un-run is narrower (other regions/species,
chart-vs-chart), and it runs on published data.

## INVENTORY — verified real, published, no comparison completed

- **ExtractCompare demo catalogues — tiger / leopard /
  clouded leopard / zebra / giraffe (PUBLISHED-BY-DESIGN,
  live, verified). Niches: tiger, leopard-jaguar, zebra,
  giraffe.** Conservation Research Ltd's old site still
  serves the complete 2010–12 demo piles for its pattern-
  extraction software — the wave's only loose files, and
  they are *demos*: each zip is one small working catalogue
  (flank photographs + extensionless pattern-extract files
  with pose suffixes — `_FL`, `_HL`, `_HA`, `_NK` — + an
  Access `.mdb` catalogue), published so programmes could
  trial the tool. Stream-verified in full (md5 over the
  whole file; one JPEG sample extracted and saved per zip):

  | Zip | Bytes | md5 | Entries | Images | Catalogue |
  |---|---|---|---|---|---|
  | tiger_demo_folders.zip | 22,138,354 | `4160f1eed46e500664daa525c67b9da0` | 196 | 31 | tiger_demo.mdb |
  | leopard_demo_folders.zip | 15,656,495 | `0a7694af2e7001feaacabbec393f6807` | 373 | 76 | leopard_demo.mdb |
  | zebra_demo_folders.zip | 30,341,304 | `5e7038ce5efbd23d6e1ab811aacfda8e` | 298 | 62 | zebra_demo.mdb |
  | giraffe_demo_folders.zip | 56,105,944 | `1a9a1bd654041fe95d94803bd6db0074` | 136 | 30 | giraffe_demo.mdb |
  | clouded_leopard_demo.zip | 73,152,804 | `22a5f2dc587e70987ff51fc8c7f1dc87` | 1,094 | 205 | clouded_leopard_demo.mdb |

  The installer itself is live too (HEAD 200, 8,441,862 B).
  Real, charming, and a recovery of nothing: the demo
  animals are a trial handful per species, not a stranded
  field catalogue. INVENTORY for all four niches it touches.
- **Cabo Blanco monk-seal programme report, 2017–2018
  (PUBLISHED-BY-DESIGN programme report on a loose host;
  sample truncated, stated). Niche: pinniped-pelage-
  patterns.** The Mediterranean Monk Seal Conservation
  Program's annual report — including its Resophom sighting-
  network annex (observer-level records with pelage, ventral
  patch, scars, photos/videos fields) — sits as a PDF on
  `freqstats.marineland.fr`, an unrelated statistics host.
  The host is unreachable from this campaign's client live
  (proxy failure, both attempts); Wayback holds it
  (status-200; the /dl tree: 172 status-200 files). The
  Wayback sample download stopped at exactly **1,048,576 B
  with no EOF marker — a truncated head**, md5
  `e7c082d197df3b6bafb008c0d96d7561` *of the truncated
  bytes*, REAL PDF magic; the full report is claimed only
  as CDX-verified + search-indexed, not as read. The
  underlying slide catalogue (Cap Blanc, 1993–96, ≥228
  individuals in the 2000 *Marine Mammal Science* study)
  has no file surface anywhere probed — custody, below.
- **ChimpFace dataset paper (PUBLISHED-BY-DESIGN ML
  dataset, paper verified). Niche: primate-face-pattern-
  archives.** PrimNet's *Face Recognition: Primates in the
  Wild* (arXiv 1804.08790; **REAL PDF, 9,348,378 B, md5
  `9bfde4871c0d764a46f0f9f86754f67a`**) documents the
  merged C-Zoo (2,109 images / 24 chimps) + C-Taï (5,078 /
  78) sets = **ChimpFace, 5,559 images / 90 individuals** —
  a scraped-together ML benchmark, published by design, and
  pointedly *not* any field site's portrait archive. The
  sites' own archives (Gombe's, held by the Jane Goodall
  Institute — its news surface describes the archive as
  among the most comprehensive in the world and a
  ChimpFace-*technology* collaboration, not a data release)
  remain site patrimony. INVENTORY.
- **Matson's Laboratory web surface (PUBLISHED-BY-DESIGN
  commercial site). Niche: cementum-annuli-tooth-archives.**
  The lab's site serves furniture and forms, not ages: 16
  status-200 Wayback data files (uploads + images), the
  live Biologist Order Form sampled (**REAL xlsx, 30,520 B,
  md5 `fdd7972868c7ef020492688c81248814`**). The archive
  itself is the business — see Kills.

## KILLS & CUSTODY FINDINGS — probed, nothing claimable, evidence stated

- **Rhino ear-notch / horn profiles — KILL for recovery;
  the wave's most security-clear custody finding. Niche:
  rhino-ear-notch-horn-profiles.** The system works exactly
  as carded — Save the Rhino's Ezemvelo explainer (fetched
  live) describes the internationally templated notch code
  (>150 combinations), front-on ear photographs, and a
  **"personal rhino file"** per animal holding photos + life
  history + sightings — and every part of it is per-reserve
  custody, deliberately: these are anti-poaching records.
  The anchor is forensic custody of the same order: RhODIS
  (Univ. of Pretoria VGL) **exceeded 180,000 samples by
  2024** (IRF page, fetched live), is a law-enforcement
  system modelled on CODIS, and its eRhODIS access is by
  request to Parties/agencies (CITES 2025 outcome). The
  RhODIS home domain's whole Wayback surface is 1 status-200
  data file (site furniture). No reserve sighting book,
  notch diagram set or horn-profile pile exists on any
  surface probed. Documented, never circumvented, no
  location data sought or kept.
- **Tiger stripe catalogues — KILL for recovery; national
  custody. Niche: tiger-stripe-catalogues.** The real
  catalogue is India's: NTCA/WII's national estimation
  (2022: 32,588 camera locations, 3,080 individually
  photographed tigers, ExtractCompare + MSTrIPES) — and the
  pattern files behind the published counts are restricted
  by design (the WII surface crawled here serves programme
  furniture only). Every other programme's catalogue is a
  silo of the same shape, justified by poaching risk, as
  the niche card itself said. The only public stripe files
  are the demo handful (INVENTORY above). Counts are
  published; stripes are not, and will not be hunted past
  that line.
- **Leopard & jaguar rosettes — KILL for the field
  catalogues; custody = the projects + Wildbook. Niche:
  leopard-jaguar-rosettes.** Study-shaped exactly as carded:
  hundreds of camera-trap projects each publish a density
  estimate and keep the rosette catalogue (recent example
  verified in discovery: WII's Kumbhalgarh report — 55
  leopards from 762 photographs, catalogue in the project,
  report is the publication). Wildbook ingests a fraction
  by design. The Cockscomb-era long-term sets did not
  surface as files anywhere probed; the public surface is
  the ExtractCompare demos (INVENTORY above).
- **Giraffe coat patterns — KILL beyond the published
  census; platform custody. Niche: giraffe-coat-patterns.**
  The living system is GiraffeSpotter, a Wildbook platform
  (fetched live; researcher-mediated by design — its whole
  Wayback data surface is 2 furniture files). Tower-by-tower
  ranger/guide catalogues did not surface; GZGC (SILVER
  above) is the one published exception, and it is one park,
  two days.
- **Zebra stripe patterns — KILL beyond the published
  sets; the drawn-code era is paper. Niche:
  zebra-stripe-patterns.** StripeSpotter's published set
  (45 individuals, 820 images, 2011) and GZGC (SILVER) are
  the public layer; both are deliberate releases. The
  Petersen-era hand-drawn stripe codes and the ecosystem
  catalogues behind them produced no file surface anywhere
  probed — the same paper-custody shape as Campaign 7's
  elephant cards and Campaign 8's Murie casts.
- **Cementum-annuli archives — KILL for recovery; the
  wave's clearest service-industry custody. Niche:
  cementum-annuli-tooth-archives.** Matson's Laboratory
  (aging mammals commercially since 1969; >100,000 teeth/yr
  per ADF&G's 2025 account, 62 species in 2024) returns a
  number per tooth to its client agency; the section images
  and the paired field guesses stay in the lab's and the
  agencies' files. The one full report that reached a loose
  host — Matson's 31 May 2006 cementum report for Minnesota
  DNR (2,448 whitetail teeth), formerly served from the
  Minnesota Legislature's site — is **404 live today, and
  no Wayback copy was found** under either host shape or as
  a filtered prefix over the whole 2013 docs tree (255
  collapsed / 250 status-200, zero C130010 hits): stated as
  *unrecovered from this client after three query shapes*,
  not as never-archived. The two-rulers panel the card
  wants (cementum vs wear vs known age) exists — inside
  the Foley et al. paper (tooth-wear SILVER above), which
  is where this niche's comparison also already lives.
- **Monk-seal slide catalogues + Hawaiian monk-seal
  database — custody. Niche: pinniped-pelage-patterns.**
  Cap Blanc's 1993–96 slide catalogue (the 228-individual
  set) is programme custody with no file surface; NOAA's
  Hawaiian Monk Seal Photo ID Database is an InPort record
  whose page states, verified live, **"No Distributions
  available"** — use of the photos must be cleared with
  NMFS/PIFSC. Documented, never circumvented.
- **Primate face archives proper — custody. Niche:
  primate-face-pattern-archives.** Gombe/Taï portrait files
  are field-site patrimony (JGI surface, above); the ML
  world answered by scraping its own small sets (ChimpFace,
  INVENTORY) rather than joining sixty years of site
  portraits — the niche card's own sentence, confirmed as
  the finding.

## Ranking

1. **SealID (Saimaa) — SILVER.** A complete, expert-matched
   pelage benchmark, published whole with a DOI; the niche's
   anchor, delivered by its own authors.
2. **GZGC (zebra + giraffe) — SILVER.** One park, two days,
   2,056 named individuals, published whole — and the
   exception that proves the platform-custody rule for both
   coat niches.
3. **Tooth-wear chart stack — SILVER, with its comparison
   already published.** Foley et al. ran the two-rulers
   audit in 2021; the charts survive as a kept agency stack.
4. **ExtractCompare demo catalogues — INVENTORY, and the
   wave's most interesting surface.** Five complete miniature
   pattern catalogues (photos + extracts + Access DBs),
   live since 2010 on a small company site — the Fonozoo
   *shape* (loose files, old site, one keeper) with a
   deliberate-publication *provenance*, which under the
   fixed grades is exactly the line between gold and
   inventory.
5. **RhODIS (180,000+ samples) + India's national tiger
   archive + Matson's half-century of sections — the wave's
   custody map.** Three of the largest pattern/age archives
   in mammalogy, all real, all counted here, and all
   reachable only with institutions, not crawlers. The
   digitisation-with-institutions list from Waves 1–2
   (Wagyu cards, ATE Access, Murie drawers) now has its
   coat-pattern and teeth volumes.

*Method notes (standing + this wave's corrections): Wayback
counts status-200-filtered before counting; every grade
rests on ≥1 sample download with size + md5 + magic in
`outputs/verify11-20261118-200047.json` /
`outputs/verify11b-20261118-200117.json`, except where a host
blocked this client and the shortlist says so (MDPI PDF
endpoint — phantom to this client, arXiv version sampled;
freqstats live — proxy failure, Wayback sample truncated at
1 MiB and reported as such; GZGC tarball — 10.4 GB, HEAD
only by design). Corrections made mid-wave and recorded:
the giraffe/zebra ExtractCompare pages are lowercase
(`giraffe.html`, `zebra.html` — the capitalised guesses 404);
verify11b's first Matson census row-pick matched the wrong
label and was corrected against the campaign output before
this shortlist was written; the MN report's absence is
reported only after three CDX query shapes. README
verified-results NOT updated — no find in this wave meets
the stranded bar those entries set.*
