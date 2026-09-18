#!/usr/bin/env python3
"""Record semantic assignments for the sixth full-paper D3 set."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "bandekar25_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination", "Multi-target pretraining uses linguistic and articulatory labels to make acoustic-to-articulatory inversion useful under scarce paired data and lower inference cost."),
    "baser25_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy", "WavShape treats a speech embedding as an information budget: reduce dependence on sensitive attributes while retaining task-relevant speech information."),
    "bhattacharya25_interspeech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching", "The study connects code-switching behavior to language background and proficiency, showing why multilingual speech cannot be interpreted without speaker and language context."),
    "elmers25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary", "Triadic voice-activity projection predicts who will speak next from acoustic history, replacing fixed silence thresholds with joint temporal state prediction."),
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
notes = {n["paper_id"]: n for n in json.loads((DATA / "interspeech-2025-sixth-d3-notes.json").read_text())["notes"]}
rows = []
for pid, assignment in ASSIGNMENTS.items():
    p = papers[pid]
    n = notes[pid]
    abstract = p["abstract"]
    rows.append({
        "paper_id": pid, "title": p["title"], "decision": "supported",
        "confidence": "analyst-reviewed-D3", "theme_id": assignment[0],
        "subtheme_id": assignment[1], "concept_id": assignment[2],
        "semantic_reasoning": assignment[3],
        "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "eval", "ww", "limits"],
        "evidence_excerpt": "Problem: " + n["bp"] + " Mechanism: " + n["mech"] + " Reported result: " + n["ww"] + " Boundary: " + n["limits"],
        "source_location": p["paper_url"],
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": "D3", "review_state": "analyst-reviewed",
        "claim_boundary": "Full-paper note is backed by the captured official PDF; result remains author-reported and was not independently reproduced.",
    })
payload = {
    "schema_version": 1, "batch_id": "interspeech-2025-semantic-d3-batch-004",
    "status": "analyst-reviewed-D3-batch",
    "claim_boundary": "These four assignments are analyst-reviewed from captured official PDFs and structured notes; claims remain paper-reported and are not independent reproductions.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "interspeech-2025-semantic-reviewed-d3-batch-004.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D3": len(rows)}))
