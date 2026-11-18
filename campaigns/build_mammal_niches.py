#!/usr/bin/env python3
"""Build mammal_niches.json + MAMMAL-NICHES-50.md — the MAMMAL-GRAIN
niche registry (Atharva's correction, 2026-11-18: he meant niche
domains at the grain of "paws and fingerprint analysis of mammals
and all that" — NOT broad cross-domain fields. The broad 50-niche
registry was the wrong grain; this one is 50 niches inside ONE
intuitive world, mammals, each a specific body part, trace, print
or pattern system).

Why these systems are fertile (the pattern, stated in the MD too):
 (a) a RAW capture — print, cast, photo, scan, hair cast, X-ray —
     taken the SAME way across many individuals/species;
 (b) used for individual ID or age/sex/species reading, so labels
     exist but live in old catalogues, forensic atlases, photo-ID
     archives and museum cast collections — often on a SECOND RULER
     (DNA, tags, collars, dissection, known-age animals);
 (c) instantly HEADLINE-shaped — a layperson gets it in one
     sentence.

Canonical headline, VERIFIED 2026-11-18 (not just repeated):
koala fingerprints — Henneberg, Lambert & Leigh (1997), "Fingerprint
homoplasy: koalas and humans", Univ. of Adelaide: ~20 koalas, ink
prints + scanning electron microscopy; ridges "nearly identical" to
human in microscopic morphology, pattern organisation and individual
uniqueness; the authors themselves called a crime-scene mix-up
"extremely unlikely" and no documented confusion exists. The
registry uses the verified form: near-indistinguishable under the
microscope, never documented at a crime scene.

Excluded: mammal brains (landed) and rhino forearm centroid work
(landed) — rhino ear-notch/horn ID is a different system, allowed.
"""
import json

N = []
def add(*a): N.append(a)

# ---------- Family A: Skin prints — fingers, palms, pads & noses ----------
add("primate-fingerprints-dermatoglyphics","Primate fingerprints & dermatoglyphic archives","A. Skin prints — fingers, palms, pads & noses",9,
 "The original fingerprint science was built on animal prints too — Cummins-era dermatoglyphic collections cover dozens of primate species, ridge counts never re-joined across collections.",
 ["primate dermatoglyphics archive","ape monkey fingerprint ridge count data","dermatoglyphic collection photographs download","chimpanzee fingerprint identification study"],
 [".jpg",".tif",".pdf",".csv"], ["dermatoglyph","fingerprint","ridge count","triradius"],
 "Ink and rolled fingerprints, palm prints and dermatoglyphic tracings in anthropology and forensic collections",
 "One finger/palm — thousands of prints across dozens of primate species in the classic collections, one ink-print protocol",
 "Species/individual called from ridge pattern vs DNA taxonomy of the same zoo/museum animals (second ruler)",
 "Zoo studbooks and museum specimens tied to print cards",
 "Police once fingerprinted the chimps at a zoo to rule them out of a crime — the apes' prints were that close to ours.",
 "Dermatoglyphics was a mid-century industry whose collections sit in anthropology departments and forensic museums; genetics replaced it before its cross-species ridge data was ever pooled.")
add("koala-fingerprints","Koala fingerprint collections","A. Skin prints — fingers, palms, pads & noses",8,
 "Headline is perfect and verified (Henneberg 1997), but the known print population is small — one species, tens of documented individuals — so archive depth caps the score.",
 ["koala fingerprint print collection","koala dermatoglyphics images","Henneberg koala fingerprint data","marsupial fingerprint ridge study"],
 [".jpg",".tif",".pdf"], ["koala","fingerprint","ridge","homoplasy"],
 "Ink prints and SEM fingertip images from wildlife-park and university anatomy collections",
 "One fingertip — one species, tens of individuals in the published study, unknown numbers in zoo/wildlife-park files, one ink-print protocol",
 "Koala ridge pattern vs human prints in the same forensic reference files (the second ruler is our own fingerprint system)",
 "The 1997 Adelaide reference prints (Henneberg, Lambert & Leigh)",
 "A koala's fingerprint is nearly indistinguishable from a human's under a microscope — verified in 1997, and no, it has never actually turned up at a crime scene.",
 "One famous study, then near-silence: wildlife parks handle koalas daily and no print collection was ever built on the 1997 foundation.")
add("primate-palm-sole-dermatoglyphics","Primate & clinical palm/sole dermatoglyphics (atd angle archives)","A. Skin prints — fingers, palms, pads & noses",7,
 "Palmar atd angles and sole patterns fill medical-genetics archives (Down syndrome diagnostics era) plus primate atlases; two literatures never met.",
 ["palmar dermatoglyphics atd angle data","sole pattern dermatoglyphics archive","dermatoglyphics Down syndrome print collection","primate palm print atlas"],
 [".jpg",".pdf",".csv"], ["atd","palmar","sole","dermatoglyph"],
 "Palm and sole prints with measured atd angles and pattern maps, in clinical genetics files and primate atlases",
 "One palm/sole — thousands of clinical prints, hundreds of primate specimens, one measurement convention",
 "Pattern diagnosis from prints vs chromosome/DNA diagnosis of the same patients and species (second ruler)",
 "Karyotyped clinical series and museum primate material",
 "Doctors once read a baby's palm the way they now read its chromosomes — the angle in the palm was a genetic test.",
 "Clinical dermatoglyphics died the day karyotyping arrived; its print archives sit in medical-school files, unlinked to the primate dermatoglyphic collections that used the same measures.")
add("paw-pad-ridge-patterns","Paw-pad surface & ridge pattern atlases (bears, raccoons, carnivores)","A. Skin prints — fingers, palms, pads & noses",7,
 "Pad photos/casts are how trackers separate look-alike species; pad atlases are regional, hand-drawn era, never pooled.",
 ["paw pad identification atlas","bear paw pad photograph collection","animal footprint pad pattern guide","raccoon paw print dermatoglyphics"],
 [".jpg",".tif",".pdf"], ["pad","paw","plantar","track"],
 "Paw-pad photographs, casts and drawn pad maps in tracking atlases and museum collections",
 "One pad — dozens of carnivore/omnivore species per atlas, hundreds of specimens, standard pad-on-glass or cast protocol",
 "Species called from pad pattern vs the track/trail it came from and DNA from scat at the same site (second rulers)",
 "Zoo and museum specimens photographed pad-up",
 "A raccoon's hand looks eerily like a tiny human hand — and its palm print is in the tracking atlases to prove it.",
 "Tracking literature is a cottage world of regional guides; the pad reference photos behind them live in authors' and museums' files, not in any shared atlas.")
add("dog-nose-prints","Dog nose-print archives","A. Skin prints — fingers, palms, pads & noses",8,
 "Petersen took 350+ animal nose prints in 1922; kennel clubs and insurers ran nose-print registries for decades — paper archives, modern apps are rebuilding from zero.",
 ["dog nose print identification archive","canine nose print registry records","nose print kennel club registration","dog nose pattern dataset download"],
 [".jpg",".tif",".pdf",".csv"], ["nose print","noseprint","muzzle","canine nose"],
 "Ink nose prints on index cards and nose photographs in kennel-club, insurer and lab collections",
 "One nose — registries ran to thousands of dogs; the 2021 viability study re-proved uniqueness on 70 dogs / 19 breeds, one ink-or-camera protocol per era",
 "Nose pattern ID vs microchip/tag records for the same dogs (second ruler)",
 "Longitudinal re-prints of the same dog months apart (pattern invariance series)",
 "Your dog's nose print is its fingerprint — kennel clubs were filing them on index cards a century ago.",
 "Historic nose-print registries were paper and breed-club local; the smartphone-era startups each built tiny private datasets and none inherited the card archives.")
