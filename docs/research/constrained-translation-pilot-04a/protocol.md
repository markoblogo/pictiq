# Constrained Translation Pilot Stress Test 04A Protocol

> Status: executed pilot protocol
> Date: 2026-09-11
> Boundary: no translator implementation, no vocabulary change, no grammar change, no renderer change, no RAG primary condition.

## Research question

Can one modern LLM produce Pictiq Message JSON v0.1 directly from simple natural-language intents when given the Message Schema, current registries, compatibility notes, and minimal grammar guidance?

## Prerequisite

The pilot runs only after publication of Pictiq Message Format v0.1, Pictiq Shorthand v0.1, and Renderer v0.1. That prerequisite is satisfied by the earlier v1.1.1 publication.

## Corpus

The corpus contains 18 cases fixed before model output. Categories cover direct needs, composition, negation/evaluation, numeric notation, Entity Symbols, contextual polysemy, intentional omission, and boundary ambiguity.

Human targets are stored in [`human-targets.json`](human-targets.json). The full corpus with required, optional, invalid, and omittable slots is stored in [`corpus.json`](corpus.json).

## Primary condition

The tested condition is:

LLM + Pictiq Message Schema v0.1 + current ordinary registry + Entity Symbol registry + numeric notation registry + compatibility notes + minimal grammar prompt.

The condition excludes RAG, embeddings, TF-IDF, fuzzy matching, product UI, Composer, and any repair step before scoring.

## Model and structured output

Model metadata is stored in [`model-metadata.json`](model-metadata.json). The run used OpenAI Chat Completions structured output with `response_format: json_schema`, passing the repository schema in `strict=false` mode. Local validation is authoritative for schema shape, registry validity, and rendering.

The exact system prompt is stored in [`system-prompt.md`](system-prompt.md). Per-case user prompts used the fixed pattern: `Source intent: <case source> Return one Pictiq Message JSON object.`

## Validation and scoring

Every raw model output is archived under [`raw/`](raw/). Outputs were scored without repairing failed model messages.

For each output, the pilot records:

- Message Schema shape validity;
- registry validity after Renderer normalization;
- renderability through Renderer v0.1;
- semantic slot recovery;
- unjustified concepts;
- legacy ID use;
- true vocabulary-gap candidates;
- intentional omissions.

Only valid normalized messages are archived under [`normalized/`](normalized/) and rendered under [`rendered/`](rendered/). The QA sheet [`qa-sheet.html`](qa-sheet.html) uses actual Renderer SVG output only.

## Schema-change gate

If a recurring structural schema problem appeared, this pilot was required to stop and propose a schema change rather than silently continuing. The observed recurring issue was five responses copying the schema document `$id` into the generated message. This is classified as model-instruction/provider-mode friction, not a structural flaw in Pictiq Message Schema v0.1.

Verdict: `MESSAGE_SCHEMA_V0_1_SUFFICIENT_FOR_PILOT`.

## RAG baseline

The RAG/TF-IDF baseline is deferred. The old prototype was not used in the primary condition and was not rebuilt in this pass.
