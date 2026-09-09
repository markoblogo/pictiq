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

The project described scoped entity symbols such as `entity:odysseus@odyssey-pack`, distinguishing a named entity from `person_generic`. Governance separates personal authority from project-local canonicity and rejects universal first-claim ownership.

### Evidence

[Protocol entity symbols](../../spec/PROTOCOL.md#12-communication-primitive-classes) and [backlog prototype](../../spec/STANDALONE_BACKLOG.md#entity-symbol-namespace-and-prototype).

### Decision / outcome

Entity symbols remain an **ARCHITECTURE PROTOTYPE — NOT IMPLEMENTED**.

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
