# Human-Machine Shared Symbols

> **Status:** HYPOTHESIS / EXPERIMENT CANDIDATE  
> **Added:** 2026-09-09  
> **Source:** [Perplexity ideas harvest](../research/perplexity-ideas-harvest-2026-09.md)

## Core hypothesis

A Pictiq tile may become a dual-readable marker.

Human reading:

- The person recognizes the visible symbol and interprets it through context, grammar, and learned convention.

Machine reading:

- Software detects the canonical frame and silhouette, then resolves the tile to an `icon_id` in the lexicon.

This differs from QR codes and conventional fiducial markers. A QR code is highly machine-readable but semantically opaque to most people. A Pictiq tile could be machine-detectable while still carrying human-readable meaning.

## Why Pictiq is suited to this experiment

Pictiq already has stable IDs, canonical SVGs, a rounded-square tile frame, monochrome rendering, lexicon metadata, phrase/grid layout rules, and notes for computer vision/parsing in [Protocol §6](../../../spec/PROTOCOL.md#notes-for-computer-vision--parsing).

The useful software target is `icon_id`, not inferred meaning from image pixels. Meaning can then be retrieved from the versioned lexicon, aliases, examples, i18n metadata, and current context.

## Possible contexts

- signage;
- packaging;
- printed instructions;
- physical products;
- e-ink displays;
- kiosks;
- human-robot interfaces;
- accessibility and travel aids.

## Required experiment

Do not claim reliable fiducial-marker detection yet. A valid experiment should compare:

- canonical SVG detection;
- raster detection at 64 px and 24 px;
- physical print;
- phone screen;
- shirt/card/luggage-tag surfaces;
- perspective and rotation;
- poor lighting;
- damaged or low-contrast prints.

## Boundaries

This is not a claim that Pictiq already outperforms QR codes, barcodes, AprilTags, ArUco markers, or trained classifiers. The research value is the possible shared human/machine semantic layer.
