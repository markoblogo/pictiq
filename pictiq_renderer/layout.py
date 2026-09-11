from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LayoutOptions:
    tile_size: int = 64
    token_gap: int = 8
    frame_gap: int = 16
    padding: int = 16
    direction: str = "ltr"


def layout_message(message: dict[str, Any], options: LayoutOptions) -> dict[str, Any]:
    max_tokens = max(len(frame["tokens"]) for frame in message["frames"])
    width = options.padding * 2 + max_tokens * options.tile_size + max(0, max_tokens - 1) * options.token_gap
    height = options.padding * 2 + len(message["frames"]) * options.tile_size + max(0, len(message["frames"]) - 1) * options.frame_gap
    frames = []
    for frame_i, frame in enumerate(message["frames"]):
        y = options.padding + frame_i * (options.tile_size + options.frame_gap)
        token_count = len(frame["tokens"])
        row_width = token_count * options.tile_size + max(0, token_count - 1) * options.token_gap
        if options.direction == "rtl":
            x0 = width - options.padding - row_width
        else:
            x0 = options.padding
        tokens = []
        for token_i, token in enumerate(frame["tokens"]):
            x = x0 + token_i * (options.tile_size + options.token_gap)
            tokens.append({"x": x, "y": y, "width": options.tile_size, "height": options.tile_size, "token": token})
        frames.append({"tokens": tokens})
    return {"width": width, "height": height, "frames": frames}
