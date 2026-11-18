#!/usr/bin/env python3
"""Build niches.json + NICHES-50.md — the niche-keyword registry
(Atharva, 2026-11-18: ~50 niche domain keywords with gold potential,
headline-shaped like mammals; campaigns are GENERATED from this
registry, not hand-picked).

Every entry passed three tests on paper before scoring:
 (a) FIDELITY — raw capture kept, one protocol over dozens+ comparable
     units, labels gapped/stranded/on a second ruler, a local anchor;
 (b) HEADLINE — a non-specialist gets the comparison in one sentence;
 (c) FRAGMENTATION — NOT a mature field whose central product is
     already reconciliation (those publish by design: CRU / Reptile /
     ATNF, Campaign 5).
Excluded: everything already hunted, landed or killed in Campaigns
1-5 and the fidelity campaign (Brain Catalogue, rhino, Maddison, CRU,
Gaia/GALAH, cryo-EM, cosmology, HCA, WorldClim, SILSO, SDSS, and the
Campaign 2-5 host lists).
"""
import json

# slug, name, family, score, score_why, keywords, exts, gold_words,
# RAW, UNIT, LABEL_GAP, ANCHOR, headline, why_niche
N = []
def add(*a): N.append(a)

# ---------- Family A: Animal bodies & senses — beyond brains ----------
add("fish-otoliths","Fish otolith (ear-stone) image & chemistry archives","A. Animal bodies & senses",9,
 "Raw images + chemistry, dozens of lab collections, reader-vs-reader age gap, known-age anchors exist.",
 ["otolith image archive jpg","sagitta otolith database download","otolith age reading csv xls","otolith microchemistry transect data"],
 [".jpg",".tif",".csv",".xls"], ["otolith","sagitta","annuli","microchem"],
 "High-resolution otolith photographs and LA-ICP-MS / isotope transect files on lab and institute sites",
 "One fish specimen — hundreds per collection, dozens of species, same imaging protocol",
 "Age read by reader A vs reader B vs chemistry; usually only published means survive",
 "Known-age hatchery fish and bomb-radiocarbon validated ages",
 "A stone inside a fish's head has recorded every winter of its life — and two experts reading it can disagree by years.",
 "Age labs keep their own image piles; there is no central reconciliation product, only per-lab atlases (AFORO, national collections) that never joined each other's readings.")
add("electric-fish-eod","Weakly electric fish EOD waveform recordings","A. Animal bodies & senses",9,
 "Raw .wav is the specimen; species-specific signal; taxonomy rewritten by DNA after recordings were filed by ear.",
 ["electric organ discharge wav download","mormyrid EOD recordings archive","gymnotiform EOD waveform data","electric fish finder mp3 recordings"],
 [".wav",".mp3",".csv"], ["eod","discharge","waveform","mormyrid","gymnotiform"],
 "Uncompressed .wav/.mp3 electric-organ-discharge recordings with oscillogram exports, on lab and personal research sites",
 "One recorded fish — hundreds of individuals, dozens of species per expedition, one electrode protocol",
 "Species named by waveform at capture vs later DNA-barcode revisions of the same vouchers",
 "Museum voucher specimens tied to recording numbers",
 "A fish that 'sees' with electricity broadcasts its own name in a waveform — and the recordings were filed under names DNA later changed.",
 "A handful of labs (Cornell mormyrids, Crampton's gymnotiforms) hold expedition piles on their own sites; no cross-lab EOD library exists.")
add("cephalopod-beaks","Cephalopod beak collections from predator stomachs","A. Animal bodies & senses",8,
 "Beaks are the only hard part that survives digestion; measurement piles sit in marine-lab theses and supplements.",
 ["cephalopod beak measurements csv","squid beak identification guide pdf","octopus beak morphometrics data","beak collection stomach contents database"],
 [".csv",".xls",".jpg"], ["beak","rostral","cephalopod","morphometr"],
 "Beak photographs and rostral-length measurement tables from whale, seal and albatross stomach-content studies",
 "One beak — thousands per predator-sampling programme, dozens of prey species, one measuring key",
 "Prey species ID from beak keys vs DNA metabarcoding of the same stomachs (second ruler)",
 "Whole-specimen beak-to-body regressions from museum material",
 "The only part of a giant squid that survives a whale's stomach is its beak — and the beak remembers how big the squid was.",
 "Stomach-content programmes publish summary diet percentages; the beak-by-beak measurement piles stay on lab sites and in thesis appendices.")
add("bivalve-shell-rings","Bivalve shell growth-ring (sclerochronology) image archives","A. Animal bodies & senses",8,
 "Cross-section images are raw chronologies; each lab reads its own shells; isotope profiles are an independent ruler.",
 ["sclerochronology shell image archive","clam shell growth increments data","bivalve cross section photograph collection","shell ring chronology csv"],
 [".jpg",".tif",".csv"], ["sclerochron","increment","shell","chronology"],
 "Shell cross-section / acetate-peel images and increment-width measurement files on sclerochronology lab sites",
 "One shell — hundreds per site chronology, same sectioning and imaging protocol",
 "Ring-count ages vs oxygen-isotope years measured on the same shell (second ruler)",
 "Known-collection-date shells and crossdated master chronologies",
 "A clam on the seafloor has been keeping a yearly diary in its shell longer than most countries have existed.",
 "Sclerochronology is a small community of labs with personal chronology pages; the image archives behind the published chronologies were never pooled.")
add("bat-echolocation-libraries","Regional bat echolocation call libraries","A. Animal bodies & senses",7,
 "Raw full-spectrum calls are re-identifiable forever; regional libraries were built before the big platforms and never merged.",
 ["bat call library wav download","echolocation call reference collection zip","bat detector recordings species csv","full spectrum bat calls archive"],
 [".wav",".csv",".zip"], ["echolocation","call","pipistrelle","myotis"],
 "Full-spectrum .wav call files with detector metadata, on regional bat-group and university lab sites",
 "One call sequence — thousands per regional library, dozens of species, similar detector protocols",
 "Species ID by call analyst vs DNA / roost-emergence identification of the same bats (second ruler)",
 "Hand-released known-species reference calls",
 "A bat shouts its name in ultrasound every night — but half the regional call libraries call the same shout by different species.",
 "National platforms exist, but the older regional .wav piles (bat groups, consultancies, theses) predate them and were never ingested or re-checked.")

# ---------- Family B: Birds, fish, reptiles, amphibians, insects ----------
add("frog-call-archives","Frog & toad call archives (regional fonotecas)","B. Other taxa",9,
 "The task's own example: raw .wav/.mp3 per species, regional sound libraries, call IDs vs DNA-split species.",
 ["frog call archive wav","anuran calls download mp3","fonoteca frog recordings catalogue","toad advertisement call recordings site"],
 [".wav",".mp3",".csv"], ["call","anuran","frog","fonoteca","advertisement"],
 "Original .wav/.mp3 advertisement-call recordings with accession numbers, on regional fonoteca and lab sites",
 "One calling male — thousands of accessions per fonoteca, hundreds of species, standard field-recorder protocol",
 "Call filed under the species name at recording vs the DNA-split taxonomy of today (second ruler)",
 "Voucher specimens and type-locality recordings",
 "A frog smaller than your thumbnail has a unique voice — and thousands of taped voices are filed under species that have since been split in three.",
 "Fonoteca Zoológica (Madrid), Fonoteca Neotropical and university piles each hold their own accessions; the big platforms host photos, not these accessioned raw calls.")
