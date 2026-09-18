#!/usr/bin/env python3
"""Assign the sixteenth D3 paper to the canonical taxonomy."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
paper = next(p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"] if p["paper_id"] == "fathan25_interspeech")
capture = json.loads((DATA / "interspeech-2025-sixteenth-d3-papers.json").read_text())["papers"][0]
note = json.loads((DATA / "interspeech-2025-sixteenth-d3-notes.json").read_text())["notes"][0]
row = {
    "paper_id": paper["paper_id"], "title": paper["title"], "decision": "supported", "confidence": "analyst-reviewed-D3",
    "theme_id": "people-variation-and-health", "subtheme_id": "speaker-characteristics", "concept_id": "speaker-verification",
    "semantic_reasoning": "The captured paper directly studies how training and optimization affect verification of speaker identity under changed conditions.",
    "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "eval", "ww", "limits"],
    "evidence_excerpt": "Problem: " + note["bp"] + " Mechanism: " + note["mech"] + " Result: " + note["ww"] + " Boundary: " + note["limits"],
    "source_location": paper["paper_url"], "source_sha256": hashlib.sha256(paper["abstract"].encode()).hexdigest(),
    "evidence_depth": "D3", "review_state": "analyst-reviewed",
    "claim_boundary": "Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced.",
}
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d3-batch-014", "status": "analyst-reviewed-D3-batch", "claim_boundary": "One additional official-PDF assignment closes a two-case D3 contrast for speaker characteristics; claims are not independent reproductions.", "reviewed_count": 1, "rows": [row]}
(DATA / "interspeech-2025-semantic-reviewed-d3-batch-014.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": 1, "D3": 1}))
