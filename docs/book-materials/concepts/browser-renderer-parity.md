# Browser Renderer Parity as an Interoperability Boundary

> Status: book-material / architecture note
> Date: 2026-09-11
> Source event: Pictiq Composer Technical Spike 01 — Browser Renderer Parity

The Composer planning pass exposed a useful architectural distinction: Pictiq should not confuse an implementation language with the language protocol itself.

Python Renderer v0.1 is the accepted reference implementation, but Python source code is not the semantic source of truth. The source of truth is the combination of Message Schema, registries, compatibility metadata, Numeric Notation, Entity Symbols, canonical SVG assets, and the Renderer behavior contract.

The browser spike tested whether a second implementation could render the same canonical normalized Message JSON in a static GitHub Pages environment. The result was positive with guardrails: a browser renderer can be small and deterministic when it consumes generated canonical asset data and is tested against Python reference output. The browser path must not become a second place where vocabulary, compatibility, grammar, or semantic guessing lives.

This gives Pictiq a useful book-level story: a visual protocol becomes interoperable when its behavior can be conformed to by more than one runtime. The trade-off is clear. Sharing source code reduces drift but may limit deployment surfaces. Sharing canonical data plus behavioral parity allows more runtimes, but only if conformance tests are treated as part of the protocol infrastructure.

For Composer v0.1, the practical lesson is that preview rendering can stay static and browser-local, while normalization and validation remain explicit upstream responsibilities. The user-facing tool can be lightweight without weakening the protocol boundary.
