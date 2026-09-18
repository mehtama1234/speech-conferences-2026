#!/usr/bin/env python3
"""Render unresolved semantic cases and their evidence boundaries."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def examples(queue, decision, limit=20):
    rows = [row for row in queue["rows"] if row.get("decision") == decision and row.get("review_state") != "analyst-reviewed"]
    rows.sort(key=lambda row: (-len(row.get("candidate_assignments", [])), row.get("paper_id", "")))
    return rows[:limit]


def render_section(lines, heading, rows, icassp=False):
    lines += [f"## {heading}", ""]
    if not rows:
        lines += ["No examples in the current queue.", ""]
        return
    for row in rows:
        title = row.get("title", row.get("paper_id"))
        depth = row.get("evidence_depth", "unknown")
        excerpt = row.get("evidence_excerpt", "")
        candidates = row.get("candidate_assignments", [])
        alternatives = ", ".join(f"{c.get('theme_id')}/{c.get('subtheme_id')} ({c.get('matched_terms', [])})" for c in candidates[:3]) or "none"
        lines += [f"### {title}", "", f"- ID: `{row.get('paper_id')}`; evidence: `{depth}`", f"- Candidate alternatives: {alternatives}", f"- Evidence excerpt: {excerpt}", "- Next action: inspect the full paper where available; otherwise retain the unresolved status rather than choosing a theme from one lexical cue.", ""]


def main() -> None:
    inter = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
    icassp = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
    lines = [
        "# Semantic review gaps and unresolved cases",
        "",
        "This report makes the unresolved part of the atlas inspectable. Ambiguous means more than one first-principles reading remains plausible; insufficient-evidence means the captured title/abstract does not justify an assignment; unsupported in ICASSP means the record is outside the speech taxonomy and remains in the overall denominator.",
        "",
        "## Queue summary",
        "",
        "| Venue | Total | Analyst-reviewed | Supported proposal | Ambiguous | Insufficient | Unsupported |",
        "|---|---:|---:|---:|---:|---:|---:|",
        f"| INTERSPEECH 2025 | {inter['paper_count']:,} | {inter.get('reviewed_count', 0):,} | {inter['decision_counts']['supported']:,} | {inter['decision_counts']['ambiguous']:,} | {inter['decision_counts']['insufficient-evidence']:,} | {inter['decision_counts']['unsupported']:,} |",
        f"| ICASSP 2026 | {icassp['paper_count']:,} | {icassp.get('reviewed_count', 0):,} | {icassp['decision_counts']['supported']:,} | {icassp['decision_counts']['ambiguous']:,} | {icassp['decision_counts']['insufficient-evidence']:,} | {icassp['decision_counts']['unsupported']:,} |",
        "",
        "A supported proposal is not a completed venue-wide semantic judgment unless its row says `analyst-reviewed`; all other candidates retain the machine-assisted boundary.",
        "",
    ]
    render_section(lines, "INTERSPEECH ambiguous cases", examples(inter, "ambiguous"))
    render_section(lines, "INTERSPEECH insufficient-evidence cases", examples(inter, "insufficient-evidence"))
    render_section(lines, "ICASSP ambiguous cases", examples(icassp, "ambiguous"), True)
    render_section(lines, "ICASSP insufficient-evidence cases", examples(icassp, "insufficient-evidence"), True)
    render_section(lines, "ICASSP out-of-scope cases", examples(icassp, "unsupported"), True)
    lines += ["## Review policy", "", "Do not resolve ambiguity by selecting the paper's most fashionable model name. Resolve it by identifying the ordinary problem, the information changed by the method, the intended target, and the evidence depth. If the abstract does not distinguish those, keep the row ambiguous or insufficient and send it to full-paper review.", ""]
    (REPORTS / "SPEECH_SEMANTIC_REVIEW_GAPS.md").write_text("\n".join(lines))
    payload = {
        "interspeech": {"paper_count": inter["paper_count"], "reviewed_count": inter.get("reviewed_count", 0), "decision_counts": inter["decision_counts"]},
        "icassp": {"paper_count": icassp["paper_count"], "reviewed_count": icassp.get("reviewed_count", 0), "decision_counts": icassp["decision_counts"]},
        "examples_per_section": 20,
    }
    (DATA / "speech-semantic-review-gaps.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload))


if __name__ == "__main__":
    main()
