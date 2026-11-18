# Goldmine Hunter — Campaign 10 Shortlist (Broad Wave 2B, 2026-11-18)

*Ten unfired broad-registry 8/10s, seeds 11–20 of the
registry's 8-band. Method identical to Campaigns 6–9:
`campaign10_wave2b.py` live-crawled 26 surfaces and took
Wayback inventories filtered to statuscode:200 **before**
counting; `verify10.py` / `verify10b.py` / `verify10c.py`
then downloaded samples of every concrete pile (size + md5 +
magic in `outputs/verify10-*.json`, files in
`gold/campaign10-verify/`, 3.4 MB total). Grades per
`GRADES.md`; provenance classes never blurred. README
untouched — the GOLD below is flagged here for the lab's
call, as in Campaign 6.*

## Headline

**ONE GOLD. The Linguistic Atlas Project's full dialect
pile is stranded as loose files on its former host's site:
1,082 LAGS informant folders at lap.uga.edu, each with
topic-segmented interview MP3s beside the original
transcription file the atlas was built from — while every
formal product (the published atlas, the LDC DASS release,
DASS2019, the 2026 DASS2019_NLP cleaning) covers only a
64-informant sample of the 914 interviews.** Minted at
`~/workspace/lags-transcription-audit/` (NOVELTY.md +
PREREGISTRATION.md, comparison pre-registered before any
pile-wide run). Two SILVERs (Swiss glacier repeat photos;
Trümpy dye sample books), one SILVER-class shelf audit
(AIATSIS finding aids), and a seismogram system that turned
out to be a formal archive wearing a static site's clothes.

## Grades at a glance

| Niche (registry score) | Grade | One-line verdict |
|---|---|---|
| glacier-repeat-photos (8) | **SILVER** | Real repeat pairs verified on a living personal site + formal USGS/NSIDC collections — published by design |
| paper-seismograms (8) | **INVENTORY** | SISMOS/EuroSeismos is a formal archive; previews verified, hi-res registration-tiered; Romanian set a 9.4 GB formal deposit |
| moonwatch-satellite-cards (8) | **KILL** | ~400,000 observation cards are paper boxes in Smithsonian custody; only the finding aid + a published 1958 catalogue exist as files |
| steam-engine-indicator-cards (8) | **KILL** | Museum catalogue records for single objects; the one scan archive's "indicator cards" are orders for blank card stock |
| dye-sample-books (8) | **SILVER** | Trümpy: 17 volumes digitised + transcribed in ETH's own online catalog — published by design |
| endangered-language-tape-shelves (8) | **SILVER** | 1,384 status-200 AIATSIS finding-aid PDFs verified as the shelf list itself; the tapes are community-restricted custody |
| dialect-survey-recordings (8) | **🏆 GOLD** | Full LAGS pile stranded at lap.uga.edu; formal products cover 64 of 914 informants |
| commodity-price-currents (8) | **INVENTORY** | Real Prices Current pages verified — inside formal archive.org newspaper deposits, single issues, not port piles |
| fire-insurance-plans (8) | **INVENTORY** | Digitisation real (LAC/UCalgary inventories) but every sheet surface blocked this client; no sample obtained — stated plainly |
| photo-finish-film-strips (8) | **KILL** | No strip archive exists on the web; the one "Photo Finish" PDF is a school compilation of Wikipedia text |

---

## 1. glacier-repeat-photos — SILVER

`gletschervergleiche.ch` (SwissGlaciers.org) is a personal
site listing **61 glaciers (46 with comparisons displayed)**,
each a detail page of repeat pairs from the site's own
2005–present photography plus historic images. Crawl: 25
pages, 202 images. **Sample-verified REAL:** a comparison
JPEG (`Rhonegletscher_Stao01_2007_06.jpg`, 102,687 B,
md5 `1af6a2c1…`) and glacier thumbnails. The formal surfaces
are real too — USGS Repeat Photography Project (58 pairs,
18 glaciers; Grinnell repeat JPEG sample-verified, 115,675 B,
md5 `6ca1f472…`) and NSIDC's Glacier Photograph Collection
(45 repeat sets, order-mediated). Everything here is
**published by design**: the personal site is alive and was
updated Dec 2025/Jan 2026, and the collections are formal.
The niche card's comparison (measure today's terminus off
the photos against the published GLAMOS length series) is
genuinely un-run, but on published data that is the SILVER
definition. *Not gold because nothing is stranded or
deleted — the field's photo pairs live exactly where their
owners publish them.*

