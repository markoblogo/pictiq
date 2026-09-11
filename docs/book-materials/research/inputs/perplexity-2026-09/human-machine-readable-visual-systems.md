The strongest precedents for Pictiq are not QR codes themselves, but systems that maintain a **dual contract**: a person can infer or inspect meaning from the visible form, while software can recover a precise identifier, structure, relationship, or action from the same artifact. Their central lesson is that human legibility and machine reliability usually cannot come from one undifferentiated visual layer; successful systems use deliberate layers, redundancy, constrained syntax, and stable identifiers.

For Pictiq, the promising direction is a visual protocol in which each tile sequence remains readable as a compact human message, but also serializes unambiguously into canonical JSON, IDs, grammar roles, and optionally a camera-friendly verification layer.

## **Design space**

There are several distinct forms of “human- and machine-readable.” Pictiq can choose among them rather than trying to maximize every property in every context.

| Pattern | What a person reads | What a machine reads | Main advantage | Main tradeoff |
| ----- | ----- | ----- | ----- | ----- |
| Human-first semantic notation | Symbols, spatial relations, compact visual grammar | Structured parse from known symbol IDs and syntax | Expressive and teachable | Vision recognition and ambiguity need careful control |
| Machine-first carrier with human label | Text, icon, serial, or short explanation beside a barcode | Encoded record, identifier, or URI | Very reliable machine data capture | The code itself has little intuitive meaning |
| Hybrid visual token | Icon plus a constrained machine-recognition pattern | Symbol identity, orientation, pose, sometimes metadata | Works with cameras at distance and in physical space | Can compromise visual elegance |
| Diagram plus formal model | Flowchart, schematic, map, or model | Graph, schema, entity relationships, constraints | Rich structure and interoperability | Users need diagram literacy; authoring is heavier |
| Operational symbol system | Standard shape, color, frame, icon, modifiers | Code values and structured fields | Fast recognition under time pressure | Requires training and strict conventions |
| Accessible semantic layer | Visible sign or icon; optionally text | Alt text, semantic ID, speech output, location/action metadata | Supports assistive tech and search | The visible artifact alone may not convey full precision |

Pictiq can support all six, but should make clear which mode it is in. A traveler’s physical tile card, a chat message, an agrimarket dashboard alert, and an AI-agent message do not require the same amount of machine certainty.

## **Fiducials and physical hybrids**

### **AprilTag and ArUco: visual identity plus robust camera localization**

