# Mammal niches — the 50 at Atharva's grain (2026-11-18)

Atharva's correction: he meant niche domains at the grain of
"paws and fingerprint analysis of mammals and all that" — NOT broad
cross-domain fields. The broad registry (`NICHES-50.md`) was the wrong
grain. This registry is **50 niches inside ONE intuitive world —
mammals** (direct animal-trace analogues only where the system is the
same) — each niche a specific body part, trace, print or pattern
system. **This registry now sits AHEAD of the broad registry in the
campaign queue** (see README, 'Mammal-grain niches').

## Why these systems are fertile — the pattern

Each system here is:

(a) a **raw capture** — print, cast, photo, scan, hair cast, X-ray —
taken the **same way across many individuals/species**;
(b) used for **individual ID or age/sex/species reading**, so labels
exist but live in old catalogues, forensic atlases, photo-ID archives
and museum cast collections — often on a **second ruler** (DNA, tags,
collars, dissection, known-age animals); and
(c) **instantly headline-shaped** — a layperson gets it in one
sentence.

**Canonical headline, verified (not just repeated):** the koala's
fingerprint. Henneberg, Lambert & Leigh (1997), *Fingerprint
homoplasy: koalas and humans* (University of Adelaide): ~20 koalas,
ink prints plus scanning electron microscopy — the ridges are
nearly identical to a human's in microscopic morphology, pattern
organisation and individual uniqueness. The authors themselves
called a crime-scene mix-up "extremely unlikely", and no
documented confusion at a crime scene exists. The honest headline
is the verified one: *near-indistinguishable under the microscope*.

Excluded: mammal brains (landed) and rhino forearm centroid work
(landed) — rhino ear-notch/horn ID is a different system and is
included on its own merits.

Machine-readable twin: `mammal_niches.json`. In the hunter:
`python3 goldmine_hunter.py mammal-niches [--top N | --niche <slug>]`;
per-niche gold words + signature extensions feed
`mammal_niche_score()`.

## Ranked table

| # | Score | Niche | Family | Headline shape |
|---|-------|-------|--------|---------------|
| 1 | 9 | Primate fingerprints & dermatoglyphic archives (`primate-fingerprints-dermatoglyphics`) | A. Skin prints — fingers, palms, pads & noses | Police once fingerprinted the chimps at a zoo to rule them out of a crime — the apes' prints were that close to ours. |
| 2 | 9 | Cattle muzzle (nose) print registration archives (`cattle-muzzle-prints`) | A. Skin prints — fingers, palms, pads & noses | Japan has fingerprinted its finest cattle by nose since 1948 — over three million cows, each with a print card like a criminal record. |
| 3 | 9 | Paw-track morphometrics & FIT footprint archives (`paw-track-morphometrics-fit`) | B. Tracks, paws & gait | A photograph of a footprint can name the tiger, its sex and its age — trackers always knew; the measurement files proving it sit project by project. |
| 4 | 9 | Whale fluke trailing-edge photo-ID catalogues (`whale-fluke-trailing-edge`) | C. Flukes, fins, ears & callosities | Every humpback's tail is a fingerprint in black and white — the world spent 50 years photographing them and is only now joining the albums. |
| 5 | 9 | Dolphin dorsal-fin notch catalogues (`dolphin-dorsal-fin-notches`) | C. Flukes, fins, ears & callosities | A dolphin's fin collects nicks like a passport collects stamps — labs have filed the passports bay by bay for fifty years. |
| 6 | 9 | Elephant ear edge, tear & vein ID archives (`elephant-ear-edge-veins`) | C. Flukes, fins, ears & callosities | An elephant's ear is a torn, veined map no other elephant shares — researchers have carried its ID cards in Land Cruiser gloveboxes for fifty years. |
| 7 | 9 | Whisker-spot (vibrissae) pattern catalogues — lions & pinnipeds (`whisker-spot-patterns`) | F. Faces, ears, eyes, scars, tails & whiskers | A lion's whisker dots are a star chart printed on its muzzle — rangers have read the same chart since 1970 and kept it park by park. |
| 8 | 9 | Mammal guard-hair scale casts & hair atlases (wildlife forensics) (`guard-hair-scale-casts`) | G. Hair & applied-mark pattern atlases | A single guard hair carries a scale pattern like a fingerprint — forensic atlases were built continent by continent and never checked against each other. |
| 9 | 8 | Koala fingerprint collections (`koala-fingerprints`) | A. Skin prints — fingers, palms, pads & noses | A koala's fingerprint is nearly indistinguishable from a human's under a microscope — verified in 1997, and no, it has never actually turned up at a crime scene. |
| 10 | 8 | Dog nose-print archives (`dog-nose-prints`) | A. Skin prints — fingers, palms, pads & noses | Your dog's nose print is its fingerprint — kennel clubs were filing them on index cards a century ago. |
| 11 | 8 | Plaster track-cast museum collections (`plaster-track-cast-collections`) | B. Tracks, paws & gait | Before cameras, scientists carried plaster to the snow and poured the footprint itself — museums still hold the drawers of poured paws. |
| 12 | 8 | Elephant footprint age-estimation archives (`elephant-footprint-age`) | B. Tracks, paws & gait | You can read an elephant's age off the print its front foot leaves in the dust — if you have the calibration walks, and almost nobody kept them. |
| 13 | 8 | Right-whale head callosity catalogues (`right-whale-callosity-patterns`) | C. Flukes, fins, ears & callosities | The rough white patches on a right whale's head are as fixed as a face — whale watchers have read them from planes since the seventies. |
| 14 | 8 | Manatee scar & tail photo-ID system archives (`manatee-photo-id-scars`) | C. Flukes, fins, ears & callosities | A manatee is known by its propeller scars — the state of Florida keeps a mugshot file, part sketchbook, part database. |
| 15 | 8 | Rhino ear-notch & horn-profile ID records (`rhino-ear-notch-horn-profiles`) | C. Flukes, fins, ears & callosities | Rhino managers cut a code into the ear and read the horn's silhouette like a skyline — each reserve keeps its own skyline book. |
| 16 | 8 | Pinniped pelage-pattern photo-ID (ringed & monk seals) (`pinniped-pelage-patterns`) | C. Flukes, fins, ears & callosities | A ringed seal wears a fingerprint made of rings over its whole body — no two seals have ever worn the same one. |
| 17 | 8 | Tiger stripe-pattern camera-trap catalogues (`tiger-stripe-catalogues`) | D. Coat patterns — stripes, rosettes, spots & scales | No two tigers share a stripe map — countries count their tigers from stripe photographs and then lock the photographs away. |
| 18 | 8 | Leopard & jaguar rosette catalogues (`leopard-jaguar-rosettes`) | D. Coat patterns — stripes, rosettes, spots & scales | A jaguar's rosettes are a star-map only it wears — every valley's researchers keep their own atlas of the same sky. |
| 19 | 8 | Zebra stripe-pattern ID archives (`zebra-stripe-patterns`) | D. Coat patterns — stripes, rosettes, spots & scales | A zebra's stripes are a barcode its own foal learns by heart — scientists have been photocopying the barcodes since the sixties. |
| 20 | 8 | Giraffe coat-pattern ID archives (`giraffe-coat-patterns`) | D. Coat patterns — stripes, rosettes, spots & scales | A giraffe wears its name in patches big enough to read from a safari vehicle — every reserve reads a different page. |
| 21 | 8 | Tooth-wear age charts & jaw collections (deer and game) (`tooth-wear-age-charts`) | E. Teeth, horns, antlers & wings | A deer's teeth are a clock every hunter is taught to read — the clock was set from a few hundred jaws and never re-checked against the true ages. |
| 22 | 8 | Cementum-annuli tooth-age laboratory archives (`cementum-annuli-tooth-archives`) | E. Teeth, horns, antlers & wings | Slice a tooth and count the winters in its root — the labs that do it hold a half-century of slices nobody lined up against the ages everyone guessed in the field. |
| 23 | 8 | Primate & chimpanzee face-pattern ID archives (`primate-face-pattern-archives`) | F. Faces, ears, eyes, scars, tails & whiskers | Researchers at Gombe know two hundred chimpanzee faces the way you know your family's — the portrait files that taught them are still at the field stations. |
| 24 | 7 | Primate & clinical palm/sole dermatoglyphics (atd angle archives) (`primate-palm-sole-dermatoglyphics`) | A. Skin prints — fingers, palms, pads & noses | Doctors once read a baby's palm the way they now read its chromosomes — the angle in the palm was a genetic test. |
| 25 | 7 | Paw-pad surface & ridge pattern atlases (bears, raccoons, carnivores) (`paw-pad-ridge-patterns`) | A. Skin prints — fingers, palms, pads & noses | A raccoon's hand looks eerily like a tiny human hand — and its palm print is in the tracking atlases to prove it. |
| 26 | 7 | Bear paw mensuration & harvest track records (`bear-paw-mensuration`) | B. Tracks, paws & gait | A dead bear's back foot was measured to guess its sex — the guess was written down for fifty years before anyone checked it against DNA. |
| 27 | 7 | Wolf & canid track-size survey archives (`canid-track-size-archives`) | B. Tracks, paws & gait | A wolf and a big dog leave nearly the same footprint — the argument about which one crossed the farm is settled from tables nobody has pooled. |
| 28 | 7 | Snow-track gait & stride archives (lynx, wolverine, mustelids) (`snow-track-gait-archives`) | B. Tracks, paws & gait | In deep snow an animal writes its name in stride — surveyors read the same script every winter for forty years and filed it by province. |
| 29 | 7 | Elephant tusk shape & configuration records (`elephant-tusk-patterns`) | C. Flukes, fins, ears & callosities | An elephant's tusks are as personal as handwriting — and in one park, war selected the elephants whose tusks never grew. |
| 30 | 7 | Cheetah spot & tear-mark ID files (`cheetah-spot-patterns`) | D. Coat patterns — stripes, rosettes, spots & scales | A cheetah can be told from its spots and the black tear-lines on its face — the projects that learned the faces never shared the album. |
| 31 | 7 | Snow leopard rosette & tail catalogues (`snow-leopard-rosettes`) | D. Coat patterns — stripes, rosettes, spots & scales | The ghost cat's coat is the only name it answers to — twelve countries keep twelve partial ghost albums. |
| 32 | 7 | African wild dog coat-pattern ID archives (`painted-dog-coat-patterns`) | D. Coat patterns — stripes, rosettes, spots & scales | Every painted dog is a one-off painting — rangers name the paintings, and the name-books stay in the parks. |
| 33 | 7 | Pangolin scale-pattern & seizure ID records (`pangolin-scale-patterns`) | D. Coat patterns — stripes, rosettes, spots & scales | A pangolin's scales are its armour and its price tag — the rescued ones are photographed, the seized ones are weighed, and the two records never meet. |
| 34 | 7 | Mammal dental casts & tooth-row pattern collections (`dental-casts-mammal`) | E. Teeth, horns, antlers & wings | Before scanners, a mammal's teeth travelled the world as plaster — the plaster is still in the drawers, wearing the old names. |
| 35 | 7 | Antler tine & beam record archives (trophy and cast-antler series) (`antler-tine-records`) | E. Teeth, horns, antlers & wings | The same buck drops a bigger crown every year and picks it up nowhere — hunters kept the crowns, and together they are his growth chart. |
| 36 | 7 | Horn growth-ring (annuli) age records — sheep, goats, ibex (`horn-annuli-age-records`) | E. Teeth, horns, antlers & wings | A ram wears its birthdays as rings on its horns — check stations have read them for decades and filed the readings by district. |
| 37 | 7 | Bat wing venation & membrane pattern archives (`bat-wing-venation`) | E. Teeth, horns, antlers & wings | A bat's wing is a hand with the fingers stretched into a sail — the veins map like a palm print, and banders photographed them for decades. |
| 38 | 7 | Livestock iris-pattern ID records (`livestock-iris-patterns`) | F. Faces, ears, eyes, scars, tails & whiskers | For a few years, cows were going to log in with their eyes — the iris trials were run, photographed, and shelved when ear tags won. |
| 39 | 7 | Ear-notch & ear-punch record systems (livestock and wildlife) (`ear-notch-punch-registries`) | F. Faces, ears, eyes, scars, tails & whiskers | A pig's ear is punched with its litter number like a train ticket — the ticket stubs fill a century of farm record books. |
| 40 | 7 | Spotted hyena ear-notch & spot ID archives (`hyena-ear-notch-id`) | F. Faces, ears, eyes, scars, tails & whiskers | A hyena's torn ear is its signature, drawn by hand into the clan file the day it is first recognised. |
| 41 | 7 | Scar & wound-pattern photo-ID archives (cross-species) (`scar-based-photo-id`) | F. Faces, ears, eyes, scars, tails & whiskers | An animal's worst day becomes its ID card — the scar sketches are filed species by species, programme by programme. |
| 42 | 7 | Hair medulla & cross-section pattern atlases (`hair-medulla-cross-sections`) | G. Hair & applied-mark pattern atlases | Cut a hair across and it shows a tiny patterned core — a second fingerprint inside the first, keyed in separate books. |
| 43 | 6 | Sheep & goat nose-print and muzzle records (`sheep-goat-nose-prints`) | A. Skin prints — fingers, palms, pads & noses | Sheep were nose-printed to catch show-ring fraud — the print proved the prize ram was a substitute. |
| 44 | 6 | Cat nose-leather pattern records (`cat-nose-leather-patterns`) | A. Skin prints — fingers, palms, pads & noses | Every cat's nose is said to be one of a kind — but unlike dogs and cattle, nobody ever built the card file to prove it. |
| 45 | 6 | Hoof & cloven-track measurement systems (deer, livestock, poaching forensics) (`hoof-cloven-track-systems`) | B. Tracks, paws & gait | Two toes in the mud can put a poacher in court — if the reference prints for every hoofed suspect were ever gathered in one place. |
| 46 | 6 | Claw-mark & scratch-tree archives (bears, big cats) (`claw-mark-archives`) | B. Tracks, paws & gait | A bear signs the tree it rubs — the width of its claw strokes is a signature researchers measure and then file away study by study. |
| 47 | 6 | Bite-mark & tooth-pit records (predation and forensic) (`bite-mark-records`) | E. Teeth, horns, antlers & wings | The spacing of two punctures in bone can name the jaws that made them — palaeontologists and wardens measure the same holes and never compare notes. |
| 48 | 6 | Vibrissae follicle & mystacial pad maps (small mammals & pinnipeds) (`vibrissae-follicle-maps`) | F. Faces, ears, eyes, scars, tails & whiskers | Every whisker has an address, and the brain keeps a map of the addresses — the address books are drawn lab by lab and never compared across species. |
| 49 | 6 | Tail pattern & tail-ring ID systems (lemurs, raccoons, cats, marine mammals) (`tail-pattern-systems`) | F. Faces, ears, eyes, scars, tails & whiskers | Half of a cheetah's name is written on the last white rings of its tail — tail patterns are everyone's second clue and nobody's archive. |
| 50 | 6 | Lab-animal marking-pattern records (ear punch, toe clip, tattoo archives) (`lab-animal-marking-records`) | G. Hair & applied-mark pattern atlases | Generations of lab mice were named by holes punched in their ears — the punch charts are a pattern language filed with the colony books. |

