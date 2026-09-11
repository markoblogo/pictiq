# Composer v0.1 Human Acceptance Fix Pass 2 QA

> Status: acceptance-fix evidence / ready for human review.
> Date: 2026-09-11
> Runtime: current `docs/` site served over local HTTP at `http://127.0.0.1:57118/composer/`; not `file://`. Automated screenshots used installed Google Chrome headless. Safari remains the manual browser under test on the same local HTTP server.

## Scope

Fix Pass 2 addresses three accepted Composer v0.1 UX issues only: compact Message Workspace tiles, a compact single-row desktop header, and a visual COLOR control. It does not change Pictiq vocabulary, grammar, Message Schema, Shorthand grammar, Renderer semantics, Browser Renderer semantics, canonical SVG geometry, Entity Symbols, Numeric Notation, Profiles, or Context Pack semantics.

## Evidence summary

| Scenario | Viewport | Frames | Tokens | Header | Token tile | Labels hidden | Preview SVG | Horizontal overflow |
| --- | --- | ---: | ---: | --- | --- | --- | --- | --- |
| `desktop-water-question` | 1440×900 | 1 | 2 | 46 px | 62×100 px | true | true | false |
| `desktop-five-token-frame` | 1440×900 | 1 | 5 | 46 px | 62×100 px | true | true | false |
| `desktop-three-frame-message` | 1440×900 | 3 | 6 | 46 px | 62×100 px | true | true | false |
| `color-control-expanded` | 1440×900 | 1 | 1 | 46 px | 62×100 px | true | true | false |
| `narrow-water-question` | 640×900 | 1 | 2 | 84 px | 62×100 px | true | true | false |

## COLOR control

| Step | Canonical JSON result |
| --- | --- |
| `color-control-expanded` | contains no token-local color param; default black is restored |
| `color-swatch-blue` | contains `params.color = #1976D2` from quick swatch |
| `color-picker-green` | contains `params.color = #388E3C` from native color picker |
| `color-hex-custom` | contains `params.color = #3A6F8F` from HEX input |
| `color-reset-default` | contains no token-local color param; default black is restored |

Feature-detected EyeDropper button was available in the automated Chrome runtime. The Composer only shows that control when the browser exposes `window.EyeDropper`.

The swatches are authoring shortcuts only. They do not create semantic color vocabulary and do not alter canonical icon identity.

## Screenshots

- [`pass2-desktop-water-question.png`](pass2-desktop-water-question.png)
- [`pass2-desktop-five-token-frame.png`](pass2-desktop-five-token-frame.png)
- [`pass2-desktop-three-frame-message.png`](pass2-desktop-three-frame-message.png)
- [`pass2-color-control-expanded.png`](pass2-color-control-expanded.png)
- [`pass2-color-changed-preview.png`](pass2-color-changed-preview.png)
- [`pass2-narrow-responsive-composer.png`](pass2-narrow-responsive-composer.png)

## Non-results

This pass does not claim completed usability validation, Safari-specific behavior, accessibility compliance, or Stress Test 04B completion. It is a focused implementation and QA pass for the accepted human-review issues before the next authoring test.
