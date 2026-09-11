# Human Testing Methodology for Pictiq

> Status: research methodology note
> Source input: [`inputs/perplexity-2026-09/pictogram-comprehension-testing-methods.md`](inputs/perplexity-2026-09/pictogram-comprehension-testing-methods.md)
> Rule: exact standards claims require primary-source verification before publication.

## Test constructs

Do not use “icon comprehension” as a vague umbrella. Name the construct being tested.

| Construct | Question | Example task | What it does not prove |
| --- | --- | --- | --- |
| Recognition | What does the user think the graphic depicts? | Show `food_meat`; ask what objects are visible. | It does not prove the user understands the intended message. |
| Comprehension | What meaning does the user infer? | Show `surface_wavy + punct_exclaim`; ask what action or condition it means. | It does not prove production ability. |
| Context of use | Does the user choose the right interpretation in a realistic situation? | Show a Pictiq message in a road, medical, hotel, or embodied pointing scenario. | It may not generalize outside that context. |
| Production | Can the user construct a valid Pictiq message for an intent? | Give “ask where drinking water is” and use Composer to build a message. | It does not prove another person will decode it. |
| Communication success | Does a sender's Pictiq message produce the intended receiver interpretation? | Sender→Composer→Message→Receiver signaling game. | It does not isolate whether failure came from icon, grammar, context, or interface. |

## AAC-adjacent constructs

| Construct | Practical meaning for Pictiq |
| --- | --- |
| Transparency | A naive user can infer the symbol's meaning without teaching. |
| Translucency | After being told the meaning, the user sees why the symbol fits. |
| Name agreement | Users give the same or compatible names to what the icon depicts. |
| Learnability | Users improve after exposure, feedback, or training and retain the association. |

## ISO / ANSI methodology notes

The supplied research identifies useful methodological distinctions:

- ISO 9186-1: comprehensibility testing.
- ISO 9186-2: perceptual quality / element identification.
- ISO 9186-3: referent association for trained/specialized referents.
- ANSI Z535.3: safety-symbol criteria, including stronger acceptance / critical-confusion concerns as reported by the source.
- Open-ended testing and multiple-choice testing answer different questions.
- Critical confusion matters more than raw correct percentage when mistakes are dangerous.
- Cross-cultural and in-context testing are necessary when deployment context is cross-cultural, public, safety-critical, or AAC-adjacent.

Do not state “ISO requires 85% comprehension.” Preserve the distinction between older ISO-style criteria around 66%, ANSI-style 85% / critical-confusion thresholds as reported, and later ISO editions where adopting organizations may set acceptance criteria. Treat exact threshold and sample-size claims as `VERIFICATION_REQUIRED` until checked against primary standards.

## Small-project experimental rule

For Pictiq, start with modest, explicit tests:

1. define the construct;
2. define the target population;
3. separate icon, composition, context, and production tasks;
4. record wrong answers and critical confusions;
5. preserve negative results;
6. avoid universal claims from small convenience samples.
