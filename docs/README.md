# Docs (GitHub Pages)

This folder is the published GitHub Pages artifact for the static lexicon dictionary (no build step).

Note on negation:
- Primary form is token-based: `X + logic_no`.
- Physical shortcut: users may also draw the diagonal slash with a marker on fabric.

## Enable GitHub Pages

GitHub Pages publishes the `main` branch `/docs` folder in legacy mode. The artifact therefore includes its
own `lexicon/` data and resolves all app assets relative to the site root.

In GitHub:
1. Go to **Settings** -> **Pages**
2. **Build and deployment**: **Deploy from a branch**
3. **Branch**: `main`
4. **Folder**: `/docs`

Then open:
- `https://<user>.github.io/<repo>/`

## Local preview

Browsers block `fetch()` for `file://` pages, so use a simple local server from the repo root:

```bash
python3 -m http.server 8000
```

Open:
- `http://localhost:8000/docs/` (the local path mirrors the published folder)

## Optional i18n

The UI exposes only locales shipped in `docs/lexicon/i18n/` (`en`, `es`, `fr`). If `lexicon/i18n/{lang}.json` exists, it will be loaded and will override
`meaning_en`, `aliases_en`, and (if provided) `tags_en` and `examples` for matching icon ids.

## Composer

The static Composer v0.1 candidate is available at [`composer/`](composer/). It is a human authoring surface for Message v0.1 and uses the browser Renderer for preview/export.
