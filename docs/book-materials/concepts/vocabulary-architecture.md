# Vocabulary architecture after v1.0.2

## Starting question

How can Pictiq grow beyond the first accepted icon batches without letting “canonical” become a synonym for “Core”?

## Decision / outcome

Pictiq now separates five layers: canonical registry, Core vocabulary, Standalone Core, context packs/profiles, and entity registry. A tile can be accepted and canonical while still being contextual or specialized. Entity symbols remain scoped visual proper names and do not increase the ordinary Core count. The post-Odyssey audit also accepted `food_meat` as a broad Core food-category gap, without adding narrower meat taxa for symmetry.

Two principles capture the decision:

- **Canonical does not mean Core.**
- **Complexity belongs to the context that requires it, not to Core.**

## Why it matters

The early project used “Core” in filenames and prose for what later became the broader canonical registry. That was workable during the first release, but the accepted standalone batches, Paris-specific symbols, nightlife items, machine-interface symbols, and entity-symbol pilot make the distinction necessary. Without it, every accepted icon would silently inflate Core and make the protocol look less minimal than it is.

## Source evidence

The normative source is [Vocabulary Classification](../../../spec/VOCABULARY_CLASSIFICATION.md), backed by [`lexicon/vocabulary-classification.json`](../../../lexicon/vocabulary-classification.json). Phrase behavior is governed by [Grammar](../../../spec/GRAMMAR.md), which keeps bare adjacency contextual and avoids importing natural-language clause structure into Pictiq.

## Possible future book use

Use this as a short architecture chapter: growth does not require making the language bloated if the system distinguishes universal primitives, standalone needs, context-specific vocabulary, mechanisms, and named-entity symbols.

The reconciliation pass clarified semantic migration, deprecate-composable compounds, and legacy contextual vocabulary as separate outcomes. `need_bar` and `place_hotel` are migrations, `place_fashion_shopping` is composable deprecation, and `move_boat` is legacy contextual under the accepted `move_watercraft` hierarchy.
