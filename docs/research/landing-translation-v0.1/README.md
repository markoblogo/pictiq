# Pictiq Landing Translation v0.1

Status: **implemented locally; READY FOR HUMAN REVIEW**. Publication remains a
milestone candidate and is not promoted by implementation alone.

The landing now has a deterministic static mode switch:

- English: `/landing/`
- Pictiq: `/landing/?mode=pictiq`

The switch uses `URLSearchParams` and `history.replaceState`, so the Pictiq mode
is linkable and reloadable on static hosting. It preserves the approximate
scroll position during an in-page switch. The controls are real keyboard
buttons with visible focus and explicit `English mode` / `Pictiq mode` labels.

English content and layout remain the accepted baseline. Pictiq mode is shorter
by design, uses canonical SVG assets, omits the Lexicon destination, keeps exact
URLs and technical fallback text, and uses the accepted GitHub, PDF, Medium, and
Substack Entity Symbols. Composer uses `action_write` and `action_combine`; no
Composer Entity Symbol was created.

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
| Exact technical identifiers | visible fallback | PDF/EPUB/version/URL text retained where useful | text fallback |

The analytical zero-training statuses and the full pressure log are recorded in
[`landing-translation-findings-2026-09.md`](../../book-materials/research/landing-translation-findings-2026-09.md).
