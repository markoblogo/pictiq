# GitHub Pages audit

## Question

Does the deployed dictionary use paths valid for the actual Pages artifact?

## Setup

Inspect Pages configuration, source paths, workflows, and live URLs; then run local artifact and production HTTP smoke checks.

## Result

Pages used legacy `main:/docs`. `../lexicon` and `../books` escaped the published folder. The artifact now carries its own dictionary assets, exposes only `en/es/fr`, and links handbook binaries through raw repository URLs.

## Failures

The original site could load its shell while dictionary and handbook assets returned 404.

## Interpretation

Repository layout and deployed artifact layout must be tested as one system.

## Evidence

[Pages contract](../../README.md), [validator](../../../tools/validate_pages_artifact.py), [repair commit](https://github.com/markoblogo/pictiq/commit/9b0bfc8), [live site](https://markoblogo.github.io/pictiq/).

## Follow-up

Keep the artifact validator in CI; consider a workflow-built Pages artifact only if the deployment model changes.
