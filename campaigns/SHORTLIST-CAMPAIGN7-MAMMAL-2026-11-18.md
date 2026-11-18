# Goldmine Hunter — Campaign 7 shortlist: the Mammal Wave (2026-11-18)

The **mammal-grain registry's** first campaign: all 7 seed groups
from `PROBE-MAMMAL-SEEDS.md`, in firing order, heads of the seven
9/10 mammal niches. Grades are `GRADES.md`'s, fixed before
Campaign 6 and applied unchanged — GOLD / DIAMOND / SILVER /
INVENTORY / KILL, never awarded on raw counts. Method: live
crawl + Wayback inventory filtered to statuscode:200 before
counting (`campaign7_mammal.py`,
`outputs/campaign7-20261118-184037.json`), then two targeted
verify passes (`verify7.py`, `verify7b.py` plus a correction
pass; `outputs/verify7-20261118-184432.json`,
`outputs/verify7b-20261118-184955.json`; samples in
`gold/campaign7-verify/`, 33 MB total new disk). Password-
protected / researcher-only systems (Gorongosa Who's Who,
GoMDIS) were documented as custody questions and **not** scraped
or circumvented, per the campaign's terms.

**Headline, plainly: the Mammal Wave found NO GOLD and NO
DIAMOND.** Two SILVER, three INVENTORY, and a run of honest
kills — several of them major *custody* findings, which are
reported as exactly that. The mammal photo-ID world was
professionalised into platforms, databases and card custody a
generation before frog calls were; at this grain the pattern
files live behind catalogues, inside databases, or on paper.
The autonomous chain therefore stops here: with no GOLD set
there is no novelty scrub and no pre-registration to write.

## SILVER — published-by-design, verified

**Juneau Flukes humpback catalogue — edition stack
(PUBLISHED-BY-DESIGN, live, verified). Niche:
whale-fluke-trailing-edge.** The little Juneau non-profit openly
serves its catalogue as a kept series of PDF editions — 2015
(v5), 2019, 2021, 2023, 2025 — the classic regional-catalogue
shape, done properly:

| Edition | Evidence |
|---|---|
| 2015 v5 (Wayback) | REAL PDF, 9,233,339 B, md5 `96c5f262b4bf1b9d889765335ff1d4db` |
| 2019 (live HEAD) | 200, 8,108,821 B, application/pdf |
| 2021 (live HEAD) | 200, 8,108,821 B (same size as 2019 — the two URLs may serve the same file; stated, not resolved) |
| 2023 (live HEAD) | 200, 21,420,332 B, application/pdf |
| 2025 (Wayback capture, 2025-06-14) | REAL PDF, 5,242,880 B, md5 `43e364672251747023c716e37aab2fdc` |
| 2025 (live, today) | REAL PDF, 12,755,000 B as downloaded, md5 `2403f00bd987c2759f3583d5b8b4295f` |

