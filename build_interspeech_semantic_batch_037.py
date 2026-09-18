#!/usr/bin/env python3
"""Adjudicate the remaining clear speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Regularized Federated Learning for Privacy-Preserving Dysarthric and Elderly Speech Recognition": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Evaluating the Usefulness of Non-Diagnostic Speech Data for Developing Parkinson's Disease Classifiers": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "A Simple-Yet-Effective Data Augmentation Method for Speaker Identification in Novels": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Simple and Effective Content Encoder for Singing Voice Conversion via SSL-Embedding Dimension Reduction": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "No Audiogram: Leveraging Existing Scores for Personalized Speech Intelligibility Prediction": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "Cross-corpus open-set Speech Emotion Recognition Method Based on Spatiotemporal Features with Inverse-Entropy Regularization": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "A Robust Hybrid ACC-PM Approach for Personal Sound Zones": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "SSF-DST: A Spectro-Spatial Features Enhanced Deep Spatiotemporal Network for EEG-Based Auditory Attention Detection": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Towards Efficiently Whisper Fine-tuning with Monotonic Alignments": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "The Sub-3Sec Problem: From Text-Independent to Text-Dependent Corpus": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-037", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-037.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
