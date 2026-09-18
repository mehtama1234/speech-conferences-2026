#!/usr/bin/env python3
"""Adjudicate clear speech-specific INTERSPEECH ambiguous cases."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Towards Sentence Level Imagined Speech Generation from EEG signals": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Accurate, fast, cheap: Choose three. Replacing Multi-Head-Attention with Bidirectional Recurrent Attention for Long-Form ASR": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "Whilter: A Whisper-based Data Filter for \"In-the-Wild\" Speech Corpora Using Utterance-level Multi-Task Classification": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Effect of physical exercise on voice in people living with COPD": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Advancing Pediatric ASR: The Role of Voice Generation in Disordered Speech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Dhvani: A Weakly-supervised Phonemic Error Detection and Personalized Feedback System for Hindi": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Unified Microphone Conversion: Many-to-Many Device Mapping via Feature-wise Linear Modulation": ("sound-and-production", "room-channel-and-sensing", "microphone-channel"),
    "A Cookbook for Community-driven Data Collection of Impaired Speech in Low-Resource Languages": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Adversarial Attacks on Text-dependent Speaker Verification System": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Approaching Dialogue State Tracking via Aligning Speech Encoders and LLMs": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "FaVC: A Validated, Transcribed, Parallel Farsi Speech Dataset for Voice Conversion": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "Automatic Speech Recognition Biases in Newcastle English: an Error Analysis": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "Spoken Question Answering for Visual Queries": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "A real-time MRI study on asymmetry in velum dynamics during VCV production with nasal sounds": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "ARiSE: Auto-Regressive Multi-Channel Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Speaker-Aware Multi-Task Learning for Speech Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-016", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-016.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
