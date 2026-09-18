#!/usr/bin/env python3
"""Render second-pass D3 notes and claims."""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
notes = json.loads((HERE / "data/interspeech-2025-second-d3-notes.json").read_text())["notes"]
papers = {x["paper_id"]: x for x in json.loads((HERE / "data/interspeech-2025-second-d3-papers.json").read_text())["papers"]}
labels = {"bp":"Big picture","wh":"Why hard","naive":"Naive attempt","ap":"Central move","mech":"Mechanism","math":"Mathematical idea","dots":"Connections","ww":"What paper reports","limits":"Limits"}
parts = ["# INTERSPEECH 2025 second-pass full-paper notes\n", "These eight additional notes extend the D3 sample to two papers per initial theme. They are based on captured official PDFs and remain paper-reported, not independently reproduced.\n"]
claims = []
for i, note in enumerate(notes, 1):
    paper = papers[note["paper_id"]]
    parts.append(f"## {i}. {note['theme']}\n\n**Paper:** [{paper['title']}]({paper['paper_url']})  \n**Evidence:** D3; PDF SHA-256 `{paper['pdf_sha256']}`; {paper['page_count']} pages.\n")
    for key, label in labels.items():
        parts.append(f"- **{label}:** {note[key]}")
    parts.append("")
    claims.append({"claim_id": f"IS25-D3B-{i:02d}", "paper_id": note["paper_id"], "theme": note["theme"], "claim": note["ww"], "evidence_depth": "D3", "pdf_sha256": paper["pdf_sha256"], "full_text_sha256": paper["full_text_sha256"], "support_status": "paper-reported-not-independently-verified", "independent_support_status": "not-established", "limitations": note["limits"]})
parts.append("## Cross-paper observation\n\nThe second set reinforces that speech systems are evaluated against variation in language, health, identity, domain, and listener-relevant content—not only average benchmark quality. This is a D3 observation over sixteen reviewed papers, not venue-wide prevalence.\n")
(HERE / "reports/INTERSPEECH_2025_SECOND_D3_NOTES.md").write_text("\n".join(parts))
(HERE / "data/interspeech-2025-second-claim-ledger.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","claim_count":len(claims),"claims":claims}, indent=2, ensure_ascii=False) + "\n")
print("wrote second-pass notes and claim ledger")
