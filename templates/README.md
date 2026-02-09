# Templates

## tile-template.svg

Canonical working template for creating Pictiq lexicon icons.

How to use:
1. Duplicate `templates/tile-template.svg` into `icons/svg/{id}.svg`
2. Open the copy in your editor (Inkscape recommended)
3. Draw or paste the pictogram into the `content` layer
4. Keep the `frame` layer unchanged (geometry + stroke)
5. Keep artwork inside the safe area (enable the hidden `guides` group if needed)

Authoring tips:
- Prefer `fill="currentColor"` and/or `stroke="currentColor"` so black/white variants render correctly.
- Keep shapes simple and readable at small sizes.

