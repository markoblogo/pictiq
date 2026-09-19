# Pictiq Landing Translation v0.1

Status: **visible-text-free acceptance fix implemented locally; READY FOR HUMAN REVIEW**. Publication remains a
milestone candidate and is not promoted by implementation alone.

The landing now has a deterministic static mode switch:

- English: `/landing/`
- Pictiq: `/landing/?mode=pictiq`

The switch uses `URLSearchParams` and `history.replaceState`, so the Pictiq mode
is linkable and reloadable on static hosting. It preserves the approximate
scroll position during an in-page switch. The controls are real keyboard
buttons with visible focus and explicit `English mode` / `Pictiq mode` labels.

English content and layout remain the accepted baseline. Pictiq mode is now a
strict visual-language experiment: it exposes no natural-language UI text,
omits the Lexicon destination, and uses canonical SVGs, the accepted GitHub,
English, PDF, Medium, Substack, and author Entity Symbols. Composer uses
`action_write` and `action_combine`; no Composer Entity Symbol was created.

No vocabulary, Entity Symbol, pack, grammar, notation, Renderer, Composer, or
Message Schema changes were made. The current frozen counts remain **87 ordinary
primitives** and **16 Entity Symbols**.

## QA matrix

| Surface | EN | PICTIQ | Result |
|---|---|---|---|
| Desktop layout | accepted English baseline | compact semantic sections | structural checks pass; human visual review pending |
| Tablet / narrow desktop | responsive landing grid | responsive compact sections | CSS media rules present |
| Mobile | stacked accepted sections | stacked compact sections | CSS media rules present |
| Mode control | EN active | Pictiq glyph active | keyboard buttons, focus, labels pass |
| Linkability | `/landing/` | `?mode=pictiq` | deterministic static URL |
| Lexicon | visible and linked | omitted from navigation and content | intentional omission |
| Exact technical identifiers | visible fallback | PDF Entity Symbol; EPUB action omitted; no visible technical text | intentional omission |

## Visible-text-free decisions

- Pictiq mode contains no visible natural-language UI text. Accessibility labels,
  alt text, metadata, and semantic HTML remain available to assistive technology.
- The English switch uses the accepted English Entity Symbol in Pictiq mode; the
  visible `EN` abbreviation remains only in the accepted English baseline.
- The book cover remains an allowed external visual artifact even though its
  printed cover text is visible; it is not landing UI text.
- The numeric layer remains unchanged. `0` and `5` are implemented digits, while
  `1`, `2`, and `6` are not. `qty_1`, `qty_2`, and `qty_5` remain additive phrase
  quantities and do not encode exact year digits.

The analytical zero-training statuses and the full pressure log are recorded in
[`landing-translation-findings-2026-09.md`](../../book-materials/research/landing-translation-findings-2026-09.md).
