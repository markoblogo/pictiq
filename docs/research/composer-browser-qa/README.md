# Composer v0.1 QA — S01.23 / S01.24 / S01.25

**Current status (S01.26): Composer downloads PASS; Composer browser QA PASS; CBQA-01 FIXED.**
Owner-downloaded files independently verified below; the S01.23/S01.24 blocked
observations remain historical evidence, not current export status.

2026-11-19, Europe/Paris. S01.23 clean starting HEAD:
`f89bfc62c2236200c8ad125cac3ac11fa243d8c0`.

```text
COMPOSER BROWSER QA: PASS
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


## S01.24 — downloadable exports follow-up (2026-11-19)

Starting clean HEAD: `70139f9da4ff315b433effe3a1ab1996ff81d225`.
Actual Chrome over HTTP, `http://localhost:8000/docs/composer/`.
Rebuilt B from palette buttons in the exact order:
`move_public + media_text + time + punct_question`.
Displayed Message has schema 0.1, pictiq 1.1, profile
`standalone-core-v0.1`, contexts `["universal-core"]`, one frame and four icon
tokens without additional params. Actual preview data-ids match that order.

The earlier BLOCKED was not proof of a broken export button: it combined a
background-tab/native-save interruption and lack of an inspectable saved file.
This follow-up activated the Composer tab in Chrome. Chrome displayed a
localhost multiple-file-download permission prompt, which was allowed for these
requested exports. Even after that permission, no downloadable artifact was
confirmed. The browser automation's download waiter timed out for JSON (15s),
.pictiq (5s) and SVG (5s). No Save As dialog subsequently appeared. Captured tab
console contained zero warnings/errors. This establishes the observable blocker,
not its deeper cause; it does not establish a Composer implementation failure.

A dedicated target directory was prepared outside the repository:
`/tmp/pictiq-s0124-exports`. It remained empty after the attempts. The runtime does
not support `Page.setDownloadBehavior` to direct files there; it requires its
`waitForEvent("download")` route, which did not supply a file. No download path
or protection was bypassed. No user Downloads files were edited or replaced.

| Button | Real file confirmed | Content / SHA-256 / downloaded-file round-trip |
| --- | --- | --- |
| Download JSON | NO — download event timed out | NOT AVAILABLE / NOT VERIFIED |
| Download .pictiq | NO — download event timed out | NOT AVAILABLE / NOT VERIFIED |
| Download SVG | NO — download event timed out | NOT AVAILABLE / NOT VERIFIED |

The earlier inspected JSON/shorthand/preview checks remain valid but are not
substituted for downloaded bytes. No hashes are invented and no downloaded-file
round-trip is claimed. This is neither a confirmed broken button nor a confirmed
successful download whose file merely cannot be inspected: completion itself
remains unconfirmed through the available browser interface.

Minimal independent check: in an ordinary foreground Chrome session, open the
same local HTTP Composer, build B, and use each Download button once. In Save As,
choose the temporary directory above and retain `pictiq-message.json`,
`pictiq-message.pictiq`, `pictiq-message.svg`. Once those actual files exist,
compute `shasum -a 256 /tmp/pictiq-s0124-exports/*`, run existing Message validation,
parse the downloaded shorthand and compare canonical Renderer SVG structure;
then paste the downloaded JSON and shorthand into the existing Import UI and
compare the full Message. This manual save is the only missing prerequisite;
no new Composer feature or code change is proposed.

Only this README is updated. Previous evidence and all previously tracked code,
data, frozen Dictionary records/manifests, SVGs and decisions are preserved.
`git diff --check` passes. CBQA-01 remains OPEN / LOW; it is not fixed here.

```text
COMPOSER DOWNLOADS: BLOCKED
COMPOSER BROWSER QA: BLOCKED
CBQA-01: OPEN / LOW
DICTIONARY BASELINE: FROZEN / PRESERVED
PUBLIC RELEASE: NOT PERFORMED
```


## S01.25 — owner-downloaded files independently validated (2026-11-19)

Technical verification started from clean HEAD
`972eec302900aa01bb9dd4627148dcecb6c4a980`. Owner confirms manual download from
ordinary Chrome; Codex independently read the actual saved bytes. No browser
automation, synthetic export or replacement file was used in this pass.
The superseded pictiq-export-qa directory was not used.

Exactly one Composer-named candidate per requested format was found in
`/Users/antonbiletskiy-volokh/Downloads`; unrelated files were not inspected.
Creation times below are Europe/Paris, 2026-11-19. Files were read without editing,
deleting, renaming or copying them into the repository.

| Actual file | Creation time | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `pictiq-message.json` | 18:22:34.075227 +01:00 | 478 | `8d33829db2fdc0fa78b5dd5f1511985d9a3eba73963dcec368df37dcae74ade2` |
| `pictiq-message.pictiq` | 18:22:38.547168 +01:00 | 98 | `9a633d98d0bbbbd2bfb0203221af48dd1fe95b3bd9c90e0db23de98e9ca5a788` |
| `pictiq-message.svg` | 18:22:40.805423 +01:00 | 12631 | `b296064c6a9dd5bbdc4df29b88c2c9eb5a554293d0f4f51cac7b1a54ca78b6f2` |

### Results

