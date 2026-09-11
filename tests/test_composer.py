from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ComposerTests(unittest.TestCase):
    def test_composer_core_semantics(self):
        completed = subprocess.run(['node', str(ROOT / 'tests' / 'js' / 'composer-core.test.mjs')], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn('OK: Composer core semantics', completed.stdout)

    def test_generated_browser_artifacts_are_fresh(self):
        completed = subprocess.run([sys.executable, str(ROOT / 'tools' / 'validate_generated_browser_assets.py')], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == '__main__':
    unittest.main()
