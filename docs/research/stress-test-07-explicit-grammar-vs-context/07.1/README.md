# Stress Test 07.1 — Raster-safe execution package

**Status:** `PREPARED / NOT EXECUTED`

Stress Test 07.1 is a clean execution package for the frozen Stress Test 07 design. It changes only participant delivery: SVG is replaced by a metadata-free PNG rasterization. Hypotheses, semantic targets, A/B mechanisms, visual geometry, randomized orders, prompts, micro-learning content, coding rules, and transfer method remain frozen.

## Participant delivery

- 6 primary and 6 transfer stimuli, all `1872×768` RGBA PNGs.
- Neutral participant filenames: `stimulus-01.png` through `stimulus-06.png`, and `transfer-01.png` through `transfer-06.png`.
- Internal mappings, source/delivery hashes, and intended meanings are in [delivery manifest](delivery-manifest.json); never send it to a participant.
- [Visual-fidelity review](visual-fidelity-review.svg) is internal only. `07C-A` is explicitly checked: it shows toilet plus question, never a no-smoking sign.

## Frozen inputs

The exact delivery copies and hashes for the blind prompt, practical task prompts, and micro-learning guide are recorded in the manifest. No wording changed. The guide is delivered only after every blind and practical response is saved.

## Execution controls

- [Pre-run checklist](pre-run-checklist.md)
- [Delivery log schema](delivery-log.schema.json)
- [Fresh panel assignments](rerun-assignments.json)
- [Pilot separation record](../pilot/README.md)

Use a new conversation for each assigned system. Never substitute SVG. If PNG display cannot be verified, record `DELIVERY FAILURE` and stop that run.
