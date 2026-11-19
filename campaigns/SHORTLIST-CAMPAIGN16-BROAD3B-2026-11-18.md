# Goldmine Hunter — Campaign 16 Shortlist (Broad Wave 3B, 2026-11-18)

*Nine unfired broad-registry niches, ranks 37–45 in registry
order (seven 7s, two 6s), GENERATED from `niches.json` — no
hand-picking. Method identical to Campaigns 6–10:
`campaign16_broad3b.py` live-crawled 28 surfaces and took
Wayback inventories filtered to statuscode:200 **before**
counting (one documented exception: the Mount Wilson FTP
drawing tree, whose captures carry statuscode **226** — see
§9); `verify16.py` / `verify16b.py` / `verify16c.py` /
`verify16d.py` then downloaded samples of every concrete pile
(size + md5 + magic in `outputs/verify16*.json`, files in
`gold/campaign16-verify/`, 26 MB total). Grades per
`GRADES.md`; custody classes per Custody Mapper, assigned
from probe evidence (post-probe gate). README and registries
untouched.*

## Headline

**NO GOLD.** One small SILVER (UNLV's regional menu
collection), six INVENTORY, two KILL. The 7-band behaved
exactly as the calibration laws predict: every niche in this
wave has already acquired its infrastructure — a formal
repository dataset (British Library playbills), a national
survey database (BGS/USGS boreholes), an observatory archive
(KSO/Mount Wilson drawings), a university digital collection
(UNLV menus, Clowes reports, USDA seed catalogues) — or its
population never became files at all (municipal concrete
ledgers, factory wage books). No loose working pile on an
unadopted site surfaced at any of the 28 surfaces probed.

**Factory-payroll prior test: CONFIRMED.** The research-tools
CUSTODY-1 campaign KILLed `factory-payroll-wage-books`
prospectively from its fidelity card (CUSTODY_RESTRICTED cue).
The probe evidence confirms it at every host: wages books are
physical volumes in record offices (JCU Pioneer PMR/WB/1–13,
Derbyshire D6948/E/9/4), and the one digitisation-adjacent
surface (Fulton Bag) holds its ~50,000 personnel cards under
an explicit confidentiality restriction. The prior stands —
and it was a card-text prior, so this wave is its first
probe-level confirmation.

## Grades at a glance

