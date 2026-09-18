#!/usr/bin/env python3
"""Adjudicate another clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Enhancing Lyrics Transcription on Music Mixtures with Consistency Loss": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Investigating the Impact of Word Informativeness on Speech Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Mamba-based Hybrid Model for Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Synthetic Dysarthric Speech: A Supplement, Not a Substitute for Authentic Data in Dysarthric Speech Recognition": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Robust Personal Voice Activity Detection for Mitigating Domain Mismatch and False Acceptance Scenarios": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "speaker-adaptation"),
    "SupraDoRAL: Automatic Word Prominence Detection Using Suprasegmental Dependencies of Representations with Acoustic and Linguistic Context": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Clustering-based Hard Negative Sampling for Supervised Contrastive Speaker Verification": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "FlowTSE: Target Speaker Extraction with Flow Matching": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Source Verification for Speech Deepfakes": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Dialogue Response Prefetching Based on Semantic Similarity and Prediction Confidence of Language Model": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "LIST: Language-Independent Speech Token for Multilingual Speech Synthesis with Language Models": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "SpeechSEC: A Unified Multi-Task Framework for Speech Synthesis, Editing, and Continuation": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "Web-Based Application for Real-Time Biofeedback of Vocal Resonance in Gender-Affirming Voice Training: Design and Usability Evaluation": ("people-variation-and-health", "human-centered-evaluation", "user-control-and-consent"),
    "Switch Conformer with Universal Phonetic Experts for Multilingual ASR": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Scaling Laws for Synthetic Speech for Model Training": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "A Neural Codec Approach for Noise-Robust Bandwidth Expansion": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-017", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-017.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