add("cattle-muzzle-prints","Cattle muzzle (nose) print registration archives","A. Skin prints — fingers, palms, pads & noses",9,
 "The biggest fingerprint-style archive in the animal world: Japan's Wagyu Registry has ink muzzle prints for 3M+ beef cattle since 1948 — and it is a paper/card system.",
 ["cattle muzzle print registration","wagyu nose print certificate archive","beppu nose print cattle identification","muzzle pattern cattle dataset"],
 [".jpg",".tif",".pdf",".csv"], ["muzzle","nose print","beppu","wagyu"],
 "Ink muzzle prints lifted on paper/cards at registration (before 4 months, again after 14 months in the Japanese system), plus modern muzzle photographs",
 "One muzzle — millions registered in Japan since 1948, thousands in Petersen-era and university series elsewhere, one ink-lift protocol",
 "Muzzle print ID vs ear-tag / RFID / DNA pedigree records for the same animals (second ruler)",
 "The Wagyu Registry Association's own registration certificates (nose print + pedigree on one card)",
 "Japan has fingerprinted its finest cattle by nose since 1948 — over three million cows, each with a print card like a criminal record.",
 "The registration archives are institutional paper; the computer-vision literature trains on a few hundred fresh photos and has never touched the historical card millions.")
add("sheep-goat-nose-prints","Sheep & goat nose-print and muzzle records","A. Skin prints — fingers, palms, pads & noses",6,
 "Same system as cattle, a tenth the attention: show and sale sheep/goats were nose-printed for identity in fraud disputes; records are society-level paper.",
 ["sheep nose print identification","goat muzzle print pattern study","nose print sheep sale identification","small ruminant noseprint dataset"],
 [".jpg",".pdf",".csv"], ["nose print","muzzle","sheep","goat"],
 "Ink nose prints and muzzle photographs in breed-society and agricultural-college collections",
 "One muzzle — hundreds to thousands per society/college series, same ink-lift protocol as cattle",
 "Nose ID vs ear-tag and tattoo records for the same animals (second ruler)",
 "Agricultural-college teaching series with known animals",
 "Sheep were nose-printed to catch show-ring fraud — the print proved the prize ram was a substitute.",
 "A footnote literature beside the cattle work; breed societies kept their own cards and no cross-society set was ever assembled.")
add("cat-nose-leather-patterns","Cat nose-leather pattern records","A. Skin prints — fingers, palms, pads & noses",6,
 "Pet-ID folklore says the cat nose is unique; the actual old evidence is thin vet/clinic photo files — a claim waiting for its archive, hence the lower score.",
 ["cat nose print unique identification","feline nose leather pattern photograph","cat noseprint registration","cat nose pattern study images"],
 [".jpg",".pdf"], ["nose leather","nose print","feline nose"],
 "Nose-leather photographs in vet-clinic, shelter and cattery files; a small patent-era print literature",
 "One nose — hundreds in scattered clinic/shelter photo sets, no standard protocol (that absence is itself the finding to test)",
 "Nose pattern vs microchip identity for the same cats (second ruler)",
 "Shelter intake photo series where chip ID is recorded",
 "Every cat's nose is said to be one of a kind — but unlike dogs and cattle, nobody ever built the card file to prove it.",
 "The claim circulates in pet culture with almost no archival base; any systematic clinic photo piles sit unexamined in shelter systems.")

# ---------- Family B: Tracks, paws & gait ----------
add("paw-track-morphometrics-fit","Paw-track morphometrics & FIT footprint archives","B. Tracks, paws & gait",9,
 "WildTrack's FIT extracts 120+ measures per print and reports >90% species/sex/age accuracy across 13+ species — yet each species training set lives with its project, captive-known prints are the rarest data in tracking.",
 ["footprint identification technology FIT dataset","animal track measurements csv download","WildTrack footprint database images","track morphometrics landmark data"],
 [".jpg",".csv",".xls"], ["footprint","track","FIT","morphometric"],
 "Footprint photographs taken to one ruler-and-slip protocol (WildTrack FIT and its predecessors), plus hand-measured track tables",
 "One print/trail — training sets of known captive individuals per species, field trails by the thousand, 13+ species with FIT algorithms",
 "Individual/sex/age called from print vs the known captive animal or collared wild animal that made it (second ruler)",
 "Captive-animal known-identity trail sets (the FIT training gold standard)",
 "A photograph of a footprint can name the tiger, its sex and its age — trackers always knew; the measurement files proving it sit project by project.",
 "FIT standardised the capture but not the custody: species datasets sit with NGOs, zoos and consultancies, and the pre-FIT hand-measured track tables were never digitised at all.")
add("plaster-track-cast-collections","Plaster track-cast museum collections","B. Tracks, paws & gait",8,
 "Museums hold drawers of plaster paw casts — snow leopard, wolf, lynx — made when casts were the data; catalogued as objects, never measured as a set.",
 ["plaster track cast collection museum","animal track casts catalogue","snow leopard track cast specimen","wolf footprint cast museum collection"],
 [".jpg",".tif",".csv",".pdf"], ["cast","plaster","track","footprint"],
 "Plaster and latex track casts with specimen labels in natural-history museum collections",
 "One cast — hundreds per large collection, dozens of species, one cast-making tradition across a century",
 "Species/sex on the cast label vs the cast re-measured today against FIT-style morphometrics (second ruler)",
 "Casts tied to collected specimens or known zoo animals",
 "Before cameras, scientists carried plaster to the snow and poured the footprint itself — museums still hold the drawers of poured paws.",
 "Cast collections were catalogued by accession, not by measurement; nobody has run a single morphometric pass across a museum's cast drawers.")
add("elephant-footprint-age","Elephant footprint age-estimation archives","B. Tracks, paws & gait",8,
 "Forefoot circumference converts to shoulder height and age; the calibration sets (known-age Amboseli elephants walking in sand) are small, old and priceless.",
 ["elephant footprint age estimation data","elephant forefoot circumference age","elephant track measurement archive","footprint shoulder height elephant study"],
 [".jpg",".csv",".xls",".pdf"], ["footprint","forefoot","circumference","age"],
 "Footprint photographs and forefoot-circumference measurement sheets from known-age elephant studies and ranger monitoring",
 "One footprint — calibration series from known-age individuals (Amboseli), monitoring trails by the thousand across Africa/Asia",
 "Age read from the footprint vs the elephant's known birth year in the long-term ID catalogues (second ruler)",
 "Amboseli known-age individuals measured directly",
 "You can read an elephant's age off the print its front foot leaves in the dust — if you have the calibration walks, and almost nobody kept them.",
 "The method is used by rangers everywhere; the underlying known-age measurement series live in a few theses and project files from the 1980s–2000s.")
add("bear-paw-mensuration","Bear paw mensuration & harvest track records","B. Tracks, paws & gait",7,
 "Agencies measured hind-foot length on harvested bears for a century to sex/age them; the ledgers predate DNA sexing and were never audited against it.",
 ["bear paw measurement harvest records","bear hind foot length sex identification","bear track measurement data archive","grizzly paw mensuration study"],
 [".csv",".xls",".pdf",".jpg"], ["paw","hind foot","mensuration","bear"],
 "Paw measurement cards/ledgers from harvest check stations, plus track-measurement tables in agency reports",
 "One paw — thousands of harvested bears per jurisdiction across decades, one measuring-board protocol per agency",
 "Sex/age from paw size vs DNA/tooth-cementum determination on the same bear (second ruler)",
 "Check-station bears with both paw cards and cementum ages",
 "A dead bear's back foot was measured to guess its sex — the guess was written down for fifty years before anyone checked it against DNA.",
 "Harvest records are jurisdiction paperwork; the paw-size rules in the hunting guides descend from ledgers nobody re-audited.")
