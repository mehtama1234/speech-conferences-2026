#!/usr/bin/env python3
"""Record semantic assignments for the seventh full-paper D3 set."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "franz25_interspeech": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture", "Room acoustics alter clinical voice measures, so the paper tests the boundary between speaker quality and recording-path effects."),
    "goswami25_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "A three-stage enhancer separates signal-level recovery from generative perceptual repair and then fuses their different targets."),
    "ducorroy25_interspeech": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "speaker-adaptation", "Weight merging uses multiple fine-tuning solutions to stabilize recognition of disordered speech under speaker and data variation."),
    "feng25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Soft emotion distributions and minority-aware training treat affect as uncertain human judgment rather than one unquestionable class."),
    "hope25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "speaker-identity", "Controllable synthetic voice features are evaluated as identity and embodiment choices for nonbinary users of speech-generating devices."),
    "gao25b_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Longitudinal public speech and speaker-disjoint evaluation test whether acoustic and linguistic changes near diagnosis can be separated from recording and person effects."),
    "fort25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation", "IsiZulu pronunciation assessment exposes how language-specific data and incomplete error labels limit the meaning of recognition scores."),
    "choi25f_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use", "Generation-assisted multimodal retrieval tests whether audio and text evidence agree on what should be retrieved, rather than rewarding fluent captions alone."),
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
notes = {n["paper_id"]: n for n in json.loads((DATA / "interspeech-2025-seventh-d3-notes.json").read_text())["notes"]}
rows = []
for pid, assignment in ASSIGNMENTS.items():
    paper = papers[pid]
    note = notes[pid]
    rows.append({
        "paper_id": pid, "title": paper["title"], "decision": "supported",
        "confidence": "analyst-reviewed-D3", "theme_id": assignment[0],
        "subtheme_id": assignment[1], "concept_id": assignment[2],
        "semantic_reasoning": assignment[3],
        "evidence_fields": ["bp","wh","naive","ap","mech","math","eval","ww","limits"],
        "evidence_excerpt": "Problem: " + note["bp"] + " Mechanism: " + note["mech"] + " Reported result: " + note["ww"] + " Boundary: " + note["limits"],
        "source_location": paper["paper_url"],
        "source_sha256": hashlib.sha256(paper["abstract"].encode()).hexdigest(),
        "evidence_depth": "D3", "review_state": "analyst-reviewed",
        "claim_boundary": "Full-paper note is backed by the captured official PDF; result remains author-reported and was not independently reproduced.",
    })
payload = {
    "schema_version": 1, "batch_id": "interspeech-2025-semantic-d3-batch-005",
    "status": "analyst-reviewed-D3-batch",
    "claim_boundary": "These eight assignments are analyst-reviewed from captured official PDFs and structured notes; claims remain paper-reported and are not independent reproductions.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "interspeech-2025-semantic-reviewed-d3-batch-005.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D3": len(rows)}))

