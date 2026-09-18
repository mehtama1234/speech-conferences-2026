#!/usr/bin/env python3
"""Assign another explicit batch of speech papers to first-principles concepts."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
already = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    if path.name != "icassp-2026-semantic-reviewed-batch-037.json":
        already.update(r["paper_id"] for r in json.loads(path.read_text()).get("rows", []))
assignments = {
    "Mitigating False Alarms in Open-Set Speaker Identification with a Decoupled Framework": ("people-and-variation", "speaker-characteristics", "speaker-verification"),
    "Automatic Estimation of Speaker Diarization Error Rate Based on Features of Audio Quality and Speaker Discriminability": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use"),
    "ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "On The Design of Efficient Neural Methods for Geometry-Agnostic Multichannel Speech Enhancement": ("listening-and-separation", "noise-enhancement", "spectral-mask"),
    "Modeling Inter-Segment Relationships in Speech for Dementia Detection with Audio Spectrogram Transformers and Graph Attention Networks": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Temporal Graph Modeling for Speech Emotion Recognition Using LSTM-Aggregated Multigraph Networks": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Probing Content and Channel in Speaker Verification Models": ("people-and-variation", "speaker-characteristics", "speaker-verification"),
    "Production-Scale Dynamic Vocabulary ASR Biasing with Word-Level FST and Robust Training": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
}
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
by_title = {r["title"]: r for r in queue["rows"]}
missing = [t for t in assignments if t not in by_title or by_title[t]["paper_id"] in already]
if missing:
    raise SystemExit(f"missing or already reviewed requested titles: {missing}")
rows = []
for title, (theme, subtheme, concept) in assignments.items():
    p = papers[by_title[title]["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paperId"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The title and preserved abstract identify a speech problem and a mechanism that directly instantiates the {concept} concept under {subtheme}.", "evidence_excerpt": abstract[:1200] if abstract else title, "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance or prevalence claim."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-037", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These eight records are explicit speech-taxonomy assignments supported by title and, where available, abstract evidence; D2 does not imply full-paper verification.", "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-037.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
