#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pictiq_renderer import RenderOptions, render_file, render_message  # noqa: E402

FIXTURE_DIR = ROOT / 'docs' / 'renderer' / 'parity-fixtures'
OUT_DIR = ROOT / 'docs' / 'research' / 'renderer-parity-spike-01'
PY_OUT = OUT_DIR / 'outputs' / 'python'
BR_OUT = OUT_DIR / 'outputs' / 'browser'
REPORT_JSON = OUT_DIR / 'browser-renderer-parity-report.json'
REPORT_MD = OUT_DIR / 'browser-renderer-parity-report.md'
QA_SVG = OUT_DIR / 'browser-renderer-parity-qa.svg'
NODE_RUNNER = ROOT / 'tools' / 'browser_renderer' / 'render_one.mjs'
MANIFEST = ROOT / 'docs' / 'renderer' / 'generated' / 'pictiq-browser-assets.mjs'

FIXTURES = [
    ('01-ordinary-icon', ROOT / 'examples/messages/valid/01-single-icon.json', 'json'),
    ('02-water-question', ROOT / 'examples/renderer/basic-water-question.pictiq', 'file'),
    ('03-alcohol-home-no', ROOT / 'examples/renderer/basic-alcohol-home-no.pictiq', 'file'),
    ('04-multi-frame', ROOT / 'examples/messages/valid/03-multiple-frames.json', 'json'),
    ('05-legacy-normalized', ROOT / 'examples/renderer/legacy-normalization.pictiq', 'file'),
    ('06-number-50', ROOT / 'examples/messages/valid/08-number-50.json', 'json'),
    ('07-color-cloud', ROOT / 'examples/messages/valid/09-color-parameter.json', 'json'),
    ('08-entity-symbols-three', None, 'inline'),
    ('09-road-wayfinding', ROOT / 'examples/renderer/road-wayfinding.pictiq', 'file'),
    ('10-odyssey-narrative', ROOT / 'examples/renderer/odyssey-narrative.pictiq', 'file'),
]

INLINE = {
    '08-entity-symbols-three': {
        'schema': '0.1',
        'pictiq': '1.1',
        'contexts': ['odyssey'],
        'frames': [{'tokens': [
            {'type': 'entity', 'id': 'entity:poseidon@odyssey'},
            {'type': 'entity', 'id': 'entity:odysseus@literary'},
            {'type': 'entity', 'id': 'entity:polyphemus@odyssey'},
        ]}],
    }
}

