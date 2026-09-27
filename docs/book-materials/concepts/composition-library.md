# Pictiq Composition Library v0.1 — architecture concept

> **Status:** research / knowledge-infrastructure proposal; not implemented, not normative, not a vocabulary source.
> **Current controlled research status:** Stress Test 07.1 — `PAUSED / PRESERVED / RETURN AFTER COMPOSITION-LIBRARY ROTATION`.

## Purpose and boundary

The **Lexicon** answers: “What primitives exist?” A future **Composition Library** would answer: “Which communicative intents have been represented with those primitives, under what context, with what provenance and evidence?” It is an evidence-bearing reference for compositions, not another lexical registry and not an English-to-Pictiq phrase table.

The library could serve as:

1. a human reference for how existing primitives have been assembled;
2. a check against unnecessary vocabulary growth;
3. a durable record of compositions discovered in research, books, interfaces, deployments, and human review;
4. a retrieval source for a future Translator before it attempts constrained generation;
5. an evidence record that lets a candidate accrue human, production, and test evidence without silently becoming “correct Pictiq”;
6. a memory of ambiguity, rejected attempts, and known failures as well as useful examples.

The library has no authority to change Grammar, the Lexicon, the Message Schema, or the meaning of an icon. It is downstream of those sources. A normative Grammar example can be recorded with its source authority; an external reviewer’s proposed phrase remains an external candidate.

## Message formation: compose intent, do not translate words

The repository already has the principles needed to explain Pictiq message formation. This note reconciles them; it adds no normative doctrine.

`MEANING-BEFORE-WORDING`, `PRIORITY-FIRST COMMUNICATION`, and `FUNCTIONAL SUFFICIENCY` apply to practical communication: preserve what the receiver needs for the goal, lead with the highest-priority actionable meaning, and stop when the message is sufficient for an appropriate response. They do not license distortion or universal omission. `NEED-BEFORE-VOCABULARY` governs when a new symbol may be considered. `EMBODIED` / `STANDALONE` tells us which information the communicator, gesture, visible referent, shared location, or durable artifact must carry. `CONTEXT` and `POLYSEMY` constrain interpretation; they do not make every adjacency safe.

Use this authoring/review sequence:

1. What is the communicative intent?
2. Which information changes the receiver’s relevant action, decision, safety, rights, or interpretation?
3. What does the actual social and physical context already provide?
4. Can an existing primitive express the intent directly?
5. Can existing primitives compose it under the current Grammar?
6. Can named context or action-relevant polysemy supply a distinction honestly?
7. Can secondary information be intentionally omitted without distorting the task?
8. Is the result functionally sufficient for this receiver, mode, and task?
9. If not, is a relevant distinction `LOSSY`, or is there a true `GAP` in current Pictiq capacity?
10. Only then consider vocabulary pressure under `NEED-BEFORE-VOCABULARY`.

The exact current governance order is **existing primitive → composition → context → polysemy → intentional omission → only then consider a new symbol**. The Protocol additionally asks whether embodiment supplies meaning reliably, whether the standalone surface must preserve it, whether a modifier/operator, parameter, or scoped Entity Symbol is more appropriate, and whether the remaining result is embodied-omittable, standalone gap, out-of-scope, intentional omission, lossy, or gap. The [Protocol](../../../spec/PROTOCOL.md), [Grammar](../../../spec/GRAMMAR.md), [Vocabulary Governance](../../../spec/VOCABULARY_GOVERNANCE.md), and [Semantic Compression Framework](semantic-compression-framework.md) remain authoritative.

### Preservation terms

Use the existing research assessment labels where they apply: `PRESERVED_EXPLICITLY`, `PRESERVED_BY_COMPOSITION`, `CONTEXT-SUFFICIENT`, `INTENTIONAL_OMISSION`, `LOSSY`, `GAP`, and `OUT-OF-SCOPE`. Also retain Protocol absence/surface states such as `EMBODIED-OMITTABLE` and `STANDALONE-GAP` when relevant. These are assessments, not grammar tokens or new Message Schema fields.

