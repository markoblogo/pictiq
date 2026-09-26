# Pictiq Publishing Case — Good Dog, Bad System

**INTERNAL / PREPUBLICATION — NOT A PUBLIC CASE PAGE**

## Case record

- **Book:** *Good Dog, Bad System: A Darkly Comic System Apocalypse LitRPG*
- **Author:** Sminx Jonahtan J.
- **Project / series:** Good Dogs of the Apocalypse
- **Use case:** `LONG_FORM_FICTION`
- **Medium:** `PRINT_BOOK + EBOOK`
- **Status:** `PREPUBLICATION`
- **Role:** `IN-WORLD CANINE COMMUNICATION`
- **Publication evidence:** Not supplied. No Amazon URL, ASIN, ISBN, publication date, or sales claim is recorded.

This case records Pictiq as the in-world visual language for direct canine communication in a full-length English LitRPG novel. Human characters speak English. System notices use the book's system typography and English conventions. This lets readers encounter Pictiq in the illustrations without requiring the prose novel to be written in or translated into Pictiq.

## Production convention and source authority

| Communication | Production form |
| --- | --- |
| Dog spoken / direct communication | Pictiq |
| Human spoken dialogue | English |
| System communication | System typography / English as defined by the book |

**Critical rule:** Pictiq glyphs must never be generated, approximated, or imitated by image generation. Generative image systems may alter glyph identity, order, speaker assignment, or dialogue sequence. Composer output is the authoritative graphical source; approved Pictiq must be treated as an immutable graphic asset during composition.

`English semantic dialogue → Pictiq Composer → owner-approved Composer output → comic composition → final book illustration`

The final illustration is not an authority for reconstructing Pictiq. Preserve Composer sources separately from flattened artwork. Human English lines remain contextual evidence and are not Pictiq output.

## Asset set

The six supplied final illustrations and four Composer source sheets are preserved byte-for-byte in the [asset manifest](GOOD_DOG_BAD_SYSTEM_PICTIQ_ASSET_MANIFEST_V1.json). `GD1art.jpg` is additionally preserved as a **production-reference / semantic-source image**, not promoted to a final illustration. GD0 and GD5 are non-Pictiq opening and closing illustrations; GD1–GD4 are Pictiq comics. All ten required source files are accounted for; the extra reference is clearly typed separately.

## Dialogue ledger and correction history

See the [machine-readable dialogue ledger](GOOD_DOG_BAD_SYSTEM_PICTIQ_DIALOGUE_LEDGER_V1.json). It stores approved semantic dialogue separately from glyph artwork. The owner clarified that dialogue sequence 01 is the dog exchange transcribed from `GD1art.jpg`; the three previously supplied numbered exchanges are sequences 02–04, aligned to GD2–GD4. Dialogue sequence labels are not asset renamings.

### GD1 — dog exchange; English semantic source confirmed

`GD1art.jpg` shows six dog-spoken turns between the light-coated dog at left and the dark-coated dog at right:

1. Left dog: “Is she alive?”
2. Right dog: “Yes.”
3. Left dog: “You sound farther away.”
4. Right dog: “Now?”
5. Left dog: “Too close.”
6. Left dog: “Good. I have always liked upstairs.”

The final human line, “He says good night.”, is contextual English, not Pictiq. The supplied Illustration Continuity Audit identifies the small pale shaggy dog as Borscht and the larger dark dog as Mriya; the Visual Character Canon independently establishes Borscht's small, low, broad build and Mriya's distinct identity. Accordingly, the left/light-coated speaker is Borscht and the right/dark-coated speaker is Mriya in this reference. The exact correspondence of each semantic turn to an individually addressable Composer block in GD01P remains unresolved. GD1 is documented as Mriya/Borscht canine communication plus Emil's human English dialogue per the supplied production brief.

### GD2 — Mriya / Atlas

1. Atlas: “A Hearth makes dependence.”
2. Mriya: “So does a pack.”
3. Atlas: “A pack has command.”
4. Mriya: “This has return.”
5. Atlas: “Return to what?”
6. Mriya: “A place where leaving is allowed.”

All six are canine direct communication and therefore Pictiq. System notices, if present in the final comic, remain system communication. Semantic wording and speaker order are owner-supplied; per-turn glyph-block boundaries in GD02P are not independently identified.

### GD3 — Pixel / Vale / Irena

1. Pixel: “He is easily influenced.” — Pictiq.
2. Vale: “I participated in quality assurance.” — English; not Pictiq.
3. Pixel: “Defective.” — Pictiq.
4. Irena: “Successful.” — English; not Pictiq.

The former Composer experiments translating Vale or Irena, if retained elsewhere, are `NOT_USED_IN_FINAL_BOOK` and do not override this final convention.

### GD4 — Pixel / Rook / Nika

1. Pixel: “We call it the Bite Key.” — Pictiq.
2. Rook: “It is not a dog tool.” — Pictiq.
3. Nika: “It is not a human tool.” — English; not Pictiq.
4. Rook: “Then whose?” — Pictiq.
5. Pixel: “The valve’s.” — Pictiq.

Any earlier Composer translation of Nika's English line is `NOT_USED_IN_FINAL_BOOK`.

### Source limits

Semantic text above is recorded from the owner's supplied dialogue and the supplied GD1art reference. It is not derived from looking at glyph shapes. Dog identity in GD1 is cross-checked against `GOOD_DOG_ILLUSTRATION_CONTINUITY_AUDIT_V1.md` (GD1 character description) and `GOOD_DOG_VISUAL_CHARACTER_CANON_V1.md` (Mriya/Borscht entries); these older-art review documents inform identification only and do not alter the current case's owner-designated final asset set. The available Composer source sheets are image sheets without stable machine-readable block IDs, explicit per-turn region coordinates, or export metadata. Consequently, the exact Pictiq region for each turn, lexicon-ID sequence, Composer version, and Pictiq version remain `UNRESOLVED`; no visual guess is substituted for those missing records.

## Scope and evidence boundary

- No lexicon entries, relations, grammar, icon, or vocabulary were changed.
- Composer and supplied illustrations were not modified.
- No public-facing case page was created.
- The supplied GD0–GD5 set is treated as the owner-designated final set for this ingest. Rejected intermediate generations were not imported.
- This is a production record, not evidence of reader comprehension, product success, sales, or broad language performance.

## Case-specific workflow observations

This case demonstrates a long-form-fiction production use for Pictiq, with distinct language conventions for canine, human, and system communication. It also exposes a provenance need: each approved semantic turn should travel with a stable Composer block ID, speaker ID/type, semantic source, and final panel-placement reference. This is a workflow observation only; no Composer feature is implemented here.

## Publication update gate

Keep this same case record and update it from `PREPUBLICATION` to `PUBLISHED` only after the owner supplies confirmed live-publication evidence. At that point this record may be extended with the final cover, Kindle and paperback ASINs/ISBN, publication date, Amazon URLs, and final interior provenance. Do not create a duplicate case.

## Related records

- [Asset manifest](GOOD_DOG_BAD_SYSTEM_PICTIQ_ASSET_MANIFEST_V1.json)
- [Dialogue ledger](GOOD_DOG_BAD_SYSTEM_PICTIQ_DIALOGUE_LEDGER_V1.json)
- [Case learning record](GOOD_DOG_BAD_SYSTEM_PICTIQ_LEARNING_V1.md)
- ABVX-OS cross-reference supplied by the owner: `books/rn10-003 — Good Dog, Bad System`. The external workspace was not present in the inspected local project directories, so no local link is asserted and no manuscript was copied.