add("canid-track-size-archives","Wolf & canid track-size survey archives","B. Tracks, paws & gait",7,
 "Wolf-vs-dog-vs-coyote by track size is a live forensic question in rewilding Europe/North America; survey track tables sit in agency PDFs.",
 ["wolf track measurements survey data","canid track size identification table","wolf dog track comparison measurements","snow track wolf survey archive"],
 [".csv",".pdf",".jpg",".xls"], ["track","wolf","canid","snow"],
 "Track measurement tables (length/width/gait) from wolf and carnivore snow surveys, agency reports and tracker archives",
 "One track set — thousands per national survey across decades, ruler-in-photo or calliper protocol",
 "Species called from the track vs DNA from scat/hair collected on the same survey line (second ruler)",
 "Tracks of known captive wolves, dogs and coyotes measured the same way",
 "A wolf and a big dog leave nearly the same footprint — the argument about which one crossed the farm is settled from tables nobody has pooled.",
 "Each country's monitoring programme publishes summary presence maps; the measurement-level track tables stay in project reports and trackers' notebooks.")
add("snow-track-gait-archives","Snow-track gait & stride archives (lynx, wolverine, mustelids)","B. Tracks, paws & gait",7,
 "Nordic snow-tracking transects recorded stride/gait patterns for decades — a designed comparable set, province by province.",
 ["snow tracking transect data archive","lynx track gait measurements","wolverine snow track survey records","animal track stride pattern data"],
 [".csv",".pdf",".jpg"], ["snow track","gait","stride","transect"],
 "Snow-transect record cards and gait diagrams from Nordic and boreal wildlife triangle / survey schemes",
 "One track crossing — tens of thousands of transect crossings per country across decades, standard route protocol",
 "Species from gait pattern vs camera/DNA confirmation in the same survey areas (second ruler)",
 "Finland's wildlife-triangle long-run series as the published benchmark",
 "In deep snow an animal writes its name in stride — surveyors read the same script every winter for forty years and filed it by province.",
 "Snow tracking is a Nordic institutional tradition with paper-era roots; digitisation happened province by province and the gait-level records were left behind the presence counts.")
add("hoof-cloven-track-systems","Hoof & cloven-track measurement systems (deer, livestock, poaching forensics)","B. Tracks, paws & gait",6,
 "Deer/sheep/goat/cattle slot measurements are poaching-case evidence; reference sets are police/lab-local and small, hence the score.",
 ["hoof print identification measurements","cloven hoof track deer sheep comparison","livestock track forensic identification","deer slot measurement data"],
 [".jpg",".pdf",".csv"], ["hoof","cloven","slot","track"],
 "Hoof-print photographs, casts and slot-measurement tables in forensic and game-warden reference sets",
 "One hoof print — hundreds per reference collection, dozens of ungulate species, ruler protocol",
 "Species called from the slot vs the animal carcass/DNA in the same poaching case (second ruler)",
 "Farm and zoo ungulates printed on known ground",
 "Two toes in the mud can put a poacher in court — if the reference prints for every hoofed suspect were ever gathered in one place.",
 "Hoof ID is casework knowledge held by wildlife forensic labs and wardens; their reference casts and photos were never published as a set.")
add("claw-mark-archives","Claw-mark & scratch-tree archives (bears, big cats)","B. Tracks, paws & gait",6,
 "Claw spacing on marked trees is measured in bear/cat studies plot by plot; a real system but the archives are thin and local, hence 6.",
 ["bear claw mark tree measurements","claw mark identification archive","big cat scratch mark tree data","claw spacing measurement study"],
 [".jpg",".csv",".pdf"], ["claw mark","scratch","mark tree"],
 "Photographs and spacing/height measurements of claw marks on trees and posts, from bear and big-cat field studies",
 "One marked tree — hundreds per study area, tape-and-photo protocol",
 "Species/individual suggested from claw spacing vs camera-trap photos at the same trees (second ruler)",
 "Marks made by known captive bears/cats on standard posts",
 "A bear signs the tree it rubs — the width of its claw strokes is a signature researchers measure and then file away study by study.",
 "Claw-mark data is a by-product of habitat studies; no cross-study archive of mark measurements exists.")

# ---------- Family C: Flukes, fins, ears & callosities — megafauna photo-ID ----------
add("whale-fluke-trailing-edge","Whale fluke trailing-edge photo-ID catalogues","C. Flukes, fins, ears & callosities",9,
 "39 North-Pacific catalogues were unified by Happywhale (27,956 individuals) — proof of value AND the narrowing: the un-joined remainder is film-era, Southern Ocean and non-humpback catalogues.",
 ["whale fluke photo identification catalogue","humpback fluke catalog archive download","sperm whale fluke catalogue photographs","fluke trailing edge identification collection"],
 [".jpg",".tif",".csv"], ["fluke","trailing edge","photo-id","catalogue"],
 "Fluke photographs (film-era prints/slides and digital) in regional whale research catalogues",
 "One fluke — tens of thousands of individuals globally; 39 catalogues in the North Pacific alone, one underside-photo protocol",
 "Fluke match vs genetic sample taken at the same encounter (second ruler)",
 "The Happywhale/NPPID unified North Pacific set as the benchmark of what joining yields",
 "Every humpback's tail is a fingerprint in black and white — the world spent 50 years photographing them and is only now joining the albums.",
 "Happywhale joined the North Pacific digital era; the pre-digital slide cabinets, the Southern Ocean and Atlantic regional catalogues, and sperm-whale fluke sets remain separate piles.")
add("dolphin-dorsal-fin-notches","Dolphin dorsal-fin notch catalogues","C. Flukes, fins, ears & callosities",9,
 "Sarasota alone holds 5,000+ fin images since 1970 and GoMDIS joins 35 Gulf catalogues (23,444 animals) — outside the Gulf, hundreds of FinBase-era catalogues never joined anything.",
 ["dolphin dorsal fin catalogue download","bottlenose dolphin photo ID FinBase","dorsal fin notch identification archive","dolphin fin catalogue photographs"],
 [".jpg",".tif",".csv",".mdb"], ["dorsal fin","finbase","notch","photo-id"],
 "Dorsal-fin photographs and FinBase/Access-era catalogue databases on lab and institute sites",
 "One fin — hundreds of regional catalogues, hundreds to thousands of individuals each, one trailing-edge protocol since Würsig 1977",
 "Fin ID vs freeze-brand/tag/genetic identity of the same dolphin (second ruler)",
 "Sarasota's known-history individuals (births/deaths observed since 1970)",
 "A dolphin's fin collects nicks like a passport collects stamps — labs have filed the passports bay by bay for fifty years.",
 "FinBase standardised hundreds of local catalogues on desktop databases that were never networked; GoMDIS proved joining works for one gulf and stopped there.")
add("right-whale-callosity-patterns","Right-whale head callosity catalogues","C. Flukes, fins, ears & callosities",8,
 "The callosity pattern is read from aerial photos since the 1970s; the North Atlantic consortium catalogue is curated but the southern-hemisphere catalogues (Argentina, South Africa, Australia) grew separately.",
 ["right whale callosity pattern identification","right whale photo identification catalog","whale head callosity photographs archive","Eubalaena individual catalogue"],
 [".jpg",".tif",".csv"], ["callosity","right whale","photo-id","head pattern"],
 "Aerial and boat photographs of head callosity patterns in consortium and regional catalogues",
 "One head — ~400 living North Atlantic individuals, thousands in southern catalogues, aerial-photo protocol since Payne's 1970s work",
 "Callosity ID vs genetic profiles from biopsy of the same whales (second ruler)",
 "The North Atlantic Right Whale Consortium catalogue as the curated anchor",
 "The rough white patches on a right whale's head are as fixed as a face — whale watchers have read them from planes since the seventies.",
 "Three ocean basins built three callosity catalogues in three institutions; cross-basin matching (whales do cross) rests on personal correspondence, not a joined archive.")