Do not overload assessment with method. A message may use direct tiles and also be context-sufficient; a composition may intentionally omit low-priority background while losing another needed distinction. Record each semantic slot or intent neighborhood separately when one overall label would hide this. No preservation result is implied by storage in the library.

## Composition records and semantic neighborhoods

The proposed record model is in the [machine-readable record schema proposal](composition-library-record.schema.proposal.json). Each exact-message record may have multiple evidence-scoped `applicability` entries, each pairing one mode, one extensible surface, structured context, and evidence. A shared intent neighbourhood may carry coverage findings by mode/surface, including LOSSY or GAP when no exact composition exists. The schema is a discussion artifact only; it is not used by CI and does not authorize a production registry.

One record represents one exact Pictiq Message (including its Message Schema form, frames, Entity Symbol namespace, and formal numeric tokens where present) with its evidenced mode, surface, and compatibility context. It can support multiple **context-bounded semantic neighborhoods**. This avoids duplicating a record for every English paraphrase while preserving ambiguity limits. Different compositions that serve approximately the same intent in different contexts remain separate records and may be cross-linked. A shared intent/neighbourhood reference links records; it does not make their messages interchangeable. The relationship is many-to-many:

```text
one semantic intent/neighborhood → one or more exact composition records
one exact composition → one or more supported, context-bounded interpretations
```

For example, a sequence such as `WATER + punct_question` might, depending on the named context and evidence, support “Water?”, “Do you have water?”, or “Is water available?” A library must not flatten those into three fixed word-for-word translations or claim they are interchangeable everywhere. It should record what context supports each reading, the evidence for that reading, and any unresolved ambiguities.

`semantic_examples` are examples of intended communicative meaning, not canonical English glosses. Keep **SOURCE TEXT**, **SEMANTIC INTENT**, **COMPOSITION RECORD**, **PICTIQ MESSAGE JSON**, **AUTHORING SHORTHAND**, and **RENDERED SVG/PNG** as separate layers. Reuse the existing [Pictiq Message Schema](../../../spec/pictiq-message.schema.json) for the actual message; do not invent a second Pictiq syntax.

## One intent across modes and surfaces

Mode and surface are separate: `EMBODIED` / `STANDALONE` says whether a live communicator/body/situation supplies meaning; `LIVE_INTERACTION`, `BOOK`, `COMIC`, `SIGN`, `UI`, `PORTABLE_CARD`, `LOCKSCREEN`, `LABEL`, `STICKER`, `WAYFINDING`, and `OTHER` say where/how a representation is consumed. Surface labels are extensible examples, not a closed enum. A book/comic remains STANDALONE even when its illustration, panel order, speaker, known character, prior turn, or scene supplies context.

The record model supports the required cases without treating records as translations: (A) one exact Message can have multiple evidence-scoped applicability entries; (B) compact EMBODIED and expanded STANDALONE Messages are separate records linked by the same intent/neighbourhood; (C) neighborhood coverage findings can mark one mode/surface SUPPORTED and another LOSSY/GAP; (D) BOOK and SIGN can have separate applicability contexts or linked compositions; (E) one exact composition can link to several context-bounded semantic neighborhoods; (F) competing candidate Messages remain separate records with separate evidence histories. These are model capabilities, not populated examples or accepted translations.

Mode-aware coverage distinguishes “can express this intent?” from “can express it under this mode + surface + context?” It can record a gap even when no exact composition exists, without manufacturing a placeholder Message.

## Context is structured and open-ended

Context is first-class, not one free-form tag. Proposed dimensions are extensible strings rather than frozen vocabularies:

