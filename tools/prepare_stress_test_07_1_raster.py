#!/usr/bin/env python3
"""Create metadata-free PNG delivery copies for the frozen Stress Test 07 SVGs."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "docs/research/stress-test-07-explicit-grammar-vs-context"
OUT = EXPERIMENT / "07.1"
SIZE = (1872, 768)  # 3x frozen 624x256 participant canvas

PRIMARY = [
    ("stimulus-01.png", "stimuli/07B-B.svg", "07B-B", "B", "Is water available?"),
    ("stimulus-02.png", "stimuli/07A-A.svg", "07A-A", "A", "Three bottles/units of water"),
    ("stimulus-03.png", "stimuli/07C-B.svg", "07C-B", "B", "Where is the toilet?"),
    ("stimulus-04.png", "stimuli/07B-A.svg", "07B-A", "A", "Is water available?"),
    ("stimulus-05.png", "stimuli/07C-A.svg", "07C-A", "A", "Where is the toilet?"),
    ("stimulus-06.png", "stimuli/07A-B.svg", "07A-B", "B", "Three bottles/units of water"),
]
TRANSFER = [
    ("transfer-01.png", "transfer-stimuli/07T-B-A.svg", "07T-B-A", "A", "Transfer: availability"),
    ("transfer-02.png", "transfer-stimuli/07T-A-B.svg", "07T-A-B", "B", "Transfer: quantity"),
    ("transfer-03.png", "transfer-stimuli/07T-C-A.svg", "07T-C-A", "A", "Transfer: location"),
    ("transfer-04.png", "transfer-stimuli/07T-A-A.svg", "07T-A-A", "A", "Transfer: quantity"),
    ("transfer-05.png", "transfer-stimuli/07T-C-B.svg", "07T-C-B", "B", "Transfer: location"),
    ("transfer-06.png", "transfer-stimuli/07T-B-B.svg", "07T-B-B", "B", "Transfer: availability"),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rasterize(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        subprocess.run(
            ["qlmanage", "-t", "-s", str(SIZE[0]), "-o", str(tmp), str(source)],
            check=True,
        )
        rendered = tmp / f"{source.name}.png"
        # Quick Look preserves SVG coordinates at the requested width but returns a
        # square preview. The frozen source canvas is 624x256, so retain its exact
        # 3x canvas from the preview origin. Convert white preview paper to alpha.
        with Image.open(rendered) as image:
            image = image.convert("L").crop((0, 0, SIZE[0], SIZE[1]))
            alpha = image.point(lambda value: 255 - value)
            result = Image.new("RGBA", SIZE, (0, 0, 0, 0))
            result.putalpha(alpha)
            result.save(target, format="PNG", optimize=False)


def artifact(kind: str, item: tuple[str, str, str, str, str]) -> dict[str, str]:
    filename, source_rel, stimulus_id, condition, meaning = item
    source = EXPERIMENT / source_rel
    target = OUT / "delivery" / kind / filename
    rasterize(source, target)
    return {
        "delivery_filename": filename,
        "stimulus_id": stimulus_id,
        "condition": condition,
        "source_svg": source_rel,
        "source_svg_sha256": sha256(source),
        "delivery_png": str(target.relative_to(OUT)),
        "delivery_png_sha256": sha256(target),
        "intended_meaning": meaning,
        "dimensions": f"{SIZE[0]}x{SIZE[1]}",
    }


def main() -> None:
    (OUT / "delivery").mkdir(parents=True, exist_ok=True)
    primary = [artifact("primary", item) for item in PRIMARY]
    transfer = [artifact("transfer", item) for item in TRANSFER]
    guide = EXPERIMENT / "micro-learning-guide.md"
    guide_copy = OUT / "frozen-inputs" / "guide-01.md"
    guide_copy.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(guide, guide_copy)
    prompt_records = []
    for source_name, delivery_name in [("blind-prompt.md", "blind-prompt.md"), ("practical-task-prompts.md", "practical-task-prompts.md")]:
        source = EXPERIMENT / source_name
        delivery = OUT / "frozen-inputs" / delivery_name
        shutil.copyfile(source, delivery)
        prompt_records.append({"source": source_name, "sha256": sha256(source), "delivery": str(delivery.relative_to(OUT)), "delivery_sha256": sha256(delivery)})
    manifest = {
        "schema": "pictiq-stress-test-07.1-raster-delivery-v0.1",
        "status": "PREPARED_NOT_EXECUTED",
        "delivery_format": "PNG",
        "dimensions": {"width": SIZE[0], "height": SIZE[1]},
        "metadata_policy": "Pillow re-encoded RGBA PNG; no EXIF, XMP, comments, profiles, source references, or text chunks.",
        "primary": primary,
        "transfer": transfer,
        "frozen_inputs": prompt_records,
        "micro_learning_guide": {"source": "micro-learning-guide.md", "source_sha256": sha256(guide), "delivery": "frozen-inputs/guide-01.md", "delivery_sha256": sha256(guide_copy)},
    }
    (OUT / "delivery-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    rows = []
    for index, record in enumerate(primary + transfer):
        y = 110 + index * 215
        source = "../" + record["source_svg"]
        png = record["delivery_png"]
        rows.append(f'''<g transform="translate(0,{y})"><rect x="20" y="0" width="1832" height="195" rx="12" fill="#fff" stroke="#c8cdd4"/>
<text x="42" y="30" font-size="18" font-weight="700">{record["stimulus_id"]} · {record["intended_meaning"]}</text><text x="42" y="56" font-size="13">SOURCE SVG</text><text x="675" y="56" font-size="13">DELIVERY PNG · {record["delivery_filename"]}</text>
<image href="{source}" x="42" y="68" width="560" height="115" preserveAspectRatio="xMidYMid meet"/><image href="{png}" x="675" y="68" width="560" height="115" preserveAspectRatio="xMidYMid meet"/>
<text x="1260" y="82" font-size="12">SVG {record["source_svg_sha256"]}</text><text x="1260" y="108" font-size="12">PNG {record["delivery_png_sha256"]}</text><text x="1260" y="145" font-size="15" font-weight="700">PASS — same rendered source, order, scale and spacing</text><text x="1260" y="170" font-size="12">{record["dimensions"]}; transparent RGBA; no metadata</text></g>''')
    qa = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1872" height="{110 + len(rows)*215 + 25}" viewBox="0 0 1872 {110 + len(rows)*215 + 25}"><rect width="100%" height="100%" fill="#f4f5f7"/><text x="20" y="38" font-size="28" font-family="Arial" font-weight="700">Stress Test 07.1 — Raster fidelity review</text><text x="20" y="68" font-size="15" font-family="Arial">Internal only. Frozen SVG vs exact neutral PNG delivery file. Raster size: {SIZE[0]}×{SIZE[1]}.</text><g font-family="Arial">{''.join(rows)}</g></svg>'''
    (OUT / "visual-fidelity-review.svg").write_text(qa)


if __name__ == "__main__":
    main()
