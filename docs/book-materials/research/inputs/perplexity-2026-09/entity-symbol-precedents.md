Visual naming systems distinguish a **unique referent**—this specific person, family, place, institution, deity, product, or character—from a reusable lexical concept such as PERSON, PLACE, BIRD, WATER, or HOUSE. Their central lesson for Pictiq is that Entity Symbols need a different contract from ordinary semantic tiles: they need consent, stable identity binding, collision handling, context/namespace, lifecycle rules, and a way to remain recognizable across repeated narrative use.

A Pictiq `PERSON` tile can mean any person. A Pictiq Entity Symbol should mean *this person in this story, conversation, community, or account*—without pretending that a visual resemblance, association, or logo is a globally unique identity on its own.

## **Entity symbols versus concepts**

A lexical Pictiq tile should be reusable and compositional:

PERSON  
HOME  
WATER  
MOVE  
HELP  
CHILD  
WORK  
FAMILY

An Entity Symbol is referential:

this person  
this team  
this vessel  
this farm  
this city  
this restaurant  
this fictional character  
this organization  
this recurring object

The semantic distinction matters:

| Property | Lexical concept | Entity Symbol |
| ----- | ----- | ----- |
| Refers to | A category, action, property, or relation | One particular individual/entity within a scope |
| Example | `core:person` | `entity:anton-biletskyi-volokh` |
| Meaning source | Shared Pictiq lexicon and grammar | A registry, story bible, user profile, map layer, or declared context |
| Can be reused globally? | Usually yes | Only if namespace and identity authority support it |
| Can be inferred from drawing alone? | Often partially | Usually no; drawing cues need a known context |
| Main risk | Polysemy | Mistaken identity, impersonation, stereotyping, collision, stale reference |
| Best rendering | Standard tile | Portrait, chosen badge, associative token, logo, map label, or a compound |
| Primary test | “Do users understand the concept?” | “Do users resolve this to the intended entity?” |

A generic person icon plus a colour or hairstyle may look personalized, but it is still not a safe identity system unless the system declares who it refers to. A portrait can improve recognition, but it still requires consent, update policy, and scope. A logo can indicate a company to people who know it, but it is not semantically self-explanatory.

## **Precedents**

### **Sign-language name signs**

