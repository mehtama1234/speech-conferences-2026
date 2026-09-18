#!/usr/bin/env python3
"""Audit whether the current taxonomy has real first-principles writeups.

This is deliberately stricter than the structural atlas validator.  It checks
that every theme and subtheme has prose for the ordinary problem, failed simple
approach, recurring move, boundary, and evidence.  It also reports where a
subtheme has too little named paper evidence for the intended teaching claim.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"


def words(value: object) -> int:
    return len(str(value or "").split())


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    syntheses = json.loads((DATA / "speech-subtheme-syntheses.json").read_text())
    synthesis_by_id = {row["subtheme_id"]: row for row in syntheses.get("records", [])}

    required_theme_fields = {
        "ordinary_problem": "ordinary problem",
        "naive_failure": "failed simple approach",
        "recurring_move": "recurring move",
        "tradeoff": "tradeoff or limit",
    }
    required_family_fields = {
        "ordinary_pressure": "ordinary pressure",
        "naive_shortcut": "failed simple approach",
        "recurring_move": "recurring move",
        "subtheme_boundary": "neighbor boundary",
        "evidence_boundary": "evidence boundary",
        "unresolved_question": "unresolved question",
    }

    failures: list[dict] = []
    records: list[dict] = []
    for theme in taxonomy.get("themes", []):
        missing_theme = [label for key, label in required_theme_fields.items() if not str(theme.get(key, "")).strip()]
        if missing_theme:
            failures.append({"level": "theme", "id": theme["id"], "missing": missing_theme})
        for subtheme in theme.get("subthemes", []):
            sid = subtheme["id"]
            row = synthesis_by_id.get(sid, {})
            family = row.get("family_synthesis", {}) or {}
            missing = [label for key, label in required_family_fields.items() if not str(family.get(key, "")).strip()]
            named_papers = len(row.get("paper_ids", []))
            d3_papers = len(row.get("d3_paper_ids", []))
            # A short generic question or boundary is not a teaching writeup.
            if words(subtheme.get("question")) < 12:
                missing.append("specific subtheme question")
            if words(subtheme.get("derivation_boundary")) < 12:
                missing.append("specific derivation boundary")
            if not subtheme.get("baseline_anchor"):
                missing.append("baseline anchor")
            if words(subtheme.get("derivation_evidence")) < 45:
                missing.append("complete baseline-to-boundary derivation")
            if named_papers < 2:
                missing.append("at least two named supporting papers")
            if not row:
                missing.append("subtheme synthesis record")
            if missing:
                failures.append({"level": "subtheme", "id": sid, "theme_id": theme["id"], "missing": sorted(set(missing))})
            records.append({
                "theme_id": theme["id"],
                "subtheme_id": sid,
                "subtheme_words": words(subtheme.get("question")) + words(subtheme.get("derivation_boundary")),
                "named_paper_count": named_papers,
                "d3_paper_count": d3_papers,
                "missing": sorted(set(missing)),
            })

    payload = {
        "status": "pass" if not failures else "incomplete",
        "claim_boundary": "This audit checks writeup completeness, not whether the conceptual boundaries are intellectually correct.",
        "theme_count": len(taxonomy.get("themes", [])),
        "subtheme_count": len(records),
        "complete_subtheme_count": sum(not row["missing"] for row in records),
        "failures": failures,
        "records": records,
    }
    (DATA / "speech-first-principles-writeup-audit.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# First-principles writeup audit",
        "",
        f"**Status:** `{payload['status']}`",
        "",
        "This audit checks whether the current reports contain the required plain-language reasoning. A green result would not by itself prove that the boundaries are correct.",
        "",
        f"Themes: **{payload['theme_count']}**; subthemes: **{payload['subtheme_count']}**; complete subtheme writeups: **{payload['complete_subtheme_count']}**.",
        "",
        "| Subtheme | Named papers | D3 papers | Missing requirements |",
        "|---|---:|---:|---|",
    ]
    for row in records:
        missing = ", ".join(row["missing"]) or "—"
        lines.append(f"| {row['subtheme_id']} | {row['named_paper_count']} | {row['d3_paper_count']} | {missing} |")
    (REPORTS / "SPEECH_FIRST_PRINCIPLES_WRITEUP_AUDIT.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"status": payload["status"], "subthemes": payload["subtheme_count"], "complete": payload["complete_subtheme_count"], "failures": len(failures)}))


if __name__ == "__main__":
    main()
