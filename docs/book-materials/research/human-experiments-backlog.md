# Human Experiments Backlog

> Status: future research backlog
> Boundary: no experiment is run by this document.

## Priority tests

### Human Test 01 — Core Recognition / Transparency

Question: What do naive users think each Core icon depicts or means?

Scope: current Core only, not all historical or contextual canonical identifiers.

Measures: recognition labels, transparency, name agreement, common confusions, cultural/language background, and 24 px / 64 px survival where relevant.

Why it matters: this tests the visual substrate, not full Pictiq communication.

### Human Test 02 — Composition Comprehension

Question: Can users infer intended meaning from actual multi-token Pictiq compositions?

This is more important to Pictiq than isolated-icon testing alone because Pictiq's architecture depends on composition.

Future candidate grammar examples, not final corpus:

- question;
- negation;
- quantity;
- HOME / shelter context;
- SACRED as modifier;
- CONFLICT;
- contextual polysemy such as `surface_wavy`;
- higher-stakes medical/safety examples with critical-confusion tracking.

Measures: semantic-slot recovery, wrong slot addition, omitted slot, critical confusion, confidence, context benefit, and back-interpretation.

### Human Test 03 — Human Signaling Game

Pipeline:

HUMAN SENDER -> COMPOSER -> PICTIQ MESSAGE -> HUMAN RECEIVER.

Sender receives a semantic intent. Sender constructs Pictiq without manually editing JSON. Receiver interprets the rendered message.

Measures: sender production validity, receiver semantic-slot recovery, unnecessary concepts, intentional omissions, time, revisions, confidence, and failure class.

Dependency: Composer. Do not run at meaningful scale before users can construct valid messages without manual SVG or JSON editing.

## Human / AI signaling matrix

A future matrix can reuse the same semantic corpus, Pictiq Message representation, Renderer, and semantic-slot scoring:

| Sender | Receiver | Use |
| --- | --- | --- |
| HUMAN | HUMAN | Tests Pictiq as a human communication protocol. |
| AI | AI | Tests symbolic coordination and generator/receiver consistency. |
| HUMAN | AI | Tests whether AI can interpret human-authored Pictiq. |
| AI | HUMAN | Tests whether AI-authored Pictiq is useful and not over-specific. |

This is a high-value future research direction, not an implementation task now.
