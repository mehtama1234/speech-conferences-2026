#!/usr/bin/env python3
"""Adjudicate a seventh clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Chain-of-Thought Distillation with Fine-Grained Acoustic Cues for Speech Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "DuRep: Dual-Mode Speech Representation Learning via ASR-Aware Distillation": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Understanding Dementia Speech Alignment with Diffusion-Based Image Generation": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Beat gestures made by human-like avatars affect speech perception": ("meaning-and-interaction", "grounding-and-action", "interactional-feedback"),
    "Data-driven approaches to pitch modelling in two Mexican Spanish ethnolects: K-means Clustering & GAMMs": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Towards Adaptable and Intelligible Speech Synthesis in Noisy Environments": ("voice-generation-and-control", "text-to-speech-and-content", "intelligibility-naturalness"),
    "Network of acoustic characteristics for the automatic detection of suicide risk from speech. Contribution to the 2025 SpeechWellness challenge by the Semawave team": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Automatic detection of speech sound disorders in German-speaking children: augmenting the data with typically developed speech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Identification of Pathological Pronunciation Profiles in ASR Transcription Errors": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Accessible Delivery of Visual-Acoustic Biofeedback for Speech Sound Disorder": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "Optimizing ASR for Catalan-Spanish Code-Switching: A Comparative Analysis of Methodologies": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching"),
    "Multimodal Silent Recognition of Phonemes Using Radar and Optopalatographic Silent Speech Interfaces": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Effective Context in Neural Speech Models": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "First Steps Towards Voice Anonymization for Code-Switching Speech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "When The MOS Predictor Asks For Training Annotation In Cross Lingual/Domain Adaptation": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "A Naturally Elicited Multimodal Stress Database and Speech Breathing Based Stress Detection": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-022", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-022.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
