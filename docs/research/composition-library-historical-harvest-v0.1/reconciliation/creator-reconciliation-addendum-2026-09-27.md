# Creator Reconciliation Addendum — 2026-09-27

This is a subsequent creator decision record for the first reconciliation pass. It supplements, and does not rewrite, the byte-preserved [original creator export](creator-export-2026-09-27.json) or the initial [review report](creator-review-2026-09-27.md). It is bound to Harvest v0.1 snapshot `8fae507`.

## Record decisions

| Harvest ID | Historical composition and disposition | Creator replacement / note |
|---|---|---|
| `clh-v01-0008` — Less noise, please. | `comm_sound + qty_minus + comm_speak + logic_yes` — `SUPERSEDED / HISTORICAL EVIDENCE`; unnecessarily verbose. | `comm_sound + qty_minus` (`CREATOR_RECONCILIATION`). SOUND + LESS is functionally sufficient; the final two tiles over-explain. |
| `clh-v01-0010` — A beautiful blue hotel near the old city center. | `place_home + rel_here + qual_good + media_image` — `REJECTED / SUPERSEDED`. Using a recolored referenced-object glyph as semantic color conflates rendering style and meaning. | Creator intent: `HOTEL + BLUE + GOOD`, with “near the old city center” intentionally omitted. **No valid current Message replacement yet:** no explicit color tile mechanism exists. `COLOR_AS_RENDER_STYLE` is rejected; `COLOR_AS_EXPLICIT_TILE` is the creator decision and needs a separate system repair. Do not invent a color ID. |
| `clh-v01-0012` — This place is a battlefield. | `place_home + action_conflict` — `REJECTED / SUPERSEDED`; `place_home` supplies a false/more-specific referent (HOME), while the source is HERE / THIS PLACE. | `rel_here + action_conflict` (`CREATOR_RECONCILIATION`): approximately HERE + CONFLICT / conflict here under relevant context. Translator lesson: preserve deixis or return `GAP`; do not fill generic LOCATION with a specific `place_*` primitive unless the source supplies it. |
| `clh-v01-0070` — Loading / processing. | `time` — `REJECTED / SUPERSEDED`; TIME expresses waiting or a consequence, not the central PROCESS / CHANGE. | `action_change` (`CREATOR_RECONCILIATION`; current canonical ID for human-readable “change”). `action_change + time` remains a distinct possible expression such as “processing / please wait” or “the process is taking time”; it is **not** the automatic replacement. |

The original export remains unchanged with SHA-256 `455588e54a561e162d4b8ffdad38ad1b0f59612ccb3fafb889cc6e8ba41b40bc`. The structured form of these later decisions is in [creator-reconciliation-addendum-2026-09-27.json](creator-reconciliation-addendum-2026-09-27.json).

## Color audit: existing behavior and repair requirement

The current protocol describes COLOR as a **proposed parametric mechanism**: a standalone color sample is conceptually a neutral shape filled with the requested value, but canonical token, geometry, syntax, implementation, and acceptance are explicitly undefined. Grammar has no color composition rule. Message Schema v0.1 does not accept a `type: color` tile. It does accept `params.color` on an icon token; Composer exposes a color picker for that token and writes the parameter; Renderer applies it to the referenced glyph. That is actual token recoloring, not a separate semantic color sample following the object.

Therefore current Composer / Message Schema / Renderer cannot author and render the creator’s desired `OBJECT + COLOR` tile sequence. Record this as a separate repair requirement: review and specify an explicit parametric color tile and align protocol, schema, shorthand, validation, Renderer, and Composer in a separately authorized pass. No part of that implementation is included here; no color ID is proposed or added.

## Dictionary / Corpus architecture clarification

The Composition Library umbrella has two distinct future layers:

- **Lexicon:** canonical individual primitives.
- **Composition Dictionary:** future public, dictionary-like reusable concepts, compositional words, short phrases, and compact practical expressions.
- **Composition Corpus:** broader internal evidence-bearing record of known use, including dictionary candidates, long narrative/discourse, experiments, historical forms, production examples, rejected variants, and failures.

Semantic acceptance does not imply public Dictionary eligibility. Add the separate proposed `PUBLIC_DICTIONARY_ELIGIBILITY` values `YES`, `CORPUS_ONLY`, and `REVIEW`; do not overload creator `ACCEPT` / `REJECT` or lifecycle. Eligibility is semantic/reusability-based rather than token/frame-count-based. A whole accepted Odyssey multi-frame narrative record remains `ACCEPT` as Pictiq evidence and is Corpus-only; do not treat those prior ACCEPT decisions as mistakes or automatically split narrative records. Sub-composition extraction remains a later human-reviewed task. Uncertain records should remain `REVIEW` rather than be batch-classified.

The future Translator should retrieve reusable Dictionary solutions first, then consult Corpus records as broader evidence and context. Both layers must expose authority and status. A future public Library UI should primarily show the Dictionary, not dump the whole Corpus.

## Scope and stage

This addendum records decisions and architecture only. It creates no accepted Composition Dictionary or Composition Corpus baseline, does not classify every candidate’s Dictionary eligibility, and does not start the Practical Coverage Corpus. It does not change Lexicon, Grammar, Protocol, Numeric Notation, canonical assets, Message Schema, Composer, Renderer, public UI, or any product behavior. The frozen Harvest and paused Stress Test 07.1 remain preserved.

**Current stage:** `Composition Library Human Reconciliation v0.1` — first decision layer complete; creator addendum captured. **Next:** `Human Reconciliation Processing / Accepted Baseline v0.1` as a separate pass, including record-level Dictionary/Corpus eligibility and review of the color mechanism repair requirement.
