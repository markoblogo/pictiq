# Semantic Boundary Corpus Plan

> Status: future research corpus plan
> Source: [Pictiq AI Experiments Harvest 2026-09](pictiq-ai-experiments-harvest-2026-09.md)
> Boundary: research planning only; no corpus is executed here.

## Purpose

The Semantic Boundary corpus tests where a source message fails as it moves through:

SOURCE -> semantic decomposition -> Pictiq selection/composition -> reconstruction.

This is not simply an LLM failure test. It should distinguish source-language ambiguity, translator failure, Pictiq structural limitation, vocabulary gap, and intentional omission.

## Candidate pressure types

- idiom;
- metaphor;
- sarcasm;
- double negation;
- indirect request;
- euphemism;
- deliberate ambiguity;
- poetry.

## Evaluation labels

Use labels compatible with prior Pictiq stress-test work:

- `SURVIVED`
- `COMPRESSED`
- `INTENTIONAL_OMISSION`
- `LOSSY`
- `GAP`
- `UNTRANSLATABLE_OR_STRUCTURALLY_INCOMPATIBLE`
- `TRANSLATOR_FAILURE`
- `SOURCE_AMBIGUITY`

## Timing

Some small cases can be written as Message JSON immediately after Renderer v0.1, but the main corpus belongs after Composer because manual construction would bias the sample and slow iteration.

## Relation to poetry

This plan extends [Pictiq Poetry / Visual Prosody](pictiq-poetry-stress-test-plan.md). Poetry is a high-value boundary case because rhythm, sound, connotation, line structure, and ambiguity cannot be assumed to survive semantic compression.
