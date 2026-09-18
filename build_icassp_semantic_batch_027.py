#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on generated and expressive speech."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Leveraging Large Speech Language Models as Evaluators for Expressive Speech": (
        "evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness",
        "The title evaluates expressive speech with large speech-language models; the ordinary problem is judging whether generated speech conveys a desired style or feeling, not only whether words are intelligible.",
    ),
    "A Dynamic Gated Cross-Attention Framework for Audio-Text Apparent Personality Analysis": (
        "meaning-and-interaction", "prosody-and-intent", "paralinguistic-state",
        "The title analyzes apparent personality from audio and text, matching the problem of inferring a speaker's social or affective presentation from signals beyond lexical content.",
    ),
    "Wavenext 2: Convnext-Based Fast Neural Vocoders with Residual Denoising and Sub-Modeling for Gan And Diffusion Models": (
        "voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder",
        "The title explicitly develops fast neural vocoders and residual denoising; the conceptual task is turning an intermediate speech representation into a waveform without losing audible detail or making generation too slow.",
    ),
    "Robust and Efficient Autoregressive Speech Synthesis with Dynamic Chunk-Wise Prediction Policy": (
        "voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning",
        "The title explicitly synthesizes speech autoregressively while changing prediction chunk size; the ordinary problem is coordinating future speech detail with generation speed and stability.",
    ),
    "MSBench: Can Speech Language Models Generate Multi-Speaker Dialogues in One Passƒ": (
        "meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state",
        "The title evaluates one-pass generation of multi-speaker dialogue, matching the problem of maintaining who is speaking, what has been said, and when a conversational turn changes.",
    ),
    "T-Cache: Fast Inference For Masked Generative Transformer-Based TTS Via Prompt-Aware Feature Caching": (
        "voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency",
        "The title accelerates text-to-speech inference by caching prompt-aware features; the conceptual tradeoff is making generated speech responsive without discarding the conditioning that controls its voice and style.",
    ),
    "Retrieval-Based Speculative Decoding For Autoregressive Speech Synthesis": (
        "voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency",
        "The title uses retrieval and speculative decoding to speed autoregressive speech synthesis, directly addressing the ordinary problem of producing controlled speech quickly enough for interactive use.",
    ),
    "Synthetic yet Striking? Assessing Vocal Charisma in TTS via Perceptual and Algorithmic Measures": (
        "voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control",
        "The title assesses vocal charisma in text-to-speech with listener and algorithmic measures; the ordinary problem is controlling a socially perceived quality that is not reducible to word accuracy or pitch alone.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-027",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-027.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
