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

    def test_pending_exclusion_keeps_baseline_and_creator_decision_separate(self):
        result = read_composition('dictionary', 'pcd-v01-0025')
        self.assertTrue(result['ok'], result['diagnostics'])
        self.assertEqual(result['baseline_record']['preferred_variant']['token_sequence'], 'rel_here + logic_no')
        self.assertEqual(result['baseline_record']['creator_review']['decision'], 'KEEP_IN_DICTIONARY')
        decision, = result['subsequent_creator_decisions']
        self.assertEqual(decision['action'], 'MOVE_TO_CORPUS_ONLY')
        self.assertTrue(decision['link_verified'])
        self.assertIn('PENDING', decision['application_status'])
        self.assertFalse(decision['baseline_mutated_by_reader'])
        self.assertIn('PENDING_CREATOR_DECISION', self.codes(result))
        corpus = read_composition('corpus', 'clh-v01-0044')
        self.assertEqual(corpus['subsequent_creator_decisions'], result['subsequent_creator_decisions'])

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
                result = read_composition('dictionary', 'pcd-v01-0025', root)
                self.assertFalse(result['ok'])
                self.assertIn('DECISION_LINK_UNRESOLVED', self.codes(result))
                self.assertTrue(all(not d['link_verified'] for d in result['subsequent_creator_decisions']))
                expected = next(e for e in self.load(DICTIONARY + '/dictionary.json', root)['entries'] if e['dictionary_entry_id'] == 'pcd-v01-0025')
                self.assertEqual(result['baseline_record'], expected)

    def test_ambiguous_source_id_is_not_selected(self):
        root = self.fixture()
        self.edit(root, DICTIONARY + '/dictionary.json',
                  lambda d: d['entries'].append(copy.deepcopy(next(e for e in d['entries'] if e['dictionary_entry_id'] == 'pcd-v01-0025'))))
        result = read_composition('dictionary', 'pcd-v01-0025', root)
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
            ref = result['baseline_provenance']; selected = json.loads((ROOT / ref['path']).read_text())
            for part in ref['selector'].split('/')[1:]: selected = selected[int(part)] if isinstance(selected, list) else selected[part]
            self.assertEqual(selected, result['baseline_record'])
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})


if __name__ == '__main__':
    unittest.main()
