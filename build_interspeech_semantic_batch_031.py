#!/usr/bin/env python3
"""Adjudicate a sixteenth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "SPEAKtoCOPD: a flashmob study to collect COPD speech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Robust Unsupervised Adaptation of a Speech Recogniser Using Entropy Minimisation and Speaker Codes": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "Phonetically-Augmented Discriminative Rescoring for Voice Search Error Correction": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "Legally validated evaluation framework for voice anonymization": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "Swedish Whispers; Leveraging a Massive Speech Corpus for Swedish Speech Recognition": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "The Role of Voiced Consonant Duration in Sung Vowel-Consonant and Consonant-Vowel Recognition": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Real-time TSE demonstration via SoundBeam with KD": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Decoding Alzheimer’s: Interpretable Visual and Logical Attention in Picture Description Tasks": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "On Apical Vowels in Eastern Zhenjiang Mandarin": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Contextual Paralinguistic Data Creation for Multi-Modal Speech-LLM: Data Condensation and Spoken QA Generation": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "ASDA: Audio Spectrogram Differential Attention Mechanism for Self-Supervised Representation Learning": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "A Self-Training Approach for Whisper to Enhance Long Dysarthric Speech Recognition": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Self-Improvement for Audio Large Language Model using Unlabeled Speech": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "The mutual exclusivity bias of bilingual visually grounded speech models": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "Foundation Model Hidden Representations for Heart Rate Estimation from Auscultation": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Brain-tuned Speech Models Better Reflect Speech Processing Stages in the Brain": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-031", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-031.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
