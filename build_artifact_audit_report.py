#!/usr/bin/env python3
"""Render the non-deterministic artifact reachability audit."""

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
audit = json.loads((HERE / "data/interspeech-2025-artifact-access-audit.json").read_text())
ledger = json.loads((HERE / "data/interspeech-2025-artifact-ledger.json").read_text())
kind_by_url = {row["url"]: row["artifact_kind"] for row in ledger["rows"]}
lines = [
    "# INTERSPEECH 2025 artifact reachability audit",
    "",
    f"This point-in-time HEAD-request audit checked {len(audit['results'])} unique URLs cited by the eight D3 representative papers.",
    "",
    f"- Audited at: `{audit['audited_at_utc']}`",
    f"- Status counts: `{dict(Counter(row['access_status'] for row in audit['results']))}`",
    "- Execution status for every URL: **not attempted**.",
    "",
    "Reachability is weaker than reproducibility: a reachable URL does not establish that code, data, checkpoints, licenses, dependencies, or run instructions are complete. Some extracted bibliography URLs are visibly truncated by PDF text extraction and are recorded as malformed rather than silently repaired.",
    "",
    "| Kind | URL | Status | HTTP |",
    "|---|---|---|---:|",
]
for row in audit["results"]:
    lines.append(f"| {kind_by_url.get(row['url'], 'unknown')} | {row['url']} | {row['access_status']} | {row.get('http_status') or ''} |")
out = HERE / "reports/INTERSPEECH_2025_ARTIFACT_ACCESS_AUDIT.md"
out.write_text("\n".join(lines) + "\n")
print(f"wrote {out}")
