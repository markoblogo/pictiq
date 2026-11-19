import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.read_composition import ROOT, DICTIONARY, CORPUS, read_composition

HARVEST = 'docs/research/composition-library-historical-harvest-v0.1'


class CompositionReaderTests(unittest.TestCase):
    def codes(self, result):
        return {d['code'] for d in result['diagnostics']}

    def load(self, relative, root=ROOT):
        return json.loads((root / relative).read_text())

    def fixture(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for relative in (DICTIONARY, CORPUS, HARVEST, 'icons/svg'):
            shutil.copytree(ROOT / relative, root / relative)
        for relative in ('lexicon/icon-index.json', 'entities/entity-index.json', 'notation/numeric/index.json'):
            target = root / relative; target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        return root

    def edit(self, root, relative, mutate):
        data = self.load(relative, root); mutate(data)
        (root / relative).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

    def test_dictionary_exact_messages_variants_and_package_qa(self):
        result = read_composition('dictionary', 'pcd-v01-0006')
        self.assertTrue(result['ok'], result['diagnostics'])
        entry = next(e for e in self.load(DICTIONARY + '/dictionary.json')['entries'] if e['dictionary_entry_id'] == result['id'])
        self.assertEqual(result['baseline_record'], entry)
        self.assertEqual(len(result['baseline_record']['variants']), 4)
        self.assertIn('AWAITING FINAL VISUAL QA', result['package']['declared_status'])
        self.assertIn('FINAL_QA_OUTSTANDING', self.codes(result))
        self.assertEqual(result['subsequent_creator_decisions'], [])
        self.assertEqual(result['linked_corpus_records'][0]['record']['corpus_record_id'], 'clc-v01-0008-r1')
        self.assertTrue(all(r['exists'] for r in result['renders']))
        self.assertTrue(all(t['registered'] and t['asset']['exists'] for t in result['canonical_assets']))

    def test_applied_exclusion_returns_no_dictionary_entry_and_keeps_corpus_evidence(self):
        result = read_composition('dictionary', 'pcd-v01-0025')
        self.assertTrue(result['ok'], result['diagnostics'])
        self.assertIsNone(result['baseline_record'])
        self.assertIsNone(result['baseline_provenance'])
        self.assertEqual(result['record_statuses']['dictionary_projection'], 'CORPUS_ONLY')
        self.assertIn('CORPUS_ONLY_APPLIED', self.codes(result))
        self.assertNotIn('PENDING_CREATOR_DECISION', self.codes(result))
        decision, = result['subsequent_creator_decisions']
        self.assertEqual(decision['action'], 'MOVE_TO_CORPUS_ONLY')
        self.assertEqual(decision['application_status'], 'APPLIED')
        self.assertIn('PENDING', decision['raw_decision']['application_status'])
        self.assertTrue(decision['link_verified'])
        applied, = result['applied_creator_decisions']
        self.assertEqual(applied['application_status'], 'APPLIED')
        self.assertEqual(applied['scope'], 'CORPUS_ONLY_PROJECTION')
        self.assertEqual(applied['application']['removed_entry']['preferred_variant']['token_sequence'], 'rel_here + logic_no')
        corpus = read_composition('corpus', 'clh-v01-0044')
        self.assertTrue(corpus['ok'], corpus['diagnostics'])
        original = next(r for r in self.load(CORPUS + '/accepted-corpus.json')['records'] if r['corpus_record_id'] == 'clh-v01-0044')
        self.assertEqual(corpus['baseline_record'], original)
        self.assertEqual(result['linked_corpus_records'][0]['record'], original)
        self.assertEqual(corpus['record_statuses']['dictionary_projection'], 'CORPUS_ONLY')
        self.assertEqual(corpus['subsequent_creator_decisions'], result['subsequent_creator_decisions'])
        self.assertTrue(all(r['exists'] for r in result['renders']))
        self.assertFalse(any(e['dictionary_entry_id'] == 'pcd-v01-0025' for e in self.load(DICTIONARY + '/dictionary.json')['entries']))

    def test_medical_context_application_keeps_messages_and_qa_separate(self):
        result = read_composition('dictionary', 'pcd-v01-0002')
        self.assertTrue(result['ok'], result['diagnostics'])
        entry = result['baseline_record']
        self.assertIn('including written requests', entry['usage_note'])
        self.assertIn('explicitly pointed to', entry['usage_note'])
        self.assertIn('outside shared visual contact', entry['usage_note'])
        self.assertIn('not a grammatical first-person pronoun', entry['usage_note'])
        self.assertEqual([v['token_sequence'] for v in entry['variants']], [
            'safety_medical + punct_exclaim',
            'person_generic + safety_medical + punct_exclaim'])
        self.assertTrue(all(v['message']['profile'] == 'standalone-core-v0.1'
                            and v['message']['contexts'] == ['universal-core']
                            and v['mode'] == ['STANDALONE'] and v['surface'] == ['OTHER']
                            for v in entry['variants']))
        applied, = result['applied_creator_decisions']
        self.assertEqual(applied['application_status'], 'APPLIED')
        self.assertEqual(applied['scope'], 'CONTEXT_CLARIFICATION_ONLY')
        self.assertEqual(applied['source_decision']['decision'], 'NEEDS_CORRECTION')
        self.assertTrue(applied['link_verified'])
        self.assertIn('AWAITING FINAL VISUAL QA', result['package']['dictionary_qa_status'])
        self.assertIn('FINAL_QA_OUTSTANDING', self.codes(result))
        self.assertEqual(result['subsequent_creator_decisions'], [])

    def test_communication_context_applied_without_reinterpreting_speech_variants(self):
        result = read_composition('dictionary', 'pcd-v01-0006')
        self.assertTrue(result['ok'], result['diagnostics'])
        entry = result['baseline_record']
        self.assertEqual(entry['headword'], 'Less noise, please.')
        self.assertIn('oral, written and social-media messages', entry['usage_note'])
        self.assertIn('Natural sounds such as rain and animal sounds', entry['usage_note'])
        self.assertIn('пиши меньше', entry['usage_note'])
        self.assertIn('comm_sound + qty_minus and comm_sound + rel_down', entry['usage_note'])
        self.assertEqual(entry['variants'][2]['semantic_distinction'],
                         'Noise specifically from shouting or conversation, expressed with SPEECH + LESS.')
        self.assertEqual(entry['variants'][3]['semantic_distinction'],
                         'Noise specifically from shouting or conversation, expressed with SPEECH + DOWN.')
        applied, = result['applied_creator_decisions']
        self.assertEqual(applied['application_status'], 'APPLIED')
        self.assertEqual(applied['source_decision']['decision'], 'NEEDS_CORRECTION')
        self.assertEqual(applied['source_provenance']['selector'], '/records/2')
        self.assertTrue(applied['link_verified'])
        self.assertIn('AWAITING FINAL VISUAL QA', result['package']['dictionary_qa_status'])

    def test_shopping_context_application_preserves_the_existing_food_shop_message(self):
        result = read_composition('dictionary', 'pcd-v01-0009')
        self.assertTrue(result['ok'], result['diagnostics'])
        entry = result['baseline_record']
        self.assertEqual(entry['headword'], 'General food shop')
        self.assertEqual([v['variant_id'] for v in entry['variants']], ['pcd-v01-0009-preferred'])
        variant, = entry['variants']
        self.assertEqual(variant['token_sequence'], 'place_shop + need_food')
        self.assertEqual(variant['message'], {'schema': '0.1', 'pictiq': '1.1', 'frames': [
            {'tokens': [{'type': 'icon', 'id': 'place_shop'}, {'type': 'icon', 'id': 'need_food'}]}]})
        self.assertIn('place_shop denotes the process of shopping', entry['usage_note'])
        self.assertIn('need_food specifies a grocery / food shop or a classic supermarket', entry['usage_note'])
        self.assertIn('specialized meat shop', entry['usage_note'])
        self.assertIn('DIY shop', entry['usage_note'])
        self.assertIn('not a universal rule', entry['context_warnings'][0])
        applied, = result['applied_creator_decisions']
        self.assertEqual(applied['application_status'], 'APPLIED')
        self.assertEqual(applied['source_decision']['decision'], 'NEEDS_CORRECTION')
        self.assertEqual(applied['source_provenance']['selector'], '/records/3')
        self.assertTrue(applied['link_verified'])
        self.assertIn('AWAITING FINAL VISUAL QA', result['package']['dictionary_qa_status'])

    def test_parking_context_applied_without_adding_or_reordering_messages(self):
        result = read_composition('dictionary', 'pcd-v01-0030')
        self.assertTrue(result['ok'], result['diagnostics'])
        entry = result['baseline_record']
        self.assertEqual(entry['headword'], 'No parking')
        self.assertEqual([v['variant_id'] for v in entry['variants']], ['pcd-v01-0030-preferred'])
        variant, = entry['variants']
        self.assertEqual(variant['status'], 'CURRENT_ACCEPTED')
        self.assertEqual(variant['token_sequence'], 'rel_here + logic_no + move_car')
        self.assertEqual([t['id'] for t in variant['message']['frames'][0]['tokens']],
                         ['rel_here', 'logic_no', 'move_car'])
        self.assertEqual(entry['lineage']['source_sequence'], 'rel_here + move_car + logic_no')
        self.assertIn('In writing or on a map', entry['usage_note'])
        self.assertIn('no passage at a passage/road', entry['usage_note'])
        self.assertIn('no parking at a place that may be taken for parking', entry['usage_note'])
        self.assertIn('or both where both situations apply', entry['usage_note'])
        self.assertIn('logic_no + move_car and move_car + logic_no are equivalent', entry['usage_note'])
        self.assertNotIn('preserve the parking-specific reading', ' '.join(entry['context_warnings']))
        self.assertIn('not a general negation-order rule', ' '.join(entry['context_warnings']))
        applied, = result['applied_creator_decisions']
        self.assertEqual(applied['application_status'], 'APPLIED')
        self.assertEqual(applied['source_decision']['decision'], 'NEEDS_CORRECTION')
        self.assertEqual(applied['source_provenance']['selector'], '/records/8')
        self.assertTrue(applied['link_verified'])
        self.assertIn('AWAITING FINAL VISUAL QA', result['package']['dictionary_qa_status'])

    def test_pedestrian_preferred_is_scoped_to_road_sign_and_preserves_three_forms(self):
        result = read_composition('dictionary', 'pcd-v01-0028')
        self.assertTrue(result['ok'], result['diagnostics'])
        entry = result['baseline_record']
        self.assertEqual(entry['headword'], 'Pedestrian movement')
        self.assertEqual(entry['preferred_variant']['token_sequence'], 'move_feet')
        self.assertEqual([v['token_sequence'] for v in entry['variants']], [
            'move_feet', 'person_generic + move_feet', 'person_generic + move_feet + rel_here'])
        self.assertTrue(all(v['status'] == 'CURRENT_ACCEPTED' for v in entry['variants']))
        self.assertEqual(entry['variants'][1]['variant_id'], 'pcd-v01-0028-preferred')
        self.assertEqual(entry['lineage']['source_sequence'], 'person_generic + move_feet + rel_here')
        self.assertEqual(entry['lineage']['preferred_sequence'], 'move_feet')
        self.assertEqual(entry['surface'], ['WAYFINDING'])
        self.assertIn('not a universal preference', entry['usage_note'])
        self.assertIn('does not by itself identify a crossing point', entry['usage_note'])
        self.assertTrue(all('crossing point; drivers yield' not in str(v['context']) for v in entry['variants']))
        applied, = result['applied_creator_decisions']
        self.assertEqual(applied['action'], 'KEEP_ENTRY_CHANGE_PREFERRED')
        self.assertEqual(applied['scope'], 'PREFERRED_VARIANT_CHANGE')
        self.assertEqual(applied['source_provenance']['selector'], '/records/7')
        self.assertTrue(applied['link_verified'])
        self.assertIn('AWAITING FINAL VISUAL QA', result['package']['dictionary_qa_status'])

    def test_application_receipt_cannot_hide_other_edits_or_rebind_source(self):
        from tools.research.medical_context_clarification import RECEIPT
        for change in ('source_selector', 'duplicate_field', 'unrelated_entry', 'medical_message'):
            with self.subTest(change=change):
                root = self.fixture()
                receipt = self.load(DICTIONARY + '/' + RECEIPT, root)
                dictionary = self.load(DICTIONARY + '/dictionary.json', root)
                if change == 'source_selector':
                    receipt['source_decision']['selector'] = '/records/1'
                elif change == 'duplicate_field':
                    receipt['changed_fields'].append(copy.deepcopy(receipt['changed_fields'][0]))
                else:
                    if change == 'unrelated_entry':
                        dictionary['entries'][4]['usage_note'] = 'unapproved change'
                    else:
                        dictionary['entries'][1]['variants'][0]['message']['profile'] = 'embodied-core-v0.1'
                    raw = (json.dumps(dictionary, ensure_ascii=False, indent=2) + '\n').encode()
                    (root / DICTIONARY / 'dictionary.json').write_bytes(raw)
                    receipt['dictionary_after_sha256'] = hashlib.sha256(raw).hexdigest()
                    self.edit(root, DICTIONARY + '/manifest.json',
                              lambda m: m['artifact_sha256'].update({'dictionary.json': receipt['dictionary_after_sha256']}))
                raw = (json.dumps(receipt, ensure_ascii=False, indent=2) + '\n').encode()
                (root / DICTIONARY / RECEIPT).write_bytes(raw)
                self.edit(root, DICTIONARY + '/manifest.json',
                          lambda m: m['context_clarifications'][0].update(sha256=hashlib.sha256(raw).hexdigest()))
                result = read_composition('corpus', 'clh-v01-0044', root)
                self.assertFalse(result['ok'])
                self.assertIn('CONTEXT_CLARIFICATION_MISMATCH', self.codes(result))
                self.assertEqual(result['applied_creator_decisions'], [])
                self.assertFalse(result['subsequent_creator_decisions'][0]['link_verified'])

    def test_application_sequence_accepts_six_steps_and_rejects_intermediate_substitution(self):
        from tools.research.communication_context_clarification import receipt_refs, verify_sequence, encode, verify as verify_communication
        from tools.research.shopping_context_clarification import verify as verify_shopping
        from tools.research.parking_context_clarification import verify as verify_parking
        from tools.research.pedestrian_preferred_application import verify as verify_pedestrian
        from tools.research.corpus_only_application import verify as verify_corpus_only
        manifest = self.load(DICTIONARY + '/manifest.json')
        refs = receipt_refs(manifest)
        receipts = [self.load(DICTIONARY + '/' + ref['path']) for ref in refs]
        raw = (ROOT / DICTIONARY / 'dictionary.json').read_bytes()
        five_steps, _, _ = verify_corpus_only(raw, receipts[5], ROOT)
        four_steps, _, _ = verify_pedestrian(encode(five_steps), receipts[4], ROOT)
        three_steps, _, _ = verify_parking(encode(four_steps), receipts[3], ROOT)
        two_steps, _, _ = verify_shopping(encode(three_steps), receipts[2], ROOT)
        one_step, _, _ = verify_communication(encode(two_steps), receipts[1], ROOT)
        ids = ['pcd-v01-0002', 'pcd-v01-0006', 'pcd-v01-0009', 'pcd-v01-0030', 'pcd-v01-0028', 'pcd-v01-0025']
        for count, state in enumerate((encode(one_step), encode(two_steps), encode(three_steps), encode(four_steps), encode(five_steps), raw), 1):
            original, _, decisions = verify_sequence(state, receipts[:count], ROOT)
            self.assertEqual([d['dictionary_entry_id'] for d in decisions], ids[:count])
            self.assertEqual(hashlib.sha256(encode(original)).hexdigest(), receipts[0]['dictionary_before_sha256'])
        self.assertEqual(receipt_refs({'context_clarification': refs[0]}), refs[:1])
        self.assertEqual(receipt_refs({'context_clarifications': refs[:2]}), refs[:2])
        self.assertEqual(receipt_refs({'context_clarifications': refs[:3]}), refs[:3])
        self.assertEqual(receipt_refs({'context_clarifications': refs[:4]}), refs[:4])
        self.assertEqual(receipt_refs({'context_clarifications': refs[:5]}), refs[:5])
        for i in (1, 2, 3, 4, 5):
            self.assertEqual(receipts[i-1]['dictionary_after_sha256'], receipts[i]['dictionary_before_sha256'])
        for entry_id in ids:
            result = read_composition('dictionary', entry_id)
            self.assertTrue(result['ok'], result['diagnostics'])
            self.assertEqual(result['applied_creator_decisions'][0]['application_status'], 'APPLIED')
        cases = [(change, i) for change in ('gap', 'substituted_intermediate') for i in (1, 2, 3, 4, 5)]
        cases += [(change, None) for change in ('reordered', 'missing_step', 'source_selector', 'duplicate_field')]
        for change, i in cases:
            with self.subTest(change=change, link=i):
                root = self.fixture()
                edited = copy.deepcopy(receipts)
                if change in ('gap', 'substituted_intermediate'):
                    edited[i]['dictionary_before_sha256'] = 'a' * 64
                    if change == 'substituted_intermediate':
                        edited[i-1]['dictionary_after_sha256'] = 'a' * 64
                elif change == 'source_selector':
                    edited[-1]['source_decision']['selector'] = '/records/0'
                elif change == 'duplicate_field':
                    edited[-1]['changed_fields'].append(copy.deepcopy(edited[-1]['changed_fields'][0]))
                if change in ('gap', 'substituted_intermediate', 'source_selector', 'duplicate_field'):
                    for ref, receipt in zip(refs, edited):
                        (root / DICTIONARY / ref['path']).write_bytes(encode(receipt))
                    def rehash(m):
                        for ref in m['context_clarifications']:
                            digest = hashlib.sha256((root / DICTIONARY / ref['path']).read_bytes()).hexdigest()
                            ref['sha256'] = digest
                            m['artifact_sha256'][ref['path']] = digest
                    self.edit(root, DICTIONARY + '/manifest.json', rehash)
                elif change == 'reordered':
                    self.edit(root, DICTIONARY + '/manifest.json', lambda m: m['context_clarifications'].reverse())
                else:
                    self.edit(root, DICTIONARY + '/manifest.json', lambda m: m['context_clarifications'].pop(0))
                result = read_composition('dictionary', 'pcd-v01-0028', root)
                self.assertFalse(result['ok'])
                self.assertIn('CONTEXT_CLARIFICATION_MISMATCH', self.codes(result))
                self.assertEqual(result['applied_creator_decisions'], [])

    def test_historical_corpus_id_render_and_unresolved_token(self):
        original = next(e for e in self.load(CORPUS + '/accepted-corpus.json')['records']
                        if e.get('source_harvest', {}).get('composition_id') == 'clh-v01-0015')
        actual_id = original['corpus_record_id']  # Do not infer Corpus ID from Harvest ID.
        result = read_composition('corpus', actual_id)
        self.assertTrue(result['ok'], result['diagnostics'])
        self.assertEqual(result['baseline_record'], original)
        self.assertEqual(result['baseline_record']['historical_message']['frames'][0]['tokens'][0]['id'], 'place_hotel')
        self.assertIsNone(result['baseline_record']['current_message'])
        hotel, = [t for t in result['canonical_assets'] if t['original_id_or_value'] == 'place_hotel']
        self.assertFalse(hotel['registered']); self.assertIsNone(hotel['asset']['path'])
        self.assertIsNone(hotel['substitution'])
        self.assertTrue(result['renders'][0]['exists'])
        self.assertIn(HARVEST, result['renders'][0]['path'])
        self.assertIn('HISTORICAL_ONLY', self.codes(result))
        self.assertIn('UNRESOLVED_CANONICAL_TOKEN', self.codes(result))

    def test_unknown_id_and_source_cli_no_fallback_and_json_diagnostics(self):
        for source, identity in [('dictionary', 'unknown'), ('dictionary', 'clh-v01-0015'),
                                 ('corpus', 'pcd-v01-0006'), ('invalid', 'pcd-v01-0006')]:
            with self.subTest(source=source, identity=identity):
                result = subprocess.run([sys.executable, str(ROOT / 'tools/read_composition.py'),
                                         '--source', source, '--id', identity], cwd='/tmp', capture_output=True, text=True)
                self.assertEqual(result.returncode, 1)
                data = json.loads(result.stdout)
                self.assertFalse(data['ok']); self.assertIn('READ_FAILED', self.codes(data))
                self.assertNotIn('baseline_record', data)

    def test_incompatible_binding_and_ambiguous_or_inconsistent_decisions(self):
        cases = [
            lambda a: a['source_dictionary_baseline'].update(dictionary_json_sha256='wrong'),
            lambda a: a['source_dictionary_baseline'].update(source_snapshot='wrong'),
            lambda a: a['decisions'].append(copy.deepcopy(a['decisions'][0])),
            lambda a: a['decisions'][0].update(dictionary_entry_id='pcd-v01-0006'),
            lambda a: a['decisions'][0]['current_baseline']['message']['frames'][0]['tokens'].pop(),
        ]
        for mutate in cases:
            with self.subTest(mutate=mutate):
                root = self.fixture()
                self.edit(root, DICTIONARY + '/final-creator-qa-addendum-v0.2.json', mutate)
                result = read_composition('corpus', 'clh-v01-0044', root)
                self.assertFalse(result['ok'])
                self.assertIn('DECISION_LINK_UNRESOLVED', self.codes(result))
                self.assertTrue(all(not d['link_verified'] for d in result['subsequent_creator_decisions']))
                expected = next(e for e in self.load(CORPUS + '/accepted-corpus.json', root)['records'] if e['corpus_record_id'] == 'clh-v01-0044')
                self.assertEqual(result['baseline_record'], expected)

    def test_ambiguous_source_id_is_not_selected(self):
        root = self.fixture()
        self.edit(root, DICTIONARY + '/dictionary.json',
                  lambda d: d['entries'].append(copy.deepcopy(next(e for e in d['entries'] if e['dictionary_entry_id'] == 'pcd-v01-0006'))))
        result = read_composition('dictionary', 'pcd-v01-0006', root)
        self.assertFalse(result['ok'])
        self.assertNotIn('baseline_record', result)
        self.assertIn('Ambiguous', result['diagnostics'][0]['message'])

    def test_missing_assets_reported_without_replacement(self):
        root = self.fixture()
        (root / 'icons/svg/comm_sound.svg').unlink()
        (root / DICTIONARY / 'renders/pcd-v01-0006-preferred.svg').unlink()
        result = read_composition('dictionary', 'pcd-v01-0006', root)
        self.assertIn('MISSING_CANONICAL_ASSET', self.codes(result))
        self.assertIn('MISSING_RENDER', self.codes(result))
        sound = next(t for t in result['canonical_assets'] if t['original_id_or_value'] == 'comm_sound')
        self.assertTrue(sound['registered']); self.assertFalse(sound['asset']['exists'])
        self.assertIsNone(sound['substitution'])

    def test_record_contradiction_preserved_and_reported(self):
        root = self.fixture()
        self.edit(root, DICTIONARY + '/dictionary.json', lambda d: next(e for e in d['entries'] if e['dictionary_entry_id'] == 'pcd-v01-0006')['preferred_variant'].update(token_sequence='wrong'))
        result = read_composition('dictionary', 'pcd-v01-0006', root)
        self.assertFalse(result['ok'])
        self.assertEqual(result['baseline_record']['preferred_variant']['token_sequence'], 'wrong')
        self.assertIn('MESSAGE_SEQUENCE_MISMATCH', self.codes(result))
        self.assertIn('BINDING_MISMATCH', self.codes(result))

    def test_runs_are_read_only_and_file_hashes_and_selectors_are_checkable(self):
        paths = [p for base in (DICTIONARY, CORPUS, HARVEST) for p in (ROOT / base).rglob('*') if p.is_file()]
        paths += [ROOT / p for p in ('lexicon/icon-index.json', 'entities/entity-index.json', 'notation/numeric/index.json')]
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
        for source, identity in [('dictionary', 'pcd-v01-0006'), ('dictionary', 'pcd-v01-0025'), ('corpus', 'clh-v01-0015')]:
            result = read_composition(source, identity)
            self.assertTrue(result['ok'], result['diagnostics'])
            for rel, digest in result['files_sha256'].items():
                self.assertEqual(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest(), digest)
            ref = result['baseline_provenance']
            expected = result['baseline_record']
            if ref is None:
                self.assertIsNone(expected)
                self.assertEqual(result['record_statuses']['dictionary_projection'], 'CORPUS_ONLY')
                linked, = result['linked_corpus_records']
                ref, expected = linked['provenance'], linked['record']
                application, = result['applied_creator_decisions']
                historical = application['application']['removed_entry_provenance']
                self.assertEqual(historical['selector'], '/entries/24')
                self.assertNotEqual(historical['sha256'], result['files_sha256'][historical['path']])
            selected = json.loads((ROOT / ref['path']).read_text())
            for part in ref['selector'].split('/')[1:]: selected = selected[int(part)] if isinstance(selected, list) else selected[part]
            self.assertEqual(selected, expected)
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})


if __name__ == '__main__':
    unittest.main()
