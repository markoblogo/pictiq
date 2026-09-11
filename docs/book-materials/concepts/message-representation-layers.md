# Message Representation Layers

> Status: book-material / architecture note  
> Source spec: [Pictiq Message Format v0.1](../../../spec/PICTIQ_MESSAGE_SCHEMA.md) and [Pictiq Shorthand v0.1](../../../spec/PICTIQ_SHORTHAND.md)  
> Rule: This note does not implement renderer, generator, Composer, browser translation, AI translation, vocabulary, grammar, icons, profiles, packs, or Entity Symbols.

## Maturation step

After Pictiq v1.1.0, the project distinguishes five layers that earlier examples often blurred:

1. **Language** — accepted Pictiq semantics, grammar, vocabulary, profiles, context packs, numeric notation, and Entity Symbols.
2. **Message representation** — the canonical JSON object that records an ordered set of typed Pictiq tokens.
3. **Authoring syntax** — optional human shorthand that normalizes into canonical JSON.
4. **Rendering** — deterministic transformation from canonical message plus render options into SVG, PNG, HTML, or other outputs.
5. **Translation** — upstream semantic decomposition from natural language, AI systems, or external inputs into Pictiq concepts.

The renderer does not translate. It renders an already specified Pictiq message.

## Why grouping and 2D semantics stay deferred

Pictiq already has evidence that grouping or spatial arrangement may matter later: Odyssey narrative fragments, poetry/visual-prosody ideas, UI/web navigation, and public-wayfinding examples all create pressure for richer structure. That pressure is real, but it is not yet accepted grammar.

Message Format v0.1 therefore keeps one frame as a flat ordered token sequence. This makes the first renderer/generator layer simpler, testable, and compatible with the current language. If future experiments prove that grouping or 2D semantic layout is necessary, that evidence can justify a later schema/language extension instead of being smuggled into v0.1.

## Book value

This is a useful chapter-level moment: Pictiq becomes less like a folder of icons and more like a protocol stack. The distinction lets books, tools, examples, and AI experiments share the same canonical message object while still keeping translation, rendering, and authoring separate.
