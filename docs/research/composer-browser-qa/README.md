# S01.23 — Composer v0.1 real Chrome QA

2026-11-19, Europe/Paris. Clean starting HEAD:
`f89bfc62c2236200c8ad125cac3ac11fa243d8c0`.

```text
COMPOSER BROWSER QA: BLOCKED
DICTIONARY BROWSER QA: PASS / PRESERVED
DICTIONARY BASELINE: FROZEN / PRESERVED
PUBLIC RELEASE: NOT PERFORMED
```

## Scope and environment

Actual Google Chrome on macOS; HTTP URL `http://localhost:8000/docs/composer/`.
Repository-root Python HTTP server bound to 127.0.0.1:8000. Read the existing
Composer HTML/app, docs/README.md and Message Schema documentation before testing.
No app/source/data changes. This is tool QA, not creator semantic acceptance or
translation/comprehension evidence. Browser build number and physical-device
compatibility were not assessed.

## Completed browser checks

- UI/catalog load; search by canonical ID; updated comm_sound description includes
  oral/written/social-media human communication and human-produced sound, excluding
  natural/animal sound without a human source.
- A: palette assembly `comm_sound + qty_minus`; B: palette assembly
  `move_public + media_text + time + punct_question`. Both assembled and rendered
  correctly at all three actual viewport sizes. Preview data-id order equals
  Message token order. No Dictionary lookup/integration was assumed.
- Delete tile, Undo/Redo and delete-frame/reset were exercised. Profile switched
  to Embodied Core and back to Standalone; exported profile changed accordingly,
  contexts retained `universal-core`. Other parameter controls were not exhaustively
  tested. Alt+ArrowLeft moved the question before time; Undo restored the original
  order. No semantic data was changed.
- JSON and .pictiq import both restored the complete displayed B Message, including
  schema/pictiq/profile/contexts/frame/token order. These imports exist in v0.1;
  neither is classified NOT SUPPORTED. SVG import was not claimed or required.

| Actual CSS viewport | Document scrollWidth | Both examples / delete+Undo / preview |
| --- | --- | --- |
| 1280 × 900 | 1280 | PASS |
| 390 × 844 | 390 | PASS |
| 320 × 844 | 320 | PASS |

The initial browser-wide viewport control did not resize the intended background
tab after an automation restart. Those duplicate desktop observations were not
accepted as mobile evidence. Mobile was repeated with tab-scoped Chrome device
metrics and actual clientWidth/height checked. Both overrides were cleared at end.
[observations.json](observations.json) retains only the actual desktop and mobile
measurements. All six recorded compositions report `No validation errors.`

At mobile widths, panels stack vertically; all add/delete/search/export actions
remain reachable through normal page scrolling, without overlapping panels.
At 320px, workspace tiles wrap (3 + 1 for B), preserving sequence; canonical
preview keeps all four signs in order. JSON/shorthand inspect blocks have bounded
local scrolling rather than widening the document. Desktop preview panel also
has local vertical scrolling to reach inspect/export. No important action was
observed hidden or unreachable. Console capture: **0 warnings, 0 errors**.

## Export evidence and exact limitation

The UI implements Download JSON, Download .pictiq, Download SVG and Copy JSON /
Copy .pictiq. All three Download buttons were invoked. Download completion could
**not** be verified: the download-event waiter timed out; native Save As dialogs
were encountered, a save attempt did not yield a confirmed file, and outstanding
QA save dialogs were cancelled. No downloaded file is claimed as verified.
An unrelated PDF Save As dialog initially blocked browser control; the owner
completed it before testing continued. Their file/settings were not modified.
Copy JSON also exposed a prompt fallback during the interrupted sequence; clipboard
copy completion is not claimed. This is an environment/automation limitation,
not proof that Composer's download or clipboard implementation is defective.

Available inspect outputs were instead preserved with explicit names:

- [inspected-message.json](inspected-message.json): actual displayed Canonical JSON.
- [inspected-message.pictiq](inspected-message.pictiq): actual displayed shorthand.
- [preview.svg](preview.svg): serialized actual browser SVG preview, **not a
  verified Download SVG artifact**.

Existing `schema_errors` and `semantic_errors` accept the preserved Message.
Existing `parse_shorthand` produces a fully equal Message. The SVG tree (tags,
attributes, non-whitespace text and child order) equals the output of the existing
Python canonical `render_message` for that Message. No extra params or metadata
appeared. Both UI import round-trips preserved the same complete Message.
These checks prove inspect/preview consistency; they do not close the unverified
filesystem download path. Therefore overall QA remains **BLOCKED** pending a
verified save and inspection of all three Download artifacts. No new export
format or feature is requested.

## Defect and limitations

**CBQA-01 — Low: keyboard reordering hint omits Alt.** Tile accessible labels say
“Use arrow keys to move”; plain ArrowLeft did not change order. Alt+ArrowLeft
successfully reordered the selected tile, as the existing handler requires.
This is a misleading instruction, not a failure of the working Alt shortcut.
No fix was applied. No Critical/High functional defect was observed.

Downloads are supported but completion is NOT VERIFIED, not NOT SUPPORTED.
The earlier foreign dialog and native save/download-event limitations are not
assigned product-defect severity. No persistence across reload, drag-and-drop,
color editing, multiple-frame export or complete browser compatibility claim is
made from this bounded run.

## Screenshots and preservation

- [Desktop A](desktop-A.jpg).
- [Desktop B / inspect](viewport-1280.jpg).
- [Mobile 390 B](viewport-390.jpg).
- [Mobile 320 B](viewport-320.jpg).

All previously tracked repository files remain byte-identical, including Composer
source/generated data, Dictionary/freeze records, Lexicon, Renderer, canonical
assets, Corpus, creator exports and application records. Only this QA directory
is added. Existing Message/Renderer validation and local evidence links pass;
`git diff --check` passes. No Node simulation substituted for browser interaction.
No fixes, push, tag, release or Dictionary re-evaluation were performed.
