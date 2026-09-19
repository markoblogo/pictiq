# Landing translation findings — 2026-09

> Status: human-reviewed reference translation implemented locally; pending visual and semantic acceptance. No publication status is promoted by this pass.

## Source and pressure

The first complete manual semantic pass over the accepted English landing established `ENGLISH_SOURCE_BASELINE_V0_1`. It tested the question: **Can Pictiq explain Pictiq?** The review found that many explanatory phrases are rhetorical, redundant, or recoverable from context. A Pictiq mode should therefore be substantially shorter than English mode and preserve communicative intent rather than source wording.

Three concepts created genuine Core pressure across the landing rather than a website-only gap:

- `action_combine` — combine, join, compose, assemble;
- `action_learn` — learn, study, practice, train;
- `action_write` — the action of creating written information, distinct from `media_text` as the text object or result.

They passed NEED-BEFORE-VOCABULARY after existing composition, context, polysemy, and omission were insufficient. No other landing pressure justified a new primitive in this pass. Machine/Computer, Browser, Workspace, Project, System, Symbol, New, Archive, Video, and IT/Server remain deferred. Protocol can be handled contextually through INFORMATION where appropriate; Experiment can use existing CHANGE/cycle semantics where useful.

## Communication principles

The normative protocol now records:

1. **MEANING-BEFORE-WORDING** — preserve communicative meaning, not every source word or rhetorical layer.
2. **PRIORITY-FIRST COMMUNICATION** — lead with the highest-priority actionable intent; add background only when needed.
3. **FUNCTIONAL SUFFICIENCY** — stop when the receiver has enough meaning to respond or act appropriately.

Their compact relationship is: `Meaning before wording. Priority before background. Sufficiency before completeness.` These principles connect to the existing semantic-compression states. `INTENTIONAL_OMISSION` can preserve functional sufficiency and is not automatically `LOSSY`; `LOSSY` marks a meaningful missing distinction, while `GAP` marks a currently inadequate representational capacity.

Practical examples retained for future writing:

- `TOILET + punct_question` can be enough to get directions; apology, travel history, and politeness need not be encoded first.
- Start with `NEED + WATER`. Add identity, quantity, payment, reason, or other context only if the receiver asks or the task requires it.

This is progressive practical communication, not a claim that literary translation should discard narrative structure. Literary and poetic translation remains a separate boundary research track. In an Odyssey-like narrative, source order may remain relevant; in a live help request, `NEED WATER` may be the right first message.

Shorter goal-first messages may reduce decoding burden for a receiver with no prior Pictiq training. That is a design hypothesis, not human evidence.

## Deferred hypotheses and candidates

The short/long/high/low arrow notation idea remains a `DEFERRED NOTATION HYPOTHESIS`; current landing work can use `SMALL + COMMUNICATION` for short messages. Entity-symbol pressure was observed for Composer, GitHub, English/England, PDF, EPUB, Medium, and Substack. These are candidates for a dedicated Entity Symbol pass, not additions here.

The landing translation/deployment remains `PUBLICATION MILESTONE CANDIDATE`, with the possible angle **Can a Visual Language Explain Itself?** Rendering is substantive and linkable, but READY remains a human-review decision.

## Implemented translation pressure log

| English source | Semantic intent | Pictiq representation | Context / omission / fallback | Compression | Outcome | Zero-training observation | Vocabulary pressure | Final decision |
|---|---|---|---|---|---|---|---|---|
| Hero meta and headline | small visual communication | `qual_good + media_image + comm_speak + action_combine`; `rel_lesser + media_image + comm_speak` | Rhetorical “when words are too much” omitted | compressed | short identity and purpose | likely transparent with context | none | implemented |
| Hero description | visual concepts combine into useful messages | `media_image + comm_speak + action_combine` | machines/systems/protocol omitted | compressed | functional explanation | context-dependent | none | implemented |
| About | small by design | Pictiq mark + `rel_lesser` | Explanatory paragraphs omitted | intentional omission | concise principle | context-dependent | none | implemented |
| Zero-training claim | begin with minimal prior learning | compact text fallback | No canonical zero rendering added; no claim of proven comprehension | text fallback | avoids overclaim | unclear | `0 + action_learn` pressure candidate | omitted from visible Pictiq mode |
| Book | visual information for short communication | text fallback + PDF Entity Symbol | EPUB remains text fallback; exact URLs retained | compressed | preserves useful download actions | context-dependent | none | implemented |
| Composer | write/combine Pictiq messages | `action_write` + Pictiq mark; `action_combine` action | browser/workspace/vocabulary omitted | compressed | direct authoring path | context-dependent | none | implemented |
| Lexicon | English reference destination | omitted from Pictiq navigation and page | English mode retains full Lexicon | intentional omission | keeps Pictiq mode short | learned convention likely required | none | implemented |
| Publications | public notes and project writing | `action_write + comm_speak`; Medium/Substack Entity Symbols | full article titles compressed; links and labels retained | compressed | publication destinations remain actionable | context-dependent | none | implemented |
| Footer | identity, author, year, essential links | logo + textual fallback | legal/static note omitted | intentional omission | keeps metadata precise | likely transparent | none | implemented |
