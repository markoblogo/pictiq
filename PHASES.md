# Phases

- Infrastructure & Docs (pre-icons): complete (`v0.3.0-infra`)
- Canonical icons v1: pending

### User test protocol (quick)

Goal: validate guessability of the first canonical icons across different language/culture backgrounds.

Participants:
- 5–10 people, mixed native languages/cultures (as diverse as possible).
- Avoid recruiting only designers or only people already familiar with symbol systems.

Materials:
- The first 6 canonical tiles:
  - punct_question, punct_exclaim, logic_yes, logic_no, need_toilet, need_water
- Show icons with **no labels** first.

Tasks (10 prompts):
1) “Where is the toilet?”
2) “Urgent medical help!”
3) “Need water (two)”
4) “Is card payment accepted?”
5) “No / not allowed”
6) “Where can I get Wi-Fi?” (icon may not exist yet; note confusion)
7) “Need a place to sleep”
8) “More water”
9) “Less food”
10) “Taxi?” (baseline transport comprehension)

Procedure:
- Phase 1: show icons without labels; record first guess + confidence (1–5).
- Phase 2: show minimal context (“Pictiq is for short universal messages”); record updated guess.
- Measure time-to-first-guess (rough: <3s / 3–10s / >10s).

Metrics:
- First-guess accuracy per icon
- Common confusion pairs
- Accuracy improvement after minimal context
- Notes about cultural ambiguity

Pass criteria (initial):
- Operators (punct_question, punct_exclaim, logic_yes, logic_no) ≥ 70% correct first-guess.
- need_toilet / need_water: identify major confusion patterns; redesign if repeated confusion appears.

Recording template fields:
- participant_id, native_language, country/region
- icon_id, guess_1, confidence_1, time_bucket_1
- guess_2, confidence_2
- notes/confusions
