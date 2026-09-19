# Imported icon clipping — root-cause repair

`action_combine` was traced from the supplied complete reference through the
canonical SVG, Pages copy, Browser Renderer asset, landing use, and legacy QA.
The foreground was complete in the source/vector/canonical path. The actual
landing defect was a **stale Pages copy**: `docs/lexicon/svg/action_combine.svg`
(and the corresponding LEARN and WRITE copies) did not match the canonical SVG
after the prior local transform change.

The legacy SVG QA rasterizer was independently invalid: its ImageMagick path
omitted the frame stroke. It is removed from acceptance evidence. This is not a
canonical clipping defect.

## Classification

| Asset | Classification | Evidence |
| --- | --- | --- |
| `action_combine` | `STALE_ASSET` | Canonical foreground complete; Pages asset was stale. |
| `action_learn` | `STALE_ASSET` | Same unsynchronized lexicon-copy path. |
| `action_write` | `STALE_ASSET` | Same unsynchronized lexicon-copy path. |
| GitHub | `NO_PROBLEM` | Landing asset was current; transform stack normalized. |
| English | `NO_PROBLEM` | Landing asset was current; transform stack normalized. |
| PDF | `NO_PROBLEM` | Landing asset was current; transform stack normalized. |
| Medium | `NO_PROBLEM` | Landing asset was current; transform stack normalized. |
| Substack | `NO_PROBLEM` | Landing asset was current; transform stack normalized. |

The existing `clipPath` continues to protect only the foreground inside the
canonical frame. Pixel-edge measurements for COMBINE retain positive space on
all sides, so no frame, CSS, or source cropping repair was required.

- [Large human QA](imported-icon-human-correction-qa.html)
- [A–G pipeline forensic](forensic/action-combine-pipeline-forensic.html)
- Run `python3 tools/make_landing_optical_qa.py` to regenerate the human sheet.
- Run `python3 tools/validate_imported_icon_geometry.py` for normalized-transform,
  clipping, safe-area, and exact Pages-mirror checks.
