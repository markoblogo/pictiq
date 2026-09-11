# Compositional Visual Systems Comparison

> Status: comparative research note / verification required before book-public claims
> Source input: [`inputs/perplexity-2026-09/compositional-visual-systems-comparison.md`](inputs/perplexity-2026-09/compositional-visual-systems-comparison.md)
> Rule: do not claim Pictiq is the first visual language with grammar.

## Correction to preserve

The defensible claim is not “Pictiq is the first visual language with grammar” and not “most pictogram systems have no grammar.” Historical and contemporary counterexamples include Blissymbolics, SignWriting, military symbology, visual programming / DSL notations, and some formal wayfinding or safety systems.

A safer positioning hypothesis is that Pictiq may be interesting because it combines:

- deliberately small vocabulary;
- explicit composition;
- contextual extensions;
- machine-readable Message representation;
- deterministic rendering;
- automated validation / CI;
- Embodied vs Standalone distinction;
- open experimental development.

This remains a comparative hypothesis, not a uniqueness claim.

## Comparison table

| System | Compositional dimension | Machine / governance dimension | Useful Pictiq comparison | Caution |
| --- | --- | --- | --- | --- |
| Blissymbolics | Semantic primitives, classifier/specifier compounds, grammatical indicators, word-order rules, generative vocabulary. | Authorized vocabulary and long AAC history; reported digital encoding work. | Strongest comparator for “small semantic pieces can generate larger meanings.” | Do not portray Bliss as a primitive pictogram dictionary. Verify grammar/governance claims from primary Bliss sources. |
| ISOTYPE | Repetition, scaling, pictorial statistics, diagrammatic composition. | Design-system discipline more than message grammar. | Useful for explaining quantity/visual economy and public education. | Do not overstate as full linguistic grammar. |
| AAC symbol sets / PODD / PECS | Communication books, aided language, pragmatic sequencing, partner-assisted context. | Clinical/educational practice and symbol-set governance vary by system. | Important for transparency, learnability, and context-of-use testing. | AAC claims require specialist sources and user research. |
| SignWriting | Spatial/visual notation for signed languages; handshape, movement, location, facial expression. | Writing-system / encoding comparator. | Shows visual systems can encode grammar-rich languages. | It writes existing signed languages; Pictiq is not a sign-language writing system. |
| Unicode emoji | ZWJ sequences, skin-tone modifiers, variation selectors, flags, CLDR names. | Strong standardization and locale layer. | Comparator for modifiers, compatibility, and localization. | Emoji grammar is limited and socially emergent; avoid treating it as equivalent to Pictiq grammar. |
| Road / wayfinding systems | Shape, color, arrows, prohibitions, supplementary plates, placement context. | Strong public standards and jurisdictional localization. | Useful for context economy and action-oriented interpretation. | Sign comprehension varies cross-culturally; do not assume universality. |
| APP-6 / MIL-STD-2525 | Component-based symbol construction from affiliation/status/entity/activity/modifiers. | Machine-readable/bidirectional encoding; strong operational governance. | Engineering precedent: composition solves scale where enumeration fails. | Do not import military semantics or complexity. |
| UML / BPMN / Scratch | Formal visual grammar, typed nodes, connectors, constraints. | Tooling, validation, execution, or semi-formal semantics. | Comparator for machine-readable visual DSLs and Composer tooling. | These are not pictographic human travel languages. |
| Icono | Reported constructed visual language / symbol-composition comparator. | Needs verification. | Possible book comparator for constructed visual-language attempts. | Treat current source as unverified. |
| IKON / KomunIKON | Reported icon-language / AAC-adjacent comparator. | Needs verification. | Possible comparator for pictographic communication and user testing. | Verify existence, scope, and claims before book use. |
| Toki Pona / sitelen pona | Minimal lexicon and visual writing, not a direct ancestor of Pictiq. | Community orthography and comparative research value. | Useful for minimal lexical language vs embodied visual protocol comparison. | Keep non-normative and historically accurate. |
| Pictiq | Explicit small vocabulary, composition, Context Packs, Message JSON, Renderer, validation, Entity Symbols, numeric notation. | Open repository, versioned releases, validation scripts, compatibility metadata. | Modern experiment-driven visual protocol. | Current claims remain project evidence, not universal proof. |

## Blissymbolics focus

Blissymbolics matters because it is a serious generative visual-semantic system, not a flat pictogram catalog. The supplied research reports:

- semantic primitives and compound construction;
- classifier/specifier structure;
- grammatical indicators;
- word-order rules;
- strategies for generating or repairing vocabulary;
- authorized vocabulary governance;
- AAC history;
- digital/machine encoding efforts.

Meaningful differences from Pictiq should be framed neutrally:

- Blissymbolics has a long AAC and formal-vocabulary lineage; Pictiq is a young open protocol project.
- Bliss uses its own established symbol-writing conventions; Pictiq currently emphasizes framed canonical tiles, Message JSON, deterministic SVG rendering, and validation.
- Pictiq's Context Packs and Embodied/Standalone distinction are current architectural interests, not proof of superiority.

## Military symbology focus

APP-6 / MIL-STD-2525 is useful as an engineering comparator because it shows a mature shift from exhaustive enumeration toward component-based symbol construction with machine-readable encoding. The lesson for Pictiq is narrow: composition and formal encodings can support extensibility better than a giant flat icon list.

This does not imply that Pictiq should adopt military semantics, military visual density, operational hierarchy, or standards-body complexity.

## Book-safe positioning draft

Pictiq belongs in a lineage of visual and symbolic systems that includes strong compositional precedents. Its claim should be modest: a small, open, experiment-driven visual protocol can combine human-readable tiles with machine-readable messages and deterministic validation. That combination may make Pictiq useful for modern tooling and research even though it is not historically first.
