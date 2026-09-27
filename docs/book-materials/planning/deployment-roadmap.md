# Pictiq Deployment Roadmap

> Status: deployment/stress-test planning, not a product commitment.
> Source event: Research & Deployment Policy pass, 2026-09-11.

## Deployment principle

Pictiq deployments should preferably solve another product's problem rather than exist only to demonstrate Pictiq.

Pictiq is often a secondary infrastructure or communication layer. A children's book should primarily work as a children's picture book. A LitRPG novel should primarily work as LitRPG. A travel aid should help communication. A showbook should help a person show requests. An AI Action Receipt should help a person inspect an AI action.

## Product families

### Picture books

Primary product: picture book. Pictiq is secondary.

Working hypothesis:

IMAGE -> STRUCTURED VISUAL SYMBOLS -> LATER CONVENTIONAL WRITING.

Large illustrations carry the story. Pictiq may represent thoughts, simple speech, actions, wants, questions, small dialogue, and recurring character communication. The child does not need to know that the system is called Pictiq.

This is a pre-reading / symbolic-reading design hypothesis. Do not claim proven literacy benefits.

### Pictiq as secondary narrative layer

Possible uses in LitRPG, comics, and illustrated fiction:

- visual dialogue;
- creature thoughts;
- system messages;
- environmental signage;
- alien or machine communication;
- spells/statuses;
- recurring visual motifs.

Readers should ideally understand enough from narrative context without a Pictiq lesson. This is both deployment and a zero-training pressure test.

### Embodied cross-language communication

Deployment family: show / point / combine.

Candidate formats:

- child travel/playground card;
- pocket communication card;
- fold-out sheet;
- small booklet;
- T-shirt;
- backpack card or patch;
- traveler communication aid.

The user may point to symbols or combine symbols. The other person may have zero prior Pictiq knowledge.

### Showbook / flipbook

Each spread functions as a mini-poster intended to be shown to another person. The owner is not necessarily the audience: the owner selects the message, another person reads the displayed spread.

Low-risk candidate messages:

- I need food;
- I need water;
- please help;
- I need somewhere to sleep;
- can you take me there?;
- I am lost;
- toilet;
- phone/charging;
- simple transport/direction;
- basic safety/help.

Avoid high-stakes legal, medical, identity, eligibility, or emergency-authority claims.

## Scenario candidates

Future deployment/stress-test candidates, not current packs:

- Paris first visit;
- Gastronomic France;
- Digital / tech conference;
- Family travel;
- Road / wayfinding;
- Child cross-language communication.

Each future scenario should test Core + Context + composition + gaps + pack-level shorthand pressure.

## Existing/future publishing integrations

Pictiq may be integrated into:

- Tiny Language Protocol;
- Toki Pona and the Machine Mind;
- LitRPG/comic projects;
- children's picture books;
- a future Pictiq popular-science book.

Pictiq does not need to be the primary subject in every product.

## Current high-level tracks

### Active / can proceed without human recruitment

- Composer v0.1 release — RELEASED.
- Web/UI Stress Test.
- Logistics / Maritime Stress Test.
- Inspectable Action Receipt.
- Cross-model AI tests when practical.
- Publication milestones.
- Book evidence and content mapping.

### Opportunistic creative deployments

- Children's picture book with secondary Pictiq layer.
- LitRPG / comic Pictiq inserts.
- Tourist / scenario products.
- Gastronomic France.
- Child cross-language communication aid.
- Showbook / flipbook.

Children's products are not primarily "Learn Pictiq." They are picture books where Pictiq may act as a secondary symbolic layer for thought, speech, action, desire, or dialogue. The research hypothesis remains IMAGE -> STRUCTURED SYMBOLS -> LATER CONVENTIONAL WRITING, without claiming proven literacy benefit.

### Deferred human track

- Stress Test 04B.
- Pictiq Games / Human Communication Lab.
- Formal comprehension studies.
- Cross-cultural human tests.

These deferred human tracks must not block active development.

## Immediate active roadmap

1. Web/UI reconciliation + CHANGE — PUBLISHED TO MAIN.
2. Web/UI publication milestone — READY / BACKLOG.
3. English Landing v0.1 — CREATOR ACCEPTANCE PASSED.
4. EN -> PICTIQ translation architecture/methodology — CURRENT TASK.
5. Translate Header/Hero first.
6. Human review.
7. Translate the next accepted block, continuing block by block.
8. Integrate the EN | PICTIQ switch only after enough accepted translated blocks exist.
9. Full responsive/accessibility QA.
10. Production/legal/privacy review.
11. Configure `pictiq.abvx.xyz` only after review.
12. Public launch.
13. Observe real use and feedback.

Human/game tracks remain non-blocking. Composer v0.1 remains RELEASED as the current public authoring surface. The accepted English landing is `ENGLISH_SOURCE_BASELINE_V0_1`; future translation work should not silently rewrite it to make translation easier.

## Landing v0.1 acceptance closure — 2026-09-19

English Landing v0.1 and the Pictiq translation are **CREATOR ACCEPTED** and ready for public deployment verification. Once production verification completes, landing implementation and visual polish cease to be the active development track.

Immediate active work then returns to:

