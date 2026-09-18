#!/usr/bin/env python3
"""Materialize corpus-wide semantic dispositions without confusing proposals with judgment.

Every captured record receives one explicit disposition:
analyst-confirmed, analyst-rejected, provisional-candidate, or unresolved.
The latter two preserve the evidence and the reason a human reading is still needed.
"""

from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def materialize(queue_path: Path, venue: str) -> list[dict]:
    queue = json.loads(queue_path.read_text())
    out = []
    for row in queue.get("rows", []):
        reviewed = row.get("analyst_review") or {}
        candidates = row.get("candidate_assignments") or []
        if row.get("review_state") == "analyst-reviewed":
            decision = row.get("decision")
            if decision == "supported":
                status = "analyst-confirmed"
            elif decision == "unsupported":
                status = "analyst-rejected"
            else:
                status = "analyst-unresolved"
            assignment = reviewed
            reason = reviewed.get("semantic_reasoning") or reviewed.get("claim_boundary")
            boundary = reviewed.get("claim_boundary") or "Analyst decision is bounded by the source evidence depth."
            evidence = reviewed.get("evidence_excerpt") or row.get("evidence_excerpt")
            basis = f"analyst-reviewed-{row.get('evidence_depth', 'unknown')}"
        else:
            decision = row.get("decision")
            assignment = candidates[0] if candidates else {}
            evidence = assignment.get("evidence_excerpt") or row.get("evidence_excerpt")
            if decision == "supported" and candidates:
                status = "provisional-candidate"
                reason = "A title/abstract rule found a plausible first-principles destination, but no analyst has confirmed that the conceptual move is central."
            elif decision == "unsupported":
                status = "unresolved"
                reason = "The available metadata does not establish that this is a speech paper; a lexical match, if present, is not accepted as semantic evidence."
            else:
                status = "unresolved"
                reason = "The available title/abstract evidence leaves competing concepts or too little evidence; human semantic adjudication is required."
            boundary = row.get("review_rule") or "Machine proposal only; not a final semantic assignment."
            basis = f"machine-proposed-{row.get('evidence_depth', 'unknown')}"
        out.append({
            "venue": venue,
            "paper_id": row.get("paper_id"),
            "title": row.get("title"),
            "source": row.get("source", "queue"),
            "evidence_depth": row.get("evidence_depth"),
            "semantic_disposition": status,
            "queue_decision": decision,
            "theme_id": assignment.get("theme_id"),
            "subtheme_id": assignment.get("subtheme_id"),
            "concept_id": assignment.get("concept_id"),
            "semantic_reasoning": reason,
            "evidence_excerpt": evidence,
            "alternative_assignments": [
                {
                    "theme_id": candidate.get("theme_id"),
                    "subtheme_id": candidate.get("subtheme_id"),
                    "matched_terms": candidate.get("matched_terms", []),
                    "evidence_excerpt": candidate.get("evidence_excerpt"),
                }
                for candidate in candidates[1:]
            ],
            "evidence_basis": basis,
            "claim_boundary": boundary,
            "unresolved_reason": None if status in {"analyst-confirmed", "analyst-rejected"} else reason,
        })
    return out


def write(venue: str, rows: list[dict]) -> dict:
    counts = Counter(row["semantic_disposition"] for row in rows)
    path = DATA / f"{venue.lower()}-semantic-assignments.jsonl"
    with path.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return {"venue": venue, "paper_count": len(rows), "disposition_counts": dict(sorted(counts.items())), "path": str(path)}


def main() -> None:
    interspeech = materialize(DATA / "interspeech-2025-semantic-review-queue.json", "INTERSPEECH 2025")
    icassp = materialize(DATA / "icassp-2026-semantic-review-queue.json", "ICASSP 2026")
    summaries = [write("interspeech-2025", interspeech), write("icassp-2026", icassp)]
    report = [
        "# Corpus-wide semantic assignments",
        "",
        "Every captured record has an explicit semantic disposition. analyst-confirmed and analyst-rejected are human decisions. provisional-candidate is an explainable title/abstract proposal that still needs human adjudication. unresolved records ambiguity, insufficient evidence, or an out-of-scope/non-speech case without pretending that the evidence is stronger than it is.",
        "",
        "The JSONL files preserve the candidate evidence, alternatives, source depth, and unresolved reason for every paper. A machine proposal is never counted as an analyst-confirmed conceptual assignment.",
        "",
    ]
    for summary in summaries:
        report += [f"## {summary['venue']}", "", f"Records: **{summary['paper_count']}**", "", "| Disposition | Count |", "|---|---:|"]
        report += [f"| {key} | {value} |" for key, value in summary["disposition_counts"].items()]
        report += [""]
    (REPORTS / "SPEECH_CORPUS_SEMANTIC_ASSIGNMENTS.md").write_text("\n".join(report) + "\n")
    print(json.dumps(summaries))


if __name__ == "__main__":
    main()

