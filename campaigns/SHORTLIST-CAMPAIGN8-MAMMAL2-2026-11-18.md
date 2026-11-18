# Goldmine Hunter — Campaign 8 shortlist: Mammal Wave 2 (2026-11-18)

The **mammal-grain registry's** second campaign, generated from
the recalibrated queue after Campaign 7's cuts: guard-hair-
scale-casts (9), then the 8s — koala-fingerprints, dog-nose-
prints, plaster-track-cast-collections, elephant-footprint-age,
right-whale-callosity-patterns, manatee-photo-id-scars. Grades
are `GRADES.md`'s, unchanged. Method = Campaign 7's exactly:
live crawl + Wayback inventory filtered to statuscode:200
before counting (`campaign8_mammal2.py`,
`outputs/campaign8-20261118-191554.json`), then targeted
verify passes (`verify8.py`, `verify8b.py` plus a correction
pass; `outputs/verify8-20261118-190946.json`,
`outputs/verify8b-20261118-191140.json`; samples in
`gold/campaign8-verify/`, 13 MB total new disk). Researcher-
only / password systems (MIPS, NARWC consortium, ATE) were
documented as custody and **not** scraped or circumvented.
One tooling patch landed before firing: the `mammal-niches`
listing now sorts by **current** score (calibration-amended),
with the stale `rank_by_score` kept only as tiebreak — the
head of the queue now reads manatee (9, after this wave),
guard-hair (8), then the unfired 8s.

**Headline, plainly: GOLD — one set, the queue's last seed.**
The manatee niche produced the mammal registry's first gold:
Wayne Hartley's hand-drawn Blue Spring scar-sheet catalogue,
frozen as of April 2013, stranded on Save the Manatee Club's
archive subdomain and absent from the formal MIPS system. One
SILVER stack (guard-hair atlases), one small SILVER (EBRWS),
and the rest inventory, kills and custody findings. No
DIAMOND — nothing in the verified set itself shows two rulers
disagreeing; that test belongs to the comparison, which the
autonomous chain has pre-registered (see the end of this
shortlist) but not run.

## GOLD — stranded, verified

**Hartley's Blue Spring "Practical Scar Sheet" set
(STRANDED, live on an old-site subdomain, verified). Niche:
manatee-photo-id-scars.** Save the Manatee Club's archive
subdomain serves the complete April-2013 edition of Wayne
Hartley's hand-drawn scar catalogue for Blue Spring:
`cam_scar_sheets_all_10-13.pdf` — **REAL PDF, 1,599,152 B,
md5 `79e2067c1ad29b6ca34227889141b50d`, 22 pages** (created
2013-09-06, Word 2007 — the sheet's own production file).
Sampled pages were visually inspected, not just hashed:
page 1 is the KEY (scar vocabulary — white / healed-grey /
cut / section-missing-from-tail; size class; ID number and
year-first-ID'd conventions), and the remaining ~21 pages
carry ~10 animals each, A–Z (page 3: Annie, Ansel, Anvil,
Aplin, Aqua…; page 22: Volusia…Zeb), each entry one tail
sketch with its scar marks, size, BS/Spring ID number and
year first identified — **≈200 individuals** in one sketch
protocol, maintained by one observer since the 1970s. A
companion 2-page adoptee sheet set sits on the club's mail
subdomain (`ScarSheet.pdf`, REAL PDF, 481,180 B, md5
`c2abc9b134530d20e42aa2dc85c8783d`, 2016). The main site's
current adoptee page mirrors only the adoptee subset; the
full 2013 sheet set lives only on these archive surfaces.

Why this is GOLD under the fixed grades, element by element:
**provenance** — the set is the working sketch catalogue of
the Blue Spring programme, hosted on the NGO's own old-site
subdomains; the formal archive for manatee photo-ID is MIPS
(FWC/FWRI, ex-USGS Sirenia), a *photographic* system —
Hartley's sketch sheets are not MIPS records and are in no
formal archive found. **Comparable set** — one derived data
type (tail-scar sketch + ID fields), one protocol, ~200
units. **Anchor** — MIPS's known individuals (5,146 animals
statewide per FWC's FY2023-24 report) and the Blue Spring
known-identity record (rescue/freeze-brand cases, the
published life histories in Hartley's own *Genealogies of
Blue Spring Manatees*). **Un-run comparison** — nobody has
audited the sketch system against the later record: the
sheet's own key states its retention rules as practice (the
Practical sheet "uses a 3 to 5 year drop"; recognised animals
are "kept on a ten year drop") — whether those rules predict
actual re-identifiability has never been measured. The
comparison, in one sentence: **join the frozen 2013 sheet
set to post-2013 Blue Spring records and measure how long a
hand-drawn scar ID actually stays re-identifiable — the
persistence curve and the true accuracy of the sheet's own
3–5-year drop rule.** Novelty scrub + pre-registration:
`~/workspace/manatee-scar-sheets/` (scrub verdict: narrowed
but open — see Kills for the priors that narrowed it).

*Caveats, plainly:* the sheets are scanned drawings (the PDF
carries almost no text layer) — any comparison starts with
manual transcription, which is real work, not a script run.
Hartley's living system continues (he updates sheets each
winter; documented manatees are transferred to the statewide
database) — the GOLD is the frozen, public, stranded 2013
snapshot, not the living archive, which remains SMC/FWC
custody. The individual count (≈200) is a page-structure
estimate (21 catalogue pages × ~10), stated as such.

