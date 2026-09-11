from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Diagnostic:
    level: str
    type: str
    message: str
    input: str | None = None
    normalizedTo: str | None = None
    location: str | None = None

    def to_dict(self) -> dict[str, str]:
        return {k: v for k, v in asdict(self).items() if v is not None}