## Full cards

### A. Skin prints — fingers, palms, pads & noses

#### Primate fingerprints & dermatoglyphic archives — `primate-fingerprints-dermatoglyphics` — score 9/10 (rank 1)
- **Score justification:** The original fingerprint science was built on animal prints too — Cummins-era dermatoglyphic collections cover dozens of primate species, ridge counts never re-joined across collections.
- **Keywords:** `primate dermatoglyphics archive`; `ape monkey fingerprint ridge count data`; `dermatoglyphic collection photographs download`; `chimpanzee fingerprint identification study`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** dermatoglyph, fingerprint, ridge count, triradius
- **RAW:** Ink and rolled fingerprints, palm prints and dermatoglyphic tracings in anthropology and forensic collections
- **UNIT:** One finger/palm — thousands of prints across dozens of primate species in the classic collections, one ink-print protocol
- **LABEL GAP / SECOND RULER:** Species/individual called from ridge pattern vs DNA taxonomy of the same zoo/museum animals (second ruler)
- **ANCHOR:** Zoo studbooks and museum specimens tied to print cards
- **HEADLINE SHAPE:** Police once fingerprinted the chimps at a zoo to rule them out of a crime — the apes' prints were that close to ours.
- **Why niche/untouched:** Dermatoglyphics was a mid-century industry whose collections sit in anthropology departments and forensic museums; genetics replaced it before its cross-species ridge data was ever pooled.

#### Koala fingerprint collections — `koala-fingerprints` — score 8/10 (rank 9)
- **Score justification:** Headline is perfect and verified (Henneberg 1997), but the known print population is small — one species, tens of documented individuals — so archive depth caps the score.
- **Keywords:** `koala fingerprint print collection`; `koala dermatoglyphics images`; `Henneberg koala fingerprint data`; `marsupial fingerprint ridge study`
- **Signature files:** .jpg, .tif, .pdf · **Gold words:** koala, fingerprint, ridge, homoplasy
- **RAW:** Ink prints and SEM fingertip images from wildlife-park and university anatomy collections
- **UNIT:** One fingertip — one species, tens of individuals in the published study, unknown numbers in zoo/wildlife-park files, one ink-print protocol
- **LABEL GAP / SECOND RULER:** Koala ridge pattern vs human prints in the same forensic reference files (the second ruler is our own fingerprint system)
- **ANCHOR:** The 1997 Adelaide reference prints (Henneberg, Lambert & Leigh)
- **HEADLINE SHAPE:** A koala's fingerprint is nearly indistinguishable from a human's under a microscope — verified in 1997, and no, it has never actually turned up at a crime scene.
- **Why niche/untouched:** One famous study, then near-silence: wildlife parks handle koalas daily and no print collection was ever built on the 1997 foundation.

#### Primate & clinical palm/sole dermatoglyphics (atd angle archives) — `primate-palm-sole-dermatoglyphics` — score 7/10 (rank 24)
- **Score justification:** Palmar atd angles and sole patterns fill medical-genetics archives (Down syndrome diagnostics era) plus primate atlases; two literatures never met.
- **Keywords:** `palmar dermatoglyphics atd angle data`; `sole pattern dermatoglyphics archive`; `dermatoglyphics Down syndrome print collection`; `primate palm print atlas`
- **Signature files:** .jpg, .pdf, .csv · **Gold words:** atd, palmar, sole, dermatoglyph
- **RAW:** Palm and sole prints with measured atd angles and pattern maps, in clinical genetics files and primate atlases
- **UNIT:** One palm/sole — thousands of clinical prints, hundreds of primate specimens, one measurement convention
- **LABEL GAP / SECOND RULER:** Pattern diagnosis from prints vs chromosome/DNA diagnosis of the same patients and species (second ruler)
- **ANCHOR:** Karyotyped clinical series and museum primate material
- **HEADLINE SHAPE:** Doctors once read a baby's palm the way they now read its chromosomes — the angle in the palm was a genetic test.
- **Why niche/untouched:** Clinical dermatoglyphics died the day karyotyping arrived; its print archives sit in medical-school files, unlinked to the primate dermatoglyphic collections that used the same measures.

