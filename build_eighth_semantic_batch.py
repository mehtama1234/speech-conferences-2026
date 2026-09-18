#!/usr/bin/env python3
"""Record semantic assignments for the eighth full-paper D3 set."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "alizadeh25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation", "Recursive separation makes the unknown speaker count part of the separation problem."),
    "arai25_interspeech": ("sound-and-production", "source-filter-production", "vocal-tract-filter", "Physical static and dynamic vocal-tract models expose how geometry and articulation shape sound."),
    "bafna25_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness", "Language identification must preserve language evidence while refusing the shortcut that treats accent as language."),
    "baumann25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech", "Pathology-aware representations and targeted data address systematic production differences rather than generic noise."),
    "chen25b_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "Diffusion-loss-regularized reward optimization improves naturalness without letting TTS drift from learned speech structure."),
    "fujita25b_interspeech": ("meaning-and-interaction", "grounding-and-action", "referential-grounding", "Dialogue continuation turns audio descriptions into answers grounded in the sound rather than fixed caption wording."),
    "chandra25b_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Attack-invariant representations test whether fake-speech detection survives changes in attack, codec, and language."),
    "ahadzi25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "speaker-adaptation", "Importance-weighted continual learning protects earlier child-speech mappings while adapting to sequential speakers."),
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
notes = {n["paper_id"]: n for n in json.loads((DATA / "interspeech-2025-eighth-d3-notes.json").read_text())["notes"]}
rows = []
for pid, assignment in ASSIGNMENTS.items():
    paper = papers[pid]
    note = notes[pid]
    rows.append({"paper_id": pid, "title": paper["title"], "decision": "supported", "confidence": "analyst-reviewed-D3", "theme_id": assignment[0], "subtheme_id": assignment[1], "concept_id": assignment[2], "semantic_reasoning": assignment[3], "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "eval", "ww", "limits"], "evidence_excerpt": "Problem: " + note["bp"] + " Mechanism: " + note["mech"] + " Result: " + note["ww"] + " Boundary: " + note["limits"], "source_location": paper["paper_url"], "source_sha256": hashlib.sha256(paper["abstract"].encode()).hexdigest(), "evidence_depth": "D3", "review_state": "analyst-reviewed", "claim_boundary": "Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced."})
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d3-batch-006", "status": "analyst-reviewed-D3-batch", "claim_boundary": "Eight assignments are analyst-reviewed from captured official PDFs and structured notes; claims are not independent reproductions.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d3-batch-006.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D3": len(rows)}))