| Niche (registry score) | Hosts probed | Verified files | Custody class (post-probe) | Grade | One-line evidence |
|---|---|---|---|---|---|
| concrete-test-ledgers (7) | Datadory/UCI, archive.org | UCI zip REAL (34,444 B); journal PDF REAL at cap | FORMAL_OR_PLATFORM → CAUTION | **KILL** | No municipal lab ledger has a web surface anywhere probed; the only dataset is UCI's published 1,030-record lab compilation |
| pigment-cross-sections (7) | ICCROM/OPD, Clowes, Rijksmuseum PSA, Tate CHSA | 3 Clowes technical-report PDFs REAL (cross-sections inside) | CUSTODY_RESTRICTED → KILL (archives); Clowes published | **INVENTORY** | The big section archives are request/in-person custody (OPD 15,400; Tate 16,000+); the verified files are a published catalogue's reports |
| playbill-programme-archives (7) | BL Research Repository, blplaybills.org, archive.org, BL libguide | **0 samples obtained** (see §3) | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** (documented, unsampled) | BL's 264-volume OCR dataset is a formal DOI deposit (87.68 MB zip, documented live); every download route was JS-gated, 404, or access-restricted for this client |
| factory-payroll-wage-books (7) | JCU Pioneer, Derbyshire RO, Georgia Tech/Fulton | JCU series-listing PDF REAL (86,802 B) — a finding aid, not wage data | CUSTODY_RESTRICTED → KILL | **KILL** | Wages books are physical volumes in record offices; Fulton personnel cards are confidentiality-restricted. **CUSTODY-1 prior CONFIRMED** |
| booth-level-election-gazettes (7) | archive.org (Karnataka, Himachal, Gazette of India) | 3 gazette PDFs REAL | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | Gazette PDFs verify, but the booth-level content is voter allotments and election petitions with constituency totals — no booth-return pile |
| seed-catalogue-varieties (7) | NYBG Mertz, archive.org USDA Gilbert (×2) | 2 catalogue PDFs REAL at cap | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | Single issues verify inside a formal collection; the variety-level unit was not verified at pile level |
| regional-menu-collections (7) | UNLV Bohn-Bettoni, UNLV finding aid, NYPL/curatingmenus | UNLV menu TIFF REAL via Wayback (3,014,656 B at cap) + 147 status-200 TIFF captures | FORMAL_OR_PLATFORM → CAUTION | **SILVER (small)** | A regional menu collection (~2,000 menus, 1870–1930) digitised and published by design, dated dish/price units intact — the card's target shape, at silver ceiling |
| borehole-well-logs (6) | USGS Geolog, WA Geologic Portal, BGS AGS | BGS OGC API GeoJSON sample saved (75,134 AGS boreholes matched) | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | Every surface is a formal survey database/API; the niche is infrastructure-complete |
| sunspot-drawings (6) | MWO (mtwilson.edu), UCLA obs/howard, Carnegie, KSO CESAR | MWO drawing JPEG REAL via Wayback (157,839 B); KSO .dat REAL (1,459 B) | FORMAL_OR_PLATFORM → CAUTION | **INVENTORY** | Drawings verify at three surfaces, all formally digitised/published; the howard FTP tree is a deleted mirror of the same MWO set. **Drawings angle only — SILSO v1 not re-hunted** |

---

## 1. concrete-test-ledgers — KILL

No municipal or university materials-lab ledger pile exists
on the web at any host probed. What the niche's keywords
actually return is (a) the UCI Concrete Compressive Strength
dataset — **sample-verified REAL** (zip, 34,444 B, md5
`eba3e289…`, 1,030 laboratory mix records compiled by
Prof. I-Cheng Yeh, Chung-Hua University, donated 2007,
published by design in a machine-learning repository — a
university lab compilation, not a municipal ledger, and
already one of the most re-used datasets in its field); and
(b) published journal test tables (the October 1930
*Concrete* journal issue, PDF verified REAL at the 6 MB cap,
md5-head `6408755c…`). The card's population — city lab
crushing ledgers, one test per structure — remains exactly
where the card left it: on shelves, unscanned as data.
*The koala class: a perfect fidelity card whose population
never became files.*

## 2. pigment-cross-sections — INVENTORY

The verified files are real and good: three Clowes
Collection technical-examination reports, **sample-verified
REAL PDFs** — `c10042a-d.pdf` (18,824,836 B, md5
`40df21f5…`), `c10057.pdf` (3,362,589 B, md5 `e7fd1600…`),
`c10028.pdf` (2,868,690 B, md5 `b4a95bc8…`) — each carrying
cross-section photomicrographs with SEM-EDS/Raman pigment
identifications, published by design in a digital catalogue.
But the niche's populations are custody: OPD's 15,400 cross-
and thin-sections (ICCROM registry entry verified live) are
partly not digital and access is **on request**; Tate's CHSA
holds 16,000+ cross-sections with access by request system
and in-person visits; the Rijksmuseum Paint Sample Database
is a login-gated interface (HEAD 200, a 1,372 B HTML shell —
no file pile). *Case-study publications verify; the
per-lab populations the card imagines comparing sit behind
request desks.*

## 3. playbill-programme-archives — INVENTORY (documented, unsampled)