| Dimension | Examples (illustrative, not controlled values) |
|---|---|
| `domain` | travel, airport, road, food, web-ui, fiction, Odyssey |
| `situation` | border inspection, restaurant order, book scene, settings dialog |
| `communication_mode` | `EMBODIED`, `STANDALONE` (existing Protocol distinction) |
| `communication_surface` | `LIVE_INTERACTION`, `BOOK`, `COMIC`, `SIGN`, `UI`, `PORTABLE_CARD`, `LOCKSCREEN`, `LABEL`, `STICKER`, `WAYFINDING`, `OTHER` (extensible examples) |
| `interaction` | turn-taking, pointing, display, reading, scanning (descriptive, not the surface field) |
| `audience` | traveler, reader, staff member, machine |
| `task` | ask for help, identify a referent, preserve an event sequence |

Record `REQUIRED_CONTEXT` separately from `OPTIONAL_CONTEXT`. Also record what the context actually supplies (`context_supplies`): visible referent, pointing, gesture, gaze, speaker/listener identity, shared location, current transaction, previous turn, UI state, illustration/panel, narrative scene, established character identity, sign placement/direction, or held object. Each supplied cue should point to evidence establishing availability; an imagined “common ground” is not evidence. `communication_mode` answers whether communicator/body/shared live situation is available; `communication_surface` answers where/how the representation persists and is consumed. BOOK/COMIC remain `STANDALONE` even when panel, character, and prior-turn context supports a shorter message.

Where a context is essential, a message may be unsafe or unintelligible outside that context. Context Packs constrain available vocabulary and conventions but do not by themselves prove that a receiver knows the situation. The `profile`/`contexts` fields of a Pictiq Message remain governed by Message Schema; library context metadata adds provenance and retrieval constraints only.

## Provenance and evidence model

One `source` field is insufficient. Separate:

- **ORIGIN** — where this exact composition was first recorded;
- **USES[]** — each subsequent application, with role and context;
- **TESTS[]** — each study/test and its method, status, stimulus/message version, and results reference;
- **FAILURES[]** — attempted intent/composition, context, observed reading, failure type, evidence, and disposition.

References should include a stable repository path or external source, section/case/turn/fixture, Git commit or release, Pictiq and Message Schema version, and a hash where a frozen asset or exact transcript matters. Event dates are recorded only when present in evidence; unknown dates stay unknown. A version change never rewrites old use/test facts. It may mark a record as needing review or deprecated while preserving its historical message unchanged.

Suggested source-type examples include `GRAMMAR`, `PROTOCOL`, `HANDBOOK`, `STRESS_TEST`, `EDITORIAL_CASE`, `LANDING`, `WEB_UI`, `ROAD_WAYFINDING`, `ODYSSEY`, `COMPOSER_EXAMPLE`, `HUMAN_REVIEW`, and `PRODUCTION_DEPLOYMENT`. These are open examples, not a new source taxonomy.

### Editorial-case rule

Editorial cases may establish production use without preserving a reusable message mapping. Harvest a composition only when the semantic source maps reliably to the actual Pictiq Message or Composer output. Flattened artwork is not sufficient authority to infer IDs, order, or speaker mapping.

- **Case 001 — Bracken Ford:** production use is recorded, but its own case record says independent Composer export, sequence JSON, and exact panel mapping are not retained. Semantic summaries do not expose canonical token IDs. Production-use evidence is harvestable as a case event; exact composition records are **not safe to harvest** until source-to-output mapping is preserved.
- **Case 002 — Good Dog, Bad System:** approved dialogue and Composer source sheets are preserved, but per-turn Composer blocks/regions and exact source-sheet mapping are unresolved. GD1–GD4 flattened art must not be reverse-engineered. Dialogue semantics and production source provenance can be indexed as incomplete evidence; exact compositions are **not safe to harvest** until block mapping is resolved.

## Lifecycle, evidence, and negative knowledge

Use one **lifecycle status** plus independent, sourced evidence events. Do not encode “production used” or “tested” as mutually exclusive statuses; a record can have both after separate events. Suggested lifecycle values for a proposal are:

- `CANDIDATE` — an unverified proposal;
- `EXPERIMENTAL` — used in a named experiment, with no general acceptance implied;
- `HUMAN_ACCEPTED` — a human accepted this composition for the stated use/context;
- `NORMATIVE_EXAMPLE` — explicitly designated by project governance as a normative example under current rules;
- `REJECTED` — rejected for the stated intent/context, with reason;
- `DEPRECATED` — superseded for current use, with historical record retained.

