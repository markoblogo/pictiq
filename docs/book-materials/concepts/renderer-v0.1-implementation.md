# Renderer v0.1 Implementation Note

> Status: book-material / implementation record
> Date: 2026-09-11
> Scope: Renderer v0.1 only; no Composer, AI translation, generator API, GUI, grammar change, vocabulary expansion, icon redraw, profile change, pack change, Entity Symbol expansion, tag, release, or push implied.

Renderer v0.1 is the first executable layer after Pictiq Message Format v0.1 and Pictiq Shorthand v0.1. It proves that Pictiq can be represented as a small protocol stack instead of a loose icon folder:

1. the accepted language layer defines vocabulary, grammar, profiles, context packs, numeric notation, and Entity Symbols;
2. the message layer records explicit tokens in canonical JSON;
3. shorthand gives humans a compact authoring syntax;
4. the renderer converts the explicit message into deterministic SVG output.

The implementation pressure confirmed the earlier architectural split. Rendering can be useful only if it refuses to guess: unknown IDs, unsupported numbers, unsupported parameters, grouping syntax, ambiguous entity aliases, and invalid profiles/contexts must produce diagnostics instead of invented output.

Legacy compatibility belongs in normalization, not in new messages. `need_bar` can normalize to `drink_alcohol`, and `place_hotel` can normalize to `place_home`, because those migrations are recorded. `move_boat` remains deferred to the vocabulary audit outcome and is not silently migrated to `move_watercraft`.

The renderer also confirms that exact numeric notation and pragmatic `qty_*` quantities coexist. A token value of `50` renders through numeric notation; `qty_1`, `qty_2`, `qty_5`, `qty_plus`, and `qty_minus` remain communication quantity primitives.

This stage creates a practical foundation for later Generator API, Composer, website/editor, education examples, and book figures, while preserving the rule that translation and semantic choice happen upstream of rendering.
