# Canonical icon fitting standard

`APPROVED SHAPE IS IMMUTABLE; PLACEMENT IS NOT.`

Human-approved artwork keeps its silhouette, proportions, topology, direction,
and components. Source-sheet coordinates, crop boundaries, presentation frames,
and export canvases are never canonical coordinates.

The mandatory import workflow is:

`APPROVED SKETCH → CANONICAL SVG`

1. Isolate the approved symbol and remove labels, frames, shadows, and
   background.
2. Calculate the true tight bounding box of visible symbol geometry.
3. Normalize its origin and preserve aspect ratio.
4. Fit proportionally into the canonical safe area and center the visible
   geometry horizontally and vertically.
5. Add the canonical frame, then validate bounds and clipping.
6. Review large, 64 px, and 24 px renders in the final framed tile.
7. Apply a small whole-symbol optical position or proportional-size correction when the final tile still looks unbalanced.
8. Obtain human visual acceptance.

The canonical tile is `32 × 32`. The established safe area is the inner
`24 × 24` box at `(4, 4)`. Imported artwork uses a conservative fitting box
of `22 × 22` at `(5, 5)`; a smaller result is expected when aspect ratio leaves
unused space. The outer rounded-square frame is presentation structure and is
never included in the artwork bounding box.

Geometric fitting is necessary but not sufficient. The final decision is made from
approved artwork inside the final framed tile: the artwork must have balanced
visual mass, breathing room, and perceived size alongside established Pictiq
icons. A mathematically centered bounding box is not visual acceptance.

The complete workflow is: approved artwork → geometry isolation → geometric
fitting → safe-area validation → final framed rendering → optical position
adjustment → optical size adjustment → human visual acceptance. Optical
correction is allowed only as a small whole-symbol translation or proportional
scale change; independent X/Y stretching is prohibited. The reason is recorded.

Validators are hard safety constraints, not final aesthetic acceptance. They
catch clipping, out-of-bounds geometry, Pages/canonical mismatches, and broken
transforms. `tools/validate_icon_fitting.py` remains the repeatable geometry
report; human review remains the acceptance source for imported artwork.