## SILVER — published-by-design, verified

**Guard-hair atlases — a four-continent published stack
(PUBLISHED-BY-DESIGN, live, verified). Niche:
guard-hair-scale-casts.** The niche's material exists exactly
as carded, and every surface is a deliberate publication:

| Surface | Evidence |
|---|---|
| Texas atlas — Debelica & Thies 2009, NSRL Special Publications SP-055 (150+ Texas species, SEM scale + medulla) | REAL PDF live, 5,048,265 B, md5 `45e3581beab5e3c3d4be13365a3bb9c1` |
| CMU Michigan hair-ID pages (Swanson lab personal pages; 57 species pages, light + SEM images) | index 200 with 57 species links; full-size image sampled: REAL JPEG, 333,219 B, md5 `79846bb73504fe07049925cef80a6dbf`; thumbnails real JPEGs (4–8 KB) |
| ZSI Kolkata trichotaxonomy papers (PDFVolumes tree; De & Chakraborty, Bovidae guard hairs, *Rec. Zool. Surv. India* 112(2)) | REAL PDF live, 406,193 B, md5 `a2cd46fbe14f2c6f9b9c3b0ccc43b65c` |
| Landcare NZ factsheets (Brunner & Coman's 1974 Australian micrographs, web afterlife) | Host bot-walls this campaign's client (HTTP 202, no content) — surface documented from the discovery pass, **not** sample-verified here, and claimed as nothing more |

The cross-atlas comparison the niche card names (Texas vs
India vs Australia vs CMU — same species/genera keyed under
different scale vocabularies, never checked against each
other or against DNA) is runnable from this stack, but it is
a comparison *on published data* — the CRU class. SILVER.
The CMU pages are the stack's loosest member (a personal
faculty page, the Fonozoo shape) and are noted as such; they
are nonetheless a deliberate public teaching resource, which
keeps the niche at silver under the grades.

**EBRWS Encounter Bay catalogue-brochure stack
(PUBLISHED-BY-DESIGN, live, verified). Niche:
right-whale-callosity-patterns.** The small South Australian
project serves its Photo-ID catalogue as a brochure PDF in
its WordPress uploads — the Juneau pattern at smaller scale:
the 2019 brochure exists in two near-identical captures
(3,775,328 B / 3,775,319 B, 2020/2022), an edited-2021
capture (1,002,347 B), and the **live file today is REAL
PDF, 4,549,679 B, md5 `614df2ea622b8e50fe0ac60c3eec2b96`**
— grown again at the same URL. The uploads also hold the
project's working papers: SRW Photo-ID Data Sheet (44,667 B),
Blank Callosity Map (11,107 B), Interpretation Breakdown
info sheet (39,099 B) — all status-200 in CDX. The catalogue
(72 individuals at the 2019 edition) now feeds ARWPIC, so
the stack is a kept, joined, published one. SILVER, small —
one catalogue, one basin, already reconciled upward.

