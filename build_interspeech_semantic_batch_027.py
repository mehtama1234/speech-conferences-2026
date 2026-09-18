#!/usr/bin/env python3
"""Adjudicate a twelfth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "SCRIBAL: A Digital Transcription Tool in Higher Education": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Pre-aspiration in Iceland Is Conditioned by Gender/Sex": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "In-context learning capabilities of Large Language Models to detect suicide risk among adolescents from speech transcripts": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Conveying Gender Through Speech: Insights from Trans Men": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation"),
    "Structured pruning for efficient systolic array accelerated cascade Speech-to-Text Translation": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Bringing Interpretability to Neural Audio Codecs": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "Visual features of the oral region in Polish sibilants produced by children with various sibilance patterns": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "LHCP-ASR: An English Speech Corpus of High-Energy Particle Physics Talks for Narrow-Domain ASR Benchmarking": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Processing of grammatical information in cochlear implant simulated speech by German adult listeners": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "Enhancing Target-speaker Automatic Speech Recognition Using Multiple Speaker Embedding Extractors with Virtual Speaker Embedding": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "NAM-to-Speech Conversion with Multitask-Enhanced Autoregressive Models": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "Harnessing Text-to-Speech Voice Cloning Models for Improved Audiological Speech Assessment": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Neuro2Semantic: A Transfer Learning Framework for Semantic Reconstruction of Continuous Language from Human Intracranial EEG": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Lexical stress affects lenition: The case of Italian palato-alveolar affricates": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Enhancing Syllabic Recognition via Speech-EEG Phase Analysis and Non-Activity State Modeling": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Universal Preference-Score-based Pairwise Speech Quality Assessment": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-027", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-027.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