add("salmon-scale-archives","Salmon & fish scale image archives","B. Other taxa",9,
 "A century of scale envelopes; images are raw growth records; reader ages vs known-tag fish is a clean two-rulers setup.",
 ["salmon scale image archive","fish scale samples collection envelopes","scale reading age data xls","historic scale collection digitised images"],
 [".jpg",".tif",".xls",".csv"], ["scale","circuli","age","smolt"],
 "Scale images (slides / scans) plus envelope metadata, held by fisheries labs, rivers trusts and agency image labs",
 "One scale — thousands per river system per decade, one mounting and imaging protocol per lab",
 "Age read from the scale vs known age of PIT-tagged / coded-wire-tagged fish (second ruler)",
 "Tag-recovery fish of exactly known age",
 "A salmon carries its whole childhood — river years and ocean years — written in rings on a scale the size of a fingernail.",
 "Every fisheries lab keeps its own scale library; the 2025 known-age validation set (254 fish) showed how rarely the big archives are ever checked against truth.")
add("bird-egg-collections","Bird egg & clutch collections (oology)","B. Other taxa",8,
 "Egg photos + measurements per clutch; shell thickness is a pollution archive; collector registers vs digitised labels disagree.",
 ["bird egg collection database photographs","oology clutch measurements csv","eggshell thickness data archive","museum egg collection catalogue download"],
 [".jpg",".csv",".xls"], ["egg","clutch","shell","oology"],
 "Clutch photographs, egg measurements and shell-thickness readings on museum and university collection sites",
 "One clutch — tens of thousands across collections, same measurement conventions since the 1800s",
 "Collector's handwritten register vs the museum's digitised label (second ruler, often conflicting)",
 "Ratcliffe shell-thickness index and dated pre/post-DDT reference series",
 "An egg collected in 1890 still remembers the air of 1890 — its shell got measurably thinner when DDT arrived.",
 "Egg collections were scattered when oology fell from fashion; small museums digitised their own drawers and nobody has joined the thickness series across them.")
add("butterfly-wing-drawers","Butterfly & moth specimen drawer imaging","B. Other taxa",7,
 "Drawer photos are raw pattern data; subspecies labels from wing pattern vs DNA barcodes is a live second ruler.",
 ["butterfly collection drawer photographs","lepidoptera specimen images database","moth collection digitised drawers","butterfly wing pattern measurements"],
 [".jpg",".tif",".csv"], ["wing","drawer","lepidoptera","specimen"],
 "Whole-drawer and per-specimen wing photographs on regional museum and society collection sites",
 "One specimen — thousands per collection, standard pinning and imaging",
 "Subspecies assigned from wing pattern vs DNA barcode clusters (second ruler)",
 "Type specimens and barcode-vouchered reference series",
 "A museum drawer holds a hundred butterflies pinned in 1920 — their wing patterns still argue with their DNA about who is who.",
 "The big barcode library covers sequences, not the drawer photography of the older regional collections where the pattern-based names were made.")
add("snake-venom-spectra","Snake venom proteomics spectra by population","B. Other taxa",7,
 "Raw spectra per population; antivenom labels are a clinical second ruler; labs publish pooled profiles only.",
 ["snake venom proteomics raw data","venom mass spectra download","venom variation population data xls","antivenom efficacy table archive"],
 [".raw",".mgf",".csv",".xls"], ["venom","proteom","spectra","antivenom"],
 "Mass-spectrometry runs and protein-family tables per venom pool, on toxinology lab sites and supplements",
 "One venom pool — dozens of populations per species complex, similar LC-MS protocols",
 "Species/population name on the vial vs antivenom neutralisation results (second ruler)",
 "Reference venoms held by antivenom producers",
 "The same snake species can be a medical emergency in one valley and far less dangerous in the next — its venom keeps the receipts.",
 "Toxinology is a cottage industry of national labs; each publishes its own population profiles and the raw runs rarely leave the lab site.")

# ---------- Family C: Plants, fungi & microbes ----------
add("seed-bank-germination-vintages","Seed-bank germination-test vintages","C. Plants, fungi & microbes",8,
 "Same accession re-tested for decades — a built-in time series; genebank reports are scattered PDFs, never one panel.",
 ["seed bank germination test results archive","genebank viability monitoring data","accession germination percentage year report pdf","seed longevity trial data download"],
 [".pdf",".xls",".csv"], ["germination","viability","accession","seedbank"],
 "Germination-test result tables (accession × test year × % viable) in genebank reports and centre PDFs",
 "One accession — thousands per genebank, re-tested on a fixed cycle under one protocol",
 "Lab germination % vs field emergence of the same accession (second ruler)",
 "FAO/IPGRI standard-protocol reference trials",
 "Seeds put to sleep in 1975 were woken up in 2025 — and some of them grew. Nobody has lined up all the wake-up calls in one table.",
 "Each genebank publishes its own monitoring summaries in its own format and decade; the accession-level panel across banks was never assembled.")
add("diatom-type-slides","Diatom slide & valve image collections","C. Plants, fungi & microbes",8,
 "Glass valves photograph beautifully and forever; small personal databases hold the type-slide imagery.",
 ["diatom image database download","diatom valve photographs collection","diatom type slide catalogue","diatom identification images csv"],
 [".jpg",".tif",".csv"], ["diatom","valve","frustule"],
 "Light- and SEM-micrographs of diatom valves with slide references, on personal and institute collection sites",
 "One valve image — thousands per collection, standard microscopy protocol",
 "Names from morphology atlases vs DNA metabarcoding of the same waters (second ruler)",
 "Type slides in the historic herbaria (e.g. Hustedt collection)",
 "A one-celled alga builds itself a glass house finer than a cathedral window — and the glass outlives every name scientists give it.",
 "Diatom taxonomy lives in a few experts' personal databases and slide cabinets; the imagery behind the standard atlases is scattered across institute pages.")
add("wood-anatomy-xylarium","Wood anatomy (xylarium) section images","C. Plants, fungi & microbes",8,
 "Microscope sections per timber species; commercial names are a second ruler that often lies; forensic value keeps it fragmented.",
 ["wood anatomy image database","xylarium cross section photographs","wood identification microscopy archive","timber anatomy measurements csv"],
 [".jpg",".tif",".csv"], ["wood","xylem","anatomy","section"],
 "Transverse/radial/tangential section micrographs and feature codings on xylarium and lab sites",
 "One wood sample — thousands of species across xylaria, one sectioning protocol",
 "Commercial timber name on the sample vs anatomical identification (second ruler)",
 "IAWA feature list and reference xylaria vouchers",
 "Every plank of wood carries a fingerprint in its pores — customs officers, museums and labs each keep a piece of the fingerprint file.",
 "InsideWood joined one feature database, but the section imagery of the national xylaria sits on separate institute sites, much of it scanned once for a thesis.")
