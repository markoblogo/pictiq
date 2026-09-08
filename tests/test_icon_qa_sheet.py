"""Verify evidence fidelity, repeatability and input failures, not recognition."""
import base64
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from make_icon_qa_sheet import ROOT, build_sheet


class QASheetTests(unittest.TestCase):
    def test_representative_icons_are_repeatable_and_preserve_source_bytes(self):
        for icon_id in ('item_cannabis', 'item_cigarette', 'paris_eiffel_tower', 'need_water', 'logic_no'):
            with self.subTest(icon_id=icon_id):
                sheet = build_sheet(icon_id)
                self.assertEqual(sheet, build_sheet(icon_id))
                encoded = re.search(r'src="data:image/svg\+xml;base64,([^"]+)"', sheet)[1]
                self.assertEqual(base64.b64decode(encoded), (ROOT / 'icons/svg' / f'{icon_id}.svg').read_bytes())
                self.assertIn('Not supplied — pending', sheet)

    def test_explicit_neighbors_and_small_size(self):
        sheet = build_sheet('item_cannabis', neighbors=['item_cigarette'], small_px=16)
        self.assertIn('width="16" height="16"', sheet)
        self.assertIn('Grid in reading order: item_cannabis, item_cigarette', sheet)

    def test_rejects_invalid_inputs(self):
        for options in ({'icon_id': '../README'}, {'icon_id': 'need_water', 'small_px': 0},
                        {'icon_id': 'need_water', 'neighbors': ['missing']},
                        {'icon_id': 'need_water', 'neighbors': []}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                build_sheet(**options)

    def test_layout_is_embedded_and_bad_format_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'layout.png'
            data = (ROOT / 'docs/merch/paris-shirt-preview-1200x1600.png').read_bytes()
            path.write_bytes(data)
            sheet = build_sheet('paris_eiffel_tower', layout=path)
            self.assertIn(base64.b64encode(data).decode('ascii'), sheet)
            self.assertNotIn(str(path.parent), sheet)
            path.write_text('not an image')
            with self.assertRaises(ValueError):
                build_sheet('paris_eiffel_tower', layout=path)


if __name__ == '__main__':
    unittest.main()
