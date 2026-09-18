#!/usr/bin/env python3
"""Resolve a clear ICASSP audio-deepfake slice from ambiguous proposals."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Few-Shot Recognition of Audio Deepfake Generators using Graph-Based Prototype Adaptation": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Discrete-Continuous Fusion With Adaptive Hierarchical Features For Audio Deepfake Detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "KAN We Make Models Simpler for Audio Deepfake Detection with Kolmogorov–Arnold Networks?": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Auxiliary Multi-Label Training For Improving the Robustness of Audio Deepfake Detection on AI-Processed Data": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
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
    rows.append({"paper_id": p["paperId"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": "The title and preserved abstract identify audio-deepfake detection, a bounded security problem that instantiates spoofing-and-deepfake; this resolves taxonomy membership only.", "evidence_excerpt": abstract[:1200] if abstract else title, "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata and, where available, abstract evidence support taxonomy membership; mechanism, performance, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-050", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve ambiguous ICASSP audio-deepfake proposals using preserved title/abstract evidence; they do not establish full-paper scientific claims.", "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-050.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
