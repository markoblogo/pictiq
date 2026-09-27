# Pictiq Translator — future architecture proposal

> **Status:** future architecture only; not implemented, benchmarked, or accepted as product behavior.
> **Research rotation:** Stress Test 07.1 is paused and preserved; it is not cancelled.
> **Boundary:** the Translator assists a human; it is not a language authority. It does not change Message Schema, Grammar, Lexicon, Composer, Renderer, production landing, or licenses.

## Architecture constraint

The Translator must not be a word-to-icon mapper.

```text
Bad:       source word → icon
Preferred: source → communicative intent → task-faithful compression
           → context → known composition or constrained candidate
           → validated Pictiq Message → rendered preview → human decision
```

It should follow existing `MEANING-BEFORE-WORDING`, `PRIORITY-FIRST COMMUNICATION`, `FUNCTIONAL SUFFICIENCY`, and `NEED-BEFORE-VOCABULARY` principles. It should explain what it preserved, what the context supplies, what it intentionally omitted, and which distinctions remain lossy or unrepresented. The Pictiq Message Schema and Grammar stay the only sources of valid message structure and token behavior.

## Proposed pipeline

```text
Natural-language / dialogue / narrative / UI / structured intent
    ↓
Resolve communicative intent + receiver/task + `EMBODIED` / `STANDALONE` mode
    ↓
Resolve communication surface + available context (unknown material constraints trigger a question, alternatives, or explicit assumptions)
    ↓
Segmentation → semantic intent units → action / priority analysis
    ↓
Composition Dictionary retrieval (reusable known solutions)
    ↓ on miss / for broader evidence
Composition Corpus retrieval (historical, experimental, narrative, production, rejected, and failure evidence)
    ↓ on miss
Lexicon + Grammar constrained candidate generation
    ↓
Message Schema + registry + grammar/profile/context validation
    ↓
Renderer preview → candidate comparison / uncertainty explanation
    ↓
Human selection, repair, or rejection
    ↓ optional, provenance-preserving evidence proposal to Composition Library
```

Keep these representations distinct: SOURCE TEXT; SEMANTIC INTENT; COMPOSITION LIBRARY RECORD; PICTIQ MESSAGE JSON; AUTHORING SHORTHAND; RENDERED SVG/PNG. Existing Renderer output validates and previews a representation; it cannot prove semantic adequacy. Syntax/registry validity does not guarantee correct translation. The 04A pilot and text-to-Pictiq prototype document generation/representation failures and remain research baselines, not an accepted translator.

## Input and translation modes

Future inputs may include one practical phrase, multi-turn dialogue, UI copy, a landing/article paragraph, literary text or scene, and structured machine intent. They are not equally solvable or interchangeable.

Potential translation profiles are hypotheses only: `PRACTICAL / PRIORITY-FIRST`, `UI / INTERFACE`, `NARRATIVE / EDITORIAL`, `SIGN / STANDALONE`, `EMBODIED DIALOGUE`, `MACHINE / STRUCTURED INTENT`. The implementation should reuse current Message `profile` and `contexts` where appropriate, but not add production profiles or schema fields before a separate decision and evidence.

Practical communication can prioritize immediate action and functional sufficiency. UI may inherit a visible screen and workflow state. Standalone signs/cards must work without the communicator or transient situation. Structured machine intent may need a Pictiq preview alongside—not instead of—a stricter domain schema or permission check.

Literary/editorial work has a different target from practical communication. Event order, character identity, relationships, causal distinctions, tone-relevant information, and recurring motifs may matter even if not immediately actionable. Odyssey research shows narrative skeleton and deliberate omission need separate review; Editorial Cases 001/002 preserve source → selected semantic layer → Pictiq production as distinct stages. Do not apply a single universal compression objective to all domains. Longer narrative input will likely need human-reviewed segmentation and per-unit decisions; aggressive practical omission can erase narrative meaning.

## Segmentation and task model

Do not translate a paragraph or dialogue block as one giant phrase. A future process should:

1. segment source into intent units (propositions, turns, UI actions, or narrative beats);
2. identify the receiver, task, action, and information whose loss changes that task;
3. order units by priority or source sequence according to the selected mode;
4. retrieve/compose each unit independently while preserving dependencies and speaker/source links;
5. optionally recompose units into Message frames without inventing causality or clause relations.

Each unit should retain a pointer to source span/turn and structured semantic notes. The message output can remain the existing flat ordered-token form. Grouping or causal edges are not smuggled into Message v0.1.

## Retrieval hierarchy

Implementation-neutral retrieval should consider, in order:

1. exact or near intent in the Composition Dictionary in a compatible context, with relevant, strong evidence;
2. a semantic-neighborhood match in the Dictionary whose context constraints are satisfied;
3. broader Composition Corpus evidence, clearly distinguished by source, context, and authority (a narrative fragment is not thereby a reusable dictionary answer);
4. a reusable composition template that can be instantiated with current valid IDs;
5. Lexicon + Grammar constrained generation;
6. human-guided construction in Composer or equivalent authoring tools;
7. `GAP` / `VOCABULARY_PRESSURE` when no honest sufficient expression exists.

Dictionary eligibility is separate from semantic acceptance. Proposed eligibility values are `YES`, `CORPUS_ONLY`, and `REVIEW`; they are not lifecycle states or creator semantic decisions. Do not filter out an accepted Corpus record merely because it is not a Dictionary entry.

No embedding model, vector database, LLM, RAG stack, or vendor is selected. Retrieval should consider semantic fit, context compatibility, source quality, lifecycle, current validity, known ambiguity, tests/uses, and known failures. A failed candidate must not become the default due to lexical similarity. `PRODUCTION_USED + TESTED` would usually supply different evidence from `GENERATED_CANDIDATE`, but there is no numeric scoring formula proposed.

