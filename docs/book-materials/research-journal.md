# Research journal

Chronological notes reconstructed from repository evidence. Interpretive statements are marked as such; dates follow commit or release history when a separate event date is unavailable.

## 2026-08-26 — Handbook v1 as project entry point

### Starting question

How can Pictiq be introduced as a usable protocol rather than only an icon collection?

### What happened

Handbook v1.0 was published as PDF and EPUB. It presented the protocol, core lexicon, context packs, physical layouts, storytelling, poetry, and machine-interface ideas.

### Evidence

[Handbook files](../../books/handbook-v1/), [release note](../../releases/handbook-v1.0.0.md), and commit [`153e639`](https://github.com/markoblogo/pictiq/commit/153e639).

### Decision / outcome

The handbook became the public entry point while the repository remained the evolving evidence and implementation record. Later architecture must not be retroactively inserted into Handbook v1.0.

### Why it matters

A stable explanatory edition and a changing engineering repository can coexist when their boundaries are explicit.

### Open questions

What belongs in a future handbook revision versus an archive or case study remains open.

### Possible future book use

Use as the opening case study for how a protocol acquires a public explanation before its architecture is complete.

## 2026-08-26 — Portable communication surfaces

### Starting question

What changes when the same vocabulary moves from a screen or document onto objects people carry?

### What happened

The repository added Paris shirt artwork, wallet cards, a nightlife lighter, a luggage tag, and a phone lockscreen. Content profiles separate primary from secondary tiles, while each layout adapts the profile to its physical surface.

### Evidence

[Layout rules](../../layouts/README.md), [portable-layout overview](../../layouts/overview/portable-layouts.png), [Paris profile](../../layouts/profiles/paris.json), [Nightlife profile](../../layouts/profiles/nightlife.json), [luggage tag](../../layouts/luggage-tag/travel-transit/), and [phone lockscreen](../../layouts/phone-lockscreen/personal-demo/). Relevant commits include [`6eb24a3`](https://github.com/markoblogo/pictiq/commit/6eb24a3), [`5e4bc33`](https://github.com/markoblogo/pictiq/commit/5e4bc33), and [`f058da6`](https://github.com/markoblogo/pictiq/commit/f058da6).

### Decision / outcome

Layouts became reusable representations of content profiles rather than redrawn icon sets. Physical constraints determine hierarchy, density, and context-specific vocabulary.

### Why it matters

The carrier is part of communication design: a wallet card, lighter, shirt, tag, and lockscreen provide different reading distances and attention conditions.

### Open questions

Usability and real-world comprehension were not measured in these repository artifacts.

### Possible future book use

A case-study chapter comparing how one protocol behaves across five portable surfaces.

## 2026-09-08 — From SVG validity to perceptual QA

### Starting question

Is a technically valid SVG also a successful communication symbol?

### What happened

The project introduced perceptual design principles and a staged visual-QA protocol after recognizing that structural checks alone could not establish recognition. Earlier icon work, including the cannabis silhouette and repeated person/fire iterations, exposed the need to inspect canonical, small-size, grid, and layout renders.

### Evidence

[Icon spec and Visual QA Protocol](../../spec/ICON_SPEC.md), [silhouette input rules](../../spec/SILHOUETTE_INPUTS.md), [QA tooling](../../tools/README.md), and commits [`7e9663d`](https://github.com/markoblogo/pictiq/commit/7e9663d), [`c5a1d0a`](https://github.com/markoblogo/pictiq/commit/c5a1d0a), [`3542c23`](https://github.com/markoblogo/pictiq/commit/3542c23), [`ee80d22`](https://github.com/markoblogo/pictiq/commit/ee80d22).

### Decision / outcome

The project adopted the practical lesson: **A structurally valid icon is not necessarily a perceptually successful icon.** It also recorded: **Preserve established morphology when recognition depends on it.** The final person and fire assets used a reference-driven trace workflow and still passed the normal QA gate.

### Why it matters

Recognition is an acceptance property, not a side effect of clean source geometry.

### Open questions

Broader human recognition studies and physical-size testing remain future work.

### Possible future book use

An engineering story about why “minimal” cannot mean removing the feature people use to recognize a symbol.

## 2026-09-08 — Kinneir / Calvert reference-system discovery

### Starting question

Which historical systems provide useful design lessons without becoming claimed ancestors of Pictiq?

### What happened

After Pictiq v1.0 was developed independently, Kinneir and Calvert’s British road-sign programme was identified as a relevant comparative reference system.

### Evidence

[Reference Systems](../../spec/ICON_SPEC.md#reference-systems) and [related-systems note](../research/related-systems.md).

### Decision / outcome

The useful patterns were design for decision, legibility under real conditions, system rules over isolated drawings, relative geometry, and contextual validation. The documentation explicitly avoids claiming direct inspiration.

### Why it matters

Historical comparison can sharpen engineering principles without rewriting project history.

### Open questions

The archive does not establish a complete comparative history of visual-language systems.

### Possible future book use

A short comparative interlude on how signage turns recognition into an operational requirement.

## 2026-09-08 — Toki Pona pilot crosswalk

### Starting question

What can a Toki Pona ↔ sitelen pona ↔ sitelen emoji ↔ Pictiq comparison reveal about semantic compression?

### What happened

An initial 20-word pilot classified mappings by direct, partial, composed, contextual, or absent equivalence. It exposed semantic mismatch and the importance of zero or near-zero direct lexical equivalence.

### Evidence

[Toki Pona interoperability repository](https://github.com/markoblogo/toki-pona-translator) and Pictiq’s [Toki Pona relationship](../../spec/PROTOCOL.md#11-embodied-and-standalone-communication).

### Decision / outcome

The crosswalk became a comparative research system after Pictiq’s initial protocol, not a source or ancestor of its architecture.

### Why it matters

Cross-system gaps are evidence about different compression mechanisms, not an automatic vocabulary backlog.

### Open questions

The pilot’s detailed table belongs in the Toki Pona repository rather than this archive.

### Possible future book use

Use the pilot as a compact experiment in why translation equivalence and protocol equivalence diverge.

## 2026-09-09 — Comparative visual-language research review

### Starting question

Where does Pictiq sit historically and functionally among visual languages, symbolic conlangs, AAC systems, public-information systems, and international sign standards?

### What happened

A broad literature review was assembled covering historical visual communication, modern wayfinding, symbolic constructed languages, AAC, international graphical-symbol standards, empirical comprehension studies, and adoption mechanisms.

### Key findings

1. Pictorial resemblance does not automatically produce universal comprehension.
2. Successful systems constrain domain, teach conventions, exploit context, or gain institutional and technical infrastructure.
3. Mature systems combine pictorial form with syntax, layout, color, shape, captions, training, interaction protocols, or software tooling.
4. Pictiq is best compared with a mixture of situational protocol, symbolic visual language, AAC-style selection interface, and public-information system rather than a full replacement writing system.
5. Vocabulary size alone is not a useful measure of expressive or practical capability.
6. Adoption mechanisms matter as much as icon design.
7. Cross-cultural comprehension must be treated as empirical rather than assumed from visual style.

### Evidence

[Preserved full report](research/from-pictographs-to-protocols.md), [perceptual-design concept](concepts/perceptual-design.md), [Embodied vs Standalone concept](concepts/embodied-vs-standalone.md), and [Pictiq protocol](../../spec/PROTOCOL.md).

### Decision / outcome

The report is a comparative source, not a rewrite of Pictiq doctrine. Its ISO 9186 finding is preserved as a methodological reference for graphical-symbol comprehensibility and identifiable elements. Pictiq currently prioritizes task-based, context-rich experiments; recognition or guessability checks may be one component of those experiments, rather than a generic classroom-style gate.

### Why it matters

The communication surface, distribution infrastructure, governance, training, and context shape practical success alongside icon design.

### Possible future book use

Use the report as a source for a future history-and-design book or several essays, preserving the research-to-journal-to-concept workflow before any chapter rewrite.

## 2026-09-09 — Portable visual communication precedent study

### Starting question

What existing products already solve communication by pointing at visual representations, and how are they structurally different from Pictiq?

### What happened

Point It, Kwikpoint, ICOON, This, Please, and PECS / A Picture's Worth were researched and fact-checked as precedents, analogues, and adjacent systems. Current retail observations were separated into a dated market radar so volatile price, availability, rating, and marketplace data do not become stable historical claims.

### Main result

The adjacent field is older and richer than a simple "picture dictionary" category. It spans photography, illustrated pointing systems, specialized vertical products, humanitarian adaptation, conventional publishing, and formal interaction protocols.

### Evidence

[Portable precedent study](research/portable-visual-communication-precedents.md), [verification matrix](research/portable-visual-communication-verification-matrix.md), [market radar](market/portable-visual-communication-radar.md), [source archive](research/sources/portable-communication/README.md), and [portable communication lessons](concepts/portable-communication-lessons.md).

### Decision / outcome

No Pictiq protocol, lexicon, profile, pack, icon, or release behavior changed. The research strengthens three working distinctions: visual vocabulary is not the same as interaction protocol; distribution evidence is not the same as communication-effectiveness evidence; and physical pointing surfaces deserve their own task-based tests.

### Why it matters

Future Pictiq books and essays can now use publication-safe facts differently from attractive but weak anecdotes. The archive records which claims are ready, which need attribution, and which should not be used without better evidence.

### Possible future book use

Use as a product-history chapter on portable communication: photographic specificity in Point It, vertical specialization in Kwikpoint, humanitarian adaptation in ICOON, publisher category entry in This, Please, and protocol-over-vocabulary in PECS.

## 2026-09-09 — AI and text-to-tile research input harvest

### Starting question

What genuinely new research value is present in the supplied Pictiq idea PDF and text-to-tile RAG prototype after the verified precedent material is already in the archive?

### What happened

The supplied PDF and Python prototype were preserved as research inputs, then reviewed separately from accepted protocol/specification material. The older precedent claims in the PDF were marked as superseded where the repository already has stronger verification. The runnable prototype was inspected directly and reproduced with the then-current 70-icon lexicon in a temporary Python environment.

### Main result

The durable new material is the machine-facing research layer: Pictiq as a constrained symbolic protocol, text-to-Pictiq baseline retrieval, explicit GAP behavior, human-machine shared symbols, planned machine-vision benchmarking, back-translation evaluation, scenario stress tests, and measured hypotheses around constrained generation, safety, token cost, and agent/tool adapters.

### Evidence

[Archived inputs](research/inputs/README.md), [ideas harvest](research/perplexity-ideas-harvest-2026-09.md), [text-to-Pictiq prototype record](experiments/text-to-pictiq-rag-prototype.md), [human-machine shared symbols](concepts/human-machine-shared-symbols.md), [machine-vision benchmark plan](experiments/machine-vision-benchmark-planning.md), [scenario bank](experiments/scenario-bank.md), and [AI/machine backlog](research/ai-machine-backlog.md).

### Decision / outcome

No AI roadmap, MCP tool, protocol grammar, canonical tile, pack, profile, or release change was accepted. The prototype's two failures are preserved as evidence: multi-clause input needs segmentation, and lexical TF-IDF can produce false positives even when output syntax is valid.

### Why it matters

This creates a clean path from speculative AI ideas to testable experiments without allowing a PDF or prototype to silently become Pictiq doctrine.

### Possible future book use

Use as a chapter or essay seed about why a visual protocol becomes more interesting when humans and machines can share stable IDs, while still needing empirical tests for translation, vision, safety, and compression claims.

## 2026-09-08 — Full 120-word crosswalk

### Starting question

Does a larger Toki Pona comparison show a missing Pictiq vocabulary?

### What happened

The full study classified 120 words as 19 PARTIAL, 2 COMPOSED, 11 CONTEXTUAL, 88 NONE, and 0 DIRECT.

### Evidence

[Full crosswalk study](https://github.com/markoblogo/toki-pona-translator).

### Decision / outcome

NONE was retained as a meaningful research result rather than a failure. It can indicate embodiment, standalone need, modifier or parameter mechanisms, or Pictiq scope boundaries.

### Why it matters

Semantic non-equivalence is useful evidence when the goal is to understand architectures rather than maximize overlap.

### Open questions

Human usability of the crosswalk has not yet been established by a controlled study.

### Possible future book use

A data-backed chapter on the difference between lexical coverage and communicative coverage.

## 2026-09-08 — Embodied versus Standalone communication

### Starting question

Did every crosswalk gap require another Pictiq tile?

### What happened

The analysis showed that eyes, clothing, size, person reference, color, direction, and emotion can often be supplied by body, gaze, gesture, visible objects, environment, or shared situation in live communication. The architecture therefore distinguished Embodied Communication from Standalone Communication.

### Evidence

[Protocol §1.1](../../spec/PROTOCOL.md#11-embodied-and-standalone-communication), [architecture commit](https://github.com/markoblogo/pictiq/commit/f31c51c), and [Toki Pona relationship](../../spec/PROTOCOL.md#11-embodied-and-standalone-communication).

### Decision / outcome

The governing principle became: **Design only what the communication surface cannot already provide.** Embodiment is part of the protocol, not a workaround for it.

### Why it matters

The communication surface, not the translation table alone, determines whether a concept needs a durable symbol.

### Open questions

Reliability thresholds for embodied cues in varied cultures and environments remain open.

### Possible future book use

This is a central architecture chapter: the body is one channel in a multimodal protocol.

## 2026-09-08 — Primitive taxonomy

### Starting question

How can Pictiq expand without turning every semantic distinction into a new word?

### What happened

The protocol separated lexical tiles, modifiers/operators, parametric tiles, entity symbols, and embodied references. GOOD/BAD were separated from YES/NO; scale was treated as modifier research; color as a parameter; and proper names as scoped entities.

### Evidence

[Protocol §1.2](../../spec/PROTOCOL.md#12-communication-primitive-classes) and [standalone backlog](../../spec/STANDALONE_BACKLOG.md).

### Decision / outcome

Semantic gaps must pass a decision tree before a lexical tile is proposed.

### Why it matters

An architecture can grow by adding mechanisms, not only vocabulary.

### Open questions

Parametric color and entity namespaces remain prototypes, not implemented canonical features.

### Possible future book use

A systems-design explanation of why “more words” is often the wrong answer.

## 2026-09-09 — Parametric color proposal

### Starting question

How can standalone Pictiq identify an arbitrary color without a finite monochrome color vocabulary?

### What happened

The proposal keeps a canonical frame and carries the actual value in a color sample, conceptually `color(#747b72)`. In embodied use, pointing to the actual colored object may be enough.

### Evidence

[Protocol color mechanism](../../spec/PROTOCOL.md#12-communication-primitive-classes) and [backlog entry](../../spec/STANDALONE_BACKLOG.md#parametric-color-prototype).

### Decision / outcome

Finite lexical colors were rejected as the default. Color remains **PROPOSED PARAMETRIC MECHANISM — NOT IMPLEMENTED**.

### Why it matters

Dynamic semantic values can belong in a parameter rather than an ever-growing lexicon.

### Open questions

Machine representation, contrast, print behavior, accessibility, and syntax need a prototype.

### Possible future book use

A concise example of designing an exception without weakening the general tile system.

## 2026-09-09 — Entity symbols

### Starting question

How can Pictiq identify Odysseus, Alice, or a specific person without alphabetic spelling?

### What happened

The project described scoped entity symbols such as `entity:odysseus@literary`, distinguishing a named entity from `person_generic`. Governance separates personal authority from project-local canonicity and rejects universal first-claim ownership. The first local pilot now implements six person examples: Anton Biletskyi-Volokh, Odysseus, William Shakespeare, Albert Einstein, Leonardo da Vinci, and Buddha / Siddhartha Gautama.

### Evidence

[Protocol entity symbols](../../spec/PROTOCOL.md#12-communication-primitive-classes), [entity-symbol concept](concepts/entity-symbols.md), [pilot note](experiments/entity-symbol-pilot.md), [entity registry](../../entities/entity-index.json), and [backlog prototype](../../spec/STANDALONE_BACKLOG.md#entity-symbol-namespace-and-prototype).

### Decision / outcome

Entity symbols are **IMPLEMENTED / ACCEPTED** as official Pictiq project entity-symbol examples. They are not ordinary Core lexical tiles and do not change the Core/Standalone lexicon count.

### Why it matters

Identity is a scoped registry problem, not a request for a larger universal noun list.

### Open questions

Namespace syntax, discovery, revision, and recognition testing remain unresolved.

### Possible future book use

A bridge from visual language into narrative world-building and local dictionaries.

## 2026-09-09 — Standalone Batch A

### Starting question

Could the new taxonomy produce a small, testable set of standalone primitives?

### What happened

Six accepted primitives were implemented: `qual_good`, `qual_bad`, `person_generic`, `state_hot`, `state_cold`, and `power_energy`. The canonical inventory grew from 52 to 58. GOOD/BAD became modifiers; person, hot/cold, and energy became standalone lexical tiles.

### Evidence

[Backlog](../../spec/STANDALONE_BACKLOG.md), [core overview](../overview/pictiq-core-grid.png), [release candidate note](../../releases/v1.0.2.md), and commits [`fd25855`](https://github.com/markoblogo/pictiq/commit/fd25855), [`79f816c`](https://github.com/markoblogo/pictiq/commit/79f816c), [`f28d277`](https://github.com/markoblogo/pictiq/commit/f28d277), [`ee80d22`](https://github.com/markoblogo/pictiq/commit/ee80d22).

### Decision / outcome

All six passed structural validation and human visual acceptance. Person and fire were revised until the supplied reference morphology remained recognizable.

### Why it matters

Batch A is the first practical test of the Embodied/Standalone architecture under the existing acceptance pipeline.

### Open questions

The usability pilot and later Batch B/C candidates are not complete.

### Possible future book use

A bounded case study from architectural decision to accepted production assets.

## 2026-09-09 — GitHub Pages production failure and repair

### Starting question

Would the repository’s documented static site actually work as deployed?

### What happened

An external audit found broken dictionary and handbook paths. Verification showed that Pages deployed `main:/docs` while runtime paths used `../lexicon` and `../books`. The fix made `docs/lexicon` self-contained, removed unsupported locales, added artifact validation to CI, and moved large handbook downloads to stable raw repository URLs.

### Evidence

[Pages contract](../README.md), [artifact validator](../../tools/validate_pages_artifact.py), [repair commit](https://github.com/markoblogo/pictiq/commit/9b0bfc8), and [live dictionary](https://markoblogo.github.io/pictiq/).

### Decision / outcome

Production smoke tests passed for the index, search, icons, locales, promo, PDF, and EPUB.

### Why it matters

Repository/document architecture and deployed-artifact architecture must match.

### Open questions

The deployment remains GitHub’s legacy branch `/docs` model; a workflow-built artifact may be considered later.

### Possible future book use

A short engineering sidebar on how a correct local path can still be wrong in production.

## 2026-09-09 — Standalone Batch C local implementation

### Starting question

Could five approved reference shapes become canonical Pictiq candidates without redesigning the protocol or changing existing icons?

### What happened

Five Batch C primitives were implemented and human-accepted: `body_mouth`, `rel_here`, `rel_up`, `rel_down`, and `nature_moon`. The ordinary canonical lexicon now has 75 icons. Standalone Core includes all five; Embodied Core includes the three relation operators and omits mouth and moon/night by default because live body/context can often supply them.

### Evidence

[Batch C QA note](experiments/standalone-batch-c-reference-qa.md), [Protocol §1.1](../../spec/PROTOCOL.md#11-embodied-and-standalone-communication), [Grammar §7.1](../../spec/GRAMMAR.md#71-relational-and-directional-operators-provisional), and local QA sheets in `build/qa/`.

### Decision / outcome

Batch C is implemented, structurally validated, and human-accepted as canonical. Push/public verification remain separate gates; no new tag or GitHub release is implied.

### Why it matters

The batch turns the Embodied/Standalone distinction into practical profile decisions and clarifies action-relevant ambiguity, relation operators, and daylight/nighttime composition.

### Open questions

Post-publication task validation, Road Signs × Pictiq stress testing, and any future release/tag decision remain separate gates.

### Possible future book use

A concise case study showing how a visual protocol decides between body-supplied meaning, standalone explicitness, operators, and lexical tiles.

## 2026-09-10 — Vocabulary architecture classification

### Starting question

How should Pictiq classify accepted icons after the ordinary canonical registry reached 75 IDs and entity symbols became a separate accepted pilot?

### What happened

The project formalized a source-of-truth vocabulary classification file and a human-readable architecture document. The migration separated Canonical Registry, Core Vocabulary, Standalone Core, Context Packs, Specialized vocabulary, Mechanisms, and Entity Registry without changing canonical IDs, icon morphology, or accepted lexical semantics.

### Evidence

[Vocabulary Classification](../../spec/VOCABULARY_CLASSIFICATION.md), [`lexicon/vocabulary-classification.json`](../../lexicon/vocabulary-classification.json), and [Grammar](../../spec/GRAMMAR.md).

### Decision / outcome

“Canonical does not mean Core” became explicit architecture. Contextual and specialized complexity now belongs in the context that requires it, while profiles remain communication-surface selections rather than separate icon libraries.

### Why it matters

The distinction lets Pictiq grow through evidence-led context packs and entity namespaces while preserving a small Core vocabulary and clear protocol mechanics.

### Possible future book use

Use as a design-governance case study about how a visual protocol can scale without treating every accepted symbol as universal vocabulary.

## 2026-09-10 — Road Wayfinding accepted additions

### Starting question

Which Stress Test 02 findings should become durable architecture after visual acceptance?

### What happened

The project accepted `surface_wavy` and `state_dead` as contextual ordinary canonical primitives and introduced partial shared numeric notation demonstrated by `50`. The ordinary canonical lexicon now has 77 icons. Numeric notation stays outside ordinary lexical count and coexists with the pragmatic `qty_*` quantity system.

### Evidence

[Road Wayfinding Stress Test](experiments/road-wayfinding-stress-test.md), [Stress Test 02 research artifact](../research/road-wayfinding-stress-test-v1.md), [Numeric Notation](../../spec/NUMERIC_NOTATION.md), and accepted-concepts QA sheet in `build/qa/stress-test-02-accepted-concepts.png`.

### Decision / outcome

`surface_wavy` remains broad enough for wavy, uneven, unstable, slippery, waves, and surface irregularity. `state_dead` remains contextual because cross-domain usefulness alone does not make it Core. Numeric `50` is rendered through notation assets, not a lexical `num_50`.

### Why it matters

The decision preserves action-relevant distinctions while keeping Core small: context packs select and reuse primitives or notation, they do not own them exclusively.

## 2026-09-10 — Road Wayfinding final visual acceptance

### Starting question

Which visual output should represent Stress Test 02 after human review rejected the first generated comparison sheets?

### What happened

The supplied image `road-wayfinding-pictiq-representation.png` became the human-accepted final visual representation. It replaces the earlier Codex-generated comparison sheets as the current visual result while preserving them as rejected intermediate artifacts.

### Corrections preserved

Pedestrian route/prohibition/crossing now use PERSON plus FEET/WALKING. Exact `50` uses numeric notation, not `qty_5 + qty_5`. Slippery, uneven, and speed-bump cases use the broad `surface_wavy + punct_exclaim` compression where the practical action is surface problem → slow down / proceed carefully. `state_dead` is recorded as death/deadly/not-alive and is explicitly not used for dead end; dead end remains forward/ahead plus NO.

### Method lesson

Future stress tests should validate source meaning, validate Pictiq semantic mapping, obtain human acceptance, and only then create the final visual comparison.