#### Paw-pad surface & ridge pattern atlases (bears, raccoons, carnivores) — `paw-pad-ridge-patterns` — score 7/10 (rank 25)
- **Score justification:** Pad photos/casts are how trackers separate look-alike species; pad atlases are regional, hand-drawn era, never pooled.
- **Keywords:** `paw pad identification atlas`; `bear paw pad photograph collection`; `animal footprint pad pattern guide`; `raccoon paw print dermatoglyphics`
- **Signature files:** .jpg, .tif, .pdf · **Gold words:** pad, paw, plantar, track
- **RAW:** Paw-pad photographs, casts and drawn pad maps in tracking atlases and museum collections
- **UNIT:** One pad — dozens of carnivore/omnivore species per atlas, hundreds of specimens, standard pad-on-glass or cast protocol
- **LABEL GAP / SECOND RULER:** Species called from pad pattern vs the track/trail it came from and DNA from scat at the same site (second rulers)
- **ANCHOR:** Zoo and museum specimens photographed pad-up
- **HEADLINE SHAPE:** A raccoon's hand looks eerily like a tiny human hand — and its palm print is in the tracking atlases to prove it.
- **Why niche/untouched:** Tracking literature is a cottage world of regional guides; the pad reference photos behind them live in authors' and museums' files, not in any shared atlas.

#### Dog nose-print archives — `dog-nose-prints` — score 8/10 (rank 10)
- **Score justification:** Petersen took 350+ animal nose prints in 1922; kennel clubs and insurers ran nose-print registries for decades — paper archives, modern apps are rebuilding from zero.
- **Keywords:** `dog nose print identification archive`; `canine nose print registry records`; `nose print kennel club registration`; `dog nose pattern dataset download`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** nose print, noseprint, muzzle, canine nose
- **RAW:** Ink nose prints on index cards and nose photographs in kennel-club, insurer and lab collections
- **UNIT:** One nose — registries ran to thousands of dogs; the 2021 viability study re-proved uniqueness on 70 dogs / 19 breeds, one ink-or-camera protocol per era
- **LABEL GAP / SECOND RULER:** Nose pattern ID vs microchip/tag records for the same dogs (second ruler)
- **ANCHOR:** Longitudinal re-prints of the same dog months apart (pattern invariance series)
- **HEADLINE SHAPE:** Your dog's nose print is its fingerprint — kennel clubs were filing them on index cards a century ago.
- **Why niche/untouched:** Historic nose-print registries were paper and breed-club local; the smartphone-era startups each built tiny private datasets and none inherited the card archives.

#### Cattle muzzle (nose) print registration archives — `cattle-muzzle-prints` — score 9/10 (rank 2)
- **Score justification:** The biggest fingerprint-style archive in the animal world: Japan's Wagyu Registry has ink muzzle prints for 3M+ beef cattle since 1948 — and it is a paper/card system.
- **Keywords:** `cattle muzzle print registration`; `wagyu nose print certificate archive`; `beppu nose print cattle identification`; `muzzle pattern cattle dataset`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** muzzle, nose print, beppu, wagyu
- **RAW:** Ink muzzle prints lifted on paper/cards at registration (before 4 months, again after 14 months in the Japanese system), plus modern muzzle photographs
- **UNIT:** One muzzle — millions registered in Japan since 1948, thousands in Petersen-era and university series elsewhere, one ink-lift protocol
- **LABEL GAP / SECOND RULER:** Muzzle print ID vs ear-tag / RFID / DNA pedigree records for the same animals (second ruler)
- **ANCHOR:** The Wagyu Registry Association's own registration certificates (nose print + pedigree on one card)
- **HEADLINE SHAPE:** Japan has fingerprinted its finest cattle by nose since 1948 — over three million cows, each with a print card like a criminal record.
- **Why niche/untouched:** The registration archives are institutional paper; the computer-vision literature trains on a few hundred fresh photos and has never touched the historical card millions.

#### Sheep & goat nose-print and muzzle records — `sheep-goat-nose-prints` — score 6/10 (rank 43)
- **Score justification:** Same system as cattle, a tenth the attention: show and sale sheep/goats were nose-printed for identity in fraud disputes; records are society-level paper.
- **Keywords:** `sheep nose print identification`; `goat muzzle print pattern study`; `nose print sheep sale identification`; `small ruminant noseprint dataset`
- **Signature files:** .jpg, .pdf, .csv · **Gold words:** nose print, muzzle, sheep, goat
- **RAW:** Ink nose prints and muzzle photographs in breed-society and agricultural-college collections
- **UNIT:** One muzzle — hundreds to thousands per society/college series, same ink-lift protocol as cattle
- **LABEL GAP / SECOND RULER:** Nose ID vs ear-tag and tattoo records for the same animals (second ruler)
- **ANCHOR:** Agricultural-college teaching series with known animals
- **HEADLINE SHAPE:** Sheep were nose-printed to catch show-ring fraud — the print proved the prize ram was a substitute.
- **Why niche/untouched:** A footnote literature beside the cattle work; breed societies kept their own cards and no cross-society set was ever assembled.

#### Cat nose-leather pattern records — `cat-nose-leather-patterns` — score 6/10 (rank 44)
- **Score justification:** Pet-ID folklore says the cat nose is unique; the actual old evidence is thin vet/clinic photo files — a claim waiting for its archive, hence the lower score.
- **Keywords:** `cat nose print unique identification`; `feline nose leather pattern photograph`; `cat noseprint registration`; `cat nose pattern study images`
- **Signature files:** .jpg, .pdf · **Gold words:** nose leather, nose print, feline nose
- **RAW:** Nose-leather photographs in vet-clinic, shelter and cattery files; a small patent-era print literature
- **UNIT:** One nose — hundreds in scattered clinic/shelter photo sets, no standard protocol (that absence is itself the finding to test)
- **LABEL GAP / SECOND RULER:** Nose pattern vs microchip identity for the same cats (second ruler)
- **ANCHOR:** Shelter intake photo series where chip ID is recorded
- **HEADLINE SHAPE:** Every cat's nose is said to be one of a kind — but unlike dogs and cattle, nobody ever built the card file to prove it.
- **Why niche/untouched:** The claim circulates in pet culture with almost no archival base; any systematic clinic photo piles sit unexamined in shelter systems.

### B. Tracks, paws & gait

#### Paw-track morphometrics & FIT footprint archives — `paw-track-morphometrics-fit` — score 9/10 (rank 3)
- **Score justification:** WildTrack's FIT extracts 120+ measures per print and reports >90% species/sex/age accuracy across 13+ species — yet each species training set lives with its project, captive-known prints are the rarest data in tracking.
- **Keywords:** `footprint identification technology FIT dataset`; `animal track measurements csv download`; `WildTrack footprint database images`; `track morphometrics landmark data`
- **Signature files:** .jpg, .csv, .xls · **Gold words:** footprint, track, FIT, morphometric
- **RAW:** Footprint photographs taken to one ruler-and-slip protocol (WildTrack FIT and its predecessors), plus hand-measured track tables
- **UNIT:** One print/trail — training sets of known captive individuals per species, field trails by the thousand, 13+ species with FIT algorithms
- **LABEL GAP / SECOND RULER:** Individual/sex/age called from print vs the known captive animal or collared wild animal that made it (second ruler)
- **ANCHOR:** Captive-animal known-identity trail sets (the FIT training gold standard)
- **HEADLINE SHAPE:** A photograph of a footprint can name the tiger, its sex and its age — trackers always knew; the measurement files proving it sit project by project.
- **Why niche/untouched:** FIT standardised the capture but not the custody: species datasets sit with NGOs, zoos and consultancies, and the pre-FIT hand-measured track tables were never digitised at all.

#### Plaster track-cast museum collections — `plaster-track-cast-collections` — score 8/10 (rank 11)
- **Score justification:** Museums hold drawers of plaster paw casts — snow leopard, wolf, lynx — made when casts were the data; catalogued as objects, never measured as a set.
- **Keywords:** `plaster track cast collection museum`; `animal track casts catalogue`; `snow leopard track cast specimen`; `wolf footprint cast museum collection`
- **Signature files:** .jpg, .tif, .csv, .pdf · **Gold words:** cast, plaster, track, footprint
- **RAW:** Plaster and latex track casts with specimen labels in natural-history museum collections
- **UNIT:** One cast — hundreds per large collection, dozens of species, one cast-making tradition across a century
- **LABEL GAP / SECOND RULER:** Species/sex on the cast label vs the cast re-measured today against FIT-style morphometrics (second ruler)
- **ANCHOR:** Casts tied to collected specimens or known zoo animals
- **HEADLINE SHAPE:** Before cameras, scientists carried plaster to the snow and poured the footprint itself — museums still hold the drawers of poured paws.
- **Why niche/untouched:** Cast collections were catalogued by accession, not by measurement; nobody has run a single morphometric pass across a museum's cast drawers.

#### Elephant footprint age-estimation archives — `elephant-footprint-age` — score 8/10 (rank 12)
- **Score justification:** Forefoot circumference converts to shoulder height and age; the calibration sets (known-age Amboseli elephants walking in sand) are small, old and priceless.
- **Keywords:** `elephant footprint age estimation data`; `elephant forefoot circumference age`; `elephant track measurement archive`; `footprint shoulder height elephant study`
- **Signature files:** .jpg, .csv, .xls, .pdf · **Gold words:** footprint, forefoot, circumference, age
- **RAW:** Footprint photographs and forefoot-circumference measurement sheets from known-age elephant studies and ranger monitoring
- **UNIT:** One footprint — calibration series from known-age individuals (Amboseli), monitoring trails by the thousand across Africa/Asia
- **LABEL GAP / SECOND RULER:** Age read from the footprint vs the elephant's known birth year in the long-term ID catalogues (second ruler)
- **ANCHOR:** Amboseli known-age individuals measured directly
- **HEADLINE SHAPE:** You can read an elephant's age off the print its front foot leaves in the dust — if you have the calibration walks, and almost nobody kept them.
- **Why niche/untouched:** The method is used by rangers everywhere; the underlying known-age measurement series live in a few theses and project files from the 1980s–2000s.

