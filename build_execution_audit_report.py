#!/usr/bin/env python3
"""Render static artifact inspection results without implying reproduction."""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "data/interspeech-2025-execution-audit.json").read_text())
attempts_path = HERE / "data/speech-artifact-execution-attempts.json"
attempts = json.loads(attempts_path.read_text()).get("attempts", []) if attempts_path.exists() else []
lines = [
    "# INTERSPEECH 2025 artifact execution audit",
    "",
    "This is a static repository/dependency inspection. No paper experiment, model inference, dataset download, or listener study was executed.",
    "",
    "| Paper | Artifact | Clone | Observed commit | Dataset/runtime boundary | Execution |",
    "|---|---|---|---|---|---|",
]
for row in data["records"]:
    commit = row.get("observed_commit") or "not-resolved"
    lines.append(f"| {row['paper_id']} | {row['artifact']} | {row['repository_clone']} | `{commit[:12]}` | {row['dataset_status']} | {row['execution_status']} |")
lines += ["", "## Findings", ""]
for row in data["records"]:
    lines.append(f"### {row['paper_id']} — {row['artifact']}")
    for finding in row["static_findings"]:
        lines.append(f"- {finding}")
    lines.append(f"- Next action: {row['next_action']}")
    lines.append("")
lines += ["## Bounded local checks", "", "These checks are intentionally separate from the artifact ledger. They establish only the recorded local command outcome at the observed commit; they do not reproduce a paper experiment.", "", "| Artifact | Papers | Commit | Scope | Status |", "|---|---|---|---|---|"]
for row in attempts:
    papers = ", ".join(row.get("paper_ids", [])) or "not mapped"
    lines.append(f"| {row.get('artifact', 'unknown')} | {papers} | `{(row.get('commit') or 'not-resolved')[:12]}` | {row.get('execution_scope', 'not recorded')} | {row.get('status', 'not recorded')} |")
if not attempts:
    lines.append("| none | — | `—` | no bounded local check recorded | not-attempted |")
lines += ["", "The bounded syntax and toy-smoke results above do not establish dependency resolution, dataset/checkpoint access, inference behavior, metric agreement, or scientific reproduction.", ""]
out = HERE / "reports/INTERSPEECH_2025_EXECUTION_AUDIT.md"
out.write_text("\n".join(lines))
print(f"wrote {out}")
