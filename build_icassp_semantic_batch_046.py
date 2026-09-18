#!/usr/bin/env python3
"""Assign clear speech cases from the remaining ICASSP queue."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "Audience-Aware Co-speech Gesture Generation in Public Speaking via Anticipation Tokens": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "Graph-Biased EEG Transformers for Silent Speech Decoding": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Obstructive Sleep Apnea Endotype Prediction During Wakefulness Using Voice Biomarkers": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Keeping Models Listening: Segment- and time-aware attention rescaling at decoding time": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "Semantic Anchor Transfer from Short to Long Speech in a Distillation-Based Summarization Framework": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "Learning to Align with Unbalanced Optimal Transport in Linguistic Knowledge Transfer for ASR": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Spike-Driven Low-Power Speech Bandwidth Extension": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "HASap: Hierarchical Acoustic-Semantic Annotation Pipeline for Scripted Speech Data": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Why Do Speech Language Models Fail to Generate Semantically Coherent Outputs? A Modality Evolving Perspective": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "LLM-Based Post-ASR Error Correction for Disordered Speech": ("people-and-variation", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Do Speech LLMs Learn Crossmodal Embedding Spaces?": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "IBPCodec : A Low-Bitrate Lightweight Speech Codec With Inter-Band Prediction": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "JUND-F0: A Novel Deep Learning Framework for Joint Unvoiced/Voiced Detection And F0 Estimation": ("sound-and-production", "source-filter-production", "periodic-source"),
    "A Bimodal Approach for Detecting Fatigue Using Speech and Personal Assessments in College Students": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Slot Filling as a Reasoning Task for Speechllms": ("meaning-and-interaction", "grounding-and-action", "speech-act"),
    "Bringing Multimodal Foundation Models to Hearing Aids": ("people-and-variation", "human-centered-evaluation", "accessibility-fit"),
}

queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
by_title = {row["title"]: row for row in queue["rows"]}
already = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    if path.name != "icassp-2026-semantic-reviewed-batch-046.json":
        already |= {row["paper_id"] for row in json.loads(path.read_text()).get("rows", [])}

missing = [title for title in ASSIGNMENTS if title not in by_title or by_title[title]["paper_id"] in already]
if missing:
    raise SystemExit(f"missing or already reviewed: {missing}")

rows = []
for title, (theme, subtheme, concept) in ASSIGNMENTS.items():
    candidate = by_title[title]
    if candidate["decision"] != "insufficient-evidence" or candidate["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not an unresolved insufficient-evidence case: {title}")
    paper = papers[candidate["paper_id"]]
    abstract = paper.get("abstract") or ""
    rows.append({
        "paper_id": paper["paperId"],
        "title": title,
        "decision": "supported",
        "confidence": "analyst-reviewed-D1",
        "theme_id": theme,
        "subtheme_id": subtheme,
        "concept_id": concept,
        "semantic_reasoning": f"The title explicitly identifies a speech task or speech signal and supports a bounded assignment to {concept} under {subtheme}; no claim about mechanism or performance is made beyond title evidence.",
        "evidence_excerpt": title,
        "source_location": paper.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": "D1",
        "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance, mechanism, or prevalence claim.",
    })

payload = {
    "schema_version": 1,
    "batch_id": "icassp-2026-semantic-batch-046",
    "status": "analyst-reviewed-explicit-speech-assignment-batch",
    "claim_boundary": "These records are explicit speech-taxonomy assignments supported by title evidence only; D1 does not imply abstract or full-paper verification.",
    "reviewed_count": len(rows),
    "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-046.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": len(rows)}))
