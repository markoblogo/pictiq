Intentional polysemy is valuable when a single sign gives users a stable **conceptual centre** and its different readings can be recovered from grammar, composition, situation, or interface context. It becomes harmful when users must distinguish meanings that have different consequences but lack a reliable contextual cue.

For Pictiq, the key distinction is not “one glyph \= one dictionary word.” It is: **can one primitive consistently evoke one mental model, while contextual mechanisms select its intended use?** Polysemy is a compression tool; unmarked ambiguity is a decoding cost.

## **Core distinction**

In linguistics, **polysemy** is one form with multiple *related* meanings; it differs from homonymy, where unrelated meanings merely share a form. The relatedness matters: “paper” can mean a physical sheet, a document, or an academic article because those senses form a connected conceptual family.\[[direct.mit](https://direct.mit.edu/coli/article/50/1/351/118497/Polysemy-Evidence-from-Linguistics-Behavioral)\]

A productive minimal visual language usually has:

* A broad **core meaning**: the invariant concept a user recognizes.  
* Predictable **extensions**: figurative, functional, grammatical, or compositional readings derived from that core.  
* **Disambiguators**: position, modifiers, surrounding symbols, frame, color, interaction state, or domain.  
* A way to request or express **precision** when it matters.

It fails when a symbol’s possible readings are unrelated, equally plausible in the same context, or lead to an unsafe/wrong action.

A useful shorthand:

\\text{Keep one primitive} \\quad \\text{if} \\quad  
\\text{relatedness} \+ \\text{contextual recoverability} \> \\text{cost of added ambiguity}.

## **What minimal languages show**

### **Toki Pona: broad roots plus compositional repair**

Toki Pona deliberately uses a small lexicon—roughly 120–137 content words—with broad semantic ranges. Its words have fluid grammatical roles: *moku* can mean “food” as a noun, “eat” as a verb, or “edible” as a modifier according to position. This is not merely a vocabulary shortcut; grammar does work that English often assigns to distinct lexical items.\[[en.wikipedia](https://en.wikipedia.org/wiki/Toki_Pona)\]

Its successful pattern is especially relevant to Pictiq:

| Design feature | Toki Pona pattern | Pictiq analogue |
| ----- | ----- | ----- |
| Broad primitive | *tomo* spans built enclosures, rooms, houses, and even vehicles; *lipu* spans sheets, paper, documents, websites, and blogs. \[[aclanthology](https://aclanthology.org/2026.scil-main.4.pdf)\] | One “container/enclosure” or “surface/document” primitive, not separate primitives for every implementation |
| Role assigned by context | Word position can determine whether a root is noun-like, verb-like, or modifier-like. \[[arxiv](https://arxiv.org/html/2508.10246v1)\] | Syntax slot, UI location, or a small role marker determines object/action/property |
| Precision on demand | More words can be combined when a broad root is insufficient, such as *jan pona* for friend (“good person”). \[[en.wikipedia](https://en.wikipedia.org/wiki/Toki_Pona)\] | Compound symbols such as PERSON \+ CARE for “caregiver,” or DOCUMENT \+ WEB for “web page” |
| Tolerated underspecification | Speakers omit distinctions that do not matter in the immediate situation. | Allow a primitive to remain broad in low-stakes browsing, ideation, metadata, or expressive use |
| Repair mechanism | Speakers expand the phrase or ask for clarification. Toki Pona explicitly encourages adding description where detail matters. \[[tokipona](https://tokipona.org/clarifying)\] | Let users add a qualifier, tap for a choice, or view a gloss/label |

The lesson is not that ambiguity is harmless. Rather, a tiny lexicon works because it has **regular compositional conventions** and because speakers can choose more specificity when needed. The FAQ’s claim that detailed language remains possible by adding descriptive terms captures the design principle: start broad, then refine only when the task demands it.\[[tokipona](https://tokipona.org/clarifying)\]

### **Blissymbolics: primitives, combinations, and explicit mode marking**

Blissymbolics makes the same trade-off in a more visibly systematic way. It uses a limited set of recurring key characters—around 120—which can be combined to derive a much larger vocabulary. A basic character has a semantic core, while combinations form more specific “Bliss-words.”\[[blissymbolics](https://www.blissymbolics.org/index.php/component/content/article?id=10&Itemid=0)\]

Crucially, Blissymbolics does not rely solely on the viewer’s intuition:

* Its components are semantic building blocks rather than isolated illustrations.\[[media.medfarm.uu](https://media.medfarm.uu.se/play/attachmentfile/video/7849/The_structure_of_Blissymbolics,_handouts.pdf)\]  
* It marks word class and grammatical forms with indicators above the symbol.\[[media.medfarm.uu](https://media.medfarm.uu.se/play/attachmentfile/video/7849/The_structure_of_Blissymbolics,_handouts.pdf)\]  
* A similar graphical base can be made more concrete or more abstract with markers; Unicode documentation gives the contrast between “feeling” and “heart,” and “measurement” and “ruler.”\[[unicode](https://www.unicode.org/L2/L2023/23138-n5228-blissymbols.pdf)\]  
* Its construction rules distinguish a classifier from following specifiers in a compound.\[[media.medfarm.uu](https://media.medfarm.uu.se/play/attachmentfile/video/7849/The_structure_of_Blissymbolics,_handouts.pdf)\]

That suggests a powerful Pictiq architecture: retain a broad root, but make its **semantic type** and **scope** legible. A heart-like primitive, for example, should not have to mean emotion, bodily organ, affection, favorite, health, and “like” with no cue. It can remain one family only if a marker, compound, or UI slot tells users whether the intended reading is:

* HEART \+ BODY → anatomical heart  
* HEART \+ FEELING → emotion/affection  
* HEART \+ CARE → emotional support or care  
* HEART \+ STAR/SELECT → favorite  
* HEART \+ HEALTH → cardiology/heart health

The graphical economy comes from reusing the root; clarity comes from visibly encoding the distinction.

## **Natural semantic fields and emoji**

Natural languages routinely organize vocabulary as networks rather than clean, non-overlapping boxes. The word “head,” for example, can refer to a body part, leader, top/end, mind, or a toilet; the uses remain historically and conceptually connected, but only work because syntax and discourse narrow the intended sense. Polysemy research defines exactly this pattern as “multiple distinct but related interpretations.”\[[direct.mit](https://direct.mit.edu/coli/article/50/1/351/118497/Polysemy-Evidence-from-Linguistics-Behavioral)\]

Emoji work similarly—but with a crucial warning for Pictiq.

### **Emoji succeed when social context is rich**

A single emoji can communicate an object, action, attitude, discourse move, or tone:

* ❤️ can mean a heart, love, support, approval, favorite, sympathy, or “I saw/acknowledge this.”  
* 🔥 can mean literal fire, danger, heat, enthusiasm, excellence, virality, or urgency.  
* 👀 can mean looking, attention, monitoring, interest, suspicion, or “I’m following this.”

These readings are often successful in a chat because sender identity, preceding text, platform convention, shared culture, and low stakes do most of the disambiguation. Emoji ambiguity is also sometimes the point: it preserves interpersonal softness or playful indirection.

### **Emoji fail when used as precise operational language**

The same looseness is risky in product UI, instructions, data systems, interfaces, accessibility controls, navigation, compliance, healthcare, or emergency contexts. A flame beside a commodity price might mean “hot market,” “risk,” “alert,” “top performer,” or “production issue.” If the action differs, the sign needs a qualifier, label, or separate concept.

For Pictiq, emoji demonstrate that culturally learned, broad primitives can be memorable—but they are poor evidence that a standalone glyph is sufficient for a controlled language.

## **Signage and AAC: contexts where ambiguity costs more**

### **Signage: one public message, not expressive breadth**

Public-information signage prioritizes quick, consistent recognition by strangers in noisy, multilingual environments. ISO 7001 covers graphical symbols for public information in publicly accessible places, and notes that symbols can be paired with text to improve comprehension. The underlying design assumption is clear: a sign should reduce the user’s decision burden, not invite semantic exploration.\[[iso](https://www.iso.org/standard/77442.html)\]

ISO-oriented guidance also describes symbols as normally conveying **one** public-information message and belonging to one category. That is a strong default for Pictiq whenever a pictogram tells a user where to go, what is available, what is prohibited, or what action to take.\[[blog.ansi](https://blog.ansi.org/ansi/iso-7001-2023-registered-public-information-symbols/)\]

The practical consequence:

* A toilet icon can cover a broad enough family—restroom, toilets, sanitary facilities—because the desired next action is essentially the same: locate/use the facility.  
* A person-with-suitcase icon might ambiguously mean baggage claim, luggage storage, travel information, or “traveler.” Those lead to different paths, so it should split or be composed/labelled.  
* A cross symbol can be medically ambiguous across cultures and contexts; “first aid,” “hospital,” “pharmacy,” and “emergency care” should not collapse into one generic health primitive if users must choose a destination.

### **AAC: reduce symbol burden without limiting expression**

AAC systems use pictures, icons, words, gestures, and other symbols to let people communicate. The appropriate vocabulary should be functional, personally meaningful, and tailored to the communicator’s real daily needs; assessment includes teaching symbols in relevant contexts and testing their understanding and use.\[[forbesaac](https://www.forbesaac.com/post/navigating-symbolic-terrain-in-aac-assessment)\]

Two AAC findings are particularly transferable:

* A pictographic symbol is not interpreted in isolation; the surrounding communication board or display affects its iconicity and usability. Perceptually and semantically distinctive symbols help reduce ambiguity.\[[repository.up.ac](https://repository.up.ac.za/bitstreams/37607383-84c9-4004-a1b6-bce35e47b07b/download)\]  
* Users may need symbols for people, actions, objects, locations, questions, and social language—not just highly imageable nouns.\[[forbesaac](https://www.forbesaac.com/post/navigating-symbolic-terrain-in-aac-assessment)\]

Therefore, broadness is often helpful in AAC when it gives a user faster access to flexible, high-frequency language such as WANT, GO, MORE, STOP, GOOD, HELP, or NOT. But it becomes damaging if a single symbol hides distinctions the communicator repeatedly needs to express—for example, different kinds of pain, consent/refusal, medication vs. food, or family members with different communication consequences.

A good Pictiq test is: **does consolidation make the user’s next message easier, or does it force the user to explain away the icon afterward?**

## **Criteria for Pictiq**

Use the following decision framework before creating a new primitive. Score each proposed merge or split qualitatively—high, medium, low—then test it with real tasks.

| Criterion | Keep one broad primitive when… | Split into contextual concepts when… |
| ----- | ----- | ----- |
| Conceptual kinship | Meanings share a clear prototype or causal/functional relation | Meanings are merely associated, visually similar, or translated by the same English word |
| Stable visual anchor | One image naturally evokes the shared core | The image privileges one sense so strongly that other readings feel arbitrary |
| Context recoverability | Sentence role, neighbor symbols, category, screen location, or modifier makes one sense overwhelmingly likely | Two readings remain plausible in the same actual use case |
| Action equivalence | All readings prompt the same user action or decision | Readings require different actions, destinations, permissions, or data operations |
| Stakes of error | Misreading is reversible, low-cost, and easy to repair | Misreading could create harm, loss, exclusion, legal/compliance failure, or lost time |
| Frequency balance | One core is frequent; rarer senses can be expressed by compounds | Multiple senses are independently frequent and users search for them separately |
| Compositionality | Modifiers systematically yield the required sub-concepts | Combinations are long, hard to parse, or inconsistent across the grammar |
| Learnability | Users can infer or learn the extension from examples | Users must memorize an exception or repeatedly ask what it means |
| Cultural robustness | Intended readings travel well across languages and cultures | Meaning depends on a local convention, metaphor, color, or platform-specific emoji use |
| Accessibility | The broad symbol remains distinguishable from nearby symbols and works with labels/speech output | Similar-looking or semantically crowded symbols increase selection and recall errors |

### **A practical threshold**

Keep one primitive only if all of the following are true:

1. The meanings form a coherent family, not a coincidence.  
2. The symbol has an identifiable invariant core.  
3. At least one reliable disambiguator is present in normal use.  
4. Misinterpretation does not change a high-stakes action.  
5. The system offers a short, regular way to request specificity.  
6. First-time and returning users can identify the intended interpretation in realistic tasks.

If either of these is true, split:

* Users must choose among senses **before** they can see the context.  
* The distinction changes what the system will do.

## **A Pictiq design pattern**

A robust model would use **three levels**, rather than treating every concept as either a one-off icon or an overburdened universal glyph.

### **1\. Broad primitives**

These are reusable semantic roots with strong imageability and high combinatorial value:

* PERSON  
* PLACE  
* CONTAINER  
* PATH / DIRECTION  
* BODY  
* HAND  
* EYE / SEE  
* MOUTH / SPEAK  
* MARK / DOCUMENT  
* TIME  
* MOVE  
* TAKE / GIVE  
* GROW  
* WATER  
* VALUE / MEASURE

The primitive should name a semantic domain, not pretend to encode every final lexical meaning.

### **2\. Contextual operators**

Use a small, visible mechanism to constrain interpretation:

* **Role**: thing, action, property, relation, question, negation  
* **Scope**: physical, digital, social, institutional, temporal  
* **State**: available, desired, completed, prohibited, urgent  
* **Direction**: toward, from, through, into, out of  
* **Viewpoint**: self, other person, group, public

This is the Blissymbolics lesson: grammar and type markers relieve the base sign from doing all the semantic work.\[[media.medfarm.uu](https://media.medfarm.uu.se/play/attachmentfile/video/7849/The_structure_of_Blissymbolics,_handouts.pdf)\]\[[unicode](https://www.unicode.org/L2/L2023/23138-n5228-blissymbols.pdf)\]

### **3\. Conventional compounds**

Reserve distinct, stable compounds for concepts people retrieve as units:

* EYE \+ DOCUMENT → read / inspect document  
* EYE \+ ALERT → watch / monitor  
* PERSON \+ PATH → visitor / traveler, depending on domain marker  
* WATER \+ GROW → irrigation  
* FIELD \+ VALUE \+ TIME → market or time-series indicator  
* PLACE \+ SLEEP → accommodation  
* PLACE \+ FOOD → restaurant/food venue

If a compound becomes extremely frequent, users consistently treat it as one concept, and its composition is no longer transparent, it can graduate into a lexicalized symbol or shortcut. That creates growth without prematurely expanding the primitive inventory.

## **Evaluation protocol**

Do not settle this purely by semantic intuition. Test candidate primitives in the situations where Pictiq will actually be used.

1. **Create a sense map.** For every primitive, list its proposed readings, the invariant core, its likely modifiers, and the contexts in which each reading occurs.  
2. **Write minimal-pair tasks.** Hold the glyph constant and vary only the intended meaning. For example, can users distinguish EYE \+ DOCUMENT (“read”), EYE \+ ALERT (“monitor”), and EYE \+ PERSON (“watch someone”)?  
3. **Measure first interpretation.** Show the unlabelled symbol in its expected interface or sentence frame. Record the first reading, confidence, and time-to-answer—not only whether a user can accept the intended gloss after being told it.  
4. **Test production as well as recognition.** Ask users to select a symbol to express an intended meaning. A sign can be understandable after the fact but still fail as a tool people can retrieve quickly.  
5. **Inspect confusion asymmetry.** If A is often mistaken for B but B is not mistaken for A, the visual prototype likely belongs to B. Split, redraw, or add a disambiguator rather than blaming users.  
6. **Run high-stakes tests separately.** A symbol that works in an exploratory content tool may be unacceptable for navigation, transactions, alerts, accessibility, or anything safety-related.  
7. **Use labels during transition.** Signage standards explicitly allow symbols to be used with text to improve comprehension. Pictiq can similarly use a visible or accessible gloss while its conventions are still being learned.\[[iso](https://www.iso.org/standard/77442.html)\]

## **Bottom line**

Pictiq should preserve a broad primitive when it behaves like a **productive semantic root**: its senses are related, its image communicates a stable core, context selects the reading reliably, and compounds or operators supply precision when needed.

It should split when one glyph becomes a **choice point with no visible choice architecture**—especially when meanings are unrelated, users encounter them independently, the next action differs, or an incorrect reading has material consequences. Toki Pona shows how a small vocabulary can remain expressive through context and compositional elaboration; Blissymbolics shows why visible grammar and systematic compounds matter; signage and AAC show that user context, distinctiveness, and the cost of error must ultimately govern the design.\[[tokipona](https://tokipona.org/clarifying)\]\[[blissymbolics](https://www.blissymbolics.org/index.php/component/content/article?id=10&Itemid=0)\]\[[repository.up.ac](https://repository.up.ac.za/bitstreams/37607383-84c9-4004-a1b6-bce35e47b07b/download)\]