The flagship is a formal deposit and it is documented live:
the British Library Research Repository's *Theatrical
playbills from Britain and Ireland (OCR text only)* —
`playbills-ocr-text.zip`, **87.68 MB**, 264 volumes,
1660–1902, DOI `10.21250/pb2`, checksum published on the
record page (fetched 200). **No sample could be obtained
from this client, stated plainly:** the repository product
page is a JS app whose crawl "data files" are 249 i18n
`.label` phantoms; its Samvera concern page exposes no
static download href; the DOI resolved 404 for this client;
Sceneweb's playbill downloads are JS-served; and the one
archive.org playbill item (Plymouth Theatre, *The Happy
Time*, 1951; 16 files incl. a 6,842,856 B PDF and a
23,013,718 B JP2 zip) is an **access-restricted**
patron-library item whose downloads returned 172 B HTML
stubs. Under the standing evidence rule an unsampled surface
cannot grade SILVER — this is the Campaign 10 fire-insurance
treatment. A browser-equipped pass at the BL repository
would very likely upgrade this to SILVER (the dataset is a
published register-as-data stack); the grade records what
was verified. The undigitised remainder of the BL collection
is microfilm (libguide, verified live).

## 4. factory-payroll-wage-books — KILL (CUSTODY-1 prior CONFIRMED)

Three hosts, one shape. **JCU Pioneer Sugar Mill:** the
archive page (200) lists Wages Books PMR/WB/1–13 (1915–1965)
and Drysdale wages books 1923–1938 under a stated *Archive
Location*; its only PDFs are series listings —
**sample-verified REAL** (`Pioneer CT 1883 to 1906.pdf`,
86,802 B, md5 `a26a3a4f…`), i.e. a finding aid for physical
volumes. (The whole-domain Wayback count of 877 status-200
files for libserver.jcu.edu.au is domain noise — 662 in an
unrelated Stations archive, the rest library tutorials —
and is **not** quoted as payroll data.) **Derbyshire Record
Office:** the Strutt mill hands' weekly wages book
1895–1897 is a catalogue record for *1 outsize volume*,
manuscript (catalogue text search-verified; the CalmView
host timed out for this client). **Fulton Bag (Georgia
Tech):** payroll records sit in 257 archival volumes, and
the ~50,000 personnel cards are explicitly *restricted so
as to maintain confidentiality* (page text verified live).
The CUSTODY-1 prospective KILL — assigned from card text
alone — is confirmed by probe evidence at every host.
*Never circumvented: the restriction is the finding.*

## 5. booth-level-election-gazettes — INVENTORY

Gazette PDFs verify cleanly inside formal archive.org
deposits — **all REAL**: Mysore Gazette (July–Dec 1948
volume text PDF, 210,565 B, md5 `e7d020c0…`), Himachal
Pradesh Gazette 1986-09-13 (2,152,131 B, md5 `e8623ec2…`),
Gazette of India 1953 (1,284,429 B, md5 `6ba82513…`, saved).
But reading them kills the pile premise: the Mysore booth
content is a *statement of polling stations, booths and
voters allotted to each booth* — allotments, not returns;
the Himachal and 1953 items are election-petition judgments
carrying constituency-level totals. The booth-level return
(the card's unit: votes per booth, summed against the
declared total) does not appear as an extractable series in
the gazette surfaces probed. *The container is real and
formal; the unit inside it is a different document than the
card imagines.*

## 6. seed-catalogue-varieties — INVENTORY

Two USDA Henry G. Gilbert collection catalogues on
archive.org **verify REAL** (PDF magic at the 6 MB cap):
the 1926 Northern Seed & Nursery Co. catalogue (md5-head
`2923c1a2…`) and the 1906 Nebraska Seed Co. catalogue
(md5-head `ee69933e…`). The formal frame is large — NYBG's
Mertz Library reports 58,000 nursery/seed items catalogued
and 1,400 pre-1923 catalogues digitised; archive.org's
advancedsearch returned numFound 93,315 for the USDA
collection query (as returned; not relied on for grading).
This is silver-*shaped* — an annual, comparable, price-
bearing stack, published by design — but it is graded
INVENTORY on the evidence bound: the verified samples are
single issues, and the variety-level unit (the card's
census) was not verified at pile level. A pile-level pass
over one firm's multi-decade run could upgrade it.

