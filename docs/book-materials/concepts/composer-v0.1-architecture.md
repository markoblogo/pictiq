# Composer v0.1 Architecture Note

> Status: book-material / implementation-planning note
> Source spec: [`../../../spec/PICTIQ_COMPOSER.md`](../../../spec/PICTIQ_COMPOSER.md)
> Rule: no Composer implementation is created by this note.

Composer v0.1 is the next engineering milestone after Message Format v0.1, Shorthand v0.1, Renderer v0.1, and Stress Test 04A. Its purpose is not translation. Its purpose is human authoring: can a person make a valid Pictiq message without editing JSON, shorthand, SVG, or repository files?

The architecture boundary matters:

HUMAN INTENT -> HUMAN SELECTION -> MESSAGE JSON -> NORMALIZER / VALIDATOR -> RENDERER -> SVG.

Composer should make Pictiq usable while preserving explicit human choice. It may search, filter, and recommend concepts by profile/context, but it must not infer intent or silently rewrite semantic selections.

## Why Composer comes before Translator

Stress Test 04A showed that Message Schema v0.1 was sufficient for a small LLM-to-message pilot, but the failures were generation and representation failures. Composer tests the other side first: whether humans can author valid messages intentionally. That keeps future evidence clean:

- human authoring failures;
- AI generation failures;
- Renderer/Message failures;
- vocabulary or grammar gaps.

## Key implementation risk

The current public site is static GitHub Pages with browser JavaScript. Renderer v0.1 is Python. Public Composer cannot directly run the Python Renderer in the normal static browser environment.

The future implementation must make an explicit renderer decision. A server/API renderer keeps one implementation but adds hosting. A browser-compatible renderer adapter fits static Pages but must be parity-tested against Python Renderer. Pyodide may preserve Python logic but is likely heavy. The spec therefore treats renderer parity as a hard acceptance gate.

## UX principle

Composer should be compact and work-like: palette, workspace, preview. It should not be a marketing landing page. It should expose labels and glosses first, IDs second, and diagnostics in human language.

## Book value

Composer is the moment Pictiq stops being only a documented protocol plus rendered examples and becomes a usable writing surface. It will also create the conditions for Human Authoring Stress Test 04B and later human/AI signaling comparisons.

## Implementation candidate

Composer v0.1 now has a static implementation candidate at [`../../composer/`](../../composer/). It keeps the accepted architecture: human palette selection edits canonical Message v0.1 state, validation/normalization happens before rendering, and preview/export SVG comes from the Browser Renderer. The implementation uses generated repository data instead of a manually duplicated frontend vocabulary.

This candidate prepares Stress Test 04B but does not run it. Automated tests cover core state transitions, imports, exports, diagnostics, shorthand serialization, Renderer preview/export semantics, generated-data freshness, and Browser/Python Renderer parity.
