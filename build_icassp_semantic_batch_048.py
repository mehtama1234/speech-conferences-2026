#!/usr/bin/env python3
"""Resolve a bounded batch of clear speech/audio ICASSP ambiguous proposals."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Dynamic Noise-Aware Multi Lora Framework Towards Real-World Audio Deepfake Detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Two-Stage Language Model Framework for Acoustic Echo Cancellation": ("listening-and-separation", "echo-and-reconstruction", "acoustic-echo-cancellation"),
    "An Unsupervised Alignment Feature Fusion System for Spoken Language-Based Dementia Detection": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "EdgeSpot: Efficient and High-Performance Few-Shot Model for Keyword Spotting": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "Stereophonic Acoustic Echo Cancellation Using an Improved Affine Projection Algorithm with Adaptive Multiple Sub-Filters": ("listening-and-separation", "echo-and-reconstruction", "acoustic-echo-cancellation"),
    "Beamforming Using Virtual Microphones for Hearing Aid Applications": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "AVATAR: Audio-Visual Adaptive Fusion via Trained Agent Reinforcement for Multimodal Deepfake Detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "When Voice Matters: A Controlled Study of Audio LLM Behavior in Clinical Decision-Making": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
}
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
by_title = {r["title"]: r for r in queue["rows"]}
already = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    already |= {r["paper_id"] for r in json.loads(path.read_text()).get("rows", [])}
missing = [t for t in ASSIGNMENTS if t not in by_title or by_title[t]["paper_id"] in already]
if missing:
    raise SystemExit(f"missing or already reviewed: {missing}")
rows = []
for title, (theme, subtheme, concept) in ASSIGNMENTS.items():
    c = by_title[title]
    if c["decision"] != "ambiguous" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not ambiguous: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paperId"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The title and preserved abstract identify a bounded speech/audio problem that instantiates {concept} under {subtheme}; this resolves taxonomy membership only.", "evidence_excerpt": abstract[:1200] if abstract else title, "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata and, where available, abstract evidence support taxonomy membership; mechanism, performance, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-048", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve ambiguous ICASSP proposals using preserved title/abstract evidence; they do not establish full-paper scientific claims.", "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-048.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