add("heritage-tree-ring-cores","Heritage dendrochronology — building & art timbers","C. Plants, fungi & microbes",7,
 "Building-timber ring series live on heritage-lab sites, outside the climate tree-ring banks; radiocarbon is the anchor.",
 ["dendrochronology building timbers data","tree ring dating historic buildings report","oak panel painting dendro data","ring width series download txt"],
 [".txt",".rwl",".csv",".pdf"], ["dendro","ring","timber","chronology"],
 "Ring-width series files (.rwl/.txt) and dating reports for building timbers and panel paintings, on heritage dendro lab sites",
 "One timber — hundreds of dated buildings per lab, one crossdating protocol",
 "Dendro date vs radiocarbon / documented construction date (second ruler)",
 "Regional master chronologies held by the labs themselves",
 "The beam in a 600-year-old roof knows the year its tree was felled — to the year, sometimes to the season.",
 "Climate dendro has its bank (ITRDB); heritage dendro — houses, ships, paintings — is dozens of small labs whose series files sit beside their client reports.")
add("phage-plaque-hostrange","Bacteriophage plaque & host-range collections","C. Plants, fungi & microbes",7,
 "Plaque photos + host-range tables per phage; genome labels arrived later and renamed the collection.",
 ["bacteriophage collection host range table","phage plaque photographs archive","phage bank catalogue download","phage host range data csv"],
 [".jpg",".csv",".xls"], ["phage","plaque","host","lytic"],
 "Plaque photographs and host-range assay tables on university phage-bank and lab sites",
 "One phage — hundreds per teaching/lab collection, standard plaque-assay protocol",
 "Host range by plaque assay vs host predicted from genome (second ruler)",
 "Reference host strains and typed type-phages",
 "A virus you cannot see leaves a clear hole in a lawn of bacteria that you can — and the hole's shape is its signature.",
 "Phage banks are teaching-collection scale, kept by individual labs; the pre-genomic host-range tables were never re-checked against the genomes.")

# ---------- Family D: Human body & medicine history ----------
add("longitudinal-growth-studies","Longitudinal child growth study records","D. Human body & medicine history",9,
 "Same child measured yearly for decades — the rarest design in human biology; most collections joined one consortium, the strays did not.",
 ["longitudinal growth study records archive","child growth study radiographs collection","growth study cephalometric images download","Fels Bolton Brush records data"],
 [".jpg",".tif",".csv"], ["growth","cephalometr","longitudinal","radiograph"],
 "Serial radiographs, photographs, casts and measurement sheets per child, on growth-centre and foundation sites",
 "One child — hundreds per study, measured at fixed ages under one protocol for 20+ years",
 "Skeletal-maturity stage called by rater A vs rater B on the same films (second ruler)",
 "The child's known chronological age and the Greulich–Pyle / Tanner–Whitehouse atlases built from these very films",
 "The same child, X-rayed every birthday from 2 to 25, is a ruler for human growing that no snapshot study can replace.",
 "Nine US craniofacial collections were consolidated by the AAOF — but the non-craniofacial series, the non-US studies and the two un-joined collections remain on centre sites, un-reconciled.")
add("autopsy-cause-of-death-ledgers","Hospital autopsy & cause-of-death ledgers (pre-1950)","D. Human body & medicine history",9,
 "One hospital's dead, protocolled for 70 years; period diagnoses vs modern recoding is a textbook second ruler.",
 ["autopsy reports archive 19th century hospital","cause of death register digitised pdf","dissection register archive download","postmortem records historical hospital data"],
 [".pdf",".csv",".jpg"], ["autopsy","postmortem","cause of death","register"],
 "Autopsy protocol books, dissection registers and death registers as PDFs/images on hospital, university and state archive sites",
 "One hospital — thousands of protocols per institution, one protocol form for decades",
 "Diagnosis written at death vs the same case recoded to modern ICD by historians (second ruler)",
 "The hospitals' own published annual reports and Registrar-General series",
 "A hospital's dead, counted the same way for 70 years, show diseases disappearing before the drugs that cured them were invented.",
 "Each archive digitised its own registers (Barts, Columbia, state asylums) as catalogue PDFs; nobody has built the cross-hospital case-level panel.")
add("blood-group-surveys","Pre-DNA blood-group population surveys (1919–1970s)","D. Human body & medicine history",8,
 "Humanity's first genetic map, made with needles and antisera; the tables live in old supplements and society sites.",
 ["blood group frequencies population table","ABO blood group survey data archive","serological anthropology data download","blood group distribution historical csv"],
 [".csv",".xls",".pdf"], ["blood group","ABO","Rh","frequency"],
 "Population frequency tables for ABO/Rh and other systems, in journal supplements and anthropological society files",
 "One population sample — hundreds of populations worldwide, one serological protocol family",
 "Allele frequencies implied by serology vs modern DNA frequencies for the same populations (second ruler)",
 "Mourant's standard compilations as the published benchmark to audit against",
 "Before DNA, scientists mapped the whole human species with nothing but blood types, needles and trains — and their tables are still the only record for some peoples.",
 "Mourant's books froze the published version; the underlying expedition tables and later regional surveys sit scattered in supplements nobody re-digitised.")
add("pathology-museum-jars","Pathology museum specimen catalogues","D. Human body & medicine history",8,
 "Wet specimens with 1800s diagnoses; modern re-diagnosis of the same jar is a stark second ruler.",
 ["pathology museum specimen catalogue","anatomical museum collection database photographs","wet specimen catalogue download","medical museum specimens csv"],
 [".jpg",".csv",".pdf"], ["specimen","pathology","museum","wet preparation"],
 "Specimen photographs and catalogue entries (jar number, period diagnosis, provenance) on medical museum sites",
 "One specimen — hundreds to thousands per museum, one cataloguing tradition",
 "The 19th-century label diagnosis vs modern pathologist re-diagnosis (second ruler)",
 "Linked case notes and postmortem records where they survive",
 "A jar on a museum shelf carries a diagnosis from 1850 that its doctors could not possibly have verified — modern medicine can, without opening the jar.",
 "Every medical school museum catalogued its own shelves; the catalogues are small PDFs and pages, and cross-museum re-diagnosis has never been attempted.")