add("manatee-photo-id-scars","Manatee scar & tail photo-ID system archives","C. Flukes, fins, ears & callosities",8,
 "Florida's MIPS system has matched manatees by scars/tail notches since the 1970s — a state-run pattern archive with sketch-era roots, mirrored by separate Caribbean/Brazil sets.",
 ["manatee photo identification system MIPS","manatee scar catalogue identification","manatee tail notch photographs","manatee individual identification database"],
 [".jpg",".tif",".pdf",".csv"], ["manatee","scar","MIPS","tail notch"],
 "Underwater photographs and hand-drawn scar sketches in the Manatee Photo-ID System and sister programmes",
 "One manatee — thousands of individuals in Florida alone since the 1970s, sketch-then-photo protocol",
 "Scar-pattern ID vs PIT-tag/genetic identity recorded at rescue/health assessments (second ruler)",
 "Rescued manatees whose identity is known absolutely at release",
 "A manatee is known by its propeller scars — the state of Florida keeps a mugshot file, part sketchbook, part database.",
 "MIPS is an agency system with restricted doors; the sketch-era archive and the non-Florida programmes were never part of any public pattern set.")
add("elephant-ear-edge-veins","Elephant ear edge, tear & vein ID archives","C. Flukes, fins, ears & callosities",9,
 "Amboseli has ID'd 1,600+ elephants since 1972 by ear tears/holes/veins on physical ID cards; every long-term site (Gorongosa, Mara, Samburu…) keeps its own card tradition.",
 ["elephant ear identification cards archive","Amboseli elephant ID ear tears","elephant individual identification ear pattern","elephantvoices who's who database ear"],
 [".jpg",".tif",".pdf",".csv"], ["ear","elephant","ID card","notch"],
 "Photographic ear ID cards (physical card files, later digital) recording ear edge tears, holes and vein patterns, per long-term study site",
 "One ear — 1,600+ known individuals at Amboseli, hundreds to thousands per other site, one card-and-photo protocol per site tradition",
 "Ear ID vs DNA from dung/biopsy and vs tusk/body marks recorded on the same card (second rulers)",
 "Amboseli's known-birth individuals (exact ages since 1972)",
 "An elephant's ear is a torn, veined map no other elephant shares — researchers have carried its ID cards in Land Cruiser gloveboxes for fifty years.",
 "The ID-card tradition is per-site and partly still physical; Gorongosa's Who's Who went digital behind a password, Amboseli's cards span paper and digital, and no cross-site ear archive exists.")
add("elephant-tusk-patterns","Elephant tusk shape & configuration records","C. Flukes, fins, ears & callosities",7,
 "Tusk shape is the second ID feature on every elephant card and the trait poaching selects on (Gorongosa tusklessness) — but it changes with breakage, capping the score.",
 ["elephant tusk shape identification records","tusk configuration individual elephant data","tuskless elephant registry Gorongosa","elephant tusk pattern photographs"],
 [".jpg",".csv",".pdf"], ["tusk","tuskless","configuration","elephant"],
 "Tusk shape/configuration fields and photographs inside elephant ID databases and ivory-seizure records",
 "One tusk pair — thousands of registered individuals across site databases, card-description protocol",
 "Tusk ID vs ear ID on the same individual (second ruler — two pattern systems, one animal)",
 "Seized-ivory DNA assignments back to populations (the forensic anchor)",
 "An elephant's tusks are as personal as handwriting — and in one park, war selected the elephants whose tusks never grew.",
 "Tusk data rides inside ear-ID databases and seizure labs, never extracted as its own cross-site pattern record.")
add("rhino-ear-notch-horn-profiles","Rhino ear-notch & horn-profile ID records","C. Flukes, fins, ears & callosities",8,
 "Distinct from the landed rhino forearm work: this is the applied ID system — ear notches cut by managers plus horn silhouette profiles, kept per-reserve in sighting books. (Forearm centroid work excluded.)",
 ["rhino ear notch identification records","rhino horn profile individual identification","rhino sighting book ear notch archive","rhino ID database ear pattern"],
 [".jpg",".csv",".pdf"], ["ear notch","horn profile","rhino","identification"],
 "Ear-notch diagrams, horn-profile photographs and sighting-book pages from reserves and rhino monitoring programmes",
 "One rhino — hundreds per reserve, thousands across programmes, notch-code + profile-photo protocol",
 "Notch/horn ID vs DNA from ear-tissue taken at the notching itself, and horn DNA (RhODIS) (second rulers)",
 "RhODIS forensic horn-DNA database as the cross-check anchor",
 "Rhino managers cut a code into the ear and read the horn's silhouette like a skyline — each reserve keeps its own skyline book.",
 "Ear-notching is universal practice and per-reserve paperwork; horn profiles accumulate in monitoring photos that no cross-reserve system ingests.")
add("pinniped-pelage-patterns","Pinniped pelage-pattern photo-ID (ringed & monk seals)","C. Flukes, fins, ears & callosities",8,
 "Saimaa's SealID set (57 seals, 2,080 images) proved a pelage dataset can be published — and exposed how many seal colonies still match patterns by eye from slide boxes.",
 ["seal pelage pattern photo identification","ringed seal fur pattern catalogue","monk seal photo identification catalog","seal coat pattern individual identification"],
 [".jpg",".tif",".csv"], ["pelage","seal","fur pattern","photo-id"],
 "Seal flank photographs (slides, then digital) in colony photo-ID catalogues",
 "One flank pattern — hundreds of individuals per colony catalogue (Saimaa ~400 animals; Cap Blanc monk seals since 1993), haul-out photo protocol",
 "Pelage ID vs flipper-tag / telemetry identity of the same seal (second ruler)",
 "SealID's expert-matched public benchmark set (57 individuals, 2,080 images)",
 "A ringed seal wears a fingerprint made of rings over its whole body — no two seals have ever worn the same one.",
 "Each seal colony's catalogue belongs to its research group; slide-era catalogues (monk seals 1990s) predate the ML datasets and were never digitised into them.")

# ---------- Family D: Coat patterns — stripes, rosettes, spots & scales ----------
add("tiger-stripe-catalogues","Tiger stripe-pattern camera-trap catalogues","D. Coat patterns — stripes, rosettes, spots & scales",8,
 "Every tiger's stripes are mapped by camera traps nationally, but the catalogues are security-sealed per country/programme; the pattern data behind published counts is the stranded layer.",
 ["tiger stripe pattern identification catalogue","camera trap tiger individual identification data","tiger stripe database photographs","Panthera tigris stripe pattern archive"],
 [".jpg",".tif",".csv"], ["stripe","tiger","camera trap","individual"],
 "Camera-trap flank photographs and stripe-matching files in national and NGO tiger programmes",
 "One flank — thousands of individuals across range countries, standard paired-camera protocol",
 "Stripe ID vs genetic ID from scat collected in the same grids (second ruler)",
 "India's national tiger estimation archive as the (restricted) anchor set",
 "No two tigers share a stripe map — countries count their tigers from stripe photographs and then lock the photographs away.",
 "Counts are published, pattern files are not; each programme's catalogue is a silo justified by poaching risk, so cross-border tigers are matched by personal contact.")
add("leopard-jaguar-rosettes","Leopard & jaguar rosette catalogues","D. Coat patterns — stripes, rosettes, spots & scales",8,
 "Rosettes ID individuals across hundreds of separate camera-trap studies; Wildbook ingests some, the long tail of thesis-era catalogues is the niche.",
 ["jaguar rosette identification catalogue","leopard rosette pattern camera trap data","jaguar individual identification photographs","leopard spot pattern archive"],
 [".jpg",".tif",".csv"], ["rosette","jaguar","leopard","camera trap"],
 "Camera-trap rosette photographs and matching spreadsheets from individual study sites",
 "One rosette flank — dozens to hundreds of individuals per study, hundreds of studies, paired-camera protocol",
 "Rosette ID vs GPS-collar/genetic identity in the same study animals (second ruler)",
 "Long-term sites (e.g. Cockscomb jaguars, since the 1980s) with known individuals",
 "A jaguar's rosettes are a star-map only it wears — every valley's researchers keep their own atlas of the same sky.",
 "Camera-trap science is study-shaped: each project publishes a density estimate and keeps its rosette catalogue in a drawer or a dead laptop.")
