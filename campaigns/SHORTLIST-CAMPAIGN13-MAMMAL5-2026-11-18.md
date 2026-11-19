# Goldmine Hunter — Campaign 13 shortlist: Mammal Wave 5, the 7/10 batch part 2 (2026-11-18)

The **mammal-grain registry's** fifth campaign, generated from
the recalibrated queue: the next eight unfired 7/10 niches, in
registry order (ranks 34–41) — dental-casts-mammal,
antler-tine-records, horn-annuli-age-records, bat-wing-venation,
livestock-iris-patterns, ear-notch-punch-registries,
hyena-ear-notch-id, scar-based-photo-id. Grades are
`GRADES.md`'s, unchanged. Method = Campaigns 7–8/12 exactly:
live crawl + Wayback inventory filtered to statuscode:200
before counting (`campaign13_mammal5.py`,
`outputs/campaign13-20261118-214142.json`), then targeted verify
passes (`verify13.py`, `verify13b.py`;
`outputs/verify13-20261118-214423.json`,
`outputs/verify13b-20261118-214522.json`; samples in
`gold/campaign13-verify/`, 36 MB total new disk).
Subscription / registration-gated systems (Boone & Crockett
Big Game Records LIVE), project photo albums (Mara Hyena
Project), and breed-association books of record were documented
as custody and **not** scraped or circumvented.

