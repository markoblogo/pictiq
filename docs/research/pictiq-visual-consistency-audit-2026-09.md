# Pictiq Visual Consistency Audit — 2026-09

Status: read-only visual diagnosis for human review. This note and the QA sheets do not redesign icons, change SVG geometry, change IDs, change semantics, change classification, migrate IDs, deprecate code, push, tag, or release anything.

## Source of truth

The 12 candidates were extracted from the current Architecture & Vocabulary Audit:

- [`pictiq-architecture-vocabulary-audit-2026-09.md`](pictiq-architecture-vocabulary-audit-2026-09.md)
- [`pictiq-architecture-vocabulary-audit-2026-09.json`](pictiq-architecture-vocabulary-audit-2026-09.json)

The Markdown and JSON contain the same 12 candidate IDs; their presentation order differs.

## QA sheets

- Main 12-candidate sheet: `build/qa/pictiq-visual-consistency-audit-2026-09.png`
- Optional all-83 observation grid: `build/qa/pictiq-all-83-observation-grid-2026-09.png`

Both sheets use only current repository SVGs rendered from `icons/svg/`.

## Candidate table

| ID | Semantic field | Classification | Concern categories | Reason |
| --- | --- | --- | --- | --- |
| `money_card` | card payment | CONTEXTUAL | VISUAL_WEIGHT, EXCESSIVE_DETAIL, POOR_24PX_SURVIVAL | Overlapping card/cash forms may be dense at 24 px; contextual payment icon should be retested. |
| `money_atm_bank` | ATM / bank | CONTEXTUAL | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | ATM details/keypad create small-size density; contextual finance/travel icon should be retested. |
| `place_landmark_park` | park / landmark | CONTEXTUAL | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Dense older travel/city artwork; 24 px readability and visual mass should be retested. |
| `move_public` | public transport | CONTEXTUAL | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Vehicle detail is dense at 24 px; transport contextual icon should be retested. |
| `paris_arc_de_triomphe` | Arc de Triomphe | CONTEXTUAL | OLD_GENERATION_STYLE, VISUAL_WEIGHT, POOR_24PX_SURVIVAL | Landmark form may need mass/readability retest in the Paris context pack. |
| `paris_notre_dame` | Notre-Dame cathedral | CONTEXTUAL | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Detailed landmark silhouette; Paris contextual icon should be retested at small size. |
| `paris_sacre_coeur` | Sacre-Coeur basilica | CONTEXTUAL | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Detailed landmark silhouette; Paris contextual icon should be retested at small size. |
| `paris_moulin_windmill` | Paris windmill cabaret landmark | CONTEXTUAL | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Detailed landmark silhouette; Paris contextual icon should be retested at small size. |
| `place_catacombs` | catacombs | CONTEXTUAL | EXCESSIVE_DETAIL, VISUAL_WEIGHT, POOR_24PX_SURVIVAL | Skull cluster is dense at small size; contextual Paris asset should be retested before broad reuse. |
| `place_theme_park` | theme park | CONTEXTUAL | EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Detailed amusement-park/city artwork; 24 px readability and older generation style should be retested. |
| `place_art_gallery` | art gallery | CONTEXTUAL | OUTLINE_VS_FILLED, EXCESSIVE_DETAIL, OLD_GENERATION_STYLE, POOR_24PX_SURVIVAL | Detailed/outlined exhibition-room artwork; visual mass and small-size clarity should be retested. |
| `place_fashion_shopping` | fashion shopping | CONTEXTUAL | OLD_GENERATION_STYLE, SEMANTIC_VISUAL_MISMATCH, COMPOSITIONALLY_OBSOLETE, POOR_24PX_SURVIVAL | Obsolete compound plus visually inconsistent older artwork; do not redesign until future visual-redesign pass decides whether legacy asset remains needed. |

## Special cases

- `place_fashion_shopping` is also `DEPRECATE_COMPOSABLE`; the sheet marks it as “DO NOT REDESIGN BY DEFAULT — candidate for deprecation.”
- `need_bar` and `place_hotel` are semantic-migration concepts in the architecture audit, but they are not among the current 12 visual-redesign candidates. No migration or artwork change is performed here.

## Human decision field

The main sheet leaves the human decision blank for each candidate: KEEP AS IS, MINOR NORMALIZATION, REDRAW, DO NOT REDRAW / DEPRECATE, or OTHER. These fields must be filled by human review before any visual-redesign task begins.

## Confirmation

- No SVG geometry changed.
- No vocabulary, classification, profile, pack, numeric notation, or entity registry changed.
- The audit does not add new redesign candidates automatically.
