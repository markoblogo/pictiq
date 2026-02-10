# Docs (GitHub Pages)

This folder contains a minimal static lexicon dictionary site (no build step).

Note on negation:
- Primary form is token-based: `X + logic_no`.
- Physical shortcut: users may also draw the diagonal slash with a marker on fabric.

## Enable GitHub Pages

Because the site loads data from `../lexicon/icon-index.json`, GitHub Pages must serve the repository root.

In GitHub:
1. Go to **Settings** -> **Pages**
2. **Build and deployment**: **Deploy from a branch**
3. **Branch**: `main`
4. **Folder**: `/ (root)`

Then open:
- `https://<user>.github.io/<repo>/docs/`

## Local preview

Browsers block `fetch()` for `file://` pages, so use a simple local server from the repo root:

```bash
python3 -m http.server 8000
```

Open:
- `http://localhost:8000/docs/`

## Optional i18n

The UI has a language selector. If `lexicon/i18n/{lang}.json` exists, it will be loaded and will override
`meaning_en`, `aliases_en`, and (if provided) `tags_en` and `examples` for matching icon ids.
