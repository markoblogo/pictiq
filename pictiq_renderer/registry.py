from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .diagnostics import Diagnostic

ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


class Registry:
    def __init__(self, root: Path = ROOT):
        self.root = root
        self.lexicon = self._load_json("lexicon/icon-index.json")
        self.compatibility = self._load_json("lexicon/compatibility.json")
        self.entities = self._load_json("entities/entity-index.json")
        self.numeric = self._load_json("notation/numeric/index.json")
        self.profiles = {
            "standalone-core-v0.1": self._load_json("profiles/standalone-core-v0.1.json"),
            "embodied-core-v0.1": self._load_json("profiles/embodied-core-v0.1.json"),
        }
        self.packs = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted((root / "packs").glob("*.json"))}
        self.icon_entries = {entry["id"]: entry for entry in self.lexicon["icons"]}
        self.entity_entries = {entry["id"]: entry for entry in self.entities["symbols"]}
        self.legacy_map = self._build_legacy_map()
        self.entity_aliases = self._build_entity_aliases()
        self.implemented_numbers = {int(entry["value"]): entry for entry in self.numeric.get("implemented_numbers", [])}

    def _load_json(self, rel: str) -> Any:
        return json.loads((self.root / rel).read_text(encoding="utf-8"))

    def _build_legacy_map(self) -> dict[str, str]:
        out: dict[str, str] = {}
        for entry in self.compatibility.get("migrations", []):
            if entry.get("kind") == "SEMANTIC_MIGRATION" and entry.get("preferred_id"):
                out[entry["legacy_id"]] = entry["preferred_id"]
        return out

    def _build_entity_aliases(self) -> dict[str, list[str]]:
        aliases: dict[str, list[str]] = {}
        for entry in self.entities["symbols"]:
            raw = [entry["id"], entry.get("display_name", ""), entry.get("slug", ""), *entry.get("aliases", [])]
            for value in raw:
                key = slugify(value.replace("entity:", "").replace("@", "-"))
                if key:
                    aliases.setdefault(key, [])
                    if entry["id"] not in aliases[key]:
                        aliases[key].append(entry["id"])
        return aliases

    def normalize_icon_id(self, icon_id: str, location: str | None = None) -> tuple[str, list[Diagnostic]]:
        if icon_id in self.legacy_map:
            preferred = self.legacy_map[icon_id]
            return preferred, [Diagnostic("warning", "legacy-id", f"Legacy id '{icon_id}' normalized to '{preferred}'.", icon_id, preferred, location)]
        return icon_id, []

    def resolve_entity_alias(self, alias: str, contexts: list[str], location: str | None = None) -> tuple[str | None, list[Diagnostic]]:
        key = slugify(alias.lstrip("@"))
        candidates = list(self.entity_aliases.get(key, []))
        if not candidates:
            return None, [Diagnostic("error", "unknown-id", f"Unknown entity alias '@{key}'.", alias, None, location)]
        context_filtered = [entity_id for entity_id in candidates if entity_id.rsplit("@", 1)[-1] in contexts]
        if len(context_filtered) == 1:
            return context_filtered[0], []
        if len(candidates) == 1:
            return candidates[0], []
        return None, [Diagnostic("error", "ambiguous-entity", f"Ambiguous entity alias '@{key}'.", alias, None, location)]

    def icon_path(self, icon_id: str) -> Path:
        return self.root / "icons" / "svg" / f"{icon_id}.svg"

    def entity_path(self, entity_id: str) -> Path:
        return self.root / self.entity_entries[entity_id]["icon_path"]

    def number_path(self, value: int) -> Path:
        return self.root / self.implemented_numbers[value]["svg"]

    def profile_ids(self, profile: str) -> set[str]:
        if profile == "standalone":
            profile = "standalone-core-v0.1"
        if profile == "embodied":
            profile = "embodied-core-v0.1"
        data = self.profiles.get(profile)
        return set(data.get("included_ids", [])) if data else set()

    def context_ids(self, context: str) -> set[str]:
        data = self.packs.get(context)
        return set(data.get("icons", [])) if data else set()
