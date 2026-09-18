#!/usr/bin/env python3
"""Build the first paper-family/subtheme synthesis from reviewed D3 papers."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from taxonomy_normalization import normalize_review_row

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    canonical_triples = {
        (theme["id"], subtheme["id"], concept["id"])
        for theme in taxonomy["themes"]
        for subtheme in theme["subthemes"]
        for concept in subtheme["concepts"]
    }
    valid_concepts = {triple[2] for triple in canonical_triples}
    batch = json.loads((DATA / "interspeech-2025-semantic-reviewed-batch-001.json").read_text())
    batch_2 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-002.json").read_text())
    batch_3 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-003.json").read_text())
    batch_4 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-004.json").read_text())
    batch_5 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-005.json").read_text())
    batch_6 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-006.json").read_text())
    batch_7 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-007.json").read_text())
    batch_8 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-008.json").read_text())
    batch_9 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-009.json").read_text())
    batch_10 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-010.json").read_text())
    batch_11 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-011.json").read_text())
    batch_12 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-012.json").read_text())
    batch_13 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-013.json").read_text())
    batch_14 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-014.json").read_text())
    batch_15 = json.loads((DATA / "interspeech-2025-semantic-reviewed-d3-batch-015.json").read_text())
    eighteenth = json.loads((DATA / "interspeech-2025-eighteenth-d3-notes.json").read_text())
    nineteenth = json.loads((DATA / "interspeech-2025-nineteenth-d3-notes.json").read_text())
    twentieth = json.loads((DATA / "interspeech-2025-twentieth-d3-notes.json").read_text())
    twentyfirst = json.loads((DATA / "interspeech-2025-twentyfirst-d3-notes.json").read_text())
    twentisecond = json.loads((DATA / "interspeech-2025-twentisecond-d3-notes.json").read_text())
    twentythird = json.loads((DATA / "interspeech-2025-twentythird-d3-notes.json").read_text())
    twentyfourth = json.loads((DATA / "interspeech-2025-twentyfourth-d3-notes.json").read_text())
    twentyfifth = json.loads((DATA / "interspeech-2025-twentyfifth-d3-notes.json").read_text())
    twentysixth = json.loads((DATA / "interspeech-2025-twentysixth-d3-notes.json").read_text())
    twentyseventh = json.loads((DATA / "interspeech-2025-twentyseventh-d3-notes.json").read_text())
    twentyeighth = json.loads((DATA / "interspeech-2025-twentyeighth-d3-notes.json").read_text())
    twentyninth = json.loads((DATA / "interspeech-2025-twentyninth-d3-notes.json").read_text())
    thirtieth = json.loads((DATA / "interspeech-2025-thirtieth-d3-notes.json").read_text())
    thirtyfirst = json.loads((DATA / "interspeech-2025-thirtyfirst-d3-notes.json").read_text())
    thirtysecond = json.loads((DATA / "interspeech-2025-thirtysecond-d3-notes.json").read_text())
    thirtythird = json.loads((DATA / "interspeech-2025-thirtythird-d3-notes.json").read_text())
    thirtyfourth = json.loads((DATA / "interspeech-2025-thirtyfourth-d3-notes.json").read_text())
    thirtyfifth = json.loads((DATA / "interspeech-2025-thirtyfifth-d3-notes.json").read_text())
    thirtysixth = json.loads((DATA / "interspeech-2025-thirtysixth-d3-notes.json").read_text())
    thirtyseventh = json.loads((DATA / "interspeech-2025-thirtyseventh-d3-notes.json").read_text())
    thirtyeighth = json.loads((DATA / "interspeech-2025-thirtyeighth-d3-notes.json").read_text())
    thirtyninth = json.loads((DATA / "interspeech-2025-thirtyninth-d3-notes.json").read_text())
    fortieth = json.loads((DATA / "interspeech-2025-fortieth-d3-notes.json").read_text())
    fortyfirst = json.loads((DATA / "interspeech-2025-fortyfirst-d3-notes.json").read_text())
    fortysecond = json.loads((DATA / "interspeech-2025-fortysecond-d3-notes.json").read_text())
    fortythird = json.loads((DATA / "interspeech-2025-fortythird-d3-notes.json").read_text())
    fortyfourth = json.loads((DATA / "interspeech-2025-fortyfourth-d3-notes.json").read_text())
    fortyfifth = json.loads((DATA / "interspeech-2025-fortyfifth-d3-notes.json").read_text())
    fortysixth = json.loads((DATA / "interspeech-2025-fortysixth-d3-notes.json").read_text())
    fortyseventh = json.loads((DATA / "interspeech-2025-fortyseventh-d3-notes.json").read_text())
    fortyeighth = json.loads((DATA / "interspeech-2025-fortyeighth-d3-notes.json").read_text())
    fortyninth = json.loads((DATA / "interspeech-2025-fortyninth-d3-notes.json").read_text())
    fiftieth = json.loads((DATA / "interspeech-2025-fiftieth-d3-notes.json").read_text())
    fiftyfirst = json.loads((DATA / "interspeech-2025-fiftyfirst-d3-notes.json").read_text())
    fiftysecond = json.loads((DATA / "interspeech-2025-fiftysecond-d3-notes.json").read_text())
    fiftythird = json.loads((DATA / "interspeech-2025-fiftythird-d3-notes.json").read_text())
    fiftyfourth = json.loads((DATA / "interspeech-2025-fiftyfourth-d3-notes.json").read_text())
    fiftyfifth = json.loads((DATA / "interspeech-2025-fiftyfifth-d3-notes.json").read_text())
    fiftysixth = json.loads((DATA / "interspeech-2025-fiftysixth-d3-notes.json").read_text())
    fiftyseventh = json.loads((DATA / "interspeech-2025-fiftyseventh-d3-notes.json").read_text())
    fiftyeighth = json.loads((DATA / "interspeech-2025-fiftyeighth-d3-notes.json").read_text())
    fiftyninth = json.loads((DATA / "interspeech-2025-fiftyninth-d3-notes.json").read_text())
    sixtieth = json.loads((DATA / "interspeech-2025-sixtieth-d3-notes.json").read_text())
    sixtyfirst = json.loads((DATA / "interspeech-2025-sixtyfirst-d3-notes.json").read_text())
    sixtysecond = json.loads((DATA / "interspeech-2025-sixtysecond-d3-notes.json").read_text())
    sixtythird = json.loads((DATA / "interspeech-2025-sixtythird-d3-notes.json").read_text())
    batch["rows"] = batch["rows"] + batch_2["rows"] + batch_3["rows"] + batch_4["rows"] + batch_5["rows"] + batch_6["rows"] + batch_7["rows"] + batch_8["rows"] + batch_9["rows"] + batch_10["rows"] + batch_11["rows"] + batch_12["rows"] + batch_13["rows"] + batch_14["rows"] + batch_15["rows"]
    d3_by_id = {row["paper_id"]: row for row in (json.loads(line) for line in (DATA / "interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines() if line.strip())}
    for note in eighteenth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in nineteenth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentieth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentyfirst["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentisecond["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentythird["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentyfourth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentyfifth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentysixth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentyseventh["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentyeighth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in twentyninth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtieth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtyfirst["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtysecond["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtythird["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtyfourth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtyfifth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtysixth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtyseventh["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtyeighth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in thirtyninth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in fortieth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in fortyfirst["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in fortysecond["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in fortythird["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in fortyfourth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in fortyfifth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    for note in fortysixth["notes"]:
        row = d3_by_id.get(note["paper_id"])
        if row and row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": note["paper_id"], "title": row["title"], "theme_id": row["semantic_review"]["theme_id"], "subtheme_id": row["semantic_review"]["subtheme_id"], "concept_id": row["semantic_review"]["concept_id"], "semantic_reasoning": row["semantic_review"].get("semantic_reasoning", "")})
    normalized_rows = [normalize_review_row(row, valid_concepts, canonical_triples) for row in batch["rows"]]
    unique_rows = {}
    for row in normalized_rows:
        if row.get("theme_id") and row.get("paper_id"):
            unique_rows.setdefault(row["paper_id"], row)
    batch["rows"] = list(unique_rows.values())
    notes = {}
    for filename in ("interspeech-2025-d3-notes.json", "interspeech-2025-second-d3-notes.json", "interspeech-2025-third-d3-notes.json", "interspeech-2025-fourth-d3-notes.json", "interspeech-2025-fifth-d3-notes.json", "interspeech-2025-sixth-d3-notes.json", "interspeech-2025-seventh-d3-notes.json", "interspeech-2025-eighth-d3-notes.json", "interspeech-2025-ninth-d3-notes.json", "interspeech-2025-tenth-d3-notes.json", "interspeech-2025-eleventh-d3-notes.json", "interspeech-2025-twelfth-d3-notes.json", "interspeech-2025-thirteenth-d3-notes.json", "interspeech-2025-fourteenth-d3-notes.json", "interspeech-2025-fifteenth-d3-notes.json", "interspeech-2025-sixteenth-d3-notes.json", "interspeech-2025-seventeenth-d3-notes.json", "interspeech-2025-eighteenth-d3-notes.json", "interspeech-2025-nineteenth-d3-notes.json", "interspeech-2025-twentieth-d3-notes.json", "interspeech-2025-twentyfirst-d3-notes.json", "interspeech-2025-twentisecond-d3-notes.json", "interspeech-2025-twentythird-d3-notes.json", "interspeech-2025-twentyfourth-d3-notes.json", "interspeech-2025-twentyfifth-d3-notes.json", "interspeech-2025-twentysixth-d3-notes.json", "interspeech-2025-twentyseventh-d3-notes.json", "interspeech-2025-twentyeighth-d3-notes.json", "interspeech-2025-twentyninth-d3-notes.json", "interspeech-2025-thirtieth-d3-notes.json", "interspeech-2025-thirtyfirst-d3-notes.json", "interspeech-2025-thirtysecond-d3-notes.json", "interspeech-2025-thirtythird-d3-notes.json", "interspeech-2025-thirtyfourth-d3-notes.json", "interspeech-2025-thirtyfifth-d3-notes.json", "interspeech-2025-thirtysixth-d3-notes.json", "interspeech-2025-thirtyseventh-d3-notes.json", "interspeech-2025-thirtyeighth-d3-notes.json", "interspeech-2025-thirtyninth-d3-notes.json", "interspeech-2025-fortieth-d3-notes.json", "interspeech-2025-fortyfirst-d3-notes.json"):
        for row in json.loads((DATA / filename).read_text())["notes"]:
            notes[row["paper_id"]] = row
    for filename in ("interspeech-2025-fortieth-d3-notes.json", "interspeech-2025-fortyfirst-d3-notes.json", "interspeech-2025-fortysecond-d3-notes.json"):
        for row in json.loads((DATA / filename).read_text())["notes"]:
            notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortythird-d3-notes.json").read_text())["notes"]:
            notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfourth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfifth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortysixth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in fortyseventh["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fortyeighth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fortyninth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftieth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftyfirst["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftysecond["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftythird["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftyfourth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftyfifth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftysixth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftyseventh["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftyeighth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in fiftyninth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in sixtieth["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for row in sixtyfirst["notes"]:
        d3_by_id_row = d3_by_id.get(row["paper_id"])
        if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
            batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
        notes[row["paper_id"]] = row
    for extra in (sixtysecond, sixtythird):
        for row in extra["notes"]:
            d3_by_id_row = d3_by_id.get(row["paper_id"])
            if d3_by_id_row and d3_by_id_row.get("semantic_review", {}).get("theme_id"):
                batch["rows"].append({"paper_id": row["paper_id"], "title": d3_by_id_row["title"], "theme_id": d3_by_id_row["semantic_review"]["theme_id"], "subtheme_id": d3_by_id_row["semantic_review"]["subtheme_id"], "concept_id": d3_by_id_row["semantic_review"]["concept_id"], "semantic_reasoning": d3_by_id_row["semantic_review"].get("semantic_reasoning", "")})
            notes[row["paper_id"]] = row
    deduplicated_rows = {}
    for row in batch["rows"]:
        if row.get("theme_id") and row.get("paper_id"):
            deduplicated_rows.setdefault(row["paper_id"], row)
    batch["rows"] = list(deduplicated_rows.values())
    by_theme = defaultdict(list)
    for row in batch["rows"]:
        by_theme[row["theme_id"]].append(row)
    rows = []
    out = [
        "# Speech first-principles seed synthesis",
        "",
        f"This is the first family-synthesis layer, grounded in the {len(batch['rows'])} analyst-reviewed D3 papers. It is not a venue-wide conclusion: themes without a reviewed paper remain explicitly unestablished, and reported results remain author-reported.",
        "",
    ]
    for theme in taxonomy["themes"]:
        papers = by_theme.get(theme["id"], [])
        out += [f"## {theme['name']}", "", f"**Ordinary pressure:** {theme['ordinary_problem']}", "", f"**Naive strategy that breaks:** {theme['naive_failure']}", "", f"**Recurring move:** {theme['recurring_move']}", "", f"**Boundary:** {theme['tradeoff']}", ""]
        if not papers:
            out += ["**D3 evidence status:** No paper in the first reviewed batch is assigned here. This is an open synthesis slot, not evidence that the theme is absent.", ""]
            rows.append({"theme_id": theme["id"], "d3_paper_count": 0, "status": "unestablished"})
            continue
        out += [f"**D3 evidence status:** {len(papers)} reviewed paper(s); the family claim below is limited to these examples.", ""]
        concepts = ", ".join(f"`{p['subtheme_id']}/{p['concept_id']}`" for p in papers)
        out += [f"**Conceptual family represented:** {concepts}.", ""]
        out += ["### What the papers make concrete", ""]
        for paper in papers:
            note = notes[paper["paper_id"]]
            out += [f"#### {paper['title']}", "", f"**Why this belongs:** {paper['semantic_reasoning']}", "", f"**Mechanism:** {note['mech']}", "", f"**Mathematical/evaluation object:** {note['math']}", "", f"**Reported evidence:** {note['ww']}", "", f"**Limit:** {note['limits']}", ""]
        out += ["### Synthesis boundary", "", "These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.", ""]
        rows.append({"theme_id": theme["id"], "d3_paper_count": len(papers), "status": "seed-synthesis", "paper_ids": [p["paper_id"] for p in papers]})
    payload = {
        "schema_version": 1,
        "status": "seed-synthesis-from-reviewed-d3-batch",
        "claim_boundary": "This synthesis covers only the reviewed D3 seed batches and does not represent the full corpus.",
        "reviewed_d3_count": len(batch["rows"]),
        "theme_rows": rows,
    }
    (DATA / "speech-first-principles-seed-synthesis.json").write_text(json.dumps(payload, indent=2) + "\n")
    (REPORTS / "SPEECH_FIRST_PRINCIPLES_SEED_SYNTHESIS.md").write_text("\n".join(out) + "\n")
    print(json.dumps({"reviewed_d3_count": len(batch["rows"]), "themes": len(rows), "themes_with_d3": sum(x["d3_paper_count"] > 0 for x in rows)}))


if __name__ == "__main__":
    main()
