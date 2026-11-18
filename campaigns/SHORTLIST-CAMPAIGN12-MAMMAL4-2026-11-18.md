# Goldmine Hunter — Campaign 12 shortlist: Mammal Wave 4, the 7/10 batch part 1 (2026-11-18)

The **mammal-grain registry's** fourth campaign, generated from
the recalibrated queue: the first ten unfired 7/10 niches, in
registry order — primate-palm-sole-dermatoglyphics,
paw-pad-ridge-patterns, bear-paw-mensuration,
canid-track-size-archives, snow-track-gait-archives,
elephant-tusk-patterns, cheetah-spot-patterns,
snow-leopard-rosettes, painted-dog-coat-patterns,
pangolin-scale-patterns. Grades are `GRADES.md`'s, unchanged.
Method = Campaigns 7–8 exactly: live crawl + Wayback inventory
filtered to statuscode:200 before counting
(`campaign12_mammal4.py`,
`outputs/campaign12-20261118-195606.json`), then targeted verify
passes (`verify12.py`, `verify12b.py` plus a Wayback correction
pass; `outputs/verify12-20261118-195657.json`,
`outputs/verify12b-20261118-195725.json`,
`outputs/verify12c-20261118-195745.json`; samples in
`gold/campaign12-verify/`, 36 MB total new disk).
Researcher-only / sensitive systems (Gorongosa Who's Who,
snow-leopard PAWS locations, park pack catalogues) were
documented as custody and **not** scraped or circumvented.

**Headline, plainly: NO GOLD, NO DIAMOND, NO SILVER.** Four
INVENTORY and six KILL/custody results. The 7-band behaves
exactly as the calibration law predicts: every niche's material
exists, and every niche's files are a formal archive, a journal
PDF, a programme database, or paper — none is a loose pile on an
old website. The wave's product is its custody map, stated as
such. With no GOLD set there is no novelty scrub and no
pre-registration to write.

## INVENTORY — verified real, published, no comparison completed

- **NASA Snow Wildlife Tracks, WA & AK (ORNL DAAC 2188) —
  formal archive (PUBLISHED-BY-DESIGN, DOI
  10.3334/ORNLDAAC/2188). Niches: canid-track-size-archives AND
  snow-track-gait-archives (one dataset serves both cards).**
  Three field seasons (Jan 2021–Mar 2023), 707 sites: fresh
  tracks of wolves, coyotes, bobcats, cougars and ungulate prey
  with width/length of three consecutive footprints, sink depth,
  gait class, and snow density/hardness — measurement-level
  track data of exactly the kind both niche cards imagine
  stranded in agency PDFs, deposited instead in NASA's formal
  archive as CSV. Verified here: the user-guide PDF is REAL
  (1,204,031 B, md5 `98abda1b3bbbcd2ea6186057ce8b7f0a`) and the
  data.gov catalogue carries the 707-site description. The
  bundle zip itself is Earthdata-login-gated (HEAD 200,
  869,271 B, application/zip; the unauthenticated GET returns a
  27-byte stub, excluded and deleted) — the CSVs were **not**
  sampled, and nothing above rests on them beyond the guide and
  catalogue record. Inventory.
