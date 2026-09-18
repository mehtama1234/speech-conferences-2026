#!/usr/bin/env python3
"""Adjudicate an eighth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Hybrid HMM-SVM classifier using frication-based features for detection of non-normative sibilant articulation patterns in Polish children’s speech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Cross-lingual Data Selection Using Clip-level Acoustic Similarity for Enhancing Low-resource Automatic Speech Recognition": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "Skip-Salsa: Skip Synchronous Fusion of ASR LLM Decoders": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "Is Synthetic Data Truly Effective for Training Speech Language Models?": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "ProBiEM: Acoustic and Lexical Correlates of Prosodic Prominence in English-Malayalam Bilingual Speech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Exploring the Limits of Conformer CTC-Encoder for Speech Emotion Recognition using Large Language Models": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Vector Quantized Cross-lingual Unsupervised Domain Adaptation  for Speech Emotion Recognition": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "LiSTEN: Learning Soft Token Embeddings for Neural Audio LLMs": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Speech-Based Automatic Chronic Kidney Disease Diagnosis via Transformer Fusion of Glottal and Spectrogram Features": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Speaker-agnostic Emotion Vector for Cross-speaker Emotion Intensity Control": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "Eigenvoice Synthesis based on Model Editing for Speaker Generation": ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice"),
    "Parameter-efficient Fine-tuning of Conformer-based Streaming Speech Recognition into Non-streaming Models": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Thinking Fast and Slow: Robust Speech Recognition via Deep Filter-Tuning": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "Cocktail-Party Audio-Visual Speech Recognition": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Prolongation in Romanian": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation"),
    "Visual Cues Support Robust Turn-taking Prediction in Noise": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-023", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-023.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
