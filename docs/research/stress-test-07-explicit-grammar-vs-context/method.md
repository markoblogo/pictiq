# Method

## Design

A within-panel, paired-mechanism study. Participants receive one stimulus at a time. The primary stimulus is followed by a blind interpretation prompt, then its practical task prompt. Only after all blind responses are captured does the facilitator supply the short, condition-specific guide and show a new transfer stimulus.

The experiment keeps black-and-white rendering, tile scale, 624×256 canvas, object artwork and target practical meaning constant where possible. It varies only quantity notation, question/availability representation, or question/location representation.

## Conditions

A conditions are normative Pictiq on commit `b03233d72626a11d15f88677dd17c54755a7399f`:

- `need_water + qty_1 + qty_2` for three bottles/units of water;
- `need_water + punct_question` for availability;
- `need_toilet + punct_question` for a toilet-location question.

B conditions are researcher-designed, non-Pictiq test mechanisms. They must never be entered into the Pictiq registry, Message Schema or normal renderer.

## Phases

1. Blind interpretation.
2. Practical task response.
3. Micro-learning using the frozen guide.
4. Learned transfer on a new meaning using the same mechanism.

Do not show an A/B pair together or reveal the system before the blind phase. Record the first response without paraphrasing it.
