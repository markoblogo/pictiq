# Layouts

A **Content Profile** is the semantic selection of `primary` and `secondary` tiles. A **Layout** is a physical representation of that profile: shirt, wallet card, phone lockscreen, or another format.

Primary and secondary must not duplicate icons. Individual layouts may impose tile limits. Paris keeps its approved shirt composition intact; its `wallet_card` block records the explicit card-only exclusions required to fit the physical grids: `place_landmark_park`, `move_boat`, `need_food`, `qty_1`, `qty_2`, `qty_5`, and `qty_minus`.

An icon may appear only once within a content profile. Primary and secondary selections MUST NOT overlap.

Generate the Paris wallet card:

```bash
python3 tools/make_wallet_card.py --profile paris
```

Additional physical layouts: **Luggage Tag / Sticker** and **Phone Lock Screen**. Both read a profile; the layout script determines the form factor.

### Output layers

- Artwork — exact flat production graphic.
- Preview — schematic object with the exact artwork applied.
- Mockup — optional realistic presentation image.

Previews must consume generated artwork or canonical SVG assets. They must never redraw or reinterpret Pictiq icons. Future shirt previews use a black-outline T-shirt schematic; the approved Paris shirt assets remain unchanged.
