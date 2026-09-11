# Stress Test 04B Protocol

> Status: fixed protocol draft for human review; not run.
> Public Composer: <https://markoblogo.github.io/pictiq/composer/>
> Dependency: Composer v0.1 creator/software acceptance passed.

## Purpose

Run a tiny exploratory human-authoring pilot to see whether an unfamiliar adult can use Composer v0.1 to create valid simple Pictiq messages with minimal instruction.

## Participants

Recruit 1-3 adult participants. Preferred characteristics:

- no prior detailed Pictiq knowledge;
- ordinary everyday browser/computer experience;
- no programming or linguistics knowledge required.

Use anonymized IDs: `P01`, `P02`, `P03`. Do not collect full legal names, addresses, accounts, sensitive personal history, or unnecessary demographics. Record only approximate relevant metadata: prior Pictiq exposure, general computer comfort, browser/device class, and languages used if relevant.

## Environment record

For each session record:

- Pictiq version visible/known at test time;
- Composer version: v0.1;
- Composer URL: <https://markoblogo.github.io/pictiq/composer/>;
- browser and version if known;
- device class;
- date;
- selected Profile and Context Packs per task when relevant.

Use the public static Composer unless a newer accepted candidate is intentionally being tested locally.

## Session flow

1. Open Composer for the participant.
2. Read or paraphrase the approved introduction in [participant instructions](participant-instructions.md).
3. Ask the optional think-aloud prompt once.
4. Run the unscored training task with mechanical help allowed.
5. Run the eight scored tasks in fixed order.
6. For each scored task, observe without semantic coaching.
7. Ask optional confidence after each task.
8. Ask the [debrief questions](debrief.md).
9. Save the observer sheet and, if collected, exported SVG/Message JSON.

## Experimenter boundaries

The experimenter may explain browser/UI mechanics if the participant is blocked. The experimenter must not tell the participant which symbol to choose, suggest an intended Pictiq translation, explain internal IDs as answers, repair the composition, or confirm correctness during a scored task.

## Assistance rule

If the participant is blocked for about 60-90 seconds because they cannot operate the UI, give neutral mechanical help. Examples:

- "You can browse the Palette or use Search."
- "Symbols in the Workspace can be dragged."
- "The plus button adds another Frame."
- "The preview on the right shows the rendered message."

Do not provide semantic guidance such as "search for water" or "that icon is the right answer." Record every intervention.

## Metrics

Use descriptive metrics only:

- `TASK_COMPLETED`
- `VALID_MESSAGE_PRODUCED`
- `REQUIRED_SLOT_RECOVERY`
- `TIME_TO_FIRST_VALID_MESSAGE`
- `NUMBER_OF_CORRECTIONS`
- `HELP_REQUIRED`
- `EXPORT_SUCCESS`
- optional confidence rating, 1-5

Do not produce a single usability score.

## Friction taxonomy

Use the taxonomy in [observer sheet](observer-sheet.md). Keep Composer usability, Pictiq concept selection, Pictiq grammar, task ambiguity, and vocabulary limits separate.

## Ethics and recording

This is low-risk authoring usability work. Do not include children, vulnerable participants, medical emergency instructions, legal/benefit eligibility tasks, or sensitive identity tasks. Screen/audio recording is optional and requires explicit participant consent. The pilot must remain possible with manual notes only. Do not add telemetry or analytics to Composer.

## Scope exclusions

Do not test grouping, free 2D spatial layout, arbitrary exact numbers beyond current notation, tense, grammatical gender, IF/THEN, semantic roles, arbitrary relations, new Entity Symbols, unsupported vocabulary, or speculative grammar.