The 2025 file has *grown at the same URL* since its June
capture — the stack is alive, not stranded. SILVER, not gold,
twice over: openly published by its own project, and Southeast
Alaska sits inside the North Pacific set Happywhale already
joined (the Juneau catalogue is one of Cheeseman et al.'s 39).
A Juneau-only edition-vs-edition comparison (2015→2025: which
individuals persist, how the catalogue's own IDs churned) is
runnable from this stack but is a vintage note, not a recovery.

**Wellcome Collection — Galton fingerprint digitisation
(PUBLISHED-BY-DESIGN, live, verified). Niche:
primate-fingerprints-dermatoglyphics (the human/Galton surface
of it).** The Galton Papers' "Fingerprints" work is openly
served as a IIIF presentation manifest
(`iiif.wellcomecollection.org/presentation/v2/b20633257`) with
**3,022 canvases**; canvas 0 sampled: REAL JPEG, 123,308 B, md5
`f7c703e7bf52039008c5cd3f236ffd75`. A curated national archive
serving its digitised ledgers openly — the Barts class, SILVER.
**The split, plainly:** the niche's actual quarry is *not* in
this surface. The "Chimpanzee Fingerprints" work (Weldon's 1894
bundle, `n9q6q77r`) resolves via the catalogue API to a single
item whose only location is **closed-stores** — no IIIF, no open
images. The Penrose dermatoglyphics series is likewise
catalogue-only. The primate print sets remain reading-room
objects; see Kills.

## INVENTORY — verified real, published, no comparison completed

- **Dominica sperm-whale Fluke Book (PUBLISHED-BY-DESIGN,
  live).** The Whitehead Lab (Dalhousie) serves the Dominica
  project's fluke catalogue PDF openly: REAL PDF, 1,343,030 B,
  md5 `170f9858299f4c01857d91d1ea937b92` (`Flukebook2016.pdf` —
  the 10 regularly-encountered families' ID pictures). A single
  published project catalogue; the project also feeds
  Flukebook.org. Inventory.
- **NOAA Beaufort dolphin catalogue extracts — NCEI formal
  archive (PUBLISHED-BY-DESIGN, DOI 10.25921/4dwb-6b76).**
  The 2018 survey's match-to-master-catalogue tables are real
  and openly archived: `2018_match_to_master_catalog.csv`
  76,187 B, md5 `d1d4ba57f2ed6417277f8f734095cea7`;
  `2018_SNCES_id_dolphins.csv` 63,433 B, md5
  `860c5c3a5ac1e59e3c17de2f9f983b30`; and the companion photo
  zip (~1,000 dorsal-fin photographs of catalogue-matched
  individuals) is live in the same accession — HEAD 200,
  545,259,230 B, PK magic on a range probe (not bulk-
  downloaded, per method). Exactly what the probe hoped the
  FinBase era had left loose — except it was deposited in the
  formal archive, with a DOI. The long-term Beaufort master
  catalogue (1995– ) itself remains lab-held; this is a subset.
  Inventory.
- **Desert Lion published reports (PUBLISHED-BY-DESIGN).**
  The Kunene whisker-spot survey (Conservation Namibia):
  REAL PDF, 4,303,341 B, md5 `1f267067ff76801f7efad2fcc9393b5e`
  — 57–60 adults, 54 whisker-photographed, ID cards reproduced
  in the report. Stander's downloadable section report via
  Wayback: REAL PDF, 935,761 B, md5
  `3593f11bfdc87ee04b116ef6affd3d5e`. Published reports that
  *contain* ID-card examples — not the catalogue behind them.
  Inventory.
- **elephant.se (PUBLISHED-BY-DESIGN database; adapter
  class).** The Elephant Encyclopedia & Database serves AERP
  life-history records page-by-page (8,772 status-200 collapsed
  captures in CDX, all database pages; **zero** document-type
  files). A working public database, not a file pile — and not
  the Amboseli ear-ID card archive, whose originals stay in
  ATE custody. (Client note: the live site 403s this campaign's
  fetcher while its records are publicly indexed — a bot-wall
  result about our client, stated as such.) Inventory as a
  database; KILL as a hunter target.

## KILLS & CUSTODY FINDINGS — probed, nothing claimable, evidence stated

- **Wagyu muzzle-print archive (cattle-muzzle-prints) —
  KILL for recovery; the wave's largest custody finding.**
  The registry association's own site (wagyu.or.jp) is a
  WordPress shell: crawl + full CDX redo found **zero**
  document/data files of any kind. The NLBC 10-digit ID
  search — the second ruler, with DNA — is an interface, and
  was unreachable from this client besides. No scanned print
  surface was found on any host probed, in either language's
  literature trail this campaign followed. The finding is the
  absence: **3M+ ink muzzle prints since 1948 exist as paper
  registry cards and as the print carried on each animal's
  certificate — the archive was never digitised as images.**
  What digitisation would need, stated for the record: an
  institutional agreement with the National Wagyu Registry
  Association; scanning at the registry's prefectural
  branches (prints are taken <4 months and again >14 months,
  so most animals hold *two* dated prints — a built-in
  longitudinal pair); and the join key already exists — the
  10-digit national ID with its DNA sample in NLBC. Nobody
  needs to invent the ruler; somebody needs to scan the cards.
- **Primate print sets proper (Galton chimp bundle, Penrose,
  Wistar sources) — KILL for recovery, custody documented.**
  Chimpanzee bundle: closed-stores at UCL (see SILVER split
  above). Midlo & Cummins' 1942 monograph — the published
  layer pointing at the deposited sets — is itself openly
  digitised (archive.org `americananatomic20wist`, full text
  + PDF; this campaign's advancedsearch API returned zeros
  for every query and the record was corrected via web
  search, stated as a method correction). The Wistar-era
  print sets the monograph's source table names: no digital
  surface found anywhere probed. Reading-room archaeology,
  not a web recovery.
- **Gulf of Maine humpback catalogue (Center for Coastal
  Studies) — KILL.** The crawl found no data files; the
  domain's 309 status-200 PDFs are reports — 53 whale/report-
  named, sampled ones are annual reports (2010–11: REAL PDF,
  2,640,389 B, md5 `826bf0486f964b16d2a40cff862ee81a`;
  2014 draft: 1,723,653 B, md5 `0a1a203422a13b1ee71c855fff21bc99`)
  and right-whale survey reports. The catalogue itself is a
  curated database (CCS / Allied Whale's 11,000-individual
  North Atlantic catalogue), access by collaboration — the
  database class again. (The North Atlantic sperm-whale
  catalogue, NAMSC, is the same story one era earlier: 2,081
  photographs published **on CD in 1999**; no web file pile
  exists to hunt.)
- **Southern Ocean Danco Coast catalogue — NOT CLAIMED.**
  The only surface found is a 2026 CCAMLR meeting paper; the
  test-instance (UAT) host served an HTML phantom for it and
  the production host was unreachable from this client. A
  published meeting paper in any case — stated as unrun, not
  as zero.
- **Sarasota / GoMDIS (dolphin-dorsal-fin-notches) — KILL,
  custody documented (not a target).** Campaign crawl
  confirms the probe: sitemaps and one video; the 5,000+
  fin catalogue and GoMDIS (35 catalogues, 23,444
  individuals) are researcher-only by design. The non-Gulf
  FinBase-era catalogues left no public file piles on any
  host probed — the one concrete public extract (Beaufort)
  had been formally archived instead (INVENTORY above).
- **Elephant ID-card systems (ElephantVoices / ATE / Save
  the Elephants) — KILL, custody documented.** ElephantVoices'
  file surface is the *calls* audio (20 status-200 mp3s, the
  known 2012 pile), not ID cards; Gorongosa's Who's Who is
  password-protected (poaching precaution) and was not
  touched. ATE's site was unreachable from this client on
  every attempt (proxy failures) and returns zero status-200
  collapsed captures in CDX — a host result about reachability
  and capture coverage, not a claim about what ATE holds.
  Save the Elephants: CMS furniture only. The card tradition
  (1,600+ Amboseli elephants since 1972) remains exactly
  where the probe left it: in project custody, partly still
  physical.
- **FIT training libraries (paw-track-morphometrics-fit) —
  KILL.** WildTrack's site is furniture and sitemaps (4 live
  "data" files, all site labels). The per-species libraries
  are real and documented — the tapir algorithm's training
  set is **426 footprint images from 36 captive individuals**
  (PeerJ 2018, PMC5878928, fetched and checked) — but they
  live with the projects (Medici/WildTrack; the otter CNN's
  2,500 images with IUCN-OSG/WildTrack), the journal
  supplements carry the algorithm documents rather than the
  image libraries, and the FIT software itself is a JMP
  add-in distributed on request. No project file pile exists
  on any surface probed.
- **Whisker-spot catalogues (whisker-spot-patterns) —
  KILL.** Desert Lion's 7,527 status-200 jpgs are field-photo
  galleries filed by date, not ID-pattern files; its only
  documents are the 5 downloadable PDFs (protocols + the
  Stander report, INVENTORY above). EWT and WII are
  front-ends with no data files. The Australian sea-lion
  validation set (53 individuals) exists in the literature
  and a Curtin thesis — no dataset host found. Three
  literatures, one geometry, no joined archive — and, this
  campaign adds, no *loose* archive either: the records live
  inside project systems (Kunene Lion Rangers/MEFT, WII's
  Lion software) that do not publish files.

## Ranking

1. **Juneau Flukes edition stack — SILVER.** Five live
   editions of a regional fluke catalogue, sample-verified;
   the wave's most complete verified set, and a runnable
   (if modest) edition-vs-edition vintage comparison.
2. **Wellcome Galton IIIF digitisation — SILVER.** 3,022
   openly served canvases of the founding fingerprint
   archive; the primate subset pointedly *not* among them.
3. **Wagyu muzzle-print archive — KILL, and the wave's most
   important negative.** A 3M-print, two-print-per-animal,
   DNA-keyed archive that exists only on paper. Not gold —
   but the clearest digitisation target this hunter has yet
   produced, and it was produced by looking.
4. **Beaufort NCEI extracts + Dominica Fluke Book + Desert
   Lion reports + elephant.se — INVENTORY.** Real, verified,
   published; nothing to recover.

*Method notes (standing + this wave's corrections): Wayback
counts status-200-filtered before counting; every grade rests
on ≥1 sample download with size + md5 + magic in
`outputs/verify7-20261118-184432.json` /
`outputs/verify7b-20261118-184955.json`. Corrections made
mid-wave and recorded: verify7's first CDX alternation filters
were malformed (per-character queries) — all affected counts
were redone per-extension in verify7b and only the redone
numbers appear above; the archive.org advancedsearch zeros
were an API artefact, corrected via web search; the CCAMLR
UAT "PDF" was an HTML phantom and is claimed as nothing.
README verified-results NOT updated — no find in this wave
meets the stranded bar those entries set.*
