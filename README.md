# Pictiq

[![CI](https://github.com/markoblogo/pictiq/actions/workflows/ci.yml/badge.svg)](https://github.com/markoblogo/pictiq/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/markoblogo/pictiq)](https://github.com/markoblogo/pictiq/releases)
[![License](https://img.shields.io/github/license/markoblogo/pictiq)](LICENSE)
[![Stars](https://img.shields.io/github/stars/markoblogo/pictiq?style=flat)](https://github.com/markoblogo/pictiq/stargazers)

Pictiq is a minimal visual protocol for short, universal messages across language barriers.
It is not meant for long texts. It is meant for pointing, quick signs, stickers, and simple phrases.

All lexicon words are designed as framed tiles (rounded-square frame). The Pictiq logo is not a tile.

## Core idea
- Zero-intent: pointing at an object tile is a valid message by default (“this / need this / where is this”).
- Meaning is amplified using punctuation tiles and context.
- Negation is expressed as `X + logic_no` (and `logic_no` can be a standalone answer).
- Some nouns may act as actions depending on context (e.g., transport = ride, coins = pay).

## Start here
- Protocol rules (EN): `spec/PROTOCOL.md`
- Icon drawing brief (EN): `spec/ICON_DEFINITIONS.md`
- Protocol rules (RU): `spec/PROTOCOL.ru.md`
- Icon drawing brief (RU): `spec/ICON_DEFINITIONS.ru.md`
- Style spec: `spec/ICON_SPEC.md`
- Grammar spec: `spec/GRAMMAR.md`
- Lexicon registry: `lexicon/icon-index.json`
- Packs: `packs/universal-core.json`, `packs/universal-v1.json`
- Static dictionary site (GitHub Pages): `docs/`

## Repository structure
- `/spec` — protocol rules, grammar, and icon design definitions
- `/lexicon` — icon registry (metadata index + schema)
- `/packs` — curated icon packs (core and extensions)
- `/icons` — canonical SVG icons + exported PNGs
- `/templates` — tile template for icon authoring
- `/tools` — validation and SVG→PNG rendering scripts
- `/docs` — static dictionary site (GitHub Pages-ready)

## Tooling & CI
- `tools/validate_lexicon.py` validates that packs reference existing lexicon IDs and that metadata is well-formed.
- `tools/validate_svg.py` validates canonical SVG rules (viewBox, `currentColor`, etc.).  
  Note: SVG validation may skip if no SVG icons exist yet.
- GitHub Actions runs validation on push and pull requests.

## Licensing (summary)
- Personal use is allowed.
- Non-commercial use is allowed under `LICENSE` (CC BY-NC 4.0).
- Commercial use requires a separate agreement: see `COMMERCIAL_LICENSE.md`.

## Status
Work in progress. The lexicon and packs will grow over time.
