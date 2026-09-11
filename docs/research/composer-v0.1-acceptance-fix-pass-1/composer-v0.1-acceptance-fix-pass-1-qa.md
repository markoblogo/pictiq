# Composer v0.1 Human Acceptance Fix Pass 1 QA

> Status: acceptance-fix evidence. Actual Composer implementation loaded from `docs/composer/index.html` in installed Google Chrome headless. Safari WebDriver was not enabled on this host, so Safari is not claimed as directly automated.

## Root cause fixed

The failed desktop acceptance screenshot was caused by the Composer using three equal-weight panels with unbounded panel height and separate `max-height:42vh` limits on individual palette lists. On wider desktop layouts the profile/context/search controls and headings could consume the visible part of the palette while the actual tile lists still existed lower in the DOM. In complex imported messages, the desktop grid also stretched all panels to match the tallest workspace content, which could push the preview SVG far below the first visible screen.

The fix makes desktop panels bounded to the viewport, gives the palette one predictable scrollable vocabulary area, and makes the workspace the widest visual center. Import and export/code controls are collapsible so they do not compete with the message or preview.

## Visual QA screenshots

- `pass1-desktop-empty.png` - initial empty Composer, desktop width.
- `pass1-desktop-water-question.png` - desktop WATER + QUESTION built through palette search.
- `pass1-narrow-water-question.png` - narrow WATER + QUESTION built through palette search.
- `pass1-desktop-road-odyssey-complex.png` - desktop complex Road fixture imported through Composer import.

## Viewport and scenario checks

| Scenario | Viewport | First palette tile visible | Visible ordinary cards | Tokens | Frames | Preview SVG | Horizontal overflow |
| --- | ---: | --- | ---: | ---: | ---: | --- | --- |
| empty-640 | 640x900 | yes | 8 | 0 | 1 | empty | no |
| empty-768 | 768x900 | yes | 8 | 0 | 1 | empty | no |
| empty-1024 | 1024x900 | yes | 8 | 0 | 1 | empty | no |
| empty-1280 | 1280x900 | yes | 8 | 0 | 1 | empty | no |
| empty-1440 | 1440x900 | yes | 8 | 0 | 1 | empty | no |
| desktop-water-question | 1440x900 | yes | 1 | 2 | 1 | yes | no |
| narrow-water-question | 640x900 | yes | 1 | 2 | 1 | yes | no |
| desktop-home | 1440x900 | yes | 1 | 1 | 1 | yes | no |
| search-water | 1440x900 | yes | 4 | 1 | 1 | yes | no |
| entity-poseidon | 1440x900 | n/a | 0 | 2 | 1 | yes | no |
| number-50 | 1440x900 | yes | 8 | 1 | 1 | yes | no |
| multi-frame | 1440x900 | yes | 1 | 2 | 2 | yes | no |
| road-fixture | 1440x900 | yes | 8 | 7 | 4 | yes | no |
| odyssey-fixture | 1440x900 | n/a | 0 | 10 | 4 | yes | no |

## Human-facing labels

Profile and context controls now show human-facing labels while retaining repository IDs as secondary text/tooltips:

- `standalone-core-v0.1` -> Standalone
- `city-paris-v0.1` -> Paris
- `road-wayfinding-v0.1` -> Road / Wayfinding
- `universal-core` -> Core
- `universal-v1` -> Universal
- `narrative` -> Narrative
- `odyssey` -> Odyssey

## Scope boundary

No vocabulary, grammar, Message Schema, Shorthand grammar, canonical SVG geometry, Entity Registry, Numeric Notation, Profiles, or Context Pack semantics changed. This pass changes Composer UI presentation/layout only and records QA artifacts.
