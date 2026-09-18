#!/usr/bin/env python3
"""Adjudicate a fifteenth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Fully Few-shot Class-incremental Audio Classification Using Multi-level Embedding Extractor and Ridge Regression Classifier": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "Enhancing Serialized Output Training for Multi-Talker ASR with Soft Monotonic Alignment and Utterance-level Timestamp": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Automatic classification of stop realisation with wav2vec2.0": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Improving Audio Classification by Transitioning from Zero- to Few-Shot": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "I want a horror – comedy – movie: Slips-of-the-Tongue Impact Conversational Recommender System Performance": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation"),
    "OpusLM: A Family of Open Unified Speech Language Models": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "A simple method for predicting Clinical Scores in Huntington’s Disease by leveraging ASR's uncertainty on spontaneous speech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Improving Respiratory Sound Classification with Architecture-Agnostic Knowledge Distillation from Ensembles": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Attention Is Not Always the Answer: Optimizing Voice Activity Detection with Simple Feature Fusion": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Probing the Robustness Properties of Neural Speech Codecs": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "Does English fish sound like French fiche? Perceptual similarity judgments versus acoustic similarity": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "Lessons Learnt: Revisit Key Training Strategies for Effective Speech Emotion Recognition in the Wild": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Improving Speech Emotion Recognition Through Cross Modal Attention Alignment and Balanced Stacking Model": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "From Pretraining to Performance: Benchmarking Self-Supervised Speech Models for Interspeech-25 SER Challenge": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Self-supervised learning of speech representations with Dutch archival data": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Investigating the Reasonable Effectiveness of Speaker Pre-Trained Models and their Synergistic Power for SingMOS Prediction": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-030", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-030.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
