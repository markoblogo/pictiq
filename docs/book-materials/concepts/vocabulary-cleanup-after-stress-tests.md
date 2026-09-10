# Vocabulary cleanup after stress tests

## Starting question

What happens after a young visual language discovers that several useful canonical icons came from early travel scenarios rather than from a clean architectural model?

## Findings

The Architecture & Vocabulary Audit shows that usefulness does not equal Core membership. Pictiq can preserve practical canonical icons while moving them into context packs, semantic migrations, or legacy contextual layers.

Key examples:

- `need_bar` is a semantic migration: the useful concept remains, but its accepted primary field is ALCOHOL / ALCOHOLIC DRINK rather than BAR.
- `place_hotel` is a semantic migration: the useful concept remains, but its accepted primary field is HOME / SHELTER / SLEEPING PLACE / BUILDING.
- `place_fashion_shopping` is deprecate-composable: `place_shop + item_clothing` expresses the useful meaning better than a dedicated compound.
- `move_watercraft` is the preferred broad water-transport primitive, while `move_boat` remains a legacy contextual subtype until a compatibility audit.
- The audit produced one clear new primitive: `food_meat`, a broad Core food-category gap. It did not add other food categories for symmetry.

## Why it matters

Cleanup is part of language development, not evidence that earlier work failed. Early travel bias supplied real use cases; later stress tests made broader abstractions visible and clarified where complexity belongs.

## Future use

Use this as book material for the chapter on growth control: a protocol can expand without bloating Core when it distinguishes Core, Standalone Core, context packs, semantic migration, deprecate-composable compounds, and legacy contextual vocabulary.