add("orthodontic-dental-casts","Orthodontic study-cast & ceph archives (non-growth-centre)","D. Human body & medicine history",7,
 "Dental departments hold cast mountains; Angle classifications by different schools disagree on the same teeth.",
 ["orthodontic study casts archive","dental cast measurements data","cephalometric archive download","orthodontic records collection photographs"],
 [".jpg",".stl",".csv"], ["cast","cephalometr","orthodont","occlusion"],
 "Study-cast scans/photos and cephalometric tracings on dental-school and society archive pages",
 "One patient series — hundreds per department, standard impression protocol",
 "Malocclusion class assigned by school A vs school B conventions (second ruler)",
 "The AAOF growth collections as the untreated-growth reference anchor",
 "A century of plaster teeth in department cupboards records how human jaws changed — measured three different ways by three different schools.",
 "The famous growth centres got consolidated; ordinary teaching-department cast archives stayed local, scanned piecemeal if at all.")

# ---------- Family E: Earth & weather vintages ----------
add("river-gauge-charts","River gauge recorder charts & staff-gauge ledgers","E. Earth & weather vintages",9,
 "Rivers wrote their own diaries in ink for a century; chart archives sit in basin agencies, mostly unscanned or singly rescued.",
 ["river gauge charts archive digitised","autographic water level charts history","staff gauge readings ledger pdf","hydrometric data rescue charts download"],
 [".jpg",".tif",".pdf",".csv"], ["gauge","chart","water level","hydrometr"],
 "Autographic recorder charts and staff-gauge ledger scans on basin-authority, archive and data-rescue project sites",
 "One gauge station — hundreds of stations per country, weekly charts for decades, one recorder family",
 "Level read off the chart vs discharge computed from the period rating curve (second ruler)",
 "Modern gauging stations and surveyed gauge-zero benchmarks",
 "A river wrote down its own height, in ink, every hour for fifty years — most of those diaries have never been read by a computer.",
 "Data rescue is project-by-project (Bavarian Danube 1826–94 was only rescued in 2025); each basin authority holds its own chart rooms and few series are public.")
add("tide-marigrams","Tide-gauge marigram rolls","E. Earth & weather vintages",8,
 "Monthly means were consolidated (PSMSL); the raw hourly ink traces behind them were not.",
 ["tide gauge marigram archive","historical tide charts digitised","sea level recorder rolls photographs","port tide gauge records download"],
 [".jpg",".tif",".pdf"], ["tide","marigram","sea level","gauge"],
 "Marigram (paper tide-curve) scans and port tide tables on hydrographic and port archive sites",
 "One port — hundreds of ports, continuous hourly curves for decades",
 "Monthly mean sea level published from the rolls vs re-derived from the raw curves (second ruler)",
 "PSMSL monthly series and modern GNSS-referenced gauges",
 "Before satellites, the sea's slow rise was drawn by a pen floating on the tide itself — the pens' rolls are still in port archives.",
 "PSMSL consolidated the monthly numbers decades ago; the underlying marigrams that could expose datum shifts sit in separate national archives.")
add("glacier-repeat-photos","Glacier repeat-photography archives (club & survey)","E. Earth & weather vintages",8,
 "Same viewpoint, same glacier, decades apart; alpine-club photo piles predate the official repeat-photo databases.",
 ["glacier repeat photography archive","historical glacier photographs collection","glacier terminus survey photographs download","alpine club glacier photo archive"],
 [".jpg",".tif",".csv"], ["glacier","terminus","photograph","retreat"],
 "Dated glacier photographs from fixed viewpoints, on alpine-club, survey and regional archive sites",
 "One glacier viewpoint — hundreds of glaciers, re-occupied photo points across a century",
 "Terminus position paced/surveyed at the time vs measured off the photograph today (second ruler)",
 "Published glacier inventories and surveyed terminus series",
 "Stand where a photographer stood in 1900 and take the same picture: the glacier that filled the frame is gone. Clubs took thousands of these pairs.",
 "The famous repeat-photo databases hold the showcase pairs; alpine clubs' and surveyors' full sequences sit on club and cantonal sites, unmeasured.")
add("paper-seismograms","Paper & film seismogram archives (pre-digital stations)","E. Earth & weather vintages",8,
 "Ink seismograms are raw waveforms; phase picks in bulletins are the second ruler; regional observatories scanned their own drums.",
 ["seismogram archive scans historical","paper seismograms digitised collection","helicorder film archive earthquake","old seismograph records photographs download"],
 [".jpg",".tif",".pdf"], ["seismogram","drum","station","earthquake"],
 "Scanned smoked-paper / photographic seismograms on observatory and university archive sites",
 "One station — dozens of regional stations, continuous drums for decades",
 "Phase picks printed in station bulletins vs re-picks from the scans (second ruler)",
 "ISC / modern instrumental catalogues for the large events",
 "An earthquake in 1930 drew its own portrait on smoked paper — the portrait survives in observatory basements, the readings taken from it are a century old.",
 "Big centres (USGS, INGV) digitised flagship stations; the long tail of colonial and university stations scanned what they could, locally, once.")
add("borehole-well-logs","Borehole & water-well log archives","E. Earth & weather vintages",6,
 "Drillers' logs are raw subsurface truth; state surveys each host their own scans; headline is weaker, hence the score.",
 ["borehole logs archive download","water well logs database scans","drillers log records pdf","geological survey borehole records"],
 [".pdf",".jpg",".csv"], ["borehole","well log","driller","strata"],
 "Drillers' log sheets and borehole record scans on state geological survey and water-authority sites",
 "One borehole — tens of thousands per state survey, standard log forms",
 "Driller's plain-language strata vs geologist-coded lithology (second ruler)",
 "Mapped bedrock geology and modern geophysical logs",
 "Every farm well ever drilled left a one-page X-ray of the ground beneath it — filed county by county, never joined up.",
 "Well logs are a known resource class, but each survey's scans use different forms and portals; cross-region lithology panels remain unbuilt.")

# ---------- Family F: Sky catalogues ----------
add("moonwatch-satellite-cards","Moonwatch & amateur satellite-tracking observation cards","F. Sky catalogues",8,
 "1957's citizen observers left timed position cards; the Smithsonian holds the programme, the observations were never recomputed with modern orbits.",
 ["Moonwatch satellite tracking observations archive","amateur satellite observers records 1957","Baker-Nunn film archive observations","satellite tracking station logs download"],
 [".jpg",".pdf",".csv"], ["moonwatch","satellite","tracking","observation"],
 "Observation cards, station logs and Baker–Nunn film indexes on Smithsonian and amateur-astronomy archive sites",
 "One station pass — 200+ Moonwatch stations worldwide, one timed-position protocol",
 "Orbit computed in 1958 from the cards vs orbit recomputed today from the same cards (second ruler)",
 "Modern satellite catalogues and known re-entry records",
 "In 1957, teenagers with telescopes and stopwatches tracked Sputnik by hand — their cards still hold orbits nobody has recomputed.",
 "SAO's archive is catalogued, not data-published; observer-network ephemera sits between the Smithsonian and amateur societies, claimed by neither field.")
