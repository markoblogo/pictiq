# Pictiq book materials archive

This directory is a source archive for future Pictiq books, visual-language research writing, Medium/Substack essays, project retrospectives, case studies, and narrative experiments.

It is not a polished manuscript and not a canonical specification. Its purpose is to preserve development history before hindsight removes useful uncertainty, mistakes, and intermediate reasoning.

## Editorial rules

### Rule 1 — Preserve chronology

Do not rewrite early hypotheses to match later conclusions. When an idea changes, preserve the original idea and why it changed.

### Rule 2 — Record failures

Failed visual designs, rejected mappings, broken deployments, and negative experimental results are valid material.

### Rule 3 — Separate evidence from interpretation

Link to commits, specifications, reports, generated artifacts, releases, and research files where possible. Label interpretation clearly.

### Rule 4 — Do not turn every update into a book chapter

Capture material first. Future books may reorganize it later.

### Rule 5 — Archive substantial experiments

Meaningful usability, interoperability, product, visual-QA, protocol, machine-interface, narrative, merch, or deployment experiments get a short entry. Routine typo fixes, dependency updates, trivial polish, and CI maintenance without a broader lesson usually do not.

## Future directions

The archive supports several possible books: a visual-language/popular-science book; a practical travel-communication book using Pictiq; and a narrative or comic experiment in which characters communicate through Pictiq. No title or publication plan is decided.

Start with the [research journal](research-journal.md), then browse [concepts](concepts/), [experiments](experiments/), and [products](products/).

Recent architecture material includes the [Embodied and Standalone Profile decision](concepts/embodied-vs-standalone.md) and [Standalone Batch B planning](../../spec/STANDALONE_BACKLOG.md).

The [comparative visual-language review](research/from-pictographs-to-protocols.md) is a major preserved source for possible future popular-science or design books on visual communication history, constructed languages, signage, AAC, pictogram standards, empirical comprehension, and Pictiq as a contemporary case study. It supports multiple future books; no fixed outline is decided.

The [portable visual communication precedent study](research/portable-visual-communication-precedents.md) is a product- and case-study-oriented companion to the broader literature review. It covers Point It, Kwikpoint, ICOON, This, Please, and PECS / A Picture's Worth as precedents, analogues, and adjacent systems; the separate [market radar](market/portable-visual-communication-radar.md) preserves dated retail observations that should not be treated as stable history.

The [Perplexity ideas harvest](research/perplexity-ideas-harvest-2026-09.md) and [text-to-Pictiq RAG prototype record](experiments/text-to-pictiq-rag-prototype.md) preserve a later AI/machine-interface research input. Use these as experiment material only: they do not change Pictiq protocol behavior, canonical icons, packs, profiles, or release state.

The [vocabulary architecture classification](concepts/vocabulary-architecture.md) preserves the post-v1.0.2 distinction between canonical registry, Core, Standalone Core, context packs, specialized vocabulary, mechanisms, and entity symbols. It is book material, not a replacement for the normative spec. The [vocabulary cleanup note](concepts/vocabulary-cleanup-after-stress-tests.md) preserves the audit story: historical travel bias, semantic migration, composable deprecation, legacy contextual vocabulary, and the single clear new MEAT primitive.

The [inclusive-design and use-case harvest](research/perplexity-inclusive-design-and-use-cases-harvest-2026-09.md), [identity-neutral substrate note](concepts/identity-neutral-substrate.md), [manifesto notes](concepts/inclusive-design-manifesto-notes.md), [verification backlog](research/inclusive-design-verification-backlog.md), and [application-domain radar](research/application-domains-radar.md) preserve a critical reading of three Perplexity ideation artifacts. Treat them as research/book material only: they do not change Pictiq protocol behavior, vocabulary classification, icons, packs, profiles, or entity registry.


The [book/kids/experiment harvest](research/perplexity-book-kids-and-experiment-harvest-2026-09.md), [book architecture hypotheses](planning/pictiq-book-architecture-hypotheses.md), [kids/narrative research track](research/kids-narrative-research-track.md), [experimental methods backlog](research/experimental-methods-backlog.md), [tooling architecture note](concepts/pictiq-tooling-architecture.md), and [research workflow note](concepts/research-workflow.md) preserve a planning pass over future books, children's narrative experiments, tooling, VLM/Machine Mind work, and content/dev-diary pipelines. Treat them as research workflow and book material only: they do not change protocol behavior, vocabulary classification, icons, packs, profiles, entity registry, or release state.

The [Message Representation Layers](concepts/message-representation-layers.md) note records the post-v1.1.0 split between language, canonical JSON message representation, human shorthand, rendering, and translation. Treat it as architecture/book material only; it does not implement the renderer/generator or Composer.
The [Renderer v0.1 Implementation Note](concepts/renderer-v0.1-implementation.md) records the first executable rendering layer built on that split. It documents deterministic SVG rendering, fail-loud diagnostics, registry-aware normalization, and the boundary between rendering and translation.
The [Pictiq AI Experiments harvest](research/pictiq-ai-experiments-harvest-2026-09.md), [Machine Experiments Backlog](research/machine-experiments-backlog.md), [Signaling Game plan](research/pictiq-signaling-game-plan.md), [Semantic Boundary corpus plan](research/semantic-boundary-corpus-plan.md), and [AI experiment verification backlog](research/ai-experiment-verification-backlog.md) organize post-Renderer machine research without changing Pictiq language, vocabulary, renderer, or release state.