`CONTEXT_DEPENDENT` is a property/constraint of a composition, not a lifecycle status. Production use and tests belong in `USES[]` and `TESTS[]`; a production appearance is not comprehension evidence. A successful test is scoped to its method/sample/context and does not automatically make a composition normative. Human acceptance alone does not establish comprehension. Promotions require explicit evidence and a human decision; generated candidates never self-promote.

Failure memory is first-class. Store attempted intent, exact attempted message, test context, observed interpretation, risk, failure type, evidence source, and disposition such as rejected, ambiguous, needs context, lossy, or superseded. This prevents a future Translator from repeatedly selecting known-bad candidates based only on text similarity.

Do not assign an aggregate numeric confidence score at v0.1. Preserve method, sample, context compatibility, uncertainty, and failure history so future retrieval can explain evidence without pretending that heterogeneous evidence is commensurable.

## Bootstrap assessment — bounded, evidence-first

Principle: **HARVEST BEFORE GENERATE.** Do not mass-populate this proposal. A future Batch 01 should be a manually reviewed, bounded set (roughly 20–40 records is a planning scale, not a target) selected only where semantic intent ↔ exact Message is recoverable. Prefer a smaller set if provenance is weak. Every row remains traceable to source and version.

| Source family | Assessment | Harvest boundary |
|---|---|---|
| Protocol / Grammar | `HARVESTABLE NOW` | Explicit normative examples can seed records, preserving exact authority, current token IDs, conditions, and examples as normative examples only when the spec marks them so. Rules are not converted into unbounded phrase generation. |
| Handbook examples | `PARTIALLY HARVESTABLE` | Use only examples whose intent, message, context, and version are explicit. Narrative/descriptive prose is not enough to infer token sequences. |
| Renderer fixtures and `examples/messages` | `PARTIALLY HARVESTABLE` | Exact Message JSON is explicit; semantic intent is often absent or only in a filename. Harvest as render/validation use evidence until intent provenance is paired. |
| Composer examples | `PARTIALLY HARVESTABLE` | Exact message may be visible in a fixture/UI, but first preserve its semantic purpose and stable example identity. Creator examples are not user comprehension results. |
| Portable layouts | `PARTIALLY HARVESTABLE` | Exact tile group may be evident, but surrounding layout context and intended task may be ambiguous. Preserve surface and context; do not infer phrase gloss from decoration. |
| Road / Wayfinding Stress Test | `PARTIALLY HARVESTABLE` | Source intent, human reconciliation, outcome classes, and accepted visual result exist; harvest only cases with reliable current message mapping. Preserve test origin and distinction from normative grammar. |
| Odyssey Stress Test | `PARTIALLY HARVESTABLE` | Source fragments, manual semantic areas, contextual language candidates, and accepted vocabulary changes exist; individual composition provenance varies. Keep narrative intent/order and omission rationale; do not extract from artwork alone. |
| Web/UI Stress Test | `PARTIALLY HARVESTABLE` | Human semantic reconciliation records composition/context mappings and explicit counts, but a final exact Message may not be available for each row. Attach evidence/status per row. |
| Landing translation | `HARVESTABLE NOW` for explicit rows | The accepted translation table records intent, Pictiq representation, context/omission, and outcome. Preserve it as creator-accepted deployed production/use evidence, not external comprehension. |
| Stress Test 05 | `PARTIALLY HARVESTABLE` | Frozen target/message mappings can be stored as experimental stimuli; supplied cross-model transcripts mismatch the frozen published stimulus and cannot be merged as its result. Do not turn model guesses into human-accepted composition. |
| Stress Test 06 | `NOT SAFE TO HARVEST` as accepted Pictiq compositions | It studies generative symbol convergence; generated proposals and cross-model agreement are not accepted Pictiq output. Specific Pictiq comparison rows may be indexed only as experimental candidates with exact provenance. |
| Stress Test 06B | `NOT SAFE TO HARVEST` as Pictiq compositions | Independent systems were created before Pictiq disclosure; their architectures and proposals are comparative evidence, not Pictiq messages. |
| Stress Test 07 / 07.1 | `PARTIALLY HARVESTABLE` as test artifacts only | 07 pilot is invalid/partial for primary inference. 07.1 stimuli and target are frozen but unexecuted. Keep status and version explicit; no result/acceptance flags. |
| Editorial Case 001 — Bracken Ford | `NOT SAFE TO HARVEST` as exact messages at current provenance | Production use is established, but the case itself identifies missing independent Composer exports, sequence JSON, and exact panel mapping. Preserve production-use event; do not infer IDs from flattened art. |
| Editorial Case 002 — Good Dog, Bad System | `NOT SAFE TO HARVEST` as exact messages at current provenance | Semantic dialogue, speaker boundaries, Composer sheets, and flattened art are preserved, but per-turn Composer block mapping is unresolved. Record source/reference links and unresolved status, not invented compositions. |