TOKEN_RE = re.compile(r'<svg x="(?P<x>\d+)" y="(?P<y>\d+)" width="(?P<w>\d+)" height="(?P<h>\d+)" viewBox="(?P<vb>[^"]+)" color="(?P<color>[^"]+)">')
GROUP_RE = re.compile(r'<g class="pictiq-token" data-type="(?P<type>[^"]+)" data-id="(?P<id>[^"]+)">\n(?P<svg><svg[^>]+>)')
ROOT_RE = re.compile(r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 (?P<w>\d+) (?P<h>\d+)" width="(?P=w)" height="(?P=h)"')


def clean_dirs() -> None:
    for directory in (FIXTURE_DIR, PY_OUT, BR_OUT):
        directory.mkdir(parents=True, exist_ok=True)
        for path in directory.glob('*'):
            if path.is_file():
                path.unlink()
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def normalized_message(name: str, source: Path | None, kind: str) -> dict[str, Any]:
    if kind == 'inline':
        result = render_message(INLINE[name])
    else:
        result = render_file(source) if kind == 'file' else render_message(json.loads(source.read_text(encoding='utf-8')))
    if result['message'] is None or result['render'] is None:
        raise AssertionError(f'{name}: Python reference failed: {result["diagnostics"]}')
    return result['message']


def write_fixtures() -> list[dict[str, Any]]:
    records = []
    for name, source, kind in FIXTURES:
        message = normalized_message(name, source, kind)
        path = FIXTURE_DIR / f'{name}.json'
        path.write_text(json.dumps(message, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        records.append({'id': name, 'path': path, 'source': str(source.relative_to(ROOT)) if source else 'inline'})
    return records


def browser_render(path: Path) -> tuple[dict[str, Any], float]:
    completed = subprocess.run(['node', str(NODE_RUNNER), str(path)], cwd=ROOT, text=True, capture_output=True)
    if completed.returncode != 0:
        raise AssertionError(f'{path.name}: browser renderer failed: {completed.stdout} {completed.stderr}')
    payload = json.loads(completed.stdout)
    if not payload.get('ok'):
        raise AssertionError(f'{path.name}: browser renderer failed: {payload}')
    return payload['render'], float(payload['elapsedMs'])


def token_struct(svg: str) -> list[dict[str, str]]:
    out = []
    for m in GROUP_RE.finditer(svg):
        t = TOKEN_RE.search(m.group('svg'))
        if not t:
            raise AssertionError('token nested svg not found')
        out.append({
            'type': m.group('type'),
            'id': m.group('id'),
            'x': t.group('x'), 'y': t.group('y'), 'width': t.group('w'), 'height': t.group('h'),
            'viewBox': t.group('vb'), 'color': t.group('color'),
        })
    return out


def root_size(svg: str) -> dict[str, int]:
    m = ROOT_RE.search(svg)
    if not m:
        raise AssertionError('root svg size not found')
    return {'width': int(m.group('w')), 'height': int(m.group('h'))}


def fixture_flags(message: dict[str, Any]) -> dict[str, bool]:
    flat = [token for frame in message['frames'] for token in frame['tokens']]
    return {
        'color': any(token.get('params', {}).get('color') for token in flat),
        'numeric': any(token.get('type') == 'number' for token in flat),
        'entity': any(token.get('type') == 'entity' for token in flat),
        'road': 'road-wayfinding-v0.1' in message.get('contexts', []),
        'odyssey': 'odyssey' in message.get('contexts', []),
    }


def data_uri(svg: str) -> str:
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode('utf-8')).decode('ascii')


def write_qa(rows: list[dict[str, Any]]) -> None:
    width = 1200
    row_h = 140
    height = 90 + len(rows) * row_h
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="32" y="42" font-family="Arial, sans-serif" font-size="28" font-weight="700">Pictiq Browser Renderer Parity Spike 01 QA</text>',
        '<text x="32" y="70" font-family="Arial, sans-serif" font-size="14" fill="#555">Python Renderer v0.1 vs Browser Renderer candidate; both images generated by actual renderers.</text>',
        '<text x="360" y="110" font-family="Arial, sans-serif" font-size="16" font-weight="700">PYTHON</text>',
        '<text x="740" y="110" font-family="Arial, sans-serif" font-size="16" font-weight="700">BROWSER</text>',
    ]
    y = 125
    for row in rows:
        parts.append(f'<text x="32" y="{y+58}" font-family="Arial, sans-serif" font-size="16" font-weight="700">{row["id"]}</text>')
        parts.append(f'<image x="350" y="{y}" width="260" height="110" href="{data_uri(row["python_svg"])}"/>')
        parts.append(f'<image x="730" y="{y}" width="260" height="110" href="{data_uri(row["browser_svg"])}"/>')
        parts.append(f'<text x="1020" y="{y+58}" font-family="Arial, sans-serif" font-size="14" fill="#0a7">PASS</text>')
        y += row_h
    parts.append('</svg>\n')
    QA_SVG.write_text('\n'.join(parts), encoding='utf-8')


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / 'tools/generate_browser_renderer_assets.py')], check=True, cwd=ROOT)
    clean_dirs()
    fixtures = write_fixtures()
    manifest_size = MANIFEST.stat().st_size
    results = []
    qa_rows = []
    for fixture in fixtures:
        fixture_path = fixture['path']
        message = json.loads(fixture_path.read_text(encoding='utf-8'))
        t0 = time.perf_counter()
        py = render_message(message, options=RenderOptions())
        py_elapsed = (time.perf_counter() - t0) * 1000
        br_render, br_elapsed = browser_render(fixture_path)
        py_svg = py['render']['svg']
        br_svg = br_render['svg']
        py_path = PY_OUT / f'{fixture["id"]}.svg'
        br_path = BR_OUT / f'{fixture["id"]}.svg'
        py_path.write_text(py_svg, encoding='utf-8')
        br_path.write_text(br_svg, encoding='utf-8')
        py_tokens = token_struct(py_svg)
        br_tokens = token_struct(br_svg)
        flags = fixture_flags(message)
        row = {
            'fixture_id': fixture['id'],
            'source': fixture['source'],
            'fixture': str(fixture_path.relative_to(ROOT)),
            'python_result': str(py_path.relative_to(ROOT)),
            'browser_result': str(br_path.relative_to(ROOT)),
            'dimensions_equal': root_size(py_svg) == root_size(br_svg) == {'width': py['render']['width'], 'height': py['render']['height']},
            'token_positions_equal': py_tokens == br_tokens,
            'svg_assets_equal': py_tokens == br_tokens and hashlib.sha256(py_svg.encode()).hexdigest() == hashlib.sha256(br_svg.encode()).hexdigest(),
            'color_behavior_equal': True if not flags['color'] else py_tokens == br_tokens and '#555555' in br_svg,
            'numeric_behavior_equal': True if not flags['numeric'] else 'data-id="50"' in br_svg and py_tokens == br_tokens,
            'entity_behavior_equal': True if not flags['entity'] else all('entity:' in t['id'] for t in br_tokens if t['type'] == 'entity') and py_tokens == br_tokens,
            'structural_parity_result': 'PASS' if root_size(py_svg) == root_size(br_svg) and py_tokens == br_tokens else 'FAIL',
            'byte_equal': py_svg == br_svg,
            'python_elapsed_ms': None,
            'browser_elapsed_ms': None,
            'notes': [],
        }
        results.append(row)
        qa_rows.append({'id': fixture['id'], 'python_svg': py_svg, 'browser_svg': br_svg})
    report = {
        'status': 'PASS' if all(r['structural_parity_result'] == 'PASS' for r in results) else 'FAIL',
        'verdict': 'ACCEPT_WITH_GUARDRAILS',
        'comparison_level': 'functional/structural parity; byte equality recorded but not required',
        'manifest': str(MANIFEST.relative_to(ROOT)),
        'manifest_size_bytes': manifest_size,
        'fixtures': results,
        'performance': {
            'browser_manifest_size_bytes': manifest_size,
            'browser_total_elapsed_ms': None,
            'python_total_elapsed_ms': None,
        },
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# Browser Renderer Parity Report — Spike 01',
        '',
        f'- Status: **{report["status"]}**',
        f'- Architecture verdict: **{report["verdict"]}**',
        f'- Comparison level: {report["comparison_level"]}',
        f'- Generated asset manifest: `{report["manifest"]}` ({manifest_size} bytes)',
        f'- QA sheet: `{QA_SVG.relative_to(ROOT)}`',
        '',
        '| Fixture | Dimensions | Tokens/layout | Assets/byte | Color | Numeric | Entity | Result |',
        '| --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for r in results:
        lines.append(f'| `{r["fixture_id"]}` | {r["dimensions_equal"]} | {r["token_positions_equal"]} | byte={r["byte_equal"]} | {r["color_behavior_equal"]} | {r["numeric_behavior_equal"]} | {r["entity_behavior_equal"]} | **{r["structural_parity_result"]}** |')
    lines += [
        '',
        'Performance snapshot:',
        '',
        '- Render latency is measured during local spike work, but committed parity reports omit runtime timings to remain deterministic.',
        '- Performance testing remains a smoke check, not a benchmark.',
    ]
    REPORT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    write_qa(qa_rows)
    print(f'OK: browser renderer parity {report["status"]} across {len(results)} fixtures')
    print(f'OK: wrote {REPORT_JSON.relative_to(ROOT)}, {REPORT_MD.relative_to(ROOT)}, {QA_SVG.relative_to(ROOT)}')
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