## INVENTORY — verified real, published, no comparison completed

- **Utah Marriott Library Right Whale Collection
  (PUBLISHED-BY-DESIGN formal digital library).** The
  Península Valdés 1970–2004 photographic survey (the Payne-
  era set; Flukebook later counted Argentina at 3,350 whales
  / 8,952 images from it) is served record-by-record as
  image/jpeg with Whale ID / certainty / body-mark facets.
  This campaign's client was bot-walled on the record pages
  (HTTP 418 on both attempts) — **no sample was obtained**,
  so nothing beyond the discovery pass's search-indexed
  evidence is claimed. A formal library surface in any case.
  Inventory as a surface; unrun as a sample, stated plainly.
- **Parker East African Elephant Dataset (formal archive).**
  The forefoot/age calibration-grade data (3,199 cases, 100
  variables, incl. forefoot circumference and age) is
  already transcribed to public CSV in the University of
  Florida IR — the comparison baseline, already integrated,
  not a find. Its handbook PDF was unreachable from this
  client live and has no Wayback capture on the path tried;
  the dataset's formal status rests on the discovery pass's
  handbook text, stated as such.
- **Elephants for Africa FIT project PDF (PUBLISHED-BY-
  DESIGN).** REAL PDF, 192,777 B, md5
  `b8cffa8316154e2012d0e7e87f045672` — the Botswana
  known-individual footprint collection project, whose
  output went to the WildTrack platform (login-gated;
  Campaign 7's FIT kill stands).
- **Murie *Field Guide to Animal Tracks* full text
  (archive.org).** REAL text, 327,680 B sampled, md5
  `83d9e2e74893e773830088cd479e183a`. The book built on the
  canonical plaster-cast collection is openly digitised;
  the collection itself has no file surface (see Kills).
- **FWS manatee photography guidelines (agency document).**
  REAL PDF, 48,643 B, md5 `eb7218e1a5303a5263671eba42676a38`
  — the MIPS intake funnel's public face; no catalogue
  files in that folder.

## KILLS & CUSTODY FINDINGS — probed, nothing claimable, evidence stated

- **Koala fingerprints — KILL, paper-only (the wave's
  cleanest negative).** Four keyword searches surfaced zero
  collection hosts and zero adelaide.edu.au pages; the whole
  surface is two small papers (Henneberg et al. 1997, ~20
  koalas; the 1996/98 conference paper, 3 koalas + 1 chimp,
  platform-gated on Academia.edu). The whole-domain Adelaide
  CDX redo failed twice on Wayback's side (500, then 502 —
  the domain is too large for the query), so the CDX check
  is stated as **unrun**, not as zero; the kill rests on the
  search evidence. Any larger print set is in Henneberg's
  Adelaide custody, offline. The niche's premise — a print
  *collection* — does not survive contact.
- **Dog nose prints — KILL for recovery; custody finding.**
  The historic registry is paper: the Canadian Kennel Club
  accepted nose prints 1938–April 1992, on 3×3″ serial-
  numbered cards, and states the record is now **on
  microfiche** (verified in the NPDD article's own text this
  campaign, after verify8's first regex missed it on HTML
  entities — corrected in the completion pass). The modern
  study datasets are custody too: the Korean viability
  study's Data Availability Statement (checked in full)
  offers its 278 images / 70 dogs only by contacting the
  corresponding author; the largest modern set (Ant Group,
  6,000 dogs / 20,000 photos) was challenge-distributed and
  is no longer publicly accessible. Commercial nose-ID apps
  are live databases — custody by design, not targets.
  (Correction to the niche card, recorded: Petersen 1922,
  the "350+ nose prints" anchor, was **bovine**, not canine;
  the earliest canine work is Horning et al. 1926.)
