# Silhouette Inputs (Canonical PNG Sources)

This project uses a reproducible pipeline: **input silhouette PNG → vectorize (potrace) → fit into tile → validate**.
For icons built via silhouettes, the PNG in `inputs/silhouettes/` is the canonical source of truth.

## Canonical workflow
1. Create a black-on-white silhouette PNG (no halftones).
2. Save it as `inputs/silhouettes/<icon_id>.png`.
3. Generate the tile SVG:
   - `python3 tools/build_icon_from_silhouette.py --id <icon_id> --input inputs/silhouettes/<icon_id>.png --out icons/svg/<icon_id>.svg`
4. Validate:
   - `python3 tools/validate_svg.py`
   - `python3 tools/validate_lexicon.py`
5. Do not hand-edit `icons/svg/*.svg` for silhouette-based icons.
   Instead, adjust the PNG input and regenerate.

## Input requirements (strict)
- Canvas: **512×512 px** (recommended for stable tracing).
- Background: **white**. Foreground: **solid black** silhouette.
- No shadows, gradients, blur, opacity, or anti-aliasing effects intentionally added.
- Prefer simple, globally recognizable shapes.
- Avoid micro-details and thin bridges:
  - recommended minimum feature thickness: **≥ 2 px** at 512×512.
- The icon should be centered optically within the canvas.

## Naming rule (policy B)
- Each canonical silhouette input must be committed to git:
  - `inputs/silhouettes/<icon_id>.png`
- Keep drafts elsewhere; only approved inputs belong here.

## Punctuation icons from fonts (punct_*)
For `punct_exclaim` and `punct_question`, the silhouette is derived from a font glyph and then converted to curves before exporting to PNG.

- Font: **Helvetica Neue Bold**
- Typical working size in Affinity: **140** (on a 512×512 canvas)
- Canonical rule: final glyph size is set by **bounding box height ~75% of canvas**, and the glyph is **optically centered**.

Export as black-on-white PNG, then regenerate via the pipeline.

## Time icon (time)
The `time` icon is treated as a silhouette-based icon (not purely geometric):
- Use a simple clock face (ring + hands + small center hub).
- Avoid tick marks or extra detail.
- Adjust the silhouette in the PNG and regenerate if visual tuning is needed.
