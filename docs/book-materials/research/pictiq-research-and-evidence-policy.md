# Pictiq Research and Evidence Policy

> Status: project research policy, 2026-09-11.
> Boundary: no vocabulary, grammar, schema, renderer, Composer, icon, pack, profile, tag, or release change.

## Current phase

Pictiq is moving from primarily building the language toward putting it under pressure, deploying it inside real products, publishing results, and observing real-world response.

Formal human experiments remain useful. They normally should not block ordinary project development unless a specific claim genuinely requires them.

## Evidence sources

| Source | Use | Strengths | Limits |
| --- | --- | --- | --- |
| `CREATOR_TEST` | Project author uses the tool/language in real work. | Fast, high-context, catches obvious friction. | Not external-user evidence. |
| `MACHINE_TEST` | One model/tool attempts generation, decoding, or validation. | Cheap, repeatable, exposes machine-interface pressure. | Model-specific; not human comprehension proof. |
| `CROSS_MODEL_TEST` | Several independent model families attempt the same task. | Finds convergence/divergence across systems. | Still machine evidence. |
| `ADVERSARIAL_REVIEW` | Hostile or critical review of claims, examples, or architecture. | Good at finding overclaiming and hidden assumptions. | Does not prove usability. |
| `DOMAIN_STRESS_TEST` | Apply Pictiq to a domain such as road, Odyssey, travel, or emergency. | Reveals gaps and compression pressure. | Domain selection may bias findings. |
| `REAL_WORLD_USAGE` | People actually use tools/books/cards/Composer. | Behavioral evidence under less artificial conditions. | Harder to isolate causes. |
| `ORGANIC_FEEDBACK` | Issues, comments, criticism, external examples. | Finds unexpected interpretation and adoption paths. | Sparse and noisy. |
| `MARKET_SIGNAL` | Purchases, downloads, repeated use, ignored features. | Tests whether a product artifact matters to people. | Not direct proof of language effectiveness. |
| `EXTERNAL_RESEARCH` | Published research and precedent systems. | Grounds claims and methods. | Usually indirect; must not be overfit to Pictiq. |
| `FORMAL_HUMAN_TEST` | Planned participant study with protocol and scoring. | Strong when a concrete human claim requires it. | Recruitment cost, artificial tasks, slow iteration. |

## Formal human tests

Formal human tests are targeted evidence, not the default development gate. They are valuable when the claim is about human comprehension, learnability, authoring, safety, accessibility, or cross-cultural interpretation. They are not required before every Composer fix, stress test, product mockup, post, book note, or deployment candidate.

## Real-world evidence

Useful signals include people opening Composer, creating/exporting messages, filing issues, forking, posting examples, criticizing, citing, buying books, reviewing, downloading, adapting Pictiq unexpectedly, or ignoring a feature after meaningful exposure.

Vanity metrics do not prove language effectiveness. Negative and null results should be preserved.

## Market signal

Product behavior can be evidence. A Pictiq-enabled children's picture book may sell or fail. Readers may mention or ignore the symbol layer. A travel/showbook may help or may be unused. These signals should be recorded without converting them into stronger claims than they support.