#### Bear paw mensuration & harvest track records — `bear-paw-mensuration` — score 7/10 (rank 26)
- **Score justification:** Agencies measured hind-foot length on harvested bears for a century to sex/age them; the ledgers predate DNA sexing and were never audited against it.
- **Keywords:** `bear paw measurement harvest records`; `bear hind foot length sex identification`; `bear track measurement data archive`; `grizzly paw mensuration study`
- **Signature files:** .csv, .xls, .pdf, .jpg · **Gold words:** paw, hind foot, mensuration, bear
- **RAW:** Paw measurement cards/ledgers from harvest check stations, plus track-measurement tables in agency reports
- **UNIT:** One paw — thousands of harvested bears per jurisdiction across decades, one measuring-board protocol per agency
- **LABEL GAP / SECOND RULER:** Sex/age from paw size vs DNA/tooth-cementum determination on the same bear (second ruler)
- **ANCHOR:** Check-station bears with both paw cards and cementum ages
- **HEADLINE SHAPE:** A dead bear's back foot was measured to guess its sex — the guess was written down for fifty years before anyone checked it against DNA.
- **Why niche/untouched:** Harvest records are jurisdiction paperwork; the paw-size rules in the hunting guides descend from ledgers nobody re-audited.

#### Wolf & canid track-size survey archives — `canid-track-size-archives` — score 7/10 (rank 27)
- **Score justification:** Wolf-vs-dog-vs-coyote by track size is a live forensic question in rewilding Europe/North America; survey track tables sit in agency PDFs.
- **Keywords:** `wolf track measurements survey data`; `canid track size identification table`; `wolf dog track comparison measurements`; `snow track wolf survey archive`
- **Signature files:** .csv, .pdf, .jpg, .xls · **Gold words:** track, wolf, canid, snow
- **RAW:** Track measurement tables (length/width/gait) from wolf and carnivore snow surveys, agency reports and tracker archives
- **UNIT:** One track set — thousands per national survey across decades, ruler-in-photo or calliper protocol
- **LABEL GAP / SECOND RULER:** Species called from the track vs DNA from scat/hair collected on the same survey line (second ruler)
- **ANCHOR:** Tracks of known captive wolves, dogs and coyotes measured the same way
- **HEADLINE SHAPE:** A wolf and a big dog leave nearly the same footprint — the argument about which one crossed the farm is settled from tables nobody has pooled.
- **Why niche/untouched:** Each country's monitoring programme publishes summary presence maps; the measurement-level track tables stay in project reports and trackers' notebooks.

#### Snow-track gait & stride archives (lynx, wolverine, mustelids) — `snow-track-gait-archives` — score 7/10 (rank 28)
- **Score justification:** Nordic snow-tracking transects recorded stride/gait patterns for decades — a designed comparable set, province by province.
- **Keywords:** `snow tracking transect data archive`; `lynx track gait measurements`; `wolverine snow track survey records`; `animal track stride pattern data`
- **Signature files:** .csv, .pdf, .jpg · **Gold words:** snow track, gait, stride, transect
- **RAW:** Snow-transect record cards and gait diagrams from Nordic and boreal wildlife triangle / survey schemes
- **UNIT:** One track crossing — tens of thousands of transect crossings per country across decades, standard route protocol
- **LABEL GAP / SECOND RULER:** Species from gait pattern vs camera/DNA confirmation in the same survey areas (second ruler)
- **ANCHOR:** Finland's wildlife-triangle long-run series as the published benchmark
- **HEADLINE SHAPE:** In deep snow an animal writes its name in stride — surveyors read the same script every winter for forty years and filed it by province.
- **Why niche/untouched:** Snow tracking is a Nordic institutional tradition with paper-era roots; digitisation happened province by province and the gait-level records were left behind the presence counts.

#### Hoof & cloven-track measurement systems (deer, livestock, poaching forensics) — `hoof-cloven-track-systems` — score 6/10 (rank 45)
- **Score justification:** Deer/sheep/goat/cattle slot measurements are poaching-case evidence; reference sets are police/lab-local and small, hence the score.
- **Keywords:** `hoof print identification measurements`; `cloven hoof track deer sheep comparison`; `livestock track forensic identification`; `deer slot measurement data`
- **Signature files:** .jpg, .pdf, .csv · **Gold words:** hoof, cloven, slot, track
- **RAW:** Hoof-print photographs, casts and slot-measurement tables in forensic and game-warden reference sets
- **UNIT:** One hoof print — hundreds per reference collection, dozens of ungulate species, ruler protocol
- **LABEL GAP / SECOND RULER:** Species called from the slot vs the animal carcass/DNA in the same poaching case (second ruler)
- **ANCHOR:** Farm and zoo ungulates printed on known ground
- **HEADLINE SHAPE:** Two toes in the mud can put a poacher in court — if the reference prints for every hoofed suspect were ever gathered in one place.
- **Why niche/untouched:** Hoof ID is casework knowledge held by wildlife forensic labs and wardens; their reference casts and photos were never published as a set.

#### Claw-mark & scratch-tree archives (bears, big cats) — `claw-mark-archives` — score 6/10 (rank 46)
- **Score justification:** Claw spacing on marked trees is measured in bear/cat studies plot by plot; a real system but the archives are thin and local, hence 6.
- **Keywords:** `bear claw mark tree measurements`; `claw mark identification archive`; `big cat scratch mark tree data`; `claw spacing measurement study`
- **Signature files:** .jpg, .csv, .pdf · **Gold words:** claw mark, scratch, mark tree
- **RAW:** Photographs and spacing/height measurements of claw marks on trees and posts, from bear and big-cat field studies
- **UNIT:** One marked tree — hundreds per study area, tape-and-photo protocol
- **LABEL GAP / SECOND RULER:** Species/individual suggested from claw spacing vs camera-trap photos at the same trees (second ruler)
- **ANCHOR:** Marks made by known captive bears/cats on standard posts
- **HEADLINE SHAPE:** A bear signs the tree it rubs — the width of its claw strokes is a signature researchers measure and then file away study by study.
- **Why niche/untouched:** Claw-mark data is a by-product of habitat studies; no cross-study archive of mark measurements exists.

### C. Flukes, fins, ears & callosities

#### Whale fluke trailing-edge photo-ID catalogues — `whale-fluke-trailing-edge` — score 9/10 (rank 4)
- **Score justification:** 39 North-Pacific catalogues were unified by Happywhale (27,956 individuals) — proof of value AND the narrowing: the un-joined remainder is film-era, Southern Ocean and non-humpback catalogues.
- **Keywords:** `whale fluke photo identification catalogue`; `humpback fluke catalog archive download`; `sperm whale fluke catalogue photographs`; `fluke trailing edge identification collection`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** fluke, trailing edge, photo-id, catalogue
- **RAW:** Fluke photographs (film-era prints/slides and digital) in regional whale research catalogues
- **UNIT:** One fluke — tens of thousands of individuals globally; 39 catalogues in the North Pacific alone, one underside-photo protocol
- **LABEL GAP / SECOND RULER:** Fluke match vs genetic sample taken at the same encounter (second ruler)
- **ANCHOR:** The Happywhale/NPPID unified North Pacific set as the benchmark of what joining yields
- **HEADLINE SHAPE:** Every humpback's tail is a fingerprint in black and white — the world spent 50 years photographing them and is only now joining the albums.
- **Why niche/untouched:** Happywhale joined the North Pacific digital era; the pre-digital slide cabinets, the Southern Ocean and Atlantic regional catalogues, and sperm-whale fluke sets remain separate piles.

#### Dolphin dorsal-fin notch catalogues — `dolphin-dorsal-fin-notches` — score 9/10 (rank 5)
- **Score justification:** Sarasota alone holds 5,000+ fin images since 1970 and GoMDIS joins 35 Gulf catalogues (23,444 animals) — outside the Gulf, hundreds of FinBase-era catalogues never joined anything.
- **Keywords:** `dolphin dorsal fin catalogue download`; `bottlenose dolphin photo ID FinBase`; `dorsal fin notch identification archive`; `dolphin fin catalogue photographs`
- **Signature files:** .jpg, .tif, .csv, .mdb · **Gold words:** dorsal fin, finbase, notch, photo-id
- **RAW:** Dorsal-fin photographs and FinBase/Access-era catalogue databases on lab and institute sites
- **UNIT:** One fin — hundreds of regional catalogues, hundreds to thousands of individuals each, one trailing-edge protocol since Würsig 1977
- **LABEL GAP / SECOND RULER:** Fin ID vs freeze-brand/tag/genetic identity of the same dolphin (second ruler)
- **ANCHOR:** Sarasota's known-history individuals (births/deaths observed since 1970)
- **HEADLINE SHAPE:** A dolphin's fin collects nicks like a passport collects stamps — labs have filed the passports bay by bay for fifty years.
- **Why niche/untouched:** FinBase standardised hundreds of local catalogues on desktop databases that were never networked; GoMDIS proved joining works for one gulf and stopped there.

#### Right-whale head callosity catalogues — `right-whale-callosity-patterns` — score 8/10 (rank 13)
- **Score justification:** The callosity pattern is read from aerial photos since the 1970s; the North Atlantic consortium catalogue is curated but the southern-hemisphere catalogues (Argentina, South Africa, Australia) grew separately.
- **Keywords:** `right whale callosity pattern identification`; `right whale photo identification catalog`; `whale head callosity photographs archive`; `Eubalaena individual catalogue`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** callosity, right whale, photo-id, head pattern
- **RAW:** Aerial and boat photographs of head callosity patterns in consortium and regional catalogues
- **UNIT:** One head — ~400 living North Atlantic individuals, thousands in southern catalogues, aerial-photo protocol since Payne's 1970s work
- **LABEL GAP / SECOND RULER:** Callosity ID vs genetic profiles from biopsy of the same whales (second ruler)
- **ANCHOR:** The North Atlantic Right Whale Consortium catalogue as the curated anchor
- **HEADLINE SHAPE:** The rough white patches on a right whale's head are as fixed as a face — whale watchers have read them from planes since the seventies.
- **Why niche/untouched:** Three ocean basins built three callosity catalogues in three institutions; cross-basin matching (whales do cross) rests on personal correspondence, not a joined archive.

