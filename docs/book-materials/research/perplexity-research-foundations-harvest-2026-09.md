# Pictiq Research Foundations Harvest 2026-09

> Status: critical harvest / book-material seed
> Source type: five user-supplied Perplexity research documents
> Rule: research inputs only; not authoritative specifications and not accepted Pictiq doctrine.

## Archived inputs

| Topic | Original supplied filename | Archived file | SHA-256 | Byte-equal |
| --- | --- | --- | --- | --- |
| Pictogram comprehension testing | `How Pictogram and Symbol Comprehension Is Formally Tested  ISO 9186, AAC Research, and Practical Methods for Small Projects.md` | [`inputs/perplexity-2026-09/pictogram-comprehension-testing-methods.md`](inputs/perplexity-2026-09/pictogram-comprehension-testing-methods.md) | `cf6bb932a8bdf5bb6a2e1a0afbef4ebcb334df9afc72ace7b0a6a7c42bd94b5d` | yes |
| Compositional visual systems | `Compositional Grammar vs. Flat Symbol Lookup in Visual and Pictographic Communication Systems.md` | [`inputs/perplexity-2026-09/compositional-visual-systems-comparison.md`](inputs/perplexity-2026-09/compositional-visual-systems-comparison.md) | `22f1859ccd42d4f2b3b4e3d5099f5a7defe7b363f993df4ea556f0a2294aabbc` | yes |
| Context economy | `Context Economy in Communication  Theory, Evidence, and Implications for Pictiq.md` | [`inputs/perplexity-2026-09/context-economy-in-communication.md`](inputs/perplexity-2026-09/context-economy-in-communication.md) | `c826dbd515b91f729240c9aa5526451e7d3370142f3db6301daba50b3f590759` | yes |
| Intentional polysemy | `Intentional polysemy is valuable when a single sign gives users a stable conceptual centre and its different readings can be recovered from grammar, composition, situation, or interface context.md` | [`inputs/perplexity-2026-09/intentional-polysemy-in-visual-language.md`](inputs/perplexity-2026-09/intentional-polysemy-in-visual-language.md) | `5c0b9a9e7031690bb376876aa9021b04760750c1ec17c43860990bf77bda820e` | yes |
| Context Pack extensibility | `A durable extensibility model separates a small, interoperable core from optional, versioned domain packs that add vocabulary, constraints, examples, and localized conventions without redefining the core.md` | [`inputs/perplexity-2026-09/context-pack-extensibility-architecture.md`](inputs/perplexity-2026-09/context-pack-extensibility-architecture.md) | `fd2953e3f9af8306fe83ede0bdd75174141be8c5be9208a0233434302dc34c32` | yes |

## Harvest matrix

