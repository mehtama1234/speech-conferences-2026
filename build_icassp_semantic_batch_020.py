#!/usr/bin/env python3
"""Record a small analyst-reviewed set of ICASSP speech assignments.

These assignments are intentionally evidence-bounded: ICASSP title/abstract
metadata supports conceptual membership, but does not support claims about the
paper's full mechanism, experiments, or results.
"""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "A Framework for Controlled Multi-Speaker Audio Synthesis for Robustness Evaluation of Speaker Diarisation Systems": (
        "people-variation-and-health", "speaker-characteristics", "speaker-verification",
        "The paper explicitly constructs controlled multi-speaker audio for diarisation robustness, so its speech concept is variation in speaker evidence and identity rather than generic audio synthesis.",
    ),
    "pTSE-T: Presentation Target Speaker Extraction Using Unaligned Text Cues": (
        "listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation",
        "The title states that a target speaker is extracted from a mixture using text cues; the ordinary problem is isolating one person's speech when several sources are present.",
    ),
    "PSTalker: Realistic 3D Talking Head Synthesis via a Semantic-Aware Audio-Driven Point-Based Shape": (
        "voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning",
        "The title identifies audio-driven talking-head generation with semantic control; the bounded speech concept is generating a visible speaking performance from speech content, not merely rendering an arbitrary object.",
    ),
    "Joint Multichannel Acoustic Feedback Cancellation and Speaker Extraction via Kalman Filter and Deep Non-Linear Spatial Filter": (
        "listening-and-separation", "echo-and-reconstruction", "acoustic-echo-cancellation",
        "The title directly names acoustic feedback cancellation together with speaker extraction, matching the ordinary problem of recovering a talker's signal while a playback path feeds sound back into the microphones.",
    ),
    "SNR-Progressive TF-GridNet for Single-Channel Low-SNR Radar Acoustic Speech Enhancement": (
        "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
        "The title explicitly concerns speech enhancement at low signal-to-noise ratio; the conceptual operation is suppressing competing noise while preserving speech evidence in one channel.",
    ),
    "Curriculum Learning with Contrastive Loss for Lightweight Speaker Verification": (
        "people-variation-and-health", "speaker-characteristics", "speaker-verification",
        "The title identifies speaker verification, whose ordinary problem is deciding whether two speech samples come from the same claimed person under variation in recording and speaking conditions.",
    ),
    "PosSpec-Net: Enhancing Radar-Based Speech Signals via U-Nets and Positional Vectors": (
        "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
        "The title explicitly treats radar-based speech signals, which are a non-airborne projection of speech that must be enhanced before speech information can be recovered.",
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
    "batch_id": "icassp-2026-semantic-batch-020",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows),
    "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-020.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