- **Hokkaido brown-bear field-sign dataset, 1976–2015 —
  formal data paper (PUBLISHED-BY-DESIGN). Niche:
  bear-paw-mensuration.** Forty years of Teshio Experimental
  Forest monitoring (identifier ERDP-2026-01, *Ecological
  Research* 2026), recording front-paw pad width where
  measurable — with the paper itself carrying the niche's
  second ruler in print: front-paw width >135 mm discriminates
  adult males (Maeda & Ohdachi 1994). The journal page was
  unreachable from this campaign's client (connection broken /
  403-class failures), so this entry rests on the discovery
  pass's search-indexed full text, stated plainly; no sample
  was obtained. The harvest-ledger half of the niche (check-
  station paw cards) surfaced nowhere: the Virginia DWR page
  carrying the modern form of the rule ("a front paw track of
  4½ inches wide or greater is generally a male") bot-walled
  this client (403) and is claimed only as search-indexed
  evidence. Inventory as a dataset; KILL as a ledger hunt.
- **Murie *Field Guide to Animal Tracks* full text +
  Amherst tracks sheet (PUBLISHED-BY-DESIGN). Niche:
  paw-pad-ridge-patterns.** The pad/tracks literature's
  canonical text is openly digitised: Murie djvu text sampled
  REAL (458,752 B head, md5 `5980cfbf621cec06e9dc2619248781e9`)
  — including the polar-bear pad figure drawn from a Woodland
  Park Zoo pad-on-sand capture, the niche's protocol in 1954.
  The Amherst identification sheet is a REAL PDF (3,425,108 B,
  md5 `a18c578f62ff5c80fd65b086de40495c`). Published guides,
  not pad archives; the cast collection behind Murie was
  already killed at its own grain in Campaign 8. Inventory.
- **Kelly 2001 + Mara-Meru 2022 (PUBLISHED-BY-DESIGN).
  Niche: cheetah-spot-patterns.** The Serengeti system's
  founding paper — 3-D computer matching of ~10,000
  photographs over 25 years — survives on the author's
  personal site: REAL PDF, 262,988 B, md5
  `ede0700c3269d8bfadf4f2079b7d11dc` (mjkelly.info; its
  Wayback pile is one unrelated `Puma.mov`). The Mara-Meru
  project's 2022 annual report is a REAL PDF (8,049,538 B,
  md5 `333c4d8845fd0089d2c9da2d9444f471`): limb/tail spot ID
  from one month old, 277 adults since 2001 — and its
  >90,000 photographs are the project's own processing pile.
  The papers and reports are public; the albums are custody
  (see Kills). Inventory.

## KILLS & CUSTODY FINDINGS — probed, nothing claimable, evidence stated

- **Primate palm/sole dermatoglyphics — KILL, paper-only
  (the wave's cleanest premise failure).** No print archive
  surface exists on any host probed. What exists is a journal
  literature whose comparisons were *already run by its own
  authors against the karyotype anchor*: the 1970 Turkish
  series (72 Down cases, 473 controls; maximal atd ≈87° vs
  ≈50°) is a REAL PDF (921,950 B, md5
  `65946c224532dad75fcd19b93f3d8708`), and the 2023 Kosova
  replication (104 Down, 403 karyotyped controls; atdT 161.9°
  vs 92.6°) is a REAL PDF (561,584 B, md5
  `d66ede950e16330aa11356e66a49ea92`). The clinical print
  collections themselves are medical-school files with no web
  surface, and the niche's un-run-comparison element fails —
  the run was published in 1970. Kill.
- **Canid track tables beyond NASA — KILL for the survey
  tables.** Wisconsin's wolf programme (17,771 miles of winter
  track surveys in the 2025–26 report alone) publishes
  summary reports, not measurement tables: the 2026 report is
  a REAL PDF (3,821,391 B, md5
  `482b49a25cd9780f6735b9831cc52f88`, on a preprod Pantheon
  host) whose inputs are occupancy-model counts. The
  measurement-level exception is the NASA dataset above —
  formally archived. Kill as a stranded hunt.
- **Finland's wildlife triangles — KILL for gait-level
  files; custody is institutional.** Luke's scheme (forest
  triangles since 1989, ~1,200 triangles, >10,000 km/winter)
  is the niche card's flagship and it is a national institute
  programme: luke.fi serves no data files to this crawl (12
  pages, 0 data files), the published layer is crossing
  *counts* and indices (the 2026 *Ecography* lynx paper uses
  2016–2020 triangle counts, not gait measurements), and the
  gait/stride-level records the card imagines were never the
  scheme's published unit. Kill.
- **Elephant tusk patterns — KILL, custody documented.**
  Tusk configuration is a *field inside* the Elephant Who's
  Who & Whereabouts database (Mara + Gorongosa), not a file
  archive: the system paper is verified REAL (3,665,008 B,
  md5 `4e0eeefd03f8bf8c02b2084ed6313671`) and describes
  tusk attributes ("one left", "broken left", tuskless) as
  search keys in an admin/user database fed by the EleApp.
  Campaign 7 already documented Who's Who as
  password-protected; it was not touched. ElephantVoices'
  Wayback pile (20 status-200 files) is the known 2012 audio
  pile, not ID files. The Gorongosa tusklessness series
  (18.5% → 50.9% of females) lives in that same custody.
  Kill.