add("zebra-stripe-patterns","Zebra stripe-pattern ID archives","D. Coat patterns — stripes, rosettes, spots & scales",8,
 "Stripe ID began with hand-drawn zebra codes in the 1960s (Petersen 1972); Grevy's/plains catalogues per ecosystem, plus the famous mare-foal recognition experiments' photo files.",
 ["zebra stripe pattern identification archive","zebra individual stripe code catalogue","Grevy zebra stripe database photographs","plains zebra photo identification"],
 [".jpg",".tif",".csv",".pdf"], ["stripe","zebra","stripe code","photo-id"],
 "Stripe photographs and hand-coded stripe diagrams from ecosystem monitoring programmes",
 "One flank/shoulder pattern — thousands of individuals in the large ecosystem catalogues, photo protocol since the film era",
 "Stripe ID vs ear-notch/collar/genetic identity in the same herds (second ruler)",
 "Long-term known-individual herds (e.g. Grevy's in Kenya) as anchor",
 "A zebra's stripes are a barcode its own foal learns by heart — scientists have been photocopying the barcodes since the sixties.",
 "Zebra ID moved from drawn codes to StripeSpotter-era software per project; the drawn-code archives and most ecosystem catalogues were never merged.")
add("giraffe-coat-patterns","Giraffe coat-pattern ID archives","D. Coat patterns — stripes, rosettes, spots & scales",8,
 "Giraffe spots are lifelong and individual; tower-by-tower catalogues across Africa, Wildbook for Giraffe ingests a fraction — the rest are ranger/guide photo files.",
 ["giraffe coat pattern identification catalogue","giraffe spot pattern individual database","giraffe photo identification archive","Masai giraffe pattern photographs"],
 [".jpg",".tif",".csv"], ["coat pattern","giraffe","spot","photo-id"],
 "Flank/torso coat-pattern photographs in reserve and research catalogues",
 "One torso pattern — hundreds to thousands per population catalogue, right-flank photo convention",
 "Coat ID vs GPS-collar and genetic identity in monitored populations (second ruler)",
 "Long-term Serengeti/Murchison known-individual sets",
 "A giraffe wears its name in patches big enough to read from a safari vehicle — every reserve reads a different page.",
 "Tourism and research both photograph giraffes constantly; the ID catalogues sit with individual reserves and guides' hard drives, Wildbook coverage notwithstanding.")
add("cheetah-spot-patterns","Cheetah spot & tear-mark ID files","D. Coat patterns — stripes, rosettes, spots & scales",7,
 "Cheetah ID leans on spot patterns plus tail rings and tear marks; Serengeti's decades of ID photos are one project, farm-level Namibian files are another world.",
 ["cheetah spot pattern identification","cheetah individual identification photographs archive","cheetah tear marks tail rings ID","Serengeti cheetah project identification data"],
 [".jpg",".tif",".csv"], ["spot","cheetah","tear mark","identification"],
 "Spot-pattern ID photographs and drawn ID sheets from long-term cheetah projects and farmer/researcher files",
 "One flank/face — hundreds of known individuals in the Serengeti project alone since the 1970s, photo protocol",
 "Spot ID vs radio-collar/genetic identity in the same animals (second ruler)",
 "Serengeti Cheetah Project's known-pedigree individuals",
 "A cheetah can be told from its spots and the black tear-lines on its face — the projects that learned the faces never shared the album.",
 "Fewer, larger projects than leopards, but the same shape: ID albums are project property, and the pre-digital Serengeti sheets are one fire away from loss.")
add("snow-leopard-rosettes","Snow leopard rosette & tail catalogues","D. Coat patterns — stripes, rosettes, spots & scales",7,
 "The hardest coat catalogue: 12 range countries, tiny densities, every programme's rosette files precious and separate; scores capped by access and sample size.",
 ["snow leopard rosette identification catalogue","snow leopard camera trap individual data","snow leopard spot pattern photographs","Panthera uncia identification archive"],
 [".jpg",".tif",".csv"], ["rosette","snow leopard","camera trap","individual"],
 "Camera-trap rosette and tail photographs in range-country programme files",
 "One flank — tens of individuals per valley study, hundreds range-wide in files, paired-camera protocol",
 "Rosette ID vs genetic ID from the large scat programmes (second ruler)",
 "Mongolia's long-term collared population as anchor",
 "The ghost cat's coat is the only name it answers to — twelve countries keep twelve partial ghost albums.",
 "Snow leopard science is grant-by-grant and valley-by-valley; the global programme publishes status maps, not the pattern files beneath them.")
add("painted-dog-coat-patterns","African wild dog coat-pattern ID archives","D. Coat patterns — stripes, rosettes, spots & scales",7,
 "No two painted dogs share a coat; pack catalogues per park are guide-and-researcher photo books, some running since the 1990s.",
 ["African wild dog coat pattern identification","painted dog individual identification photographs","wild dog pack catalogue archive","Lycaon pictus pattern ID"],
 [".jpg",".tif",".csv"], ["coat","painted dog","wild dog","pattern"],
 "Coat-pattern ID photographs and pack catalogues from parks and den-monitoring projects",
 "One flank — dozens per pack, hundreds per park catalogue, photo protocol at dens and sightings",
 "Coat ID vs ear-notch/collar identity in monitored packs (second ruler)",
 "Long-term Selous/Kruger known packs",
 "Every painted dog is a one-off painting — rangers name the paintings, and the name-books stay in the parks.",
 "Pack catalogues are working tools of individual parks and guides; when a project ends, its coat archive typically ends with it.")
add("pangolin-scale-patterns","Pangolin scale-pattern & seizure ID records","D. Coat patterns — stripes, rosettes, spots & scales",7,
 "Pangolin scales carry individual pattern and are the seized commodity itself — rescue-centre ID photos and seizure inventories are two unjoined pattern archives.",
 ["pangolin scale pattern identification","pangolin individual identification photographs","pangolin seizure scale inventory records","pangolin scale pattern study"],
 [".jpg",".csv",".pdf"], ["scale","pangolin","pattern","seizure"],
 "Dorsal scale-pattern photographs from rescue/rehab centres and confiscated-scale inventory photographs",
 "One scale field — hundreds of rescued individuals per large centre; seizure lots by the tonne, photo protocol at intake",
 "Scale-pattern ID vs DNA sampled at the same intake/seizure (second ruler)",
 "Rehab centres' known residents photographed repeatedly",
 "A pangolin's scales are its armour and its price tag — the rescued ones are photographed, the seized ones are weighed, and the two records never meet.",
 "Pangolin work is split between welfare centres (photos, no genetics budget) and enforcement (genetics, no pattern archive); the pattern system itself is barely studied.")

# ---------- Family E: Teeth, horns, antlers & wings — hard & membrane patterns ----------
add("tooth-wear-age-charts","Tooth-wear age charts & jaw collections (deer and game)","E. Teeth, horns, antlers & wings",8,
 "Every game agency aged deer by tooth wear from chart sets built on a handful of known-age jaws; the jaw collections behind rival charts were never compared head-to-head.",
 ["tooth wear age chart deer known age","tooth eruption wear ageing jaw collection","red deer jaw age data archive","game animal tooth wear reference photographs"],
 [".jpg",".pdf",".csv",".xls"], ["tooth wear","jaw","age","eruption"],
 "Jaw photographs/specimens and wear-score sheets in agency and university game collections",
 "One jaw — known-age reference sets of hundreds per species; agency-scored jaws by the hundred thousand, standard wear-chart protocol",
 "Wear age vs cementum-annuli age from the same jaw (second ruler — the classic two-rulers pair)",
 "Known-age penned deer/elk herds whose jaws built the original charts",
 "A deer's teeth are a clock every hunter is taught to read — the clock was set from a few hundred jaws and never re-checked against the true ages.",
 "Wear charts are regional (each agency its own poster) and their reference jaw collections sit in freezers and museum drawers, un-cross-validated.")