- **Plaster track casts — KILL for recovery; custody
  finding.** No loose cast file pile exists on any surface
  probed. The Smithsonian's cast-bearing specimen records
  sit in its formal DwC-A/IPT archive (database by design);
  the one digitisation project, Idaho Virtual Museum's
  footprint virtualization (Patterson/Titmus casts 3D-
  scanned), serves 2D/3D views on a platform whose own
  Sources page states — verified this campaign — "Access
  to original models is subject to owner approval" by
  email. Murie's plaster-cast collection (assembled since
  1921, the basis of the *Field Guide*) has **no online
  catalogue surface at all**; its plausible custodian (the
  Murie Museum, Teton Science Schools) publishes no cast
  inventory. Drawers, not files.
- **Elephant footprint age — KILL for the calibration set;
  custody finding.** The known-age calibration series the
  niche exists for (Western/Moss/Georgiadis; Lee & Moss)
  lives in ATE's internal Microsoft Access demography and
  sightings databases — ElephantVoices' own science page
  (crawled; its only data files are ethogram videos) states
  the arrangement, and no measurement sheet is served
  anywhere probed. The one public calibration-grade set
  (Parker) was already formally published (INVENTORY
  above). What a campaign would need is an ATE data
  agreement, not a crawler.
- **Right-whale big systems — KILL, custody documented.**
  The North Atlantic catalogue is researcher-only by
  written protocol: NARWC's database-access PDF is live
  (HEAD 200, 110,041 B) and states access is refused for
  open-ended exploration or any use making data public;
  ARWPIC is the Australian platform into which the regional
  catalogues (Encounter Bay included) have been updated;
  the Valdés catalogue is curated ICB custody, ingested
  into Flukebook. Documented, never circumvented.
- **MIPS — custody (the GOLD's anchor, stated as such).**
  Florida's Manatee Individual Photo-ID System (5,146
  animals, 126,800+ sighting records, FWC FY2023-24) is an
  agency database with role-based access. The GOLD set's
  comparison will need it only through a formal data
  request or through the public Blue Spring derivatives
  (SMC's adoptee sheets and Hartley's published
  *Genealogies*) — the pre-registration is written to run
  on the public ruler first and says so.

## Ranking

1. **Blue Spring Practical Scar Sheets (2013) — GOLD.**
   The mammal registry's first gold, from its last seed:
   a frozen, complete, one-observer sketch catalogue of
   ~200 manatees, stranded on an NGO's archive subdomains,
   with its anchor (MIPS / Blue Spring known identities)
   and its un-run comparison (scar-ID persistence vs the
   sheet's own drop rules) both named. Pre-registered for
   comparison in `~/workspace/manatee-scar-sheets/`.
2. **Guard-hair atlas stack — SILVER.** Four continents of
   forensic hair atlases, all published, never cross-
   checked; the comparison is runnable today on public
   data, which is exactly what silver means.
3. **EBRWS catalogue stack — SILVER (small).** A live,
   growing regional catalogue in the open — and already
   reconciled into ARWPIC, which caps it.
4. **CKC nose-print microfiche + ATE Access databases +
   Murie cast drawers — the wave's custody map.** Three
   more archives that exist, matter, and are not files:
   the digitisation-with-institutions list grows.

*Method notes (standing + this wave's corrections): Wayback
counts status-200-filtered before counting; every grade
rests on ≥1 sample download with size + md5 + magic in
`outputs/verify8-20261118-190946.json` /
`outputs/verify8b-20261118-191140.json`, except where a host
blocked this client and the shortlist says so (Utah, Parker
handbook, Landcare). Corrections made mid-wave and recorded:
verify8's CDX filters used `(?i)` inline flags, which made
Wayback return 500 — the affected counts (ZSI, Adelaide)
were re-examined in verify8b and are reported as unrun/
restated, never as zeros; verify8's CMU samples were
thumbnails — a full-size image was sampled in the
completion pass (md5 above); the NPDD microfiche line was
recovered on tag-stripped text after the first regex missed
it. README verified-results NOT updated in this report —
the parent agent decides whether the scar-sheet set joins
the Fonozoo entry there.*
