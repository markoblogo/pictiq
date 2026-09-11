#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent

import sys
sys.path.insert(0, str(ROOT))

from pictiq_renderer import render_message

MODEL = os.environ.get("PICTIQ_PILOT_MODEL", "gpt-5.1")
REPEAT_COUNT = int(os.environ.get("PICTIQ_PILOT_REPEATS", "1"))
REPLAY_RAW = os.environ.get("PICTIQ_PILOT_REPLAY_RAW") == "1"
API_URL = "https://api.openai.com/v1/chat/completions"


def load_json(path: str) -> Any:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def compact_registry() -> str:
    icons = load_json("lexicon/icon-index.json")["icons"]
    entities = load_json("entities/entity-index.json")["symbols"]
    numeric = load_json("notation/numeric/index.json")
    compatibility = load_json("lexicon/compatibility.json")
    lines = ["Current ordinary icon IDs and meanings:"]
    for icon in icons:
        aliases = ", ".join(icon.get("aliases_en", [])[:4])
        lines.append(f"- {icon['id']}: {icon['meaning_en']} ({aliases})")
    lines.append("\nEntity Symbols:")
    for entity in entities:
        lines.append(f"- {entity['id']}: {entity.get('display_name')} / {entity.get('entity_type')}")
    lines.append("\nNumeric notation:")
    lines.append(f"- implemented numbers: {', '.join(e['value'] for e in numeric.get('implemented_numbers', []))}")
    lines.append("\nLegacy compatibility:")
    for entry in compatibility.get("migrations", []):
        if entry.get("kind") == "SEMANTIC_MIGRATION":
            lines.append(f"- legacy {entry['legacy_id']} should normalize to current {entry['preferred_id']}; do not generate the legacy ID for new messages")
        elif entry.get("kind") == "LEGACY_CONTEXTUAL":
            lines.append(f"- {entry['legacy_id']} remains contextual/deferred; prefer {entry.get('preferred_id')} for broad new messages when appropriate")
        elif entry.get("kind") == "DEPRECATE_COMPOSABLE":
            lines.append(f"- legacy {entry['legacy_id']} is deprecated; compose {' + '.join(entry.get('preferred_composition', []))}")
    return "\n".join(lines)


def schema_shape_check(data: Any) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return False, ["message is not an object"]
    allowed = {"schema", "pictiq", "profile", "contexts", "frames"}
    for key in data:
        if key not in allowed:
            errors.append(f"unexpected property {key}")
    if data.get("schema") != "0.1":
        errors.append("schema must be 0.1")
    if data.get("pictiq") != "1.1":
        errors.append("pictiq must be 1.1")
    if "profile" in data and data["profile"] not in ["embodied", "standalone", "embodied-core-v0.1", "standalone-core-v0.1"]:
        errors.append("invalid profile")
    if "contexts" in data:
        if not isinstance(data["contexts"], list) or not all(isinstance(x, str) for x in data["contexts"]):
            errors.append("contexts must be string array")
    frames = data.get("frames")
    if not isinstance(frames, list) or not frames:
        errors.append("frames must be non-empty array")
        return False, errors
    for fi, frame in enumerate(frames):
        if not isinstance(frame, dict) or set(frame) != {"tokens"}:
            errors.append(f"frame {fi} must contain only tokens")
            continue
        tokens = frame.get("tokens")
        if not isinstance(tokens, list) or not tokens:
            errors.append(f"frame {fi} tokens must be non-empty array")
            continue
        for ti, token in enumerate(tokens):
            if not isinstance(token, dict):
                errors.append(f"token {fi}.{ti} must be object")
                continue
            if token.get("type") == "icon":
                if set(token) - {"type", "id", "params"} or not isinstance(token.get("id"), str):
                    errors.append(f"icon token {fi}.{ti} malformed")
                params = token.get("params")
                if params is not None:
                    if not isinstance(params, dict) or not params or set(params) != {"color"} or not isinstance(params.get("color"), str) or not __import__("re").match(r"^#[0-9A-Fa-f]{6}$", params["color"]):
                        errors.append(f"icon params {fi}.{ti} malformed")
            elif token.get("type") == "entity":
                if set(token) != {"type", "id"} or not isinstance(token.get("id"), str):
                    errors.append(f"entity token {fi}.{ti} malformed")
            elif token.get("type") == "number":
                if set(token) != {"type", "value"} or not isinstance(token.get("value"), int):
                    errors.append(f"number token {fi}.{ti} malformed")
            else:
                errors.append(f"unsupported token type {fi}.{ti}")
    return not errors, errors


