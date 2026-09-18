#!/usr/bin/env python3
"""Adjudicate the remaining clear speech/audio ICASSP D1 candidates in this slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Domain Partitioning Meets Parameter-Efficient Fine-Tuning: A Novel Method for Improved Language-Queried Audio Source Separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "RIR-Former: Coordinate-Guided Transformer for Continuous Reconstruction of Room Impulse Responses": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "NeuroSIFT: A Biologically-Inspired Framework with Explicit Signal-Noise Separation for Robust Multimodal Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "The Synergistic Role of Audio and Large Video-Language Model in Source-Free Video Domain Adaptation": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
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
    if c["decision"] != "supported" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not provisional supported: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    rows.append({"paper_id": p["paperId"], "title": title, "decision": "supported", "confidence": "analyst-reviewed-D1", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The title identifies a bounded speech/audio problem that instantiates {concept} under {subtheme}; this is a taxonomy assignment, not a mechanism or performance claim.", "evidence_excerpt": title, "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": "D1", "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata supports taxonomy membership only; abstract/full-paper mechanism, failure analysis, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-047", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records are explicit speech/audio-taxonomy assignments supported by title evidence only; they do not establish paper mechanisms, outcomes, or reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-047.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": len(rows)}))
