# Results-analysis method

## Evidence and scope

Five supplied consumer-product transcripts were reviewed: ChatGPT, Claude, Gemini, Mistral, and Microsoft Copilot. DeepSeek is excluded because no comparable usable run was supplied. No further model was queried.

The source DOCX files are retained unchanged in [evidence/source-docx](evidence/source-docx/). Analysis records what each transcript says; it does not infer hidden model versions, training data, or architecture.

## Analytical layers

1. **Visual recognition** records what a model says the visible glyph is before receiving the guide.
2. **Structure** records recovery of the four-turn question → answer → question → answer exchange and cross-turn referents.
3. **Blind semantics** compares stated meaning to the user-supplied intended dialogue.
4. **Guided production** distinguishes documented use, conservative omission, contextual approximation, and invention.
5. **Repair** evaluates proposals against the current repository, not against a model's claimed rules.

No aggregate score or model ranking is produced.

## Slot labels

`CORRECT`, `APPROXIMATE`, `INFERRED_FROM_CONTEXT`, `OMITTED`, `WRONG`, and `HALLUCINATED` retain their protocol meanings. `NOT_REACHED_DUE_TO_VISUAL_ERROR` is added when a wrong visual object prevents semantic evaluation. A slot label is an audit aid, not a general measure of a model.

## Current-state comparison

The analysis compares transcripts against the current repository at this pass. `spec/GRAMMAR.md` makes consecutive `qty_1`, `qty_2`, and `qty_5` tiles additive: `qty_1 + qty_2 = 3`; `qty_5 + qty_5 = 10`. `spec/NUMERIC_NOTATION.md` keeps exact written numeric notation separate. The current frozen 05A artifact intentionally avoids exact `3` and `6`, whereas the supplied evidence image does not. The Handbook v1.0 provided to systems did not make the additive quantity rule explicit.

## Evidence-provenance gate

The supplied result image differs materially from the frozen published 05A image. Findings about visual recognition, transaction structure, and guided protocol behavior remain useful. Findings about the frozen 05A's exact semantic slots and its intentional omissions are not attributable to that frozen artifact. A later replication must first use one byte-identified published PNG and record its hash.
