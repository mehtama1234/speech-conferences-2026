#!/usr/bin/env python3
"""Assign a small, explicit batch of unmistakable speech papers."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
already_reviewed = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    if path.name != "icassp-2026-semantic-reviewed-batch-036.json":
        already_reviewed.update(row["paper_id"] for row in json.loads(path.read_text()).get("rows", []))
assignments = {
    "Enhancing Speaker Verification with Layer-Wise Mixture-of-Experts on Pre-Trained Models": ("people-and-variation", "speaker-characteristics", "speaker-verification"),
    "Uncertainty Factorization with Linear-Time Sequential Modeling for Speaker Embedding": ("people-and-variation", "speaker-characteristics", "speaker-verification"),
    "Grey-Box Prompt Tuning With Graph Alignment for Speech-Language Models": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "S-PHiNe: Physics-Informed Multichannel Speech Enhancement Using Spectro-Spatial Fusion for Low-SNR Conditions": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Speech Emotion Recognition based on Hierarchical Transformer with Shifted Windows": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Neural Variable Span Filters for Interpretable Multi-Channel Speech Enhancement": ("listening-and-separation", "noise-enhancement", "spectral-mask"),
    "Abs-Hunet: An Ultra-Lightweight Speech Enhancement Model with Adaptive Band-Split and Half-Unet Design": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Mambaformer: State-Space Augmented Self-Attention with Downup Sampling for Monaural Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
}
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
by_title = {row["title"]: row for row in queue["rows"]}
missing = [title for title in assignments if title not in by_title or by_title[title]["paper_id"] in already_reviewed]
if missing:
    raise SystemExit(f"missing or already reviewed requested titles: {missing}")
rows = []
for title, (theme_id, subtheme_id, concept_id) in assignments.items():
    candidate = by_title[title]; paper = papers[candidate["paper_id"]]
    abstract = paper.get("abstract") or ""; depth = "D2" if abstract else "D1"
    rows.append({"paper_id": paper["paperId"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme_id, "subtheme_id": subtheme_id, "concept_id": concept_id, "semantic_reasoning": f"The title and preserved abstract identify a speech task and a mechanism that directly instantiates the {concept_id} concept under the {subtheme_id} subtheme.", "evidence_excerpt": abstract[:1200] if abstract else title, "source_location": paper.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance or prevalence claim."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-036", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These eight records are explicit speech-taxonomy assignments supported by title and, where available, abstract evidence; D2 does not imply full-paper verification.", "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-036.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
