#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on usefulness and deployment."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Condition-Invariant fMRI decoding of speech intelligibility with deep state space model": (
        "people-variation-and-health", "human-centered-evaluation", "listener-effort",
        "The title decodes speech intelligibility from fMRI across conditions; the ordinary problem is measuring whether speech is accessible to a listener without reducing intelligibility to a clean-room acoustic score.",
    ),
    "IRIS: Low-Complexity High-Efficiency Neural Network Codec for Real-Time Audio Transmission": (
        "evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource",
        "The title explicitly targets low-complexity real-time audio transmission, matching the deployment tradeoff between preserving usable speech and meeting bitrate, computation, and delay limits.",
    ),
    "SpatialNet-Echo: Real-Time Acoustic Echo Cancellation via Integrated Narrow-Band and Cross-Band Processing": (
        "listening-and-separation", "echo-and-reconstruction", "acoustic-echo-cancellation",
        "The title explicitly cancels acoustic echo in real time; the ordinary problem is letting a far-end conversation remain intelligible while loudspeaker playback leaks back into the microphone.",
    ),
    "Low-Frequency Harmonic Control for Speech Intelligibility in Open-Ear Headphones": (
        "people-variation-and-health", "human-centered-evaluation", "listener-effort",
        "The title controls low-frequency harmonics to improve speech intelligibility in open-ear headphones, matching the human problem of hearing speech while preserving awareness of the surrounding environment.",
    ),
    "Emilia-NV: A Non-Verbal Speech Dataset with Word-Level Annotation for Human-Like Speech Modeling": (
        "languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection",
        "The title creates a word-level dataset for non-verbal speech, addressing the ordinary data problem that vocal sounds without ordinary words still carry communicative information that standard transcripts omit.",
    ),
    "PADAM: Perceptual Audio Defect Assessment Model": (
        "evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness",
        "The title assesses perceptual audio defects, matching the ordinary evaluation problem of identifying artifacts that listeners notice even when a numerical signal metric appears acceptable.",
    ),
    "NanoCodec: Towards Low Bitrate and Low Complexity Real-Time Neural Audio Codec": (
        "evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource",
        "The title explicitly combines low bitrate, low complexity, and real-time neural coding; the conceptual tradeoff is deciding which speech detail can be discarded without damaging communication.",
    ),
    "A Long-Form Single-Speaker Real-Time MRI Speech Dataset and Benchmark": (
        "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
        "The title provides long-form real-time MRI speech data, where imaging observes vocal-tract motion rather than ordinary airborne sound; the dataset makes that alternate physical projection usable for speech research.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-032",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-032.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
