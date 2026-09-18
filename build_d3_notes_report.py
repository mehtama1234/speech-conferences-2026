#!/usr/bin/env python3
"""Render structured representative-paper notes as Markdown."""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "data/interspeech-2025-d3-notes.json").read_text())
records = json.loads((HERE / "data/interspeech-2025-representative-papers.json").read_text())["papers"]
by_id = {row["paper_id"]: row for row in records}
labels = {
    "bp": "Big picture", "wh": "Why it is hard", "naive": "Naive attempt",
    "ap": "Central move", "mech": "Mechanism", "math": "Mathematical idea",
    "dots": "Connections", "ww": "What the paper reports", "limits": "Limits",
}
parts = [
    "# INTERSPEECH 2025 representative full-paper notes\n",
    "These eight notes are the first D3 pass: one representative paper per initial conceptual theme. They are based on the official ISCA PDFs captured in `data/interspeech-2025-representative-papers.json`; they summarize paper evidence and do not independently reproduce experiments.\n",
]
for i, note in enumerate(data["notes"], 1):
    paper = by_id[note["paper_id"]]
    parts.append(f"## {i}. {note['theme']}\n")
    parts.append(f"**Paper:** [{note['title']}]({paper['paper_url']})  \n**Evidence:** D3 full-text capture; PDF SHA-256 `{paper['pdf_sha256']}`; {paper['page_count']} pages.\n")
    for key, label in labels.items():
        parts.append(f"- **{label}:** {note[key]}")
    parts.append("")
parts.append("## Cross-paper observation\n\nThese papers show a speech-specific pattern: the central object is rarely just the model. It is a relationship between a signal and a human or physical condition—articulation, impairment, direction, aging, identity, social context, or listener judgment. The notes support this interpretation at D3 depth for this small review set; they do not establish venue-wide prevalence.\n")
out = HERE / "reports/INTERSPEECH_2025_REPRESENTATIVE_NOTES.md"
out.write_text("\n".join(parts))
print(f"wrote {out}")
