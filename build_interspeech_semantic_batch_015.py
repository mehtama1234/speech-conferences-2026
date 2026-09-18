#!/usr/bin/env python3
"""Adjudicate clear INTERSPEECH ambiguous cases at title/abstract depth."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "Neural Speech Extraction with Human Feedback": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Whisper-Based Multilingual Alzheimer's Disease Detection and Improvements for Low-Resource Language": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Contrastive Learning-based Syllable-Level Mispronunciation Detection and Diagnosis for Speech Audiometry": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "End-to-End DOA-Guided Speech Extraction in Noisy Multi-Talker Scenarios": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "An Exploratory Framework for LLM-assisted Human Annotation of Speech Datasets": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "MATER: Multi-level Acoustic and Textual Emotion Representation for Interpretable Speech Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "TELVID: A Multilingual Multi-modal Corpus for Speaker Recognition": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Diarization-Guided Multi-Speaker Embeddings": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "On the Within-class Variation Issue in Alzheimer's Disease Detection": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "VocalAgent: Large Language Models for Vocal Health Diagnostics with Safety-Aware Evaluation": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Stack Less, Repeat More: A Block Reusing Approach for Progressive Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "A Hybrid Approach to Combining Role Diarization with ASR for Professional Conversations": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "Spotlight-TTS: Spotlighting the Style via Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "Open-Set Source Tracing of Audio Deepfake Systems": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Towards Classification of Typical and Atypical Disfluencies: A Self Supervised Representation Approach": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation"),
    "Lightweight and Robust Multi-Channel End-to-End Speech Recognition with Spherical Harmonic Transform": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Multimodal Speech-Based Biomarkers Outperform the ALS Functional Rating Scale in Predicting Individual Disease Progression in ALS": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "“KAN you hear me?” Exploring Kolmogorov-Arnold Networks for Spoken Language Understanding": ("meaning-and-interaction", "grounding-and-action", "intent-in-context"),
    "Towards Frame-level Quality Predictions of Synthetic Speech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "xLSTM-SENet: xLSTM for Single-Channel Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Parameter-Efficient Fine-Tuning for Low-Resource Text-to-Speech via Cross-Lingual Continual Learning": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "Real-Time Diffusion Buffer for Speech Enhancement On A Laptop": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Articulatory Feature Prediction from Surface EMG during Speech Production": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Vo-Ve: An Explainable Voice-Vector for Speaker Identity Evaluation": ("voice-generation-and-control", "voice-identity-and-conversion", "speaker-identity"),
    "Towards Inclusive ASR: Investigating Voice Conversion for Dysarthric Speech Recognition in Low-Resource Languages": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "VoiceMark: Zero-Shot Voice Cloning-Resistant Watermarking Approach Leveraging Speaker-Specific Latents": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "Bayesian Learning for Domain-Invariant Speaker Verification and Anti-Spoofing": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Speaker Diarization with Overlapping Community Detection Using Graph Attention Networks and Label Propagation Algorithm": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Delayed-KD: Delayed Knowledge Distillation based CTC for Low-Latency Streaming ASR": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "The Development of Speech Rhythm in Putonghua-Learning Preschool Children in South Xinjiang Uyghur Autonomous Region of China": ("people-variation-and-health", "speaker-characteristics", "age-and-development"),
    "MASV: Speaker Verification with Global and Local Context Mamba": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "E2E-BPVC: End-to-End Background-Preserving Voice Conversion via In-Context Learning": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
}

queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
by_title = {row["title"]: row for row in queue["rows"]}
already = set()
for path in DATA.glob("interspeech-2025-semantic-reviewed-*.json"):
    already |= {row["paper_id"] for row in json.loads(path.read_text()).get("rows", [])}
missing = [title for title in ASSIGNMENTS if title not in by_title or by_title[title]["paper_id"] in already]
if missing:
    raise SystemExit(f"missing or already reviewed: {missing}")

rows = []
for title, (theme, subtheme, concept) in ASSIGNMENTS.items():
    candidate = by_title[title]
    if candidate["decision"] != "ambiguous" or candidate["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not an unresolved ambiguous case: {title}")
    paper = papers[candidate["paper_id"]]
    abstract = paper.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({
        "paper_id": paper["paper_id"], "title": title, "decision": "supported",
        "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept,
        "semantic_reasoning": f"The title and preserved abstract identify a speech problem whose object and intended intervention fit {concept} under {subtheme}; the assignment does not claim performance beyond the available source.",
        "evidence_excerpt": abstract[:1400] if abstract else title,
        "source_location": paper.get("paper_url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": depth, "review_state": "analyst-reviewed",
        "claim_boundary": "Official INTERSPEECH abstract evidence supports taxonomy membership; full-paper mechanism, failure analysis, and independent reproduction remain unestablished.",
    })
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-015", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-015.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