The [Composer v0.1 Architecture Note](concepts/composer-v0.1-architecture.md), [Composer spec](../../spec/PICTIQ_COMPOSER.md), and [Stress Test 04B plan](research/composer-human-authoring-stress-test-04b.md) define the next human-authoring milestone after Stress Test 04A. Composer v0.1 creator/software acceptance has passed after implementation and three acceptance-fix passes, but Stress Test 04B external human-authoring usability remains not run.


The [Zero-Training Entry Principle](concepts/zero-training-entry.md), [Research and Evidence Policy](research/pictiq-research-and-evidence-policy.md), [Deployment Roadmap](planning/deployment-roadmap.md), [Publication Milestones](planning/publication-milestones.md), and [Stress Test 05 plan](research/stress-test-05-zero-training-visual-comprehension.md) mark the current project shift from primarily building the language toward pressure, deployment, publication, and real-world feedback. Treat these as strategy/research planning only: they do not change protocol behavior, vocabulary, grammar, icons, packs, profiles, renderer, Composer, or release state.

The [Research Foundations harvest](research/perplexity-research-foundations-harvest-2026-09.md), [Compositional Visual Systems comparison](research/compositional-visual-systems-comparison.md), [Context Economy note](concepts/context-economy-and-common-ground.md), [Human Testing Methodology](research/human-testing-methodology.md), [Polysemy Decision Framework](concepts/polysemy-decision-framework.md), [Context Pack Architecture hypotheses](concepts/context-pack-architecture-hypotheses.md), [Human Experiments Backlog](research/human-experiments-backlog.md), and [Book-safe Claims backlog](research/book-safe-claims-and-verification-backlog.md) preserve five research-foundation inputs. Treat them as book/research material only: they correct positioning and methodology, but do not change protocol behavior, vocabulary, grammar, icons, packs, profiles, renderer, Composer, or release state.

The [Pictiq Poetry harvest](research/pictiq-poetry-harvest-2026-09.md), [Visual Prosody concept note](concepts/visual-prosody.md), [poetry stress-test plan](research/pictiq-poetry-stress-test-plan.md), and [poetry precedents verification backlog](research/poetry-precedents-verification-backlog.md) preserve a post-Composer research track about poetic form, semantic compression, repetition, and visual constraints. Treat this as research/book material only: it does not change grammar, vocabulary, icons, profiles, packs, renderer, Composer, or release state.

## Current research threads

- Road Wayfinding accepted additions: `surface_wavy`, `state_dead`, and partial numeric notation are recorded in [`experiments/road-wayfinding-stress-test.md`](experiments/road-wayfinding-stress-test.md) and [`../research/road-wayfinding-stress-test-v1.md`](../research/road-wayfinding-stress-test-v1.md).
- Odyssey × Toki Pona × sitelen pona Stage 1 records narrative architecture findings, `INTENTIONAL_OMISSION`, structural gender neutrality, and Stage 2 entity/primitive candidates in [`experiments/odyssey-toki-pona-pictiq-stress-test.md`](experiments/odyssey-toki-pona-pictiq-stress-test.md) and [`../research/odyssey-toki-pona-pictiq-stress-test-03-stage-1.md`](../research/odyssey-toki-pona-pictiq-stress-test-03-stage-1.md).
- Odyssey Stage 2A accepted ordinary primitives (`action_conflict`, `move_watercraft`, `qual_sacred`, `nature_animal`, `nature_cloud`) are recorded in [`experiments/odyssey-toki-pona-pictiq-stress-test.md`](experiments/odyssey-toki-pona-pictiq-stress-test.md) and [`../research/odyssey-toki-pona-pictiq-stress-test-03-stage-2a.md`](../research/odyssey-toki-pona-pictiq-stress-test-03-stage-2a.md).
- Odyssey Stress Test 03 is closed as a final six-fragment narrative-compression case study in [`experiments/odyssey-toki-pona-pictiq-stress-test.md`](experiments/odyssey-toki-pona-pictiq-stress-test.md), [`../research/odyssey-toki-pona-pictiq-stress-test-03.md`](../research/odyssey-toki-pona-pictiq-stress-test-03.md), and [`../research/odyssey-toki-pona-pictiq-stress-test-03.json`](../research/odyssey-toki-pona-pictiq-stress-test-03.json).
- Book, kids, tooling, and experimental-methods planning is captured in [`research/perplexity-book-kids-and-experiment-harvest-2026-09.md`](research/perplexity-book-kids-and-experiment-harvest-2026-09.md), with children's books treated as a future experimental track rather than a prerequisite for Book 1.
- Pictiq Poetry / Visual Prosody is recorded as a post-Composer research track in [`research/pictiq-poetry-harvest-2026-09.md`](research/pictiq-poetry-harvest-2026-09.md) and [`concepts/visual-prosody.md`](concepts/visual-prosody.md). It is a negative-test candidate for expressivity under ambiguity and formal constraint, not a grammar or vocabulary change.
- Constrained Translation Pilot 04A is CLOSED / ACCEPTED and recorded in [`experiments/constrained-translation-pilot-04a.md`](experiments/constrained-translation-pilot-04a.md) and [`../research/constrained-translation-pilot-04a/README.md`](../research/constrained-translation-pilot-04a/README.md). It tests LLM-to-Message JSON generation as a research condition only; it does not implement a Translator or change schema, renderer, vocabulary, grammar, packs, profiles, icons, or Entity Symbols.
