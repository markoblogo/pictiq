# Constrained Translation Pilot Stress Test 04A

> Status: executed machine-facing pilot
> Date: 2026-09-11
> Primary artifact: [`../../research/constrained-translation-pilot-04a/README.md`](../../research/constrained-translation-pilot-04a/README.md)

## Question

Can a modern LLM produce valid Pictiq Message JSON v0.1 directly from simple natural-language intents after being given the accepted Message Schema, current registries, semantic metadata, and minimal grammar guidance?

## Result

The pilot ran 18 prewritten corpus cases with one OpenAI `gpt-5.1-2025-11-13` repeat. It used structured JSON output in non-strict schema mode, then applied local schema, registry, profile/context, and Renderer v0.1 gates. No output was repaired before scoring.

Key result: raw model messages contained all 32 required semantic slots, but only 13 of 18 outputs were schema-valid, registry-valid, and renderable. Five failures came from the model copying the schema document `$id` into the generated message. Seven cases added unjustified concepts. No legacy IDs were generated and no true vocabulary gap was found.

## Architecture finding

Pictiq Message Schema v0.1 is sufficient for this pilot. The main pressure is not a schema redesign; it is generator discipline, validation, and possible repair/retry behavior in a future Translator layer.

This preserves the architecture split introduced in v1.1.1:

1. language and vocabulary;
2. canonical JSON message representation;
3. shorthand authoring;
4. deterministic rendering;
5. future translation/generation.

## Book value

This is useful book material because it shows a concrete difference between a visual protocol and an AI translator. A stable symbolic message format can be a good target even when a model sometimes produces invalid or over-specific messages. Failures become evidence about translation and generator design rather than evidence against the core protocol.

## Boundary

No vocabulary, grammar, icon, renderer, profile, pack, Entity Symbol, tag, release, product UI, or RAG implementation changed in this experiment.

## Evidence

- [Pilot report](../../research/constrained-translation-pilot-04a/README.md)
- [Protocol](../../research/constrained-translation-pilot-04a/protocol.md)
- [Machine-readable results](../../research/constrained-translation-pilot-04a/constrained-translation-pilot-04a.json)
- [Human targets](../../research/constrained-translation-pilot-04a/human-targets.json)
- [Renderer QA sheet](../../research/constrained-translation-pilot-04a/qa-sheet.html)