- **Snow-leopard rosettes — KILL, custody documented (and
  location-sensitive by design).** The pattern files are
  programme libraries: the Snow Leopard Trust's own page —
  text-checked this campaign — describes >1,000,000 images
  tagged across the Himalayan/Trans-Himalayan PAWS effort and
  rosette ID by ≥3 markings, all inside the programmes; the
  site's live data files are outreach mp4s. Range-country
  catalogues (WCS Afghanistan, Sanjiangyuan's ~10,000 events)
  are likewise project-held, and their locations are
  poaching-sensitive — documented, never targeted. Kill.
- **Painted-dog coat patterns — KILL, park custody.** No
  loose catalogue pile on any surface probed: Painted Dog
  Conservation's crawl is furniture (12 pages, 0 data files;
  its Wayback status-200 set is 4 site-furniture XML files),
  EWT's surface is a front-end (Campaign 7's class), and the
  pack catalogues the card names (Selous/Kruger/Botswana)
  publish nothing file-shaped. The name-books stay in the
  parks, exactly as carded — which is a custody finding, not
  a recovery. Kill.
- **Pangolin scale patterns — KILL, and the premise is the
  wave's weakest.** The PUNS preprint (REAL PDF, 758,358 B,
  md5 `a8baf6957968800d771e87ab58cc5e63`) states the field's
  own position: *no universal marking system exists, half of
  programmes mark scales, each with its own system* — and the
  marking is **notching**, not pattern photography. The
  seizure side is species-level only: the IUCN monitoring
  methods document (CITES CoP18 Inf. 75) was verified via
  Wayback after the live host failed this client — REAL PDF,
  1,328,974 B as downloaded, md5
  `46989cfadb549f8704171b85b8852ff8` — and WTI's 2026
  post-seizure guide (REAL PDF, 13,586,838 B, md5
  `bd2e3db9148cd8beadd0f4f6dc587533`) keys pangolins by scale
  *shape per species*, never by individual pattern. No
  individual scale-pattern archive was found because, on the
  evidence, none is kept. Kill.

## Ranking

1. **NASA Snow Wildlife Tracks (ORNL DAAC 2188) —
   INVENTORY.** The wave's most complete verified dataset:
   measurement + gait level, 707 sites, three seasons, DOI'd
   in the formal archive — the comparison the canid and
   snow-track cards want is runnable from it today, which is
   what inventory means.
2. **Hokkaido 40-year bear field-sign dataset —
   INVENTORY.** A designed long-run paw-width series with its
   sexing rule carried in the same paper; formal data-paper
   custody (and unsampled from this client, stated).
3. **Kelly 2001 on a personal site + Mara-Meru reports —
   INVENTORY.** The cheetah ID literature's public layer;
   the 10,000- and 90,000-photo albums behind it are the
   wave's clearest digitisation-with-projects targets.
4. **The custody map — the wave's real product.**
   Who's Who (tusk fields), PAWS (1M+ images), Luke's
   triangles, Wisconsin's survey inputs, the parks' painted-
   dog name-books, and pangolin programmes' incompatible
   notching systems: six more archives that exist, matter,
   and are not files.

*Method notes (standing + this wave's corrections): Wayback
counts status-200-filtered before counting; every grade rests
on ≥1 sample download with size + md5 + magic in
`outputs/verify12-20261118-195657.json` /
`verify12b` / `verify12c`, except where a host blocked this
client and the shortlist says so (Virginia DWR 403, Hokkaido
journal page, NASA login-gated bundle). Corrections made
mid-wave and recorded: verify12b's first CITES Wayback URL
was malformed and returned a 4,757 B HTML phantom — excluded,
re-fetched via the `id_` form in verify12c and only the
re-fetched PDF is claimed; the NASA bundle's 27-byte
unauthenticated stub was likewise excluded and deleted, never
counted as a sample. README verified-results NOT updated —
no find in this wave meets the stranded bar those entries
set.*
