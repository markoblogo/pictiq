# Stress Test 05 — Zero-Training Visual Comprehension & Cross-Model Signaling

> Status: planning document only; experiment not run.
> Source event: Research & Deployment Policy pass, 2026-09-11.
> Boundary: no external model calls, no corpus execution, no language change.

## Purpose

Stress Test 05 tests the zero-training entry hypothesis through current multimodal AI systems. It asks whether a decoder that receives only rendered Pictiq images can infer useful meaning without the name Pictiq, vocabulary, grammar, internal IDs, Message JSON, examples, or repository links.

This is machine evidence. Cross-model agreement does not prove human comprehension.

## 05A — Blind visual decoding

A human author creates a Pictiq message in Composer. For each case preserve privately:

- intended meaning;
- required semantic slots;
- optional details;
- intentional omissions;
- source Message JSON;
- rendered visual artifact.

The decoder receives only the rendered Pictiq image.

Do not provide the Pictiq name, vocabulary, grammar, internal IDs, Message JSON, or intended meaning.

Neutral decoder prompt concept:

> This image contains a message or short dialogue expressed entirely through visual symbols. You have not been given its vocabulary or grammar. Interpret it as best you can. Describe the overall meaning, give your most likely reconstruction, and identify ambiguous parts or alternative readings.

Preserve the exact prompt later when the experiment is run.

## Initial 05 corpus plan

Plan about 10-12 new cases. Do not simply reuse Road/Odyssey fixtures that models may indirectly encounter through public project material.

Suggested progression:

1. very simple message;
2. question;
3. negation;
4. request/need;
5. 4-5-token composition;
6. two Frames;
7. short dialogue;
8. Entity Symbol;
9. broad/polysemous primitive;
10. intentional omission;
11. short narrative;
12. difficult boundary case.

Include easy cases where failure would be meaningful. The human author will create the final blind corpus later.

## Multi-model condition

Use several independent contemporary multimodal model families where practical. Do not hardcode versions now. At experiment time record provider, exact model ID, date, vision capability, parameters, prompt, and image supplied.

Prefer diversity across model families rather than many variants of one provider.

## Evaluation

Do not grade primarily by exact sentence match. Evaluate:

- overall intent;
- required semantic slots;
- participants/entities;
- action;
- object;
- negation;
- question;
- sequence;
- dialogue structure;
- important relations;
- invented/unjustified concepts;
- ambiguity.

Reuse semantic-compression labels where useful:

- `PRESERVED_EXPLICITLY`
- `PRESERVED_BY_COMPOSITION`
- `CONTEXT_SUFFICIENT`
- `INTENTIONAL_OMISSION`
- `LOSSY`
- `GAP`

## Cross-model agreement

Record where independent model families converge and where they diverge. Agreement is a signal, not proof of human comprehension.

## 05B — Reveal and repair

After blind decoding, reveal the intended meaning and ask the same model:

- what was ambiguous;
- what it misunderstood;
- which visual elements caused the problem;
- how it would make the message clearer using a similar visual-symbol approach.

Initially allow unconstrained visual suggestions. Do not automatically adopt model suggestions.

## 05C — Pictiq-constrained repair

Then provide current Pictiq vocabulary / available symbols and ask the model to reconstruct the intended message using only current Pictiq resources.

Compare:

- original human encoding;
- model unconstrained repair;
- model Pictiq-constrained repair.

Record recurring suggestions across model families.

## 05D — Cross-model signaling

Later condition:

MODEL A receives natural-language intent -> constructs Pictiq -> MODEL B receives only rendered Pictiq -> reconstructs intent.

Rotate senders/receivers where practical. Exact providers/models are chosen at run time.

## Semantic-native control

For selected cases, run a separate control where the model receives canonical Message representation / IDs rather than rendered image. This distinguishes visual recognition failure from composition/semantic failure. Do not mix this with the zero-training primary condition.

## Failure taxonomy

- `ICON_RECOGNITION_FAILURE`
- `ENTITY_RECOGNITION_FAILURE`
- `COMPOSITION_FAILURE`
- `ORDER_FAILURE`
- `FRAME_DIALOGUE_FAILURE`
- `POLYSEMY_FAILURE`
- `NEGATION_FAILURE`
- `QUESTION_FAILURE`
- `CONTEXT_FAILURE`
- `UNJUSTIFIED_INFERENCE`
- `MODEL_SPECIFIC_FAILURE`
- `CROSS_MODEL_FAILURE`
- `POSSIBLE_LANGUAGE_PRESSURE`
- `TRUE_GAP_CANDIDATE`

Do not classify every failure as Pictiq failure.

## Language change gate

Stress Test 05 must not automatically change Pictiq. A language/vocabulary change candidate should require evidence such as:

- recurring failure across several independent models;
- failure persists in constrained repair;
- current composition is genuinely inadequate;
- issue is not merely icon recognition;
- issue matters to intended Pictiq use.

All changes require later human review.

## Publication milestone

Stress Test 05 is a likely publication milestone. Potential editorial angle: "Can AI read a visual language it has never seen before?"

Possible outputs include a public article, technical appendix, figures/QA sheets, and book material.
