#!/usr/bin/env python3
"""Adjudicate a thirteenth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Lateral Channel Formation in Australian English /l/: Insights from Magnetic Resonance Imaging": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Improving Automatic Speech Recognition for Children's Reading Assessment with Disfluency-aware Language Models": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation"),
    "Regularizing Learnable Feature Extraction for Automatic Speech Recognition": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "Analysis and Extension of a Near-End Listening Enhancement Method Based on Long-Term Fractile Noise Statistics": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "Spoken Language Modeling with Duration-Penalized Self-Supervised Units": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Multimodal Prosody Modeling: A Use Case for Multilingual Sentence Mode Prediction": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Personalized Fine-Tuning with Controllable Synthetic Speech from LLM-Generated Transcripts for Dysarthric Speech Recognition": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Open Universal Arabic ASR Leaderboard": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "Calm-Whisper: Reduce Whisper Hallucination On Non-Speech By Calming Crazy Heads Down": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "end-to-end-recovery"),
    "CAGCRN: Real-Time Speech Enhancement with a Lightweight Model for Joint Acoustic Echo Cancellation and Noise Suppression": ("listening-and-separation", "echo-and-reconstruction", "acoustic-echo-cancellation"),
    "A Lightweight Hybrid Dual Channel Speech Enhancement System under Low-SNR Conditions": ("listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "FLASepformer: Efficient Speech Separation with Gated Focused Linear Attention Transformer": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "FlowSE: Efficient and High-Quality Speech Enhancement via Flow Matching": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "The role of audio-visual integration in the time course of phonetic encoding in self-supervised speech models": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "SQ-AST: A Transformer-Based Model for Speech Quality Prediction": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "What the Filler? Both ASR Systems and Humans Struggle More With Other Kinds of Disfluencies Than With Filler Particles": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-051", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-051.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