The system may return multiple candidates, including different exact messages for the same intent across mode/surface contexts. For each, show semantic neighborhood, exact Message JSON, canonical render reference, mode/surface match, context supplies/assumptions, lifecycle/evidence, uses/failures, preservation assessment, and uncertainty. Human selection and repair are first-class. Unknown mode/surface must not silently default to live or standalone: ask, offer alternatives, or label assumptions.

## Candidate outcomes (proposed Translator API, not protocol enums)

Potential result classes are:

- `KNOWN_COMPOSITION`;
- `KNOWN_CONTEXTUAL_COMPOSITION`;
- `MULTIPLE_CANDIDATES`;
- `GENERATED_CANDIDATE`;
- `INTENTIONAL_OMISSION`;
- `LOSSY`;
- `GAP`;
- `VOCABULARY_PRESSURE`;
- `NEEDS_HUMAN_REVIEW`.

These labels would report a translation attempt. They are not new Grammar, Message Schema, Lexicon classifications, or protocol states. Several may accompany one segmented input. The system must be able to say “I do not know how to express this reliably.” A candidate's syntactic validity is not a semantic confidence claim. Avoid a numeric confidence score until a useful, calibrated evidence model exists.

## Vocabulary-pressure loop

When translation fails, use the accepted sequence: (1) search known compositions; (2) try existing primitives; (3) try current composition; (4) test named context and action-relevant polysemy; (5) consider intentional omission; (6) label meaningful loss; (7) identify a true gap; and (8) only then emit vocabulary pressure. Vocabulary creation remains a separate, human-governed NEED-BEFORE-VOCABULARY process. A Translator never creates a canonical icon or ID. Composition Library lookup is retrieval memory, not a license to treat a near match as established.

## Safety and authority

For medical urgency, missing people, danger, prohibitions, emergencies, and other action-critical meanings, a short or plausible-looking composition is not sufficient by itself. If ambiguity could materially change the action, prefer `NEEDS_HUMAN_REVIEW`, `LOSSY`, or `GAP` over false certainty. This is an architecture boundary, not a complete safety policy. Pictiq is not an authority for legal, medical, financial, identity, eligibility, consent, or destructive actions; use required text/professional process and structured controls.

The future Translator may retrieve, propose, compare, explain, flag uncertainty, render, and identify possible gaps. It may **not** autonomously create canonical vocabulary, redefine icon meaning, change Grammar, promote an experimental composition to normative, or resolve safety-critical ambiguity without human review.

## Evidence and learning loop

```text
SOURCE INTENT
→ candidate from known composition or constrained generation
→ human correction / selection / rejection
→ Composer authoring + Renderer preview
→ real use (if any)
→ provenance/evidence event
→ proposed Composition Library update for review
```

`GENERATED_CANDIDATE → HUMAN_ACCEPTED → PRODUCTION_USED → TESTED` is one possible sequence, not a mandatory pipeline. Evidence may arrive in another order, and each event has a different meaning. A generated candidate never automatically becomes accepted. Human acceptance is scoped to a use; production use records that it appeared in a product; a test records its method and result. The Composition Library human-governed lifecycle decides what status follows.

Future Composer integration may let the Translator submit valid candidate Message JSON to Composer, where a person inspects and edits it. Reverse/reference lookup should prefer exact Message JSON, Composer/Renderer structured export, and canonical asset IDs/hashes before visual matching; vision can suggest candidates only when structured provenance is absent. The AI must retrieve canonical SVG/Renderer output and must not draw substitute glyphs. A future provenance sidecar could preserve block/frame/source-turn IDs and source placement; Case 002 exact per-turn mappings remain unresolved and must not be reconstructed from flattened artwork. Machine/agent discovery is a prerequisite architecture, described separately in [Pictiq Machine / Agent Access](pictiq-machine-agent-access.md). An accepted composition may be saved with intent and provenance metadata separately from the message itself. Future Composer exports could include stable block/frame IDs, speaker IDs, semantic-source references, and placement references. These are future ideas, not changes to Composer v0.1. Case 002’s unresolved per-turn block mapping is concrete workflow friction: do not infer mapping from flattened artwork.

## Known limits and future health metrics

Any later expressive-coverage metric must distinguish ordinary primitives, Entity Symbols, documented compositions, human-accepted compositions, production-used compositions, tested compositions, known ambiguous/rejected compositions, and known gaps. Do not advertise counts until there is a validated, evidence-bearing library and clear counting rules.

The Composition Library could eventually demonstrate practical expressive capacity alongside the Lexicon. A future public surface may show intent, composition, render, context, status, where used, and evidence. The Lexicon, Composition Library, Composer, and Translator remain distinct: what signs exist; what messages were evidenced; how people build/edit; how a candidate may be proposed.

## Current-track boundary

- **Paused controlled research:** Stress Test 07.1, preserved and to resume after the Composition Library rotation.
- **Production evidence:** Editorial Case 001 — Bracken Ford; Editorial Case 002 — Good Dog, Bad System.
- **Knowledge infrastructure:** Composition Library v0.1 proposal.
- **Future product/machine architecture:** Pictiq Translator proposal.
- **Documentation pressure:** README/Handbook should eventually explain composition-first formation more clearly; no rewrite here.

These tracks do not substitute for one another. This rotation pauses (does not cancel or redesign) Stress Test 07.1; neither architecture proposal establishes comprehension or creates a public Translator. A future Agent Retrieval Stress Test is planned separately and is not a comprehension test.