Sign languages have one of the strongest precedents for Pictiq Entity Symbols because they distinguish ordinary lexical signs from socially situated names. Name signs function both to identify people in conversation and to signal membership in a signing community. They are commonly classified as arbitrary, descriptive, or nontraditional/hybrid.\[[project-easier](https://www.project-easier.eu/news/2021/10/28/name-signs/)\]

The main types map closely to your proposed categories:

| Name-sign type | How it identifies | Pictiq parallel | Principal risk |
| ----- | ----- | ----- | ----- |
| Arbitrary / initialized | A conventional handshape, often related to an initial letter, plus location/movement | Self-chosen abstract badge or monogram-like Entity Symbol | Meaning is opaque outside the community |
| Descriptive | A salient personal characteristic, behavior, occupation, or feature | Associative symbol or stylized portrait cue | Can become reductive, outdated, mocking, or imposed |
| Nontraditional / hybrid | Combines initialized and descriptive components | Initial/ID marker \+ chosen association | More recognizable but more visually complex |

Descriptions of name-sign practice note that arbitrary signs often use a handshape tied to a person’s name, whereas descriptive signs can draw on personal characteristics, work, movement, or tendencies. These are not generic public labels: assignment and acceptance are embedded in community norms.\[[lifeprint](https://www.lifeprint.com/asl101/pages-layout/namesigns3.htm)\]\[[deafservicesunlimited](https://deafservicesunlimited.com/deaf-history-month-name-signs/)\]

**Pictiq lesson:** a person’s Entity Symbol should normally be **self-chosen or community-confirmed**, not assigned by an app, manager, AI model, or designer based on perceived appearance.

A sound default policy:

Self-chosen:  
The entity chooses a symbol or approves one.

Context-bound:  
Its identity is valid inside a declared space:  
a story, team, conversation, family, account, or project.

Optional association:  
Personal traits or visual cues are opt-in and can be changed.

Stable identifier:  
The rendered visual mark maps to an internal entity ID.

No automatic profiling:  
Pictiq must not derive an Entity Symbol from race, gender,  
age, nationality, disability, religion, body shape, or facial traits.

This aligns with Pictiq’s broader principle of representing functional facts and needs rather than imposing identity categories.

### **Heraldry: visual identity plus strict differencing**

Heraldry was designed to make a person, family, office, institution, or polity recognizable through a structured visual composition. A coat of arms is a unique personal emblem and may be inherited; official registries can record granted, registered, approved, or confirmed arms.\[[gg](https://www.gg.ca/en/heraldry)\]

Heraldry is especially instructive for four reasons:

1. **Visual identity is compositional.**  
   Meaning comes from a structured grammar of field, tincture, division, charges, placement, and arrangement—not merely a single illustration.  
2. **Uniqueness is an explicit requirement.**  
   The purpose of arms is identification, so sufficient visual distinction matters.\[[heraldicscienceheraldique](https://www.heraldicscienceheraldique.com/chapter-iii-arms-versus-logo.html)\]  
3. **A registry resolves collisions.**  
   A device becomes attributable through a register, authority, and legal/social convention—not because no two images could ever look alike.  
4. **Small modifications can encode relationship.**  
   Heraldic cadency differentiates related bearers of arms through small marks of difference, such as a label, crescent, mullet, martlet, annulet, fleur-de-lis, rose, cross moline, and double quatrefoil.\[[college-of-arms.gov](https://www.college-of-arms.gov.uk/resources/the-law-of-arms)\]

This is a direct precedent for reusable Pictiq narrative/entity syntax:

Base entity:  
\[HOUSE OF RIVER\]

Related entity:  
\[HOUSE OF RIVER\] \+ \[RELATION / BRANCH MARK\]

Specific individual:  
\[HOUSE OF RIVER\] \+ \[PERSONAL DIFFERENCE MARK\]

However, Pictiq should not reproduce heraldry’s inherited status, complex genealogy, or historical gender rules. Borrow the **technical design principle**, not the social hierarchy:

> A shared base symbol can be differentiated by small, predictable, non-destructive modifiers when the relationship itself is relevant.

Possible Pictiq uses:

TEAM \+ role marker  
FAMILY \+ individual marker  
ORGANIZATION \+ regional branch marker  
FICTIONAL HOUSE \+ character-specific badge  
PROJECT \+ environment marker: test / staging / production  
VESSEL CLASS \+ hull-specific identifier

The key is that a modifier must have a declared relation. A coloured dot should not ambiguously mean “junior,” “private,” “inactive,” “European,” “female,” or “version two.”

### **Logos and trademarks**

A trademark is legally defined as a sign capable of distinguishing the goods or services of one enterprise from those of another. Protection may be obtained through national/regional registration or through the international Madrid System, and WIPO’s Global Brand Database includes more than 28 million records of marks, appellations of origin, and official emblems.\[[wipo](https://www.wipo.int/en/web/trademarks)\]

Brand marks are a useful but limited precedent:

* They show how a graphic symbol becomes a stable shortcut for a known entity.  
* They show the importance of distinctiveness and search/registration.  
* They show that an image can accumulate meaning through repeated use.  
* They show that familiar image-based logos can be preferred over text logos, while less familiar brands benefit from text because users lack learned association.\[[link.springer](https://link.springer.com/article/10.1007/s11747-020-00760-0)\]  
* They show that recognition is social and learned, not automatic.

The last point is crucial. A logo is not universally transparent; it works because users have encountered it, or because text and context teach the association. Research on brand marks finds that familiarity affects visual attention, search efficiency, and recognition accuracy. Large logo datasets likewise measure familiarity and recognition separately rather than treating one as guaranteed by the other.\[[link.springer](https://link.springer.com/article/10.1007/s12144-025-07839-3)\]\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649726/)\]

**Pictiq lesson:** a self-chosen Entity Symbol can become powerful through repetition in a bounded community, but new users need a discovery bridge:

First encounter:  
\[entity symbol\] \+ display name

Learning phase:  
\[entity symbol\] \+ short alias / role

Established narrative:  
\[entity symbol\] alone, if the audience demonstrably knows it

Accessible rendering:  
Entity Symbol → stable name/ID spoken or shown on demand

Do not use a personal Entity Symbol as a replacement for the legal name, account handle, organization name, or verified identifier in contracts, payments, access control, medical data, or other high-stakes contexts.

### **Cartographic symbols and place identity**

Maps distinguish between **feature class** and **feature instance**. A blue `P` can identify parking as a type of amenity; a label, coordinates, feature ID, map context, and geometry identify *this particular parking facility*. Map symbology uses form, size, pattern, color, and lightness to represent geographic features.\[[mapserver](https://mapserver.org/mapfile/symbology/construction.html)\]

OpenStreetMap’s documentation illustrates the distinction clearly: a single symbol may denote several kinds of point of interest or larger area, but when a map feature has a name, that name is usually displayed below the symbol.\[[wiki.openstreetmap](https://wiki.openstreetmap.org/wiki/OpenStreetMap_Carto/Symbols)\]

For Pictiq:

Category layer:  
\[PORT\]  
\[HOSPITAL\]  
\[TRAIN\]  
\[MARKET\]  
\[WAREHOUSE\]  
\[FIELD\]

Entity layer:  
\[PORT\] \+ “Nantes Saint-Nazaire”  
\[WAREHOUSE\] \+ “Dock C”  
\[FIELD\] \+ “Plot 7B”  
\[VESSEL\] \+ “IMO 1234567”

A pictorial symbol gives rapid class recognition. Unique-entity resolution requires at least one of:

* Proper name.  
* Map position or coordinates.  
* Registry identifier.  
* Visual portrait/photo.  
* Contextual anchoring in a current screen/story.  
* Stable entity URI/UUID.

For your logistics and agrimarket interests, this is decisive. A `[PORT]` tile can support broad human understanding. But a cargo instruction needs exact reference:

\[WHEAT\] \[MOVE\] \[TO\] \[PORT\]

is visually comprehensible but operationally incomplete.

\[WHEAT\] \[MOVE\] \[TO\] \[PORT:NANTES-SAINT-NAZAIRE\]  
\[TERMINAL:CHEVIRÉ\] \[4\]

requires an entity registry and typed location data. The Pictiq layer can render a location badge, but backend identity should use stable IDs, coordinates, terminal codes, or linked operational systems.

### **Religious iconography: associative identification and narrative memory**

In Christian art, saints are often identified through recurring attributes or emblems associated with their life, work, martyrdom, or tradition: Peter with keys, Andrew with a saltire, Catherine with a wheel, Jerome with a lion or skull, and so on. These attributes helped illiterate viewers identify figures and scenes, while also giving saints a recognizable visual personality.\[[en.wikipedia](https://en.wikipedia.org/wiki/Saint_symbolism)\]

This is a powerful precedent for **associative Entity Symbols**:

Person or character  
\+  
chosen recurring attribute  
\=  
narrative shorthand

Examples for a fictional Pictiq narrative might be:

Character A \= \[PERSON\] \+ \[RED SCARF\]  
Character B \= \[PERSON\] \+ \[BICYCLE\]  
Character C \= \[PERSON\] \+ \[STAR MAP\]  
Character D \= \[PERSON\] \+ \[TEA CUP\]

The association does not need to be literal. It can encode an object, accomplishment, place, habit, profession, ethical role, fictional event, or chosen metaphor.

But religious iconography also shows the weakness of associative naming:

* The symbolism depends on prior cultural knowledge.  
* The same attribute can identify multiple figures.  
* Attribution can change by artistic tradition, time, or region.  
* An attribute can flatten a person into one story, role, suffering, or stereotype.  
* Recognition works best within a trained interpretive community.

**Pictiq lesson:** associative symbols should be treated as **narrative handles**, not self-sufficient identity proofs. Their meaning should be discoverable through an entity card, legend, hover/long-press label, alt text, or story introduction.

A strong design pattern:

First mention:  
\[ENTITY:ALINA\] \+ \[ASSOCIATION:BICYCLE\]  
“Alina — the bicycle courier”

Subsequent mention:  
\[BICYCLE-ALINA\] / \[her Entity Symbol\]

Expanded access:  
Entity Symbol → “Alina, courier and neighborhood guide”

The person remains the referent; the association is a recall cue.

### **Pictographic and logo-syllabic scripts**

Maya writing is a useful contrast because it combines logograms, which represent words or concepts, and syllabograms, which represent sounds. It can therefore encode proper names in more than one way:\[[worldhistoryedu](https://worldhistoryedu.com/maya-glyph-the-writing-system-of-the-maya-civilization/)\]\[[mayaarchaeologist.co](https://www.mayaarchaeologist.co.uk/public-resources/maya-world/maya-writing-system/)\]

* Through a meaningful logographic sign.  
* Through phonetic spelling.  
* Through a combination of semantic and phonetic elements.  
* Through titles, lineage markers, place associations, and conventional iconography.

The “Emblem Glyph” became a recognizable sign associated with particular Maya kingdoms; before full decipherment, researchers treated these as unique “logos” of city-states.\[[mayan](https://mayan.org/symbols/emblem-glyph/)\]

The lesson for Pictiq is to preserve two separate pathways for entities:

Semantic/associative path:  
A self-chosen icon or compound evokes a narrative association.

Phonetic/label path:  
A displayed name, initials, transliteration, or stable text/voice form  
disambiguates the entity.

Machine-identity path:  
A persistent entity ID ensures exact reference.

Pictiq should not force all names into icon rebuses. Rebus naming is playful and memorable but fragile across languages.

For example:

“Rose” → \[ROSE\]  
“Pierre” → \[STONE\]  
“Sunny” → \[SUN\]

works only in a language community that shares the phonetic/semantic pun. It becomes misleading in French, Ukrainian, Arabic, Japanese, or any unrelated language. It is suitable for fiction, games, informal group culture, or merchandise—not as a universal identity protocol.

## **Three Entity Symbol modes**

Pictiq should define self-chosen, portrait-based, and associative symbols as separate modes with distinct semantics and safeguards.

| Mode | What the image represents | Human advantage | Machine requirement | Main risk | Best uses |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Self-chosen symbol | A chosen abstract mark, badge, glyph, or personal emblem | Agency, privacy, stable narrative shorthand | Stable entity ID \+ owner consent \+ namespace | Unfamiliarity, collision, impersonation | Communities, games, projects, pseudonymous identity, private communication |
| Portrait-based symbol | A face, avatar, silhouette, photo, or stylized likeness | Fast recognition in a known group | Consent, privacy metadata, alternate name/ID, update/revocation policy | Biometric/privacy harm, aging/staleness, biased recognition, false match | Contacts, family boards, staff rosters, personal devices, consented story characters |
| Associative symbol | Object, creature, color, gesture, place, profession, story attribute | Memorable and expressive; supports recurring narrative reference | Entity ID \+ association definition \+ accessible label | Stereotype, outdated association, multiple people sharing cue | Fiction, education, recurring characters, informal group shorthand |
| Composite entity mark | Base person/org/place symbol plus modifiers | Scalable; expresses relationship, role, branch, version | Grammar for attachments and namespace registry | Overcomplexity and modifier collision | Teams, organizations, family/story relationships, operations |
| Text/phonetic companion | Proper name, initials, handle, code, label | Precise, searchable, translatable/voiceable | Stable ID mapping and locale labels | Less visual/minimal | First mention, legal/operational interfaces, accessibility, search |

### **Self-chosen symbols**

These should be the default for living people who want a visual identity. The person chooses, approves, changes, or revokes the mark.

A Pictiq Entity Symbol can be:

One simple base glyph:  
  a knot, comet, seed, wave, tool, geometric form

A controlled compound:  
  \[MOUNTAIN\] \+ \[DOT\]  
  \[STAR\] \+ \[PATH\]  
  \[LEAF\] \+ \[SQUARE\]

A personal variation:  
  core symbol \+ fixed, declared differentiator

Requirements:

* Do not infer identity categories from the mark.  
* Do not treat it as legal identity.  
* Require a namespace and entity ID.  
* Support aliases and historical symbols.  
* Make the symbol reversible: the person can replace it without invalidating old messages.  
* Preserve a text/speech equivalent for accessibility.  
* Run visual-confusion tests against nearby symbols and existing community marks.

### **Portrait-based symbols**

Portraits are highly effective when the target is a known individual, but they are **instances**, not semantic primitives. Use them for recognition, not inference.

Safe metadata:

{  
  "entity\_id": "did:pictiq:person:7c9e…",  
  "symbol\_mode": "portrait",  
  "display\_name": "Alina K.",  
  "image\_source": "user-uploaded",  
  "consent": {  
    "scope": "family-board",  
    "expires\_at": "2027-09-11",  
    "revocable": true  
  },  
  "alt\_text": "Portrait of Alina K.",  
  "not\_for": \[  
    "biometric-identification",  
    "automated-demographic-inference",  
    "public-indexing"  
  \]  
}

A Pictiq system should never claim that facial likeness offers robust universal identification. The image can be blurred, stylized, old, altered, culturally interpreted differently, unavailable to blind users, or dangerous in a humanitarian, employment, policing, migration, or public context.

### **Associative symbols**

Associations are excellent for stories and recurring collaboration because they make a character memorable. They should be chosen, reviewed, and contextualized.

Good associative choices:

* A favorite or signature object chosen by the person.  
* A recurring fictional motif.  
* A skill or role the person wishes to foreground.  
* A non-sensitive place/object in a shared story.  
* A narrative event used with consent.  
* A color/shape/systematic visual motif that differentiates characters.

Poor associative choices:

* Visible disability or medical condition.  
* Trauma, migration status, poverty, legal history, or family separation.  
* Race, ethnicity, nationality, religion, or gender presentation unless self-chosen and contextually appropriate.  
* Weight, height, body shape, age markers, or other physical traits imposed by others.  
* A stereotype linked to profession, culture, or class.  
* An embarrassing incident or a trait likely to become outdated.

A useful Pictiq rule:

> An associative Entity Symbol should identify someone by a relationship they endorse, not by a trait observers extract from them.

## **Identity, ambiguity, and namespace governance**

A visual identity mark does not become unambiguous simply because it is unique-looking. It needs a **resolution context**.

Same visual mark:  
\[BLUE BIRD\]

Possible meanings:  
a person in a family board  
a fictional character  
a local cycling club  
a social-media platform  
a birdwatching category  
a specific vessel  
a municipal environmental campaign

The renderer, human, and software need to know which namespace governs interpretation.

### **Recommended Pictiq entity addressing**

pictiq:core:person  
pictiq:entity:person:anton  
pictiq:entity:person:alina-k  
pictiq:entity:org:cropto  
pictiq:entity:place:nantes  
pictiq:entity:vessel:imo-1234567  
pictiq:story:river-city:character:mira  
pictiq:team:field-ops:member:delta

The visible symbol can remain compact:

\[COMET\]         → entity:person:alina-k  
\[WHEAT MARK\]    → entity:org:cropto  
\[WAVE \+ TOWER\]  → entity:place:nantes

But a canonical Pictiq message should carry the full reference:

{  
  "node\_id": "n1",  
  "type": "entity\_reference",  
  "entity\_id": "pictiq:story:river-city:character:mira",  
  "rendering": {  
    "symbol\_id": "story:river-city:mira-comet",  
    "mode": "associative"  
  },  
  "fallback": {  
    "display\_name": "Mira",  
    "spoken\_name": "Mira",  
    "locale": "en"  
  }  
}

### **Four namespace levels**

| Namespace level | Who governs it | Identity guarantee | Example use |
| ----- | ----- | ----- | ----- |
| Private | Individual or household | Unique only inside a private space | Family board, personal notes, home dashboard |
| Community | Group moderators or project maintainers | Unique within the community registry | Pictiq forum, club, classroom, cooperative |
| Narrative | Author/editorial canon | Unique inside a story/world | Graphic novel, game, tourism narrative, educational guide |
| Organizational | Verified organization | Bound to organizational records and permissions | Team roster, warehouse roles, tourism partner network |
| Public/global | Formal registry or decentralized identifier layer | Resolves beyond a single app/context, but requires high governance | Public organizations, registered marks, verified entities |

A Pictiq core standard should support every level but not falsely imply the same reliability.

### **Collision and similarity policy**

Heraldry and trademark systems both show that visual collision cannot be handled only by exact-pixel comparison. Humans confuse marks that are perceptually or conceptually similar.

Pictiq should check:

* Exact duplicate visual assets.  
* Near-duplicate silhouette.  
* Same symbol with only a low-visibility color difference.  
* Same symbol with a minor rotation/mirror change.  
* Similar association in the same narrative cast.  
* Collision at 24 px, not only at large SVG size.  
* Collision in monochrome, dark mode, print, and color-vision variation.  
* Collision with core grammatical operators such as NOT, HELP, DANGER, QUESTION, and CONFIRM.  
* Collision across installed Context Packs.

Suggested registry policy:

Core grammar symbols:  
Globally reserved. No Entity Symbol may look too similar.

Official public entity marks:  
Registry review and stable ID required.

Community entity marks:  
Collision check within the community namespace.

Private marks:  
User choice permitted, with local warnings only.

Narrative casts:  
Require distinctness among characters appearing in the same scene.

### **Lifecycle and revocation**

Unlike ordinary lexicon tiles, entities change:

* People change preferred names, symbols, pronouns, roles, and affiliation.  
* Portraits age or should be removed.  
* Organizations merge, rebrand, dissolve, or lose verification.  
* Places change name, jurisdiction, or status.  
* Story versions fork.  
* A person may withdraw permission for a symbol or portrait.

Use immutable entity IDs and versioned renderings:

{  
  "entity\_id": "pictiq:entity:person:7c9e…",  
  "display\_name\_history": \[  
    {"value": "A. B.", "valid\_until": "2026-09-11"},  
    {"value": "Anton Biletskyi-Volokh", "valid\_from": "2026-09-11"}  
  \],  
  "symbol\_history": \[  
    {"symbol\_id": "private:comet-v1", "status": "deprecated"},  
    {"symbol\_id": "private:comet-v2", "status": "active"}  
  \],  
  "resolution\_policy": "show-current-symbol-preserve-original-reference"  
}

Old narratives can retain the original symbol for historical coherence, while live systems can show a current symbol or a respectful replacement according to the entity’s preference.

## **Reuse in narrative**

Entity Symbols shine when they make repeated reference lighter than repeating a full name. They are especially useful for:

* Visual stories and comics.  
* Children’s material and language learning.  
* Tourism itineraries involving recurring guides, places, transport modes, or fictional mascots.  
* Team boards and project handoffs.  
* Family communication boards.  
* Pictiq instruction sequences with recurring actors.  
* Games and collaborative planning.  
* Agent/system dashboards, where an agent has a stable visual identity but its technical ID remains available.

### **Narrative introduction rule**

Use a three-stage convention:

1\. Establish:  
\[ENTITY SYMBOL\] \+ name \+ role/association

2\. Reinforce:  
\[ENTITY SYMBOL\] \+ short name or title

3\. Reuse:  
\[ENTITY SYMBOL\] alone within a bounded, recently established context

Example:

First panel:  
\[COMET PERSON\] Mira — route planner

Second panel:  
\[COMET PERSON\] \[CHECK\] \[MAP\]

Later:  
\[COMET PERSON\] \[GO\] \[PORT\]

The narrative audience learns the reference through repetition. This is how logos, heraldic arms, saint attributes, and sign-language name signs become efficient: not through innate universal transparency, but through **stable association in a community or story**.

### **Avoid cast collision**

A story with ten characters whose symbols are all animals, all colored circles, or all face silhouettes can be hard to parse. Use differentiated semantic anchors:

Mira:   comet / map motif  
Niko:   bicycle / route motif  
Sana:   seed / garden motif  
Ivo:    wave / boat motif

Then distinguish each at 24 px by silhouette and a fixed primary feature. The identifier should still be selectable and expandable to the character’s name.

## **Proposed Pictiq Entity Symbol specification**

### **Minimal entity record**

{  
  "entity\_id": "pictiq:story:harbor-notes:character:mira",  
  "entity\_type": "person",  
  "namespace": "pictiq:story:harbor-notes",  
  "status": "active",  
  "symbol": {  
    "id": "harbor-notes:mira-comet",  
    "mode": "associative",  
    "asset": "entities/mira-comet.svg",  
    "core\_base": "core:person",  
    "association": "comet",  
    "approved\_by\_entity": true  
  },  
  "labels": {  
    "en": \["Mira"\],  
    "fr": \["Mira"\],  
    "uk": \["Міра"\]  
  },  
  "accessible\_name": "Mira, the route planner",  
  "first\_use\_rendering": {  
    "show\_name": true,  
    "show\_role": true  
  },  
  "reuse\_rendering": {  
    "show\_name": false,  
    "show\_role": false  
  },  
  "created\_at": "2026-09-11",  
  "version": "1.0.0"  
}

### **Required rules**

1. **Every Entity Symbol resolves to a stable entity ID.**  
   The mark is a rendering, not the identity itself.  
2. **Every Entity Symbol belongs to a declared namespace.**  
   No visual symbol has a global meaning by default.  
3. **Living people choose or explicitly approve their symbol.**  
   Do not algorithmically derive a personal mark from appearance, demographic data, or behavioral profiling.  
4. **Portraits require explicit, revocable consent.**  
   State the display scope, public/private status, reuse policy, and accessibility fallback.  
5. **Associative symbols require an entity-approved relationship.**  
   They can represent a chosen affiliation or narrative motif, not an externally imposed label.  
6. **First mention includes a text/speech fallback.**  
   Use name, role, alias, or explanation until the referent is established.  
7. **Entity symbols cannot masquerade as core grammar.**  
   Reserve enough perceptual distance from high-impact operators—NOT, STOP, HELP, DANGER, QUESTION, CONFIRM, and URGENT.  
8. **Do not silently reuse or repurpose an entity symbol.**  
   Deprecate, alias, or retire it; preserve old references through versioned mapping.  
9. **Do not use Entity Symbols as legal, medical, financial, security, or consent identifiers without an authoritative linked record.**  
10. **Support public, narrative, organizational, community, and private identity profiles separately.**  
    The necessary verification and collision rules differ sharply.

## **Bottom line**

The best precedent for Pictiq Entity Symbols is not a single system but a combination:

* **Sign-language name signs** show how identification can be arbitrary, descriptive, or hybrid—and why social consent matters.\[[project-easier](https://www.project-easier.eu/news/2021/10/28/name-signs/)\]\[[lifeprint](https://www.lifeprint.com/asl101/pages-layout/namesigns3.htm)\]  
* **Heraldry** shows compositional visual identity, registries, visual distinctiveness, and small systematic marks for related entities.\[[gg](https://www.gg.ca/en/heraldry)\]\[[college-of-arms.gov](https://www.college-of-arms.gov.uk/resources/the-law-of-arms)\]  
* **Logos and trademarks** show that graphic marks become useful identifiers through stable repeated use, distinctiveness, governance, and learned familiarity—not innate universal legibility.\[[wipo](https://www.wipo.int/en/web/trademarks)\]\[[link.springer](https://link.springer.com/article/10.1007/s11747-020-00760-0)\]  
* **Cartography** shows how a category symbol becomes a unique place only when paired with a name, geometry, or identifier.\[[mapserver](https://mapserver.org/mapfile/symbology/construction.html)\]\[[wiki.openstreetmap](https://wiki.openstreetmap.org/wiki/OpenStreetMap_Carto/Symbols)\]  
* **Religious iconography** shows the narrative power of recurring associative attributes, while warning that associations depend on learned context and can reduce people to a single trait.\[[en.wikipedia](https://en.wikipedia.org/wiki/Saint_symbolism)\]  
* **Pictographic scripts** show that semantic association, phonetic labels, and formal identity can coexist rather than compete.\[[worldhistoryedu](https://worldhistoryedu.com/maya-glyph-the-writing-system-of-the-maya-civilization/)\]\[[mayan](https://mayan.org/symbols/emblem-glyph/)\]

For Pictiq, design Entity Symbols as **consented, namespaced visual references with a text/voice fallback**, not as universal pictures of identity. Let people choose abstract marks when privacy and agency matter; use portraits only in bounded, consented contexts; use associative motifs to make recurring narrative reference memorable; and always retain a stable ID beneath the visible symbol.

