# Pictiq Signaling Game Plan

> Status: future experiment plan
> Source: [Pictiq AI Experiments Harvest 2026-09](pictiq-ai-experiments-harvest-2026-09.md)
> Rule: do not run this experiment from this plan; rebuild all corpora from the current registry and Message Schema before execution.

## Research question

Can two independent AI agents coordinate when their communication channel is restricted to valid Pictiq Messages?

## Roles

- **Sender** receives a private scenario.
- **Receiver** receives only the allowed Pictiq channel output and reconstructs meaning or chooses an action.
- **Judge/Evaluator** knows the scenario and scores the result against predefined semantic slots.

## Two channels

### Symbolic channel

Receiver receives canonical Pictiq Message JSON or validated token IDs. This tests Pictiq as an interpretable symbolic machine protocol.

### Visual channel

Receiver sees only Renderer-produced Pictiq visual output. This tests Pictiq as a shared human/machine visual language.

These are separate conditions. A model may do well on symbolic IDs and fail on visual interpretation, or the reverse may expose useful icon-recognition behavior.

## Control conditions

Start with:

- Pictiq-only channel;
- natural-language channel.

Potential later controls:

- constrained but non-Pictiq symbolic baseline;
- emergent/convention-building mode.

Do not include emergent mode in the first pilot unless the baseline task is already stable.

## Corpus design

Do not reuse the source-document scenario cards directly. They reflect an older 52-icon state and old IDs.

Build separate corpora for separate questions:

- protocol-comprehension corpus: scenarios expressible with existing Pictiq;
- vocabulary-coverage corpus: scenarios intentionally containing missing concepts.

Do not mix these in one score.

Future categories:

- one-concept messages;
- negation;
- quantity;
- location;
- need/action;
- multi-frame narrative;
- Entity Symbol use;
- clarification dialogue.

## Metrics

Use semantic-slot evaluation as the primary metric:

- recovered-slot accuracy;
- task success;
- message length;
- number of Pictiq tokens;
- validation failures;
- grammar/profile/context violations;
- clarification requests;
- error categories;
- cross-model robustness.

Literal reconstructed sentence equality is not the primary metric. Pictiq intentionally compresses natural-language distinctions.

## Model-pairing rule

Use different Sender and Receiver model families in at least some trials. Same-model self-play can hide protocol failures behind shared model priors.

## First pilot candidate

A tiny post-Renderer symbolic pilot can use 8-12 current-registry scenarios, with one Sender pass, one Receiver pass, and one Judge pass. The output should be a transcript and metric table, not a product claim.
