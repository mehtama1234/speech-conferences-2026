#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on speech robustness and security."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Adversarial Fine-Tuning on Speech Foundation Model with Vulnerable Attention Consistency Regularization for Robust Speech Recognition": (
        "evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift",
        "The title explicitly makes speech recognition robust to adversarial or shifted evidence by fine-tuning a speech foundation model; the ordinary problem is keeping recognition usable when the input is deliberately or unexpectedly altered.",
    ),
    "Three-Stage BSRNN for Universal Speech Enhancement and Data Curation Using a Large Pre-Trained Speech Restoration Model": (
        "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
        "The title explicitly restores speech across universal enhancement conditions and uses a pretrained speech-restoration prior; the conceptual operation is separating speech structure from varied degradation.",
    ),
    "PG-SE: Predictive Acceleration and Correction for Generative Speech Enhancement": (
        "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
        "The title identifies generative speech enhancement with predictive acceleration and correction, matching the problem of reconstructing plausible speech without allowing the restoration model to invent unsupported detail.",
    ),
    "Uncertainty-Guided Domain Augmentation for Domain Generalization in Speaker Verification and Anti-Spoofing": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title explicitly combines speaker verification with anti-spoofing under domain variation; the ordinary security problem is distinguishing a genuine speaker from an imitation when recording conditions change.",
    ),
    "Robust Deepfake Audio Detection via Multi-Level Intermediate Feature Fusion": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title directly detects synthetic audio and emphasizes robustness, so the conceptual task is finding evidence of generated or manipulated speech rather than trusting apparent voice identity.",
    ),
    "Detecting and Attributing Synthetic Spanish Speech: The HISPASpoof Dataset": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title explicitly detects and attributes synthetic Spanish speech through a dataset, making the ordinary problem both recognizing manipulation and identifying its source or generation condition.",
    ),
    "Combining SSL Speech Features, Contextual Transformers and Mamba Models for Realistic Audio Spoofing Detection": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title directly addresses audio spoofing detection and combines speech representations with contextual sequence modeling; the conceptual boundary is deciding whether speech evidence is authentic under realistic attacks.",
    ),
    "Dynamic Spectrogram Analysis with Local-Aware Graph Networks for Audio Anti-Spoofing": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title explicitly performs audio anti-spoofing using changing spectrogram structure; the ordinary problem is detecting artifacts that unfold over time rather than classifying a speaker's identity alone.",
    ),
}

papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
rows = []
for paper in papers.values():
    if paper["title"] not in RULES:
        continue
    theme, subtheme, concept, reasoning = RULES[paper["title"]]
    abstract = paper.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({
        "paper_id": paper["paperId"], "title": paper["title"], "decision": "supported",
        "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme,
        "concept_id": concept, "semantic_reasoning": reasoning,
        "evidence_excerpt": abstract[:1200] if abstract else paper["title"],
        "source_location": paper.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": depth, "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP title/abstract evidence supports broad conceptual membership; full-paper mechanism and outcomes are not captured.",
    })

if len(rows) != len(RULES):
    missing = sorted(set(RULES) - {row["title"] for row in rows})
    raise SystemExit(f"expected {len(RULES)} exact titles, missing: {missing}")
payload = {
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-024",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-024.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
