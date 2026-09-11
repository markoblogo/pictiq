# Stress Test 04B — Human Authoring / Composer Usability Kit

> Status: experiment kit ready for human review; participant study not run.
> Date: 2026-09-11
> Public Composer: <https://markoblogo.github.io/pictiq/composer/>
> Boundary: no participant data, no simulated users, no Composer release.

## Research question

Can a person who does not know Pictiq's internal repository architecture use Composer v0.1 to construct simple valid Pictiq messages after minimal instruction?

This pilot tests authoring with Composer. It does not test whether the participant has memorized Pictiq, does not ask for visual preference, and does not establish broad usability or grammar learnability.

## Kit files

- [Protocol](protocol.md)
- [Participant instructions](participant-instructions.md)
- [Fixed task corpus](tasks.md)
- [Experimenter guide](experimenter-guide.md)
- [Observer sheet](observer-sheet.md)
- [Semantic targets](semantic-targets.md)
- [Debrief](debrief.md)
- [Machine-readable results template](results-template.json)

## Intended pilot shape

- Participants: 1-3 adults with ordinary browser/computer experience and no detailed Pictiq knowledge.
- Duration: approximately 15-25 minutes per participant.
- Training: 1 unscored task.
- Scored tasks: 8 fixed-order tasks.
- Method: manual observation, optional think-aloud, optional screen/audio recording only with explicit participant consent.

## Decision outcomes

The tiny pilot can support one of four practical outcomes:

- `READY_FOR_RELEASE`: no recurring blocking authoring problem appears.
- `FIX_BEFORE_RELEASE`: recurring Composer UX/mechanics problems prevent task completion.
- `LANGUAGE_PRESSURE_OBSERVED`: failures appear to come from Pictiq language/composition rather than Composer.
- `INCONCLUSIVE`: too little evidence, task problems, or participant/session problems.

Do not derive rigid statistical claims from 1-3 participants.

## Current status distinction

Composer v0.1 creator/software acceptance has passed. Stress Test 04B asks a different question: whether unfamiliar users can author messages after minimal instruction. 04B is still not run, and this directory contains no results.
