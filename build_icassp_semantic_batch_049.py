#!/usr/bin/env python3
"""Resolve a bounded ICASSP insufficient-evidence speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "MangaVox: Dataset of Acted Voices Aligned with Manga Images Towards Computer Understanding of Audio Comics": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "A Speech-Driven Paradigm for Physics-Informed Modeling of Coupled Micro-Speakers": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Estimating Hand-Related Features from Speech Using Machine Learning": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "An Anomaly-Aware and Audio-Enhanced Dual-Pathway Framework for Alzheimer’s Disease Progression Classification": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Cross-Domain Contrastive Learning with Dynamic Threshold Calibration for Source Speaker Tracing": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "SODA: A Unified Framework for Joint Estimation of Speaker Orientation and Direction of Arrival": ("sound-and-production", "room-channel-and-sensing", "microphone-channel"),
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
    if c["decision"] != "insufficient-evidence" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not insufficient-evidence: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paperId"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The title identifies a bounded speech-centered object that instantiates {concept} under {subtheme}; this resolves taxonomy membership only.", "evidence_excerpt": abstract[:1200] if abstract else title, "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata and, where available, abstract evidence support taxonomy membership; mechanism, performance, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-049", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve insufficient-evidence ICASSP proposals using preserved title/abstract evidence; they do not establish full-paper scientific claims.", "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-049.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