add("cementum-annuli-tooth-archives","Cementum-annuli tooth-age laboratory archives","E. Teeth, horns, antlers & wings",8,
 "One lab (Matson's) has sectioned teeth since 1969 for agencies continent-wide — annuli counts vs the wear ages and harvest records on the same animals are a ready two-rulers panel.",
 ["cementum annuli age data archive","tooth section age laboratory records","Matson cementum age reports","bear deer cementum annuli dataset"],
 [".jpg",".tif",".csv",".pdf"], ["cementum","annuli","tooth section","age"],
 "Tooth cross-section images and annuli count records in ageing-lab and agency files",
 "One tooth — hundreds of thousands of teeth sectioned across species since 1969, one histology protocol per lab",
 "Cementum age vs tooth-wear age and vs known age for marked animals (two second rulers)",
 "Known-age marked bears/deer submitted blind to the labs",
 "Slice a tooth and count the winters in its root — the labs that do it hold a half-century of slices nobody lined up against the ages everyone guessed in the field.",
 "Ageing is a service industry: labs return a number, agencies file it, and the section images plus the field guesses were never joined into one audit set.")
add("dental-casts-mammal","Mammal dental casts & tooth-row pattern collections","E. Teeth, horns, antlers & wings",7,
 "Dental casts are how mammalogy measured tooth rows before CT; cast drawers in museums carry collector-era labels that CT-era taxonomy revised.",
 ["dental cast collection mammal museum","tooth cast specimens archive","dental impression mammal specimens","mammal dentition cast photographs"],
 [".jpg",".tif",".csv",".pdf"], ["dental cast","dentition","tooth row","cast"],
 "Plaster dental casts and tooth-row photographs in museum and dental-school collections",
 "One tooth row — hundreds to thousands of casts per collection across dozens of species, impression protocol",
 "Cast-era species labels vs modern CT/morphometric re-identification of the same specimens (second ruler)",
 "Type specimens whose casts circulated to other museums",
 "Before scanners, a mammal's teeth travelled the world as plaster — the plaster is still in the drawers, wearing the old names.",
 "Cast collections were teaching infrastructure; digitisation prioritised skulls, and the cast drawers kept their paper labels.")
add("antler-tine-records","Antler tine & beam record archives (trophy and cast-antler series)","E. Teeth, horns, antlers & wings",7,
 "Record books scored antlers for a century; cast-antler series from known bucks (same animal, yearly sheds) are growth curves hiding in trophy rooms.",
 ["antler records scoring archive data","cast antler collection known deer yearly","antler tine measurements dataset","trophy antler record book photographs"],
 [".jpg",".csv",".pdf",".xls"], ["antler","tine","beam","record book"],
 "Antler measurement sheets, score charts and shed-antler series photographs in record-book, agency and ranch collections",
 "One antler set — record books hold tens of thousands of scored heads; known-buck shed series run 5–10 yearly sets per animal, one scoring protocol (Boone & Crockett / SCI / CIC)",
 "Score-book age/identity vs the same buck's known history and yearly sheds (second ruler)",
 "Pen-raised known-age bucks with complete shed series",
 "The same buck drops a bigger crown every year and picks it up nowhere — hunters kept the crowns, and together they are his growth chart.",
 "Trophy records were compiled for ranking, not biology; shed series sit with ranches and collectors, and agencies' measurement sheets were never pooled with them.")
add("horn-annuli-age-records","Horn growth-ring (annuli) age records — sheep, goats, ibex","E. Teeth, horns, antlers & wings",7,
 "Bighorn/ibex ages are read off horn rings at check stations; the ring counts were validated on a few known-age herds and then applied continent-wide.",
 ["horn annuli age bighorn sheep data","horn growth ring ageing ibex records","horn segment measurements archive","mountain goat horn age validation study"],
 [".jpg",".csv",".pdf",".xls"], ["horn","annuli","growth ring","age"],
 "Horn photographs, segment-length measurement sheets and annuli counts in agency and alpine-club collections",
 "One horn — thousands of checked rams/ibex per jurisdiction across decades, tape-and-photo protocol",
 "Ring age vs cementum age and vs known age of marked animals (second rulers)",
 "Known-age marked herds (e.g. Ram Mountain bighorns) as the anchor",
 "A ram wears its birthdays as rings on its horns — check stations have read them for decades and filed the readings by district.",
 "Horn ageing is agency routine in a dozen jurisdictions with a dozen filing systems; the validation herds are famous, the routine counts unexamined.")
add("bite-mark-records","Bite-mark & tooth-pit records (predation and forensic)","E. Teeth, horns, antlers & wings",6,
 "Tooth-pit spacing on bones identifies the predator in fossil and modern kill studies; reference bite sets are few and lab-local — real but thin, hence 6.",
 ["bite mark tooth pit measurements predator","tooth mark bone identification data","bite mark forensic animal reference","predator tooth pit spacing study"],
 [".jpg",".csv",".pdf"], ["bite mark","tooth pit","tooth mark","predation"],
 "Bite/tooth-pit photographs and spacing measurements on bone, from taphonomy labs and kill-site studies",
 "One bitten bone — hundreds per taphonomy reference set, calliper protocol",
 "Biter called from pit spacing vs DNA/feeding-trial bites by known animals (second ruler)",
 "Feeding-trial bones from known captive predators",
 "The spacing of two punctures in bone can name the jaws that made them — palaeontologists and wardens measure the same holes and never compare notes.",
 "Bite-mark reference work is split between fossil taphonomy and wildlife forensics, each with small private reference sets.")
add("bat-wing-venation","Bat wing venation & membrane pattern archives","E. Teeth, horns, antlers & wings",7,
 "Wing veins and membrane scars ID bats in the hand; banding-era wing photographs and venation drawings sit in chiroptera collections, pre-dating the DNA revisions of bat taxonomy.",
 ["bat wing venation identification","bat wing membrane pattern photographs","bat wing morphology archive specimens","chiroptera wing vein pattern study"],
 [".jpg",".tif",".pdf",".csv"], ["wing","venation","bat","membrane"],
 "Spread-wing photographs and venation tracings in bat research and museum collections",
 "One wing — thousands of banded bats per long-term study, dozens of species per regional collection, wing-against-light photo protocol",
 "Wing-based species ID vs DNA barcode of the same banded bat (second ruler)",
 "Banding records tying wing photos to recaptures",
 "A bat's wing is a hand with the fingers stretched into a sail — the veins map like a palm print, and banders photographed them for decades.",
 "Bat taxonomy was rebuilt by DNA while the wing-photo files of the banding era stayed with their collectors; nobody re-ran the old wings against the new names.")

# ---------- Family F: Faces, ears, eyes, scars, tails & whiskers ----------
add("primate-face-pattern-archives","Primate & chimpanzee face-pattern ID archives","F. Faces, ears, eyes, scars, tails & whiskers",8,
 "Chimp faces were ID'd by human eye at Gombe/Taï for 60 years; ChimpFace-era ML now trains on scraped sets while the sites' own portrait archives stay home.",
 ["chimpanzee face recognition archive","primate individual identification photographs","chimpanzee ID cards Gombe archive","ape face pattern database"],
 [".jpg",".tif",".csv"], ["face","chimpanzee","identification","portrait"],
 "Portrait ID photographs and face-description cards from long-term primate field sites",
 "One face — hundreds of known individuals per site (Gombe since 1960), thousands across sites, portrait protocol",
 "Face ID vs genetic ID from faecal DNA of the same chimps (second ruler)",
 "Known-pedigree individuals at the long-term sites",
 "Researchers at Gombe know two hundred chimpanzee faces the way you know your family's — the portrait files that taught them are still at the field stations.",
 "Face archives are field-site patrimony; the ML community built its own small scraped datasets rather than joining the sites' sixty years of portraits.")