- **JSON PASS:** declared JSON Schema checked with Draft202012Validator, including
  validity of the schema itself; existing `schema_errors` / `semantic_errors`
  also pass. Exactly one frame and four `{type: icon, id: ...}` tokens, ordered
  `move_public + media_text + time + punct_question`. No params are present or
  added. `schema=0.1`, `pictiq=1.1`, `profile=standalone-core-v0.1`,
  `contexts=[universal-core]` are preserved by normalization and all round-trips.
- **.pictiq PASS:** existing Python `parse_shorthand` and `render_file` parse the
  actual downloaded shorthand; the complete Message equals downloaded JSON,
  including metadata and token order. Rendering both real files gives equal
  canonical SVG output.
- **SVG PASS:** valid XML with SVG namespace/root; four data-id groups in the
  expected order. Complete structural tree comparison (tags, attributes,
  meaningful text and ordered children) matches the existing canonical Renderer
  using its default RenderOptions, also used by Composer's export. For these
  particular files, SVG is additionally **byte-identical** to Python Renderer
  output (12,631 bytes). Byte identity is an observed stronger result, not a
  general requirement imposed on equivalent Composer SVGs. No external image,
  script, foreignObject or external resource reference; local fragment/url
  references are resolved against existing IDs.
- **Round-trip PASS:** existing Composer core `parseJsonText` and
  `parseShorthandText` import the actual downloaded text in the local Node runtime.
  JSON → `serializeShorthand(...).text` → shorthand parser → Message preserves
  the full Message; serialization is byte-identical to downloaded .pictiq.
  Downloaded .pictiq → Message → JSON → JSON importer also preserves the full
  Message. This is a technical importer/serializer check, not a new browser UI
  round-trip; the earlier actual-browser round-trips remain separately recorded.

### Remaining qualifications

Python Renderer emits `profile-mismatch` and `context-mismatch` warnings for
`move_public` outside the selected standalone-core-v0.1 / universal-core sets.
They are non-fatal applicability warnings, not a schema error or lost export
metadata. No profile/context was changed to suppress them. No new semantic or
translation approval follows from this check.

Manual saving by the owner closes the previous download-completion evidence gap;
it does not prove unattended browser automation downloads now work. Earlier
browser functionality checks plus independently validated real files support
bounded Composer browser QA **PASS**, with CBQA-01 still **OPEN / LOW**. No new
browser/device compatibility or untested Composer feature is claimed.

All three files' bytes and SHA-256 were rechecked after validation. Only this
README changes; Composer, generated data, Dictionary/freeze records, Lexicon,
Renderer, Messages, canonical SVG, Corpus and application records remain
byte-identical. `git diff --check` passes. No push, tag or release.

```text
COMPOSER DOWNLOADS: PASS
COMPOSER BROWSER QA: PASS
CBQA-01: OPEN / LOW
DICTIONARY BASELINE: FROZEN / PRESERVED
PUBLIC RELEASE: NOT PERFORMED
```


## S01.26 — CBQA-01 shortcut instruction fixed (2026-11-19)

Starting clean HEAD: `1624eaa7fcae7557802431772888cafbcb2be92d`.
Reconfirmed actual Chrome behavior before editing: focus/select a tile button;
plain ArrowLeft does not reorder, while Alt+Left/Right Arrow moves it within its
frame. On macOS Alt corresponds to Option. The existing handler is unchanged.

Only the tile-button accessible instruction in `docs/composer/app.mjs` changes:

- Before: `Drag to reorder. Use arrow keys to move, Delete to remove.`
- After: `Drag to reorder. With a keyboard, focus this tile and press Alt (Option on macOS) + Left/Right Arrow to move; Delete to remove.`

This corrects an accessible label, not a new visible control or new gesture.
The mobile instruction is conditional on having a keyboard; it does not promise
an on-screen Alt key or a new touch-reordering feature. Existing drag wording
and deletion behavior remain unchanged.

Actual browser regression used HTTP Composer at desktop 1280×900 and mobile
390×844. A cached old module persisted on localhost:8000, so the final verification
used fresh local origin `http://localhost:8001/docs/composer/`. The new accessible
label was read from actual rendered buttons before accepting the regression.
The temporary viewport and cache settings were restored after the check.

On the changed version, `comm_sound + qty_minus` becomes `qty_minus + comm_sound`
with Alt+Left; Alt+Right restores the original order. Canonical JSON, .pictiq
inspect/export text and SVG preview data-id order all match the moved sequence.
Deletion + Undo and an extra palette addition + Undo restore the original Message;
profile and contexts remain unchanged. No fresh filesystem download is claimed:
this tests the serialized export payload and preview; the independently validated
S01.25 real downloads remain separate evidence and are not overwritten.

At mobile width the new labels include “With a keyboard”; clientWidth and
scrollWidth both equal 390px. Captured browser console: zero warnings/errors.
No other Composer surface or Dictionary was changed.

Existing `tests.test_composer`: **2 tests PASS**. Existing generated-browser-assets
freshness validation passes; app.mjs is a hand-maintained source and requires no
regeneration. All generated assets remain byte-identical. The source diff is
exactly the one instruction replacement, with event handlers and export logic
unchanged. All other tracked files except this report are preserved.
`git diff --check` passes. Historical CBQA-01 OPEN / LOW statements above describe
the earlier passes; this follow-up closes that defect without rewriting evidence.

```text
CBQA-01: FIXED
COMPOSER BROWSER QA: PASS
DICTIONARY BROWSER QA: PASS / PRESERVED
DICTIONARY BASELINE: FROZEN / PRESERVED
PUBLIC RELEASE: NOT PERFORMED
```
