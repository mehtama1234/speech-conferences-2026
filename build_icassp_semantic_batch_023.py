#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on robustness and alternate speech sensing."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Whisper with Benefits: A Unified Approach to Speech and Speaker Attribute Recognition": (
        "people-variation-and-health", "speaker-characteristics", "style-and-state-variation",
        "The title jointly recognizes speech and speaker attributes, making the conceptual problem separating what was said from properties of who is speaking and how they are speaking.",
    ),
    "A Dual-Channel ASR-LLM Architecture with a Progressive Training Strategy for Low-Resource Speech Recognition": (
        "languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation",
        "The title explicitly targets low-resource speech recognition and combines acoustic recognition with a language model; the central problem is adapting a recognizer when labeled speech is scarce.",
    ),
    "Multilingual Supervised Pretraining with Lm-Assisted Decoding for Visual Speech Recognition": (
        "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
        "Visual speech recognition observes mouth motion rather than airborne sound, so it is a different projection of the speaking act whose usefulness depends on what articulation remains visible.",
    ),
    "Hybrid Speech Enhancement with Discriminative and Codec Token Prediction Models Guided by Cleaned SSL Features for the ICASSP 2026 Urgent Challenge": (
        "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
        "The title explicitly restores speech from degraded audio using both discriminative prediction and codec tokens; the ordinary problem is preserving speech structure while removing corruption.",
    ),
    "Matching Reverberant Speech Through Learned Acoustic Embeddings": (
        "sound-and-production", "room-channel-and-sensing", "reverberant-mixture",
        "The title treats reverberant speech as speech altered by delayed room reflections; the conceptual challenge is comparing or matching utterances when the room has mixed earlier sound into the current signal.",
    ),
    "Optimization of High Directivity Beamforming and WPE Method for Improved Speech Dereverberation": (
        "listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering",
        "The title combines directional beamforming with dereverberation, matching the ordinary problem of selecting sound arriving from a desired direction while reducing the room's delayed copies.",
    ),
    "Target-Speaker Voice Activity Detection with Chunk-Level Speaker Queries": (
        "recognition-and-alignment", "boundaries-and-sequence-structure", "alignment",
        "The title asks when a particular speaker is active, so the conceptual task is placing time boundaries around one person's speech rather than treating every detected voice segment as interchangeable.",
    ),
    "A Generalization Strategy for Speech Quality Prediction: From Domain-Specific to Unified Datasets": (
        "evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness",
        "The title explicitly predicts speech quality across domains; the ordinary problem is making a listener-oriented judgment remain meaningful when recording conditions and datasets change.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-023",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-023.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
