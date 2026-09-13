# Pictiq Vocabulary Governance

This document records vocabulary-addition governance for Pictiq. It complements the canonical lexicon, vocabulary classification, grammar, and protocol specifications; it does not add icons by itself.

## NEED-BEFORE-VOCABULARY

**Status:** accepted project rule.

Pictiq does not add a new primitive or contextual icon merely because a concept is common, useful, conventional, or theoretically desirable.

A new symbol is added only when a concrete current use case creates a direct need that cannot be expressed clearly enough with the existing vocabulary, composition, context, polysemy, or intentional omission.

Normal decision sequence:

1. Existing primitive.
2. Composition.
3. Context.
4. Polysemy.
5. Intentional omission.
6. Only then consider a new symbol.

A plausible future use is not sufficient justification by itself.

## Why this rule exists

Pictiq deliberately values a small vocabulary, discoverability, zero-training entry, combinatorial reuse, semantic economy, and resistance to dictionary growth. Adding every useful concept would gradually turn Pictiq into a pictogram dictionary rather than a minimal compositional visual protocol.

## DEFERRED_UNTIL_NEEDED

`DEFERRED_UNTIL_NEEDED` is a research/planning status, not a vocabulary classification. It means:

- a concept may plausibly be useful later;
- a possible visual treatment may already be known;
- no current direct need justifies implementation;
- no canonical ID or icon should be created yet.

Deferred candidates belong in research and planning notes only. They must not affect canonical vocabulary counts.

## Current example: Web/UI semantic reconciliation

The Web/UI Stress Test initially made several software concepts look like vocabulary gaps. Human semantic reconciliation found that many were acceptable through current context, composition, or polysemy. One domain pressure produced a real Core addition: `action_change`, because EDIT exposed a broader CHANGE / TRANSFORM / MODIFY primitive. Other plausible concepts, including archive, IT/system, and video, remain deferred until a concrete current need appears.
