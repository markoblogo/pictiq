# Constrained Translation Pilot Stress Test 04A

> Status: pilot results / research artifact  
> Date: 2026-09-11  
> Provider/model: OpenAI / gpt-5.1-2025-11-13  
> Boundary: no RAG, no translator implementation, no Composer, no vocabulary/grammar/icon/schema/renderer change.

## Research question

Can an LLM produce schema-valid, registry-valid, semantically reasonable Pictiq Message JSON v0.1 directly from simple natural-language intents?

## Method

- Corpus: 18 cases, built before model output.
- Repeats: 1 per case.
- Structured-output method: Chat Completions response_format json_schema using spec/pictiq-message.schema.json with strict=false.
- Provider guarantee recorded: syntactic JSON was observed; full schema, enum, and registry conformance still required local validation.
- Primary condition: no RAG, no embeddings, no TF-IDF, no fuzzy lookup.

## Metrics

| Metric | Result |
| --- | ---: |
| Runs | 18 |
| Schema-valid outputs | 13 / 18 |
| Registry-valid outputs | 13 / 18 |
| Renderable outputs | 13 / 18 |
| Semantic slots recovered in renderable normalized messages | 24 / 32 |
| Raw semantic slots present before validation gate | 32 / 32 |
| Cases with unjustified concepts | 7 |
| Legacy-ID cases | 0 |
| Model-instruction/schema-leakage failures | 5 |
| True vocabulary-gap candidates | 0 |
| Intentional-omission successes | 0 |

## Case table

| Case | Category | Schema | Registry | Rendered | Slots | Unjustified | Classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 04a-01 | DIRECT_BASIC | no | no | no | raw 1/1; rendered 0/1 | person_generic | MESSAGE_SCHEMA_FAILURE, REGISTRY_FAILURE, MODEL_INSTRUCTION_FAILURE, CONCEPT_SELECTION_FAILURE |
| 04a-02 | DIRECT_BASIC | yes | yes | yes | raw 2/2; rendered 2/2 | - | OK |
| 04a-03 | DIRECT_BASIC | yes | yes | yes | raw 2/2; rendered 2/2 | - | OK |
| 04a-04 | DIRECT_BASIC | yes | yes | yes | raw 2/2; rendered 2/2 | - | OK |
| 04a-05 | COMPOSITION | yes | yes | yes | raw 2/2; rendered 2/2 | - | OK |
| 04a-06 | COMPOSITION | yes | yes | yes | raw 2/2; rendered 2/2 | - | OK |
| 04a-07 | COMPOSITION | yes | yes | yes | raw 2/2; rendered 2/2 | - | OK |
| 04a-08 | COMPOSITION | yes | yes | yes | raw 1/1; rendered 1/1 | - | OK |
| 04a-09 | NEGATION_EVALUATION | yes | yes | yes | raw 2/2; rendered 2/2 | logic_no, qty_minus | CONCEPT_SELECTION_FAILURE |
| 04a-10 | NEGATION_EVALUATION | yes | yes | yes | raw 2/2; rendered 2/2 | comm_speak, logic_yes | CONCEPT_SELECTION_FAILURE |
| 04a-11 | NUMBER | no | no | no | raw 1/1; rendered 0/1 | - | MESSAGE_SCHEMA_FAILURE, REGISTRY_FAILURE, MODEL_INSTRUCTION_FAILURE |
| 04a-12 | NUMBER | no | no | no | raw 2/2; rendered 0/2 | person_generic | MESSAGE_SCHEMA_FAILURE, REGISTRY_FAILURE, MODEL_INSTRUCTION_FAILURE, CONCEPT_SELECTION_FAILURE |
| 04a-13 | ENTITY | no | no | no | raw 2/2; rendered 0/2 | - | MESSAGE_SCHEMA_FAILURE, REGISTRY_FAILURE, MODEL_INSTRUCTION_FAILURE |
| 04a-14 | ENTITY | yes | yes | yes | raw 3/3; rendered 3/3 | - | OK |
| 04a-15 | CONTEXT_POLYSEMY | no | no | no | raw 2/2; rendered 0/2 | - | MESSAGE_SCHEMA_FAILURE, REGISTRY_FAILURE, MODEL_INSTRUCTION_FAILURE |
| 04a-16 | INTENTIONAL_OMISSION | yes | yes | yes | raw 1/1; rendered 1/1 | media_image, rel_here | CONCEPT_SELECTION_FAILURE |
| 04a-17 | BOUNDARY | yes | yes | yes | raw 2/2; rendered 2/2 | person_generic | CONCEPT_SELECTION_FAILURE |
| 04a-18 | BOUNDARY | yes | yes | yes | raw 1/1; rendered 1/1 | place_home | CONCEPT_SELECTION_FAILURE |

## Schema friction

MINOR FRICTION. Five outputs copied the schema document `$id` into the generated message. This is a recurring model/provider-mode instruction failure, not evidence that Pictiq Message Schema v0.1 should change. The OpenAI Chat Completions `json_schema` mode was used with `strict=false` because the repository schema is the accepted v0.1 schema, not a provider-specific strict subset. Local validation remained necessary and caught schema/registry problems.

No recurring structural Message Schema problem appeared that justifies changing accepted v0.1 in this pass. Verdict: MESSAGE_SCHEMA_V0_1_SUFFICIENT_FOR_PILOT.

## Pilot finding

This is a pilot finding only. The run tests Pictiq Message JSON as a target format, not a production translator and not a claim that LLMs understand Pictiq generally.

## RAG baseline

DEFERRED. The old TF-IDF/RAG prototype was not used in the primary condition and was not rebuilt for this pilot.
