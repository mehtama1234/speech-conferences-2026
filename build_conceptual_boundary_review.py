#!/usr/bin/env python3
"""Audit the conceptual boundaries of every first-principles subtheme.

This is a consistency review of the authored taxonomy, not an independent
scientific validation of the papers.  It checks the derivation chain that a
reader would use to inspect each proposed boundary.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"


def words(value):
    return len(str(value or "").split())


def main():
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    baseline = json.loads((DATA / "speech-baseline-source.json").read_text())
    syntheses = json.loads((DATA / "speech-subtheme-syntheses.json").read_text())
    synthesis_by_id = {r["subtheme_id"]: r for r in syntheses.get("records", [])}
    anchors = {a.get("anchor") for a in baseline.get("anchors", [])}
    taxonomy_anchor_ids = {
        subtheme.get("baseline_anchor")
        for theme in taxonomy.get("themes", [])
        for subtheme in theme.get("subthemes", [])
        if subtheme.get("baseline_anchor")
    }
    rows = []
    failures = []
    seen_questions = set()
    seen_subthemes = set()
    seen_concepts = set()
    for theme in taxonomy.get("themes", []):
        for subtheme in theme.get("subthemes", []):
            sid = subtheme["id"]
            row = synthesis_by_id.get(sid, {})
            family = row.get("family_synthesis", {}) or {}
            concepts = subtheme.get("concepts", [])
            checks = {
                "unique_subtheme_id": sid not in seen_subthemes,
                "unique_question": subtheme.get("question") not in seen_questions,
                "baseline_anchor_present": bool(subtheme.get("baseline_anchor")),
                "baseline_anchor_known": subtheme.get("baseline_anchor") in taxonomy_anchor_ids and bool(anchors),
                "derivation_is_concrete": words(subtheme.get("derivation_evidence")) >= 45,
                "neighbor_boundary_is_concrete": words(subtheme.get("derivation_boundary")) >= 12,
                "family_boundary_present": words(family.get("subtheme_boundary")) >= 12,
                "evidence_boundary_present": words(family.get("evidence_boundary")) >= 12,
                "named_evidence": len(row.get("paper_ids", [])) >= 2,
                "d3_evidence": row.get("d3_paper_count", 0) >= 1,
                "concepts_present": bool(concepts),
            }
            concept_failures = []
            for concept in concepts:
                cid = concept.get("id")
                if cid in seen_concepts:
                    concept_failures.append(f"duplicate concept id: {cid}")
                seen_concepts.add(cid)
                for field in ("definition", "boundary", "positive_example", "negative_example", "membership_evidence_rule"):
                    if not str(concept.get(field, "")).strip():
                        concept_failures.append(f"{cid}: missing {field}")
            if concept_failures:
                checks["concept_rules_complete"] = False
            else:
                checks["concept_rules_complete"] = True
            failures.extend({"subtheme_id": sid, "check": key} for key, value in checks.items() if not value)
            failures.extend({"subtheme_id": sid, "check": item} for item in concept_failures)
            rows.append({
                "theme_id": theme["id"],
                "subtheme_id": sid,
                "review_status": "agent-reviewed-with-explicit-boundaries" if not any(not v for v in checks.values()) else "needs-revision",
                "checks": checks,
                "named_paper_count": len(row.get("paper_ids", [])),
                "d3_paper_count": row.get("d3_paper_count", 0),
                "concept_count": len(concepts),
            })
            seen_subthemes.add(sid)
            seen_questions.add(subtheme.get("question"))

    payload = {
        "status": "pass-with-explicit-boundaries" if not failures else "needs-revision",
        "review_scope": "Consistency review of the authored first-principles derivation and evidence boundaries; not independent scientific validation or a claim that the taxonomy covers all speech research.",
        "baseline_source_id": baseline.get("source_id"),
        "theme_count": len(taxonomy.get("themes", [])),
        "subtheme_count": len(rows),
        "reviewed_subtheme_count": sum(r["review_status"] == "agent-reviewed-with-explicit-boundaries" for r in rows),
        "failures": failures,
        "records": rows,
    }
    (DATA / "speech-conceptual-boundary-review.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# Conceptual boundary review",
        "",
        f"**Status:** `{payload['status']}`",
        "",
        payload["review_scope"],
        "",
        f"Reviewed **{payload['reviewed_subtheme_count']} / {payload['subtheme_count']}** subthemes against the baseline source, derivation chain, neighboring boundary, named evidence, and concept membership rules.",
        "",
        "| Subtheme | Papers | D3 | Concepts | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(f"| {row['subtheme_id']} | {row['named_paper_count']} | {row['d3_paper_count']} | {row['concept_count']} | {row['review_status']} |")
    if failures:
        lines.extend(["", "## Failures", ""])
        lines.extend(f"- `{f['subtheme_id']}`: `{f['check']}`" for f in failures)
    (REPORTS / "SPEECH_CONCEPTUAL_BOUNDARY_REVIEW.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"status": payload["status"], "subthemes": payload["subtheme_count"], "reviewed": payload["reviewed_subtheme_count"], "failures": len(failures)}))


if __name__ == "__main__":
    main()
