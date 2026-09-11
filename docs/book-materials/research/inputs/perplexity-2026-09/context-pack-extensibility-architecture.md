A durable extensibility model separates a **small, interoperable core** from optional, versioned domain packs that add vocabulary, constraints, examples, and localized conventions without redefining the core. The systems that scale best do not merely permit additions: they define ownership, identifiers, compatibility rules, validation, release discipline, and a formal path for promoting widely useful extensions into the core.

For Pictiq, Context Packs should behave less like informal icon collections and more like **profiled, namespaced semantic modules** built on a stable visual grammar. A “Paris visitor” pack, “farm-market intelligence” pack, and “medical appointment” pack could share the same primitives and composition rules while introducing domain concepts, task flows, labels, and locally meaningful conventions.

## **Recurring architecture**

Across programming ecosystems, healthcare standards, controlled languages, alerts, and localization, the same layered structure appears:

| Layer | Purpose | Comparable systems | Pictiq equivalent |
| ----- | ----- | ----- | ----- |
| Core | Defines stable primitives, grammar, rendering rules, IDs, and minimum interoperability | Programming-language core; FHIR base resources; SNOMED CT International Edition; Unicode | Pictiq primitives, tile geometry, compositional syntax, semantic roles, accessibility behavior, canonical identifiers |
| Extension mechanism | Provides a sanctioned way to add concepts without changing the core | Modules/namespaces; FHIR extensions; SNOMED extensions; locale-data additions | Namespaced Context Pack concepts, compounds, modifiers, workflows, localized labels |
| Profile | Narrows or configures a base system for a specific operational setting | W3C profiles; FHIR implementation guides; CAP national profiles | “Pictiq Airport Wayfinding Profile,” “Pictiq Vineyard Operations Profile,” “Pictiq Emergency Shelter Profile” |
| Terminology set | Selects a controlled subset for a use case | SNOMED reference sets; CAP event-term lists; STE approved terminology | A pack’s allowed/required tile set, synonyms, deprecated forms, task-specific phrases |
| Implementation guidance | Explains how to use the system consistently in a real workflow | FHIR implementation guides; ASD-STE100 writing rules | Visual grammar guide, composition recipes, examples, anti-patterns, user-testing results |
| Localization | Changes labels, conventions, formats, and culturally specific references without changing meaning IDs | CLDR/LDML | French, English, Ukrainian labels; local place/category variants; cultural notes; alternate speech output |

The key is to keep these layers distinct. A local label should not create a new concept ID. A workflow-specific rule should not silently alter the universal grammar. A pack-specific compound should not be promoted to a core primitive just because it is useful in one commercial vertical.

## **Patterns from other systems**

### **Programming languages and DSLs: explicit modules prevent semantic collision**

