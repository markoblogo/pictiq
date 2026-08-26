# Layouts

A **Content Profile** is the semantic selection of `primary` and `secondary` tiles. A **Layout** is a physical representation of that profile: shirt, wallet card, phone lockscreen, or another format.

Primary and secondary must not duplicate icons. Individual layouts may impose tile limits. Paris keeps its approved shirt composition intact; its `wallet_card` block records the explicit card-only exclusions required to fit the physical grids: `place_landmark_park`, `move_boat`, `need_food`, `qty_1`, `qty_2`, `qty_5`, and `qty_minus`.

Generate the Paris wallet card:

```bash
python3 tools/make_wallet_card.py --profile paris
```