add("lunar-occultation-timings","Lunar occultation & graze timing reports","F. Sky catalogues",7,
 "Stopwatch timings measured the Moon's limb for a century; IOTA's files are personal-site era and never re-reduced against modern star positions.",
 ["lunar occultation timings archive","graze occultation reports data","occultation observations download txt","IOTA occultation records"],
 [".txt",".csv",".pdf"], ["occultation","graze","timing","lunar limb"],
 "Observer timing reports (text/PDF) on IOTA section and personal astronomy sites",
 "One event — thousands of timed disappearances per decade, one reporting protocol",
 "Limb profile derived from 1970s timings vs the same timings re-reduced with modern satellite star positions (second ruler)",
 "Kaguya / LOLA lunar limb profiles",
 "Amateurs with stopwatches mapped the mountains on the Moon's edge to a hair's breadth — using stars that have since been re-measured from space.",
 "Occultation astronomy is a volunteer world of section coordinators and personal pages; reductions were published, the raw timing files mostly were not pooled.")
add("observatory-plate-logbooks","Small-observatory glass plate logbooks & plate stacks","F. Sky catalogues",7,
 "Plate logbooks are the index to a century of sky photos; big plate archives are famous, small observatories' are attic material.",
 ["observatory plate archive logbook","glass plate collection catalogue download","photographic plate inventory observatory","plate logbook digitised pdf"],
 [".pdf",".csv",".jpg"], ["plate","logbook","glass","observatory"],
 "Plate logbook scans and plate-stack inventories on small observatory and university archive sites",
 "One plate — thousands per observatory, one logbook tradition",
 "Object named in the logbook vs what modern plate-solving finds on the plate (second ruler)",
 "DASCH / APPLAUSE reductions for the flagship collections as method anchor",
 "A century of the night sky sits on glass in observatory attics — the logbooks that say what's on each plate are themselves fading paper.",
 "Harvard and Sonneberg got digitisation programmes; the dozens of smaller plate stacks have, at best, a PDF logbook on an archive page.")
add("early-radio-astronomy-charts","Early radio-astronomy chart recordings","F. Sky catalogues",7,
 "Pen-chart drift scans are the raw data of radio astronomy's first decades; each observatory's charts were read once, by hand.",
 ["early radio astronomy chart recordings","radio telescope pen chart archive","drift scan records historical","Jodrell Bank archive charts"],
 [".jpg",".pdf",".csv"], ["radio","chart","drift scan","receiver"],
 "Pen-chart / photographic drift-scan records and observing logs on observatory history and archive sites",
 "One receiver chart — years of continuous drift scans per early observatory",
 "Source fluxes read off charts at the time vs modern survey fluxes for the same sources (second ruler)",
 "Modern radio catalogues (NVSS etc.) as the anchor sky",
 "The first maps of the radio sky were drawn by pens on paper tape, in real time, by night staff — the tapes were never re-read.",
 "Radio astronomy's history is well told but its chart archives are observatory-by-observatory, mostly unscanned, and the field moved to digital too fast to consolidate them.")
add("sunspot-drawings","Individual-observer sunspot drawings archives","F. Sky catalogues",6,
 "Distinct from the (excluded, killed) sunspot-number series: the drawings themselves, per observer, are image data with personal equations built in.",
 ["sunspot drawings archive observer","historical sunspot sketches collection","sunspot drawing digitised photographs","solar drawings observatory archive"],
 [".jpg",".pdf"], ["sunspot","drawing","solar","observer"],
 "Sunspot drawing sheets (observer, date, group sketch) on observatory and society archive sites",
 "One observer-day — dozens of long-running observers, daily cadence for decades",
 "Groups counted from the drawing vs the same observer's reported count (second ruler)",
 "Modern SDO/HMI imagery for the overlap years and the published group-number benchmark",
 "For 150 years, people drew the Sun's spots by hand every clear day — each drawer quietly drew a slightly different Sun.",
 "The number series built from drawings is consolidated (and was hunted/killed as a target); the drawing sheets themselves, observer by observer, sit in separate observatory archives.")

# ---------- Family G: Chemistry, materials & the built world ----------
add("steam-engine-indicator-cards","Steam-engine indicator diagram cards","G. Chemistry, materials & built world",8,
 "An engine drew its own power curve in pencil; engineering societies hold card collections nobody has measured as a set.",
 ["steam engine indicator diagram archive","indicator cards collection engine","steam engine test records pdf","indicator diagram measurements data"],
 [".jpg",".pdf",".csv"], ["indicator","diagram","steam","engine"],
 "Indicator-card scans (pressure–volume loops drawn by the engine itself) on engineering heritage and museum sites",
 "One engine test — hundreds of carded engines in society collections, one instrument (the indicator)",
 "Power computed from the card in its day vs recomputed by modern planimetry (second ruler)",
 "Engines still in steam whose cards can be re-taken today",
 "A steam engine drew a picture of its own power, in pencil, on a card — and engineers filed the cards instead of the numbers.",
 "Indicator cards survive in heritage-society and museum collections as pictures; the engineering literature used individual cards, never a measured population.")
add("dye-sample-books","Victorian & trade dye sample books","G. Chemistry, materials & built world",8,
 "Each swatch is a chemical experiment with its recipe attached; small museums digitised their own books, chemistry untested.",
 ["dye sample book digitised collection","dyers sample book archive photographs","textile dye recipes historical book","aniline dye swatch collection"],
 [".jpg",".pdf",".csv"], ["dye","swatch","sample book","recipe"],
 "Dye sample book page images (swatch + recipe per sample) on museum and library digital collections",
 "One swatch — thousands per book, dozens of books, one trade format",
 "Dye named in the recipe vs dye identified by modern chemical analysis of the swatch (second ruler)",
 "Modern HPLC / Raman dye reference libraries",
 "A Victorian dye book holds ten thousand colours, each with its recipe — and half the chemicals in it are now banned.",
 "Sample books are catalogued as design history, one museum at a time; nobody has treated the swatch-plus-recipe pages as a chemical dataset.")
add("concrete-test-ledgers","Concrete & materials test ledgers (municipal labs)","G. Chemistry, materials & built world",7,
 "Every structure began as crushed cubes; city lab ledgers are uniform, long, and almost entirely unscanned as data.",
 ["concrete cube test records archive","materials testing laboratory ledger historical","cement strength test results 1920 pdf","municipal laboratory test records download"],
 [".pdf",".csv",".jpg"], ["concrete","cube","strength","test"],
 "Cube/cylinder crushing-test ledgers and cement test tables in municipal and university lab archive PDFs",
 "One test — thousands per lab per decade, standard test forms",
 "Strength recorded in the ledger vs the same structures' cores tested today (second ruler)",
 "Modern standards' reference curves and surviving structure cores",
 "Every bridge and dam was once a tray of little concrete cubes, crushed one by one — the crushing ledgers are still on shelves.",
 "Materials testing was municipal routine, archived as paperwork; engineering history used the standards, not the ledgers behind them.")
