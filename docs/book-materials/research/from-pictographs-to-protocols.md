# From Pictographs to Protocols:
## Visual Languages, Symbolic Conlangs, AAC Systems, and International Sign Standards

> **Status:** Research source / literature review  
> **Added:** 2026-09-09  
> **Purpose:** Background research for Pictiq development and future publications.  
> **Relationship to Pictiq:** Comparative research source, not normative protocol specification.
>
> **Editorial note:** This report contains research-derived observations and recommendations. They are evidence and input for Pictiq development, not automatically accepted Pictiq protocol decisions. Where the project later differs, both the source position and the subsequent project decision are preserved.

## Abstract

Visual communication systems occupy several different design spaces that are often conflated: pictures that preserve or prompt meaning, scripts that encode a spoken language, autonomous symbolic languages, assistive vocabularies, and tightly regulated signs for public action. This review traces that landscape from prehistoric graphic communication and Egyptian writing through Isotype, modernist wayfinding, road-sign treaties, AAC systems, pictographic constructed languages, and Unicode emoji. Its central finding is that visual resemblance does not by itself produce universality: cross-cultural studies find substantial variation in the understanding of device symbols and traffic signs ([International Journal of Industrial Ergonomics](https://www.sciencedirect.com/science/article/pii/S0169814101000075); [traffic-sign guessability study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6338990/)). Systems scale when they limit their semantic domain, teach a stable convention, embed symbols in repeated situations, or acquire institutional and technical infrastructure. The most successful systems therefore combine pictorial motivation with non-pictorial supports: syntax, color and shape codes, captions, training, interaction protocols, or software keyboards.

Pictiq—a minimal protocol of framed icon “tiles,” punctuation, yes/no logic, quantity, compounds, and distinct phrase-line and catalog-grid modes—is used only as a comparison anchor ([Pictiq repository](https://github.com/markoblogo/pictiq)). The broader evidence suggests that projects in this class should be evaluated not by whether their icons appear “universal,” but by whether intended users can infer, learn, compose, repair, and act on messages in specified contexts. The relevant precedents are consequently not one lineage but four: pictorial statistics, regulated signage, pictographic/pasigraphic language design, and aided communication.

For product-level precedents adjacent to portable pointing and physical communication surfaces, see the companion [Portable Visual Communication Precedents](portable-visual-communication-precedents.md) study. That document covers Point It, Kwikpoint, ICOON, This, Please, and PECS / A Picture's Worth as case studies, while this report remains the broader historical and academic context.

## 1. Introduction: one visual field, several communicative jobs

A pictogram resembles or schematizes a referent; an ideogram denotes an idea; a logogram conventionally represents a linguistic unit; and a writing system encodes enough of a language to support open-ended linguistic expression. Britannica accordingly describes pictography as communication by pictures and drawings with a communicative aim, while distinguishing painted rock *petrograms* from carved *petroglyphs* ([Encyclopaedia Britannica](https://www.britannica.com/topic/pictography)). These categories overlap in practice, but they should not be treated as stages on a single ladder toward “universal language.”

The systems surveyed here solve four different problems. **Writing systems** externalize language; **supplementary symbol systems** support expression or comprehension when speech or literacy is unavailable; **public-information systems** trigger a narrow interpretation in a recurrent environment; and **symbolic conlangs or pasigraphies** attempt broader, language-independent composition. Emoji form a fifth, hybrid category: a globally standardized character repertoire used mostly inside ordinary written discourse rather than as a complete replacement for it ([Unicode Consortium](https://unicode.org/emoji/charts/emoji-counts.html)).

This distinction matters for Pictiq. Its repository defines the project as “a minimal visual protocol for short messages across language barriers,” with pointing, quick signs, stickers, and portable phrase displays among its intended uses ([Pictiq repository](https://github.com/markoblogo/pictiq)). That goal is nearer to a constrained interaction protocol than to a full writing-system replacement. The most informative comparisons are therefore systems that deliberately control context, vocabulary, composition, and interaction—not simply systems that happen to contain pictures.

## 2. Historical evolution of pictographic communication

### 2.1 Prehistoric graphic communication: precursor, not deciphered writing

Rock art demonstrates durable symbolic representation, but its communicative content is usually unrecoverable. Pictographs, petroglyphs, engravings, petroforms, and geoglyphs can depict animals, tools, and activities, yet the images are frequently symbolic rather than documentary ([Encyclopaedia Britannica](https://www.britannica.com/art/rock-art)). Researchers therefore describe many Paleolithic marks more cautiously as graphic communication rather than as writing, because writing ordinarily entails connected signs that represent language ([PBS NOVA](https://www.pbs.org/wgbh/nova/article/cave-painting-calendar-earliest-writing/)).

Recent work on lines, dots, and Y-shaped marks associated with European animal images argues that at least some sequences recorded calendrical information about animal behavior. Even favorable summaries call the proposed system “proto-writing,” because the marks encode numbers and seasonal reference rather than speech ([Smithsonian Magazine](https://www.smithsonianmag.com/smart-news/could-these-cave-markings-be-the-earliest-form-of-writing-180981403/)). The lesson for modern pictographic systems is methodological: visible recurrence can establish conventionality, but it does not by itself establish a vocabulary, grammar, or universally recoverable meaning.

### 2.2 Egyptian hieroglyphs: why pictorial appearance is not semantic transparency

Egyptian hieroglyphs are a crucial counterexample to the idea that picture-like signs constitute a universally readable “language of images.” The system emerged from late fourth-millennium BCE proto-writing, with early attestations around the thirty-third century BCE, and functioned as a formal writing system for the Egyptian language ([Egyptian hieroglyphs overview](https://en.wikipedia.org/wiki/Egyptian_hieroglyphs)). Its signs could function phonographically, logographically, or as unpronounced semantic determinatives; their pictorial form therefore did not tell an untrained viewer how a particular sign operated in a word ([Egyptian hieroglyphs overview](https://en.wikipedia.org/wiki/Egyptian_hieroglyphs)).

Hieroglyphic writing consequently demonstrates a general principle: a graphic sign can be iconic in shape yet conventional in linguistic value. Once a system carries names, inflection, phonetic complements, and grammatical language, learnability depends on shared code knowledge rather than resemblance alone. Modern “universal” pictogram projects often rediscover the same trade-off: increasing expressive range increases the burden of convention.

### 2.3 Isotype: pictorial statistics as designed explanation

The International System of Typographic Picture Education, or Isotype, began in 1920s Vienna and developed through later work in The Hague, Oxford, and London ([University of Reading, Isotype Collection](https://www.isotyperevisited.org/isotype-collection/)). Otto Neurath conceived the method to communicate social, economic, and political facts through simplified pictures, while Gerd Arntz supplied the disciplined graphic vocabulary; Neurath recruited Arntz in 1928 after seeing his political prints, and the 1930 *Gesellschaft und Wirtschaft* atlas contained 100 visual charts ([Gerd Arntz Web Archive](https://www.gerdarntz.org/content/gerd-arntz.html)).

Isotype was not a general-purpose pictographic language. Its core innovation was a rhetoric of quantitative comparison: repeated figures represented repeated units, visual transformation replaced decorative illustration, and layout made ratios and trends apprehensible. The University of Reading archive describes Isotype as a method for designing and disseminating data across public health, housing, social planning, museums, and children’s education ([University of Reading, Isotype Collection](https://www.isotyperevisited.org/isotype-collection/)). Meaning emerged from symbol, repetition, legend, scale, and explanatory composition together.

Arntz’s silhouettes also established an influential modernist style: reduced internal detail, clear profiles, and systematic contrasts among roles and objects. The archive records more than 4,000 Isotype linocut symbols in The Hague collections, although that archival count should not be confused with a single simultaneously active “vocabulary” ([Gerd Arntz Web Archive](https://www.gerdarntz.org/content/related-archives.html)). Isotype’s enduring contribution is thus not proof that pictures need no language, but a demonstration that a constrained visual grammar can make complex information comparatively legible.

### 2.4 Otl Aicher and the 1972 Munich Olympics

Otl Aicher’s identity system for the 1972 Munich Olympics integrated pictograms, structural grids, typography, color, tickets, uniforms, posters, and signage into one environmental program ([San Francisco Museum of Modern Art](https://www.sfmoma.org/exhibition/otl-aicher/)). The sports pictograms used a consistent geometric construction and bodily articulation, allowing distinct events to read as members of a family rather than as unrelated illustrations. Their significance lies as much in system governance as in drawing style: a shared grid and controlled visual variables created predictable differentiation.

The Munich program also illustrates how event-based wayfinding gains comprehensibility. Visitors encounter a limited universe of meanings—sports, facilities, directions, services—at locations where possible interpretations are already narrowed. A pictogram for swimming need not express tense, negation, or agency; it must discriminate one destination or event from nearby alternatives. This domain restriction helps explain why Aicher’s visual language became influential in environmental graphics without becoming autonomous writing.

### 2.5 Britain’s road-sign redesign

Jock Kinneir and Margaret Calvert developed Britain’s motorway and road-sign system between 1957 and 1967. The first motorway implementation appeared on the Preston bypass in 1958, and the coordinated system was introduced across British roads on 1 January 1965 ([Design Museum, Kinneir and Calvert](https://designmuseum.org/designers/jock-kinneir-and-margaret-calvert); [Design Museum, British Road Signs](https://designmuseum.org/discover-design/all-stories/british-road-signs)). The program responded to rapidly increasing traffic and an inconsistent inheritance of typefaces, symbol forms, and sign constructions ([Design Museum, British Road Signs](https://designmuseum.org/discover-design/all-stories/british-road-signs)).

The British case shows that road communication is multimodal within the visual channel. Type, pictogram, border shape, color, spacing, capitalization, mounting, and approach speed cooperate; no single icon carries the whole message. It also shows how national adoption differs from grassroots diffusion: committee mandate, transport engineering, fabrication rules, and universal deployment created repeated exposure, making initially learned conventions feel “natural” over time.

### 2.6 The Vienna Convention and international road signs

The United Nations Convention on Road Signs and Signals was adopted in Vienna on 8 November 1968 and entered into force on 6 June 1978. As of 6 September 2026, the UN Treaty Collection listed 35 signatories and 75 parties ([United Nations Treaty Collection](https://treaties.un.org/pages/ViewDetailsIII.aspx?src=TREATY&mtdsg_no=XI-B-20&chapter=11)). UNECE maintains the convention alongside the 1949 protocol, the 1971 European supplementary agreement, road-marking instruments, and subsequent amendments ([UNECE](https://unece.org/road-traffic-and-road-signs-and-signals-agreements-and-conventions)).

The convention harmonizes classes, shapes, colors, and meanings while permitting bounded national variation. Its success is therefore not a story of unaided pictorial intuition; it is a treaty-backed interoperability regime supported by driver education, licensing, road codes, and repeated exposure. Its 75 parties also mean that “international” is not identical to global uniformity: non-parties and local implementations remain important.

### 2.7 AIGA/DOT passenger symbols and airport wayfinding

In the United States, the Department of Transportation commissioned the American Institute of Graphic Arts to develop passenger and pedestrian symbols for transport hubs and large international events. Roger Cook and Don Shanosky designed the set; 34 symbols appeared in 1974 and 16 more in 1979, producing a 50-symbol system ([AIGA](https://www.aiga.org/resources/symbol-signs)). The project evaluated existing signs, consolidated variants, and released reproducible symbol artwork, making it both a design exercise and a public infrastructure intervention.

Airports intensify the need for language-reduced guidance because users are mobile, time-constrained, and linguistically diverse. Yet airport signage rarely relies on pictograms alone: codes, arrows, bilingual labels, color zones, maps, and architectural sightlines form the larger system. ICAO’s facilitation guidance points airports to dedicated planning and signing references, including FAA terminal-planning and airport-signing materials ([ICAO](https://www.icao.int/facilitation-programmes/Annex9/best-practices-international-signs-provide-guidance-persons-airports-and-marine-terminals)). “IATA airport pictograms” are therefore better understood as an ecosystem of industry guidance, ISO/AIGA-derived symbols, and local standards than as one globally binding pictogram alphabet.

### 2.8 ISO 7001 and the formalization of public-information symbols

ISO 7001:2023 is the fourth edition of the international standard for registered public-information symbols. It applies to locations and sectors accessible to the public, permits symbols to appear with text to improve comprehension, and explicitly excludes safety signs and road-traffic signs governed by other rules ([ISO](https://www.iso.org/standard/77442.html)). That boundary is conceptually valuable: public information, safety commands, and traffic control have different risk profiles and therefore different validation and design requirements.

ISO/TC 145, created in 1970 with a BSI secretariat, standardizes graphical symbols and the colors and shapes that form part of their messages. Its remit includes principles for preparing, coordinating, and applying graphical symbols ([ISO/TC 145](https://www.iso.org/committee/52662.html)). The 2023 standard is a maintained registry rather than a fixed “universal icon set”; amendments and new registrations reflect changing services and social needs. Because the ISO public preview does not state a single inventory total, claims that ISO 7001 contains a precise number of symbols should be tied to a specified edition, amendment state, and counting method rather than repeated without qualification ([ISO](https://www.iso.org/standard/77442.html)).

### 2.9 Emoji: from handset glyphs to an encoded global repertoire

Shigetaka Kurita designed the historically canonical early emoji set for NTT DoCoMo in 1998–1999; the Museum of Modern Art holds the work under Kurita’s name and dates it accordingly ([Museum of Modern Art](https://www.moma.org/collection/works/196070)). Emoji later moved from carrier-specific repertoires into Unicode, where characters and sequences receive interoperable identifiers while vendors retain stylistic freedom in rendering.

Unicode Emoji 17.0 contains 3,953 emoji characters and sequences when skin-tone variants, gendered and multi-person sequences, flags, and other constructions are counted according to Unicode’s table ([Unicode Emoji Counts](https://unicode.org/emoji/charts/emoji-counts.html)). This number is much larger than the 1,388 single-character entries in the same table, showing how composition and variation selectors expand the practical repertoire ([Unicode Emoji Counts](https://unicode.org/emoji/charts/emoji-counts.html)). Unicode’s frequency data for Emoji 12.0 ranked 😂 in the highest-frequency position; the Consortium states that frequency is one consideration among several in evaluating new proposals ([Unicode Consortium](https://home.unicode.org/emoji/emoji-frequency/)).

Platform statistics indicate extraordinary adoption but should be labeled by platform and date. Facebook reported an average of five billion emoji sent daily on Messenger in 2017, a claim preserved by Emojipedia with attribution to Facebook ([Emojipedia](https://blog.emojipedia.org/5-billion-emojis-sent-daily-on-messenger/)). Broader claims of “more than ten billion per day” circulate widely but generally aggregate estimates across platforms without a transparent global denominator; they are useful as scale indicators, not as auditable census data.

Emoji succeeded because it did not require users to abandon ordinary language. It supplies affect, stance, objects, identity markers, and discourse cues inside existing keyboards, messaging systems, and Unicode text. Its ambiguity is often socially productive, but that same ambiguity makes emoji unsuitable as a substitute for safety signage or precision AAC without contextual conventions.

## 3. Symbolic and pictographic constructed languages

### 3.1 Blissymbolics

Charles K. Bliss developed Semantography—later called Blissymbolics—between 1942 and 1949 and first published it in 1949, with expanded editions in 1965 and 1978 ([Blissymbols overview](https://en.wikipedia.org/wiki/Blissymbols)). Bliss intended a language-independent system for international communication, using simple graphic elements and relative position to construct concepts rather than encoding the sounds of one spoken language ([Blissymbolics Communication International training resource](https://www.blissymbolics.org/WebTraining/NewResourceHTMLCSS/resource9.php)).

Blissymbolics combines basic characters into Bliss-words and marks grammatical or semantic classes with indicators. Spatial relations, superimposition, size, orientation, and composition contribute to meaning, giving it substantially more formal morphology than an ordinary icon library. Its trajectory changed in 1971 when an interdisciplinary team at the Ontario Crippled Children’s Centre began using it with nonspeaking children with physical disabilities; it became one of the earliest major graphic AAC systems ([Blissymbolics Communication International training resource](https://www.blissymbolics.org/WebTraining/NewResourceHTMLCSS/resource9.php)).

Blissymbolics Communication International now authorizes vocabulary and maintains the language. Its July 2026 release lists 6,556 authorized symbols, including more than 370 additions in that update ([Blissymbolics Communication International](https://www.blissymbolics.org/)). BCI reports use by people with severe speech and physical impairments in more than 33 countries and translations into more than 15 languages, with strongest contemporary AAC presence in parts of Scandinavia and Europe ([BCI, “Who uses Bliss?”](https://www.blissymbolics.org/index.php/who-uses-bliss)).

The adoption record is real but specialized. No reliable current global user census is publicly available, and training attendance should not be equated with active symbol users. Bliss nevertheless outlived many universal-language projects because a defined clinical-educational population, an international steward, authorized vocabulary governance, and software encoding gave it institutional continuity.

### 3.2 LoCoS

Japanese designer Yukio Ota created LoCoS—“Lovers Communication System”—in 1964 as a left-to-right ideographic auxiliary language intended for communication across linguistic and literacy barriers, including use by deaf, nonspeaking, and non-literate people ([LoCoS overview](https://en.wikipedia.org/wiki/LoCoS_%28language%29)). Its graphic primitives include eight major semantic shapes, while words and relations are built through additional signs, placement, and sequencing ([LoCoS overview](https://en.wikipedia.org/wiki/LoCoS_%28language%29)).

LoCoS is more language-like than a signage set because it attempts predication and modification. Its sentence pattern assigns graphic zones to actor, action, object, and related information; tense and other relations are handled with dedicated signs and placement. This explicit syntax reduces some ambiguity but raises the learning cost beyond “point at the picture.”

The system remains a recurring subject in design and human-computer-interface research rather than a large living speech community. Recent work has explored LoCoS-based keyboards and empirical redesign, evidence of continuing academic interest but not mass adoption ([CEUR Workshop Proceedings](https://ceur-ws.org/Vol-2744/paper83.pdf)). Published global user numbers, active-speaker counts, and a continuously governed standard vocabulary could not be verified.

### 3.3 Toki Pona and sitelen pona

Sonja Lang created Toki Pona in 2001 as a minimalist constructed language oriented toward simplicity and “the big picture.” The official site describes 120–140 basic words and presents the language as complete despite its small lexicon ([Official Toki Pona site](https://tokipona.org/)). Its canonical 2014 book consolidated a 120-word core, while later community and dictionary practice commonly produces totals near 137 depending on which words are counted as established ([Toki Pona overview](https://en.wikipedia.org/wiki/Toki_Pona)).

Toki Pona is primarily a spoken and alphabetically written language, not a pictographic conlang. It belongs in this survey because its isolating grammar and radical lexical economy show how composition can substitute for vocabulary size. Broad concepts are narrowed through modifier chains, context, compounding, and paraphrase; speakers trade lexical precision for interpretive negotiation.

Sitelen pona, published in Lang’s 2014 book, gives Toki Pona a logographic/pictographic script in which a glyph generally corresponds to a Toki Pona word ([Official sitelen pona page](https://tokipona.org/sitelenpona)). The script can place modifier glyphs inside or around head glyphs, visually reflecting phrase structure. Because readers must know Toki Pona grammar and vocabulary, sitelen pona is not “universally readable” merely because many glyphs are iconic.

Toki Pona has achieved unusually robust grassroots adoption for a minimalist conlang. The 2021 community census received almost 1,000 responses, the 2022 census almost 2,000, and the 2024 census 1,997; participation was open even to beginners, so these totals are not counts of fluent speakers ([2021 census](https://tokiponacensus.github.io/results/); [2022 census](https://tokiponacensus.github.io/results2022/); [2024 census](https://tokiponacensus.github.io/results2024/)). A 2021 ISO 639-3 request estimated between 500 and 5,000 speakers, approximately 1,600, while current Discord membership is larger but includes learners and inactive accounts ([SIL ISO 639-3 request](https://iso639-3.sil.org/sites/iso639-3/files/change_requests/2021/2021-043_tok.pdf); [Discord server listing](https://discord.com/servers/ma-pona-pi-toki-pona-301377942062366741)).

The evidence supports a community in the low thousands of active or competent users and a broader online audience in the tens of thousands, not a mass-language population. No official Duolingo Toki Pona course or auditable Duolingo learner total was found; references to one should therefore not be used as an adoption metric.

### 3.4 Sitelen sitelen and derivative scripts

Jonathan Gabel’s sitelen sitelen is a non-linear artistic writing system for Toki Pona built from nested “hieroglyphic blocks.” Its author describes the script as a way to break from linear habits and organize words in two-dimensional compositions ([Jonathan Gabel](https://jonathangabel.com/toki-pona/)). Unlike sitelen pona’s relatively direct word-to-glyph relationship, sitelen sitelen makes page architecture and visual enclosure central to reading.

Other community scripts transliterate or reimagine Toki Pona, but they inherit its language rather than constituting separate pictographic languages. This distinction is analytically important: a visual script can be inventive without changing the underlying grammar, semantic categories, or speech community.

### 3.5 iConji

Kai Staats created iConji in 2009 as a digital pictographic communication project combining SMS speed with a global art vocabulary. iConji Messenger launched in May 2010, iConji Social followed in December 2010, and an artist community opened in 2011 ([iConji overview](https://en.wikipedia.org/wiki/IConji)). The system supplied a defined icon lexicon, user-contributed symbols, inflection-like markers, and sequences intended to carry complete messages.

iConji’s dependence on dedicated applications was both its affordance and its weakness. Software enabled search, glosses, composition, and distribution, but users had to install or visit an iConji-specific environment rather than use an already ubiquitous character standard. Development ended in December 2012, leaving the project as an instructive example of a technically functioning but ecosystem-limited visual language ([iConji overview](https://en.wikipedia.org/wiki/IConji)).

### 3.6 Icono, Symbolics, and other visual-language experiments

Peter Kramer’s 2023 proposal **Icono** aims at an international written language in which strings of icons depict word meanings and graphic layout reveals sentence structure before linear reading. The paper presents a research program rather than evidence of an established user community ([Frontiers in Psychology](https://pmc.ncbi.nlm.nih.gov/articles/PMC10421668/)). Icono is notable because it treats syntax visualization—not only pictorial vocabulary—as the central design problem.

**Symbolics** is a contemporary independent proposal for pictographic literacy, numeracy, and ecological literacy, drawing on the longstanding ideal of a *characteristica universalis*. Its public materials articulate a design ambition but do not provide a verified user population, standardized vocabulary census, or independent effectiveness studies ([Symbolics project](https://www.sustainable.soltechdesigns.com/symbolics.html)). It should therefore be categorized as an exploratory design project rather than an adopted language.

Related projects include Pictoperanto, Earth Language, Symese, and numerous personal pasigraphies. An academic survey of constructed pictographic communication discusses Pictoperanto, LoCoS, Earth Language, Blissymbolics, iConji, and related systems as recurrent attempts at universality ([University of Plymouth doctoral research](https://pure.plymouth.ac.uk/ws/portalfiles/portal/38462588/2016Nawar10322746PHD_Edited.pdf)). Their common pattern is easy initial icon recognition but difficult expansion into abstract vocabulary, grammatical scope, input methods, and a self-sustaining community.

Ithkuil is intentionally excluded. It is a morphologically elaborate constructed spoken language with specialized scripts, not a genuinely pictographic communication system; visual distinctiveness alone does not make a language pictographic.

## 4. AAC symbol systems in real-world assistive communication

### 4.1 AAC as a use ecology

Augmentative and alternative communication includes unaided modes such as gesture and signing and aided modes ranging from paper boards to speech-generating devices. Pictographic AAC may support autistic people, people with cerebral palsy, aphasia after stroke, intellectual disabilities, motor impairments, or other conditions affecting speech and language; the ARASAAC norms study lists autism, aphasia, cognitive impairment, and cerebral palsy among populations using pictographic systems ([Frontiers in Psychology](https://www.frontiersin.org/articles/10.3389/fpsyg.2018.02538/full)). The same person may use speech, writing, gesture, signs, partner-assisted scanning, and pictograms together rather than adopting one “replacement language.”

AAC effectiveness consequently depends on more than symbol guessability. Motor access, visual complexity, vocabulary availability, partner training, pragmatic opportunities, device reliability, and consistent modeling all influence whether a symbol set becomes communicatively useful; PECS outcome research, for example, emphasizes implementation, maintenance, and generalization rather than picture recognition alone ([Flippin, Reszka, and Watson](https://pubmed.ncbi.nlm.nih.gov/20181849/)). A visual vocabulary is an interface to interaction, not merely a collection of labeled pictures.

### 4.2 Picture Communication Symbols and Boardmaker

Picture Communication Symbols (PCS) were created by Roxanna Mayer Johnson; *The Picture Communication Symbols, Book I* was published by Mayer-Johnson in 1981 ([ERIC bibliographic record](https://files.eric.ed.gov/fulltext/ED393256.pdf)). PCS became the commercial symbol library associated with Mayer-Johnson and Boardmaker, now distributed by Tobii Dynavox. The system uses relatively transparent color drawings to represent core and fringe vocabulary and is distributed through Boardmaker authoring and educational products ([Tobii Dynavox](https://www.tobiidynavox.com/pages/picture-communication-symbols)).

PCS is a symbol set, not a grammar. Users and clinicians arrange symbols in boards, visual schedules, sentence strips, and speech-generating interfaces; grammatical relations can be supplied by ordering, written labels, color coding, or the language system of a device. Commercial software, school procurement, a large installed base, and professional familiarity helped PCS become a default comparison set in AAC research.

Cross-cultural work cautions against assuming that PCS transparency transfers unchanged. A 2025 study comparing Indian Picture Symbols for Communication with PCS tested guessability and translucency among Indian participants, explicitly treating cultural-linguistic fit as an empirical question ([PubMed](https://pubmed.ncbi.nlm.nih.gov/38850205/)). The broader implication is that “more pictorial” is not the same as “equally interpretable everywhere.”

### 4.3 Widgit Symbols

Widgit Symbols are designed to make written information accessible and to support independent reading and writing. Widgit reports more than 20,000 symbols covering over 55,000 English words, with 17 language versions and a schematic design structure intended to support vocabulary extension ([Widgit](https://www.widgit.com/about-symbols/widgit_symbol_set.htm)). The current set grew from decades of development, including a major relaunch in October 2002 after a two-year practitioner-led project ([Widgit](https://www.widgit.com/about-symbols/widgit_symbol_set.htm)).

The many-to-many relationship between symbols and words demonstrates an important AAC distinction. A concept-oriented symbol inventory may map one graphic to several inflected or related written forms, while some abstract words require conventional rather than depictive graphics. Widgit’s strength is therefore not pure iconicity but consistent illustration, extensive lexical coverage, authoring tools, localization, and use in symbol-supported text.

### 4.4 SymbolStix

SymbolStix originated in News-2-You’s educational materials and depicts people and actions with a distinctive stick-figure style. n2y describes SymbolStix PRIME as a “universal visual language” with more than 90,000 symbols and tools for AAC, routines, social narratives, worksheets, and learning activities ([n2y](https://www.n2y.com/symbolstix-prime/symbolstix-prime-2021/)). Vendor counts have grown over time and differ across licensed subsets, so inventory claims should always name the product edition and date rather than treat “SymbolStix” as one timeless number.

SymbolStix illustrates platform-based adoption. The same drawings circulate through curricula, school materials, web authoring, and AAC devices, so exposure occurs across receptive and expressive contexts. This distribution network can matter more than whether the figures are intrinsically more guessable than competing libraries.

### 4.5 Makaton

Makaton is a multimodal communication program combining speech, key-word signs, and graphic symbols. Margaret Walker’s original 1972–73 work at Botleys Park Hospital developed a functional core vocabulary for deaf adults with intellectual disabilities, with the name formed from Walker, Katherine Johnston, and Tony Cornforth ([Makaton history overview](https://en.wikipedia.org/wiki/Makaton); [ERIC paper by Margaret Walker](https://files.eric.ed.gov/fulltext/ED249674.pdf)). The Makaton Charity describes the current program as supporting attention, comprehension, memory, language organization, and expression; signs can accompany unclear or absent speech, while printed symbols support people who cannot or prefer not to sign ([Makaton Charity](https://makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx)). It is therefore not a pictographic language alone.

The Charity states that more than 100,000 children and adults use Makaton as a main method or speech support ([Makaton Charity](https://makaton.org/TMC/TMC/AboutMakaton.aspx)). Published figures vary across organizational pages and years, and some secondary organizations report much higher totals; the conservative first-party figure is preferable unless a transparent counting method is available.

Makaton’s research bibliography spans roughly five decades and includes communication, language, and literacy studies, but the evidence base is heterogeneous in design and population ([Makaton Charity research](https://makaton.org/TMC/TMC/About_Makaton/Research.aspx)). Its durable adoption reflects training networks, local sign adaptation, educational practice, and the redundancy of speech-plus-sign-plus-symbol rather than reliance on a single visual channel.

### 4.6 PECS: an interaction protocol, not a symbol vocabulary

The Picture Exchange Communication System was developed in the United States in 1985 by Andy Bondy and Lori Frost and first implemented with preschool autistic students at the Delaware Autism Program ([PECS](https://pecsusa.com/pecs/)). PECS begins with exchanging one picture for a desired item or action and progresses through discrimination, sentence construction, modifiers, answering questions, and commenting. Its defining innovation is the prompted and reinforced social exchange, not ownership of a particular icon style.

This distinction is frequently blurred. PECS can use photographs, PCS, or other graphics; calling every laminated picture board “PECS” erases the six-phase teaching protocol. Pyramid Educational Consultants reports more than 441,000 people trained since 1994 and services in more than 95 countries, metrics of training reach rather than a census of active AAC users ([PECS Global Impact](https://pecsusa.com/global-impact/)).

The evidence is positive but bounded. A 2010 meta-analysis of studies published from 1994 through June 2009 found PECS effective for communication outcomes, but gains in speech were small to negative and maintenance and generalization evidence was limited; the authors characterized the evidence as promising but not yet strong ([Flippin, Reszka, and Watson](https://pubmed.ncbi.nlm.nih.gov/20181849/)). Later studies continue to show that outcomes vary with learner characteristics, implementation fidelity, target behavior, and intervention phase.

### 4.7 Aphasia and post-stroke communication

People with post-stroke aphasia may use communication books, topic boards, drawings, photographs, written keywords, gesture, or speech-generating systems. A 2021 trial protocol evaluated a paper AAC board designed for Mandarin-speaking inpatients with moderate to severe aphasia to communicate with medical staff and family, illustrating how language, clinical setting, and urgent topic vocabulary shape symbol selection ([Trials](https://pmc.ncbi.nlm.nih.gov/articles/PMC8611624/)).

Here, success may mean communicating pain, toileting, consent, hunger, or immediate care needs—not producing decontextualized sentences. This functional criterion closely resembles travel and pointing protocols: a small, available, jointly visible system can be valuable even if it cannot replace language.

## 5. Formal sign and pictogram standards

### 5.1 How graphical-symbol standardization works

Standards bodies do not discover universally self-evident pictures; they coordinate proposals, design principles, expert review, testing, ballots, publication, and maintenance. ISO/TC 145 has general responsibility for graphical-symbol standardization, while subcommittees and sectoral bodies address public information, safety, equipment, transport, and accessibility ([ISO/TC 145](https://www.iso.org/committee/52662.html)). National member bodies participate in ISO committees, and published standards are revised as technologies and public needs change.

This process converts a drawing into a governed convention. Registration provides a stable referent and reproduction form; testing estimates comprehension; deployment and training create familiarity; revision handles ambiguity or social change. Standardization therefore reduces interoperability risk, but it cannot eliminate cultural interpretation.

### 5.2 ISO 3864 safety-sign grammar

ISO 3864-1:2011 establishes safety identification colors and design principles for signs and markings used in workplaces and public areas for accident prevention, fire protection, hazard information, and emergency evacuation ([ISO](https://www.iso.org/standard/51021.html)). ISO 3864-2:2016 extends those principles to product safety labels that identify a hazard and how it can be avoided, while excluding chemical labels and dangerous-goods transport governed elsewhere ([ISO](https://www.iso.org/standard/66836.html)).

Safety signs function through a visual “grammar” of shape and color as well as pictorial content: warning, prohibition, mandatory action, safe condition, and fire equipment occupy recognizable formal classes. This redundancy is deliberate. A user who cannot resolve the internal pictogram may still perceive the class of required response.

### 5.3 ISO 9186: testing comprehensibility

ISO 9186 provides methods for testing graphical symbols with intended users: Part 1 measures the extent to which a symbol communicates its intended message, while Part 2 tests whether its constituent elements are readily identifiable by the eventual user population ([ISO 9186-1:2014](https://www.iso.org/standard/59226.html); [ISO 9186-2:2008](https://www.iso.org/standard/43484.html)). The standard’s role is to replace designer intuition with sampled evidence about what respondents think a symbol means and how well they can see its relevant features.

Open-ended testing is especially important because the ISO method seeks to measure whether a symbol communicates its intended message without supplementary explanatory text ([ISO 9186-1:2014](https://www.iso.org/standard/59226.html)). Results also depend on respondent culture, prior exposure, wording, context, and scoring rules, as cross-cultural symbol studies demonstrate ([International Journal of Industrial Ergonomics](https://www.sciencedirect.com/science/article/pii/S0169814101000075)). A passing score in one population should not be treated as timeless proof of universality.

### 5.4 GHS chemical hazard pictograms

The Globally Harmonized System of Classification and Labelling of Chemicals coordinates hazard classes, signal words, statements, and pictograms. UNECE distinguishes red-bordered GHS workplace/supply pictograms from transport labels used under dangerous-goods rules ([UNECE](https://unece.org/transport/dangerous-goods/ghs-pictograms)). OSHA presents nine GHS pictograms: flame over circle, flame, exploding bomb, skull and crossbones, corrosion, gas cylinder, health hazard, environment, and exclamation mark ([OSHA](https://www.osha.gov/hazcom/pictograms)).

The GHS case shows why a high-stakes system cannot be an icon dictionary alone. Border, red frame, black graphic, white field, product classification, signal word, and hazard statements jointly communicate risk. The pictogram is one layer in a legally governed label.

### 5.5 Medical and pharmaceutical pictograms

The United States Pharmacopeial Convention began a standardized pharmaceutical-pictogram initiative in 1987 and produced the current set of 81 pictograms in 1997. The set is freely available and has been widely evaluated and adapted internationally, especially for lower-literacy and second-language contexts ([Evaluation of USP pictograms](https://pmc.ncbi.nlm.nih.gov/articles/PMC7897753/)).

Evidence repeatedly shows that comprehension is population-dependent. A 2023 South African study tested medication-indication and side-effect pictograms with 90 first-language isiXhosa-speaking adults of limited formal education and examined the association between health literacy and comprehension ([Health SA Gesondheid](https://pmc.ncbi.nlm.nih.gov/articles/PMC10623492/)). Such studies support using pictograms as supplements to counseling and text, not as an automatic substitute.

### 5.6 Adoption is layered, not binary

Formal systems have different legal statuses. The Vienna Convention binds parties through treaty obligations and national implementation; ISO standards are generally voluntary unless incorporated into regulation, procurement, or contracts; GHS is implemented through jurisdiction-specific law; and AIGA/DOT symbols are public design resources rather than a treaty. “Standardized” can therefore mean registered, recommended, regulated, or merely widely reused.

Counting symbols is similarly nontrivial. ISO 7001 changes by edition and amendment; Unicode distinguishes characters from sequences; GHS counts nine pictograms while transport regulations include additional labels; and AAC vendors continuously expand localized libraries. Credible comparisons must name the edition, unit of count, and date.

## 6. Empirical case studies and statistics

### 6.1 Cross-cultural comprehension is uneven

A Swedish-American study tested 21 small graphical-symbol meanings in three visual versions each and found that interpretation varied across symbol design and cultural group, undermining the assumption that simplified graphics are automatically culture-free ([International Journal of Industrial Ergonomics](https://www.sciencedirect.com/science/article/pii/S0169814101000075)). Traffic-sign research comparing Chinese and German participants similarly found that familiarity, design features, and cultural context contribute to guessability even where signs share Vienna-Convention ancestry ([Traffic-sign guessability study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6338990/)).

The design implication is not that pictograms fail, but that recognition has components. **Iconicity** supports an initial hypothesis; **familiarity** stabilizes it; **context** narrows alternatives; **distinctiveness** prevents confusion; and **training** converts an uncertain guess into a convention. Systems can compensate for weakness in one component by strengthening others.

### 6.2 Medical pictograms expose the cost of false confidence

Medication graphics are a stringent test because a plausible but wrong interpretation may be harmful. Research on USP pictograms has shown that education affects comprehension and that online samples can underrepresent low-literacy users, making convenient testing populations a poor substitute for intended users ([Journal of Medical Internet Research](https://www.jmir.org/2013/6/e108/)). The 81-symbol USP repertoire’s long history of modification across countries also demonstrates that standard artwork often needs localization and retesting rather than simple export ([Evaluation of USP pictograms](https://pmc.ncbi.nlm.nih.gov/articles/PMC7897753/)).

### 6.3 Emoji scale and the denominator problem

Unicode 17.0’s 3,953 entries include 2,418 in the People & Body category, largely because skin-tone, gender, hair, family, and multi-person sequences generate many variants ([Unicode Emoji Counts](https://unicode.org/emoji/charts/emoji-counts.html)). Growth in “emoji count” therefore reflects representational combinatorics as well as entirely new pictorial concepts.

Daily-use statistics are even more denominator-sensitive. Facebook’s five-billion-per-day Messenger figure is a platform average from 2017, while “ten billion globally” estimates combine unlike services and periods ([Emojipedia](https://blog.emojipedia.org/5-billion-emojis-sent-daily-on-messenger/)). The safe conclusion is enormous, routine global use—not a precise current worldwide daily total.

### 6.4 Toki Pona: participation versus proficiency

Toki Pona’s community censuses doubled from roughly 1,000 responses in 2021 to roughly 2,000 in 2022, then remained near 2,000 in 2024 ([2021 census](https://tokiponacensus.github.io/results/); [2022 census](https://tokiponacensus.github.io/results2022/); [2024 census](https://tokiponacensus.github.io/results2024/)). Because beginners could respond, census participation measures community reach rather than fluent speaker population. Discord membership likewise measures account affiliation, not language competence.

This distinction matters when comparing a conlang with signage or AAC. A road sign has no “speaker community”; an AAC symbol library may have many users but little peer-to-peer prose; a conlang can have a small population yet rich cultural production. Adoption must be operationalized by system type.

### 6.5 Blissymbolics and AAC reach

BCI’s claims of use in more than 33 countries and more than 15 translated languages establish geographical reach but do not reveal current active-user totals ([BCI, “Who uses Bliss?”](https://www.blissymbolics.org/index.php/who-uses-bliss)). The absence of a global census should be reported rather than filled with inherited web estimates. Bliss’s more defensible adoption evidence is longitudinal: continuous organizational stewardship, thousands of authorized symbols, educational use since 1971, and ongoing vocabulary releases ([Blissymbolics Communication International](https://www.blissymbolics.org/)).

## 7. Comparative synthesis

### 7.1 Design philosophies and mechanisms

| System or family | Primary communicative job | Inventory / scope | Composition or “grammar” | Adoption mechanism | Current position |
|---|---|---|---|---|---|
| Egyptian hieroglyphs | Encode the Egyptian language | Large historical sign repertoire | Phonograms, logograms, determinatives, linguistic syntax | State, scribal, religious and monumental institutions | Historical writing system; not transparently pictorial ([overview](https://en.wikipedia.org/wiki/Egyptian_hieroglyphs)) |
| Isotype | Explain quantitative social information | Task-specific picture dictionaries and charts | Repetition, scale, layout, legends, comparison | Museums, education, publishing, modernist design networks | Foundational information-design method ([Reading](https://www.isotyperevisited.org/isotype-collection/)) |
| Munich 1972 / AIGA DOT | Event and transport wayfinding | Bounded service and activity sets; DOT totals 50 | Grid consistency, arrows, environmental placement | Public commission and infrastructure | Highly influential and widely reused ([AIGA](https://www.aiga.org/resources/symbol-signs)) |
| Vienna / ISO / GHS | Regulated public action and safety | Bounded, versioned registries | Shape, color, border, pictogram, text, context | Treaties, standards bodies, law, procurement, training | Strongest interoperability where implemented ([UN Treaty Collection](https://treaties.un.org/pages/ViewDetailsIII.aspx?src=TREATY&mtdsg_no=XI-B-20&chapter=11); [OSHA](https://www.osha.gov/hazcom/pictograms)) |
| Blissymbolics | Language-independent semantics and AAC | 6,556 authorized symbols in July 2026 | Graphic primitives, spatial composition, indicators, sequencing | AAC institutions, BCI governance, localization | Durable specialist system ([BCI](https://www.blissymbolics.org/)) |
| LoCoS | Universal auxiliary visual language | Small primitives plus derived signs | Ordered semantic zones and relation markers | Designer publication and research | Niche / academic ([LoCoS](https://en.wikipedia.org/wiki/LoCoS_%28language%29)) |
| Toki Pona + sitelen pona | Minimal spoken conlang with visual script | Roughly 120–140 basic words | Isolating syntax, modifier chains, compounds; word-glyph script | Books, online community, open cultural production | Active grassroots community in low thousands ([official site](https://tokipona.org/); [2024 census](https://tokiponacensus.github.io/results2024/)) |
| iConji | Digital visual messaging | Application-defined icon lexicon | Icon sequences and grammatical markers | Dedicated apps and contributor community | Development ended in 2012 ([overview](https://en.wikipedia.org/wiki/IConji)) |
| PCS / Widgit / SymbolStix | AAC and symbol-supported literacy | Tens of thousands of commercial graphics | Board layout, device language, captions, modeling | Schools, clinicians, vendors, devices, procurement | Large real-world assistive ecosystems ([Widgit](https://www.widgit.com/about-symbols/widgit_symbol_set.htm); [n2y](https://www.n2y.com/symbolstix-prime/symbolstix-prime-2021/)) |
| Makaton | Multimodal language support | Curated signs and symbols | Speech plus key signs plus graphic support | Charity, training, schools, families | More than 100,000 users claimed by the Charity ([Makaton](https://makaton.org/TMC/TMC/AboutMakaton.aspx)) |
| PECS | Teach spontaneous functional exchange | Any suitable picture vocabulary | Six-phase partner-mediated teaching protocol | Certified training, autism services, schools | Global specialist adoption; 441,000+ people trained reported ([Global Impact](https://pecsusa.com/global-impact/)) |
| Emoji | Supplement digital text and social interaction | 3,953 characters/sequences in Emoji 17.0 | Juxtaposition, repetition, platform conventions, ordinary-language context | Unicode, keyboards, platforms, network effects | Mass global adoption ([Unicode](https://unicode.org/emoji/charts/emoji-counts.html)) |

### 7.2 Vocabulary versus composition

The systems distribute expressive burden differently. AAC vendors and emoji favor large inventories and search interfaces; Toki Pona uses a tiny lexicon with heavy contextual compounding; Blissymbolics combines a governed vocabulary with productive graphic construction; signs minimize both vocabulary and grammar by restricting the situation.

Minimal isolating strategies reduce memorization but shift effort to interpretation. A Toki Pona phrase can paraphrase an unknown concept because interlocutors share spoken grammar and can negotiate meaning. A short pictogram protocol used by strangers may lack that repair channel, so it needs clearer punctuation, deictic pointing, yes/no responses, quantity, and mode distinctions. Minimalism is therefore not simply “fewer symbols”; it is a redistribution of complexity among lexicon, grammar, context, and interaction.

### 7.3 Why some systems achieved adoption

Five recurrent conditions explain adoption:

1. **A sharply specified use case.** Road signs guide driving; PECS teaches requesting and commenting; airport symbols guide movement; emoji enrich digital text. Bounded tasks make interpretation easier.
2. **Institutional or technical distribution.** Treaties, standards, schools, clinics, device vendors, keyboards, and app stores place the system where communication already occurs.
3. **Repetition and training.** Driver education, AAC modeling, recurring interface positions, and classroom use transform convention into apparent obviousness.
4. **Governance and maintenance.** ISO committees, Unicode, BCI, charities, and vendors add vocabulary, resolve duplicates, localize content, and preserve backward compatibility.
5. **Compatibility with existing language.** Emoji, Makaton, Widgit-supported text, and pharmaceutical pictograms supplement speech or writing rather than demanding total replacement.

Systems remain niche when their benefits are strongest only after users learn a novel grammar, but there is no institution to supply training or no installed channel for use. Dedicated visual-messaging apps face a two-sided network problem: a person gains little by learning or installing the system until likely partners have done so. Open-source publication lowers access barriers but does not by itself create interoperability, curriculum, empirical evidence, or network density.

### 7.4 Universality is an outcome, not a visual style

A black silhouette, rounded icon, or geometric radical can look international while still invoking culture-specific artifacts, reading directions, gestures, or metaphors. Empirical studies show cross-cultural variation even for small device symbols and standardized traffic signs ([cross-cultural device-symbol study](https://www.sciencedirect.com/science/article/pii/S0169814101000075); [traffic-sign study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6338990/)). “Universal” should therefore mean demonstrated performance across specified populations and contexts, not an aesthetic claim.

The strongest visual systems accept this limitation. They add labels, define classes through color and shape, constrain the domain, teach use, or test variants. Their universality is engineered and maintained.

## 8. Conclusion: locating Pictiq in the landscape

Pictiq belongs between symbolic conlang, AAC board, and situational protocol rather than in the category of full writing systems. Its compositional minimalism resembles Toki Pona’s strategy of deriving messages from a small core, while framed tiles and catalog selection resemble AAC boards and passenger-symbol inventories. Its punctuation, yes/no logic, quantity tiles, compounds, and phrase-line/catalog-grid distinction explicitly address interactional and layout problems that ordinary icon sets often leave to context ([Pictiq repository](https://github.com/markoblogo/pictiq)).

Its most distinctive framing is the separation between embodied use—pointing, arranging, or indicating a tile—and standalone messages that must survive without the sender’s immediate repair. That distinction aligns with the historical evidence: Isotype charts, road signs, PECS exchanges, and emoji messages succeed under different assumptions about context and response.

The open questions are empirical and institutional. Can unfamiliar travelers, AAC users, and communication partners infer intended meanings without prompting? Which errors are benign, and which reverse polarity, quantity, agency, or urgency? How quickly are compounds learned and retained? Do phrase-line and grid modes remain distinguishable under time pressure? How do cultural group, literacy, visual acuity, motor access, and icon familiarity affect performance?

The appropriate next step for projects of this kind is staged validation modeled on ISO 9186 and AAC research: open-ended guessability tests; confusion matrices; tests with and without context; learnability and delayed-retention studies; partner-mediated repair tasks; and field trials in actual travel, signage, and access scenarios ([ISO 9186-1:2014](https://www.iso.org/standard/59226.html); [PECS meta-analysis](https://pubmed.ncbi.nlm.nih.gov/20181849/)). Grassroots growth can generate creativity and examples, but stable versioning, symbol governance, accessible authoring tools, multilingual glosses, and partnerships with users and institutions are what turn a visual proposal into communication infrastructure.

## References and sources

- AIGA. “Symbol Signs.” https://www.aiga.org/resources/symbol-signs
- Blissymbolics Communication International. Home and Authorized Vocabulary. https://www.blissymbolics.org/
- Blissymbolics Communication International. “Who uses Bliss?” https://www.blissymbolics.org/index.php/who-uses-bliss
- Blissymbolics Communication International. Training Resource 9. https://www.blissymbolics.org/WebTraining/NewResourceHTMLCSS/resource9.php
- Britannica. “Pictography.” https://www.britannica.com/topic/pictography
- Britannica. “Rock art.” https://www.britannica.com/art/rock-art
- CEUR Workshop Proceedings. “Development of a Universal Pictographic Language…” https://ceur-ws.org/Vol-2744/paper83.pdf
- Design Museum. “British Road Signs.” https://designmuseum.org/discover-design/all-stories/british-road-signs
- Design Museum. “Jock Kinneir and Margaret Calvert.” https://designmuseum.org/designers/jock-kinneir-and-margaret-calvert
- Discord. “ma pona pi toki pona.” https://discord.com/servers/ma-pona-pi-toki-pona-301377942062366741
- Dowse, R., et al. “Pharmaceutical indication pictograms for low literacy viewers.” https://pmc.ncbi.nlm.nih.gov/articles/PMC10623492/
- Emojipedia. “5 Billion Emojis Sent Daily on Messenger.” https://blog.emojipedia.org/5-billion-emojis-sent-daily-on-messenger/
- Flippin, M., Reszka, S., and Watson, L. R. “Effectiveness of PECS…” https://pubmed.ncbi.nlm.nih.gov/20181849/
- Gabel, J. “sitelen sitelen.” https://jonathangabel.com/toki-pona/
- Gerd Arntz Web Archive. “Gerd Arntz.” https://www.gerdarntz.org/content/gerd-arntz.html
- Gerd Arntz Web Archive. “Related archives.” https://www.gerdarntz.org/content/related-archives.html
- ICAO. “Best Practices on International Signs…” https://www.icao.int/facilitation-programmes/Annex9/best-practices-international-signs-provide-guidance-persons-airports-and-marine-terminals
- ISO. ISO 3864-1:2011. https://www.iso.org/standard/51021.html
- ISO. ISO 3864-2:2016. https://www.iso.org/standard/66836.html
- ISO. ISO 7001:2023. https://www.iso.org/standard/77442.html
- ISO. ISO/TC 145 Graphical Symbols. https://www.iso.org/committee/52662.html
- ISO. ISO 9186-1:2014. https://www.iso.org/standard/59226.html
- ISO. ISO 9186-2:2008. https://www.iso.org/standard/43484.html
- Kramer, P. “Icono: a universal language that shows what it says.” https://pmc.ncbi.nlm.nih.gov/articles/PMC10421668/
- Makaton Charity. “What is Makaton?” https://makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx
- Makaton Charity. “About Makaton.” https://makaton.org/TMC/TMC/AboutMakaton.aspx
- Makaton Charity. “Research.” https://makaton.org/TMC/TMC/About_Makaton/Research.aspx
- Walker, Margaret. “Makaton in the 1980s.” ERIC. https://files.eric.ed.gov/fulltext/ED249674.pdf
- ERIC bibliographic record citing Mayer-Johnson’s 1981 *Picture Communication Symbols, Book I*. https://files.eric.ed.gov/fulltext/ED393256.pdf
- Museum of Modern Art. “Shigetaka Kurita. Emoji. 1998–1999.” https://www.moma.org/collection/works/196070
- n2y. “SymbolStix PRIME.” https://www.n2y.com/symbolstix-prime/symbolstix-prime-2021/
- OSHA. “Hazard Communication Pictograms.” https://www.osha.gov/hazcom/pictograms
- PECS USA. “PECS.” https://pecsusa.com/pecs/
- PECS USA. “Global Impact.” https://pecsusa.com/global-impact/
- PBS NOVA. “Ice Age cave paintings decoded…” https://www.pbs.org/wgbh/nova/article/cave-painting-calendar-earliest-writing/
- Philip, V. S., Koul, R., and Goswami, S. P. “Guessability of Indian Picture Symbols…” https://pubmed.ncbi.nlm.nih.gov/38850205/
- Pictiq repository. https://github.com/markoblogo/pictiq
- San Francisco Museum of Modern Art. “Otl Aicher: München 1972.” https://www.sfmoma.org/exhibition/otl-aicher/
- SIL International. Toki Pona ISO 639-3 New Code Request. https://iso639-3.sil.org/sites/iso639-3/files/change_requests/2021/2021-043_tok.pdf
- Smithsonian Magazine. “Could These Cave Markings Be the Earliest Form of Writing?” https://www.smithsonianmag.com/smart-news/could-these-cave-markings-be-the-earliest-form-of-writing-180981403/
- Society of Signs. “Semantography a.k.a. Blissymbolics.” https://www.societyofsigns.com/projects/semantography
- SolTech Designs. “Symbolics.” https://www.sustainable.soltechdesigns.com/symbolics.html
- Toki Pona. Official site. https://tokipona.org/
- Toki Pona. “sitelen pona.” https://tokipona.org/sitelenpona
- Toki Pona Census. 2021 results. https://tokiponacensus.github.io/results/
- Toki Pona Census. 2022 results. https://tokiponacensus.github.io/results2022/
- Toki Pona Census. 2024 results. https://tokiponacensus.github.io/results2024/
- Tobii Dynavox. “Picture Communication Symbols.” https://www.tobiidynavox.com/pages/picture-communication-symbols
- UNECE. “GHS pictograms.” https://unece.org/transport/dangerous-goods/ghs-pictograms
- UNECE. “Road Traffic and Road Signs and Signals Agreements and Conventions.” https://unece.org/road-traffic-and-road-signs-and-signals-agreements-and-conventions
- Unicode Consortium. “Emoji Counts, v17.0.” https://unicode.org/emoji/charts/emoji-counts.html
- Unicode Consortium. “Emoji Frequency.” https://home.unicode.org/emoji/emoji-frequency/
- United Nations Treaty Collection. “Convention on Road Signs and Signals.” https://treaties.un.org/pages/ViewDetailsIII.aspx?src=TREATY&mtdsg_no=XI-B-20&chapter=11
- University of Plymouth doctoral research on pictographic communication systems. https://pure.plymouth.ac.uk/ws/portalfiles/portal/38462588/2016Nawar10322746PHD_Edited.pdf
- University of Reading. “Otto and Marie Neurath Isotype Collection.” https://www.isotyperevisited.org/isotype-collection/
- Widgit. “Widgit Symbol Set.” https://www.widgit.com/about-symbols/widgit_symbol_set.htm
- Yu, B., et al. “Crowdsourcing Participatory Evaluation of Medical Pictograms…” https://www.jmir.org/2013/6/e108/
- Zhang, D., et al. “Investigation of the Contributory Factors to the Guessability of Traffic Signs.” https://pmc.ncbi.nlm.nih.gov/articles/PMC6338990/
- “Understanding small graphical symbols: a cross-cultural study.” https://www.sciencedirect.com/science/article/pii/S0169814101000075
- “Evaluation of Pharmaceutical Pictograms by Older ‘Turkers’.” https://pmc.ncbi.nlm.nih.gov/articles/PMC7897753/
- “Augmentative and alternative communication intervention for in-patient people with post-stroke aphasia.” https://pmc.ncbi.nlm.nih.gov/articles/PMC8611624/
- Blissymbols overview. https://en.wikipedia.org/wiki/Blissymbols
- Egyptian hieroglyphs overview. https://en.wikipedia.org/wiki/Egyptian_hieroglyphs
- iConji overview. https://en.wikipedia.org/wiki/IConji
- LoCoS overview. https://en.wikipedia.org/wiki/LoCoS_%28language%29
- Makaton history overview. https://en.wikipedia.org/wiki/Makaton
- Toki Pona overview. https://en.wikipedia.org/wiki/Toki_Pona
