# Canonical icon fitting standard — 2026-09

This record establishes the permanent import/fitting rule in
[`spec/ICON_FITTING.md`](../../../spec/ICON_FITTING.md) and repairs placement for
`action_combine`, `action_learn`, and `action_write`.

The approved silhouettes were preserved. The source-sheet/crop coordinates had
been reused as canonical placement, leaving the visible compositions too small,
off-center, or partially clipped. Each icon now uses a deterministic wrapper
transform around the existing path geometry. No path was redrawn or regenerated.

The established canonical safe area is `(4,4)` to `(28,28)`; imported artwork is
fitted into `(5,5)` to `(27,27)` with proportional scale and geometric centering.
The outer frame is excluded from the visible-geometry bbox.

Run:

```text
python3 tools/validate_icon_fitting.py
```

The tool reports visible bbox, X/Y center deltas, edge clearances, safe-area
bounds, and clipping status. The visual before/after evidence is
[`qa-sheet.html`](qa-sheet.html).