#### Manatee scar & tail photo-ID system archives — `manatee-photo-id-scars` — score 8/10 (rank 14)
- **Score justification:** Florida's MIPS system has matched manatees by scars/tail notches since the 1970s — a state-run pattern archive with sketch-era roots, mirrored by separate Caribbean/Brazil sets.
- **Keywords:** `manatee photo identification system MIPS`; `manatee scar catalogue identification`; `manatee tail notch photographs`; `manatee individual identification database`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** manatee, scar, MIPS, tail notch
- **RAW:** Underwater photographs and hand-drawn scar sketches in the Manatee Photo-ID System and sister programmes
- **UNIT:** One manatee — thousands of individuals in Florida alone since the 1970s, sketch-then-photo protocol
- **LABEL GAP / SECOND RULER:** Scar-pattern ID vs PIT-tag/genetic identity recorded at rescue/health assessments (second ruler)
- **ANCHOR:** Rescued manatees whose identity is known absolutely at release
- **HEADLINE SHAPE:** A manatee is known by its propeller scars — the state of Florida keeps a mugshot file, part sketchbook, part database.
- **Why niche/untouched:** MIPS is an agency system with restricted doors; the sketch-era archive and the non-Florida programmes were never part of any public pattern set.

#### Elephant ear edge, tear & vein ID archives — `elephant-ear-edge-veins` — score 9/10 (rank 6)
- **Score justification:** Amboseli has ID'd 1,600+ elephants since 1972 by ear tears/holes/veins on physical ID cards; every long-term site (Gorongosa, Mara, Samburu…) keeps its own card tradition.
- **Keywords:** `elephant ear identification cards archive`; `Amboseli elephant ID ear tears`; `elephant individual identification ear pattern`; `elephantvoices who's who database ear`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** ear, elephant, ID card, notch
- **RAW:** Photographic ear ID cards (physical card files, later digital) recording ear edge tears, holes and vein patterns, per long-term study site
- **UNIT:** One ear — 1,600+ known individuals at Amboseli, hundreds to thousands per other site, one card-and-photo protocol per site tradition
- **LABEL GAP / SECOND RULER:** Ear ID vs DNA from dung/biopsy and vs tusk/body marks recorded on the same card (second rulers)
- **ANCHOR:** Amboseli's known-birth individuals (exact ages since 1972)
- **HEADLINE SHAPE:** An elephant's ear is a torn, veined map no other elephant shares — researchers have carried its ID cards in Land Cruiser gloveboxes for fifty years.
- **Why niche/untouched:** The ID-card tradition is per-site and partly still physical; Gorongosa's Who's Who went digital behind a password, Amboseli's cards span paper and digital, and no cross-site ear archive exists.

#### Elephant tusk shape & configuration records — `elephant-tusk-patterns` — score 7/10 (rank 29)
- **Score justification:** Tusk shape is the second ID feature on every elephant card and the trait poaching selects on (Gorongosa tusklessness) — but it changes with breakage, capping the score.
- **Keywords:** `elephant tusk shape identification records`; `tusk configuration individual elephant data`; `tuskless elephant registry Gorongosa`; `elephant tusk pattern photographs`
- **Signature files:** .jpg, .csv, .pdf · **Gold words:** tusk, tuskless, configuration, elephant
- **RAW:** Tusk shape/configuration fields and photographs inside elephant ID databases and ivory-seizure records
- **UNIT:** One tusk pair — thousands of registered individuals across site databases, card-description protocol
- **LABEL GAP / SECOND RULER:** Tusk ID vs ear ID on the same individual (second ruler — two pattern systems, one animal)
- **ANCHOR:** Seized-ivory DNA assignments back to populations (the forensic anchor)
- **HEADLINE SHAPE:** An elephant's tusks are as personal as handwriting — and in one park, war selected the elephants whose tusks never grew.
- **Why niche/untouched:** Tusk data rides inside ear-ID databases and seizure labs, never extracted as its own cross-site pattern record.

#### Rhino ear-notch & horn-profile ID records — `rhino-ear-notch-horn-profiles` — score 8/10 (rank 15)
- **Score justification:** Distinct from the landed rhino forearm work: this is the applied ID system — ear notches cut by managers plus horn silhouette profiles, kept per-reserve in sighting books. (Forearm centroid work excluded.)
- **Keywords:** `rhino ear notch identification records`; `rhino horn profile individual identification`; `rhino sighting book ear notch archive`; `rhino ID database ear pattern`
- **Signature files:** .jpg, .csv, .pdf · **Gold words:** ear notch, horn profile, rhino, identification
- **RAW:** Ear-notch diagrams, horn-profile photographs and sighting-book pages from reserves and rhino monitoring programmes
- **UNIT:** One rhino — hundreds per reserve, thousands across programmes, notch-code + profile-photo protocol
- **LABEL GAP / SECOND RULER:** Notch/horn ID vs DNA from ear-tissue taken at the notching itself, and horn DNA (RhODIS) (second rulers)
- **ANCHOR:** RhODIS forensic horn-DNA database as the cross-check anchor
- **HEADLINE SHAPE:** Rhino managers cut a code into the ear and read the horn's silhouette like a skyline — each reserve keeps its own skyline book.
- **Why niche/untouched:** Ear-notching is universal practice and per-reserve paperwork; horn profiles accumulate in monitoring photos that no cross-reserve system ingests.

#### Pinniped pelage-pattern photo-ID (ringed & monk seals) — `pinniped-pelage-patterns` — score 8/10 (rank 16)
- **Score justification:** Saimaa's SealID set (57 seals, 2,080 images) proved a pelage dataset can be published — and exposed how many seal colonies still match patterns by eye from slide boxes.
- **Keywords:** `seal pelage pattern photo identification`; `ringed seal fur pattern catalogue`; `monk seal photo identification catalog`; `seal coat pattern individual identification`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** pelage, seal, fur pattern, photo-id
- **RAW:** Seal flank photographs (slides, then digital) in colony photo-ID catalogues
- **UNIT:** One flank pattern — hundreds of individuals per colony catalogue (Saimaa ~400 animals; Cap Blanc monk seals since 1993), haul-out photo protocol
- **LABEL GAP / SECOND RULER:** Pelage ID vs flipper-tag / telemetry identity of the same seal (second ruler)
- **ANCHOR:** SealID's expert-matched public benchmark set (57 individuals, 2,080 images)
- **HEADLINE SHAPE:** A ringed seal wears a fingerprint made of rings over its whole body — no two seals have ever worn the same one.
- **Why niche/untouched:** Each seal colony's catalogue belongs to its research group; slide-era catalogues (monk seals 1990s) predate the ML datasets and were never digitised into them.

### D. Coat patterns — stripes, rosettes, spots & scales

#### Tiger stripe-pattern camera-trap catalogues — `tiger-stripe-catalogues` — score 8/10 (rank 17)
- **Score justification:** Every tiger's stripes are mapped by camera traps nationally, but the catalogues are security-sealed per country/programme; the pattern data behind published counts is the stranded layer.
- **Keywords:** `tiger stripe pattern identification catalogue`; `camera trap tiger individual identification data`; `tiger stripe database photographs`; `Panthera tigris stripe pattern archive`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** stripe, tiger, camera trap, individual
- **RAW:** Camera-trap flank photographs and stripe-matching files in national and NGO tiger programmes
- **UNIT:** One flank — thousands of individuals across range countries, standard paired-camera protocol
- **LABEL GAP / SECOND RULER:** Stripe ID vs genetic ID from scat collected in the same grids (second ruler)
- **ANCHOR:** India's national tiger estimation archive as the (restricted) anchor set
- **HEADLINE SHAPE:** No two tigers share a stripe map — countries count their tigers from stripe photographs and then lock the photographs away.
- **Why niche/untouched:** Counts are published, pattern files are not; each programme's catalogue is a silo justified by poaching risk, so cross-border tigers are matched by personal contact.

#### Leopard & jaguar rosette catalogues — `leopard-jaguar-rosettes` — score 8/10 (rank 18)
- **Score justification:** Rosettes ID individuals across hundreds of separate camera-trap studies; Wildbook ingests some, the long tail of thesis-era catalogues is the niche.
- **Keywords:** `jaguar rosette identification catalogue`; `leopard rosette pattern camera trap data`; `jaguar individual identification photographs`; `leopard spot pattern archive`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** rosette, jaguar, leopard, camera trap
- **RAW:** Camera-trap rosette photographs and matching spreadsheets from individual study sites
- **UNIT:** One rosette flank — dozens to hundreds of individuals per study, hundreds of studies, paired-camera protocol
- **LABEL GAP / SECOND RULER:** Rosette ID vs GPS-collar/genetic identity in the same study animals (second ruler)
- **ANCHOR:** Long-term sites (e.g. Cockscomb jaguars, since the 1980s) with known individuals
- **HEADLINE SHAPE:** A jaguar's rosettes are a star-map only it wears — every valley's researchers keep their own atlas of the same sky.
- **Why niche/untouched:** Camera-trap science is study-shaped: each project publishes a density estimate and keeps its rosette catalogue in a drawer or a dead laptop.