## 2. paper-seismograms — INVENTORY

The EuroSeismos static pages at `storing.ingv.it` look like
the classic loose pile — station pages (PRA alone carries
195 references, event lists back to 1905) — but the system
behind them is SISMOS, INGV's formal historical-seismogram
archive: 200-dpi previews are the free tier of a
registration service (`seismogramrequest.rm.ingv.it`;
600-dpi restricted to project members — **documented as
custody tiers, not circumvented**). The preview images
themselves live on `sismos.rm.ingv.it`, unreachable from
this client, and the Wayback Machine holds **zero** captures
of its `~hsds/JPG/` preview tree — the loose recovery route
is closed. What was verified: a real seismogram image from
the SISMOS surface via Wayback (crop of `DBN_E_1908122708361A`,
PNG, 101,251 B, md5 `018c3684…`); and the Romanian
EUROSEISMOS set as a formal Mendeley deposit — API-verified
as exactly two files, `EuroSeismos D1 D2 D3.zip`
(**9,424,531,553 B**) + `Readme.zip` (24,395,157 B; head
download PK-magic at the 6 MB cap), 431 seismograms per the
deposit record. *A formal archive with a free preview tier
is published-by-design infrastructure, not a stranded pile.*

## 3. moonwatch-satellite-cards — KILL (custody)

Smithsonian Archives Record Unit 255 is **24.0 cu ft of
paper** — station files, ~400,000 visual observations,
observer correspondence — in SIA custody. **Sample-verified:**
the collection's own finding aid (PDF, 199,370 B,
md5 `99013756…`), which is an inventory of boxes, not of
cards. The one Moonwatch data publication that exists as a
file is inside IGY Satellite Report No. 4 (NSIDC NOAA copy
sample-verified: PDF, 1,769,151 B, md5 `946c4ad3…`), whose
Moonwatch Catalogue prints 154 observations from 24 stations
for Mar–Apr 1958 — published by design in 1958, and a
catalogue excerpt, not the card population. The niche's
fidelity card is true (the cards are a real, uniform,
one-per-observation population) and the recovery premise is
false: the population sits in archival boxes. *The koala
class: score cut in calibration.*

## 4. steam-engine-indicator-cards — KILL

No measured card population has a web surface. The Science
Museum Group catalogue holds single objects (a 1919 Watt
indicator diagram; the page bot-walled this client at 403 —
catalogue metadata only, no sample claimed). The Holcroft
papers' eight bundles of steam-chest pressure cards are a
paper archive entry. The one digital scan archive probed,
Rolls-Royce's Experimental Archives, names "indicator cards"
in Box 52 — and its own text shows they are **orders and
instrument lists for blank card stock** ("Indicator Cards.
Engine Indicator Diagram Cards. Sample enclosed."), not
measured diagrams; its record pages serve no scan images to
this client (Blazor app; only the site logo was retrievable,
recorded as furniture, not evidence). The Smithsonian's
Lippincott indicator ships "record cards in box" — with the
instrument, in a museum. *Cards survive as objects and
bundles, never as a file population.*

## 5. dye-sample-books — SILVER

ETH Zürich's Trümpy catalog is the niche's best object and
it is **published by design**: 17 Jenny-Trümpy fabric sample
books (Glarus, 19th c.) digitised **and transcribed** in a
purpose-built online catalog at
`truempy-druckmuster.ethz.ch` (17 volume routes counted;
volume page image sample-verified REAL, PNG 88,095 B,
md5 `6a6a412d…`; ETH's e-heritage article documents the
project). Yale's Koechlin & Frères books (2 vols, several
thousand swatches with recipes) are a catalogue record only
— reading-room custody; the Crutchley dyers' archive is
mid-digitisation by announcement. The headline comparison
(recipe-named dye vs measured dye identity) remains un-run,
but the sample books it would run on are a university's own
publication — SILVER, same class as Juneau's editions.

