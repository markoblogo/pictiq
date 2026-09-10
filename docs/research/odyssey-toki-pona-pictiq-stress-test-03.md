# Pictiq Stress Test 03: Odyssey × Toki Pona × sitelen pona × Pictiq

> Status: FINAL LOCAL RESEARCH ARTIFACT / HUMAN-ACCEPTED STAGES 1, 2A, AND 2B  
> Date: 2026-09-10  
> Supersedes as primary human-readable artifact: Stage 1, Stage 2A, and Stage 2B notes; those files remain historical evidence.  
> Source manuscript: `/Volumes/Work/books archive/odyssey/OD-TP-kdp-layout-v1.odt`  
> Source manuscript SHA-256: `ab373fc21f9a230dda230b7a4244546d48789bc13c8f909fa5c698ed21226c37`

## Source project

This experiment uses the author-owned manuscript for *The Odyssey: Toki Pona Edition with Sitelen Pona* by Anton Biletskyi-Volokh. The supplied listing identifies the published Amazon page as <https://www.amazon.com/dp/B0HHSK3Y45>. The manuscript contains three reading layers: English reference text, Toki Pona translation, and the same Toki Pona rendered in sitelen pona.

## Comparative frame

The comparison path is English → Toki Pona → sitelen pona → Pictiq, but these are not equivalent translation systems. English is the literary source/reference. Toki Pona is a minimalist natural/conlang rendering that rebuilds complex propositions from a small vocabulary. sitelen pona is a writing system for the same Toki Pona text. Pictiq is a separate visual symbolic protocol that compresses toward pragmatic and narrative semantic structure.

sitelen pona is visually interesting here because the same Toki Pona proposition can be seen alphabetically and through glyphs. It is not a direct ancestor, source, or equivalent of Pictiq. sitelen pona glyphs encode Toki Pona words; Pictiq primitives participate in a different semantic protocol.

## Method

Six manually reviewed semantic fragments were used exactly. No extra fragments were added to increase sample size. The Pictiq representations below reconstruct the accepted Stage 1 review decisions using only current accepted ordinary Pictiq IDs and current Entity Symbols. Where exact sitelen pona rendering cannot be safely reproduced from the ODT/font pipeline in this repository, the exact Toki Pona text is preserved with a publication instruction instead of fake glyphs.

## Case 1. Return from war / Odysseus / Calypso

### A. English source

> By now all the others who had escaped death in the war were safely home, free from battle and the sea. Odysseus alone still longed to return to his home and his wife. The goddess Calypso kept him in her deep caves, for she desired him as her husband.

### B. Toki Pona

```text
tenpo ni la jan ante ale pi weka tan moli lon utala li kama sin tawa tomo ona. ona li weka tan utala li weka tan telo suli. taso jan Osite taso li awen lon ma weka. ona li wile mute e kama sin tawa tomo ona tawa meli ona. sewi Kalipso li awen e ona lon lupa ma suli ona. sewi ni li olin e jan Osite li wile e ona sama mije ona.
```

### C. sitelen pona

SITELEN PONA PUBLICATION ASSET: render this exact Toki Pona passage using the same sitelen pona font/rendering pipeline used in the published Odyssey edition. No substitute glyphs or image-generator imitation are used in this research artifact.

### D. Pictiq representation


- `person_generic + qty_5 + qty_plus + action_conflict + state_dead + logic_no`

- `entity:odysseus@literary + action_conflict + state_dead + logic_no`

- `entity:odysseus@literary + love_heart + person_generic`

- `entity:calypso@odyssey + entity:odysseus@literary + logic_no`


Machine-readable ID sequence:

```json
[
  [
    "person_generic",
    "qty_5",
    "qty_plus",
    "action_conflict",
    "state_dead",
    "logic_no"
  ],
  [
    "entity:odysseus@literary",
    "action_conflict",
    "state_dead",
    "logic_no"
  ],
  [
    "entity:odysseus@literary",
    "love_heart",
    "person_generic"
  ],
  [
    "entity:calypso@odyssey",
    "entity:odysseus@literary",
    "logic_no"
  ]
]
```

