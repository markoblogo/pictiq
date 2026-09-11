# Composer v0.1 Human Authoring QA Checklist

> Status: human acceptance checklist / not a completed usability study
> Date: 2026-09-11
> Scope: Composer v0.1 implementation smoke QA before Stress Test 04B.

Open the static Composer at [`../../composer/`](../../composer/).

## Required reviewer actions

| # | Action | Expected result |
| --- | --- | --- |
| 1 | Create a basic message: add `need_water` and `punct_question`. | Workspace shows one frame; preview renders actual Browser Renderer SVG; JSON export contains two icon tokens. |
| 2 | Reorder and delete tokens. | Token order changes through explicit arrow controls; deleted token disappears from JSON/shorthand/SVG. |
| 3 | Create a second frame. | JSON contains ordered `frames`; preview stacks rows through Renderer output. |
| 4 | Insert number. | Number token exports as `{ "type": "number", "value": 50 }`; no ordinary `num_50` ID appears. |
| 5 | Change supported COLOR. | Selected icon token receives `params.color`; preview/export SVG comes from Browser Renderer. |
| 6 | Add Entity Symbol. | Entity appears as typed `entity` token and is not flattened into ordinary vocabulary. |
| 7 | Import valid JSON. | Composer normalizes/validates and loads editable state. |
| 8 | Import `.pictiq`. | Composer parses shorthand and loads editable state. |
| 9 | Import legacy shorthand `need_bar` / `place_hotel`. | Diagnostics show warnings; exported JSON uses `drink_alcohol` / `place_home`. |
| 10 | Export/copy JSON. | Output is canonical Message JSON only; no UI state. |
| 11 | Export/copy shorthand. | Output is deterministic `.pictiq`; round-trips through parser/normalizer. |
| 12 | Export SVG. | Downloaded SVG is the same Renderer output shown in preview. |
| 13 | Reproduce Road fixture. | `surface_wavy punct_exclaim`, `50`, and road context render without semantic invention. |
| 14 | Reproduce Odyssey fixture. | Odyssey Entity Symbols, `move_watercraft`, `surface_wavy`, and COLOR case render from canonical assets. |

## Non-results

This checklist does not claim usability success, accessibility compliance, cross-cultural comprehension, or Stress Test 04B completion. It is the acceptance gate for whether the implementation is ready for human authoring tests.


## Human Acceptance Fix Pass 1

First human acceptance failed before authoring because the desktop Composer palette did not present tiles immediately and the three-panel layout gave Palette, Workspace, and Preview equal visual weight. Fix Pass 1 keeps Composer v0.1 architecture unchanged while making the Message Workspace the visual center, bounding desktop panels to the viewport, making the vocabulary area predictably scrollable, moving import/export/code into compact disclosure controls, and showing human-facing labels for profiles/context packs while retaining canonical IDs.

QA artifacts: [`../../research/composer-v0.1-acceptance-fix-pass-1/composer-v0.1-acceptance-fix-pass-1-qa.md`](../../research/composer-v0.1-acceptance-fix-pass-1/composer-v0.1-acceptance-fix-pass-1-qa.md).

## Human Acceptance Fix Pass 2

Second human acceptance review found three UI issues after Pass 1: Message Workspace tokens still carried visible semantic labels that consumed composition space, the desktop header used too much vertical space, and COLOR editing was too text-field-oriented for ordinary authoring.

Fix Pass 2 keeps the Composer v0.1 architecture and language unchanged. Workspace tokens are now compact icon-first controls with reorder/delete actions and accessible labels/tooltips retained outside the visual surface. The desktop header is a compact single row when space allows, while narrow layouts can wrap and hide the subtitle. COLOR editing now offers quick swatches, a native browser color picker, feature-detected EyeDropper support, secondary HEX precision input, and a Default reset that removes token-local `params.color`.

QA artifacts: [`../../research/composer-v0.1-acceptance-fix-pass-2/composer-v0.1-acceptance-fix-pass-2-qa.md`](../../research/composer-v0.1-acceptance-fix-pass-2/composer-v0.1-acceptance-fix-pass-2-qa.md).

This pass still does not claim completed usability validation or Stress Test 04B completion.

## Human Acceptance Fix Pass 3

Third human acceptance review found one concentrated issue: persistent structural controls still consumed Workspace area and made Composer feel like a technical structure editor rather than a surface for arranging Pictiq symbols.

Fix Pass 3 changes Workspace interaction to direct manipulation while preserving the same canonical flat Message structure. The Workspace header no longer carries persistent Add/Clear/Delete controls. Frames can be dragged by their header, deleted through a small contextual `×`, and appended through a compact bottom `+`. Workspace tiles can be dragged within a Frame or across Frames, and their delete action is now a hover/focus/selection overlay instead of a permanent action row.

Keyboard fallbacks are documented for v0.1: focused tiles support `Alt+ArrowLeft` / `Alt+ArrowRight` and Delete/Backspace; focused Frame headers support `Alt+ArrowUp` / `Alt+ArrowDown` and Delete/Backspace. This preserves a functional non-pointer path without adding persistent visual arrow controls.

QA artifacts: [`../../research/composer-v0.1-acceptance-fix-pass-3/composer-v0.1-acceptance-fix-pass-3-qa.md`](../../research/composer-v0.1-acceptance-fix-pass-3/composer-v0.1-acceptance-fix-pass-3-qa.md).

This pass still does not claim completed usability validation, mobile/touch drag support, or Stress Test 04B completion.
