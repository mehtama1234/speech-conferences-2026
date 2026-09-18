#!/usr/bin/env python3
"""Resolve the remaining clearly out-of-scope INTERSPEECH audio rows."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
TITLES = {
    "InfiniteAudio: Infinite-Length Audio Generation with Consistency": "The title describes unconstrained audio generation, not a speech, voice, language, or spoken-interaction problem.",
    "Improving Linguistic Diversity of Large Language Models with Possibility Exploration Fine-Tuning": "The title identifies a general language-model diversity method without a speech or spoken-language object.",
    "Beyond Conventional Metrics: using Entropic Triangles to Explain Balancing Methods in Acoustic Scene Classification": "Acoustic scene classification concerns environmental sound scenes rather than speech or spoken interaction.",
    "StarGAN-Aug: A Cross-domain Fault Audio Generation Method for High-performance Fault Diagnosis of Power Transformers": "The paper targets transformer fault audio, outside speech production, perception, recognition, and interaction.",
    "TinyClick: Single-Turn Agent for Empowering GUI Automation": "The title describes GUI automation without a speech-specific object or spoken communication problem.",
    "Adaptive Across-Subcenter Representation Learning for Imbalanced Anomalous Sound Detection": "Anomalous sound detection is not a speech-specific recognition, production, or interaction task.",
    "Anomalous Sound Detection Based Feature Fusion and Dual-path Non-linear Independent Components Estimation": "The title identifies generic anomalous-sound detection, not a speech or voice problem.",
    "TVC-MusicGen: Time-Varying Structure Control for Background Music Generation via Self-Supervised Training": "The title targets background music generation rather than speech or spoken interaction.",
    "EnvSDD: Benchmarking Environmental Sound Deepfake Detection": "Environmental sound deepfake detection is outside the speech/deepfake voice boundary of this atlas.",
    "Training Onset-and-Offset-Aware Sound Event Detection  on a Heterogeneous Dataset via Probabilistic Sequential Modeling": "The paper targets generic sound-event detection, not speech activity, speech recognition, or spoken interaction.",
    "DiffStereo: End-to-End Mono-to-Stereo Audio Generation with Diffusion Transformer": "The title describes generic stereo audio generation without a speech-specific object.",
}
queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
by_title = {r["title"]: r for r in queue["rows"]}
already = set()
for path in DATA.glob("interspeech-2025-semantic-reviewed-*.json"):
    already |= {r["paper_id"] for r in json.loads(path.read_text()).get("rows", [])}
missing = [t for t in TITLES if t not in by_title or by_title[t]["paper_id"] in already]
if missing:
    raise SystemExit(f"missing or already reviewed: {missing}")
rows = []
for title, reasoning in TITLES.items():
    c = by_title[title]
    if c["decision"] != "ambiguous" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not unresolved ambiguous: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paper_id"], "title": title, "decision": "unsupported", "confidence": f"analyst-reviewed-{depth}", "theme_id": None, "subtheme_id": None, "concept_id": None, "semantic_reasoning": reasoning, "evidence_fields": ["title", "abstract"] if abstract else ["title"], "evidence_excerpt": abstract[:1400] if abstract else title, "source_location": p.get("paper_url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "Official abstract/title evidence was sufficient to establish that the paper is outside the speech taxonomy; no speech concept is assigned."})
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-out-of-scope-batch-038", "status": "analyst-reviewed-explicit-out-of-scope-batch", "claim_boundary": "These records resolve clearly non-speech rows using title and abstract evidence; they remain visible as unsupported corpus records.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-out-of-scope-batch-038.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
