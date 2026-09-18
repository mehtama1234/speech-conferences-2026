#!/usr/bin/env python3
"""Record semantic assignments for the ninth full-paper D3 set."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "ahn25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "VICReg constraints make noisy speech representations retain useful acoustic units before recognition."),
    "bai25_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness", "Discrete tokens change pronunciation while preserving speaker identity with nonparallel accent data."),
    "b25_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Structured codebooks reduce enhancement cost by exploiting regularities in speech parameters."),
    "cordlandwehr25_interspeech": ("sound-and-production", "room-channel-and-sensing", "spatial-filtering", "TDOA and speaker embeddings combine room geometry with voice identity without equating position to identity."),
    "botelho25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Class-aware acoustic and linguistic ensembles test cognitive-decline signals while exposing clinical data imbalance."),
    "cho25b_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "Disentangled emotion embeddings change delivery while protecting the target speaker's voice."),
    "chen25j_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Codec taxonomy makes fake-speech source tracing a provenance problem rather than only binary detection."),
    "puhach25_interspeech": ("meaning-and-interaction", "grounding-and-action", "interactional-feedback", "Default speaker assignment makes social associations in speech generation observable as an accountability behavior."),
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
notes = {n["paper_id"]: n for n in json.loads((DATA / "interspeech-2025-ninth-d3-notes.json").read_text())["notes"]}
rows = []
for pid, a in ASSIGNMENTS.items():
    p, n = papers[pid], notes[pid]
    rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D3","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_fields":["bp","wh","naive","ap","mech","math","eval","ww","limits"],"evidence_excerpt":"Problem: "+n["bp"]+" Mechanism: "+n["mech"]+" Result: "+n["ww"]+" Boundary: "+n["limits"],"source_location":p["paper_url"],"source_sha256":hashlib.sha256(p["abstract"].encode()).hexdigest(),"evidence_depth":"D3","review_state":"analyst-reviewed","claim_boundary":"Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced."})
payload = {"schema_version":1,"batch_id":"interspeech-2025-semantic-d3-batch-007","status":"analyst-reviewed-D3-batch","claim_boundary":"Eight assignments are analyst-reviewed from captured official PDFs and structured notes; claims are not independent reproductions.","reviewed_count":len(rows),"rows":rows}
(DATA / "interspeech-2025-semantic-reviewed-d3-batch-007.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D3":len(rows)}))
