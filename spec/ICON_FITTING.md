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
6. Review large, 64 px, and 24 px renders before human acceptance.

The canonical tile is `32 × 32`. The established safe area is the inner
`24 × 24` box at `(4, 4)`. Imported artwork uses a conservative fitting box
of `22 × 22` at `(5, 5)`; a smaller result is expected when aspect ratio leaves
unused space. The outer rounded-square frame is presentation structure and is
never included in the artwork bounding box.

Geometric centering is the default. Optical correction is allowed only when a
mathematically centered symbol is visibly unbalanced, the adjustment is small,
and the reason is recorded. Proportional scaling is mandatory; independent X/Y
stretching is prohibited.

`tools/validate_icon_fitting.py` measures rendered visible geometry and fails
when it clips, exceeds the inner safe area, or is materially off-center. It is
also the repeatable report used for imported artwork, so future fitting does not
depend on ad-hoc offsets.

