# Standalone Batch B reference QA

## Question

Can the supplied approved reference sheet be transferred into canonical Pictiq tiles without changing the approved morphology?

## Setup

The reference image was cropped into black/white 512 px silhouettes, traced with the existing silhouette pipeline, and placed in fresh canonical 32×32 frames. Each result was rendered at canonical review scale, 64 px, and 24 px, then placed in representative compositions. COLOR was kept as a separate value-bearing prototype.

## Result

Twelve non-parametric candidates were implemented and accepted after human visual review: `eye_look`, `item_clothing`, `comm_speak`, `comm_sound`, `media_text`, `media_image`, `nature_sun`, `state_light`, `food_produce`, `food_bakery`, `rel_greater`, and `rel_lesser`. The approved sheet’s `>` / `<` morphology is retained as canonical relational operators in v1.0.2.

## Failures / limitations

COLOR is not a lexical icon and is demonstrated separately at red, blue, yellow, dark grey-green, and very light values. Grayscale preserves luminance differences where present, not hue.

## Evidence

Source: `Зображення Codex 9 вер. 2026 р., 18_04_51.png` supplied on 2026-09-09. Review sheets: `build/qa/standalone-batch-b.png`, `build/qa/standalone-batch-b-compositions.png`, and `build/qa/color-param/grayscale-comparison.png`.

## Follow-up

Human visual acceptance is complete. Release v1.0.2 includes the accepted Batch B IDs; later work keeps COLOR as a separate parametric mechanism and entity symbols as a separate registry mechanism.