### E. Back interpretation

Many people survived conflict; Odysseus is alive after conflict, wants/keeps a loved-person relation in the narrative, and Calypso blocks or holds him in context.


### F. What survived

survival after war, Odysseus as named entity, Calypso as named entity, spouse/love pressure, captivity/blocking pressure


### G. What was compressed

war/battle/conflict -> action_conflict; wife/husband -> loved person; cave/home detail not lexicalized


### H. Intentional omissions

deep cave description, desire-as-husband detail, exact home location/Ithaca in this case


### I. Gaps / architecture findings

Exact HOME/RETURN/CAVE/PREVENT remain unresolved; no cave primitive added.


### J. Why this translation was chosen

The accepted review prioritizes narrative skeleton and relationship pressure over literal spouse/cave vocabulary.


## Case 2. Gods / Poseidon / hostility / homecoming

### A. English source

> But when the year came in which the gods had decided that he should return to Ithaca, his troubles were still not over, even among his own people. All the gods felt pity for him except Poseidon, who remained angry with Odysseus until he finally reached his own land.

### B. Toki Pona

```text
taso tenpo sike ni li kama. sewi ale li wile e ni: jan Osite o kama sin tawa ma Itaka. taso pakala ona li pini ala. lon poka jan ona kin la pakala li awen. sewi ale li pilin e pakala ona. taso sewi Poseton li awen pilin utala tawa jan Osite. pilin utala ni li awen tawa tenpo pi kama jan Osite lon ma mama ona.
```

### C. sitelen pona

SITELEN PONA PUBLICATION ASSET: render this exact Toki Pona passage using the same sitelen pona font/rendering pipeline used in the published Odyssey edition. No substitute glyphs or image-generator imitation are used in this research artifact.

### D. Pictiq representation


- `qual_sacred + qty_5 + qty_plus`

- `entity:poseidon@odyssey + qual_bad + power_energy + entity:odysseus@literary`

- `entity:poseidon@odyssey + action_conflict + entity:odysseus@literary`


Machine-readable ID sequence:

```json
[
  [
    "qual_sacred",
    "qty_5",
    "qty_plus"
  ],
  [
    "entity:poseidon@odyssey",
    "qual_bad",
    "power_energy",
    "entity:odysseus@literary"
  ],
  [
    "entity:poseidon@odyssey",
    "action_conflict",
    "entity:odysseus@literary"
  ]
]
```

### E. Back interpretation

The sacred/divine group wants Odysseus home in context, while Poseidon maintains strong hostility and active opposition toward Odysseus.


### F. What survived

divine group, Poseidon, Odysseus, hostility, homecoming pressure


### G. What was compressed

gods -> sacred + many in narrative context; anger/fury -> bad + energy as contextual hypothesis; trouble not separately lexicalized


### H. Intentional omissions

Ithaca and “own people” details are not fully represented by existing IDs.


### I. Gaps / architecture findings

ENERGY-as-intensifier remains hypothetical; HOME/RETURN exactness remains a gap.


### J. Why this translation was chosen

The review separates negative attitude from hostile action and avoids adding GOD or ANGER just for the Odyssey.


## Case 3. Ship / sea / dark sky

### A. English source

> When we had left the island and no other land was in sight, but only sky and sea, the son of Saturn raised a dark cloud over our ship and the sea grew dark beneath it.

### B. Toki Pona

```text
“mi weka tan ma sike li ken lukin ala e ma ante, sewi en telo suli taso la sewi Suse, jan lili pi sewi Satuno, li pana e kon pimeja lon sewi pi tomo tawa telo mi. telo suli lon anpa ona li kama pimeja.”
```

### C. sitelen pona

