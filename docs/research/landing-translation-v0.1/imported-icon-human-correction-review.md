# Imported SVG coordinate repair

Direct browser raster measurement found a coordinate bug in the prior imported
SVG correction. The prior optical transform was flattened into a single matrix,
but its incorrect displacement and scaling were preserved. For
`action_combine`, direct 1024-pixel semantic-foreground measurement was
`(152,156,793,788)`, centre `(472.5,472)`, instead of the intended safe-area
centre `(512,512)`.

The repair derives one replacement matrix per asset from the measured rendered
foreground: preserve the approved silhouette and current proportional scale,
then solve the matrix translation so the final foreground centre equals the
canonical safe-area centre. `action_combine` also uses a 20-unit maximum extent
(90.9% of the 22-unit fitting width). No new outer offset or transform chain was
added.

The earlier Pages-copy mismatch for COMBINE / LEARN / WRITE was a separate
stale-asset fault and remains protected by exact canonical-to-Pages validation.
Source extraction, canonical viewBox, frame clip, and landing CSS did not lose
approved geometry.

- [Coordinate audit and accepted-reference comparison](imported-svg-coordinate-audit.md)
- [Raw 1024-pixel action_combine diagnostic](forensic/action-combine-raw-coordinate-diagnostic.svg)
- [Large human QA](imported-icon-human-correction-qa.html)
- Run `python3 tools/validate_imported_icon_geometry.py` for centre, containment,
  normalized-transform, and exact Pages-mirror regression checks.
