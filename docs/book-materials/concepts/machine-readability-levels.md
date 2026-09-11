# Machine Readability Levels

> Status: research framework / architecture vocabulary
> Source event: Pictiq Research Foundations — Batch 02
> Scope: classification only; no scanner, fiducial, barcode, Renderer, or Message Schema change implied.

## Level 1 — Visual

A person can see Pictiq artwork and attempt to interpret it. This says nothing about deterministic machine parsing.

## Level 2 — Semantic-native

A digital artifact directly carries canonical Pictiq semantics through Message JSON, IDs, SVG/HTML metadata, app state, or another structured representation. Machines recover semantics without computer vision.

Pictiq already has important foundations for this level through Message Format, canonical IDs, registries, Renderer output, and parity-tested browser rendering.

## Level 3 — Vision-robust

A camera can recover Pictiq reliably from a physical or visual instance under defined conditions. This requires actual testing, an error model, confidence policy, physical rendering constraints, and a recognition benchmark.

Do not claim Level 3 currently exists.

## Parsing routes

| Route | Use when | Principle |
| --- | --- | --- |
| Semantic-native parsing | Pictiq already exists digitally: web, app, SVG, Message JSON, generated document. | Do not use computer vision when canonical semantics are available. |
| Vision-native parsing | Meaning crosses from physical to digital: printed card, sign, label, camera, object. | Requires scanner/vision research and confidence policy. |
| Linked data | A visible message points to QR, DataMatrix, NFC, URL, beacon, or embedded metadata. | Visible Pictiq remains human-readable; linked data carries exact identity, live state, provenance, detailed values, or authoritative records. |

Pictiq should not be redesigned as a barcode. Linked data is an optional adjacent layer for cases where visible symbols are not enough.

## Future Pictiq Scan Profile hypothesis

A future scan profile could make physical Pictiq more reliably machine-recognizable through fixed geometry, quiet zones, orientation rules, stricter spacing, contrast, silhouette distinguishability, optional machine-verification layers, and confidence/error policy.

This remains long-term, post-Composer physical research. This harvest does not implement fiducials, microcodes, border encodings, QR integration, or physical scanning.