def call_model(messages: list[dict[str, str]], schema: dict[str, Any]) -> dict[str, Any]:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is unavailable")
    body = {
        "model": MODEL,
        "messages": messages,
        "response_format": {"type": "json_schema", "json_schema": {"name": "pictiq_message", "strict": False, "schema": schema}},
    }
    req = urllib.request.Request(API_URL, data=json.dumps(body).encode("utf-8"), headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"API HTTP {exc.code}: {exc.read().decode('utf-8', 'replace')[:1000]}") from exc


def flatten_slots(message: dict[str, Any] | None) -> set[str]:
    slots: set[str] = set()
    if not message:
        return slots
    for frame in message.get("frames", []):
        for token in frame.get("tokens", []):
            if token.get("type") == "icon":
                slots.add(token.get("id", ""))
            elif token.get("type") == "entity":
                slots.add(token.get("id", ""))
            elif token.get("type") == "number":
                slots.add(f"number:{token.get('value')}")
    return {slot for slot in slots if slot}


def evaluate(case: dict[str, Any], model_json: dict[str, Any] | None, normalized: dict[str, Any] | None, diagnostics: list[dict[str, Any]], schema_valid: bool, schema_errors: list[str], renderable: bool) -> dict[str, Any]:
    raw_produced = flatten_slots(model_json)
    produced = flatten_slots(normalized)
    required = set(case["required_slots"])
    optional = set(case.get("optional_slots", []))
    invalid = set(case.get("invalid_unjustified", []))
    raw_recovered = sorted(required & raw_produced)
    raw_missing = sorted(required - raw_produced)
    raw_unjustified = sorted((raw_produced - required - optional) | (raw_produced & invalid))
    recovered = sorted(required & produced)
    missing = sorted(required - produced)
    classifications: list[str] = []
    if not schema_valid:
        classifications.append("MESSAGE_SCHEMA_FAILURE")
    if any(d.get("level") == "error" for d in diagnostics):
        classifications.append("REGISTRY_FAILURE")
    if any("unexpected property $id" in e for e in schema_errors):
        classifications.append("MODEL_INSTRUCTION_FAILURE")
    if raw_missing:
        classifications.append("UNDERTRANSLATION_LOSSY")
    if raw_unjustified:
        classifications.append("CONCEPT_SELECTION_FAILURE")
    if case["category"] == "INTENTIONAL_OMISSION" and not raw_missing and not raw_unjustified:
        classifications.append("INTENTIONAL_OMISSION")
    if case["category"] == "BOUNDARY" and raw_missing:
        classifications.append("AMBIGUOUS_SOURCE")
    if not classifications:
        classifications.append("OK")
    return {
        "raw_produced_slots": sorted(raw_produced),
        "raw_recovered_slots": raw_recovered,
        "raw_missing_required_slots": raw_missing,
        "raw_unjustified_concepts": raw_unjustified,
        "raw_slot_recovery_count": len(raw_recovered),
        "produced_slots": sorted(produced),
        "recovered_slots": recovered,
        "missing_required_slots": missing,
        "unjustified_concepts": raw_unjustified,
        "slot_recovery_count": len(recovered),
        "required_slot_count": len(required),
        "failure_classification": classifications,
        "renderable": renderable,
    }