#### Zebra stripe-pattern ID archives — `zebra-stripe-patterns` — score 8/10 (rank 19)
- **Score justification:** Stripe ID began with hand-drawn zebra codes in the 1960s (Petersen 1972); Grevy's/plains catalogues per ecosystem, plus the famous mare-foal recognition experiments' photo files.
- **Keywords:** `zebra stripe pattern identification archive`; `zebra individual stripe code catalogue`; `Grevy zebra stripe database photographs`; `plains zebra photo identification`
- **Signature files:** .jpg, .tif, .csv, .pdf · **Gold words:** stripe, zebra, stripe code, photo-id
- **RAW:** Stripe photographs and hand-coded stripe diagrams from ecosystem monitoring programmes
- **UNIT:** One flank/shoulder pattern — thousands of individuals in the large ecosystem catalogues, photo protocol since the film era
- **LABEL GAP / SECOND RULER:** Stripe ID vs ear-notch/collar/genetic identity in the same herds (second ruler)
- **ANCHOR:** Long-term known-individual herds (e.g. Grevy's in Kenya) as anchor
- **HEADLINE SHAPE:** A zebra's stripes are a barcode its own foal learns by heart — scientists have been photocopying the barcodes since the sixties.
- **Why niche/untouched:** Zebra ID moved from drawn codes to StripeSpotter-era software per project; the drawn-code archives and most ecosystem catalogues were never merged.

#### Giraffe coat-pattern ID archives — `giraffe-coat-patterns` — score 8/10 (rank 20)
- **Score justification:** Giraffe spots are lifelong and individual; tower-by-tower catalogues across Africa, Wildbook for Giraffe ingests a fraction — the rest are ranger/guide photo files.
- **Keywords:** `giraffe coat pattern identification catalogue`; `giraffe spot pattern individual database`; `giraffe photo identification archive`; `Masai giraffe pattern photographs`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** coat pattern, giraffe, spot, photo-id
- **RAW:** Flank/torso coat-pattern photographs in reserve and research catalogues
- **UNIT:** One torso pattern — hundreds to thousands per population catalogue, right-flank photo convention
- **LABEL GAP / SECOND RULER:** Coat ID vs GPS-collar and genetic identity in monitored populations (second ruler)
- **ANCHOR:** Long-term Serengeti/Murchison known-individual sets
- **HEADLINE SHAPE:** A giraffe wears its name in patches big enough to read from a safari vehicle — every reserve reads a different page.
- **Why niche/untouched:** Tourism and research both photograph giraffes constantly; the ID catalogues sit with individual reserves and guides' hard drives, Wildbook coverage notwithstanding.

#### Cheetah spot & tear-mark ID files — `cheetah-spot-patterns` — score 7/10 (rank 30)
- **Score justification:** Cheetah ID leans on spot patterns plus tail rings and tear marks; Serengeti's decades of ID photos are one project, farm-level Namibian files are another world.
- **Keywords:** `cheetah spot pattern identification`; `cheetah individual identification photographs archive`; `cheetah tear marks tail rings ID`; `Serengeti cheetah project identification data`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** spot, cheetah, tear mark, identification
- **RAW:** Spot-pattern ID photographs and drawn ID sheets from long-term cheetah projects and farmer/researcher files
- **UNIT:** One flank/face — hundreds of known individuals in the Serengeti project alone since the 1970s, photo protocol
- **LABEL GAP / SECOND RULER:** Spot ID vs radio-collar/genetic identity in the same animals (second ruler)
- **ANCHOR:** Serengeti Cheetah Project's known-pedigree individuals
- **HEADLINE SHAPE:** A cheetah can be told from its spots and the black tear-lines on its face — the projects that learned the faces never shared the album.
- **Why niche/untouched:** Fewer, larger projects than leopards, but the same shape: ID albums are project property, and the pre-digital Serengeti sheets are one fire away from loss.

#### Snow leopard rosette & tail catalogues — `snow-leopard-rosettes` — score 7/10 (rank 31)
- **Score justification:** The hardest coat catalogue: 12 range countries, tiny densities, every programme's rosette files precious and separate; scores capped by access and sample size.
- **Keywords:** `snow leopard rosette identification catalogue`; `snow leopard camera trap individual data`; `snow leopard spot pattern photographs`; `Panthera uncia identification archive`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** rosette, snow leopard, camera trap, individual
- **RAW:** Camera-trap rosette and tail photographs in range-country programme files
- **UNIT:** One flank — tens of individuals per valley study, hundreds range-wide in files, paired-camera protocol
- **LABEL GAP / SECOND RULER:** Rosette ID vs genetic ID from the large scat programmes (second ruler)
- **ANCHOR:** Mongolia's long-term collared population as anchor
- **HEADLINE SHAPE:** The ghost cat's coat is the only name it answers to — twelve countries keep twelve partial ghost albums.
- **Why niche/untouched:** Snow leopard science is grant-by-grant and valley-by-valley; the global programme publishes status maps, not the pattern files beneath them.

#### African wild dog coat-pattern ID archives — `painted-dog-coat-patterns` — score 7/10 (rank 32)
- **Score justification:** No two painted dogs share a coat; pack catalogues per park are guide-and-researcher photo books, some running since the 1990s.
- **Keywords:** `African wild dog coat pattern identification`; `painted dog individual identification photographs`; `wild dog pack catalogue archive`; `Lycaon pictus pattern ID`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** coat, painted dog, wild dog, pattern
- **RAW:** Coat-pattern ID photographs and pack catalogues from parks and den-monitoring projects
- **UNIT:** One flank — dozens per pack, hundreds per park catalogue, photo protocol at dens and sightings
- **LABEL GAP / SECOND RULER:** Coat ID vs ear-notch/collar identity in monitored packs (second ruler)
- **ANCHOR:** Long-term Selous/Kruger known packs
- **HEADLINE SHAPE:** Every painted dog is a one-off painting — rangers name the paintings, and the name-books stay in the parks.
- **Why niche/untouched:** Pack catalogues are working tools of individual parks and guides; when a project ends, its coat archive typically ends with it.

#### Pangolin scale-pattern & seizure ID records — `pangolin-scale-patterns` — score 7/10 (rank 33)
- **Score justification:** Pangolin scales carry individual pattern and are the seized commodity itself — rescue-centre ID photos and seizure inventories are two unjoined pattern archives.
- **Keywords:** `pangolin scale pattern identification`; `pangolin individual identification photographs`; `pangolin seizure scale inventory records`; `pangolin scale pattern study`
- **Signature files:** .jpg, .csv, .pdf · **Gold words:** scale, pangolin, pattern, seizure
- **RAW:** Dorsal scale-pattern photographs from rescue/rehab centres and confiscated-scale inventory photographs
- **UNIT:** One scale field — hundreds of rescued individuals per large centre; seizure lots by the tonne, photo protocol at intake
- **LABEL GAP / SECOND RULER:** Scale-pattern ID vs DNA sampled at the same intake/seizure (second ruler)
- **ANCHOR:** Rehab centres' known residents photographed repeatedly
- **HEADLINE SHAPE:** A pangolin's scales are its armour and its price tag — the rescued ones are photographed, the seized ones are weighed, and the two records never meet.
- **Why niche/untouched:** Pangolin work is split between welfare centres (photos, no genetics budget) and enforcement (genetics, no pattern archive); the pattern system itself is barely studied.

### E. Teeth, horns, antlers & wings

#### Tooth-wear age charts & jaw collections (deer and game) — `tooth-wear-age-charts` — score 8/10 (rank 21)
- **Score justification:** Every game agency aged deer by tooth wear from chart sets built on a handful of known-age jaws; the jaw collections behind rival charts were never compared head-to-head.
- **Keywords:** `tooth wear age chart deer known age`; `tooth eruption wear ageing jaw collection`; `red deer jaw age data archive`; `game animal tooth wear reference photographs`
- **Signature files:** .jpg, .pdf, .csv, .xls · **Gold words:** tooth wear, jaw, age, eruption
- **RAW:** Jaw photographs/specimens and wear-score sheets in agency and university game collections
- **UNIT:** One jaw — known-age reference sets of hundreds per species; agency-scored jaws by the hundred thousand, standard wear-chart protocol
- **LABEL GAP / SECOND RULER:** Wear age vs cementum-annuli age from the same jaw (second ruler — the classic two-rulers pair)
- **ANCHOR:** Known-age penned deer/elk herds whose jaws built the original charts
- **HEADLINE SHAPE:** A deer's teeth are a clock every hunter is taught to read — the clock was set from a few hundred jaws and never re-checked against the true ages.
- **Why niche/untouched:** Wear charts are regional (each agency its own poster) and their reference jaw collections sit in freezers and museum drawers, un-cross-validated.

#### Cementum-annuli tooth-age laboratory archives — `cementum-annuli-tooth-archives` — score 8/10 (rank 22)
- **Score justification:** One lab (Matson's) has sectioned teeth since 1969 for agencies continent-wide — annuli counts vs the wear ages and harvest records on the same animals are a ready two-rulers panel.
- **Keywords:** `cementum annuli age data archive`; `tooth section age laboratory records`; `Matson cementum age reports`; `bear deer cementum annuli dataset`
- **Signature files:** .jpg, .tif, .csv, .pdf · **Gold words:** cementum, annuli, tooth section, age
- **RAW:** Tooth cross-section images and annuli count records in ageing-lab and agency files
- **UNIT:** One tooth — hundreds of thousands of teeth sectioned across species since 1969, one histology protocol per lab
- **LABEL GAP / SECOND RULER:** Cementum age vs tooth-wear age and vs known age for marked animals (two second rulers)
- **ANCHOR:** Known-age marked bears/deer submitted blind to the labs
- **HEADLINE SHAPE:** Slice a tooth and count the winters in its root — the labs that do it hold a half-century of slices nobody lined up against the ages everyone guessed in the field.
- **Why niche/untouched:** Ageing is a service industry: labs return a number, agencies file it, and the section images plus the field guesses were never joined into one audit set.

#### Mammal dental casts & tooth-row pattern collections — `dental-casts-mammal` — score 7/10 (rank 34)
- **Score justification:** Dental casts are how mammalogy measured tooth rows before CT; cast drawers in museums carry collector-era labels that CT-era taxonomy revised.
- **Keywords:** `dental cast collection mammal museum`; `tooth cast specimens archive`; `dental impression mammal specimens`; `mammal dentition cast photographs`
- **Signature files:** .jpg, .tif, .csv, .pdf · **Gold words:** dental cast, dentition, tooth row, cast
- **RAW:** Plaster dental casts and tooth-row photographs in museum and dental-school collections
- **UNIT:** One tooth row — hundreds to thousands of casts per collection across dozens of species, impression protocol
- **LABEL GAP / SECOND RULER:** Cast-era species labels vs modern CT/morphometric re-identification of the same specimens (second ruler)
- **ANCHOR:** Type specimens whose casts circulated to other museums
- **HEADLINE SHAPE:** Before scanners, a mammal's teeth travelled the world as plaster — the plaster is still in the drawers, wearing the old names.
- **Why niche/untouched:** Cast collections were teaching infrastructure; digitisation prioritised skulls, and the cast drawers kept their paper labels.

#### Antler tine & beam record archives (trophy and cast-antler series) — `antler-tine-records` — score 7/10 (rank 35)
- **Score justification:** Record books scored antlers for a century; cast-antler series from known bucks (same animal, yearly sheds) are growth curves hiding in trophy rooms.
- **Keywords:** `antler records scoring archive data`; `cast antler collection known deer yearly`; `antler tine measurements dataset`; `trophy antler record book photographs`
- **Signature files:** .jpg, .csv, .pdf, .xls · **Gold words:** antler, tine, beam, record book
- **RAW:** Antler measurement sheets, score charts and shed-antler series photographs in record-book, agency and ranch collections
- **UNIT:** One antler set — record books hold tens of thousands of scored heads; known-buck shed series run 5–10 yearly sets per animal, one scoring protocol (Boone & Crockett / SCI / CIC)
- **LABEL GAP / SECOND RULER:** Score-book age/identity vs the same buck's known history and yearly sheds (second ruler)
- **ANCHOR:** Pen-raised known-age bucks with complete shed series
- **HEADLINE SHAPE:** The same buck drops a bigger crown every year and picks it up nowhere — hunters kept the crowns, and together they are his growth chart.
- **Why niche/untouched:** Trophy records were compiled for ranking, not biology; shed series sit with ranches and collectors, and agencies' measurement sheets were never pooled with them.

#### Horn growth-ring (annuli) age records — sheep, goats, ibex — `horn-annuli-age-records` — score 7/10 (rank 36)
- **Score justification:** Bighorn/ibex ages are read off horn rings at check stations; the ring counts were validated on a few known-age herds and then applied continent-wide.
- **Keywords:** `horn annuli age bighorn sheep data`; `horn growth ring ageing ibex records`; `horn segment measurements archive`; `mountain goat horn age validation study`
- **Signature files:** .jpg, .csv, .pdf, .xls · **Gold words:** horn, annuli, growth ring, age
- **RAW:** Horn photographs, segment-length measurement sheets and annuli counts in agency and alpine-club collections
- **UNIT:** One horn — thousands of checked rams/ibex per jurisdiction across decades, tape-and-photo protocol
- **LABEL GAP / SECOND RULER:** Ring age vs cementum age and vs known age of marked animals (second rulers)
- **ANCHOR:** Known-age marked herds (e.g. Ram Mountain bighorns) as the anchor
- **HEADLINE SHAPE:** A ram wears its birthdays as rings on its horns — check stations have read them for decades and filed the readings by district.
- **Why niche/untouched:** Horn ageing is agency routine in a dozen jurisdictions with a dozen filing systems; the validation herds are famous, the routine counts unexamined.

#### Bite-mark & tooth-pit records (predation and forensic) — `bite-mark-records` — score 6/10 (rank 47)
- **Score justification:** Tooth-pit spacing on bones identifies the predator in fossil and modern kill studies; reference bite sets are few and lab-local — real but thin, hence 6.
- **Keywords:** `bite mark tooth pit measurements predator`; `tooth mark bone identification data`; `bite mark forensic animal reference`; `predator tooth pit spacing study`
- **Signature files:** .jpg, .csv, .pdf · **Gold words:** bite mark, tooth pit, tooth mark, predation
- **RAW:** Bite/tooth-pit photographs and spacing measurements on bone, from taphonomy labs and kill-site studies
- **UNIT:** One bitten bone — hundreds per taphonomy reference set, calliper protocol
- **LABEL GAP / SECOND RULER:** Biter called from pit spacing vs DNA/feeding-trial bites by known animals (second ruler)
- **ANCHOR:** Feeding-trial bones from known captive predators
- **HEADLINE SHAPE:** The spacing of two punctures in bone can name the jaws that made them — palaeontologists and wardens measure the same holes and never compare notes.
- **Why niche/untouched:** Bite-mark reference work is split between fossil taphonomy and wildlife forensics, each with small private reference sets.

#### Bat wing venation & membrane pattern archives — `bat-wing-venation` — score 7/10 (rank 37)
- **Score justification:** Wing veins and membrane scars ID bats in the hand; banding-era wing photographs and venation drawings sit in chiroptera collections, pre-dating the DNA revisions of bat taxonomy.
- **Keywords:** `bat wing venation identification`; `bat wing membrane pattern photographs`; `bat wing morphology archive specimens`; `chiroptera wing vein pattern study`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** wing, venation, bat, membrane
- **RAW:** Spread-wing photographs and venation tracings in bat research and museum collections
- **UNIT:** One wing — thousands of banded bats per long-term study, dozens of species per regional collection, wing-against-light photo protocol
- **LABEL GAP / SECOND RULER:** Wing-based species ID vs DNA barcode of the same banded bat (second ruler)
- **ANCHOR:** Banding records tying wing photos to recaptures
- **HEADLINE SHAPE:** A bat's wing is a hand with the fingers stretched into a sail — the veins map like a palm print, and banders photographed them for decades.
- **Why niche/untouched:** Bat taxonomy was rebuilt by DNA while the wing-photo files of the banding era stayed with their collectors; nobody re-ran the old wings against the new names.

### F. Faces, ears, eyes, scars, tails & whiskers

#### Primate & chimpanzee face-pattern ID archives — `primate-face-pattern-archives` — score 8/10 (rank 23)
- **Score justification:** Chimp faces were ID'd by human eye at Gombe/Taï for 60 years; ChimpFace-era ML now trains on scraped sets while the sites' own portrait archives stay home.
- **Keywords:** `chimpanzee face recognition archive`; `primate individual identification photographs`; `chimpanzee ID cards Gombe archive`; `ape face pattern database`
- **Signature files:** .jpg, .tif, .csv · **Gold words:** face, chimpanzee, identification, portrait
- **RAW:** Portrait ID photographs and face-description cards from long-term primate field sites
- **UNIT:** One face — hundreds of known individuals per site (Gombe since 1960), thousands across sites, portrait protocol
- **LABEL GAP / SECOND RULER:** Face ID vs genetic ID from faecal DNA of the same chimps (second ruler)
- **ANCHOR:** Known-pedigree individuals at the long-term sites
- **HEADLINE SHAPE:** Researchers at Gombe know two hundred chimpanzee faces the way you know your family's — the portrait files that taught them are still at the field stations.
- **Why niche/untouched:** Face archives are field-site patrimony; the ML community built its own small scraped datasets rather than joining the sites' sixty years of portraits.

#### Whisker-spot (vibrissae) pattern catalogues — lions & pinnipeds — `whisker-spot-patterns` — score 9/10 (rank 7)
- **Score justification:** Pennycuick & Rudnai's 1970 lion method is pure pattern: dot maps of whisker follicles, still used in Kruger/India (WII's Lion software) and re-invented for sea lions — three literatures, one geometry, zero joining.
- **Keywords:** `whisker spot pattern lion identification`; `vibrissae pattern sea lion identification`; `lion whisker spot catalogue archive`; `whisker pattern individual identification data`
- **Signature files:** .jpg, .csv, .pdf · **Gold words:** whisker, vibrissae, spot pattern, lion
- **RAW:** Whisker-spot dot maps and muzzle photographs in lion and pinniped ID catalogues
- **UNIT:** One muzzle — hundreds of lions per park catalogue (method since 1970), pinniped sets of 50–1,000, dot-map protocol
- **LABEL GAP / SECOND RULER:** Whisker ID vs scar/ear-mark ID and genetic ID in the same individuals (second rulers)
- **ANCHOR:** Australian sea lion known-individual sets used to validate the method (99% pattern uniqueness at n=50)
- **HEADLINE SHAPE:** A lion's whisker dots are a star chart printed on its muzzle — rangers have read the same chart since 1970 and kept it park by park.
- **Why niche/untouched:** The lion, sea-lion and seal whisker literatures cite different ancestors and hold separate catalogues; the shared point-pattern geometry has never been run across them.

#### Vibrissae follicle & mystacial pad maps (small mammals & pinnipeds) — `vibrissae-follicle-maps` — score 6/10 (rank 48)
- **Score justification:** Whisker follicle arrangements are mapped whisker-by-whisker in neuroscience (barrel cortex) and pinniped sensory labs — deep data, narrow archives, hence 6.
- **Keywords:** `vibrissae follicle map mystacial pad`; `whisker follicle arrangement pattern study`; `mystacial vibrissae map seal rodent`; `whisker identity follicle archive`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** vibrissae, follicle, mystacial, whisker map
- **RAW:** Follicle maps and mystacial-pad photographs/drawings from sensory-neuroscience and pinniped labs
- **UNIT:** One whisker pad — tens to hundreds of mapped individuals per lab across a dozen species, dissection/photo protocol
- **LABEL GAP / SECOND RULER:** Follicle-map identity vs the same animal's whisker-spot photo ID (second ruler — two readings of one pad)
- **ANCHOR:** Lab colonies where the same individuals are mapped and photographed
- **HEADLINE SHAPE:** Every whisker has an address, and the brain keeps a map of the addresses — the address books are drawn lab by lab and never compared across species.
- **Why niche/untouched:** A methods detail inside neuroscience papers; the comparative pattern data was never the point of any single lab, so nobody assembled it.

#### Livestock iris-pattern ID records — `livestock-iris-patterns` — score 7/10 (rank 38)
- **Score justification:** Iris ID was piloted for cattle/horses in the 2000s (IrisScan-era trials) and abandoned for RFID — the trial image sets are stranded pilots, perfect hunter shape.
- **Keywords:** `cattle iris recognition identification trial`; `horse iris pattern identification system`; `livestock iris scan database archive`; `iris biometric livestock study images`
- **Signature files:** .jpg, .bmp, .csv, .pdf · **Gold words:** iris, livestock, identification, biometric
- **RAW:** Iris photographs and match-score files from livestock biometric pilot trials (universities, defunct startups)
- **UNIT:** One iris — hundreds to thousands of animals per trial series, fixed-camera protocol
- **LABEL GAP / SECOND RULER:** Iris match vs RFID/DNA identity of the same animals (second ruler)
- **ANCHOR:** Trial herds with full tag records
- **HEADLINE SHAPE:** For a few years, cows were going to log in with their eyes — the iris trials were run, photographed, and shelved when ear tags won.
- **Why niche/untouched:** Pilot-era data lives with defunct vendors and thesis appendices; the livestock-biometrics literature cites the trials without their image sets ever surfacing.

#### Ear-notch & ear-punch record systems (livestock and wildlife) — `ear-notch-punch-registries` — score 7/10 (rank 39)
- **Score justification:** The pig litter-notch system and cattle notch codes are pattern languages recorded on registration cards for a century — applied marks, but archived like print collections.
- **Keywords:** `ear notch system pig litter identification records`; `cattle ear notch registration archive`; `ear punch code wildlife marking records`; `ear notching identification chart historical`
- **Signature files:** .jpg, .pdf, .csv · **Gold words:** ear notch, ear punch, notch code, marking
- **RAW:** Ear-notch diagrams on registration cards, breed-association records and wildlife marking logs
- **UNIT:** One notched ear — millions of pigs/cattle registered under notch codes since the early 1900s, standard notch-position charts
- **LABEL GAP / SECOND RULER:** Notch code as read from the card vs the animal's pedigree/DNA record (second ruler)
- **ANCHOR:** Breed associations' master registration books
- **HEADLINE SHAPE:** A pig's ear is punched with its litter number like a train ticket — the ticket stubs fill a century of farm record books.
- **Why niche/untouched:** Notch systems are taught in every animal-science course and archived nowhere centrally; association card files are the only corpus and they are paper.

#### Spotted hyena ear-notch & spot ID archives — `hyena-ear-notch-id` — score 7/10 (rank 40)
- **Score justification:** Hyena ID combines natural ear notches, spots and scars — the Mara/Talek clan archives run since 1979 with drawn ear diagrams per animal.
- **Keywords:** `spotted hyena ear notch identification`; `hyena individual identification ear diagrams`; `Mara hyena project ID archive`; `hyena spot pattern individual recognition`
- **Signature files:** .jpg, .pdf, .csv · **Gold words:** hyena, ear notch, identification, clan
- **RAW:** Drawn ear-notch diagrams, spot photos and ID files from long-term hyena projects
- **UNIT:** One ear/flank — hundreds of known hyenas in the Mara archive since 1979, dozens in Ngorongoro and other clan studies, diagram protocol
- **LABEL GAP / SECOND RULER:** Ear/spot ID vs genetic ID from darting samples of the same hyenas (second ruler)
- **ANCHOR:** Known-pedigree clan members (births observed)
- **HEADLINE SHAPE:** A hyena's torn ear is its signature, drawn by hand into the clan file the day it is first recognised.
- **Why niche/untouched:** Clan archives are single-lab treasures (the Mara files span 45 years); no second clan's ear diagrams have ever been compared with them.

#### Scar & wound-pattern photo-ID archives (cross-species) — `scar-based-photo-id` — score 7/10 (rank 41)
- **Score justification:** Scars are the accidental ID system — shark-bite scars on seals, propeller scars on manatees/dugongs, fight scars on hippos — each programme sketches them alone.
- **Keywords:** `scar based photo identification animals`; `shark bite scar identification seal archive`; `propeller scar manatee dugong identification`; `wound pattern individual identification photographs`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** scar, wound, photo-id, sketch
- **RAW:** Scar sketches and wound photographs in photo-ID programme files across taxa
- **UNIT:** One scar pattern — hundreds to thousands of individuals per programme, sketch-then-photo protocol
- **LABEL GAP / SECOND RULER:** Scar ID vs tag/genetic ID recorded at the same encounters (second ruler)
- **ANCHOR:** Rescue/rehab animals with known identity and dated wound photos
- **HEADLINE SHAPE:** An animal's worst day becomes its ID card — the scar sketches are filed species by species, programme by programme.
- **Why niche/untouched:** Scar ID is always the backup system inside another programme's catalogue, never extracted or compared as a pattern archive in its own right.

#### Tail pattern & tail-ring ID systems (lemurs, raccoons, cats, marine mammals) — `tail-pattern-systems` — score 6/10 (rank 49)
- **Score justification:** Tail rings/notches close many ID calls (cheetah tail tips, lemur rings, dolphin tail stocks) but are recorded as a field inside other catalogues — thinnest standalone archive here, hence 6.
- **Keywords:** `tail ring pattern identification animal`; `lemur tail pattern individual identification`; `tail notch identification catalogue`; `cheetah tail tip pattern ID`
- **Signature files:** .jpg, .pdf, .csv · **Gold words:** tail, ring pattern, notch, identification
- **RAW:** Tail photographs and ring/notch diagrams inside multi-feature ID catalogues
- **UNIT:** One tail — hundreds of individuals per host catalogue, photo protocol shared with the host system
- **LABEL GAP / SECOND RULER:** Tail ID vs the host catalogue's primary feature (flank/face) for the same animal (second ruler)
- **ANCHOR:** Catalogues where tail photos were taken at every encounter (cheetah, dolphin sets)
- **HEADLINE SHAPE:** Half of a cheetah's name is written on the last white rings of its tail — tail patterns are everyone's second clue and nobody's archive.
- **Why niche/untouched:** Tail data exists only as a column in other systems' files; a tail-first pass over those files has never been run.

### G. Hair & applied-mark pattern atlases

#### Mammal guard-hair scale casts & hair atlases (wildlife forensics) — `guard-hair-scale-casts` — score 9/10 (rank 8)
- **Score justification:** The Texas atlas alone covers 150+ species with SEM scale images; ZSI Kolkata, FBI/USFWS-style labs and Brunner & Coman built parallel atlases on three continents that cite different standards.
- **Keywords:** `guard hair scale cast identification atlas`; `mammal hair atlas SEM scale pattern`; `hair identification key mammals download`; `trichotaxonomy guard hair microphotographs`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** guard hair, scale cast, trichotaxonomy, cuticular
- **RAW:** Cuticular scale casts (gelatin/cellulose impressions), SEM surface images and photomicrographs in forensic hair atlases
- **UNIT:** One hair — 150+ species in the Texas atlas, 100+ in the Indian and Australian atlases, one cast-and-mount protocol per atlas tradition
- **LABEL GAP / SECOND RULER:** Species called from scale cast vs DNA barcoding of the same hair/specimen (second ruler)
- **ANCHOR:** Museum-vouchered hairs (atlas specimens tied to skins/skulls)
- **HEADLINE SHAPE:** A single guard hair carries a scale pattern like a fingerprint — forensic atlases were built continent by continent and never checked against each other.
- **Why niche/untouched:** Hair ID is a forensic service literature: regional atlases (Texas 2009, ZSI series, Brunner & Coman 1974) each keyed their own fauna with their own scale vocabulary.

#### Hair medulla & cross-section pattern atlases — `hair-medulla-cross-sections` — score 7/10 (rank 42)
- **Score justification:** The second preparation of forensic hair work: medulla types and cross-section shapes keyed separately from scale casts, often by different authors for the same fauna.
- **Keywords:** `hair medulla pattern identification mammals`; `hair cross section shape atlas`; `medullary index mammal hair data`; `hair microscopy medulla types archive`
- **Signature files:** .jpg, .tif, .pdf, .csv · **Gold words:** medulla, cross section, hair, medullary
- **RAW:** Whole-mount medulla photomicrographs and hair cross-section images with medullary-index tables
- **UNIT:** One hair section — dozens to 150+ species per atlas, sectioning protocol
- **LABEL GAP / SECOND RULER:** Medulla-based species call vs scale-cast call on the same hairs (second ruler — the two preparations audit each other)
- **ANCHOR:** Vouchered museum hairs sectioned and cast in parallel in the classic atlases
- **HEADLINE SHAPE:** Cut a hair across and it shows a tiny patterned core — a second fingerprint inside the first, keyed in separate books.
- **Why niche/untouched:** Medulla/cross-section data rides inside the same regional atlases as the casts but was tabulated separately and never joined across regions either.

#### Lab-animal marking-pattern records (ear punch, toe clip, tattoo archives) — `lab-animal-marking-records` — score 6/10 (rank 50)
- **Score justification:** Colonies marked animals by punch/clip codes for a century; the marking logs of famous long-lived colonies are identity infrastructure that outlived the experiments — archival, hence 6.
- **Keywords:** `laboratory animal ear punch marking records`; `toe clip marking code archive`; `mouse colony marking system historical`; `animal tattoo identification colony records`
- **Signature files:** .pdf, .jpg, .csv · **Gold words:** ear punch, toe clip, tattoo, marking
- **RAW:** Marking code charts and colony marking logs from long-running laboratory and field colonies
- **UNIT:** One marked animal — thousands per colony across decades, standard punch-position code charts (several rival charts)
- **LABEL GAP / SECOND RULER:** Mark as logged vs genotype/pedigree of the same animal in the colony records (second ruler)
- **ANCHOR:** Colonies with complete pedigrees (e.g. classic mouse/rat colonies)
- **HEADLINE SHAPE:** Generations of lab mice were named by holes punched in their ears — the punch charts are a pattern language filed with the colony books.
- **Why niche/untouched:** Marking charts were standardised locally and published as methods figures; the logs themselves are institutional archives, consulted by nobody outside the colony.
