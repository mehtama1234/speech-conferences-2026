#!/usr/bin/env python3
"""Record another evidence-bounded ICASSP speech concept batch."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Joint Autoregressive Modeling of Multi-Talker Overlapped Speech Recognition and Translation": (
        "recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding",
        "The title explicitly addresses recognition and translation when multiple talkers overlap; the ordinary problem is maintaining separate linguistic sequences when speech streams interfere in time.",
    ),
    "Bridging the Front-End and Back-End for Robust ASR via Cross-Attention-Based U-Net": (
        "evaluation-deployment-and-consequence", "robustness-and-system-boundary", "end-to-end-recovery",
        "The title frames robust automatic speech recognition as a connection between signal cleanup and linguistic decoding; the concept is recovery across the full chain rather than optimizing an isolated front end.",
    ),
    "Confidence-Guided Error Correction for Disordered Speech Recognition": (
        "people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech",
        "The title explicitly concerns recognition of disordered speech and confidence-guided correction, matching the ordinary problem of understanding speech whose patterns differ from typical training data.",
    ),
    "Medical ASR Enhancement by Domain-Specific Reinforcement Fine-Tuning": (
        "recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing",
        "The title identifies medical automatic speech recognition and domain-specific adaptation; the conceptual issue is shifting recognition toward specialized vocabulary and context without treating the new domain as ordinary speech.",
    ),
    "Neuromamba: Adaptive Frequency Filtering with a Pyramid Mamba for sEEG-driven Speech Synthesis": (
        "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
        "The title uses sEEG to drive speech synthesis, so the speech evidence comes from neural sensing rather than airborne sound; the central boundary is translating a different projection of speech intent into generated speech.",
    ),
    "Bridging the Semantic Gap: Cross-Attentive Fusion for Joint Acoustic-Semantic Speech Quality Assessment": (
        "evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness",
        "The title explicitly assesses speech quality from acoustic and semantic information together; the ordinary problem is judging whether speech is usable and meaningful, not merely whether its waveform resembles a reference.",
    ),
    "CodecSlime: Temporal Redundancy Compression of Neural Speech Codec via Dynamic Frame Rate": (
        "evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource",
        "The title compresses a neural speech codec by changing frame rate with temporal redundancy, directly addressing the deployment tradeoff between speech representation quality, bitrate, and computation.",
    ),
    "Low-Bandwidth High-Fidelity Speech Transmission with Generative Latent Joint Source-Channel Coding": (
        "evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource",
        "The title explicitly transmits speech under a low-bandwidth constraint while targeting fidelity; the ordinary problem is deciding what speech information to preserve when the communication channel cannot carry everything.",
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
        "paper_id": paper["paperId"],
        "title": paper["title"],
        "decision": "supported",
        "confidence": f"analyst-reviewed-{depth}",
        "theme_id": theme,
        "subtheme_id": subtheme,
        "concept_id": concept,
        "semantic_reasoning": reasoning,
        "evidence_excerpt": abstract[:1200] if abstract else paper["title"],
        "source_location": paper.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": depth,
        "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP title/abstract evidence supports broad conceptual membership; full-paper mechanism and outcomes are not captured.",
    })

if len(rows) != len(RULES):
    missing = sorted(set(RULES) - {row["title"] for row in rows})
    raise SystemExit(f"expected {len(RULES)} exact titles, missing: {missing}")

payload = {
    "schema_version": 1,
    "batch_id": "icassp-2026-semantic-batch-022",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows),
    "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-022.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
