#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / 'docs' / 'renderer' / 'generated' / 'pictiq-browser-assets.mjs',
    ROOT / 'docs' / 'composer' / 'generated' / 'pictiq-composer-data.mjs',
]


def main() -> int:
    before = {p: p.read_bytes() for p in FILES}
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'generate_browser_renderer_assets.py')], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'generate_composer_data.py')], cwd=ROOT, check=True)
    stale = [str(p.relative_to(ROOT)) for p in FILES if p.read_bytes() != before[p]]
    if stale:
        print('ERROR: generated browser artifacts are stale: ' + ', '.join(stale), file=sys.stderr)
        return 1
    print('OK: generated browser artifacts are fresh')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