SITELEN PONA PUBLICATION ASSET: render this exact Toki Pona passage using the same sitelen pona font/rendering pipeline used in the published Odyssey edition. No substitute glyphs or image-generator imitation are used in this research artifact.

### D. Pictiq representation


- `move_watercraft + surface_wavy + nature_cloud`

- `nature_cloud + surface_wavy`

- `entity:zeus@odyssey + nature_cloud + move_watercraft`


Machine-readable ID sequence:

```json
[
  [
    "move_watercraft",
    "surface_wavy",
    "nature_cloud"
  ],
  [
    "nature_cloud",
    "surface_wavy"
  ],
  [
    "entity:zeus@odyssey",
    "nature_cloud",
    "move_watercraft"
  ]
]
```

### E. Back interpretation

A watercraft is at sea/wavy surface under cloud/sky; Zeus is the named actor associated with the dark cloud in the source context.


### F. What survived

ship/watercraft, sea/waves, cloud/sky, Zeus/Saturn family reference via entity symbols


### G. What was compressed

ship -> move_watercraft; sea -> surface_wavy when surface/sea condition matters; sky/cloud -> nature_cloud


### H. Intentional omissions

island/land visibility, exact darkness if parametric COLOR is not rendered inline, mast/sail detail


### I. Gaps / architecture findings

Parametric COLOR is accepted direction but not represented as ordinary icon ID; move_boat vs move_watercraft is deferred.


### J. Why this translation was chosen

The accepted review uses cross-domain wavy evidence and avoids adding DARK/SKY/ISLAND/LAND/MAST/SAIL.


## Case 4. Arete dialogue: identity / origin / clothing

### A. English source

> “Who are you? Where do you come from? And who gave you those clothes?”

### B. Toki Pona

```text
“sina jan seme? sina kama tan ma seme? jan seme li pana e len ni tawa sina?”
```

### C. sitelen pona

SITELEN PONA PUBLICATION ASSET: render this exact Toki Pona passage using the same sitelen pona font/rendering pipeline used in the published Odyssey edition. No substitute glyphs or image-generator imitation are used in this research artifact.

### D. Pictiq representation


- `person_generic + punct_question`

- `rel_here + punct_question`

- `person_generic + item_clothing + punct_question`

- `entity:odysseus@literary`


Machine-readable ID sequence:

```json
[
  [
    "person_generic",
    "punct_question"
  ],
  [
    "rel_here",
    "punct_question"
  ],
  [
    "person_generic",
    "item_clothing",
    "punct_question"
  ],
  [
    "entity:odysseus@literary"
  ]
]
```

### E. Back interpretation

The dialogue asks for identity, place/origin in context, and clothing explanation; Odysseus can answer with his entity symbol.


### F. What survived

question frame, identity request, location/origin pressure, clothing topic


### G. What was compressed

who/you/name -> person + question in dialogue; from/origin -> here/place question; gave -> omitted unless action-relevant


### H. Intentional omissions

exact giver relation, politeness/formulaic dialogue framing


### I. Gaps / architecture findings

No WHO/YOU/I/NAME/FROM/ORIGIN/GIVE primitives were added; named places may later need Entity Symbols.


### J. Why this translation was chosen

The communication situation itself carries ask/answer structure; adding metacommunication words would overfit one passage.


## Case 5. Survival / food / animal / cooking

### A. English source

> As long as the corn and wine held out the men did not touch the cattle when they were hungry; when, however, they had eaten all there was in the ship, they were forced to go further afield, with hook and line, catching birds, and taking whatever they could lay their hands on, for they were starving.
> 
> And indeed the gods began at once to show signs and wonders among us, for the hides of the cattle crawled about, and the joints upon the spits began to low like cows, and the meat, whether cooked or raw, kept on making a noise just as cows do.

### B. Toki Pona