## 6. endangered-language-tape-shelves — SILVER

The niche's unit is the shelf list itself, and the shelf
lists are verified at scale: the Wayback CDX holds **1,384
status-200 PDFs** under AIATSIS's `catalogue_resources/`
directory (1,654 collapsed captures), each a collection
finding aid itemising field tapes by speaker, language,
place, date and tape number. **Sample-verified REAL via
Wayback** (the live host breaks this client's downloads):
Hercus L09 finding aid (PDF, 139,458 B, md5 `9563d368…`)
and Breen G11 (PDF, 201,611 B, md5 `634c638f…`). The tapes
themselves are custody in the strict sense — AIATSIS
restricts copying by community and depositor permission,
and digitised audio routes through PARADISEC's formal
catalog; **nothing restricted was requested or scraped**.
The un-run comparison (box-label language names vs the
modern classification, cross-checked where PARADISEC holds
the digitised tape) runs on the published finding aids —
SILVER, the Barts class: the register is the data, and the
register is published by design. Alaska's ANLA contributed
a cautionary PHANTOM (its crawl "data files" were
search-interface XML), recorded so the count is never
quoted as data.

## 7. dialect-survey-recordings — 🏆 GOLD

**The pile.** `lap.uga.edu/Projects/` — the Linguistic
Atlas Project's Data Download Center tree on the site of
its pre-2018 host institution: 23 project folders of raw
directory listings (LAGS, LAMSAS, LANCS, DASS, DASS2019,
SED, Gullah, Roswell…). Inside LAGS: **1,082 informant
folders** counted from the live Speakers index. Each folder
holds the informant's transcription as .xml and .xls/.xlsx,
a biography .txt, and an Audio/ tree — tape folders of
topic-segmented MP3s ("01 Wild Animals", "02 Food and
Cooking"…) with a per-tape meta.txt.

**Sample-verified REAL (verify10):** INF001 spreadsheet
(xlsx, 23,059 B, md5 `01e1b2b8…`), INF001 transcription XML
(43,293 B, md5 `817b0120…`), INF001 tape-1 segment-01 MP3
(ID3 magic, 4,063,232 B at cap, md5 `9b79ede6…`), tape
meta.txt (1,250 B, md5 `8cd21fbb…`), DASS2019 full-corpus
text (2,006 lines in the first 200 KB), and a bonus pile in
the same tree — LAP-hosted Survey of English Dialects
response datasets (kindling/parlor CSVs, sample REAL,
8,061 B, md5 `aa8fc052…`).

**Why gold, under the doctrine.** (1) *Comparable set:*
914 LAGS interviews (1968–83, one protocol, one
questionnaire), each unit carrying audio + transcription +
biography in the same folder shape. (2) *Stranded:* the
full file set lives only as loose files on the former
host's site; the project moved to Kentucky in 2018 and its
successor pages describe the transfer as still in progress
with a website "forthcoming" — no formal archive holds the
full pile. (3) *The formal products cover a sample, not
the pile:* the published LAGS atlas prints responses
without auditing them; DASS (LDC) and DASS2019 cover **64
informants**; the 2026 DASS2019_NLP paper cleaned those
same 64 and fine-tuned ASR on them. (4) *Un-run
comparison:* no treatment found audits the remaining ~850
informants' transcriptions against their surviving audio.
(5) *Anchor:* DASS2019's manual time-aligned transcriptions
calibrate the ruler before it touches the pile.

**Caveats, plainly.** The site is live and was a deliberate
public distribution in its day — this is the Fonozoo shape
(a project's own site, no formal archive), not a deleted
one; Wayback coverage of the audio tree is thin (6 MP3
captures), so every count above is a live-index count,
taken 2026-11-18. The novelty survives only in full-pile
form (see the mint's NOVELTY.md). **Minted:**
`~/workspace/lags-transcription-audit/` — NOVELTY.md +
PREREGISTRATION.md (denominator, ruler discipline —
general ASR, never the DASS-fine-tuned models — and four
registered predictions, fixed before any pile-wide run).

## 8. commodity-price-currents — INVENTORY

Real Prices Current pages exist and were **sample-verified
REAL** — but inside formal newspaper deposits: the Toronto
Trade Circular and Prices Current (archive.org PDF,
238,529 B, md5 `c6557693…`; its djvu text head shows the
prices-current matter) and the British Packet and Argentine
News of 4 Oct 1845, whose "PRICES CURRENT" section covers
hides, tallow, salted beef, jerked beef and horns (text
PDF sample-verified, 1,645,069 B, md5 `ebfd02f6…`). These
are single issues in the Internet Archive / British
Newspaper Archive system — published by design, and one
issue is not a series. No loose port-city pile (the
weekly, multi-year, one-port stack the niche card needs)
surfaced at any host probed. *The unit survives; the
comparable set does not, outside paywalled newspaper
corpora (custody, noted, not scraped).*

## 9. fire-insurance-plans — INVENTORY (surface documented, no sample)

Digitisation is real and extensive on paper: Library and
Archives Canada records show whole Goad volumes digitised
(64–81 digital objects per volume in the catalogue text),
and UCalgary's inventory libguide (fetched live, 200)
marks the 1908–10 Calgary sets digitised and downloadable,
1911–14 available via LAC, 1927–41 partial — under a stated
90-year copyright restriction. **But no sheet image could
be sampled from this client:** the LAC record host returned
nothing, its central image host timed out, and UCalgary's
digital-collections asset pages returned 403. Under the
standing evidence rule an unsampled surface cannot grade
SILVER, so this is INVENTORY claimed only as a documented
surface — the same treatment as Campaign 8's Utah surface.
The deeper custody finding stands regardless: the
authoritative *Catalogue of Canadian Fire Insurance Plans
1875–1975* is itself undigitised, and post-1917 plans are
withheld at LAC. A browser-equipped pass could likely
upgrade this; the grade records what was verified, not
what is plausible.

## 10. photo-finish-film-strips — KILL

No film-strip archive exists on the web at any host probed.
The one file literally named for the niche — a Weebly
"Photo Finish" PDF — was **sample-verified REAL as a file**
(51,886 B, md5 `0475c282…`) and is a school compilation of
Wikipedia text about photo finishes, not strips. The 1932
Kirby-camera finish (Tolan/Metcalfe, decided by 0.005 s)
survives as secondary accounts and press stills; the
Substack article's images are CDN press photos (this
client's sample of its first image returned the site's
touch icon — recorded as furniture). The strips themselves
are timing-federation / Omega custody with no public file
surface found. *A niche whose entire web presence is
writing about the objects is a kill, however good the
objects would be.*

---

## Ranking (for the next waves)

1. **dialect-survey-recordings — GOLD, minted.** The run
   (completeness census first, per the pre-registration)
   is the follow-up, not another hunt.
2. **endangered-language-tape-shelves — SILVER with a live
   seam:** the finding-aid census (1,384 PDFs) is itself a
   countable, un-run comparison surface.
3. **glacier-repeat-photos — SILVER:** the terminus-vs-
   GLAMOS comparison is a clean small paper on published
   data if the lab wants it.
4. **dye-sample-books — SILVER:** recipe-vs-measured-dye
   needs lab access, not more hunting.
5. Everything else is closed: seismograms (formal archive),
   moonwatch + steam cards (paper custody), price currents
   (formal deposits), fire plans (documented, unsampled,
   browser-pass candidate), photo-finish (no surface).

## What we did NOT do

- No bulk pulls: total new disk **3.4 MB** of samples. The
  9.4 GB Mendeley zip was inventoried via its API, never
  downloaded; LAP audio was sampled at one segment of one
  informant, not harvested — the pile-wide run waits for
  its own commission under the pre-registration.
- Registration and permission systems (SISMOS 600-dpi tier,
  AIATSIS community-restricted copying, PARADISEC access
  conditions, newspaper corpora) were documented as
  custody, never scraped or circumvented.
- Bot-walled surfaces (Science Museum Group 403, LAC
  timeouts, UCalgary 403) are reported as this client's
  results, not as absences.
- README not edited; the GOLD is flagged here and minted
  in its own project directory.