## 7. regional-menu-collections — SILVER (small)

The card said the famous collection is one city and regional
libraries hold the rest — and the regional collection
verifies. UNLV's Bohn-Bettoni *Menus: The Art of Dining*
digital project (~2,000 menus, 1870–1930, drawn from the
12.68 cu ft MS-00793 physical collection) serves each menu
as a full TIFF with dated dish/price content. The live host
breaks this client's downloads, so verification ran through
Wayback, as with AIATSIS in Campaign 10: **147 collapsed
`men000*.tif` captures, all status-200**, and a
**sample-verified REAL TIFF** (`men000017.tif`, 3,014,656 B
at cap, TIFF magic `49492a00`, md5-head `7e71ee15…`). The
flagship NYPL export is documented (four-table CSV export,
~17,547 digitised menus, 1.3 M dish records) but its
`menus.nypl.org/data` page now returns 404 and the
curatingmenus.org dictionary CSV hrefs are 379 B HTML
phantoms — recorded, not quoted. Everything verified is
**published by design**, and the card's comparison (menu
price vs same-week newspaper advertisements) is un-run on
it — SILVER, the Juneau/Trümpy class, at small scale.

## 8. borehole-well-logs — INVENTORY

The niche is infrastructure-complete. BGS's AGS borehole
index answers through its OGC API — **verified live**:
`numberMatched` **75,134** boreholes; a 5-feature GeoJSON
sample is saved (`gold/campaign16-verify/bgs-ags-api-sample.geojson`,
canonical md5 `ad08b637…`), and each feature carries its own
`ags_log_url` — the formal service *is* the log archive.
USGS's Geolog Locator (page verified live) holds 7,000+
digital borehole geophysical logs at 1,700+ locations in
LAS/PDF/original formats behind its search interface;
Washington's portal holds its subsurface database the same
way. State and national surveys each host their logs —
inside their own databases, published by design, with no
loose scan pile stranded outside them. *A known resource
class, fully platformed: the card's own score note said the
headline was weaker; the probe says the surface is closed.*

## 9. sunspot-drawings — INVENTORY (drawings angle only)

*Scope note, as instructed: this niche is the observatory
drawing piles. The SILSO sunspot-number version stack was
hunted in Campaigns 2–3 and not found by any tried route;
it is not re-hunted here.*

Drawings verify at three surfaces. **Mount Wilson:** the
old UCLA distribution tree (`ftp://howard.astro.ucla.edu/pub/obs/drawings/`)
is dead as a live host (timeouts for this client), but
Wayback holds **≥10,000 collapsed captures of it (the CDX
cap), every one statuscode 226** — the FTP transfer-complete
code, which is why the standing statuscode:200 filter
reported zero in the main probe; the exception is recorded
here rather than silently re-filtered. Per-year counts run
~150–316 drawings (1917: 310, 1918: 287, 1919: 316).
**Sample-verified REAL:** the 4 January 1917 drawing —
the first of the series — JPEG, 157,839 B, md5 `08f7c54d…`.
**KSO Kanzelhöhe:** the CESAR archive is live and complete
by design — the `automatic/1999/` directory alone lists
2,597 files (per-observation `.dat` / `.jpg` / `.spot` /
`_draw.png` sets); **sample-verified REAL** `.dat`
(1,459 B, md5 `e990a127…`); CESAR CDX 82/84 status-200.
**Why not gold:** the MWO set the FTP tree mirrored is the
same set formally digitised and published by Pevtsov et al.
2019 (extracted magnetic data at CDS; scanned images under
DOI 10.25668/7gvh-sh82), MWO's daily archive is served from
mtwilson.edu, and KSO's drawings feed its own published
position catalogues (1944–2016, with extension papers
through 2025). The recount-the-drawings comparison is the
field's own core programme (Schwabe, Spörer, Koyama and KSO
recounts all published). *A deleted mirror of a published
set is a recovery of nothing — INVENTORY, with the 226
quirk kept as the wave's one genuinely new provenance note.*

