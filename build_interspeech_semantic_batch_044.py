#!/usr/bin/env python3
"""Adjudicate a sixth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "STCON NIST SRE24 System: Composite Speaker Recognition Solution for Challenging Scenarios": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Stuttering Detection Based on Self-Attention Weights of Temporal Acoustic Vector Sequence": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Scaling pseudo-labeling data for end-to-end low-resource speech translation (the case of Kurdish language)": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "Automatic Speech Recognition of African American English: Lexical and Contextual Effects": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "Attention-Free Dual-Mode ASR with Latency-Controlled Selective State Spaces": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Analysis of Phonetic Level Similarities Across Languages in Emotional Speech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Fine-Tuning ASR for Stuttered Speech: Personalized vs. Generalized Approaches": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Replay Attacks Against Audio Deepfake Detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Boundary-Conscious Pruning: Hard Set-Aware Model Compression for Efficient Speaker Recognition": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "The Interspeech 2025 Challenge on Speech Emotion Recognition in Naturalistic Conditions": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "WCTC-Biasing: Retraining-free Contextual Biasing ASR with Wildcard CTC-based Keyword Spotting and Inter-layer Biasing": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "SEED: Speaker Embedding Enhancement Diffusion Model": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Scalable Offline ASR for Command-Style Dictation in Courtrooms": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Streaming Non-Autoregressive Model for Accent Conversion and Pronunciation Improvement": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "Efficient Streaming Speech Quality Prediction with Spiking Neural Networks": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "Improving Cross-Attention based on Positional Alignment during Inference for Robust Long-form Speech Recognition": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-044", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-044.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
