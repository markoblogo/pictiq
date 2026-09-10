# Pictiq Visual Consistency Audit — 2026-09

Status: **CLOSED** after human visual review. No SVG redesign was performed.

## Final decision

Visual age, detail level, or stylistic variation alone is not sufficient reason to redraw a working contextual icon. Old-generation style alone is not a redesign trigger.

> Visual consistency is a constraint, not a goal in itself. A working icon should be redesigned only when there is a concrete semantic, recognizability, technical, size-survival, or architectural problem.

## QA sheets

- Main 12-candidate sheet: [`../../build/qa/pictiq-visual-consistency-audit-2026-09.png`](../../build/qa/pictiq-visual-consistency-audit-2026-09.png)
- All-83 observation grid: [`../../build/qa/pictiq-all-83-observation-grid-2026-09.png`](../../build/qa/pictiq-all-83-observation-grid-2026-09.png)

## Final candidate decisions

| ID | Decision | Reason categories | Final reason |
| --- | --- | --- | --- |
| `money_card` | KEEP AS IS | VISUAL_WEIGHT, EXCESSIVE_DETAIL, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `money_atm_bank` | KEEP AS IS | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `place_landmark_park` | KEEP AS IS | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `move_public` | KEEP AS IS | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `paris_arc_de_triomphe` | KEEP AS IS | OLD_GENERATION_STYLE, VISUAL_WEIGHT, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `paris_notre_dame` | KEEP AS IS | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `paris_sacre_coeur` | KEEP AS IS | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `paris_moulin_windmill` | KEEP AS IS | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `place_catacombs` | KEEP AS IS | EXCESSIVE_DETAIL, VISUAL_WEIGHT, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `place_theme_park` | KEEP AS IS | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `place_art_gallery` | KEEP AS IS | OUTLINE_VS_FILLED, EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Current artwork is usable; no concrete semantic or technical failure justifies redesign. |
| `place_fashion_shopping` | DO NOT REDRAW / DEPRECATE | OLD_GENERATION_STYLE, SEMANTIC_VISUAL_MISMATCH, COMPOSITIONALLY_OBSOLETE, POOR_24PX_SURVIVAL | Concept is compositionally obsolete; prefer `place_shop + item_clothing`. |

## Confirmation

- No SVG geometry changed.
- No additional visual-redesign candidates were added.
- `place_fashion_shopping` should not be redesigned by default because the concept is compositionally obsolete.