---

## Ranking (for the next waves)

1. **regional-menu-collections — SILVER (small).** Closed
   as a hunt; the UNLV pile is a usable published dataset
   if the lab ever wants the menu-vs-newspaper price check.
2. **playbill-programme-archives — INVENTORY, unsampled.**
   The one live seam in the wave: a browser-equipped pass
   at the BL Research Repository download would settle
   SILVER vs INVENTORY in one sample.
3. **seed-catalogue-varieties — INVENTORY, silver-shaped.**
   A pile-level pass over one firm's run is the upgrade
   test; not worth a wave of its own.
4. Everything else is closed: concrete ledgers and factory
   wage books (populations never became files — both are
   digitisation targets for an institutions campaign, not
   a crawler), pigment sections (request custody), election
   gazettes (formal deposits, wrong document inside),
   boreholes (formal databases), sunspot drawings (formal
   observatory archives; deleted mirror of a published set).

## Score cuts recommended (registry edits are the parent's)

| Niche | Cut | Reason |
|---|---|---|
| concrete-test-ledgers | 7 → 5 | Population never became files at any host; only a published ML dataset exists (koala class) |
| pigment-cross-sections | 7 → 6 | Populations are request/in-person custody; only published catalogue subsets are files |
| playbill-programme-archives | 7 → 6 | Flagship is a formal DOI dataset — silver ceiling; long tail is microfilm |
| factory-payroll-wage-books | 7 → 5 | Probe confirms the CUSTODY-1 kill at every host: record-office paper + a structural privacy restriction |
| booth-level-election-gazettes | 7 → 6 | Gazettes are formal deposits and the booth content is allotments/petitions, not returns |
| seed-catalogue-varieties | 7 → 6 | Formal collection, silver ceiling at best; variety unit unverified at pile level |
| regional-menu-collections | 7 → 6 | Material exactly as carded, strandedness zero — published by design (Juneau pattern) |
| borehole-well-logs | 6 → 5 | Every surface is a formal survey database/API; infrastructure-complete |
| sunspot-drawings | 6 → 5 | Both flagship observatories formally digitised; recounts are the field's own programme |

## Pair Hunter flags (honest, weak)

- **BL playbill OCR (264 vols; theatre + date keys) vs
  next-day press reviews** — the card's second ruler, and
  the OCR/image datasets (pb2/pb1) have never been
  coverage-audited against each other. Low priority: both
  sides are published, and the OCR side is unsampled here.
- **KSO drawing-derived positions (`.dat`/`.spot`, date-time
  keys) vs the Debrecen Photoheliographic Data catalogue** —
  mostly *already joined* by KSO's own catalogue programme,
  so this is a largely-run pair, flagged only so nobody
  re-pitches it as fresh.
- No other surface in this wave offers independent rulers:
  the BGS AGS logs and BGS coded geology share one
  custodian; the gazette allotments have no return series
  to pair against.

## What we did NOT do

- No bulk pulls: total new disk **26 MB** of samples (three
  Clowes report PDFs are most of it). The BL playbill zip
  (87.68 MB) was inventoried from its record page, never
  downloaded; UNLV TIFFs and MWO drawings were sampled at
  one file each, not harvested.
- Restricted systems were documented, never circumvented:
  OPD/Tate request access, Rijksmuseum PSA login, Fulton
  Bag's confidentiality-restricted personnel cards, and the
  access-restricted archive.org playbill item.
- Surfaces this client could not reach (UNLV live host,
  UCLA obs/howard live, Derbyshire CalmView timeout,
  menus.nypl.org/data 404, BL DOI 404) are reported as this
  client's results, not as absences; where Wayback could
  verify the same files (UNLV, MWO), it did.
- README and registries not edited; no git commit. The
  score cuts above are recommendations for the parent.