add("whisker-spot-patterns","Whisker-spot (vibrissae) pattern catalogues — lions & pinnipeds","F. Faces, ears, eyes, scars, tails & whiskers",9,
 "Pennycuick & Rudnai's 1970 lion method is pure pattern: dot maps of whisker follicles, still used in Kruger/India (WII's Lion software) and re-invented for sea lions — three literatures, one geometry, zero joining.",
 ["whisker spot pattern lion identification","vibrissae pattern sea lion identification","lion whisker spot catalogue archive","whisker pattern individual identification data"],
 [".jpg",".csv",".pdf"], ["whisker","vibrissae","spot pattern","lion"],
 "Whisker-spot dot maps and muzzle photographs in lion and pinniped ID catalogues",
 "One muzzle — hundreds of lions per park catalogue (method since 1970), pinniped sets of 50–1,000, dot-map protocol",
 "Whisker ID vs scar/ear-mark ID and genetic ID in the same individuals (second rulers)",
 "Australian sea lion known-individual sets used to validate the method (99% pattern uniqueness at n=50)",
 "A lion's whisker dots are a star chart printed on its muzzle — rangers have read the same chart since 1970 and kept it park by park.",
 "The lion, sea-lion and seal whisker literatures cite different ancestors and hold separate catalogues; the shared point-pattern geometry has never been run across them.")
add("vibrissae-follicle-maps","Vibrissae follicle & mystacial pad maps (small mammals & pinnipeds)","F. Faces, ears, eyes, scars, tails & whiskers",6,
 "Whisker follicle arrangements are mapped whisker-by-whisker in neuroscience (barrel cortex) and pinniped sensory labs — deep data, narrow archives, hence 6.",
 ["vibrissae follicle map mystacial pad","whisker follicle arrangement pattern study","mystacial vibrissae map seal rodent","whisker identity follicle archive"],
 [".jpg",".tif",".pdf",".csv"], ["vibrissae","follicle","mystacial","whisker map"],
 "Follicle maps and mystacial-pad photographs/drawings from sensory-neuroscience and pinniped labs",
 "One whisker pad — tens to hundreds of mapped individuals per lab across a dozen species, dissection/photo protocol",
 "Follicle-map identity vs the same animal's whisker-spot photo ID (second ruler — two readings of one pad)",
 "Lab colonies where the same individuals are mapped and photographed",
 "Every whisker has an address, and the brain keeps a map of the addresses — the address books are drawn lab by lab and never compared across species.",
 "A methods detail inside neuroscience papers; the comparative pattern data was never the point of any single lab, so nobody assembled it.")
add("livestock-iris-patterns","Livestock iris-pattern ID records","F. Faces, ears, eyes, scars, tails & whiskers",7,
 "Iris ID was piloted for cattle/horses in the 2000s (IrisScan-era trials) and abandoned for RFID — the trial image sets are stranded pilots, perfect hunter shape.",
 ["cattle iris recognition identification trial","horse iris pattern identification system","livestock iris scan database archive","iris biometric livestock study images"],
 [".jpg",".bmp",".csv",".pdf"], ["iris","livestock","identification","biometric"],
 "Iris photographs and match-score files from livestock biometric pilot trials (universities, defunct startups)",
 "One iris — hundreds to thousands of animals per trial series, fixed-camera protocol",
 "Iris match vs RFID/DNA identity of the same animals (second ruler)",
 "Trial herds with full tag records",
 "For a few years, cows were going to log in with their eyes — the iris trials were run, photographed, and shelved when ear tags won.",
 "Pilot-era data lives with defunct vendors and thesis appendices; the livestock-biometrics literature cites the trials without their image sets ever surfacing.")
add("ear-notch-punch-registries","Ear-notch & ear-punch record systems (livestock and wildlife)","F. Faces, ears, eyes, scars, tails & whiskers",7,
 "The pig litter-notch system and cattle notch codes are pattern languages recorded on registration cards for a century — applied marks, but archived like print collections.",
 ["ear notch system pig litter identification records","cattle ear notch registration archive","ear punch code wildlife marking records","ear notching identification chart historical"],
 [".jpg",".pdf",".csv"], ["ear notch","ear punch","notch code","marking"],
 "Ear-notch diagrams on registration cards, breed-association records and wildlife marking logs",
 "One notched ear — millions of pigs/cattle registered under notch codes since the early 1900s, standard notch-position charts",
 "Notch code as read from the card vs the animal's pedigree/DNA record (second ruler)",
 "Breed associations' master registration books",
 "A pig's ear is punched with its litter number like a train ticket — the ticket stubs fill a century of farm record books.",
 "Notch systems are taught in every animal-science course and archived nowhere centrally; association card files are the only corpus and they are paper.")
add("hyena-ear-notch-id","Spotted hyena ear-notch & spot ID archives","F. Faces, ears, eyes, scars, tails & whiskers",7,
 "Hyena ID combines natural ear notches, spots and scars — the Mara/Talek clan archives run since 1979 with drawn ear diagrams per animal.",
 ["spotted hyena ear notch identification","hyena individual identification ear diagrams","Mara hyena project ID archive","hyena spot pattern individual recognition"],
 [".jpg",".pdf",".csv"], ["hyena","ear notch","identification","clan"],
 "Drawn ear-notch diagrams, spot photos and ID files from long-term hyena projects",
 "One ear/flank — hundreds of known hyenas in the Mara archive since 1979, dozens in Ngorongoro and other clan studies, diagram protocol",
 "Ear/spot ID vs genetic ID from darting samples of the same hyenas (second ruler)",
 "Known-pedigree clan members (births observed)",
 "A hyena's torn ear is its signature, drawn by hand into the clan file the day it is first recognised.",
 "Clan archives are single-lab treasures (the Mara files span 45 years); no second clan's ear diagrams have ever been compared with them.")
add("scar-based-photo-id","Scar & wound-pattern photo-ID archives (cross-species)","F. Faces, ears, eyes, scars, tails & whiskers",7,
 "Scars are the accidental ID system — shark-bite scars on seals, propeller scars on manatees/dugongs, fight scars on hippos — each programme sketches them alone.",
 ["scar based photo identification animals","shark bite scar identification seal archive","propeller scar manatee dugong identification","wound pattern individual identification photographs"],
 [".jpg",".tif",".pdf",".csv"], ["scar","wound","photo-id","sketch"],
 "Scar sketches and wound photographs in photo-ID programme files across taxa",
 "One scar pattern — hundreds to thousands of individuals per programme, sketch-then-photo protocol",
 "Scar ID vs tag/genetic ID recorded at the same encounters (second ruler)",
 "Rescue/rehab animals with known identity and dated wound photos",
 "An animal's worst day becomes its ID card — the scar sketches are filed species by species, programme by programme.",
 "Scar ID is always the backup system inside another programme's catalogue, never extracted or compared as a pattern archive in its own right.")
add("tail-pattern-systems","Tail pattern & tail-ring ID systems (lemurs, raccoons, cats, marine mammals)","F. Faces, ears, eyes, scars, tails & whiskers",6,
 "Tail rings/notches close many ID calls (cheetah tail tips, lemur rings, dolphin tail stocks) but are recorded as a field inside other catalogues — thinnest standalone archive here, hence 6.",
 ["tail ring pattern identification animal","lemur tail pattern individual identification","tail notch identification catalogue","cheetah tail tip pattern ID"],
 [".jpg",".pdf",".csv"], ["tail","ring pattern","notch","identification"],
 "Tail photographs and ring/notch diagrams inside multi-feature ID catalogues",
 "One tail — hundreds of individuals per host catalogue, photo protocol shared with the host system",
 "Tail ID vs the host catalogue's primary feature (flank/face) for the same animal (second ruler)",
 "Catalogues where tail photos were taken at every encounter (cheetah, dolphin sets)",
 "Half of a cheetah's name is written on the last white rings of its tail — tail patterns are everyone's second clue and nobody's archive.",
 "Tail data exists only as a column in other systems' files; a tail-first pass over those files has never been run.")

