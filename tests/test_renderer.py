from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pictiq_renderer import RenderOptions, parse_shorthand, render_file, render_message  # noqa: E402
from pictiq_renderer.registry import Registry  # noqa: E402
from pictiq_renderer.validator import normalize_and_validate_message  # noqa: E402


class RendererTests(unittest.TestCase):
    def test_shorthand_normalizes_legacy_ids(self):
        message, diagnostics = parse_shorthand("need_bar\nplace_hotel comm_wifi\n")
        self.assertIsNotNone(message)
        result = render_message(message)
        self.assertEqual(result["message"]["frames"][0]["tokens"][0]["id"], "drink_alcohol")
        self.assertEqual(result["message"]["frames"][1]["tokens"][0]["id"], "place_home")
        warning_types = [d["type"] for d in result["diagnostics"]]
        self.assertEqual(warning_types.count("legacy-id"), 2)
        self.assertFalse(any(d.get("level") == "error" for d in result["diagnostics"]))

    def test_full_entity_and_alias_resolution(self):
        message, diagnostics = parse_shorthand("!context odyssey\n@poseidon entity:polyphemus@odyssey\n")
        self.assertEqual(diagnostics, [])
        self.assertEqual(message["frames"][0]["tokens"][0], {"type": "entity", "id": "entity:poseidon@odyssey"})
        result = render_message(message)
        self.assertIn('data-id="entity:poseidon@odyssey"', result["render"]["svg"])
        self.assertIn('data-id="entity:polyphemus@odyssey"', result["render"]["svg"])

    def test_ambiguous_entity_fails_without_guessing(self):
        registry = Registry()
        registry.entity_aliases = copy.deepcopy(registry.entity_aliases)
        registry.entity_aliases["poseidon"].append("entity:zeus@odyssey")
        message, diagnostics = parse_shorthand("@poseidon\n", registry)
        self.assertIsNone(message)
        self.assertTrue(any(d.type == "ambiguous-entity" and d.level == "error" for d in diagnostics))

    def test_number_and_color_rendering(self):
        message = {
            "schema": "0.1",
            "pictiq": "1.1",
            "frames": [
                {"tokens": [{"type": "number", "value": 50}]},
                {"tokens": [{"type": "icon", "id": "nature_cloud", "params": {"color": "#555555"}}]},
            ],
        }
        result = render_message(message)
        self.assertFalse(any(d.get("level") == "error" for d in result["diagnostics"]))
        svg = result["render"]["svg"]
        self.assertIn('data-id="50"', svg)
        self.assertIn('color="#555555"', svg)

    def test_deferred_move_boat_is_not_silently_migrated(self):
        result = render_message({"schema": "0.1", "pictiq": "1.1", "frames": [{"tokens": [{"type": "icon", "id": "move_boat"}]}]})
        self.assertIsNotNone(result["render"])
        self.assertEqual(result["message"]["frames"][0]["tokens"][0]["id"], "move_boat")
        self.assertIn('data-id="move_boat"', result["render"]["svg"])
        self.assertFalse(any(d.get("type") == "legacy-id" for d in result["diagnostics"]))

    def test_invalid_cases_fail_loudly(self):
        cases = [
            ({"schema": "0.1", "pictiq": "1.1", "frames": [{"tokens": [{"type": "icon", "id": "food_pizza"}]}]}, "unknown-id"),
            ({"schema": "0.1", "pictiq": "1.1", "frames": [{"tokens": [{"type": "number", "value": 120}]}]}, "invalid-number"),
            ({"schema": "0.1", "pictiq": "1.1", "frames": [{"tokens": [{"type": "icon", "id": "nature_cloud", "params": {"color": "grey"}}]}]}, "unsupported-parameter"),
            ({"schema": "0.1", "pictiq": "1.1", "frames": [{"tokens": [[{"type": "icon", "id": "need_water"}]]}]}, "illegal-grouping"),
            ({"schema": "0.1", "pictiq": "1.1", "profile": "tourist", "frames": [{"tokens": [{"type": "icon", "id": "need_water"}]}]}, "profile-mismatch"),
            ({"schema": "0.1", "pictiq": "1.1", "contexts": ["maritime"], "frames": [{"tokens": [{"type": "icon", "id": "need_water"}]}]}, "context-mismatch"),
        ]
        for message, expected in cases:
            with self.subTest(expected=expected):
                normalized, diagnostics = normalize_and_validate_message(message)
                self.assertIsNone(normalized)
                self.assertTrue(any(d.type == expected and d.level == "error" for d in diagnostics), diagnostics)

    def test_profile_context_mismatch_warns_but_renders(self):
        message = {"schema": "0.1", "pictiq": "1.1", "profile": "standalone", "contexts": ["road-wayfinding-v0.1"], "frames": [{"tokens": [{"type": "icon", "id": "person_generic"}]}]}
        result = render_message(message)
        self.assertIsNotNone(result["render"])
        self.assertTrue(any(d["type"] == "context-mismatch" and d["level"] == "warning" for d in result["diagnostics"]))

    def test_embedded_svg_internal_ids_are_prefixed(self):
        result = render_message({"schema": "0.1", "pictiq": "1.1", "frames": [{"tokens": [{"type": "icon", "id": "need_water"}, {"type": "icon", "id": "punct_question"}]}]})
        svg = result["render"]["svg"]
        self.assertIn('id="f0_t0_icon-clip"', svg)
        self.assertIn('id="f0_t1_icon-clip"', svg)
        self.assertIn('clip-path="url(#f0_t0_icon-clip)"', svg)
        self.assertIn('clip-path="url(#f0_t1_icon-clip)"', svg)

    def test_rendering_is_byte_deterministic(self):
        path = ROOT / "examples" / "renderer" / "odyssey-narrative.pictiq"
        first = render_file(path, options=RenderOptions(tile_size=64, token_gap=8, frame_gap=16, padding=16))["render"]["svg"]
        second = render_file(path, options=RenderOptions(tile_size=64, token_gap=8, frame_gap=16, padding=16))["render"]["svg"]
        self.assertEqual(first, second)

    def test_cli_reports_malformed_json_without_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.json"
            bad.write_text("{bad", encoding="utf-8")
            completed = subprocess.run([sys.executable, str(ROOT / "tools" / "pictiq_render.py"), "render", str(bad)], cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(completed.returncode, 1)
            self.assertIn('"type": "malformed-json"', completed.stderr)
            self.assertNotIn("Traceback", completed.stderr)

    def test_cli_normalize_and_render(self):
        with tempfile.TemporaryDirectory() as tmp:
            out_json = Path(tmp) / "message.json"
            out_svg = Path(tmp) / "message.svg"
            subprocess.run([sys.executable, str(ROOT / "tools" / "pictiq_render.py"), "normalize", str(ROOT / "examples" / "renderer" / "legacy-normalization.pictiq"), "--output", str(out_json)], check=True, cwd=ROOT)
            data = json.loads(out_json.read_text())
            self.assertEqual(data["frames"][0]["tokens"][0]["id"], "drink_alcohol")
            subprocess.run([sys.executable, str(ROOT / "tools" / "pictiq_render.py"), "render", str(ROOT / "examples" / "renderer" / "basic-water-question.pictiq"), "--output", str(out_svg)], check=True, cwd=ROOT)
            self.assertIn("<svg", out_svg.read_text())


if __name__ == "__main__":
    unittest.main()
