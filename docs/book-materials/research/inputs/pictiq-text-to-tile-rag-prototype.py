"""
Pictiq RAG prototype: text -> tile sequence
=============================================

Architecture (4 stages):

  Stage A - NORMALIZE & SEGMENT (rule-based stand-in for an LLM call in production)
      Free text in any language -> {
          "content_query": <English gloss of the open-class concept, e.g. "toilet">,
          "quantity": int | "many" | None,
          "negation": bool,
          "urgent": bool,
          "question": bool,
      }
      Rationale: Pictiq's own grammar (spec/GRAMMAR.md) splits tokens into
      OPERATORS (closed, enumerable: quantity, logic_yes/no, punctuation) and
      OBJECTS (open-class: needs/places/items/...). Closed classes don't need
      ML - a handful of regexes cover them reliably in any language. Open-class
      concepts are the hard part and get routed to retrieval (Stage B).
      In production, Stage A is a single LLM call constrained to a JSON Schema
      (ties directly into the constrained-decoding approach discussed earlier),
      so it works for arbitrary phrasing/language instead of the small demo
      dictionary used below.

  Stage B - RETRIEVE (real, runnable)
      TF-IDF vector search over a corpus built from lexicon/icon-index.json:
      each content icon (needs/places/items/money/movement/...) becomes one
      document made of its id + meaning_en + aliases_en (weighted) + tags_en.
      Cosine similarity ranks candidate tile ids for the extracted concept.
      This is the actual "RAG" retrieval step and needs no external API -
      works fully offline on the existing repo data.

  Stage C - COMPOSE (real, runnable)
      Reassembles the retrieved content tile + detected operators into a
      tile sequence following spec/GRAMMAR.md ordering rules:
        object/place  ->  compound qualifier (if any)  ->  quantity  ->  negation  ->  punctuation (last)

  Stage D - VALIDATE / FALLBACK (real, runnable)
      If the best retrieval score is below a confidence threshold, the tile
      is NOT forced into the output. Instead the system flags the phrase as
      a gap and points to spec/STANDALONE_BACKLOG.md's decision tree - i.e.
      "no confident icon exists yet" becomes a structured signal for content
      design, not a wrong guess.
"""

import json
import re
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

LEXICON_PATH = Path("/home/user/workspace/pictiq/lexicon/icon-index.json")
OPERATOR_CATEGORIES = {"quantity", "logic", "punctuation"}
CONFIDENCE_THRESHOLD = 0.18

# ---------------------------------------------------------------------------
# Stage B setup: load lexicon, build TF-IDF index over content (non-operator) icons
# ---------------------------------------------------------------------------

def load_lexicon():
    data = json.loads(LEXICON_PATH.read_text())
    return data["icons"]


def icon_document(icon):
    weight_aliases = icon.get("aliases_en", []) * 3  # aliases are the strongest signal
    tags = icon.get("tags_en", [])
    id_words = icon["id"].replace("_", " ")
    parts = [icon["meaning_en"], id_words] + weight_aliases + tags
    return " ".join(parts).lower()


def build_index(icons):
    content_icons = [i for i in icons if i["category"] not in OPERATOR_CATEGORIES]
    corpus = [icon_document(i) for i in content_icons]
    # char n-grams (not word n-grams) so plurals/typos/inflections still match
    # aliases without needing a stemmer - e.g. "beers" still hits "beer".
    vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)
    matrix = vectorizer.fit_transform(corpus)
    return content_icons, vectorizer, matrix


def retrieve(query, content_icons, vectorizer, matrix, k=3):
    qv = vectorizer.transform([query.lower()])
    sims = cosine_similarity(qv, matrix)[0]
    order = np.argsort(-sims)[:k]
    return [
        {"id": content_icons[i]["id"], "meaning": content_icons[i]["meaning_en"], "score": round(float(sims[i]), 3)}
        for i in order
    ]


# ---------------------------------------------------------------------------
# Stage A: rule-based operator extraction + a *demo-only* mini RU->EN gloss
# table standing in for the production LLM normalization call.
# ---------------------------------------------------------------------------

NEGATION_WORDS = {"no", "not", "without", "нет", "без", "не"}
URGENT_WORDS = {"urgent", "please help", "help", "asap", "срочно", "помогите", "помощь"}
NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "один": 1, "одна": 1, "два": 2, "две": 2, "три": 3, "четыре": 4, "пять": 5,
}
MANY_WORDS = {"many", "much", "lots", "several", "много"}

