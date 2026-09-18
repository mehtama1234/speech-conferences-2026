#!/usr/bin/env python3
"""Adjudicate a ninth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "Characterization of voice cue sensitivity and vocal emotion recognition across the adult lifespan": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Efficient Data Selection for Domain Adaptation of ASR Using Pseudo-Labels and Multi-Stage Filtering": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "Multimodal Zero-Shot Framework for Deepfake Hate Speech Detection in Low-Resource Languages": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Synthesizing Speech with Selected Perceptual Voice Qualities – A Case Study with Creaky Voice": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation"),
    "ASR Confidence Estimation using True Class Lexical Similarity Score": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use"),
    "ReFlow-VC: Zero-shot Voice Conversion Based on Rectified Flow and Speaker Feature Optimization": ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice"),
    "On the influence of language similarity in non-target speaker verification trials": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Exploring Shared-Weight Mechanisms in Transformer and Conformer Architectures for Automatic Speech Recognition": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Running Conventional Automatic Speech Recognition on Memristor Hardware: A Simulated Approach": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Pitch Contour Model (PCM) with Transformer Cross-Attention for Speech Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Interspeech 2025 URGENT Speech Enhancement Challenge": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Speaker-Distinguishable CTC: Learning Speaker Distinction Using CTC for Multi-Talker Speech Recognition": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Multichannel Keyword Spotting for Noisy Conditions": ("listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "Can We Reconstruct a Dysarthric Voice with the Large Speech Model Parler TTS?": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "DeepFilterGAN: A Full-band Real-time Speech Enhancement System with GAN-based Stochastic Regeneration": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
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
    if c["decision"] != "supported" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not provisional supported: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paper_id"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The preserved abstract identifies a speech object and bounded intervention that instantiate {concept} under {subtheme}; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.", "evidence_excerpt": abstract[:1400] if abstract else title, "source_location": p.get("paper_url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "Official INTERSPEECH abstract evidence supports taxonomy membership; full-paper mechanism, failure analysis, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-047", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-047.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