**Headline, plainly: NO GOLD, NO DIAMOND, NO SILVER.** Three
INVENTORY and five KILL/custody results. Part 2 of the 7-band
repeats part 1's shape and adds two of its own: the flagship
record system is a *subscription platform* (B&C), and one card's
premise conflates two different organs (the livestock
"iris" trials were overwhelmingly **retinal** — Optibrand — and
that vendor's database is gone). The wave's product is again
its custody map, plus one genuinely useful published dataset
(Holekamp hyena CSVs) and one small agency vintage stack
(Montana FWP bighorn summaries).

## Verdict table

| Niche | Hosts probed | Verified files | Custody class (post-probe) | Grade | One-line evidence |
|---|---|---|---|---|---|
| dental-casts-mammal | Cambridge assets (Swindler excerpt), archive.org (RCS catalogue) | 0 sampled (excerpt unreachable from this client both schemes; RCS djvu URL returned an HTML phantom, excluded) | PHYSICAL_OBJECTS → KILL | **KILL** | The named collection (Swindler's primate plaster casts, from AMNH/Smithsonian/Field/Cleveland skulls) is a physical drawer collection whose only web surface is its book; no cast photographs or measurements exist as files anywhere probed. |
| antler-tine-records | boone-crockett.org (2 pages), Fort Carson iSportsman, Nebraskaland Magazine (UNK) | 2 REAL PDFs (sample score sheets only) | FORMAL_OR_PLATFORM → CAUTION | **KILL** | The comparable set (64,000+ B&C records, 1830–present, full score charts) lives behind the subscription Big Game Records LIVE 2.0 platform — an interface, no file pile; the known-buck shed series (UNK 11-yr Platte collection, Mississippi penned study) are project/physical holdings mentioned in articles, never posted. |
| horn-annuli-age-records | myfwp.mt.gov repository (3 years), nwsgc.net, midwestwildsheep.com | 4 REAL PDFs (3 MT summaries + NWSGC proceedings) | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | Montana FWP publishes district-level ram tables (age, horn length R/L, base circumference, kill date) as loose repository PDFs — a real small vintage stack, published by design; the card's validation comparison was already run by the field (NWSGC 2012: goat horn increments vs Matson's cementum, 24 teeth; Ram Mountain known-age horn analyses published since 2004). |
| bat-wing-venation | PMC (Seheult 2025), BioOne (Amelon 2017), archive.org (Antillean key) | 0 data files (papers only; key PDF unreachable live and absent from Wayback CDX for its exact URL) | CUSTODY_RESTRICTED → KILL | **KILL** | Two real wing-photo sets exist — Amelon's 1,212 photos / 230 bats and Seheult's 328 photos / 58 big browns — both lab-held with no repository or supplement file surface, and the individual-matching comparison the card imagines was already run by both papers (blind matching 2017; HotSpotter 2025). |
| livestock-iris-patterns | IntechOpen (Optibrand chapter), MDPI (horse iris), matr.net (Optibrand news) | 2 REAL PDFs (papers/chapter only) | CUSTODY_RESTRICTED → KILL | **KILL** | Premise correction: the 2000s livestock trials were retinal (OptiReader), stored in Optibrand's own secure database — the vendor is defunct and no image set ever surfaced; true-iris sets are equally closed (Arabian-horse database "offered to interested researchers"; Zhaosu 54-horse set is a 2025 paper's self-built data, not a stranded pilot). |
| ear-notch-punch-registries | UNL Extension, Illinois 4-H, Minnesota BAH | 2 REAL PDFs (chart + handbook) | PAPER_ONLY → KILL | **KILL** | The system itself is published everywhere (Universal 1-3-9-27-81 charts), but the registry the card wants is paper by law: a notch is official ID only when "recorded in the book of record of a purebred registry association" (9 CFR §71.19, carried in the verified Minnesota handbook) — a century of association card files with no digital surface. |
| hyena-ear-notch-id | holekamplab.org (+ whole-domain Wayback), PMC/NSF review, msuhyenas.blogspot.com (+ Wayback) | 1 REAL zip (7 CSVs + README) + 1 REAL review PDF | CUSTODY_RESTRICTED (ear albums) / FORMAL_OR_PLATFORM (CSV database) → KILL / CAUTION | **INVENTORY** | The ear/spot quarry is project custody — clan photo albums are carried in research vehicles, ear damage is only a narrowing aid, final ID is by spot pattern (verified review) — but the lab publishes its behavioural database by design: live zip, 991 hyenas in `hyenas.csv`, 61,000+ session records claimed on the page; no ear diagrams or ID photos in the zip. Blog Wayback pile is furniture only (atom/sitemap/robots). |
| scar-based-photo-id | PMC + PLOS (Rice's whale catalog), MDPI (dolphin healing) | 2 REAL PNG figures (scar-matched whales) | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | The cross-species scar layer exists only inside single-programme catalogues, each published in its own paper or held by the programme: the newest, Rice's whale (NOAA SEFSC), publishes its full 31-whale catalog in-paper — cookiecutter bite scars as primary matching features, figures verified here; the manatee arm of this niche was already exhausted as Campaign 8's GOLD, and no programme's scar sketches are stranded as files. |

## INVENTORY — verified real, published, no comparison completed

- **Montana FWP Bighorn Ram Measurement Summaries —
  agency repository (PUBLISHED-BY-DESIGN). Niche:
  horn-annuli-age-records.** Loose PDFs served by the agency's
  `getRepositoryFile` system, three years sampled REAL: 1999
  (31,876 B, md5 `64bab5d4f04f956c793cd4d04f454749`), 2001
  (72,448 B, md5 `be11083a326c1e53028c05414a65648e`), 2006
  (89,050 B, md5 `e9a596a0e9d50081775e121cea94b864`). Each carries
  per-ram district, annuli age, right/left horn length, base
  circumference and kill date — measurement-level check-station
  data of exactly the kind the card imagines filed by district,
  because it is: the agency files it, publicly. The NWSGC 2012
  proceedings are also REAL (7,013,004 B, md5
  `ec9a9fccd7888b32eca2e56b64bd36b8`) and carry the goat
  horn-increment vs cementum comparison (177 horns, 472
  increments; 24 cementum ages, 12 identical, 5 off by one) —
  the card's second-ruler run, done by the field in 2012.
  Inventory.
- **Holekamp Lab MSU Hyena Project data files —
  lab site download (PUBLISHED-BY-DESIGN). Niche:
  hyena-ear-notch-id.** One live zip, REAL (11,122,106 B, md5
  `9cdcf9dfc9f987889959489d9c83915c`), 20 entries: seven CSVs
  (`sessions.csv` 8,584,038 B; `aggression.csv` 2,161,057 B;
  `hyenas.csv` 236,297 B / 991 data rows; `immobilizations.csv`,
  `prey_count.csv`, `foods_consumed.csv`, `weather.csv`) plus a
  README .doc. The database page (text-checked) claims 61,000+
  session records since 1988 across five clans. This is a real,
  analysis-ready, individual-keyed dataset — and it contains
  no ear-notch diagrams, spot photos, or ID images at all.
  The niche's quarry is not in it. Inventory.
  **Pair Hunter flag:** `hyenas.csv` (991 individuals) joined
  to `immobilizations.csv` (darting events for the same IDs)
  is an individual-keyed pair inside one published zip — if
  the immobilization table carries the genetic/hormone lab
  results the database page describes, it is the card's
  ear/spot-vs-genetic pairing in tabular form, minus the ear
  layer. Worth a Pair Hunter look; published-by-design, so
  silver ceiling at best.
- **Rice's Whale Photo-ID Catalog, NOAA SEFSC 2004–2019 —
  journal publication (PUBLISHED-BY-DESIGN). Niche:
  scar-based-photo-id.** Thirty-one whales individually
  identified; cookiecutter shark bite scars "widely present"
  and used as primary matching features for non-distinctive
  fins (PMC text-checked). Figures sampled REAL: Fig 3,
  scar-matched whales (418,501 B PNG, md5
  `08cc7bed06933f890faccf9f40a5e9c7`), Fig 7, fin + peduncle
  scar matches 2007–2019 (392,046 B PNG, md5
  `56cbfd8b921938b8aaf236603dfc4c95`). (The PMC-instance
  supplementary .xlsx URLs returned 1.8 KB HTML stubs —
  phantoms, excluded and never counted; the MDPI dolphin
  healing PDF endpoint likewise returned a 408 B stub,
  excluded.) The catalog is published whole in its paper;
  the underlying photo archive is NOAA's. Inventory.

## KILLS & CUSTODY FINDINGS — probed, nothing claimable, evidence stated

- **Dental casts — KILL, physical objects (the koala class,
  again).** Swindler's primate dental-cast collection — the
  niche's concrete instance — was made from skulls at the
  AMNH, Smithsonian, Field Museum and Cleveland Museum, and
  its data surface is the published book *Primate Dentition*
  (search-indexed excerpt text: "plaster casts made from
  alginate impressions…"). The excerpt PDF itself was
  unreachable from this campaign's client over both http and
  https, stated plainly; the RCS fossil catalogue text URL
  returned HTML to this client (442,484 B phantom, excluded).
  No museum probed exposes cast photographs, scans, or
  tooth-row measurement files. The casts are drawers. Kill.
- **Antler tine records — KILL, platform custody.** B&C's
  Records Live 2.0 page (text-checked, status 200) describes
  a "subscription-based platform" cross-referencing "more
  than 50,000 official trophy entries"; the entry page puts
  the full century-scale set at 64,000+ records with score
  charts behind free registration and the database behind
  subscription. What is loose is only the blank instrument:
  the Fort Carson sample score sheet is a REAL PDF
  (1,142,308 B, md5 `453bf972e78bcacf27a1940294ee3409`) and
  the B&C S3 mule-deer chart is REAL (515,345 B, md5
  `42614960d5178b85348fd571f7ffa389`) — blank forms, not
  records. The shed-series half (UNK's 11-year Platte River
  cast-antler collection; the Mississippi penned-buck casting
  study) exists as magazine/journal prose about physical
  collections (the UNK magazine page bot-walled this client,
  403; claimed only as search-indexed evidence). Kill.
- **Bat wing venation — KILL, lab custody + already-run
  comparison.** The niche's real archive is two papers' photo
  sets: Amelon et al. 2017 (1,212 photographs, 230 individual
  bats, four species, blind evaluators matched 170) and
  Seheult et al. 2025 (192 adult + 136 pup photos, HotSpotter
  ranking — text-checked on PMC; no Dryad/Zenodo/figshare
  mention, no data files in the crawl). Neither set has any
  file surface, and both papers *are* the comparison the card
  proposes. The banding-era venation-tracing archive the card
  imagines surfaced nowhere; the Antillean field key PDF was
  unreachable live and has no Wayback capture for its exact
  URL (CDX rows 0). Kill.
- **Livestock iris patterns — KILL, and the card's premise
  needs correcting.** The 2000s trial literature is retinal,
  not iris: the verified IntechOpen chapter (REAL PDF,
  422,548 B, md5 `7dab7636f1c71db8654028f20a86c44d`) documents
  the Optibrand OptiReader retinal system throughout (Allen
  2008: 100% matching; Gonzales-Barron sheep: 100%), with
  images "compared visually to a printout or an online
  database" — Optibrand's database, from a defunct vendor.
  The 4-H trial behind it imaged 317 beef + 159 sheep; none of
  those images is on the web. True-iris work is no looser:
  the Arabian-horse iris database is offered to researchers
  by request, and the horse-iris paper sampled is REAL
  (6,838,585 B, md5 `37348bda857d6baf47fe63c2fee4fd78`) but
  its 54-horse Zhaosu dataset is a 2025 self-built set inside
  a super-resolution paper, not a stranded 2000s pilot. The
  stranded-pilot shape the card predicts does not exist for
  this niche. Kill.
- **Ear-notch & punch registries — KILL, paper-only by law.**
  The code is the most published object in this wave: UNL
  Extension's Universal-system page (text-checked, 200) and
  the Illinois 4-H spark sheet (REAL PDF, 505,747 B, md5
  `6da342356320f88e618d6dc0ee509c59`). The records are the
  opposite: the verified Minnesota Livestock Exhibition
  Handbook (REAL PDF, 6,221,710 B, md5
  `63a586da5e71cc6e3ea3e14bc12592f8`) carries the rule that
  swine ear notching counts as official ID only with breed
  registration paperwork, and federal rule (9 CFR §71.19, via
  the discovery pass) conditions it on the notch being
  "recorded in the book of record of a purebred registry
  association." The anchor the card names — associations'
  master registration books — is the custody: paper books and
  certificates, a century deep, never a file pile. Kill.

## Ranking

1. **Holekamp hyena CSV database — INVENTORY.** The wave's
   most complete verified dataset: 991 individuals, seven
   linked tables, published by its lab — and a Pair Hunter
   candidate (individual IDs × immobilization/lab records),
   though it holds none of the niche's ear/spot imagery.
2. **Montana FWP bighorn summaries — INVENTORY.** A genuine
   small vintage stack of measurement-level agency tables
   (1999/2001/2006 sampled; the repository pattern suggests
   more years), published by design.
3. **Rice's whale catalog — INVENTORY.** The scar-ID
   literature's newest complete catalog, published whole;
   its programme's photo archive stays NOAA's.
4. **The custody map — the wave's real product.** B&C's
   subscription platform (64,000+ records), the Mara clan
   albums in the research vehicles, Optibrand's vanished
   vendor database (317 + 159 trial animals imaged, zero
   surfaced), two lab-held bat wing photo sets (1,540 photos
   between them), Swindler's plaster drawers across four
   museums, and the purebred registries' books of record:
   six more archives that exist, matter, and are not files.

## Recommended score cuts (for the parent to apply)

| Niche | Score | Cut | Reason |
|---|---|---|---|
| dental-casts-mammal | 7 | **7 → 5** | Koala class: the collection premise is physical — plaster drawers whose only surface is a book; no digital surface at any era. |
| antler-tine-records | 7 | **7 → 6** | Flagship consolidated into a subscription platform; shed series are physical/project-held. Real records, zero hunter surface. |
| horn-annuli-age-records | 7 | **7 → 6** | Agency routine data is published as summary tables (inventory ceiling), and the validation comparison was already run by the field (2012, and Ram Mountain since 2004). |
| bat-wing-venation | 7 | **7 → 5** | Both real photo sets are lab-held with no file surface, and the headline comparison was already run twice by its own literature (2017, 2025). |
| livestock-iris-patterns | 7 | **7 → 5** | Premise falsified twice over: the trials were retinal, not iris, and the vendor database is gone; no trial image set ever surfaced. |
| ear-notch-punch-registries | 7 | **7 → 5** | The registry is paper by legal definition (book of record); the card itself named paper as the corpus — a file hunt was never available. |
| hyena-ear-notch-id | 7 | **7 → 6** | Ear albums are single-lab custody exactly as carded; the one public surface (behavioural CSVs) is a different data type from the quarry. |
| scar-based-photo-id | 7 | **7 → 6** | Every programme catalogue is custody or published-in-paper; the cross-species extraction has no stranded set to extract from, and the manatee arm was already mined as Campaign 8 gold. |

*Method notes (standing + this wave's corrections): Wayback
counts status-200-filtered before counting; every grade rests
on ≥1 sample download with size + md5 + magic in
`outputs/verify13-20261118-214423.json` / `verify13b`, except
where a host blocked or failed this client and the shortlist
says so (Swindler excerpt unreachable both schemes; UNK
magazine 403; Hokkaido-class search-indexed evidence used
only there). Corrections made mid-wave and recorded: the
PMC-instance Rice's-whale .xlsx URLs and the MDPI /pdf
endpoint returned HTML stubs — excluded as phantoms, and the
scar grade rests instead on the verbatim PLOS figure samples
fetched in verify13b; the RCS djvu-text URL likewise returned
HTML and is not counted as a text sample. The Holekamp zip's
Wayback capture (first captured 2026-09-21) is the same live
file, not a deleted set. README verified-results NOT updated
— no find in this wave meets the stranded bar those entries
set.*
