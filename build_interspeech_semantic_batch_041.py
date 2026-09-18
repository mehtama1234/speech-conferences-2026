#!/usr/bin/env python3
"""Adjudicate a third provisional INTERSPEECH D2 speech slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Automatic Dialectal Transcription: An Evaluation on Finnish and Norwegian": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "GigaAM: Efficient Self-Supervised Learner for Speech Recognition": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Bona fide Cross Testing Reveals Weak Spot in Audio Deepfake Detection Systems": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Improving Synthetic Data Training for Contextual Biasing Models with a Keyword-Aware Cost Function": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "Efficient Trie-based Biasing using K-step Prediction for Rare Word Recognition": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "VoiceQualityVC: A Voice Conversion System for Studying the Perceptual Effects of Voice Quality in Speech": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "HiFiTTS-2: A Large-Scale High Bandwidth Speech Dataset": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Exploring Generative Error Correction for Dysarthric Speech Recognition": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Multistage Universal Speech Enhancement System for URGENT Challenge": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "DGMO: Training-Free Audio Source Separation through Diffusion-Guided Mask Optimization": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "SSPS: Self-Supervised Positive Sampling for Robust Self-Supervised Speaker Verification": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Robust Vocal Intensity Prediction: Overcoming Dataset Bias with Pretrained Deep Models": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation"),
    "Zero-Shot Mono-to-Binaural Speech Synthesis": ("voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency"),
    "Towards One-bit ASR: Extremely Low-bit Conformer Quantization Using Co-training and Stochastic Precision": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Leveraging Large Language Models for Sarcastic Speech Annotation in Sarcasm Detection": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Temporal Convolutional Network with Smoothed and Weighted Losses for Distant Voice Activity and Overlapped Speech Detection": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-041", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-041.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
