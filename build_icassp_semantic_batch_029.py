#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on spatial acoustics and devices."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Low-Latency Audio Front-End Region-of-Interest Beamforming for Smart Glasses": (
        "listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering",
        "The title explicitly beamforms a region of interest on smart glasses with low latency; the ordinary problem is emphasizing the sound a wearer wants while suppressing competing sounds without making interaction feel delayed.",
    ),
    "Semi-Supervised GNN for Sound Source Localization with Prediction Intervals": (
        "listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering",
        "The title localizes sound sources and reports prediction intervals, matching the physical problem of inferring direction from sensor differences while representing uncertainty about that direction.",
    ),
    "Sound Source Localization Using Relative Circular Harmonic Coefficients": (
        "listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering",
        "The title localizes sound using relative circular-harmonic measurements; the ordinary problem is recovering where a source is from how sound reaches an array, rather than from its content alone.",
    ),
    "Sequential and Simultaneous Optimization of Microphone Array Geometry and Region-of-Interest Beamforming": (
        "sound-and-production", "room-channel-and-sensing", "microphone-channel",
        "The title jointly designs microphone placement and beamforming, matching the fact that the device geometry changes which spatial evidence can be recovered before any learned processing begins.",
    ),
    "From Fixed Positions to Free-Form Signals: Virtual Microphone Signal Estimation for General-Purpose Spatial Audio Processing": (
        "sound-and-production", "room-channel-and-sensing", "microphone-channel",
        "The title estimates signals at virtual microphone positions, matching the ordinary device problem of reconstructing what a sensor would have heard at a location where no microphone was placed.",
    ),
    "Regularized Inverse Filter Design for Rigid Spherical Microphone Array Processing: Laplace- And Time-Domain Representations": (
        "sound-and-production", "room-channel-and-sensing", "microphone-channel",
        "The title designs inverse filters for a spherical microphone array; the conceptual problem is undoing or reshaping the array's measurement response without amplifying noise and modeling error without bound.",
    ),
    "Group-Sparse Gaussian Process Regression for Inhomogeneous Sound Field Estimation": (
        "sound-and-production", "room-channel-and-sensing", "reverberant-mixture",
        "The title estimates a spatially varying sound field from sparse measurements, matching the ordinary room problem of inferring sound at unmeasured places when sources and reflections make the field nonuniform.",
    ),
    "A Learning-Based Automotive Sound Field Reproduction Method Using Plane-Wave Decomposition and Multi-Position Constraint": (
        "sound-and-production", "room-channel-and-sensing", "reverberant-mixture",
        "The title reproduces an automotive sound field from plane-wave components under multiple-position constraints; the ordinary problem is controlling what listeners hear across a cabin rather than at one ideal microphone.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-029",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-029.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