# ---------- Family G: Hair & applied-mark pattern atlases ----------
add("guard-hair-scale-casts","Mammal guard-hair scale casts & hair atlases (wildlife forensics)","G. Hair & applied-mark pattern atlases",9,
 "The Texas atlas alone covers 150+ species with SEM scale images; ZSI Kolkata, FBI/USFWS-style labs and Brunner & Coman built parallel atlases on three continents that cite different standards.",
 ["guard hair scale cast identification atlas","mammal hair atlas SEM scale pattern","hair identification key mammals download","trichotaxonomy guard hair microphotographs"],
 [".jpg",".tif",".pdf",".csv"], ["guard hair","scale cast","trichotaxonomy","cuticular"],
 "Cuticular scale casts (gelatin/cellulose impressions), SEM surface images and photomicrographs in forensic hair atlases",
 "One hair — 150+ species in the Texas atlas, 100+ in the Indian and Australian atlases, one cast-and-mount protocol per atlas tradition",
 "Species called from scale cast vs DNA barcoding of the same hair/specimen (second ruler)",
 "Museum-vouchered hairs (atlas specimens tied to skins/skulls)",
 "A single guard hair carries a scale pattern like a fingerprint — forensic atlases were built continent by continent and never checked against each other.",
 "Hair ID is a forensic service literature: regional atlases (Texas 2009, ZSI series, Brunner & Coman 1974) each keyed their own fauna with their own scale vocabulary.")
add("hair-medulla-cross-sections","Hair medulla & cross-section pattern atlases","G. Hair & applied-mark pattern atlases",7,
 "The second preparation of forensic hair work: medulla types and cross-section shapes keyed separately from scale casts, often by different authors for the same fauna.",
 ["hair medulla pattern identification mammals","hair cross section shape atlas","medullary index mammal hair data","hair microscopy medulla types archive"],
 [".jpg",".tif",".pdf",".csv"], ["medulla","cross section","hair","medullary"],
 "Whole-mount medulla photomicrographs and hair cross-section images with medullary-index tables",
 "One hair section — dozens to 150+ species per atlas, sectioning protocol",
 "Medulla-based species call vs scale-cast call on the same hairs (second ruler — the two preparations audit each other)",
 "Vouchered museum hairs sectioned and cast in parallel in the classic atlases",
 "Cut a hair across and it shows a tiny patterned core — a second fingerprint inside the first, keyed in separate books.",
 "Medulla/cross-section data rides inside the same regional atlases as the casts but was tabulated separately and never joined across regions either.")
add("lab-animal-marking-records","Lab-animal marking-pattern records (ear punch, toe clip, tattoo archives)","G. Hair & applied-mark pattern atlases",6,
 "Colonies marked animals by punch/clip codes for a century; the marking logs of famous long-lived colonies are identity infrastructure that outlived the experiments — archival, hence 6.",
 ["laboratory animal ear punch marking records","toe clip marking code archive","mouse colony marking system historical","animal tattoo identification colony records"],
 [".pdf",".jpg",".csv"], ["ear punch","toe clip","tattoo","marking"],
 "Marking code charts and colony marking logs from long-running laboratory and field colonies",
 "One marked animal — thousands per colony across decades, standard punch-position code charts (several rival charts)",
 "Mark as logged vs genotype/pedigree of the same animal in the colony records (second ruler)",
 "Colonies with complete pedigrees (e.g. classic mouse/rat colonies)",
 "Generations of lab mice were named by holes punched in their ears — the punch charts are a pattern language filed with the colony books.",
 "Marking charts were standardised locally and published as methods figures; the logs themselves are institutional archives, consulted by nobody outside the colony.")

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
    doc = {"generated": "2026-11-18", "doctrine": "mammal-grain niches (2026-11-18, Atharva's correction)",
           "grain_rule": "One intuitive animal world (mammals); a niche is ONE body/trace/pattern system. This registry sits AHEAD of the broad niches.json registry in the campaign queue.",
           "pattern": "(a) raw capture taken the same way across many individuals/species; (b) used for individual ID or age/sex/species reading, labels in old catalogues/forensic atlases/photo-ID archives/museum cast collections, often on a second ruler (DNA, tags, dissection); (c) instantly headline-shaped.",
           "koala_verification": "Henneberg, Lambert & Leigh (1997), 'Fingerprint homoplasy: koalas and humans', Univ. of Adelaide: ~20 koalas, ink prints + SEM; ridges nearly identical to human in microscopic morphology, pattern organisation and individual uniqueness; authors called a crime-scene mix-up 'extremely unlikely'; no documented crime-scene confusion exists.",
           "selection_tests": ["fidelity", "headline", "fragmentation"],
           "count": len(entries), "niches": ranked}
    with open("mammal_niches.json", "w") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
    lines = ["# Mammal niches — the 50 at Atharva's grain (2026-11-18)", "",
             "Atharva's correction: he meant niche domains at the grain of",
             "\"paws and fingerprint analysis of mammals and all that\" — NOT broad",
             "cross-domain fields. The broad registry (`NICHES-50.md`) was the wrong",
             "grain. This registry is **50 niches inside ONE intuitive world —",
             "mammals** (direct animal-trace analogues only where the system is the",
             "same) — each niche a specific body part, trace, print or pattern",
             "system. **This registry now sits AHEAD of the broad registry in the",
             "campaign queue** (see README, 'Mammal-grain niches').", "",
             "## Why these systems are fertile — the pattern", "",
             "Each system here is:", "",
             "(a) a **raw capture** — print, cast, photo, scan, hair cast, X-ray —",
             "taken the **same way across many individuals/species**;",
             "(b) used for **individual ID or age/sex/species reading**, so labels",
             "exist but live in old catalogues, forensic atlases, photo-ID archives",
             "and museum cast collections — often on a **second ruler** (DNA, tags,",
             "collars, dissection, known-age animals); and",
             "(c) **instantly headline-shaped** — a layperson gets it in one",
             "sentence.", "",
             "**Canonical headline, verified (not just repeated):** the koala's",
             "fingerprint. Henneberg, Lambert & Leigh (1997), *Fingerprint",
             "homoplasy: koalas and humans* (University of Adelaide): ~20 koalas,",
             "ink prints plus scanning electron microscopy — the ridges are",
             "nearly identical to a human's in microscopic morphology, pattern",
             "organisation and individual uniqueness. The authors themselves",
             "called a crime-scene mix-up \"extremely unlikely\", and no",
             "documented confusion at a crime scene exists. The honest headline",
             "is the verified one: *near-indistinguishable under the microscope*.", "",
             "Excluded: mammal brains (landed) and rhino forearm centroid work",
             "(landed) — rhino ear-notch/horn ID is a different system and is",
             "included on its own merits.", "",
             "Machine-readable twin: `mammal_niches.json`. In the hunter:",
             "`python3 goldmine_hunter.py mammal-niches [--top N | --niche <slug>]`;",
             "per-niche gold words + signature extensions feed",
             "`mammal_niche_score()`.", "",
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
    with open("MAMMAL-NICHES-50.md", "w") as fh:
        fh.write("\n".join(lines))
    print(f"mammal_niches.json + MAMMAL-NICHES-50.md written: {len(entries)} entries")
    print("top 10:", [(e["slug"], e["score"]) for e in ranked[:10]])

if __name__ == "__main__":
    main()