add("pigment-cross-sections","Paint & pigment cross-section archives (conservation labs)","G. Chemistry, materials & built world",7,
 "Layer stratigraphy per artwork; each museum lab holds its own section photos; Raman IDs are the second ruler.",
 ["paint cross section image archive","pigment analysis conservation data","paint layer stratigraphy photographs","conservation science pigment database"],
 [".jpg",".csv",".pdf"], ["pigment","cross section","paint layer","conservation"],
 "Paint cross-section micrographs with layer notes, on museum conservation and lab sites",
 "One sample — hundreds per museum lab, standard embedding/sectioning protocol",
 "Pigment named from optical microscopy vs Raman / SEM-EDX identification (second ruler)",
 "Reference pigment libraries (e.g. published IR/Raman spectra)",
 "A flake of paint the size of a pinhead contains every repainting a picture ever suffered — layer by layer, like tree rings.",
 "Conservation labs publish case studies, not populations; the cross-section photos accumulate per-lab and are never compared across collections.")
add("towing-tank-records","Ship-model towing-tank test records","G. Chemistry, materials & built world",6,
 "Towing tanks tested every hull form on paper first; university tank archives are local and film-era.",
 ["towing tank test records archive","ship model basin test data historical","model hull resistance measurements pdf","towing tank film archive"],
 [".pdf",".csv",".jpg"], ["towing","hull","resistance","model"],
 "Model resistance-test tables, photos and films on university and naval tank archive pages",
 "One hull model — hundreds per tank, standard towing protocol",
 "Resistance measured in the tank vs the full-size ship's trial results (second ruler)",
 "The surviving ships' documented service speeds",
 "Every great liner was first a wooden model dragged down a water tank — the drag numbers that chose its shape sit in tank archives.",
 "Towing tanks were few and famous, but their test series were client work, archived per-institution and rarely published as data.")

# ---------- Family H: Language, sound & print ----------
add("endangered-language-tape-shelves","Endangered-language field tape shelves (finding aids)","H. Language, sound & print",8,
 "The tapes are the raw capture; many exist only as catalogue cards on archive sites — the probe target is the shelf list itself.",
 ["endangered language recordings archive catalogue","field tapes linguistics archive finding aid","language recordings reels collection list","indigenous language audio archive inventory"],
 [".pdf",".csv",".wav",".mp3"], ["tape","field recording","language","reel"],
 "Reel/cassette inventories and finding aids (speaker, language, date, tape number) on linguistics archive and lab sites — the index to undigitised raw audio",
 "One tape — hundreds to thousands per archive shelf, standard field-recording practice",
 "Language/dialect name on the tape box vs modern classification of the same variety (second ruler)",
 "Digitised reference collections (e.g. ELAR/PARADISEC) for the varieties that were digitised",
 "A language with no living speakers may still have a voice — sitting on a shelf of tapes nobody has played in forty years.",
 "The big language archives catalogue what they digitised; university closets full of field tapes appear, if at all, as a PDF finding aid on a department page.")
add("dialect-survey-recordings","Regional dialect survey recordings & word lists","H. Language, sound & print",8,
 "Surveys recorded the same word list in every village — a designed comparable set, scattered by region.",
 ["dialect survey recordings archive","dialect atlas field recordings download","regional dialect word list data","dialect survey tapes collection"],
 [".wav",".mp3",".csv",".pdf"], ["dialect","survey","word list","pronunciation"],
 "Dialect survey audio and elicitation sheets on regional university and archive sites",
 "One informant — hundreds per survey, the same questionnaire word list in every locality",
 "Transcription made by the survey team vs the surviving audio re-heard today (second ruler)",
 "Published dialect atlases drawn from the same surveys",
 "In the 1950s, recorders drove village to village asking everyone the same 300 words — the tapes of how a whole region spoke are in regional piles.",
 "Each national/regional survey published its atlas and kept its own tapes; cross-survey audio was never pooled or re-transcribed.")
add("playbill-programme-archives","Theatre playbill & concert programme archives","H. Language, sound & print",7,
 "Playbills are structured data in disguise (date, cast, works); small venues and libraries scanned their own runs.",
 ["theatre playbill archive digitised","concert programme collection archive download","playbill database historical performances","opera programme archive photographs"],
 [".jpg",".pdf",".csv"], ["playbill","programme","cast","performance"],
 "Playbill/programme page images on theatre, library and local archive sites",
 "One performance — thousands per venue run, one printed format for decades",
 "Cast as printed in the playbill vs cast as reviewed in next day's press (second ruler)",
 "Published performance annals of the flagship houses",
 "Every night for a hundred years, a theatre printed who sang what — the programmes remember performances no recording ever caught.",
 "Flagship houses published their annals; the long tail of provincial theatres' programmes sits in local-library scans, unindexed as data.")
add("collector-discographies-78rpm","Collector discographies of 78rpm & folk recordings","H. Language, sound & print",6,
 "Enthusiast discographers documented labels the industry archives lost; their files live on personal sites, dying with them.",
 ["78rpm discography archive download","folk recording discography collector site","record label matrix discography data","ethnic recordings discography pdf"],
 [".pdf",".csv",".xls",".html"], ["discography","78rpm","matrix","label"],
 "Label discography files (matrix, take, personnel, date) on collector and society sites",
 "One side — tens of thousands per label run, one discographic format per collector community",
 "Session data from the discography vs the audio itself where copies survive (second ruler)",
 "Company ledgers where published (e.g. label archives) as benchmark",
 "The complete story of a record label may exist only on one collector's website, built over thirty years of evenings.",
 "Discography is a volunteer literature of personal sites and society PDFs; when a site lapses, a label's session history lapses with it.")
add("small-town-newspaper-pages","Small-town newspaper page-image runs (non-US / pre-1923 gaps)","H. Language, sound & print",6,
 "Page images are raw text-plus-ads; national programmes covered flagships, the local runs are library-by-library.",
 ["local newspaper archive digitised pages","small town newspaper scans library collection","historical newspaper page images download","regional newspaper archive photographs"],
 [".jpg",".pdf",".tif"], ["newspaper","gazette","page","archive"],
 "Newspaper page-image runs on local library and archive sites",
 "One issue — thousands per town title, daily/weekly cadence for decades",
 "OCR text layer (where present) vs the printed page re-read (second ruler)",
 "National newspaper programmes' titles as the coverage benchmark",
 "A small town's whole memory — prices, deaths, scandals, weather — ran in a weekly paper whose scans sit on one library's website.",
 "National digitisation took the metropolitan titles; thousands of local runs were scanned by single libraries with no shared index or OCR standard.")

