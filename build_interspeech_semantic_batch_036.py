#!/usr/bin/env python3
"""Adjudicate a twenty-first clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "From Speech Science to Language Transparence": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "SNIFR : Boosting Fine-Grained Child Harmful Content Detection Through Audio-Visual Alignment with Cascaded Cross-Transformer": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "Knowledge Distillation Method for Pruned RNN-T Models via Pruning Bounds Sharing and Losses Confusion": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Selective Channel Attention based Target Speaker Voice Activity Detection for Speaker Diarization under AD-HOC Microphone Array Settings": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Employing self-supervised learning models for cross-linguistic child speech maturity classification": ("people-variation-and-health", "speaker-characteristics", "age-and-development"),
    "Quantifying and Reducing Speaker Heterogeneity within the Common Voice Corpus for Phonetic Analysis": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Towards atypical speech transcription using LLM-based ASR": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "On the Design of a Robust Superdirective Beamformer and Topology Parameter Optimization with Frustum-Shaped Microphone Arrays Featuring Multiple Rings": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "ClearerVoice-Studio: Bridging Advanced Speech Processing Research and Practical Deployment": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "VS-Singer: Vision-Guided Stereo Singing Voice Synthesis with Consistency Schrödinger Bridge": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "Lightweight Front-end Enhancement for Robust ASR via Frame Resampling and Sub-Band Pruning": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "TA-RIR: Topology-Aware Neural Modeling of Acoustic Propagation for Room Impulse Response Synthesis": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "Defending Unauthorized Voice Cloning with Watermark-Aware Codecs": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "The Interspeech 2025 Speech Accessibility Project Challenge": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "FreeCodec: A Disentangled Neural Speech Codec with Fewer Tokens": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "MM-MovieDubber: Towards Multi-Modal Learning for Multi-Modal Movie Dubbing": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-036", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-036.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
