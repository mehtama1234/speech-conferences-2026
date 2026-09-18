#!/usr/bin/env python3
"""Render a single human-readable D3 report with normalized taxonomy paths."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
deep = {json.loads(line)["paper_id"]: json.loads(line) for line in (DATA / "interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines() if line.strip()}
paper_urls = {row["paper_id"]: row.get("paper_url", "") for row in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
notes = {}
for path in sorted(DATA.glob("interspeech-2025-*-d3-notes.json")):
    for note in json.loads(path.read_text()).get("notes", []):
        notes.setdefault(note.get("paper_id"), note)
fields = [("Ordinary problem", "bp"), ("Why it is hard", "wh"), ("Naive attempt", "naive"), ("Central move", "ap"), ("Mechanism", "mech"), ("Mathematical idea", "math"), ("What the paper reports", "ww"), ("Limits", "limits")]
parts = ["# INTERSPEECH 2025 normalized D3 paper notes", "", "This consolidated report uses the authoritative semantic-review path for every captured D3 paper. Results remain author-reported unless a separate bounded execution record says otherwise.", ""]
count = 0
for pid, row in sorted(deep.items(), key=lambda item: (item[1].get("semantic_review", {}).get("theme_id") or "", item[1].get("semantic_review", {}).get("subtheme_id") or "", item[0])):
    if row.get("depth") != "D3" or not row.get("semantic_review", {}).get("theme_id"):
        continue
    note, assignment = notes.get(pid, row), row["semantic_review"]
    count += 1
    parts += [f"## {count}. {row['title']}", "", f"**Paper:** [{row['title']}]({paper_urls.get(pid, '')})", f"**Taxonomy:** `{assignment['theme_id']} / {assignment['subtheme_id']} / {assignment['concept_id']}`", f"**Evidence:** D3 full-paper capture; PDF SHA-256 `{row['full_paper_evidence']['pdf_sha256']}`; full-text SHA-256 `{row['full_paper_evidence']['full_text_sha256']}`.", ""]
    parts += [f"- **{label}:** {note.get(key, '')}" for label, key in fields] + [""]
parts += [f"## Boundary", "", f"The report contains {count} D3 notes with normalized taxonomy paths. It is a purposive full-paper seed, not a venue-wide prevalence estimate or independent reproduction.", ""]
out = HERE / "reports/INTERSPEECH_2025_NORMALIZED_D3_NOTES.md"
out.write_text("\n".join(parts))
print(json.dumps({"papers": count, "output": str(out)}))
