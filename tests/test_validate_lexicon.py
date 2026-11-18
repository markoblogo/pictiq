"""Formal schema checks through the existing helper and CLI, using copied inputs."""
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validate_lexicon import validate_lexicon_index

ROOT = Path(__file__).resolve().parents[1]


class LexiconSchemaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'lexicon').mkdir()
        for name in ('icon-index.json', 'icon-index.schema.json'):
            shutil.copyfile(ROOT / 'lexicon' / name, self.root / 'lexicon' / name)
        self.data = json.loads((self.root / 'lexicon/icon-index.json').read_text())

    def write_index(self, data):
        (self.root / 'lexicon/icon-index.json').write_text(json.dumps(data))

    def cli(self, no_site=False):
        (self.root / 'tools').mkdir(exist_ok=True)
        script = self.root / 'tools/validate_lexicon.py'
        shutil.copyfile(ROOT / 'tools/validate_lexicon.py', script)
        args = [sys.executable] + (['-S'] if no_site else []) + [str(script)]
        return subprocess.run(args, cwd=self.root / 'lexicon', text=True, capture_output=True)

    def test_current_index_and_k02_metadata(self):
        entries, errors = validate_lexicon_index(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(entries, self.data['icons'])
        by_id = {e['id']: e for e in entries}
        self.assertEqual(by_id['drink_alcohol']['name'], 'Alcoholic drink')
        self.assertIsInstance(by_id['place_home']['aliases'], list)
        from jsonschema import Draft202012Validator
        Draft202012Validator.check_schema(json.loads((self.root / 'lexicon/icon-index.schema.json').read_text()))

    def test_schema_errors_through_helper_and_cli(self):
        for label, mutate, path in [
            ('version required', lambda d: d.pop('version'), '$:'),
            ('unknown property', lambda d: d['icons'][0].update(unknown_k03=True), '$.icons[0]'),
            ('invalid id', lambda d: d['icons'][0].update(id='Invalid-ID!'), '$.icons[0].id'),
            ('alias item type', lambda d: d['icons'][0].update(aliases_en=[123]), '$.icons[0].aliases_en[0]'),
            ('duplicate id', lambda d: d['icons'].append(copy.deepcopy(d['icons'][0])), 'duplicate id:'),
            ('non-object entry', lambda d: d['icons'].__setitem__(0, None), '$.icons[0]'),
            ('unhashable type', lambda d: d['icons'][0].update(type=[]), '$.icons[0].type'),
        ]:
            with self.subTest(label=label):
                data = copy.deepcopy(self.data); mutate(data); self.write_index(data)
                _, errors = validate_lexicon_index(self.root)
                self.assertTrue(errors)
                self.assertIn(path, '\n'.join(errors))
                result = self.cli()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(path, result.stderr)
                self.assertNotIn('Traceback', result.stderr)

    def test_top_level_and_parse_failures_are_diagnostic(self):
        for data in [None, [], {'icons': None}, {'icons': [None]}]:
            with self.subTest(data=data):
                self.write_index(data)
                self.assertTrue(validate_lexicon_index(self.root)[1])
        (self.root / 'lexicon/icon-index.json').write_text('not json')
        self.assertTrue(validate_lexicon_index(self.root)[1])
        result = self.cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('Traceback', result.stderr)

    def test_missing_invalid_or_unreadable_schema_fails_closed(self):
        schema_path = self.root / 'lexicon/icon-index.schema.json'
        for content in [None, 'not json', '{"$schema":"https://json-schema.org/draft/2020-12/schema","type":42}',
                        '{"$schema":"https://example.invalid/unknown-schema"}']:
            with self.subTest(content=content):
                if schema_path.exists(): schema_path.unlink()
                if content is not None: schema_path.write_text(content)
                _, errors = validate_lexicon_index(self.root)
                self.assertTrue(errors)
                self.assertIn(str(schema_path), errors[0])
                result = self.cli()
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn('Traceback', result.stderr)

    def test_declared_schema_is_the_source_of_constraints(self):
        path = self.root / 'lexicon/icon-index.schema.json'
        schema = json.loads(path.read_text())
        schema['properties']['version']['minLength'] = 100
        path.write_text(json.dumps(schema))
        _, errors = validate_lexicon_index(self.root)
        self.assertTrue(errors)
        self.assertIn('$.version', '\n'.join(errors))

    def test_missing_dependency_is_explicit_not_a_skip(self):
        result = self.cli(no_site=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('JSON Schema validation unavailable', result.stderr)
        self.assertIn('requirements.txt', result.stderr)
        self.assertNotIn('Traceback', result.stderr)

    def test_helper_resolves_schema_from_root_not_cwd(self):
        code = ('import sys;from pathlib import Path;sys.path.insert(0,sys.argv[1]);'
                'from tools.validate_lexicon import validate_lexicon_index;'
                'entries,errors=validate_lexicon_index(Path(sys.argv[2]));'
                'assert entries and not errors,errors')
        result = subprocess.run([sys.executable, '-c', code, str(ROOT), str(self.root)],
                                cwd=self.root / 'lexicon', text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