| Status | Source | Claim / idea | Current Pictiq relevance | Evidence quality | Action |
| --- | --- | --- | --- | --- | --- |
| ALREADY_SUPPORTED | Context Pack architecture | Stable Core should be separated from extensions, profiles, locales, examples, and compatibility. | Matches current Core/context/entity/notation split after v1.1.0 and v1.1.1. | Perplexity synthesis plus strong analogy set; needs primary-source verification before book claims. | Preserve as architecture hypothesis; do not implement new governance now. |
| STRONG_FINDING | Context economy | Context can reduce explicit symbolic load, but only when users share enough situational or learned background. | Supports Embodied vs Standalone distinction and context-pack caution. | Theory-backed synthesis; individual citations need verification. | Preserve as concept note and future experiment lens. |
| STRONG_FINDING | Intentional polysemy | Polysemy compresses vocabulary; unmarked ambiguity creates decoding cost. | Explains accepted broad roots such as `surface_wavy`, `nature_cloud`, `place_home`, and `qual_sacred`. | Good conceptual synthesis; exact linguistic sources require verification. | Preserve decision framework; do not reopen vocabulary audit. |
| STRONG_FINDING | Compositional visual systems | Pictiq should not claim to be the first visual language with grammar or imply that most pictogram systems are flat dictionaries. | Corrects positioning around Blissymbolics, SignWriting, military symbology, and other compositional systems. | Useful synthesis with cited systems; external details remain verification backlog. | Update comparison and claims notes. |
| EXPERIMENT_METHOD | Pictogram comprehension testing | Recognition, comprehension, context-of-use, transparency, translucency, name agreement, and learnability are distinct constructs. | Prevents vague “icon comprehension” claims and improves future human-test design. | Strong methodological framing; exact ISO/ANSI claims need primary verification. | Create human-testing methodology and human-experiments backlog. |
| VERIFICATION_REQUIRED | Pictogram comprehension testing | ISO 9186 parts, ANSI Z535.3 thresholds, sample sizes, and critical-confusion rules. | Important for future empirical claims and book chapters. | Standards access may be incomplete; Perplexity citation presence is not verification. | Keep in verification backlog; avoid “ISO requires 85%”. |
| BOOK_MATERIAL | Compositional visual systems | Blissymbolics deserves serious comparison as a generative semantic system with governance and AAC history. | Helps position Pictiq among real visual-language precedents without superiority framing. | Strong source lead; needs primary/academic confirmation. | Use in book outline; avoid primitive/flat portrayal. |
| BOOK_MATERIAL | Military symbology | APP-6 / MIL-STD-2525 is a precedent for component-based symbol construction and machine-readable encoding. | Engineering comparator for extensibility through composition. | Reported from Perplexity; primary standards and SIDC details require verification. | Preserve as comparator, not design model. |
| ARCHITECTURE_HYPOTHESIS | Context Pack architecture | Near-term context packs may eventually need machine-readable manifests. | Plausible after Composer/public surfaces, but not needed now. | Analogy-driven. | Record future fields only; do not implement. |
| OUTDATED_PICTIQ_ASSUMPTION | All sources | Some source examples may use older Pictiq vocabulary, pre-v1.1.0 assumptions, or proposed structures. | Could conflict with current registries and Message Format. | Source artifact risk. | Do not import examples as accepted compositions. |
| DO_NOT_IMPORT | Intentional polysemy | Physical/digital/social/institutional markers, role markers, viewpoint/state systems. | Potentially useful later, but no current stress test justifies them. | Speculative design ideas. | Defer; require independent pressure. |
| DO_NOT_IMPORT | Context Pack architecture | Certification tiers, authority levels, official/community/private registries, promotion pipelines. | Overbuilt for current project size. | Standards-body analogy, not current need. | Preserve as future options only. |
| FUTURE_IMPLEMENTATION_CANDIDATE | Context Pack architecture | Minimal machine-readable Context Pack manifest. | Could support validation and Composer after pack complexity grows. | Plausible architecture pattern. | Consider later: pack id, version, status, compatible Pictiq version, concepts, dependencies, locales, license. |
| EXPERIMENT_METHOD | Human/AI signaling matrix | HUMAN→HUMAN, AI→AI, HUMAN→AI, AI→HUMAN can share semantic corpus, Message JSON, Renderer, and slot evaluation. | Connects human experiments with machine experiments after Composer. | Methodological synthesis. | Add backlog; do not implement now. |
| TOO_STRONG | All sources | Pictiq is inherently cross-cultural or scientifically validated because it uses pictorial icons. | Contradicts cross-cultural pictogram findings and project evidence standard. | Too broad. | Explicitly reject in claims note. |

## Main research foundations preserved

1. Pictiq's stronger positioning is not “first grammar.” It is a combination of small vocabulary, explicit composition, Context Packs, machine-readable Message representation, deterministic rendering, automated validation, Embodied/Standalone separation, and experiment-driven development.
2. Context is useful only when it is recoverable. Ambient context and declared context frames solve different problems.
3. A Context Pack does not automatically create common ground.
4. Published semantic IDs should not be silently repurposed. If meaning changes, compatibility/deprecation metadata must preserve historical messages.
5. Human testing must identify the tested construct: recognition, comprehension, context-of-use, production, or communication success.

## No changes made by this harvest

No vocabulary, grammar, icon, profile, pack, entity, numeric notation, renderer, Message Schema, Composer, Translator, RAG system, release, or tag is created by this harvest.
