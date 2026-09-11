from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BrowserRendererParityTests(unittest.TestCase):
    def test_browser_renderer_matches_python_reference(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / 'tools' / 'run_browser_renderer_parity.py')],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        report = json.loads((ROOT / 'docs' / 'research' / 'renderer-parity-spike-01' / 'browser-renderer-parity-report.json').read_text(encoding='utf-8'))
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(len(report['fixtures']), 10)
        self.assertTrue(any(row['fixture_id'] == '06-number-50' and row['numeric_behavior_equal'] for row in report['fixtures']))
        self.assertTrue(any(row['fixture_id'] == '07-color-cloud' and row['color_behavior_equal'] for row in report['fixtures']))
        self.assertTrue(any(row['fixture_id'] == '08-entity-symbols-three' and row['entity_behavior_equal'] for row in report['fixtures']))


if __name__ == '__main__':
    unittest.main()
