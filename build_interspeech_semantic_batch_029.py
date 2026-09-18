#!/usr/bin/env python3
"""Adjudicate a fourteenth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Cantonese Punctuation Restoration using LLM Annotated Data": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "PPGs-BERT: Leveraging Phoneme Sequence and BERT for Alzheimer’s Disease Detection from Spontaneous Speech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "RA-CLAP: Relation-Augmented Emotional Speaking Style Contrastive Language-Audio Pretraining For Speech Retrieval": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Corpus-Based Insights into Mandarin Neutral Tone: Effects of Tonal Context and Structural Patterns in Spontaneous Speech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Score-Based Training for Energy-Based TTS Models": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "Efficient Speech Enhancement via Embeddings from Pre-trained Generative Audioencoders": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Towards Robust Overlapping Speech Detection: A Speaker-Aware Progressive Approach Using WavLM": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "FT-Boosted SV: Towards Noise Robust Speaker Verification for English Speaking Classroom Environments": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "PeriodCodec: A Pitch-Controllable Neural Audio Codec Using Periodic Signals for Singing Voice Synthesis": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "Fine-tuning Parakeet-TDT for Dysarthric Speech Recognition in the Speech Accessibility Project Challenge": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Development and Validation of a Wav2Vec 2.0-Based Cross-Language Methodology for Measurement of Articulatory Precision": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Anne Rowling Neurological Speech Corpus: clinically annotated longitudinal dataset for developing speech biomarkers in neurodegenerative disorders": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Multimodal Emotion Diarization: Frame-Wise Integration of Text and Audio Representations": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Exploratory Analysis of Brainstem fMRI Data During Sustained Phonation": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Pull It Together: Reducing the Modality Gap in Contrastive Learning": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Modeling Probabilistic Reduction using Information Theory and Naive Discriminative Learning": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-029", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-029.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
