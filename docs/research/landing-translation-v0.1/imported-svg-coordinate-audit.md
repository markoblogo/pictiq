# Imported SVG coordinate audit — 2026-09-19

**Method.** Each canonical SVG was directly rendered by the browser at exactly
`1024 × 1024`; the frame was excluded only for the semantic-foreground pixel
measurement. The canonical `viewBox` is `0 0 32 32` for every listed icon. The
intended safe-area centre is therefore `(512, 512)` at this raster size. The
safe fitting area is `704 × 704` pixels (`22 × 22` viewBox units).

The earlier forensic note incorrectly treated ImageMagick's tight-trim offset
as a final right edge. `159` was a trim **left offset**, while the same output's
trim width was `666`; it was not a bbox ending at `199`. That coordinate-system
mix invalidated the old conclusion and is superseded by this direct-raster
record.

| Icon | Foreground bbox at 1024 `(L,T,R,B)` | Centre | X/Y error | Occupancy of fitting area | Root cause | Changed |
| --- | --- | --- | --- | --- | --- | --- |
| `action_combine` | `192,197,832,827` | `512,512` | `0,0` | `91.1% × 89.6%` | Incorrect preserved optical matrix | Yes |
| `action_learn` | `244,197,780,826` | `512,511.5` | `0,-0.5` | `76.3% × 89.5%` | Incorrect preserved optical matrix | Yes |
| `action_write` | `238,188,786,836` | `512,512` | `0,0` | `78.0% × 92.2%` | Incorrect preserved optical matrix | Yes |
| GitHub | `257,221,767,802` | `512,511.5` | `0,-0.5` | `72.6% × 82.7%` | Incorrect preserved optical matrix | Yes |
| English | `244,311,780,714` | `512,512.5` | `0,+0.5` | `76.3% × 57.4%` | Incorrect preserved optical matrix | Yes |
| PDF | `294,227,731,797` | `512.5,512` | `+0.5,0` | `62.2% × 81.1%` | Incorrect preserved optical matrix | Yes |
| Medium | `191,322,832,702` | `511.5,512` | `-0.5,0` | `91.2% × 54.1%` | Incorrect preserved optical matrix | Yes |
| Substack | `327,279,697,745` | `512,512` | `0,0` | `52.7% × 66.3%` | Incorrect preserved optical matrix | Yes |

## Accepted-reference comparison

| Reference | Foreground bbox | Centre | Occupancy of fitting area |
| --- | --- | --- | --- |
| question | `314,218,707,804` | `510.5,511` | `56.0% × 83.4%` |
| water | `228,193,786,828` | `507,510.5` | `79.4% × 90.3%` |
| speak | `160,193,863,829` | `511.5,511` | `100.0% × 90.5%` |
| yes | `228,261,862,839` | `545,550` | `90.2% × 82.2%` |

Reference occupancy varies with silhouette aspect ratio. The imported set now
falls within the same established range and is geometrically centred. `yes` is
an intentionally asymmetric check mark, so its bbox centre is diagnostic, not
a centring target for symmetric imported glyphs.

## Direct diagnostic

[Raw 1024-pixel action_combine diagnostic](forensic/action-combine-raw-coordinate-diagnostic.svg)
contains only the canonical frame and foreground, exact centre lines, and the
measured foreground bbox. It has no HTML preview container, CSS object-fit, or
landing styling.