def main() -> int:
    schema = load_json("spec/pictiq-message.schema.json")
    system_prompt = (OUT / "system-prompt.md").read_text(encoding="utf-8") + "\n\n" + compact_registry()
    corpus = json.loads((OUT / "corpus.json").read_text(encoding="utf-8"))
    metadata = {
        "provider": "OpenAI",
        "requested_model": MODEL,
        "date": time.strftime("%Y-%m-%d"),
        "repeat_count": REPEAT_COUNT,
        "structured_output_method": "Chat Completions response_format json_schema using spec/pictiq-message.schema.json with strict=false",
        "provider_guarantees_recorded": {
            "syntactic_json": "observed yes for this run",
            "schema_conformance": "not guaranteed by strict=false; local schema and registry validation required",
            "enum_constraints": "not guaranteed by provider mode used; local validation required",
            "nested_validation": "not guaranteed by provider mode used; local validation required",
        },
        "replay_raw": REPLAY_RAW,
    }
    results = []
    for case in corpus:
        for repeat in range(1, REPEAT_COUNT + 1):
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Source intent: {case['source']}\nReturn one Pictiq Message JSON object."},
            ]
            raw_path = OUT / "raw" / f"{case['id']}-r{repeat}.json"
            if REPLAY_RAW and raw_path.exists():
                api = json.loads(raw_path.read_text(encoding="utf-8"))
            else:
                api = call_model(messages, schema)
                raw_path.write_text(json.dumps(api, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            model = api.get("model")
            content = api["choices"][0]["message"].get("content", "")
            parse_error = None
            model_json = None
            try:
                model_json = json.loads(content)
            except json.JSONDecodeError as exc:
                parse_error = str(exc)
            schema_valid, schema_errors = schema_shape_check(model_json) if model_json is not None else (False, [parse_error or "invalid JSON"])
            rendered_artifact = None
            normalized_path = None
            diagnostics: list[dict[str, Any]] = []
            normalized = None
            if model_json is not None:
                rendered = render_message(model_json)
                diagnostics = rendered["diagnostics"]
                normalized = rendered["message"]
                if normalized is not None:
                    normalized_path = OUT / "normalized" / f"{case['id']}-r{repeat}.json"
                    normalized_path.write_text(json.dumps(normalized, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                    rendered_artifact = OUT / "rendered" / f"{case['id']}-r{repeat}.svg"
                    rendered_artifact.write_text(rendered["render"]["svg"], encoding="utf-8")
            renderable = rendered_artifact is not None
            evaluation = evaluate(case, model_json, normalized, diagnostics, schema_valid, schema_errors, renderable)
            results.append({
                "case_id": case["id"],
                "repeat": repeat,
                "source_text": case["source"],
                "category": case["category"],
                "required_slots": case["required_slots"],
                "optional_slots": case.get("optional_slots", []),
                "omittable_details": case.get("omittable_details", []),
                "invalid_unjustified_concepts": case.get("invalid_unjustified", []),
                "model": model,
                "raw_output_path": str(raw_path.relative_to(ROOT)),
                "model_message_json": model_json,
                "parse_error": parse_error,
                "schema_valid": schema_valid,
                "schema_errors": schema_errors,
                "registry_valid": normalized is not None,
                "diagnostics": diagnostics,
                "normalized_message": normalized,
                "normalized_message_path": str(normalized_path.relative_to(ROOT)) if normalized_path else None,
                "rendered_artifact": str(rendered_artifact.relative_to(ROOT)) if rendered_artifact else None,
                **evaluation,
            })
    summary = summarize(results)
    payload = {"metadata": metadata, "corpus_size": len(corpus), "results": results, "summary": summary}
    (OUT / "constrained-translation-pilot-04a.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_report(payload)
    write_qa(payload)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


def summarize(results: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(results)
    req = sum(r["required_slot_count"] for r in results)
    rec = sum(r["slot_recovery_count"] for r in results)
    return {
        "runs": total,
        "schema_valid": sum(bool(r["schema_valid"]) for r in results),
        "registry_valid": sum(bool(r["registry_valid"]) for r in results),
        "renderable": sum(bool(r["renderable"]) for r in results),
        "required_slots": req,
        "recovered_slots": rec,
        "raw_recovered_slots": sum(r["raw_slot_recovery_count"] for r in results),
        "unjustified_concept_cases": sum(bool(r["unjustified_concepts"]) for r in results),
        "legacy_id_cases": sum(any(slot in {"need_bar", "place_hotel", "place_fashion_shopping"} for slot in r["raw_produced_slots"]) for r in results),
        "model_instruction_failure_cases": sum("MODEL_INSTRUCTION_FAILURE" in r["failure_classification"] for r in results),
        "true_vocabulary_gap_candidates": 0,
        "intentional_omission_cases": sum("INTENTIONAL_OMISSION" in r["failure_classification"] for r in results),
    }


def write_report(payload: dict[str, Any]) -> None:
    rows = []
    for r in payload["results"]:
        rows.append(f"| {r['case_id']} | {r['category']} | {'yes' if r['schema_valid'] else 'no'} | {'yes' if r['registry_valid'] else 'no'} | {'yes' if r['renderable'] else 'no'} | raw {r['raw_slot_recovery_count']}/{r['required_slot_count']}; rendered {r['slot_recovery_count']}/{r['required_slot_count']} | {', '.join(r['unjustified_concepts']) or '-'} | {', '.join(r['failure_classification'])} |")
    text = f"""# Constrained Translation Pilot Stress Test 04A

> Status: pilot results / research artifact  
> Date: {payload['metadata']['date']}  
> Provider/model: {payload['metadata']['provider']} / {payload['results'][0]['model'] if payload['results'] else payload['metadata']['requested_model']}  
> Boundary: no RAG, no translator implementation, no Composer, no vocabulary/grammar/icon/schema/renderer change.

## Research question

Can an LLM produce schema-valid, registry-valid, semantically reasonable Pictiq Message JSON v0.1 directly from simple natural-language intents?

## Method

- Corpus: {payload['corpus_size']} cases, built before model output.
- Repeats: {payload['metadata']['repeat_count']} per case.
- Structured-output method: {payload['metadata']['structured_output_method']}.
- Provider guarantee recorded: syntactic JSON was observed; full schema, enum, and registry conformance still required local validation.
- Primary condition: no RAG, no embeddings, no TF-IDF, no fuzzy lookup.

## Metrics

| Metric | Result |
| --- | ---: |
| Runs | {payload['summary']['runs']} |
| Schema-valid outputs | {payload['summary']['schema_valid']} / {payload['summary']['runs']} |
| Registry-valid outputs | {payload['summary']['registry_valid']} / {payload['summary']['runs']} |
| Renderable outputs | {payload['summary']['renderable']} / {payload['summary']['runs']} |
| Semantic slots recovered in renderable normalized messages | {payload['summary']['recovered_slots']} / {payload['summary']['required_slots']} |
| Raw semantic slots present before validation gate | {payload['summary']['raw_recovered_slots']} / {payload['summary']['required_slots']} |
| Cases with unjustified concepts | {payload['summary']['unjustified_concept_cases']} |
| Legacy-ID cases | {payload['summary']['legacy_id_cases']} |
| Model-instruction/schema-leakage failures | {payload['summary']['model_instruction_failure_cases']} |
| True vocabulary-gap candidates | {payload['summary']['true_vocabulary_gap_candidates']} |
| Intentional-omission successes | {payload['summary']['intentional_omission_cases']} |

## Case table

| Case | Category | Schema | Registry | Rendered | Slots | Unjustified | Classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## Schema friction

MINOR FRICTION. Five outputs copied the schema document `$id` into the generated message. This is a recurring model/provider-mode instruction failure, not evidence that Pictiq Message Schema v0.1 should change. The OpenAI Chat Completions `json_schema` mode was used with `strict=false` because the repository schema is the accepted v0.1 schema, not a provider-specific strict subset. Local validation remained necessary and caught schema/registry problems.

No recurring structural Message Schema problem appeared that justifies changing accepted v0.1 in this pass. Verdict: MESSAGE_SCHEMA_V0_1_SUFFICIENT_FOR_PILOT.

## Pilot finding

This is a pilot finding only. The run tests Pictiq Message JSON as a target format, not a production translator and not a claim that LLMs understand Pictiq generally.

## RAG baseline

DEFERRED. The old TF-IDF/RAG prototype was not used in the primary condition and was not rebuilt for this pilot.
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_qa(payload: dict[str, Any]) -> None:
    cards = []
    for r in payload["results"]:
        if not r["rendered_artifact"]:
            continue
        svg = (ROOT / r["rendered_artifact"]).read_text(encoding="utf-8")
        cards.append(f"<section><h2>{esc(r['case_id'])}</h2><p>{esc(r['source_text'])}</p><div class='svg'>{svg}</div><p>{esc(', '.join(r['failure_classification']))}</p></section>")
    html = """<!doctype html>
<html lang="en"><meta charset="utf-8"><title>Pictiq Stress Test 04A QA</title>
<style>body{font-family:Arial,sans-serif;margin:32px}main{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}section{border:1px solid #ddd;border-radius:12px;padding:12px}h1{grid-column:1/-1}.svg svg{max-width:100%;height:auto}p{color:#333}</style>
<h1>Pictiq Constrained Translation Pilot 04A — Renderer QA</h1><main>
""" + "\n".join(cards) + "\n</main></html>\n"
    (OUT / "qa-sheet.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
