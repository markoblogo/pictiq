# Pictiq Agent Retrieval Stress Test — planning note

> **Status:** `PLANNED / NOT RUN`. No model has been run and no result is claimed.

## Question

Can an unfamiliar AI reliably retrieve canonical Pictiq primitives, exact compositions, canonical assets, context, and evidence without inventing IDs or glyphs?

## Future comparison

- **A — Current repository discovery:** the participant receives the repository and the same fixed tasks.
- **B — Structured machine access:** the participant receives one future official machine-entry point. This arm cannot run until that layer exists.

Use the same model/configuration where practical, task wording, time/tool constraints, repository revision, and evidence packet. Freeze prompts, task fixtures, expected source references, and scoring rules before execution. Record model/tool/version and exact access conditions.

## Task classes

1. Find a primitive by intent/query; return exact canonical ID, meaning, status, and SVG reference.
2. Find an existing exact composition; return Message JSON and its source.
3. Select or distinguish EMBODIED vs STANDALONE and surface-specific records using supplied context.
4. Resolve Message token IDs and retrieve canonical assets; validate/render through existing contracts.
5. Report known ambiguity/failure and evidence; do not claim unsupported coverage.
6. For an absent match, return honest `GAP`/uncertainty rather than inventing an ID or glyph.

## Measures and limits

Potential measures: correct primitive/composition/asset retrieval; correct mode/surface/context match; valid exact Message retrieval; evidence/failure use; invented IDs/glyphs; wrong/deprecated asset; false coverage; honest GAP; observable steps/tool calls/time. Score each task against frozen references. Report omissions and uncertainty; do not collapse unlike evidence into an aggregate “understands Pictiq” claim.

This evaluates retrieval and source-grounded handling only. It does not test human comprehension, validate the protocol, establish agent superiority, or authorize vocabulary changes. No ranking or run occurs in this planning pass.
