import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs/research/composition-dictionary-baseline-v0.1"
BUILDER = ROOT / "tools/research/build_composition_dictionary_baseline_v0_1.py"


class CompositionDictionaryBaselineTests(unittest.TestCase):
    def test_creator_dispositions_and_protected_decisions(self):
        manifest = json.loads((PACKAGE / "manifest.json").read_text())
        self.assertEqual(manifest["validation"], "PASS")
        self.assertEqual(manifest["counts"]["dictionary_entries"], 64)
        self.assertEqual(manifest["counts"]["render_count"], 71)
        amendment = json.loads((PACKAGE / "creator-review-amendment.json").read_text())
        records = amendment["records"]
        self.assertEqual(len(records), 65)
        self.assertEqual(sum(bool(x["creator_notes"].strip()) for x in records), 10)
        dictionary = json.loads((PACKAGE / "dictionary.json").read_text())
        entries = dictionary["entries"]
        self.assertEqual(len({x["dictionary_entry_id"] for x in entries}), 64)
        self.assertTrue(all(x.get("lineage", {}).get("source_provenance") is not None for x in entries))
        self.assertFalse(any("semantic_examples" in x for x in entries))
        former_review_ids = {"clh-v01-0002", "clh-v01-0007", "clh-v01-0011", "clh-v01-0017", "clh-v01-0022"}
        self.assertTrue(former_review_ids.issubset({x["corpus_refs"][0] for x in entries}))
        for entry in entries:
            for variant in entry["variants"]:
                self.assertTrue((PACKAGE / variant["render"]).is_file())
        followups = json.loads((PACKAGE / "creator-notes-follow-up.json").read_text())
        self.assertEqual(len(followups), 2)

    def test_outputs_are_reproducible(self):
        with tempfile.TemporaryDirectory() as td:
            outputs = []
            for name in ("first", "second"):
                out = Path(td) / name
                out.mkdir()
                shutil.copyfile(PACKAGE / "creator-review-export.json", out / "creator-review-export.json")
                subprocess.run([sys.executable, str(BUILDER), "--output-dir", str(out)], check=True, capture_output=True, text=True)
                outputs.append({p.relative_to(out): hashlib.sha256(p.read_bytes()).hexdigest() for p in out.rglob("*") if p.is_file()})
            self.assertEqual(outputs[0], outputs[1])
            self.assertEqual(outputs[0], {p: hashlib.sha256((PACKAGE / p).read_bytes()).hexdigest()
                                          for p in outputs[0]})

    def test_medical_application_changes_only_explicit_description_fields(self):
        from tools.research.medical_context_clarification import RECEIPT, verify
        from tools.research.communication_context_clarification import RECEIPT as COMMUNICATION_RECEIPT, verify as verify_communication, encode
        from tools.research.shopping_context_clarification import RECEIPT as SHOPPING_RECEIPT, verify as verify_shopping
        from tools.research.parking_context_clarification import RECEIPT as PARKING_RECEIPT, verify as verify_parking
        from tools.research.pedestrian_preferred_application import RECEIPT as PEDESTRIAN_RECEIPT, verify as verify_pedestrian
        from tools.research.corpus_only_application import RECEIPT as CORPUS_ONLY_RECEIPT, verify as verify_corpus_only
        raw = (PACKAGE / 'dictionary.json').read_bytes()
        corpus_only_predecessor, _, _ = verify_corpus_only(raw, json.loads((PACKAGE / CORPUS_ONLY_RECEIPT).read_bytes()), ROOT)
        raw = encode(corpus_only_predecessor)
        pedestrian_predecessor, _, _ = verify_pedestrian(raw, json.loads((PACKAGE / PEDESTRIAN_RECEIPT).read_bytes()), ROOT)
        raw = encode(pedestrian_predecessor)
        parking_predecessor, _, _ = verify_parking(raw, json.loads((PACKAGE / PARKING_RECEIPT).read_bytes()), ROOT)
        raw = encode(parking_predecessor)
        receipt = json.loads((PACKAGE / RECEIPT).read_bytes())
        shopping_predecessor, _, _ = verify_shopping(raw, json.loads((PACKAGE / SHOPPING_RECEIPT).read_bytes()), ROOT)
        current, _, _ = verify_communication(encode(shopping_predecessor), json.loads((PACKAGE / COMMUNICATION_RECEIPT).read_bytes()), ROOT)
        original, _, _ = verify(encode(current), receipt, ROOT)
        allowed = {'semantic_neighbourhood', 'usage_note', 'context_warnings',
                   'preferred_variant/semantic_distinction', 'preferred_variant/variant_context_note',
                   'variants/0/semantic_distinction', 'variants/0/variant_context_note',
                   'variants/1/semantic_distinction', 'variants/1/variant_context_note'}
        self.assertEqual({c['selector'].removeprefix('/entries/1/') for c in receipt['changed_fields']}, allowed)
        for before, after in zip(original['entries'], current['entries']):
            if before['dictionary_entry_id'] != 'pcd-v01-0002':
                self.assertEqual(before, after)
            self.assertEqual(before['preferred_variant']['message'], after['preferred_variant']['message'])
            self.assertEqual(before['lineage'], after['lineage'])
            for old, new in zip(before['variants'], after['variants']):
                for key in ('variant_id', 'variant_type', 'message', 'mode', 'surface', 'context', 'token_sequence', 'render'):
                    self.assertEqual(old[key], new[key])

    def test_communication_application_preserves_medical_and_all_messages(self):
        from tools.research.communication_context_clarification import RECEIPT, verify, encode, BEFORE_SHA
        from tools.research.shopping_context_clarification import RECEIPT as SHOPPING_RECEIPT, verify as verify_shopping
        from tools.research.parking_context_clarification import RECEIPT as PARKING_RECEIPT, verify as verify_parking
        from tools.research.pedestrian_preferred_application import RECEIPT as PEDESTRIAN_RECEIPT, verify as verify_pedestrian
        from tools.research.corpus_only_application import RECEIPT as CORPUS_ONLY_RECEIPT, verify as verify_corpus_only
        raw = (PACKAGE / 'dictionary.json').read_bytes()
        corpus_only_predecessor, _, _ = verify_corpus_only(raw, json.loads((PACKAGE / CORPUS_ONLY_RECEIPT).read_bytes()), ROOT)
        raw = encode(corpus_only_predecessor)
        pedestrian_predecessor, _, _ = verify_pedestrian(raw, json.loads((PACKAGE / PEDESTRIAN_RECEIPT).read_bytes()), ROOT)
        raw = encode(pedestrian_predecessor)
        parking_predecessor, _, _ = verify_parking(raw, json.loads((PACKAGE / PARKING_RECEIPT).read_bytes()), ROOT)
        raw = encode(parking_predecessor)
        receipt = json.loads((PACKAGE / RECEIPT).read_bytes())
        current, _, _ = verify_shopping(raw, json.loads((PACKAGE / SHOPPING_RECEIPT).read_bytes()), ROOT)
        previous, _, _ = verify(encode(current), receipt, ROOT)
        self.assertEqual(hashlib.sha256(encode(previous)).hexdigest(), BEFORE_SHA)
        allowed = {'semantic_neighbourhood', 'usage_note', 'context_warnings',
                   'preferred_variant/semantic_distinction', 'preferred_variant/variant_context_note',
                   'variants/0/semantic_distinction', 'variants/0/variant_context_note',
                   'variants/1/semantic_distinction', 'variants/1/variant_context_note'}
        self.assertEqual({c['selector'].removeprefix('/entries/5/') for c in receipt['changed_fields']}, allowed)
        self.assertEqual(len(previous['entries']), 65)
        for before, after in zip(previous['entries'], current['entries']):
            if before['dictionary_entry_id'] != 'pcd-v01-0006':
                self.assertEqual(before, after)
            else:
                self.assertEqual(before['variants'][2:], after['variants'][2:])
                self.assertEqual([v['token_sequence'] for v in after['variants'][:2]],
                                 ['comm_sound + qty_minus', 'comm_sound + rel_down'])
            self.assertEqual(before['preferred_variant']['message'], after['preferred_variant']['message'])
            for old, new in zip(before['variants'], after['variants']):
                for key in ('variant_id', 'variant_type', 'message', 'mode', 'surface', 'context', 'token_sequence', 'render'):
                    self.assertEqual(old[key], new[key])
        manifest = json.loads((PACKAGE / 'manifest.json').read_bytes())
        self.assertEqual(manifest['counts']['entries_with_context_warnings'],
                         sum(bool(e['context_warnings']) for e in json.loads((PACKAGE / 'dictionary.json').read_bytes())['entries']))

    def test_shopping_application_changes_only_seven_descriptive_fields(self):
        from tools.research.shopping_context_clarification import RECEIPT, verify, encode, BEFORE_SHA
        from tools.research.parking_context_clarification import RECEIPT as PARKING_RECEIPT, verify as verify_parking
        from tools.research.pedestrian_preferred_application import RECEIPT as PEDESTRIAN_RECEIPT, verify as verify_pedestrian
        from tools.research.corpus_only_application import RECEIPT as CORPUS_ONLY_RECEIPT, verify as verify_corpus_only
        raw = (PACKAGE / 'dictionary.json').read_bytes()
        corpus_only_predecessor, _, _ = verify_corpus_only(raw, json.loads((PACKAGE / CORPUS_ONLY_RECEIPT).read_bytes()), ROOT)
        raw = encode(corpus_only_predecessor)
        pedestrian_predecessor, _, _ = verify_pedestrian(raw, json.loads((PACKAGE / PEDESTRIAN_RECEIPT).read_bytes()), ROOT)
        raw = encode(pedestrian_predecessor)
        parking_predecessor, _, _ = verify_parking(raw, json.loads((PACKAGE / PARKING_RECEIPT).read_bytes()), ROOT)
        raw = encode(parking_predecessor)
        receipt = json.loads((PACKAGE / RECEIPT).read_bytes())
        previous, _, _ = verify(raw, receipt, ROOT)
        self.assertEqual(hashlib.sha256(encode(previous)).hexdigest(), BEFORE_SHA)
        current = json.loads(raw)
        allowed = {'semantic_neighbourhood', 'usage_note', 'context_warnings',
                   'preferred_variant/semantic_distinction', 'preferred_variant/variant_context_note',
                   'variants/0/semantic_distinction', 'variants/0/variant_context_note'}
        self.assertEqual({c['selector'].removeprefix('/entries/8/') for c in receipt['changed_fields']}, allowed)
        self.assertEqual(len(previous['entries']), 65)
        for before, after in zip(previous['entries'], current['entries']):
            if before['dictionary_entry_id'] != 'pcd-v01-0009':
                self.assertEqual(before, after)
            else:
                self.assertEqual(before['headword'], after['headword'])
                self.assertEqual(before['lineage'], after['lineage'])
                self.assertEqual(before['preferred_variant']['message'], after['preferred_variant']['message'])
                for old, new in zip(before['variants'], after['variants']):
                    for key in ('variant_id', 'variant_type', 'message', 'mode', 'surface', 'context', 'token_sequence', 'render'):
                        self.assertEqual(old[key], new[key])
        # Both earlier receipts remain exactly reproducible, including intermediate hashes.
        for name in ('pcd-v01-0002-context.json', 'pcd-v01-0006-context.json'):
            rel = 'docs/research/composition-dictionary-baseline-v0.1/applied-decisions/' + name
            old = subprocess.run(['git', 'show', '39bf2d3:' + rel], cwd=ROOT, capture_output=True, check=True).stdout
            self.assertEqual((ROOT / rel).read_bytes(), old)


    def test_parking_application_preserves_previous_entries_messages_and_pending_work(self):
        from tools.research.parking_context_clarification import RECEIPT, verify, encode, BEFORE_SHA
        from tools.research.pedestrian_preferred_application import RECEIPT as PEDESTRIAN_RECEIPT, verify as verify_pedestrian
        from tools.research.corpus_only_application import RECEIPT as CORPUS_ONLY_RECEIPT, verify as verify_corpus_only
        raw = (PACKAGE / 'dictionary.json').read_bytes()
        corpus_only_predecessor, _, _ = verify_corpus_only(raw, json.loads((PACKAGE / CORPUS_ONLY_RECEIPT).read_bytes()), ROOT)
        raw = encode(corpus_only_predecessor)
        pedestrian_predecessor, _, _ = verify_pedestrian(raw, json.loads((PACKAGE / PEDESTRIAN_RECEIPT).read_bytes()), ROOT)
        raw = encode(pedestrian_predecessor)
        receipt = json.loads((PACKAGE / RECEIPT).read_bytes())
        previous, _, _ = verify(raw, receipt, ROOT)
        self.assertEqual(hashlib.sha256(encode(previous)).hexdigest(), BEFORE_SHA)
        current = json.loads(raw)
        allowed = {'semantic_neighbourhood', 'usage_note', 'known_ambiguity', 'context_warnings',
                   'preferred_variant/semantic_distinction', 'preferred_variant/variant_context_note',
                   'variants/0/semantic_distinction', 'variants/0/variant_context_note'}
        self.assertEqual({c['selector'].removeprefix('/entries/29/') for c in receipt['changed_fields']}, allowed)
        self.assertEqual(len(previous['entries']), 65)
        for before, after in zip(previous['entries'], current['entries']):
            if before['dictionary_entry_id'] != 'pcd-v01-0030':
                self.assertEqual(before, after)
            else:
                self.assertEqual(before['headword'], after['headword'])
                self.assertEqual(before['lineage'], after['lineage'])
                # All other variant metadata, including status and exact Messages, stays intact.
                for old, new in zip([before['preferred_variant'], *before['variants']],
                                    [after['preferred_variant'], *after['variants']]):
                    self.assertEqual({k: v for k, v in old.items() if k not in ('semantic_distinction', 'variant_context_note')},
                                     {k: v for k, v in new.items() if k not in ('semantic_distinction', 'variant_context_note')})
        for entry_id in ('0002', '0006', '0009'):
            rel = f'docs/research/composition-dictionary-baseline-v0.1/applied-decisions/pcd-v01-{entry_id}-context.json'
            old = subprocess.run(['git', 'show', '044bb69:' + rel], cwd=ROOT, capture_output=True, check=True).stdout
            self.assertEqual((ROOT / rel).read_bytes(), old)
        addendum = json.loads((PACKAGE / 'final-creator-qa-addendum-v0.2.json').read_bytes())
        timetable, = [d['new_related_entry'] for d in addendum['decisions'] if 'new_related_entry' in d]
        self.assertEqual(timetable['status'], 'CREATOR-APPROVED / PENDING BASELINE APPLICATION')
        self.assertEqual(timetable['temporary_qa_id'], 'qa-new-public-transport-timetable')
        self.assertFalse(any(e['preferred_variant']['token_sequence'] == 'move_public + media_text + time + punct_question'
                             for e in current['entries']))


    def test_pedestrian_application_preserves_history_and_renders_all_three_exact_forms(self):
        from tools.research.pedestrian_preferred_application import RECEIPT, verify, encode, BEFORE_SHA, CORPUS
        from tools.validate_message_schema import schema_errors, semantic_errors
        from pictiq_renderer.svg_renderer import render_svg
        import xml.etree.ElementTree as ET
        from tools.research.corpus_only_application import RECEIPT as CORPUS_ONLY_RECEIPT, verify as verify_corpus_only
        raw = (PACKAGE / 'dictionary.json').read_bytes()
        corpus_only_predecessor, _, _ = verify_corpus_only(raw, json.loads((PACKAGE / CORPUS_ONLY_RECEIPT).read_bytes()), ROOT)
        raw = encode(corpus_only_predecessor)
        receipt = json.loads((PACKAGE / RECEIPT).read_bytes())
        previous, _, _ = verify(raw, receipt, ROOT)
        self.assertEqual(hashlib.sha256(encode(previous)).hexdigest(), BEFORE_SHA)
        current = json.loads(raw)
        self.assertEqual(len(current['entries']), 65)
        for before, after in zip(previous['entries'], current['entries']):
            if before['dictionary_entry_id'] != 'pcd-v01-0028':
                self.assertEqual(before, after)
        entry = current['entries'][27]
        before = previous['entries'][27]
        self.assertEqual(entry['lineage']['source_message'], before['lineage']['source_message'])
        self.assertEqual(entry['variants'][1]['message'], before['preferred_variant']['message'])
        self.assertEqual(entry['variants'][1]['render'], before['preferred_variant']['render'])
        corpus = json.loads((ROOT / CORPUS).read_bytes())
        original, = [r for r in corpus['records'] if r['corpus_record_id'] == 'clh-v01-0047']
        self.assertEqual(entry['variants'][2]['message'], original['historical_message'])
        sequences = [['move_feet'], ['person_generic', 'move_feet'], ['person_generic', 'move_feet', 'rel_here']]
        for variant, ids in zip(entry['variants'], sequences):
            self.assertEqual(schema_errors(variant['message']) + semantic_errors(variant['message']), [])
            svg, _ = render_svg(variant['message'])
            self.assertEqual((PACKAGE / variant['render']).read_text(), svg)
            self.assertEqual([node.attrib['data-id'] for node in ET.fromstring(svg).iter() if 'data-id' in node.attrib], ids)
        self.assertEqual(receipt['messages_before_after']['preferred_before'], before['preferred_variant']['message'])
        self.assertEqual(receipt['messages_before_after']['preferred_after'], entry['preferred_variant']['message'])
        self.assertEqual(receipt['preference_context']['surface'], ['WAYFINDING'])
        self.assertFalse(receipt['preference_context']['universal_preference'])
        self.assertEqual(len(receipt['variant_lineage']), 3)
        # Reject even a rehashed attempt to change the author-selected Message.
        forged = json.loads(raw)
        forged['entries'][27]['preferred_variant']['message']['frames'][0]['tokens'].append({'type': 'icon', 'id': 'rel_here'})
        fake_receipt = json.loads(encode(receipt))
        fake_receipt['dictionary_after_sha256'] = hashlib.sha256(encode(forged)).hexdigest()
        with self.assertRaises(ValueError):
            verify(encode(forged), fake_receipt, ROOT)
        for name in ('pcd-v01-0002-context.json', 'pcd-v01-0006-context.json',
                     'pcd-v01-0009-context.json', 'pcd-v01-0030-context.json'):
            rel = 'docs/research/composition-dictionary-baseline-v0.1/applied-decisions/' + name
            frozen = subprocess.run(['git', 'show', 'e95b798:' + rel], cwd=ROOT, capture_output=True, check=True).stdout
            self.assertEqual((ROOT / rel).read_bytes(), frozen)
        for variant in before['variants']:
            rel = 'docs/research/composition-dictionary-baseline-v0.1/' + variant['render']
            frozen = subprocess.run(['git', 'show', 'e95b798:' + rel], cwd=ROOT, capture_output=True, check=True).stdout
            self.assertEqual((ROOT / rel).read_bytes(), frozen)
        lineage = json.loads((PACKAGE / 'lineage.json').read_bytes())
        self.assertEqual([r for r in lineage['records'] if r['dictionary_entry_id'] == entry['dictionary_entry_id']],
                         [entry['lineage']])


    def test_corpus_only_removal_is_exact_and_preserves_all_prior_versions(self):
        from tools.research.corpus_only_application import RECEIPT, verify, encode, BEFORE_SHA, CORPUS, CORPUS_SHA
        raw = (PACKAGE / 'dictionary.json').read_bytes()
        receipt = json.loads((PACKAGE / RECEIPT).read_bytes())
        previous, _, decision = verify(raw, receipt, ROOT)
        self.assertEqual(hashlib.sha256(encode(previous)).hexdigest(), BEFORE_SHA)
        self.assertEqual(decision['decision'], 'MOVE_TO_CORPUS_ONLY')
        self.assertEqual(decision['creator_note'], '')
        current = json.loads(raw)
        self.assertEqual(len(previous['entries']), 65)
        self.assertEqual(len(current['entries']), 64)
        remaining = [e for e in previous['entries'] if e['dictionary_entry_id'] != 'pcd-v01-0025']
        self.assertEqual(current['entries'], remaining)
        self.assertEqual(receipt['removed_entry'], previous['entries'][24])
        self.assertEqual(receipt['changed_fields'][0]['selector'], '/entries/24')
        self.assertEqual(receipt['removed_entry']['preferred_variant']['token_sequence'], 'rel_here + logic_no')
        corpus = (ROOT / CORPUS).read_bytes()
        self.assertEqual(hashlib.sha256(corpus).hexdigest(), CORPUS_SHA)
        preserved = json.loads(corpus)['records'][43]
        self.assertEqual(preserved['corpus_record_id'], 'clh-v01-0044')
        self.assertEqual(preserved['current_message'], receipt['removed_entry']['preferred_variant']['message'])
        self.assertEqual(receipt['preserved_corpus']['selector'], '/records/43')
        svg = ROOT / receipt['preserved_render']['path']
        self.assertEqual(hashlib.sha256(svg.read_bytes()).hexdigest(), receipt['preserved_render']['sha256'])
        manifest = json.loads((PACKAGE / 'manifest.json').read_bytes())
        for ref in manifest['context_clarifications'][:-1]:
            rel = 'docs/research/composition-dictionary-baseline-v0.1/' + ref['path']
            frozen = subprocess.run(['git', 'show', 'c21b0d9:' + rel], cwd=ROOT, capture_output=True, check=True).stdout
            self.assertEqual((ROOT / rel).read_bytes(), frozen)
        # Historical selectors belong to their exact earlier Dictionary hashes.
        pedestrian = json.loads((PACKAGE / 'applied-decisions/pcd-v01-0028-preferred.json').read_bytes())
        self.assertEqual(pedestrian['changed_fields'][0]['selector'], '/entries/27/semantic_neighbourhood')
        active_pedestrian = next(e for e in current['entries'] if e['dictionary_entry_id'] == 'pcd-v01-0028')
        self.assertEqual(current['entries'].index(active_pedestrian), 26)
        self.assertEqual(active_pedestrian['preferred_variant']['token_sequence'], 'move_feet')
        # A forged insertion position or removed record cannot rebind history.
        for change in ('index', 'removed_message'):
            fake = json.loads(encode(receipt))
            if change == 'index':
                fake['changed_fields'][0]['selector'] = '/entries/25'
            else:
                fake['removed_entry']['preferred_variant']['message']['frames'][0]['tokens'].pop()
            with self.assertRaises(ValueError):
                verify(raw, fake, ROOT)


if __name__ == "__main__":
    unittest.main()