1. non-human, domain, and machine Pictiq research;
2. real deployments and use cases;
3. cross-model comprehension work;
4. opportunistic creative deployments.

The human/game track remains deferred and non-blocking. The landing result is a self-referential implementation result, not external human-comprehension evidence.

## Production closure — 2026-09-20

The Pictiq landing delivery is closed as a deployment track. `https://pictiq.abvx.xyz/` is live over HTTPS; root English mode, `?mode=pictiq`, Composer, and Lexicon are public. The production SEO / LLMO / project-discoverability pass is complete. Pictiq is also listed through the separate ABVX OS workflow as a project, production site, and free Handbook resource.

This is not a new publication event. Preserve the existing milestone cadence: `Can a Visual Language Explain Itself?` remains `READY / BACKLOG`. The next prepared research activity is Stress Test 05 manual cross-model execution; Stress Test 04B remains deferred and non-blocking.

## Stress Test 05 results-analysis next gate — 2026-09-20

The five supplied cross-model transcripts have been analyzed, but they describe an alternate image containing additive practical-quantity tiles rather than the published frozen 05A PNG/JSON. Before more model runs or any publication decision, reconcile the evidence against one hash-identified stimulus, verbatim prompt, and Handbook version. This is a methodology/documentation gate; it does not justify a vocabulary, grammar, Numeric Notation, icon, Renderer, Composer, landing, or production change.

## Stress Test 07 — prepared experiment — 2026-09-20

`Stress Test 07 — Explicit Grammar vs Contextual Compression` has an **INVALID / PARTIAL PILOT**: SVG source exposure, one delivery mismatch, and missing learning/transfer phases prevent a primary inference. `Stress Test 07.1` is **PREPARED / NOT EXECUTED** with the frozen design delivered only through neutral, metadata-free PNGs. It remains a controlled research follow-up to 05, 06 and 06B; no production or vocabulary track is reopened.

## Parallel knowledge-infrastructure architecture — 2026-09-27

The [Composition Library v0.1](../concepts/composition-library.md) and [future Translator architecture](../concepts/pictiq-translator-architecture.md) are documented as proposals only. They form a parallel knowledge-infrastructure / future product-architecture track, not an implementation commitment. The Composition Library is not a vocabulary registry, and the Translator is not implemented. Do not displace, alter, or wait on this work to resume the active controlled research experiment: Stress Test 07.1 remains **PREPARED / NOT EXECUTED**. Production cases remain their own evidence track.


## Composition Library architecture rotation — 2026-09-27

This dated status supersedes the earlier “Parallel knowledge-infrastructure architecture” note below for current execution order. It changes planning only; it does not erase or alter Stress Test 07.1 materials.

- **ACTIVE:** Composition Library architecture and Historical Harvest preparation.
- **NEXT:** Historical Composition Harvest, then human reconciliation.
- **THEN:** Practical Coverage Corpus → Composer coverage pass → Frequency / Semantic Coverage → Translator Spike → Agent Retrieval Stress Test → return to Stress Test 07.1.
- **PAUSED / PRESERVED:** Stress Test 07.1 — `PAUSED / PRESERVED / RETURN AFTER COMPOSITION-LIBRARY ROTATION`. Resume from the frozen package, with human-approved visual assets; automation may package approved assets byte-for-byte, strip metadata if required, assign neutral delivery names, hash, and manifest them. It must not redraw, reconstruct, optimize, or reinterpret stimuli. Preserve hypotheses, prompts, coding rules, assets, hashes, and forensic history.
- **DEFERRED:** Claude airport corpus pending its separate future scope; human recruitment/games remain in their existing deferred state. No release promise follows from this working order.

The Historical Harvest preparation-only status below is superseded by the dated completion update below. Current next gate is human reconciliation; the Practical Coverage Corpus remains later and has not started.

## Historical Composition Harvest complete — 2026-09-27

- **COMPLETE:** Historical Composition Harvest v0.1 at snapshot `8fae507`; 81 unique exact-message candidates plus separate evidence-only and unsafe inventories.
- **NEXT:** Human reconciliation of the harvested records, provenance, semantic neighborhoods, lifecycle, and schema-fit notes.
- **THEN:** Practical Coverage Corpus → Composer coverage → Frequency / Semantic Coverage → Translator Spike → Agent Retrieval Stress Test → return to Stress Test 07.1.
- **PAUSED / PRESERVED:** Stress Test 07.1 remains untouched and paused. Harvesting did not inspect its visual symbols as a means of reconstructing messages.
- The harvest is internal research evidence only. No public Composition Library, new protocol claim, product change, or vocabulary change follows from its counts.

## Human Reconciliation Viewer ready — 2026-09-27

- **CURRENT:** Composition Library Human Reconciliation v0.1 — `TOOL READY / CREATOR REVIEW PENDING`.
- **NEXT:** Creator completes review of all 81 exact Harvest candidates and exports the separate reconciliation overlay.
- **AFTER REVIEW:** Process the creator’s export and prepare a first accepted Composition Library baseline candidate for separate review.
- The Practical Coverage Corpus remains **NOT STARTED** until reconciliation processing is complete. Historical Harvest v0.1 remains frozen; Stress Test 07.1 remains paused and preserved.