# ---------- Family I: Historical statistics, prices, maps & places ----------
add("commodity-price-currents","Printed commodity price currents (pre-1900 ports)","I. Historical statistics, prices, maps",8,
 "Weekly one-page price sheets from every port — the stock ticker's ancestor; library scans are port-by-port.",
 ["price current historical newspaper archive","commodity prices 19th century list download","prices current Liverpool archive pdf","market price list historical collection"],
 [".pdf",".jpg",".csv"], ["price current","prices","commodity","market"],
 "Price-current sheets (weekly printed commodity price lists) in port-city library and archive scans",
 "One port-week — hundreds of ports × decades of weeks, a standard printed table",
 "Price in the port's current vs the same week in the destination port's current (second ruler — arbitrage gap)",
 "Published long-run price series (the benchmark these sheets fed)",
 "Before the ticker, the price of wheat crossed the ocean on a one-page sheet printed at the dock — and every port printed its own.",
 "Economic historians built series city by city from these sheets; the sheets themselves are scanned, where at all, by the port's own library.")
add("fire-insurance-plans","Fire insurance plans beyond the famous sets (Goad & local)","I. Historical statistics, prices, maps",8,
 "Building-by-building risk maps for hundreds of towns; the famous US set is consolidated, the rest is not.",
 ["fire insurance plan archive town","Goad fire insurance maps collection","insurance plan digitised maps download","fire plan historical town archive"],
 [".jpg",".tif",".pdf"], ["fire insurance","plan","Goad","building"],
 "Fire insurance plan sheets (footprint, material, use per building) on local archive and library sites",
 "One town edition — hundreds of towns, revised editions over decades, one draughting convention",
 "Building material/use coded on the plan vs the same street in trade directories (second ruler)",
 "Modern cadastral / OpenStreetMap footprints for the surviving streetscape",
 "Insurers mapped every building in town — what it was made of, what would burn — and updated the map for fifty years.",
 "Sanborn's US plans got a national programme; Goad's and local plans for the rest of the world sit in the town archives that commissioned them.")
add("factory-payroll-wage-books","Factory payroll & wage books (local archives)","I. Historical statistics, prices, maps",7,
 "Worker-by-week wages are the raw data behind every published wage index; the books are in county record offices.",
 ["factory wage book archive","payroll ledger historical mill records","wage records workers archive pdf","mill pay book digitised"],
 [".pdf",".jpg",".csv"], ["wage","payroll","ledger","mill"],
 "Payroll/wage book scans and transcriptions on local archive, mill-museum and record-office sites",
 "One worker-week — hundreds of workers × decades per firm, standard ledger format",
 "Wage in the firm's book vs the published industry wage series for the same year (second ruler)",
 "Census occupational data and published wage benchmarks",
 "A mill's pay book knows what a twelve-year-old actually earned in 1880, week by week — the famous wage series are averages built from books like it.",
 "Wage books survive firm by firm in local custody; historians sampled famous firms, and the rest were never transcribed as a panel.")
add("booth-level-election-gazettes","Polling-booth-level historical election results in gazettes","I. Historical statistics, prices, maps",7,
 "National results are consolidated at constituency level; booth-level returns sleep in official gazette PDFs.",
 ["historical election results polling station gazette","election returns by booth archive pdf","parliamentary election results 19th century local","gazette election results download"],
 [".pdf",".csv",".jpg"], ["election","returns","booth","gazette"],
 "Booth/polling-place return tables in official gazette and local newspaper scans",
 "One booth — thousands per election, standard return forms",
 "Booth returns summed vs the officially declared constituency total (second ruler — they do not always agree)",
 "Published constituency-level election databases",
 "Elections were decided booth by booth, and the booth numbers were printed once, in a gazette almost nobody kept.",
 "Constituency databases are a mature product; the booth-level geography underneath them was never extracted from the gazette scans.")
add("canal-traffic-ledgers","Canal & inland-navigation traffic ledgers","I. Historical statistics, prices, maps",6,
 "Boat-by-boat cargo tolls are a complete trade census for the pre-rail economy; ledgers sit with canal societies.",
 ["canal traffic ledger archive","canal toll records boats cargo","inland navigation traffic returns pdf","canal company records tonnage download"],
 [".pdf",".jpg",".csv"], ["canal","toll","cargo","tonnage"],
 "Traffic/toll ledger scans on canal society, waterway archive and record-office sites",
 "One boat passage — thousands per canal per decade, standard toll forms",
 "Cargo declared for toll vs cargo in the receiving port's books (second ruler)",
 "Published canal company annual tonnage summaries",
 "Every boat that moved coal in 1820 paid a toll and was written down — boat, owner, cargo, miles — in ledgers canal societies still hold.",
 "Canal history is a society world; its ledgers were microfilmed or scanned locally, and the boat-level panel was never built.")

# ---------- Family J: Food, agriculture, sport & play ----------
add("long-term-crop-plot-books","Long-term crop experiment plot books (beyond the flagships)","J. Food, agriculture, sport & play",9,
 "Same plots, same treatments, a century of yields; the flagship (Rothamsted/Morrow) got curated — the other stations' plot books did not.",
 ["long term agricultural experiment plot data","experiment station yield records archive","field trial plot book historical pdf","continuous cropping experiment data download"],
 [".pdf",".xls",".csv"], ["plot","yield","trial","experiment station"],
 "Plot books and yield tables (plot × treatment × year) in experiment-station reports and university archive PDFs",
 "One plot — dozens of stations worldwide, each running one fixed layout for 50–150 years",
 "Yield printed in the station's annual report vs the plot book's own figure (second ruler)",
 "The curated flagship datasets (Rothamsted eRA, Morrow Plots 2022) as method and benchmark",
 "The same field, planted the same way since 1876, is an experiment nobody alive will see the end of — and most stations' plot books were never turned into data.",
 "Morrow Plots were only curated into a dataset in 2022 and Rothamsted has its own archive; the dozens of other long-term stations (Sanborn, Askov, Halle…) publish reports, not plot-level panels.")
add("photo-finish-film-strips","Photo-finish film strips & hand-timing slips (pre-1968 sport)","J. Food, agriculture, sport & play",8,
 "Finish films are raw measurement; official results were read off them once, by eye, and never re-measured.",
 ["photo finish film archive athletics","photo finish prints historical races","hand timing slips archive sport","finish line photographs olympics archive"],
 [".jpg",".tif",".pdf"], ["photo finish","finish","timing","race"],
 "Photo-finish strips/prints and timing slips on federation, museum and broadcaster archive sites",
 "One race — hundreds of championship races in the film era, one camera protocol per era",
 "Time/result read at the time vs the same strip re-measured digitally today (second ruler)",
 "Official results books as the published benchmark",
 "Some of sport's most famous finishes were decided by a strip of film that a judge read once, in 1960, and nobody has measured since.",
 "Photo-finish film was working material, kept by federations and photo agencies in fragments; results books kept the verdict, not the evidence.")