The bounded first batch should select about 20–40 **records only if provenance permits**, beginning with normative examples and explicit accepted Road/Web/UI/Landing compositions, plus exact fixtures paired with semantic source. This pass creates no batch and no registry.

## Mode-aware coverage, machine access, and workflows

Coverage must distinguish “can express this intent?” from “can express it under this mode + surface + context?” The same intent can have the same message in both modes, a compact EMBODIED and expanded STANDALONE message, or a supported EMBODIED form and STANDALONE `LOSSY`/`GAP`. BOOK and SIGN may need distinct standalone records when each supplies different context. Several candidate records may coexist with separate evidence/failure histories; identical messages can also support several named-context neighbourhoods. Coverage counts are not computed in this proposal.

A future machine/agent layer retrieves authoritative Lexicon primitives, exact Library records, Message JSON, evidence, and canonical assets; it does not become another semantic registry. Forward translation is intent → resolve mode/surface/context → Library retrieval → Lexicon/Grammar fallback → validation → canonical render → human decision. Reverse/reference lookup prefers Message JSON or provenance sidecar, then structured export and canonical IDs/hashes, then visual matching; unconstrained vision is last-resort candidate evidence, never canonical identification by itself.

AI may reason about or propose semantics, but must not synthesize or redraw canonical glyph artwork when canonical assets exist. Canonical visual output comes from canonical SVGs, deterministic Renderer output, or preserved immutable Composer/Renderer exports. Discoverability does not grant reuse rights. A future Composer sidecar such as `dialogue-03.pictiq.json` may link existing Message JSON with stable block/frame/source-turn IDs, speaker, mode, surface, context, placement, version, and hashes without duplicating message authority. Case 002 demonstrates the need: semantic dialogue and source sheets exist, but exact per-turn Composer-block mapping remains unresolved; do not infer it from flattened art. See [Machine / Agent Access](pictiq-machine-agent-access.md).

## Future coverage metrics and public surface

If implemented later, coverage reporting might distinguish ordinary primitives, Entity Symbols, documented compositions, human-accepted compositions, production-used compositions, tested compositions, known ambiguous/rejected compositions, and unresolved gaps. Compute only from a validated machine-readable registry with explicit definitions. Current values are not claimed here.

A future public Composition surface could complement the Lexicon and Composer:

- **Lexicon:** which signs exist;
- **Compositions:** what messages have been built, in which context, and with what evidence;
- **Composer:** build and edit a Message;
- **Translator:** propose a Message from semantic input.

One composition page could display intent neighborhood, exact Pictiq Message, canonical render, context, lifecycle, where used, evidence, and known ambiguity/failures. It remains a possible public value proposition, not a page or navigation decision now.

## Related roadmap boundary

Composition Library is **knowledge infrastructure**. Stress Test 07.1 remains the **active controlled research experiment**. Editorial Cases 001/002 remain **production evidence**. The future Translator is a separate **product/machine architecture**. Evidence in one track does not automatically validate another.