Programming systems avoid a single global pool of names. A module or package acts as a bounded unit that owns functions, types, or symbols; namespace qualification prevents collisions. Rust’s move to put enum variants under their enum’s namespace illustrates the underlying principle: related terms should reside in a visible semantic container rather than leak into a flat global name space.\[[rust-lang.github](https://rust-lang.github.io/rfcs/0390-enum-namespacing.html)\]

YANG, a language for describing network data models, makes the module the base unit of definition and specifies that extension names from a module and its submodules share a defined identifier namespace. This is close to what Pictiq needs.\[[hjp](http://www.hjp.at/\(de\)/doc/rfc/rfc6020.html)\]

**Pictiq lesson:** give every extension a globally stable, namespaced ID, even if the visual form is local.

For example:

core:person  
core:place  
core:need  
core:time  
core:move

travel:lodging  
travel:check-in  
travel:bag-drop

agri-market:spot-price  
agri-market:delivery-window  
agri-market:quality-premium

fr-tourism:chateau  
fr-tourism:terroir-route

The display might show only the tile sequence, but the machine-readable layer should preserve the full identifier. That lets two packs both use “market” without accidentally treating a food market, financial market, marketplace, and market-price data point as the same concept.

A namespace should also signal **authority**:

pictiq:      Official core  
org:         Organization-maintained pack  
geo:         Geographic/local pack  
community:   Community experimental pack  
user:        Private personal vocabulary

For a project with SVG and JSON assets, that can be native rather than bureaucratic: every pack’s manifest can specify its namespace prefix, publisher, dependency range, pack version, terms, licenses, and compatibility level.

### **FHIR and W3C profiles: constrain first; extend second**

FHIR provides a particularly strong model. A profile is an extra set of rules over a base specification that makes the base structure suitable for a particular healthcare context. Implementation guides package these profiles with vocabulary, examples, documentation, and other artifacts needed to make real-world implementations consistent.\[[docs.cloud.google](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-profiles)\]\[[fire](https://fire.ly/blog/fhir-profiles-and-implementation-guides/)\]

France’s FR Core implementation guide is a concrete national model: it keeps a common foundation while defining profiles, extensions, and value sets for French administrative, patient, professional, organizational, encounter, vital-sign, and facility use cases.\[[build.fhir](https://build.fhir.org/ig/Interop-Sante/hl7.fhir.fr.core/)\]

W3C defines a profile as a named set of constraints on identified base specifications, tailored to achieve a particular function. Its profile vocabulary allows profiles themselves to be described in machine-readable form.\[[w3c.github](https://w3c.github.io/dxwg/profiles/)\]\[[w3](https://www.w3.org/TR/dx-prof-1.0/)\]

The governance principle is:

> Do not mint a new primitive merely because a domain needs a narrower interpretation of an existing one.

First ask whether the domain need can be represented as:

* A **profile constraint**: “In this pack, this concept must include a location modifier.”  
* A **value set**: “For this workflow, use only these approved concepts.”  
* A **compound**: “This domain term is a regular combination of core symbols.”  
* An **extension**: “This genuinely new concept cannot be expressed cleanly using the existing grammar.”  
* A new **core primitive**: only after broad, cross-domain evidence shows it is irreducible and commonly needed.

For Pictiq, a “Hotel Check-in” profile could require:

PERSON \+ ARRIVE \+ PLACE \+ IDENTITY-DOCUMENT

But it might offer a conventional short form:

travel:check-in

The short form remains semantically linked to its canonical compositional definition. This preserves speed and familiarity without creating an opaque isolated icon.

### **SNOMED CT: global core, authorized extensions, reference sets**

SNOMED CT maintains a large international terminology alongside national or local extensions. Extensions may address national and local needs, but they are managed by organizations issued a namespace identifier; recognition depends on the provider’s authorization and quality-control practices.\[[docs.snomed](https://docs.snomed.org/snomed-ct-practical-guides/snomed-ct-starter-guide/10-extension-and-customization)\]

In France, the national release center publishes the international edition monthly and a national edition annually, including French translation. That is a useful example of separating:\[[esante.gouv](https://esante.gouv.fr/produits-services/cgts/snomed-ct)\]

* A globally stable semantic base.  
* A nationally governed terminology layer.  
* Translation and local adaptation.  
* Formal release cadence.

SNOMED’s **reference sets** are especially relevant. Rather than forcing every implementation to load or expose the whole terminology, a reference set selects and organizes concepts for a particular purpose. Creating one requires explicit metadata and a module identifier associated with the authoring organization.\[[docs.snomed](https://docs.snomed.org/snomed-ct-practical-guides/snomed-ct-starter-guide/10-extension-and-customization)\]

For Pictiq, a Context Pack should have both:

1. **A semantic extension layer**  
   New concepts, compounds, role conventions, and definitions.  
2. **A practical reference-set layer**  
   A curated list of what users actually see for a task.

For example, a vineyard-operations pack might technically define 120 concepts but expose different reference sets:

| Reference set | Purpose | Example Pictiq concepts |
| ----- | ----- | ----- |
| `agri-vineyard:field-scouting` | Observing vines in the field | ROW, VINE, LEAF, PEST, DISEASE, PHOTO, NOTE, URGENT |
| `agri-vineyard:irrigation` | Managing water decisions | WATER, FLOW, VALVE, SENSOR, DRY, START, STOP, REPAIR |
| `agri-vineyard:harvest` | Coordinating picking and logistics | RIPE, PICK, CRATE, WEIGHT, TRAILER, TIME, QUALITY |
| `agri-vineyard:worker-safety` | Safety and welfare messaging | HELP, INJURY, HEAT, WATER, STOP, CALL, PLACE |

This avoids the common failure mode in icon systems: giving users hundreds of possible symbols when they need 12–30 symbols for one immediate workflow.

### **Controlled language: stable core plus sanctioned terminology allowance**

ASD-STE100, Simplified Technical English, illustrates a more restrictive but highly useful governance pattern. It is built for safety-sensitive technical documentation, where misreading can have serious consequences. Its controlled dictionary uses roughly 900 approved words, generally restricting each to one meaning and one part of speech, while allowing organizations to define additional approved technical nouns and verbs for domain needs.\[[github](https://github.com/danyuchn/asd-ste100-skill/blob/master/references/writing-rules.md)\]

Its governance is not “make the dictionary large until it covers everything.” It is deliberate lexical management: retain, consolidate, remove, narrow definitions, and impose usage restrictions to protect clarity, consistency, and translatability.\[[ceur-ws](https://ceur-ws.org/Vol-4219/paper4.pdf)\]

Pictiq should not copy the one-meaning-per-word rule everywhere; its strengths include broad primitives and intentional polysemy. But it should adopt the **exception model**:

* Core signs remain broad only where their contextual reading is predictable.  
* High-stakes packs can impose stricter meanings.  
* A pack may define technical concepts only through a documented allowance process.  
* Each extension must state what it means, where it is allowed, what it must not mean, and how it composes.

For instance, the core `WATER` tile can remain intentionally broad: water, liquid, watering, hydration, or wetness depending on grammar and neighboring tiles. But a medical pack should not use `WATER` alone for “oral fluid intake,” “intravenous fluid,” “dehydration,” or “water contamination.” It should constrain the allowable compounds and labels for safety.

## **Emergency systems: common syntax, local event vocabularies**

The Common Alerting Protocol (CAP) is a simple, general, all-hazard format for exchanging emergency warnings across different communication channels. It supports consistent dissemination across multiple warning systems while simplifying authoring.\[[itu](https://www.itu.int/en/ITU-D/Emergency-Telecommunications/Pages/Common-Alerting-Protocol-and-Call-to-Action.aspx)\]

The important pattern is that CAP separates:

* A common structured message envelope.  
* Standard fields for urgency, severity, and certainty.  
* An event vocabulary that can be profiled or localized.  
* Channel-specific presentation of the same semantic alert.

CAP event-term lists classify event types and provide names and code references for particular profiles, such as the Canadian CAP profile. This allows a jurisdiction to communicate locally meaningful hazards while retaining an interoperable message architecture.\[[publicsafety.gc](https://www.publicsafety.gc.ca/cnt/rsrcs/pblctns/capcp-vnt-rfrncs/index4-en.aspx)\]\[[docs.oasis-open](https://docs.oasis-open.org/emergency/cap-etl/v1.2/cap-etl-v1.2.html)\]

For Pictiq, an emergency Context Pack should work similarly:

Core grammar:  
ACTOR \+ EVENT \+ LOCATION \+ TIME \+ REQUIRED-ACTION

Pack-specific vocabulary:  
flood, wildfire, toxic-smoke, shelter, evacuation-route,  
heat-alert, medication, charging-point, reunification

Required alert fields:  
hazard, affected area, urgency, required action,  
time validity, source, language/locale, accessible fallback

The point is not to let a pack invent arbitrary syntax. The pack supplies domain terms and stricter content requirements while the core maintains recognizability and cross-pack interoperability.

This is an important safety boundary: a `pictiq:emergency` pack should be curated, versioned, reviewed by relevant practitioners, and distributed separately from playful or experimental visual packs.

## **Icons, emoji, and signage**

Icon ecosystems provide two complementary lessons.

Unicode emoji accepts concepts through an explicit selection process rather than simply standardizing every request. Its criteria include expected usage, distinctiveness, breadth, compatibility, and whether the new emoji covers a genuinely new concept rather than a variant already expressible through an existing emoji or sequence.\[[unicode](https://unicode.org/emoji/proposals.html)\]\[[unicode](http://www.unicode.org/faq/emoji_submission.html)\]

Pictiq can adopt a similar **anti-duplication rule**:

* Do not create an official pack symbol if a clear existing core composition already covers it.  
* Add a pack-level shorthand only if the concept is frequent, visually distinctive, operationally important, and materially faster or clearer than composition.  
* Reject new symbols that differ only by decoration, identity stereotype, local branding, or a trivial visual variant.  
* Treat multiple meanings as evidence of potential reuse, but not as proof that a glyph is safe in operational settings.

Public signage takes the opposite stance where stakes and speed matter: ISO 7001 symbols are designed for public-facing use, can be used with text, and are accepted on the basis of independent comprehension testing or demonstrated international use. The system emphasizes testing across cultures because visual intuition is not universal.\[[standards.iteh](https://standards.iteh.ai/catalog/standards/iso/4af0030c-050a-4a15-8fbb-d2398316999b/iso-dis-7001)\]

For Pictiq packs used in tourism, public-facing wayfinding, or accessibility, demand a lightweight version of the same evidence:

* Recognition testing with intended users.  
* Cross-language/cross-cultural review.  
* Tests at intended physical and digital sizes.  
* Confusion testing against visually adjacent tiles.  
* Text or speech fallback where recognition is not sufficient.

A Paris tourism pack can safely carry local concepts such as `fr-paris:metro`, `fr-paris:arrondissement`, `fr-paris:reservation-required`, or `fr-paris:market-day`, provided it does not pretend these are universally transparent primitives.

## **Localization: translate labels, not semantic identity**

Unicode CLDR separates structured locale data, a specification governing how it is represented and used, and tooling that gathers, validates, and transforms data. Its data are vetted by native speakers, linguistic experts, and Unicode membership. CLDR covers locale-specific names, formats, and validation rules rather than changing the underlying character repertoire for each locale.\[[cldr.unicode](https://cldr.unicode.org/)\]\[[hilton.org](https://hilton.org.uk/blog/l10n-cldr-names)\]

This yields a vital Pictiq rule:

> A concept ID is not its English label, French label, emoji resemblance, or visual interpretation.

For each Pictiq concept, separate at least four layers:

{  
  "id": "travel:check-in",  
  "canonical\_definition": "Registering a person's arrival for a booked service or accommodation.",  
  "composition": \["core:person", "core:arrive", "core:place", "core:confirm"\],  
  "labels": {  
    "en": \["check in", "registration"\],  
    "fr": \["enregistrement", "arrivée"\],  
    "uk": \["реєстрація", "заїзд"\]  
  },  
  "speech\_output": {  
    "en": "I need to check in.",  
    "fr": "Je dois m'enregistrer.",  
    "uk": "Мені потрібно зареєструватися."  
  },  
  "status": "pack-standard"  
}

The icon composition stays semantically stable; language packs determine how it is named, voiced, sorted, searched, and explained. This is particularly useful for a multilingual Pictiq book and for travelers who need a compact visual layer plus localized text support.

Avoid making locale packs semantic forks. “French label differs” is not a reason to create `fr:restaurant` and `en:restaurant` as two concepts. A new concept is justified only when the underlying socially or operationally relevant distinction genuinely differs.

## **Governance model for Context Packs**

Pictiq can retain an unusually small, stable core if it defines extension governance before the vocabulary becomes large. I would use five explicit tiers.

| Tier | Publisher | Stability | Typical contents | Example |
| ----- | ----- | ----- | ----- | ----- |
| Core | Pictiq maintainers | Very high | Primitives, syntax, semantic roles, rendering/accessibility rules | `pictiq:person`, `pictiq:need`, `pictiq:negate` |
| Official pack | Pictiq-maintained | High | Broad reusable domains, validated compounds, reference sets | `pictiq:travel`, `pictiq:food`, `pictiq:work` |
| Certified partner pack | Named organization or expert group | Medium–high | Profession-, region-, or institution-specific terms | `fr-tourism:*`, `agri-market:*`, `clinic-x:*` |
| Community pack | Public contributors | Experimental | Niche domains, art, events, hobbies, evolving practice | `community:trail-running:*` |
| Private/local pack | Individual or organization | Local only | Internal shorthand, temporary project vocabulary | `anton:field-notes:*` |

The core must never depend on a pack. Packs may depend on the core and, carefully, on other packs.

### **Pack manifest**

Every Context Pack should include a machine-readable manifest, akin to a package descriptor plus an implementation guide:

{  
  "id": "org.pictiq.agri-market",  
  "title": "Agricultural Market Intelligence",  
  "version": "1.0.0",  
  "status": "official",  
  "publisher": "Pictiq",  
  "license": "CC BY 4.0",  
  "requires\_core": "\>=1.0.0 \<2.0.0",  
  "depends\_on": \["org.pictiq.time", "org.pictiq.measure"\],  
  "default\_locales": \["en", "fr", "uk"\],  
  "domains": \["commodities", "pricing", "logistics"\],  
  "concepts": \["agri-market:spot-price", "agri-market:basis", "agri-market:delivery-window"\],  
  "reference\_sets": \["daily-price-brief", "trader-alert", "shipment-status"\],  
  "deprecated": \[\],  
  "governance\_url": "…",  
  "conformance\_level": "strict"  
}

The exact format can remain simple JSON initially. What matters is that the pack is identifiable, attributable, versioned, testable, and capable of declaring its relationship to the core.

### **Concept record**

Require each proposed concept to include:

* Stable, non-recycled ID.  
* Namespace and owning organization.  
* Short canonical definition.  
* Scope note: when it applies.  
* Exclusion note: what it explicitly does **not** mean.  
* Core decomposition or semantic parent.  
* SVG tile or canonical composition.  
* Labels and search aliases by locale.  
* Speech-output wording, if AAC or spoken output is supported.  
* Examples in full Pictiq messages.  
* Accessibility description.  
* Usage frequency or task evidence.  
* Visual-confusion risks.  
* Version introduced and deprecation/replacement metadata.  
* Test evidence for official/public/safety packs.

This turns a Context Pack into an inspectable semantic product rather than a folder of attractive icons.

## **Change rules**

A small stable core requires a conservative promotion policy.

### **Add to a pack when**

* The concept is specific to one domain, country, institution, profession, product, or workflow.  
* It has a clear definition but limited cross-domain frequency.  
* It can be represented as a regular composition but benefits from a convenient shorthand.  
* The pack can own the maintenance burden.  
* Its introduction does not change the meaning of an existing core symbol.

Examples:

* `fr-tourism:reservation-required`  
* `agri-market:contract-month`  
* `trail:aid-station`  
* `kitchen:induction-hob`  
* `software:pull-request`

### **Add to core only when**

* The concept recurs across several independent packs.  
* It is hard to express clearly through existing primitives and grammar.  
* It supports many future compounds, rather than only one pack.  
* It has broad cultural and linguistic usability.  
* It survives user testing without requiring specialized knowledge.  
* Its meaning is stable enough that future reinterpretation is unlikely.  
* The core team can commit to long-term backward compatibility.

Examples that may deserve core status over time are concepts like LOCATION, TIME, ASK, NEED, HELP, CHOOSE, CONFIRM, CANCEL, NOT, MORE, LESS, BEFORE, AFTER, and CAUSE—not “hotel lobby,” “fungicide interval,” or “Métro line transfer.”

### **Reject or defer when**

* The request is a visual variant of an existing composition.  
* The meaning depends on brand identity, a trend, or a short-lived UI convention.  
* The term is culturally loaded but has no clear functional definition.  
* Its use evidence comes from one contributor’s private habits.  
* It can be expressed with a label/search alias rather than a new symbol.  
* It is semantically unstable or combines several unrelated actions.

### **Deprecate; never silently repurpose**

Once published, do not change an ID’s meaning. This is one of the most important rules borrowed from data standards and programming ecosystems.

Instead:

Old: agri-market:cash-price  
Status: deprecated  
Replacement: agri-market:spot-price  
Meaning: unchanged for legacy decoding

A glyph may be visually improved in a carefully versioned way, but its semantic meaning must not silently drift. If the meaning has changed, create a new ID and map the old one explicitly.

## **Recommended Pictiq policy**

Adopt this concise constitutional rule:

> **The Pictiq Core defines how concepts compose. Context Packs define which domain concepts are useful. Profiles define which concepts and compositions are permitted or required in a task. Locales define how concepts are named and presented.**

From that rule, implement the following:

1. Keep the core semantically small, visually stable, compositional, and free of region-, industry-, brand-, and identity-specific concepts.  
2. Make every pack an explicit package with an owner, namespace, semantic version, dependencies, license, status, target audience, and compatibility range.  
3. Require a canonical definition and a “not this” exclusion note for every nontrivial pack concept. This is especially important for broad visual symbols whose apparent meaning can drift.  
4. Require every pack concept to declare either a core composition or an explicit rationale for why it is irreducible.  
5. Use profiles/reference sets to make interfaces task-sized. A user sees the 20 symbols needed for “check into a hotel” or “record grain delivery,” not every tile available in every installed pack.  
6. Separate semantic IDs from artwork, labels, search aliases, speech output, and local cultural notes. This lets Pictiq stay multilingual and lets the artwork evolve without breaking data.  
7. Establish three review tracks:  
   * Lightweight community review for experimental packs.  
   * Editorial and interoperability review for official packs.  
   * Expert, user-tested, strict-versioning review for public, AAC, medical, emergency, or safety-related packs.  
8. Publish a promotion path: experimental → community stable → official pack → core candidate. Promotion should require demonstrated use across unrelated contexts, evidence of compositional insufficiency, and regression testing against existing vocabulary.  
9. Build validation tooling early. A linter can check duplicate IDs, unmet dependencies, circular pack dependencies, missing translations, invalid compositions, visual collisions, inaccessible SVG metadata, deprecated references, and incompatible core versions.  
10. Maintain a public registry and compatibility matrix. Users should be able to discover which packs are official, experimental, deprecated, interoperable, localized, or suitable for public/safety use.

## **Applied example**

Consider a potential Pictiq pack for your agricultural commodities work:

Pack: org.pictiq.agri-market  
Profile: daily-grain-market-brief  
Core dependencies: time, measure, place, move, compare, alert

The pack can introduce:

* `agri-market:spot-price`  
* `agri-market:futures-contract`  
* `agri-market:basis`  
* `agri-market:delivery-window`  
* `agri-market:quality-premium`  
* `agri-market:port-congestion`

But it should not create new primitives for PRICE, TIME, PLACE, CHANGE, UP, DOWN, QUANTITY, DELIVERY, or ALERT if those already belong to the Pictiq core. It should define each domain term through canonical compositions, such as:

spot price        \= MARKET \+ VALUE \+ NOW  
futures contract  \= MARKET \+ VALUE \+ TIME-AFTER \+ AGREEMENT  
delivery window   \= MOVE \+ GOODS \+ TIME-RANGE  
quality premium   \= QUALITY \+ VALUE \+ MORE

Then the profile selects only the concepts needed for a daily brief and specifies a predictable message order:

COMMODITY \+ MARKET \+ VALUE \+ CHANGE \+ TIME \+ PLACE \+ ALERT

This yields the central benefit of Context Packs: people retain the ability to decode the shared grammar even when they do not know every specialist shorthand. The core remains learnable, while the ecosystem can grow to cover tourism, agritech, home cooking, outdoor activity, software collaboration, local services, and professional communication without collapsing into a single ungoverned icon catalogue.

