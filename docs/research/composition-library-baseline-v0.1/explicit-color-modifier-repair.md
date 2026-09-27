# Explicit Color Modifier Mechanism

**Status: REQUIRED / NOT IMPLEMENTED.** This is a separate repair dependency, not part of the Composition Library baseline pass.

Creator decision for the blocked hotel/color intent: `OBJECT + SEPARATE COLOR TILE`. The color tile is filled with the communicated color. The canonical object glyph remains unchanged; recoloring that glyph is not semantic color.

Current mismatch: protocol material proposes a parametric color sample but defines no accepted token or geometry; Message Schema has no color-tile token; Composer's `params.color` recolors an icon; Renderer renders that icon recoloring. The current system cannot author/render the accepted object-plus-color-tile semantics.

Later authorized repair must decide token/message representation, neutral tile geometry, arbitrary value vs controlled palette, modifier scope and ordering, association when several objects/colors occur, shorthand, accessibility/fallback, rendering, Composer authoring, validation, and machine-readable value. Do not assume ordinary `color_blue` vocabulary IDs are required. No color ID or implementation is included in this pass.
