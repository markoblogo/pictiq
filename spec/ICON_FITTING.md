# Canonical icon fitting standard

Human-approved artwork keeps its silhouette, proportions, topology, direction,
and source-relative composition through canonicalization.

## Normative workflow for approved external artwork

1. Start with the **human-approved source**.
2. Isolate only the semantic foreground; remove labels, presentation frames,
   shadows, dividers, and mockup material.
3. Faithfully reconstruct/vectorize that foreground.
4. Fit it proportionally inside the canonical `0 0 32 32` Pictiq frame using
   the source foreground-to-frame relationship as the initial target.
5. Produce overlay and difference QA when extraction is uncertain.
6. Obtain human visual review and acceptance.
7. Canonicalize the accepted artwork, then synchronize Pages, renderer, and
   Composer artifacts.

Geometric centering, bounding boxes, and validators are hard-safety tools.
They can detect clipping, malformed SVG, unsafe extents, stale public copies,
or transform-stack regressions. They do not override a human-approved,
source-relative composition.

Repeated bbox centering, optical matrix compensation, and placement variants
built on an already-divergent vector are not substitutes for returning to the
approved source.

## Technical bounds

Canonical tiles use `viewBox="0 0 32 32"` and the shared rounded frame. The
hard safe area is `(4,4)` through `(28,28)`. A typical fitting area is
`(5,5)` through `(27,27)`, but it is guidance rather than a reason to alter an
accepted source-relative fit. Canonical foreground uses one normalized group
with, at most, one final transform.

`tools/validate_icon_fitting.py` and
`tools/validate_imported_icon_geometry.py` report geometry and enforce only
hard safety; human visual review remains the acceptance source.