add("seed-catalogue-varieties","Seed catalogue variety listings (1880–1970)","J. Food, agriculture, sport & play",7,
 "Every catalogue is a variety census with prices; variety names vs trial results is a second ruler for hype.",
 ["seed catalogue archive historical varieties","nursery catalogue digitised collection download","seed catalogue prices varieties 1900 pdf","vegetable varieties catalogue archive"],
 [".pdf",".jpg",".csv"], ["seed catalogue","variety","cultivar","price"],
 "Seed/nursery catalogue page images and listings on library digital collections (e.g. biodiversity and trade-catalogue libraries)",
 "One variety-listing — hundreds of firms × annual catalogues for a century",
 "Variety praised in the catalogue vs the same variety in official trial results (second ruler)",
 "Genebank accession records for varieties that survive",
 "A seed catalogue from 1900 lists 300 tomato varieties; your supermarket has six. The catalogues are the census of what was lost.",
 "Trade-catalogue libraries digitised the famous firms; variety-level extraction across the long tail of regional seedsmen was never done.")
add("regional-menu-collections","Regional restaurant menu collections","J. Food, agriculture, sport & play",7,
 "Menus are dated price-and-dish censuses; the famous collection is one city — regional libraries hold the rest.",
 ["restaurant menu collection archive library","historical menus digitised download","menu collection regional library photographs","hotel menu archive 19th century"],
 [".jpg",".pdf"], ["menu","restaurant","dish","price"],
 "Menu page images on regional library and historical society sites",
 "One menu — hundreds per city collection, dated by design",
 "Dish price on the menu vs the same dish in newspaper advertisements of the same week (second ruler)",
 "Published price indices and the flagship menu collections as benchmark",
 "A 1910 menu prices a full dinner below today's coffee — and lists dishes that no longer exist anywhere on Earth.",
 "NYPL's menu project made one city's collection famous; regional libraries hold comparable runs that were scanned as ephemera, not data.")
add("club-scorebooks-gate-ledgers","Club sport scorebooks & gate ledgers (pre-1950)","J. Food, agriculture, sport & play",6,
 "Scorebooks are the raw record behind sports databases; gate ledgers add the crowd. Club-level material is attic-grade.",
 ["cricket scorebook archive digitised","football club gate receipts ledger archive","baseball scorebook historical collection","sports club records archive download"],
 [".pdf",".jpg",".csv"], ["scorebook","gate","ledger","match"],
 "Scorebook and gate-ledger scans on club, county and society archive sites",
 "One match — hundreds of matches per club archive, standard scorebook format",
 "Scorebook innings vs the next day's newspaper scorecard (second ruler)",
 "Published results databases (the consolidated verdict layer)",
 "The official history of a football club may rest on one scorebook in a supporter's attic — crowds, scorers and all.",
 "National sports databases consolidated top-flight results; the scorebooks and gate books of the ordinary clubs were scanned, if at all, by the clubs themselves.")

def main():
    assert len(N) == 50, f"registry must have exactly 50 entries, has {len(N)}"
    entries = []
    for i, (slug, name, family, score, score_why, kw, exts, words,
            raw, unit, gap, anchor, headline, why) in enumerate(N, 1):
        entries.append({
            "rank_input_order": i, "slug": slug, "name": name, "family": family,
            "score": score, "score_justification": score_why,
            "keywords": kw, "signature_exts": list(exts), "gold_words": list(words),
            "fidelity_card": {"RAW": raw, "UNIT": unit, "LABEL_GAP": gap, "ANCHOR": anchor},
            "headline_shape": headline, "why_niche": why})
    ranked = sorted(entries, key=lambda e: (-e["score"], e["rank_input_order"]))
    for r, e in enumerate(ranked, 1):
        e["rank_by_score"] = r
    doc = {"generated": "2026-11-18", "doctrine": "niche keywords (2026-11-18)",
           "selection_tests": ["fidelity", "headline", "fragmentation"],
           "count": len(entries), "niches": ranked}
    with open("niches.json", "w") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
    # markdown
    lines = ["# The 50 — niche-keyword registry (2026-11-18)", "",
             "Atharva's commission: ~50 niche domain keywords, not touched as much but",
             "with gold potential — headline-shaped like mammals (intuitive to anyone,",
             "hunter-level scope underneath) — targeted by Goldmine Hunter and its",
             "tooling. Campaigns are now GENERATED from the top of this registry",
             "(see README, 'Design doctrine — niche keywords').", "",
             "**Selection tests (every entry passed all three on paper):**",
             "(a) *Fidelity* — raw capture kept; one protocol over dozens+ comparable",
             "units; labels gapped, stranded or on a second ruler; a local anchor.",
             "(b) *Headline* — a non-specialist gets the comparison in one sentence.",
             "(c) *Fragmentation* — NOT a mature field whose central product is already",
             "reconciliation (those publish by design: CRU, Reptile, ATNF — Campaign 5).", "",
             "Excluded: everything already hunted, landed or killed (Brain Catalogue /",
             "mammal brains, rhino forearm, Maddison, CRU, Gaia/GALAH, cryo-EM, cosmology",
             "sims, HCA, WorldClim, SILSO, SDSS, and all Campaign 2–5 hosts). Adjacent-",
             "but-distinct entries are marked as such in their why-niche line.", "",
             "Machine-readable twin: `niches.json`. In the hunter: `python3",
             "goldmine_hunter.py niches [--top N | --niche <slug>]`; per-niche gold",
             "words + signature extensions feed `niche_score()`.", "",
             "## Ranked table", "",
             "| # | Score | Niche | Family | Headline shape |",
             "|---|-------|-------|--------|---------------|"]
    for e in ranked:
        lines.append(f"| {e['rank_by_score']} | {e['score']} | {e['name']} (`{e['slug']}`) | {e['family']} | {e['headline_shape']} |")
    lines += ["", "## Full cards", ""]
    fam_order = []
    for e in entries:
        if e["family"] not in fam_order: fam_order.append(e["family"])
    for fam in fam_order:
        lines.append(f"### {fam}")
        lines.append("")
        for e in [x for x in entries if x["family"] == fam]:
            c = e["fidelity_card"]
            lines += [f"#### {e['name']} — `{e['slug']}` — score {e['score']}/10 (rank {e['rank_by_score']})",
                      f"- **Score justification:** {e['score_justification']}",
                      f"- **Keywords:** " + "; ".join(f"`{k}`" for k in e["keywords"]),
                      f"- **Signature files:** " + ", ".join(e["signature_exts"]) + " · **Gold words:** " + ", ".join(e["gold_words"]),
                      f"- **RAW:** {c['RAW']}",
                      f"- **UNIT:** {c['UNIT']}",
                      f"- **LABEL GAP / SECOND RULER:** {c['LABEL_GAP']}",
                      f"- **ANCHOR:** {c['ANCHOR']}",
                      f"- **HEADLINE SHAPE:** {e['headline_shape']}",
                      f"- **Why niche/untouched:** {e['why_niche']}", ""]
    with open("NICHES-50.md", "w") as fh:
        fh.write("\n".join(lines))
    print(f"niches.json + NICHES-50.md written: {len(entries)} entries")
    print("top 10:", [(e["slug"], e["score"]) for e in ranked[:10]])

if __name__ == "__main__":
    main()
