# Emoji Bridge (non-canonical)

This document defines how Pictiq lexicon entries may be mapped to Unicode emoji as a convenience typing layer.

## Purpose

Emoji mappings help users type short Pictiq-like messages when Pictiq tiles are not available. Emoji mappings are NOT canonical and do not override the meanings defined by the Pictiq protocol and icon tiles.

## Strict mapping rule

For each `icon_id`:
- Define exactly **1 primary emoji**.
- Define **0–2 alternative emojis**.
- Never exceed **3 emojis total** (1 primary + max 2 alt).

Rationale: keeping mappings small prevents semantic drift and avoids turning the lexicon into an emoji catalog.

## Selection criteria

Prefer:
- globally recognizable symbols,
- non-branded, non-religious, non-political symbols,
- the emoji that matches the **core meaning** of the Pictiq tile.

Avoid:
- brand-related emoji meanings,
- culture/religion-sensitive symbols (unless explicitly needed),
- emojis whose most common reading conflicts with the Pictiq meaning.

If the best emoji is still ambiguous:
- keep the mapping minimal,
- document the ambiguity (do not add many alternatives).

## Known ambiguous areas (examples)

- `logic_no`: emoji often reads as “forbidden/stop” rather than neutral “no/not/closed/not accepted”.
- `need_water`: emoji may imply tap water rather than bottled water.
- `comm_wifi`: emoji may read as cellular signal rather than Wi-Fi.
- `move_public`: emoji encodes specific modes (bus/train/metro); Pictiq meaning is the general class.

## Canonical meaning reminder

Pictiq canonical meaning is defined by:
- the tile icon,
- the protocol rules (e.g., negation `X + logic_no`),
- examples in the lexicon registry.

Emoji is only a bridge layer and may differ across platforms.
