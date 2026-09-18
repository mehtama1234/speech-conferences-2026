#!/usr/bin/env python3
"""Adjudicate a seventeenth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "On the cross-modal makeup of charisma: Insights from a field-data analysis": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Enhancing Speech Emotion Recognition with Multi-Task Learning and Dynamic Feature Fusion": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "U-SAM: An Audio Language Model for Unified Speech, Audio, and Music Understanding": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Exploiting Echo Path Priors for Enhanced Stereo Acoustic Echo Cancellation": ("listening-and-separation", "echo-and-reconstruction", "acoustic-echo-cancellation"),
    "VCapAV: A Video-Caption Based Audio-Visual Deepfake Detection Dataset": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Continual Speech Learning with Fused Speech Features": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "Can AI Understand Mandarin Speech Prosody?  A Framework and Benchmark Showcase": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Speaker Targeting via Self-Speaker Adaptation for Multi-talker ASR": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Improving Multilingual Speech Models on ML-SUPERB 2.0: Fine-tuning with Data Augmentation and LID-Aware CTC": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Robustness of F0 Ratio as a Diagnostic: Comparing Creaky Voice in Danish and Seoul Korean": ("sound-and-production", "source-filter-production", "periodic-source"),
    "Disentangling Dual-Encoder Masked Autoencoder for Respiratory Sound Classification": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Transcribing Diverse Voices: Using Whisper for ICE corpora": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "Investigating effects of sex hormones, cycle phases and age on female fundamental frequency": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation"),
    "ASVspoof2019 vs. ASVspoof5: Assessment and Comparison": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "SPCODEC: Split and Prediction for Neural Speech Codec": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "GALAXY: A Large-Scale Open-Domain Dataset for Multimodal Learning": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-032", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-032.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
