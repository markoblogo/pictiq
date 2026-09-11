# Composer v0.1 Human Acceptance Fix Pass 3 QA

> Status: acceptance-fix evidence / ready for human review.
> Date: 2026-09-11
> Runtime: current `docs/` site served over local HTTP at `http://127.0.0.1:57118/composer/`; not `file://`. Automated interaction trace used installed Google Chrome headless. Pass 2 had already been manually reviewed in Safari over local HTTP; this pass keeps the implementation to standard browser drag/drop and keyboard events intended for Safari compatibility, but direct Safari drag automation is not claimed.

## Scope

Fix Pass 3 converts the Message Workspace from persistent structure-editor controls to direct manipulation. It keeps the canonical v0.1 model unchanged: ordered document frames with ordered flat tokens. It does not introduce freeform canvas layout, grouping, arbitrary X/Y positioning, new vocabulary, new icons, schema changes, shorthand grammar changes, Renderer changes, Entity Registry changes, Numeric Notation changes, or Context Pack semantic changes.

## Interaction model

- The Workspace header now keeps only `Message workspace`.
- A compact `×` in the upper-right of each Frame deletes that Frame.
- A compact bottom `+` appends a new final Frame and selects it.
- Drag a Frame header vertically to reorder Frames.
- Drag a tile left/right within a Frame or into another Frame.
- Hover/focus/selection reveals the tile `×` overlay in the upper-left corner.
- The last Frame cannot leave the editable state invalid; deleting it leaves one empty Frame.

## Keyboard behavior

- Focus a Workspace tile, then use `Alt+ArrowLeft` / `Alt+ArrowRight` to move it within its Frame.
- Focus a Workspace tile, then use `Delete` or `Backspace` to delete it.
- Focus a Frame header, then use `Alt+ArrowUp` / `Alt+ArrowDown` to reorder it.
- Focus a Frame header, then use `Delete` or `Backspace` to delete it.
- Focus the bottom `+` and press/activate it to add a Frame.

This is a functional non-pointer path, not a completed accessibility certification. Touch drag is not claimed for v0.1; on no-hover devices selected/focused tiles expose the delete overlay, and click-to-add from Palette remains available.

## Automated interaction trace

| Scenario | Canonical Frame order | Preview | Persistent workspace toolbar | Persistent tile action row | Visible tile label | Overflow |
| --- | --- | --- | --- | --- | --- | --- |
| `three-tiles-initial` | `need_water punct_question logic_yes` | true | false | 0 | false | false |
| `three-tiles-drag-1-to-3` | `punct_question logic_yes need_water` | true | false | 0 | false | false |
| `three-tiles-drag-back` | `need_water punct_question logic_yes` | true | false | 0 | false | false |
| `cross-frame-b-between-c-d` | `need_water / logic_yes punct_question logic_no` | true | false | 0 | false | false |
| `tile-hover-delete` | `need_water punct_question` | true | false | 0 | false | false |
| `tile-delete` | `punct_question` | true | false | 0 | false | false |
| `tile-delete-undo` | `need_water punct_question` | true | false | 0 | false | false |
| `frame-3-above-frame-1` | `logic_yes / need_water / punct_question` | true | false | 0 | false | false |
| `frame-delete-middle` | `logic_yes / punct_question` | true | false | 0 | false | false |
| `frame-delete-undo` | `logic_yes / need_water / punct_question` | true | false | 0 | false | false |
| `frame-add-bottom-plus` | `logic_yes / need_water / punct_question` | true | false | 0 | false | false |
| `color-token-cross-frame-preserved` | `nature_cloud` | true | false | 0 | false | false |
| `entity-cross-frame-preserved` | `entity:poseidon@odyssey` | true | false | 0 | false | false |
| `number-cross-frame-preserved` | `50 / entity:poseidon@odyssey` | true | false | 0 | false | false |
| `keyboard-token-move-left` | `punct_question need_water` | true | false | 0 | false | false |
| `keyboard-token-delete` | `need_water` | true | false | 0 | false | false |
| `keyboard-frame-move-up` | `logic_yes / need_water` | true | false | 0 | false | false |
| `keyboard-frame-delete` | `need_water` | true | false | 0 | false | false |
| `keyboard-add-frame` | `need_water` | true | false | 0 | false | false |
| `narrow-direct-manipulation` | `need_water punct_question / logic_yes` | true | false | 0 | false | false |

## Preservation checks

- COLOR-bearing token moved across Frames and retained `params.color` in canonical JSON.
- Odyssey Entity Symbol moved across Frames and retained its `entity:...@odyssey` identity.
- Number `50` moved across Frames and retained numeric-token identity.
- Undo restored a deleted tile and a deleted Frame in the automated trace.
- Browser Renderer preview existed after every structural operation.

## Screenshots

- [`pass3-two-frame-clean-workspace.png`](pass3-two-frame-clean-workspace.png)
- [`pass3-tile-hover-delete.png`](pass3-tile-hover-delete.png)
- [`pass3-three-frame-bottom-plus.png`](pass3-three-frame-bottom-plus.png)
- [`pass3-selected-tile-inspector.png`](pass3-selected-tile-inspector.png)
- [`pass3-cross-frame-after-move.png`](pass3-cross-frame-after-move.png)
- [`pass3-narrow-direct-manipulation.png`](pass3-narrow-direct-manipulation.png)

## Non-results

This pass does not claim Stress Test 04B completion, broad usability validation, mobile/touch drag support, or final accessibility compliance. It is a focused implementation and QA pass for the accepted direct-manipulation Workspace issue.
