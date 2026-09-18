#!/usr/bin/env python3
"""Expose memberships that must be re-read after the taxonomy changed.

Concept-ID normalization can place a paper under the new parent, but that is
not the same as deciding that the paper belongs there rather than in a new
neighbor. This queue preserves the prior evidence and makes that work visible.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    concepts = {
        c["id"]: {"theme_id": t["id"], "theme_name": t["name"], "subtheme_id": s["id"], "subtheme_name": s["name"], "concept_name": c["name"], "boundary": c.get("boundary", "")}
        for t in taxonomy["themes"]
        for s in t["subthemes"]
        for c in s["concepts"]
    }
    rows = []
    for filename, venue in [
        ("interspeech-2025-semantic-review-queue.json", "INTERSPEECH 2025"),
        ("icassp-2026-semantic-review-queue.json", "ICASSP 2026"),
    ]:
        queue = json.loads((DATA / filename).read_text())
        for source in queue.get("rows", []):
            if source.get("decision") != "supported" or source.get("review_state") != "analyst-reviewed":
                continue
            review = source.get("analyst_review") or source
            concept = concepts.get(review.get("concept_id"), {})
            rows.append({
                "venue": venue,
                "paper_id": source.get("paper_id"),
                "title": source.get("title"),
                "evidence_depth": review.get("evidence_depth", source.get("evidence_depth")),
                "taxonomy_review_state": "needs-taxonomy-adjudication",
                "inherited_concept_id": review.get("concept_id"),
                "current_theme_id": concept.get("theme_id"),
                "current_subtheme_id": concept.get("subtheme_id"),
                "current_concept_name": concept.get("concept_name"),
                "current_boundary": concept.get("boundary"),
                "prior_semantic_reasoning": review.get("semantic_reasoning"),
                "prior_evidence_excerpt": review.get("evidence_excerpt"),
                "alternative_assignment": review.get("alternative_assignment"),
                "adjudication_question": "Does the captured evidence support this concept and its new subtheme boundary rather than the nearest neighboring subtheme?",
                "final_decision": None,
                "reviewer_note": None,
            })
    rows.sort(key=lambda row: (row["venue"], row["paper_id"] or ""))
    payload = {
        "schema_version": 1,
        "status": "open-taxonomy-adjudication",
        "claim_boundary": "These memberships were previously semantically reviewed against an earlier taxonomy and then normalized to the current concept parents. They are not counted as final current-taxonomy adjudications until this queue is closed.",
        "taxonomy": "data/speech-first-principles-taxonomy.json",
        "row_count": len(rows),
        "decision_counts": {"needs-taxonomy-adjudication": len(rows)},
        "rows": rows,
    }
    (DATA / "speech-taxonomy-adjudication-queue.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# Taxonomy re-adjudication queue",
        "",
        payload["claim_boundary"],
        "",
        f"Open memberships: **{len(rows)}** (INTERSPEECH and ICASSP supported rows).",
        "",
        "Every row preserves the prior reasoning and evidence excerpt, names the current concept boundary, and asks whether the evidence supports the new parent rather than a neighboring subtheme.",
        "",
        "| Venue | Evidence depth | Open rows |",
        "|---|---|---:|",
    ]
    for venue in ["INTERSPEECH 2025", "ICASSP 2026"]:
        for depth in ["D3", "D2", "D1"]:
            count = sum(row["venue"] == venue and row["evidence_depth"] == depth for row in rows)
            if count:
                lines.append(f"| {venue} | {depth} | {count} |")
    (REPORTS / "SPEECH_TAXONOMY_READJUDICATION_QUEUE.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"status": payload["status"], "open_rows": len(rows)}))


if __name__ == "__main__":
    main()
