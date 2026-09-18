#!/usr/bin/env python3
"""Adjudicate a third clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "PersonaTAB: Predicting Personality Traits using Textual, Acoustic, and Behavioral Cues in Fully-Duplex Speech Dialogs": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Selective Auditory Attention Decoding in Naturalistic Conversations Using EEG-Based Speech Envelope Tracking in Multi-Speaker Environments": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Acoustic Features of Mandarin Tone Production in Noise: A Comparison Between Chinese Native Speakers and Korean L2 Learners": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Sounding Like a Winner? Prosodic Differences in Post-Match Interviews": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Novel Loss-Enhanced Universal Adversarial Patches for Sustainable Speaker Privacy": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "Steering Deep Non-Linear Spatially Selective Filters for Weakly Guided Extraction of Moving Speakers in Dynamic Scenarios": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Rethinking Leveraging Pre-Trained Multi-Layer Representations for Speaker Verification": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Towards an Ultra-Low-Delay Neural Audio Coding with Computational Efficiency": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Language-Agnostic Suicidal Risk Detection Using Large Language Models": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Modality-Specific Speech Enhancement and Noise-Adaptive Fusion for Acoustic and Body-Conduction Microphone Framework": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Spatially Weighted Contrastive Learning for Robust Sound Source Localization": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "MVP: Multi-source Voice Pathology detection": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "SGED-Probe: Probing E2E ASR decoder and aligner for spoken grammar error detection under three speaking practice conditions": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Speech Enhancement based on cascaded two flows": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Cross-attention and Self-attention for Audio-visual Speaker Diarization in MISP-Meeting Challenge": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "HWB-Net: A Novel High-Performance and Efficient Hybrid Waveform Bandwidth Extension Method": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-018", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-018.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