# DEMO-ONLY stand-in for Stage A's real job (an LLM call). Kept intentionally
# tiny: production replaces this dict entirely with a model call, it does not
# get extended by hand.
DEMO_RU_GLOSS = {
    "туалет": "toilet",
    "вода": "water",
    "пиво": "beer",
    "еда": "food",
    "поесть": "food",
    "карта": "card",
    "деньги": "money",
    "такси": "taxi",
    "отель": "hotel",
    "гостиница": "hotel",
    "врач": "medical help",
    "полиция": "police",
    "wifi": "wifi",
    "вайфай": "wifi",
    "бар": "bar",
}


def extract_operators_and_query(text):
    t = text.lower()
    ops = {"quantity": None, "negation": False, "urgent": False, "question": "?" in text}

    if any(w in t for w in URGENT_WORDS):
        ops["urgent"] = True
    if any(re.search(rf"\b{re.escape(w)}\b", t) for w in NEGATION_WORDS):
        ops["negation"] = True

    m = re.search(r"\b(\d+)\b", t)
    if m:
        ops["quantity"] = int(m.group(1))
    else:
        for w, n in NUMBER_WORDS.items():
            if re.search(rf"\b{w}\b", t):
                ops["quantity"] = n
                break
        if ops["quantity"] is None and any(w in t for w in MANY_WORDS):
            ops["quantity"] = "many"

    # demo-only RU->EN gloss substitution (stand-in for real Stage A LLM call)
    content_query = t
    for ru, en in DEMO_RU_GLOSS.items():
        content_query = content_query.replace(ru, en)

    return ops, content_query


def quantity_to_tiles(n):
    if n is None:
        return [], None
    if n == "many":
        return ["qty_5", "qty_plus"], None
    if n in (1, 2):
        return [f"qty_{n}"], None
    if n == 5:
        return ["qty_5"], None
    if n == 3:
        return ["qty_1", "qty_2"], None
    if n == 10:
        return ["qty_5", "qty_5"], None
    # unsupported exact count under current core quantity set -> flag, don't guess
    return [], f"quantity {n} has no exact core-tile encoding (spec/GRAMMAR.md sec.6) - falls back to qty_5+qty_plus or needs a new tile"


# ---------------------------------------------------------------------------
# Stage C + D: compose final tile sequence, apply confidence gate
# ---------------------------------------------------------------------------

def compose(text, content_icons, vectorizer, matrix, threshold=CONFIDENCE_THRESHOLD):
    ops, content_query = extract_operators_and_query(text)
    candidates = retrieve(content_query, content_icons, vectorizer, matrix, k=3)
    best = candidates[0]

    flags = []
    sequence = []

    if best["score"] < threshold:
        flags.append(
            f"LOW_CONFIDENCE ({best['score']}) - no reliable lexicon match; "
            f"route to spec/STANDALONE_BACKLOG.md decision tree instead of guessing"
        )
    else:
        sequence.append(best["id"])

    qty_tiles, qty_flag = quantity_to_tiles(ops["quantity"])
    if qty_flag:
        flags.append(qty_flag)
    sequence += qty_tiles

    if ops["negation"]:
        sequence.append("logic_no")

    if ops["urgent"]:
        sequence.append("punct_exclaim")
    elif ops["question"]:
        sequence.append("punct_question")

    return {
        "input": text,
        "tiles": sequence,
        "top_match": best,
        "alt_candidates": candidates[1:],
        "flags": flags,
    }


# ---------------------------------------------------------------------------
# Demo run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    icons = load_lexicon()
    content_icons, vectorizer, matrix = build_index(icons)

    demo_queries = [
        "Where can I find a toilet?",
        "I need two beers, please",
        "No card, cash only",
        "I need medical help urgently!",
        "Мне нужна вода, срочно",
        "Where is the nearest hotel?",
        "I need sunscreen",  # expected: no good match -> flagged gap
        "Такси, пожалуйста?",
    ]

    for q in demo_queries:
        result = compose(q, content_icons, vectorizer, matrix)
        print("=" * 70)
        print(f"INPUT:   {result['input']}")
        print(f"TILES:   {' + '.join(result['tiles']) if result['tiles'] else '(none)'}")
        print(f"TOP MATCH: {result['top_match']}")
        if result["alt_candidates"]:
            print(f"ALT:       {result['alt_candidates']}")
        if result["flags"]:
            print(f"FLAGS:   {result['flags']}")

    print("\n" + "#" * 70)
    print("# Multi-clause limitation demo: single compose() call vs. pre-split clauses")
    print("#" * 70)
    multi = "No card, cash only"
    print(f"\nONE-SHOT (no segmentation): {compose(multi, content_icons, vectorizer, matrix)['tiles']}")
    clause_a = compose("no card", content_icons, vectorizer, matrix)["tiles"]
    clause_b = compose("cash", content_icons, vectorizer, matrix)["tiles"]
    print(f"PRE-SPLIT (as a real Stage A LLM would segment it): {clause_a} , {clause_b}")