```text
“pan en telo nasa li awen lon tomo tawa telo la jan mi li luka ala e soweli mani lon pilin pi moku ala ona. taso moku ale lon tomo li pini la ona o alasa e moku lon ma, kepeken ilo pi kama jo e kala en linja, li kama jo e waso e ijo ale pi ken luka ona, tan ni: moku ala li pakala e ona.”

“lon tenpo sama la sewi li open pana e sitelen nasa monsuta tawa mi. selo pi soweli mani li tawa sama ona li lon. kipisi moku lon palisa seli moku li open kalama sama soweli mani. moku soweli seli en moku soweli pi seli ala li awen pana e kalama sama soweli mani.”
```

### C. sitelen pona

SITELEN PONA PUBLICATION ASSET: render this exact Toki Pona passage using the same sitelen pona font/rendering pipeline used in the published Odyssey edition. No substitute glyphs or image-generator imitation are used in this research artifact.

### D. Pictiq representation


- `person_generic + qty_5 + qty_plus + state_dead + logic_no`

- `move_watercraft + need_food + need_water`

- `nature_animal + need_food + state_hot`


Machine-readable ID sequence:

```json
[
  [
    "person_generic",
    "qty_5",
    "qty_plus",
    "state_dead",
    "logic_no"
  ],
  [
    "move_watercraft",
    "need_food",
    "need_water"
  ],
  [
    "nature_animal",
    "need_food",
    "state_hot"
  ]
]
```

### E. Back interpretation

People survive or try not to die; the ship/watercraft carries food/water pressure; animal + food + heat frames cooked animal food/meat rather than merely an animal on fire.


### F. What survived

survival pressure, food/drink, ship supplies, animal/cattle category, cooked/raw meat pressure


### G. What was compressed

cattle/species -> nature_animal unless taxonomy matters; hunger/starvation -> survival/food/death frame; cooking -> animal + food + hot/fire frame


### H. Intentional omissions

hand/washing, hooks/lines/birds details, ritual signs, exact cow/cattle taxonomy


### I. Gaps / architecture findings

No COOK/HUNGER/STARVATION/HAND/WASH primitives added; species taxonomy deferred.


### J. Why this translation was chosen

The accepted review found FOOD necessary in the cooking frame and treated washing hands as intentional omission.


## Case 6. Poseidon / Polyphemus / eye injury / kinship / blocked homecoming

### A. English source

> “Bear in mind, however, that Neptune is still furious with Ulysses for having blinded an eye of Polyphemus king of the Cyclopes. Polyphemus is son to Neptune by the nymph Thoosa, daughter to the sea-king Phorcys; therefore though he will not kill Ulysses outright, he torments him by preventing him from getting home.”

### B. Toki Pona

```text
“taso o sona e ni: sewi Poseton li awen pilin utala mute tawa jan Osite. tan seme? jan Osite li pakala e oko wan pi jan Polupemo, jan lawa pi kulupu Siklope. jan Polupemo li jan lili pi sewi Poseton en sewi meli Tosa. sewi meli Tosa li jan lili pi sewi majuna Pokusa pi telo suli. sewi Poseton li wile ala moli e jan Osite. taso ona li pana e pakala tawa ona li awen e ona tan kama sin tawa tomo.”
```

### C. sitelen pona

SITELEN PONA PUBLICATION ASSET: render this exact Toki Pona passage using the same sitelen pona font/rendering pipeline used in the published Odyssey edition. No substitute glyphs or image-generator imitation are used in this research artifact.

### D. Pictiq representation


- `entity:odysseus@literary + action_conflict + entity:polyphemus@odyssey + eye_look + qty_1 + qty_minus`

- `entity:polyphemus@odyssey + love_heart + person_generic + rel_lesser + entity:poseidon@odyssey`

- `entity:poseidon@odyssey + state_dead + logic_no + entity:odysseus@literary`

- `entity:poseidon@odyssey + action_conflict + entity:odysseus@literary`


Machine-readable ID sequence:

```json
[
  [
    "entity:odysseus@literary",
    "action_conflict",
    "entity:polyphemus@odyssey",
    "eye_look",
    "qty_1",
    "qty_minus"
  ],
  [
    "entity:polyphemus@odyssey",
    "love_heart",
    "person_generic",
    "rel_lesser",
    "entity:poseidon@odyssey"
  ],
  [
    "entity:poseidon@odyssey",
    "state_dead",
    "logic_no",
    "entity:odysseus@literary"
  ],
  [
    "entity:poseidon@odyssey",
    "action_conflict",
    "entity:odysseus@literary"
  ]
]
```

### E. Back interpretation

Odysseus harms or removes one eye of Polyphemus; Polyphemus is represented as a child/descendant relation in context; Poseidon does not kill Odysseus but acts against his homecoming.


### F. What survived

agent, hostile action, patient, one-eye loss, kinship pressure, non-killing, hostile blocking


### G. What was compressed

blinding/injury -> eye + one + minus; son/daughter -> relationship + lesser in context; torment/prevent/return -> conflict/no-homecoming pressure


### H. Intentional omissions

Thoosa/Phorcys genealogy details beyond main kinship pressure, Cyclopes kingship, exact legal causal explanation


### I. Gaps / architecture findings

No BLIND/INJURE/PREVENT/TORMENT/SON/DAUGHTER primitives added; rel_lesser is not globally CHILD.


### J. Why this translation was chosen

The accepted decomposition preserves the narrative action and relation without adding gendered or injury-specific vocabulary.


## Structural gender neutrality

Odyssey supplied strong narrative pressure for gendered English categories: wife/husband, son/daughter, he/she, man/woman, goddess/nymph, and family. The accepted Pictiq decision is not to encode gender by default. Generic `person_generic` means human/person, and Entity Symbols identify specific named entities without needing a gender feature.

This is not an absolute prohibition. Specialized contexts may represent otherwise omitted distinctions when they are materially necessary. The Odyssey experiment shows that loved person, family, and child/descendant can often be handled through composition and entity context without adding gendered Core vocabulary.

## Entity Symbol finding

Narrative pressure validated the Entity Symbol architecture. The Odyssey entity set now includes existing `entity:odysseus@literary` plus new `entity:calypso@odyssey`, `entity:poseidon@odyssey`, `entity:zeus@odyssey`, `entity:saturn@odyssey`, and `entity:polyphemus@odyssey`.

These are visual proper names, not lexical concepts. Poseidon may visually use trident and waves, but the symbol does not semantically parse as TRIDENT + WAVES. The whole Entity Symbol atomically identifies Poseidon inside its namespace.

## Intentional omission vs loss

`DIRECT`, `COMPOSED`, `CONTEXT-SUFFICIENT`, `LOSSY`, and `GAP` describe how well a meaning is represented. `INTENTIONAL_OMISSION` records a different decision: the source detail was deliberately excluded because it did not materially contribute to the selected Pictiq narrative representation.

Examples include washing hands, mast/sail detail, redundant dialogue framing, literary politeness, and descriptive detail that does not change the narrative skeleton. Pictiq does not fail every time it declines to translate a source detail. Sometimes omission is the correct translation decision.

## Semantic compression inventory

| Source distinction | Pictiq treatment | Status |
| --- | --- | --- |
| wife / husband | `love_heart + person_generic` or entity relation in context | COMPOSITION SUFFICIENT for this test |
| anger / fury / hatred | `qual_bad` plus possible `power_energy` intensity context | DEFERRED grammar hypothesis |
| war / attack / aggression | `action_conflict` | accepted contextual ordinary primitive |
| boat / ship / watercraft | `move_watercraft` | accepted contextual ordinary primitive; `move_boat` cleanup deferred |
| cloud / sky | `nature_cloud` | accepted contextual ordinary primitive |
| animal species | `nature_animal` unless taxonomy matters | accepted Core generic category |
| dark | parametric COLOR where needed | mechanism direction, not lexical DARK |

