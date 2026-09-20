# Pictiq Production Site: SEO, LLMO, and Project Discoverability — 2026-09

## Scope

This deployment pass improves factual discoverability for the production site at `https://pictiq.abvx.xyz/`. It does not alter Pictiq vocabulary, grammar, icon artwork, Composer behavior, Lexicon behavior, research conclusions, or landing-page visual design.

## Before

- The production root, Composer, and Lexicon loaded over HTTPS.
- The repository Homepage already pointed to `https://pictiq.abvx.xyz/`.
- Production did not publish `robots.txt`, `sitemap.xml`, or `llms.txt`.
- Composer and Lexicon did not have page-specific description, canonical, social, or structured-data metadata.

## Changes

- Declared production-root canonical URLs for the landing, Composer, and Lexicon; the Pictiq query mode retains the canonical root.
- Added factual Open Graph and Twitter metadata using the existing landscape Handbook promotional artwork.
- Added JSON-LD for the site, project, creator, Handbook, Composer, and Lexicon without claims about ratings, organizations, pricing, or empirical effectiveness.
- Added `robots.txt`, `sitemap.xml`, `llms.txt`, and an SVG favicon.
- Corrected Composer’s “Lexicon” return link to `/lexicon/`.
- Added public-site, Pictiq-mode, Composer, Lexicon, and Handbook links to the repository README.

## After and open work

The public machine-readable surface is the production root, `/composer/`, and `/lexicon/`. Search Console and Bing submission remain optional operator actions; the public sitemap URL is `https://pictiq.abvx.xyz/sitemap.xml`. No new publication milestone is created by this technical discoverability pass; the existing `Can a Visual Language Explain Itself?` status remains unchanged.
