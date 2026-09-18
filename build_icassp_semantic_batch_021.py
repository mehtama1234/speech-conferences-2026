#!/usr/bin/env python3
"""Record the next evidence-bounded ICASSP speech concept assignments."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Reasoning Driven Captions to Assist Noise Robust Speech Emotion Recognition": (
        "meaning-and-interaction", "prosody-and-intent", "paralinguistic-state",
        "The title explicitly recognizes emotion from speech under noise; the ordinary problem is inferring a talker's affective state when the acoustic evidence is partly obscured.",
    ),
    "From Pretraining to Robustness: Benchmarking SSL Models for Noise-Robust Speech Emotion Recognition": (
        "meaning-and-interaction", "prosody-and-intent", "paralinguistic-state",
        "The title directly benchmarks noise-robust speech emotion recognition, so the conceptual target is speech-carried affective state and the failure caused by degraded evidence.",
    ),
    "An Envelope Separation Aided Multi-Task Learning Model for Blind Source Counting and Localization": (
        "listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation",
        "The title identifies blind source counting and localization with envelope separation; the ordinary problem is determining how many simultaneous sources exist and where they are without being given clean source references.",
    ),
    "β-AVSDNET: A Novel End-To-End Neural Network Architecture For Audio-Visual Speaker Diarization": (
        "recognition-and-alignment", "boundaries-and-sequence-structure", "alignment",
        "Speaker diarization assigns speaker identities across time, and the audio-visual formulation uses more than the waveform to decide where speaker turns and identity segments lie.",
    ),
    "A State-Dependent Markov Diffusion Process for Generative Speech Enhancement": (
        "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
        "The title explicitly generates enhanced speech from degraded observations; the conceptual operation is restoring speech structure while suppressing the corruption that competes with it.",
    ),
    "HyFlowSE: Hybrid End-To-End Flow-Matching Speech Enhancement via Generative-Discriminative Learning": (
        "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
        "The title makes speech enhancement the end task and combines generative and discriminative restoration, which is a direct instance of using a speech prior to remove degradation.",
    ),
    "Auditory-Inspired Transformer for Binaural Speech Enhancement and Spatial Cue Preservation": (
        "listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering",
        "The title explicitly preserves binaural spatial cues while enhancing speech; the ordinary problem is improving intelligibility without destroying the directional information that tells a listener where a talker is.",
    ),
    "End-To-End Speaker Verification with Uncertainty-Aware Evidential Scoring": (
        "people-variation-and-health", "speaker-characteristics", "speaker-verification",
        "The title names speaker verification and uncertainty-aware scoring; the ordinary decision is whether speech belongs to a claimed person while representing doubt instead of forcing every comparison into a confident match or non-match.",
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
    "batch_id": "icassp-2026-semantic-batch-021",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows),
    "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-021.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