## Toki Pona comparison

The manuscript uses recurring anchors such as `telo suli` for sea, `tomo tawa telo` for ship, `nasin tawa` for journey, `tomo` for home/dwelling, `ma mama` for homeland, `kama sin tawa tomo` for return home/homecoming, `sewi` for god/divine being, `utala` for battle/conflict, and `lupa ma` for cave.

Toki Pona reduces lexical vocabulary but still reconstructs rich propositions through natural-language grammar and composition. Pictiq often goes further: it may remove grammatical and literary distinctions and preserve only the semantic/narrative structure required for comprehension. This is a difference of purpose, not a superiority claim.

## What Odyssey added to Pictiq

Architecture/principles: semantic/practical translation over surface-form translation; `INTENTIONAL_OMISSION`; structural gender neutrality; semantic frames; narrative sequence as contextual event ordering; communication structure replacing some metacommunication; relationship composition; strengthened Entity Symbols.

Ordinary primitives introduced through the experiment: `action_conflict`, `move_watercraft`, `qual_sacred`, `nature_animal`, `nature_cloud`.

Entity Symbols introduced: Poseidon, Zeus, Saturn, Polyphemus, Calypso.

Reused or further validated: `surface_wavy`, `state_dead`, parametric COLOR direction, `rel_here`, `punct_question`, `love_heart`, `qual_bad`, `power_energy`, `eye_look`, and quantity/numeric mechanisms.

## What Odyssey did not add

| Candidate | Treatment |
| --- | --- |
| WHO, I, YOU, NAME, ASK, ANSWER | NOT NEEDED IN THIS TEST; dialogue structure and `punct_question` carried enough. |
| HE, SHE, MAN, WOMAN, HUSBAND, WIFE, SON, DAUGHTER | COMPOSITION SUFFICIENT / SPECIALIZED FUTURE; not needed in Core for this representation. |
| ANGER, HATE, PITY | DEFERRED; `qual_bad`, context, and possible intensity handled the reviewed cases. |
| GIVE, FROM, ORIGIN | NOT NEEDED IN THIS TEST; context and `rel_here` handled the reviewed questions. |
| COOK, HUNGER, STARVATION, HAND, WASH | NOT NEEDED IN THIS TEST; cooking via semantic frame, washing hands intentionally omitted. |
| ISLAND, LAND, MAST, SAIL, CAVE | CONTEXTUAL FUTURE; descriptive detail did not justify new primitives here. |
| BLIND, INJURE, PREVENT, TORMENT | COMPOSITION SUFFICIENT / DEFERRED; eye + one + minus and conflict/no-death frames preserved the narrative action. |

## Final conclusions

1. Pictiq could preserve a recognizable narrative skeleton across the six reviewed fragments, but only by accepting semantic compression.
2. Named entities, broad actions, survival states, basic relationships, question structure, and repeated narrative anchors survived most reliably.
3. Literary texture, grammatical gender, exact kinship labels, source-language pronouns, and fine physical details were most often compressed.
4. Intentional omissions were essential, especially for washing hands, mast/sail detail, redundant dialogue framing, and descriptive ornament.
5. Genuine vocabulary pressure appeared for CONFLICT, WATERCRAFT, SACRED, ANIMAL, CLOUD/SKY, and scoped Entity Symbols.
6. Narrative use did not force gender vocabulary into Core.
7. The experiment validated Entity Symbols as visual proper names for narrative translation.
8. `surface_wavy`, `state_dead`, COLOR direction, and relationship composition gained cross-domain evidence.
9. Unresolved grammar hypotheses include intensity with `power_energy`, child/descendant use of `rel_lesser`, and event sequencing vs causality.
10. Next tests should include a post-Odyssey Canonical Registry/Core audit, `move_boat` vs `move_watercraft`, parametric COLOR, and a smaller narrative rendering/prototype using actual tiles.
