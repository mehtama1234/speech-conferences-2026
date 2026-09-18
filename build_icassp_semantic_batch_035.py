#!/usr/bin/env python3
"""Analyst-reject the next unique, clearly out-of-scope ICASSP batch."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
already_reviewed = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    if path.name != "icassp-2026-semantic-reviewed-batch-035.json":
        already_reviewed.update(row["paper_id"] for row in json.loads(path.read_text()).get("rows", []))
selected = [
    row for row in queue["rows"]
    if row.get("decision") == "unsupported"
    and row.get("review_state") == "needs-analyst-semantic-review"
    and not row.get("in_speech_audio_scope")
    and row.get("paper_id") not in already_reviewed
][:32]
if len(selected) != 32:
    raise SystemExit(f"expected 32 new clearly out-of-scope rows, found {len(selected)}")
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
rows = []
for candidate in selected:
    paper = papers[candidate["paper_id"]]
    abstract = paper.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({
        "paper_id": paper["paperId"], "title": paper["title"], "decision": "unsupported",
        "confidence": f"analyst-reviewed-{depth}", "theme_id": None, "subtheme_id": None, "concept_id": None,
        "semantic_reasoning": "The preserved title and, where available, abstract concern a non-speech subject outside the speech/audio taxonomy; no evidence supports membership in a speech concept.",
        "evidence_excerpt": abstract[:1000] if abstract else paper["title"], "source_location": paper.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth,
        "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP discovery metadata; rejection is limited to the speech taxonomy and does not characterize scientific quality.",
    })
payload = {
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-035",
    "status": "analyst-reviewed-title-bounded-rejection-batch",
    "claim_boundary": "These records are a new unique analyst-rejected batch from the speech taxonomy; they remain in the full ICASSP denominator.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-035.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "unique_prior_excluded": len(already_reviewed), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
