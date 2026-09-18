#!/usr/bin/env python3
"""Adjudicate a fifth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Developing a High-performance Framework for Speech Emotion Recognition in Naturalistic Conditions Challenge for Emotional Attribute Prediction": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "An Exploration of Interpretable Deep Learning Models for the Assessment of Mild Cognitive Impairment": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Towards the Objective Characterisation of Major Depressive Disorder Using Speech Data from a 12-week Observational Study with Daily Measurements": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "DualCodec: A Low-Frame-Rate, Semantically-Enhanced Neural Audio Codec for Speech Generation": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "Efficient Noise-Robust Hybrid Audiovisual Encoder  with Joint Distillation and Pruning for Audiovisual Speech Recognition": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Acoustic Representation and Realization of Weak Elements Subcategories: In the Case of Tianjin Mandarin": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Disentangling Speaker and Content in Pre-trained Speech Models with Latent Diffusion for Robust Speaker Verification": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "DepressGEN: Synthetic Data Generation Framework for Depression Detection": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "WhisperMSS: A Two-Stage Framework for Mandarin Singing Transcription and Segmentation Using Pretrained Models": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "LightL2S: Ultra-Low Complexity Lip-to-Speech Synthesis for Multi-Speaker Scenarios": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "Mitigating Subgroup Disparities in Multi-Label Speech Emotion Recognition: A Pseudo-Labeling and Unsupervised Learning Approach": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Defend for Self-Vocoding: A Novel Enhanced Decoder Network for Watermark Recovery": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "Decoding Listener's Identity: Person Identification from EEG Signals Using a Lightweight Spiking Transformer": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "CNVSRC 2024: The Second Chinese Continuous Visual Speech Recognition Challenge": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Leveraging Cascaded Binary Classification and Multimodal Fusion for Dementia Detection through Spontaneous Speech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Interactive Fusion of Multi-View Speech Embeddings via Pretrained Large-Scale Speech Models for Speech Emotional Attribute Prediction in Naturalistic Conditions": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
}

queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
by_title = {r["title"]: r for r in queue["rows"]}
already = set()
for path in DATA.glob("interspeech-2025-semantic-reviewed-*.json"):
    already |= {r["paper_id"] for r in json.loads(path.read_text()).get("rows", [])}
missing = [t for t in ASSIGNMENTS if t not in by_title or by_title[t]["paper_id"] in already]
if missing:
    raise SystemExit(f"missing or already reviewed: {missing}")
rows = []
for title, (theme, subtheme, concept) in ASSIGNMENTS.items():
    c = by_title[title]
    if c["decision"] != "ambiguous" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not unresolved ambiguous: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paper_id"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The title and preserved abstract identify a speech object and bounded intervention that instantiate {concept} under {subtheme}; this resolves taxonomy membership only.", "evidence_excerpt": abstract[:1400] if abstract else title, "source_location": p.get("paper_url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "Official INTERSPEECH abstract evidence supports taxonomy membership; full-paper mechanism, failure analysis, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-020", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-020.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
