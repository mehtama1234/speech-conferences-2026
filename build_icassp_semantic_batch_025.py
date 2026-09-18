#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on clinical and assistive speech."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "ALS Detection from Phonation Audio Using Spectrogram Mosaics and Ensemble Deep Learning": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title explicitly detects ALS from phonation audio; the ordinary problem is using speech-related bodily evidence as a possible health marker while separating disease signal from ordinary speaker variation.",
    ),
    "Interval-Aware Retrieval Framework For Speech-Based Automatic Alzheimer’s Detection": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title explicitly uses speech for Alzheimer’s detection and retrieves intervals rather than treating a recording as one undifferentiated label; the concept is finding clinically relevant speech evidence while preserving uncertainty.",
    ),
    "The Speech Analysis for Neurodegenerative Diseases Challenge": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title defines a speech-analysis challenge for neurodegenerative disease, matching the ordinary problem of testing whether measurable speech changes carry health-related information without confusing prediction with diagnosis.",
    ),
    "Lend a Hand: Semi Training-Free Cued Speech Recognition via MLLM-Driven Hand Modeling for Barrier-Free Communication": (
        "people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication",
        "The title explicitly recognizes cued speech using hand information for barrier-free communication; the ordinary problem is combining visual cues with speech when ordinary audio-only access is insufficient.",
    ),
    "The 3rd Clarity Prediction Challenge: A Machine Learning Challenge for Hearing aid Speech Intelligibility Prediction": (
        "people-variation-and-health", "human-centered-evaluation", "listener-effort",
        "The title predicts hearing-aid speech intelligibility, which concerns the listener's actual effort and access rather than waveform similarity alone.",
    ),
    "Reliable AI via Age-Balanced Validation: Fair Model Selection for Parkinson’s Detection from Voice": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title explicitly detects Parkinson’s from voice and emphasizes age-balanced validation; the ordinary problem is separating health-related vocal evidence from age-related variation and other population differences.",
    ),
    "A Robust Multi-Scale Framework with Test-Time Adaptation for sEEG-Based Speech Decoding": (
        "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
        "The title decodes speech from sEEG and adapts at test time, so the signal is a neural projection of speech-related activity rather than airborne sound; robustness must account for subject and session variation.",
    ),
    "SAASDNet: An EEG-Based Streaming Auditory Attention Switch Decoding Network for Self-Initiated Attention Switching in Mixed Speech": (
        "meaning-and-interaction", "dialogue-and-turn-taking", "interactional-feedback",
        "The title decodes when auditory attention switches during mixed speech, matching the interaction problem of determining which competing stream a listener is selecting at a moment in time.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-025",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-025.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
