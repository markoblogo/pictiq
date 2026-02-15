# i18n overrides for lexicon

This folder contains optional language-specific overrides for entries from `lexicon/icon-index.json`.

## Purpose

i18n files are partial overlays. They do not duplicate the full lexicon.
Use them to override localized fields for selected IDs:
- `meaning`
- `aliases`
- `tags`
- `examples` (optional)

## File format

One file per language, for example `fr.json`, `es.json`.

```json
{
  "lang": "fr",
  "version": "0.1.0",
  "strings": {
    "need_water": {
      "meaning": "eau",
      "aliases": ["boire", "soif", "eau potable"],
      "tags": ["boisson"]
    }
  }
}
```

Field notes:
- `lang`: BCP-47 style language tag (for example `fr`, `es`, `pt-BR`)
- `strings.<id>.meaning`: localized meaning
- `strings.<id>.aliases`: localized aliases
- `strings.<id>.tags`: localized tags
- `strings.<id>.examples`: optional localized examples

## How docs language selector loads i18n

The static dictionary UI (`docs/app.js`) attempts to load:

- `../lexicon/i18n/{lang}.json`

when a user switches language in the selector.

## Recommendation

Start with partial translations (3–10 high-frequency IDs), then expand iteratively.
