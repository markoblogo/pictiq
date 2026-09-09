# Embodied and Standalone Profiles

Pictiq has one canonical lexicon. These profiles recommend canonical IDs for different communication modes; they do not redefine icon semantics or create separate libraries.

## Profile rule

Before adding a concept to Embodied Profile, ask whether a live user can communicate it more efficiently through body, gesture, gaze, environment, pointing, or the carrier object. Before adding a concept to Standalone Profile, ask whether it must remain explicit when the communicator is absent. Canonical existence and profile membership are separate decisions.

Context profiles can layer on either core profile: Paris shirt = Embodied + Paris; Paris poster = Standalone + Paris; Nightlife lighter = Embodied + Nightlife; website = Standalone + Web/UI; narrative = Standalone + Narrative/Entity namespace.

## Embodied Profile

[`profiles/embodied-core-v0.1.json`](../profiles/embodied-core-v0.1.json) is intentionally compact for person-present communication. It omits concepts reliably carried by a present body, gesture, visible surroundings, or pointing, including `person_generic`, eye/look, clothing, body, physical size, color, direction, and generic communication.

## Standalone Profile

[`profiles/standalone-core-v0.1.json`](../profiles/standalone-core-v0.1.json) contains the current practical standalone core. Batch B membership is accepted in v1.0.2, and Batch C membership is human-accepted after local visual review; the profile remains open to future research, including a parametric COLOR prototype. Entity symbols remain scoped context or narrative mechanisms outside the ordinary Core profiles.

The JSON files reference IDs in [`lexicon/icon-index.json`](../lexicon/icon-index.json); they do not duplicate SVGs or create `icons/embodied/` and `icons/standalone/` trees.
