# K01a — active timetable repair and explicit QA snapshot transfer

Starting HEAD: `0de268141ffdfb183ea66a17edb328aa1a537cae`. Working tree was clean. K01.patch applied to the current files without rollback; the original patch remains unchanged.

## Result

- **K01: ACTIVE REPAIR APPLIED**
- **QA SNAPSHOT MIGRATION: IMPLEMENTED / TESTED**
- **CREATOR BROWSER STATE: NOT ACCESSED**
- **DICTIONARY: PENDING BASELINE APPLICATION**

The pending timetable Message, token_sequence and SVG XML data-id order all match the explicit oracle `move_public + media_text + time + punct_question`. The distinct arrival-time Message stays `move_public + time + punct_question`. No new creator decision, accepted dictionary entry, QA completion or freeze is recorded.

## Known pair — only this transition is permitted

| Binding | Original | Corrected |
| --- | --- | --- |
| Dataset SHA-256 | `088da1591c833f3a0a979bd0d5814bee2ea45ad2ec36ebca7615de6ba13d4f90` | `45c041165ad17f2f8114dddd454ba42f74e9e635eb44606133f291348626f413` |
| Addendum SHA-256 | `24e7793f39790ecb462094503dfbe66d4f129adf2b2b50dcf8b067d2516df686` | `8c5cfda80ee90dea0e185d142249a03e6be83b7ec40f1523f07e74dcd5ed0b51` |

[migration-source.json](migration-source.json) preserves the original dataset/addendum and 21 rendered-asset byte hashes. Its own SHA-256 is pinned in the generator. Its dataset digest and addendum digest are verified. All referenced render bytes were compared to audit revision `f9be7228bf1b4a64ab52dd157e2663add3298d5a` before archiving. The corrected data is compared to that source after excluding only the dataset digest and pending-addendum digest. Stable IDs, complete card records, all Messages/preview references, locked decisions, counters, scope metadata and baseline bindings must therefore be identical. The generator refuses unexpected drift before writing snapshot outputs. The browser repeats the content comparison and verifies all 21 render byte hashes immediately before transfer.

The existing technical-correction provenance points to the audited revision and creator decision revision `277bbb5`. The timetable preview stays byte-identical: SHA-256 `b296064c6a9dd5bbdc4df29b88c2c9eb5a554293d0f4f51cac7b1a54ca78b6f2`.

## Existing viewer, explicit action

The same `review/final-creator-qa-v0.2.html` now:

1. Detects saved work under `pictiq.final-creator-qa.v0.2:<original dataset hash>`, shows its reviewed count and offers **Transfer saved work from previous snapshot**. It also supports **Explicit old-export transfer** for a retained JSON export.
2. Validates the old export against the exact original snapshot, downloads an original export before any target write, verifies unchanged cards and actual preview bytes, transfers records, and validates the result against the corrected snapshot.
3. Preserves decisions, notes (including notes on unreviewed cards) and existing timestamp fields. Unreviewed decisions remain null. `technical_migration` holds old→new dataset/addendum lineage, a canonical-JSON source-export hash and migration timestamp separately from author decisions.
4. Keeps the old key and original file untouched. The new key stores the overlay, migration lineage, preserved source export and exact raw source string together in one storage write. Failure leaves the old source intact. Ordinary edits/export/reload retain timestamp fields and lineage.
5. Refuses a nonempty target rather than merging/overwriting. Both source backups can be downloaded; neither is deleted. Repeating the same already installed transfer returns ALREADY_MIGRATED without rewriting or duplicating decisions.

Ordinary import still rejects old snapshots. Both ordinary and migration validation check full baseline/addendum bindings, type/version, IDs and corpus bindings, duplicates, missing records, decision values/sources, locked choices, note requirements and reviewed/unresolved counters. No arbitrary snapshot replacement or fallback to a different key is implemented. Original creator exports were not modified.

## Verification

`python -m unittest tests.test_composition_dictionary_final_qa_v0_2 tests.test_composition_dictionary_qa_migration_v0_2 -q`: **14 tests PASS**.

Coverage includes the K01 four-ID oracle/schema/canonical-ID/SVG checks; arrival-time/frozen-input preservation; partial progress, notes, timestamps and unreviewed cards; strict old/new validation; wrong snapshots; unknown/duplicate/missing IDs and counters; changed cards, Messages, preview references, locked choices or baseline; nonempty/corrupt target conflict; repeat transfer; failed storage write; original-source preservation; visible old-progress notice; browser-time preview corruption; and preflight refusal before generator writes. The complete generated HTML script is also executed with an isolated DOM/storage fixture: initial old-work notice, explicit transfer, reviewed count, original backup, new export validation and timestamp preservation all pass.

Target generation was repeated and all outputs were byte-identical. `git diff --check`: PASS. Protected source inputs remain unchanged: Dictionary baseline, Corpus, prior v0.1 QA and preview SVG; no Harvest, canonical assets, Grammar, Protocol, Composer, Renderer or Stress Test 07.1 changes.

## Real browser evidence boundary

Browser inventory located the previous in-app viewer tab, whose stored page was a connection-error document. Binding that tab failed under the browser URL policy before any access to its localStorage. A subsequent direct open of the same localhost origin returned ERR_CONNECTION_REFUSED. No real creator state was inspected, exported, modified or migrated. Verification used isolated fixtures only; absence of real decisions is not inferred. The supported compatibility action is available when the owner opens the same origin/profile again. `localhost` and `127.0.0.1`, different ports, and different browser profiles have distinct storage; this pass does not move data between them.

One local K01a commit only. No push, tag or release. No K02 work started.
