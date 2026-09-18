#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on speech-language interfaces."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Efficient Depression Detection from Speech via Language-Independent Prompt-Driven Reprogramming": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title detects depression from speech while aiming to be language-independent; the ordinary problem is separating health-related vocal evidence from the language and culture in which a person speaks.",
    ),
    "Whisper-QF: Leveraging Dual Cross-Attention Q-Former for Speech Emotion Recognition With Multi-Task Learning": (
        "meaning-and-interaction", "prosody-and-intent", "paralinguistic-state",
        "The title explicitly recognizes emotion from speech and uses cross-attention between representations; the conceptual task is inferring affective state from acoustic evidence that also carries lexical content.",
    ),
    "Hierarchical Contrastive Learning with Speech Language Model for Separating Similar Speakers": (
        "people-variation-and-health", "speaker-characteristics", "speaker-verification",
        "The title explicitly separates similar speakers with a speech language model; the ordinary problem is preserving identity distinctions when different people produce acoustically similar speech.",
    ),
    "Equipping Large Language Model with Directional Speech Understanding Capabilities": (
        "meaning-and-interaction", "grounding-and-action", "referential-grounding",
        "The title gives a language model directional speech understanding, matching the ordinary problem of connecting what was said with where the relevant sound or speaker came from.",
    ),
    "SEP-ST: Incorporating Speech Entity Prompt Into Large Language Models for Speech Translation": (
        "languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer",
        "The title explicitly translates speech while prompting on speech entities; the conceptual problem is preserving who or what is referred to as linguistic content crosses languages.",
    ),
    "Target-Speaker LLM-ASR with Speaker-Aware Speech Encoder": (
        "listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation",
        "The title conditions ASR on a target speaker through a speaker-aware encoder; the ordinary problem is transcribing one person's words while other voices are present.",
    ),
    "VChangeCodec: An Ultra Low-Complexity Neural Speech Codec with Built-In Voice Changer for Customized Real-Time Communication": (
        "voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion",
        "The title combines low-complexity speech coding with a built-in voice changer for real-time use; the conceptual tradeoff is changing perceived identity while preserving content under tight device and latency limits.",
    ),
    "Arbitrarily Settable Frame Rate Neural Speech Codec with Content Adaptive Variable Length Segmentation": (
        "evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource",
        "The title changes codec frame rate and segment length according to content, matching the deployment problem of allocating computation and bitrate where speech changes quickly without wasting resources on redundant regions.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-030",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-030.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
