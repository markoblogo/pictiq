# Pictiq licensing and “open” terminology audit

**Audit date:** 2026-09-27
**Scope:** Repository wording and license files as currently present. This records the apparent terms; it is not legal advice or a change to those terms.

## Findings

The sole root license file, [`LICENSE`](../../../LICENSE), applies broadly: it says “Pictiq is licensed” under CC BY-NC 4.0 and permits sharing/adapting material for non-commercial purposes with attribution. The repository contains no component-specific software license for Composer, Renderer, source code, or specification, and no separate MIT/BSD/Apache-style license file. On the face of the repository, source code, protocol/specification, icons/artwork, and documentation are all within that broad statement unless a file has independent third-party rights or an explicit exception. Public access to source files does not grant commercial reuse.

CC BY-NC 4.0 permits sharing and adaptation for noncommercial purposes with attribution; its deed says commercial use is not covered by that permission. The [Open Source Definition](https://opensource.org/osd) requires that a license not discriminate against fields of endeavor, including business. Therefore, describing this repository as **“open source” in the recognized open-source software sense is technically inconsistent with the stated CC BY-NC restriction**. This is a repository-terms comparison, not a legal opinion. Sources: [CC BY-NC 4.0 deed](https://creativecommons.org/licenses/by-nc/4.0/), [OSI Open Source Definition](https://opensource.org/osd).

The commercial file is explicitly titled **Draft** and discusses icons and packs; it is not itself a commercial grant. `CONTRIBUTING.md` separately grants maintainers broad rights, including commercial use by the project, over submitted contributions, while third-party use remains noncommercial unless separately agreed. This creates an asymmetry and does not clearly allocate separate terms for every repository component. In particular, Composer and Renderer are not separately governed by an explicit license notice.

## Component matrix

| COMPONENT | CURRENT LICENSE / TERMS | SOURCE | CURRENT WORDING | POSSIBLE AMBIGUITY |
|---|---|---|---|---|
| Source code, including tools, Composer, and Renderer | Root CC BY-NC 4.0 statement; no component-specific software grant found. Commercial reuse is not granted by the root license. | [`LICENSE`](../../../LICENSE); [`README.md`](../../../README.md); no separate code license file | README: personal and non-commercial use; commercial use requires separate agreement. | CC BY-NC is a content license, not a conventional open-source software license. Composer/Renderer have no explicit component-specific license notice; exact software reuse scope could be clearer. |
| Specification / protocol / schemas | Covered by the broad root Pictiq license statement; no separate spec license found. | [`LICENSE`](../../../LICENSE); specs and schema files | Landing/metadata call Pictiq an “open visual language” / “open visual-language protocol.” | “Open” may mean publicly readable or open specification, but can imply permission for unrestricted implementation or reuse. No separate patent, standards, or implementation grant is stated. |
| Icons, artwork, context packs, and other source assets | Root CC BY-NC 4.0; commercial use requires separate written permission according to project notices. | [`LICENSE`](../../../LICENSE); [`COMMERCIAL_LICENSE.md`](../../../COMMERCIAL_LICENSE.md) | Commercial-license draft refers specifically to “icons and packs.” | The root grant is broad, while the draft’s scope is narrower. Individual third-party/brand assets may have additional rights not resolved by the general statement. |
| Documentation, site copy, and research materials | Root CC BY-NC 4.0 statement; `docs/llms.txt` expressly says source assets and documentation are CC BY-NC. | [`LICENSE`](../../../LICENSE); [`docs/llms.txt`](../../llms.txt) | “open visual language”; source assets and documentation CC BY-NC 4.0. | Public documentation and an openly described language do not mean the text/art can be reused commercially. Research evidence also contains attributed third-party material with its own provenance. |
| Handbook / book files | CC BY-NC 4.0 for personal/non-commercial use; commercial use requires a separate agreement. | [`books/handbook-v1/README.md`](../../../books/handbook-v1/README.md); [`releases/handbook-v1.0.0.md`](../../../releases/handbook-v1.0.0.md) | “free” and “open project” are used alongside noncommercial terms. | “Free” describes price/access but can be confused with unrestricted reuse. Handbook terms match the NC restriction. |
| Contributions | Submitter grants maintainers perpetual, worldwide, royalty-free rights to use, modify, and distribute the contribution under project licenses, including commercial usage by the project. Third parties remain under noncommercial terms unless separately licensed. | [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) | Explicit project commercial-use rights for contributions; separate third-party permission required. | Rights differ between project/maintainer and downstream users; relation to future project licenses and scope of “contribution” are not fully elaborated here. |
| Commercial use by third parties | No general commercial grant found; a separate written agreement is required. Draft says maintainer may license selected packs/icons. | [`README.md`](../../../README.md); [`COMMERCIAL_LICENSE.md`](../../../COMMERCIAL_LICENSE.md); [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) | “Commercial use requires a separate agreement.” | The draft is not an executed agreement and does not clearly specify commercial terms for every component, especially code/spec/Composer/Renderer. |

## Wording audit

| Current wording / location | Assessment |
|---|---|
| `Open source` project metric in [`docs/landing/index.html`](../../landing/index.html) and duplicated [`docs/index.html`](../../index.html) | Incorrect or materially misleading if intended to mean open-source software under the OSI definition, because the stated license excludes commercial use. The same wording is present in both landing copies. |
| `open visual language` in landing metadata, first screen, and [`docs/llms.txt`](../../llms.txt) | Ambiguous. It may describe public availability or an openly documented concept, but in proximity to “Open source” it can imply unrestricted reuse. |
| `open visual-language protocol` in landing structured metadata | Ambiguous; “open protocol” can imply open-standard or implementation rights not granted by the repository license. |
| `free as part of the open project` in landing book copy | Ambiguous: “free” can mean no purchase price; “open project” may imply broader reuse. The handbook’s noncommercial condition is elsewhere. |
| README licensing summary | Substantially clearer about noncommercial and commercial use. “Personal use is allowed” is less precise than the license’s noncommercial-purpose wording and could be made consistent in a later owner-approved edit. |
| External archived reviews that call Pictiq “open-source” | Third-party statements, not current licensing notices. Preserve as source evidence; do not treat them as authoritative license declarations. |

## Possible wording for later human decision (not applied)

1. Replace the product metric `Open source` with **“Public repository”** or **“Public source and specification”**, followed nearby by **“CC BY-NC 4.0; commercial use requires separate written permission.”**
2. Replace `open visual language` with **“publicly documented visual language”** or **“publicly documented visual communication protocol.”** Use “open specification” only if the project owner confirms the intended implementation and reuse rights support that phrase.
3. Clarify, after a separate owner decision, whether code, specification, Composer/Renderer, icons/artwork, documentation, and Handbook all share CC BY-NC 4.0 or have component-specific grants. Keep any later change explicit and consistent across the root license, README, site, metadata, and commercial terms.
4. Replace “personal use” with the license’s direct boundary, **“non-commercial use with attribution,”** where that is the intended summary; do not imply that every personal-purpose use is automatically noncommercial.

These are proposals only. No license, README, site, metadata, or product wording was edited in this pass.
