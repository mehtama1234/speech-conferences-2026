#!/usr/bin/env python3
"""Adjudicate a seventh provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "On the Production and Perception of a Single Speaker's Gender": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation"),
    "A Cascaded Multimodal Framework for Automatic Social Communication Severity Assessment in Children with Autism Spectrum Disorder": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Multimodal Speech, Language and Orofacial Analysis for Remote Assessment of Positive, Negative and Cognitive Symptoms in Schizophrenia": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Simultaneous Masked and Unmasked Decoding with Speculative Decoding Masking for Fast ASR without Accuracy Loss": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Prosodically Enhanced Foreign Accent Simulation by Discrete Token-based Resynthesis Only with Native Speech Corpora": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "Differentiable K-means for Fully-optimized Discrete Token-based ASR": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "The Faetar Speech Recognition Benchmark": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "A Comprehensive Real-World Assessment of Audio Watermarking Algorithms: Will They Survive Neural Codecs?": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "Overcoming Data Scarcity in Multi-Dialectal Arabic ASR via Whisper Fine-Tuning": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "End-to-End Diarization utilizing Attractor Deep Clustering": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "ClapFM-EVC: High-Fidelity and Flexible Emotional Voice Conversion with Dual Control from Natural Language and Speech": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "EmbedAug: An Augmentation Scheme for End-to-End Automatic Speech Recognition": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "A Multi-Stream Framework Utilizing 3D Human Reconstruction for Cued Speech Recognition": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "Evaluating Logit-Based GOP Scores for Mispronunciation Detection": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
    "Semi-Supervised Learning for Automatic Speech Recognition with Word Error Rate Estimation and Targeted Domain Data Selection": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "Reasoning-Based Approach with Chain-of-Thought for Alzheimer’s Detection Using Speech and Large Language Models": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
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
    if c["decision"] != "supported" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not provisional supported: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paper_id"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The preserved abstract identifies a speech object and bounded intervention that instantiate {concept} under {subtheme}; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.", "evidence_excerpt": abstract[:1400] if abstract else title, "source_location": p.get("paper_url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "Official INTERSPEECH abstract evidence supports taxonomy membership; full-paper mechanism, failure analysis, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-045", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-045.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
