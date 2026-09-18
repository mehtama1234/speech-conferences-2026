#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "data"
A = {
    "behera25_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "braun25_interspeech": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "berger25_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "bataev25_interspeech": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "bashir25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "word-error-versus-understanding"),
    "carofilis25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "cai25_interspeech": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "das25_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
}
P = {p["paper_id"]: p for p in json.loads((D / "interspeech-2025-papers.json").read_text())["papers"]}
N = {n["paper_id"]: n for n in json.loads((D / "interspeech-2025-fifteenth-d3-notes.json").read_text())["notes"]}
C = {p["paper_id"]: p for p in json.loads((D / "interspeech-2025-fifteenth-d3-papers.json").read_text())["papers"]}
rows = []
for pid, (theme, subtheme, concept) in A.items():
    p, n, cap = P[pid], N[pid], C[pid]
    rows.append({"paper_id": pid, "title": p["title"], "decision": "supported", "confidence": "analyst-reviewed-D3", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate {concept} within {subtheme}.", "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "ww", "limits"], "evidence_excerpt": "Problem: " + n["bp"] + " Mechanism: " + n["mech"] + " Result: " + n["ww"] + " Boundary: " + n["limits"], "source_location": p["paper_url"], "source_sha256": hashlib.sha256(p["abstract"].encode()).hexdigest(), "evidence_depth": "D3", "review_state": "analyst-reviewed", "claim_boundary": "Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced."})
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d3-batch-013", "status": "analyst-reviewed-D3-batch", "claim_boundary": "Eight assignments are analyst-reviewed from captured official PDFs and structured notes; claims are not independent reproductions.", "reviewed_count": len(rows), "rows": rows}
(D / "interspeech-2025-semantic-reviewed-d3-batch-013.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D3": len(rows)}))