AprilTag and ArUco are **fiducial-marker systems**: deliberately artificial, high-contrast visual patterns designed for camera detection. AprilTag is used in robotics, augmented reality, and camera calibration; its detector can identify a tag and estimate its precise 3D position and orientation relative to a camera. Its coding is designed for robust detection under variation in viewing angle and lighting.\[[april.eecs.umich](https://april.eecs.umich.edu/software/apriltag)\]

ArUco uses a wide black border and an inner binary matrix. The border enables rapid candidate detection; the binary interior identifies the marker, and the marker dictionary can support error detection and correction. Its four corners also provide sufficient geometry for camera pose estimation.\[[docs.opencv](https://docs.opencv.org/4.13.0/d5/dae/tutorial_aruco_detection.html)\]

These systems are nearly the inverse of Pictiq’s current ambition:

| Dimension | AprilTag / ArUco | Pictiq opportunity |
| ----- | ----- | ----- |
| Primary audience | Machine vision system | Human and machine |
| Human semantic content | Almost none; people see a technical label | High; people can read a message or concept |
| Machine identity | Extremely strong, discrete marker ID | Should be explicit, stable, and verifiable |
| Error handling | Hamming-distance dictionaries and error correction | Could use canonical tile IDs, checksums, syntax validation, and vision confidence |
| Orientation/layout | Designed for pose estimation | Could preserve tile boundaries and reading direction for deterministic parsing |
| Aesthetic quality | Functional, intentionally artificial | Must remain legible, attractive, and culturally acceptable |

The Pictiq lesson is **not** to decorate each tile with black-and-white tag patterns. That would make Pictiq look like industrial tracking infrastructure and undermine its semantic and aesthetic purpose.

Instead, borrow the underlying engineering:

* Define a finite, versioned tile dictionary with IDs that do not change.  
* Ensure tile silhouettes or internal distinguishing features have measurable visual separation.  
* Use a quiet margin, consistent square frame, and fixed alignment grid.  
* Encode reading direction, tile boundary, and sequence segmentation visibly.  
* Design for rotation, perspective distortion, glare, partial occlusion, printing variation, and low-resolution camera capture.  
* Measure visual confusion as a formal distance problem, not only as a subjective design question.  
* Add a small sequence-level integrity mechanism where necessary.

A practical hybrid could reserve a subtle machine layer in each Pictiq tile:

Human layer:  
  pictogram \+ color/style \+ familiar square tile

Structural layer:  
  fixed frame \+ orientation notch \+ semantic-role zone

Machine layer:  
  canonical ID encoded through border geometry, micro-pattern,  
  or a visible-but-low-salience checksum band

The machine layer should verify an already interpretable pictogram, not replace it.

### **GS1 DataMatrix: structured payload plus human-readable interpretation**

GS1 DataMatrix carries structured business data in a compact 2D symbol and can be accompanied by a human-readable interpretation. The encoded values can represent product identity, expiry, batch, serial number, and other standardized fields; GS1 Application Identifiers specify what each data element means.\[[gs1](https://www.gs1.org/standards/gs1-datamatrix-guideline/25)\]\[[truegtin](https://truegtin.com/blog/gs1-datamatrix-complete-guide)\]

This offers an important semantic architecture:

Visible label:        “Olive oil · Lot A37 · Best before 2027-05”  
Machine payload:      GTIN \+ batch \+ expiry \+ serial  
Shared semantics:     Field identifiers define how software interprets the values

The human and machine do not decode exactly the same pixels in the same way. Rather, they access the **same underlying record** through complementary renderings.

For Pictiq, this supports a clean three-representation model:

Canonical semantic message  
        ↓  
Pictiq visual rendering       Human-readable gloss / speech output  
        ↓  
Optional QR, DataMatrix,  
NFC, URL, or embedded metadata

For example, a physical Pictiq product label for a food item or a tourism card could show:

\[FOOD\] \+ \[NO NUTS\] \+ \[ASK STAFF\]

Semantic record:  
{  
  "concepts": \["core:food", "allergy:nuts", "core:negate", "core:ask-staff"\],  
  "intent": "allergen-warning",  
  "locale": "fr-FR",  
  "version": "pictiq-1.1"  
}

The pictogram sequence remains meaningful to a person; a scanner gets exact allergen, language, source, and version metadata. This is superior to forcing a human to interpret a generic barcode, but safer than expecting an image model to infer medical-critical detail from an icon alone.

## **Structured visual languages**

### **BPMN: a diagram that has both operational semantics and XML**

Business Process Model and Notation is designed to be understandable by business stakeholders while being precise enough for translation into software process components. It uses a flowchart-like notation independent of a particular implementation environment.\[[omg](https://www.omg.org/spec/BPMN/machine-readable)\]

BPMN’s important architecture is that the visual diagram and the machine representation are distinct but linked. A BPMN file contains both process-model semantics and diagram/interchange information. Software can convert XML into the diagram or vice versa, allowing compatible tools to exchange models. The standardized form distinguishes the process model’s semantics from the layout used to draw it.\[[camunda](https://camunda.com/blog/2024/08/why-bpmn-interchange-is-so-important/)\]\[[omgwiki](https://www.omgwiki.org/bpmn-miwg/lib/exe/fetch.php?media=20150611_submission.pdf)\]

Pictiq should adopt the same distinction:

Semantics:  
  concepts, operators, roles, relations, sequence,  
  scope, target, confidence, time, context-pack version

Presentation:  
  tile order, grouping, line breaks, color theme,  
  glyph style, spatial layout, animation, display scale

Do not equate the SVG layout with the message’s only truth. An SVG is a rendering. The canonical message should be a graph or ordered abstract syntax tree that can generate:

* A Pictiq tile row.  
* A compact card.  
* A screen-reader utterance.  
* Plain-language text.  
* An AI-agent structured message.  
* A localized rendering.  
* A QR/NFC payload when physical linkage is useful.

This makes Pictiq much more than an icon font or sticker set. It becomes a semantic protocol with a visual surface.

### **SysML v2: multiple synchronized views over a formal model**

SysML v2 is a systems-modeling language based on a formal metamodel, with both textual and graphical syntax. Implementations emphasize two-way synchronization between textual and graphical model views, and the broader ecosystem uses standardized interchange/API mechanisms for machine interoperability.\[[omg](https://www.omg.org/sysml/SysML-2.htm)\]\[[3ds](https://www.3ds.com/products/catia/catia-magic/sysmlv2)\]\[[dalus](https://dalus.io/resources/what-is-sysml-v2)\]

The transferable lesson is **round-tripping**:

\\text{Pictiq AST/JSON} \\rightarrow \\text{SVG tiles} \\rightarrow \\text{parsed Pictiq AST/JSON}

For the subset that Pictiq claims is machine-readable, this round trip should preserve meaning. A renderer should be deterministic, and a parser should recover the same canonical ID sequence and grammatical structure—possibly with a confidence score if input is a photograph rather than source SVG.

This suggests three conformance levels:

| Level | Claim | Appropriate use |
| ----- | ----- | ----- |
| Visual | A person can recognize the tiles and infer the message | Art, merchandise, informal social use |
| Semantic | A source file or accessible metadata deterministically specifies concepts and relations | Websites, documents, UI, accessibility, search |
| Vision-robust | A camera can recover the message or stable IDs from a printed/displayed instance under stated conditions | Physical cards, wayfinding, devices, robotics, inventory, AR |

Do not claim level 3 merely because an AI vision model can sometimes guess a tile’s meaning. Level 3 requires a tested visual encoding and a defined error model.

### **Ontologies: concept identity is separate from image and wording**

In the Semantic Web, ontologies provide machine-readable concepts and relations that let data from different sources be annotated and interpreted consistently. The visible human presentation may vary, but the underlying URI or identifier preserves conceptual identity.\[[link.springer](https://link.springer.com/rwe/10.1007/978-3-540-92913-0_13)\]

That is highly applicable to Pictiq Context Packs. A Pictiq tile should ideally map to a stable concept identifier, while labels and artwork remain separate:

Concept identity:  
  pictiq:core:water

Visual asset:  
  /tiles/core/water.svg

French label:  
  eau

English labels:  
  water; drink; hydration

AAC speech output:  
  “I need water.”

Semantic relations:  
  broaderThan: liquid  
  usableAs: object, action, condition  
  pack-specific specialization:  
    agri:irrigation-water  
    medical:oral-fluid

A core tile can intentionally be broad, but the semantic model needs a way to distinguish broader, narrower, related, deprecated, and context-specific readings. That is how Pictiq can remain human-friendly without becoming opaque to software.

## **Operational symbols and diagrams**

### **Military tactical symbology: a visual grammar with a code underneath**

MIL-STD-2525 is a standardized system for military operational symbols. It explicitly combines symbol sets for command and control with a coding scheme for automation and information transfer, plus display requirements intended to support interoperability. Modern tactical-symbol systems use a structured identifier together with visual rules—frame, icon, color, modifiers, and an entity catalogue—to generate symbols consistently.\[[worldwind.arc.nasa](https://worldwind.arc.nasa.gov/milstd2525c/Mil-STD-2525C.pdf)\]\[[corvusintell](https://corvusintell.com/blog/c2-systems/app6-vs-mil-std-2525-symbology/)\]

Its model is not appropriate to copy aesthetically or politically, but it is architecturally instructive:

Machine structure:  
  identity \+ affiliation \+ status \+ domain \+ entity \+ modifiers

Visual rendering:  
  frame \+ central icon \+ fill/color \+ indicators \+ text modifiers

The representation has explicit semantic slots. A trained person reads them visually; a system stores, transmits, filters, and renders them as structured fields.

For Pictiq, this validates a grammar where meaning comes from **role, order, attachment, and modifier position**, not only from the pictogram drawing. A tile should answer a constrained question:

* What concept is this?  
* What semantic role is it playing?  
* What does it modify or relate to?  
* Is it core, pack-specific, urgent, negated, completed, requested, or uncertain?  
* Is it a literal object, an action, a status, or a category?

However, tactical symbology also warns against overloading. Its symbols become dense, require training, and are optimized for expert operational use rather than first-time public comprehension. Pictiq should preserve a low-barrier “plain visual message” layer and reveal technical modifiers only when a pack needs them.

### **ISA-5.1 and P\&IDs: symbol plus identifier plus relationship**

ANSI/ISA-5.1 standardizes symbols and identification methods for industrial measurement, monitoring, and automation. Its purpose is to let a reader with reasonable plant knowledge understand a process’s measurement and control arrangement without needing all specialist details. The notation combines graphical symbols with an identification code.\[[isa](https://www.isa.org/products/ansi-isa-5-1-2024-instrumentation-and-control-symb)\]\[[isa](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa5-1)\]

A piping and instrumentation diagram does not merely show objects. It makes relationships visible:

* A solid process line can show material flow.  
* Distinct line conventions distinguish pneumatic, electrical, hydraulic, and data signals.  
* Instrument tags encode the measured variable, function, loop number, and optional suffix.\[[pathnovo](https://pathnovo.com/standards/isa-5-1/cheat-sheet)\]  
* The symbol’s placement in the diagram establishes what it observes, controls, or affects.

The lesson for Pictiq is that **relations deserve first-class visual treatment**. If Pictiq only places independent icon tiles next to each other, it risks becoming a bag of tags. To become a machine-readable language, it needs specified relations:

SEQUENCE        A → B  
ACTOR           PERSON —does→ ACTION  
TARGET          ACTION —on→ OBJECT  
LOCATION        EVENT —at→ PLACE  
TIME            EVENT —at→ TIME  
NEGATION        NOT —scopes→ CONCEPT  
QUANTITY        NUMBER —measures→ OBJECT  
CONDITION       IF —governs→ ACTION

These may be represented by order, spacing, containers, arrows, attachment points, or small relation tiles. The design should be constrained enough that a human sees the relation quickly and software has only one valid parse.

The P\&ID caution: diagrams grow unreadable when every edge style, label, tag, and modifier competes for attention. Pictiq should use a small relation inventory and make advanced diagrammatic layout optional.

## **Accessible machine-readable signage**

### **Public pictograms: direct comprehension first**

ISO 7001 public-information pictograms aim to communicate in places used by the public without relying on a shared spoken language or strong verbal ability. They are useful for transport, toilets, parking, information, and accessibility contexts—but a static pictogram alone generally does not expose structured digital semantics to software.\[[pictograms](https://www.pictograms.info/organizations/iso.htm)\]

The accessibility opportunity is to add a semantic companion rather than assume the pixels are enough:

\<svg  
  role="img"  
  aria-labelledby="pictiq-title pictiq-desc"  
  data-pictiq="core:toilet;core:accessible"  
  data-pictiq-version="1.0"\>  
  \<title id="pictiq-title"\>Accessible toilet\</title\>  
  \<desc id="pictiq-desc"\>  
    Pictiq: FACILITY \+ TOILET \+ ACCESSIBLE.  
  \</desc\>  
\</svg\>

That lets:

* A sighted person see a pictogram.  
* A screen reader announce the intended meaning.  
* Search and content systems index the concept.  
* A Pictiq-aware app recognize the semantic ID without computer vision.  
* A translation layer deliver French, English, Ukrainian, or another local rendering.  
* A vision system use the layout as an extra verification signal rather than the sole source of truth.

For physical signage, put the machine-readable record in a linked channel: NFC, a short URL, an adjacent code, Bluetooth beacon, or a visually integrated fiducial strip when appropriate. The core public message should still work without a phone.

### **Accessibility codes should preserve intent, not only appearance**

For Pictiq, accessible output should be generated from the canonical message, not written as a loose afterthought. A visual sequence such as:

\[PERSON\] \[WHEELCHAIR\] \[NEED\] \[TOILET\]

may need different outputs depending on intent:

* “I need an accessible toilet.”  
* “Where is the accessible toilet?”  
* “This toilet is accessible.”  
* “The accessible toilet is unavailable.”

The same visible tiles can be insufficient if the system does not encode predicate roles, tense/status, interrogative form, or scope. The accessibility layer forces the grammar to become explicit—which is also what machine interpretation needs.

## **Direct comparison with Pictiq**

| System family | Human interpretability | Machine determinism | Spatial / physical robustness | Expressive breadth | Best Pictiq lesson | What Pictiq should avoid |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| AprilTag / ArUco | Very low | Very high | Very high | Very low | Fixed frames, orientation, visual distance, dictionary discipline, error handling | Replacing semantic pictograms with arbitrary binary patterns |
| GS1 DataMatrix \+ HRI | Moderate, via label | Very high | High | High for records | Canonical fields, stable IDs, human/machine complementary views | Treating raw payload encoding as a visual language |
| BPMN | Moderate–high for trained users | High | Low–medium | High for processes | Separate abstract semantics from diagram layout; serialize and interchange models | Uncontrolled freeform layouts and ambiguous edges |
| SysML v2 | Moderate for experts | High | Low | Very high | Multiple synchronized representations and round-trip tests | Requiring users to author formal models for casual messages |
| Tactical symbology | High for trained specialists | High | Medium | High inside its domain | Semantic slots, modifiers, deterministic rendering | Excessive density, specialist opacity, militarized visual language |
| P\&ID / ISA-5.1 | High for trained operators | Medium–high | Low | High for industrial processes | Relations, tags, explicit line/attachment semantics | Too many edge types and diagram clutter |
| ISO public symbols | High for familiar public tasks | Low alone | High | Low–medium | Comprehension testing, visual simplicity, independent usefulness | Claiming that a recognizable pictogram is automatically machine-readable |
| Ontologies \+ semantic markup | Indirect unless rendered | Very high | N/A | Very high | Separate concept ID, labels, visuals, and relations | Treating English names or SVG filenames as stable semantics |

Pictiq’s distinctive position can be:

> **Human-first semantic tiles, backed by a canonical machine model, with an optional vision-robust physical rendering profile.**

That is more meaningful to people than fiducials, lighter than BPMN/SysML, more compositional than conventional signage, and more legible to humans than a pure ontology or barcode.

## **Recommended Pictiq architecture**

### **1\. Define a canonical abstract message**

Treat every Pictiq utterance as an ordered abstract syntax tree or graph, not simply a sequence of SVG filenames.

{  
  "protocol": "pictiq",  
  "version": "1.0",  
  "message\_id": "urn:uuid:…",  
  "intent": "request",  
  "locale\_hint": "fr-FR",  
  "nodes": \[  
    {  
      "id": "n1",  
      "concept": "core:person",  
      "role": "agent",  
      "reference": "self"  
    },  
    {  
      "id": "n2",  
      "concept": "core:need",  
      "role": "predicate"  
    },  
    {  
      "id": "n3",  
      "concept": "travel:check-in",  
      "role": "object"  
    },  
    {  
      "id": "n4",  
      "concept": "travel:lodging",  
      "role": "location"  
    }  
  \],  
  "relations": \[  
    \["n1", "agent-of", "n2"\],  
    \["n2", "object", "n3"\],  
    \["n3", "at", "n4"\]  
  \],  
  "rendering": {  
    "profile": "core-linear-1",  
    "direction": "ltr",  
    "theme": "default"  
  }  
}

The visible tile sequence becomes one valid rendering:

PERSON \+ NEED \+ CHECK-IN \+ LODGING

The canonical form can generate localized text:

* English: “I need to check in at my accommodation.”  
* French: “Je dois m’enregistrer à mon hébergement.”  
* Ukrainian: “Мені потрібно зареєструватися в помешканні.”

The rendering does not have to encode every grammatical detail through a new distinct glyph. But the data model must preserve the distinctions.

### **2\. Separate identity, artwork, and semantics**

Each tile needs at least these identifiers:

Concept ID:             core:water  
Tile asset ID:          pictiq.tiles.water.v1  
Visual style:           outline-round  
Pack source:            org.pictiq.core  
Semantic version:       1.0.0  
SVG checksum/hash:      optional integrity value  
Accessible description: “Water / drink / hydration”

This permits a re-drawn or themed WATER tile while preserving the underlying semantic concept. It also enables alternate visual styles—for children, low vision, monochrome printing, signage, or merchandise—without destroying interoperability.

### **3\. Define a visual parsing profile**

A machine-readable visual language must specify what makes a tile parseable from pixels.

At minimum, define:

* Canonical square aspect ratio and viewBox.  
* Outer-frame thickness and protected quiet zone.  
* Orientation cue or unambiguous reading-direction convention.  
* Tile-to-tile spacing and grouping rules.  
* Fixed attachment positions for modifiers and relations.  
* A maximum allowed visual complexity at small display sizes.  
* Contrast requirements for physical and digital rendering.  
* Prohibited near-duplicate silhouettes.  
* SVG metadata requirements.  
* A test set of rotated, blurred, low-light, skewed, partially occluded, and low-resolution examples.

ArUco’s use of a marker dictionary and error correction illustrates why a symbol inventory must be designed for distinguishability, not only visual charm. For Pictiq, evaluate silhouette distance, internal-feature contrast, and confusion rates between neighboring tiles such as GO/COME, OPEN/CLOSE, YES/NO, UP/DOWN, HELP/EMERGENCY, FOOD/MEDICINE, or HOME/LODGING.\[[docs.opencv](https://docs.opencv.org/4.13.0/d5/dae/tutorial_aruco_detection.html)\]

### **4\. Use two machine-recognition routes**

Do not depend on image recognition alone.

| Route | How it works | Where it fits |
| ----- | ----- | ----- |
| Semantic-native | The SVG, HTML, app state, API payload, or JSON includes Pictiq concept IDs and structure | Websites, apps, documents, agent communication, generated images |
| Vision-native | A camera identifies tiles by standardized visual form, geometry, optional fiducial cues, and grammar validation | Printed cards, signs, labels, AR, embedded devices |
| Linked data | A QR/NFC/URL/beacon resolves a richer canonical message or live context | Dynamic status, inventory, navigation, product traceability, high-stakes communication |

If a source is digital, use semantic-native parsing. It is more accurate, accessible, searchable, localizable, and cheap than screenshot-based vision.

If the source is physical, vision-native recognition can read the visible message. Add linked data where the message requires precision beyond the tile grammar—for example, exact allergen data, a live train platform change, commodity price timestamp, room number, medication information, or emergency instructions.

### **5\. Use grammar as error correction**

A major Pictiq advantage over standalone pictograms is that structured syntax can improve machine recognition.

Suppose vision is uncertain whether a tile is `core:water` or `core:medicine`. In the message:

PERSON \+ NEED \+ ? \+ NOW

both may be grammatically valid. But in:

PLANT \+ NEED \+ ? \+ DRY

`WATER` is semantically and grammatically much more likely. The parser can retain uncertainty rather than falsely claim certainty:

{  
  "observed\_tile": "t3",  
  "candidates": \[  
    {"concept": "core:water", "vision\_confidence": 0.73},  
    {"concept": "medical:medicine", "vision\_confidence": 0.22}  
  \],  
  "grammar\_adjusted\_choice": "core:water",  
  "overall\_confidence": 0.91,  
  "needs\_confirmation": false  
}

This resembles error correction in a broader sense: constrained syntax and context reduce the effective ambiguity of noisy visual input. But for safety-critical cases, never silently “correct” a medically or operationally consequential ambiguity. Ask, display a confidence warning, or retrieve the authoritative linked record.

## **Tradeoffs Pictiq must choose**

### **Aesthetic purity versus technical robustness**

* Clean, expressive tiles support human adoption, merchandise, publishing, and social use.  
* Orientation marks, fixed borders, strict spacing, and checksums improve computer vision.  
* The practical compromise is a base human style plus an optional **Scan Profile** for physical machine-readable use.

A gallery poster can use expressive Pictiq. A warehouse label, AR trail marker, or emergency card should use Pictiq Scan Profile.

### **Broad semantic primitives versus deterministic parsing**

* Broad primitives make the vocabulary small and composition powerful.  
* Machines need explicit type, role, scope, and relation information.  
* Preserve broad primitives in the lexicon, but encode contextual interpretation in canonical structure and, where necessary, visible grammar.

Do not force separate primitive tiles for every reading of WATER, PLACE, PERSON, MARK, or MOVE. Do require that a machine-readable message states whether the concept is an object, action, condition, location, target, or modifier.

### **Vision-AI flexibility versus standards-grade reliability**

* Vision-language models may recognize novel artwork and infer intent from context.  
* They are probabilistic and can hallucinate, drift between model versions, or overgeneralize culturally familiar imagery.  
* Deterministic parsing requires fixed assets, explicit grammar, conformance tests, and versioned dictionaries.

Use AI recognition as a convenience layer, not the definition of protocol compliance. A Pictiq Vision Profile should publish measurable requirements such as minimum image resolution, allowable perspective angle, expected lighting, maximum occlusion, recognition rate, false-positive rate, and behavior below confidence threshold.

### **Compactness versus recoverability**

* Dense symbol sequences increase visual efficiency.  
* Explicit role markers, spacing, relation connectors, and redundancy make parsing safer.  
* Let communication mode determine the balance.

For example:

Informal chat:  
  \[ME\] \[COFFEE\] \[NOW?\]

Travel card:  
  \[PERSON\] \[NEED\] \[TOILET\] \[ACCESSIBLE\]

Machine/physical scan:  
  \[PERSON-role\] \[NEED-predicate\] \[TOILET-object\] \[ACCESSIBLE-modifier\]  
  \+ fixed grid \+ orientation cue \+ encoded version

The semantic message can remain identical, while the render profile changes.

## **Practical roadmap**

1. Publish a concise **Pictiq Abstract Syntax Specification**: IDs, roles, relations, composition, scope, packs, versioning, and semantic conformance.  
2. Maintain the JSON lexicon as the authoritative registry. SVG files should reference canonical concept IDs rather than act as the semantic source of truth.  
3. Create a deterministic renderer from JSON/AST to SVG and a reference parser for source SVG/HTML. Test semantic round trips.  
4. Define `Pictiq Visual Profile 1`: square frame, orientation, grid, spacing, scale, contrast, modifier placement, and required accessibility metadata.  
5. Create a separate `Pictiq Scan Profile 1`: stricter geometry, robust tile distinctions, optional micro-identifier or fiducial border, test images, and confidence/error behavior.  
6. Design a small relation grammar before expanding the noun catalog: sequence, actor, action, target, location, time, quantity, negation, condition, question, urgency, and completion are more important for machine interpretation than hundreds of extra object icons.  
7. Ship a conformance suite:  
   * Valid and invalid JSON messages.  
   * Canonical rendered SVG fixtures.  
   * Human recognition tests.  
   * Screen-reader expected outputs.  
   * OCR/vision camera test images.  
   * Pack/version compatibility tests.  
   * Ambiguity and deprecation cases.  
8. Publish a confidence policy for vision interpretation:  
   * High confidence: parse automatically.  
   * Medium confidence: show candidate reading or request confirmation.  
   * Low confidence: fall back to manual selection, linked data, or text.  
   * Safety-critical: require explicit confirmation or an authoritative semantic-native/linked source.

## **Bottom line**

Pictiq should not compete with QR, DataMatrix, AprilTag, or ArUco as a dense machine code. Those systems gain reliability by being visually arbitrary, redundant, and narrow in semantic ambition.\[[april.eecs.umich](https://april.eecs.umich.edu/software/apriltag)\]\[[docs.opencv](https://docs.opencv.org/4.13.0/d5/dae/tutorial_aruco_detection.html)\]

Instead, Pictiq can occupy a valuable middle layer: **a compositional visual language that humans can read directly and machines can parse from a formal semantic representation**. Borrow fixed geometry and error-thinking from fiducials; canonical data fields and human-readable companions from GS1; semantic/layout separation and interchange from BPMN; synchronized representations from SysML; role-and-modifier grammar from tactical and industrial notation; and semantic metadata plus accessible alternatives from web standards.\[[gs1](https://www.gs1.org/standards/gs1-datamatrix-guideline/25)\]\[[omg](https://www.omg.org/spec/BPMN/machine-readable)\]\[[omg](https://www.omg.org/sysml/SysML-2.htm)\]\[[link.springer](https://link.springer.com/rwe/10.1007/978-3-540-92913-0_13)\]\[[isa](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa5-1)\]

The decisive design principle is simple: the Pictiq drawing should communicate meaning to people, while a stable, versioned grammar and concept registry make that meaning recoverable—not guessed—by machines.

