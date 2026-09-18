#!/usr/bin/env python3
"""Adjudicate a ninth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Voice Activity-based Text Segmentation for ASR Text Denormalization": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "GST-BERT-TTS: Prosody Prediction Without Accentual Labels For Multi-Speaker TTS Using BERT With Global Style Tokens": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "Multilingual Speech Assessment Using Cross-Attention and Multitask Learning": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "Grapheme-Coherent Phonemic and Prosodic Annotation of Speech by Implicit and Explicit Grapheme Conditioning": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Simultaneous Speech Translation Integrated Compact Multiple Sound Spot Synthesis System On A Laptop Carried Out With A Backpack": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Discrete Tokens Exhibit Interlanguage Speech Intelligibility Benefit: an Analytical Study Towards Accent-robust ASR Only with Native Speech Data": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "CMSP-ST: Cross-modal Mixup with Speech Purification for End-to-End Speech Translation": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "GTAnet: Geometry-Guided Temporal Attention for EEG-Based Sound Source Tracking in Cocktail Party Scenarios": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Online Audio-Visual Autoregressive Speaker Extraction": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "A Chinese Heart Failure Status Speech Database with Universal and Personalised Classification": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Plug-and-Play Co-Occurring Face Attention for Robust Audio-Visual Speaker Extraction": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Loquacious Set: 25,000 Hours of Transcribed and Diverse English Speech Recognition Data for Research and Commercial Use": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Towards Temporally Explainable Dysarthric Speech Clarity Assessment": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Fine-tuning Strategies for Automatic Speech Recognition of Low-Resource Speech with Autism Spectrum Disorder": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Effects of Prosodic Information on Dialect Classification Using Whisper Features": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "Exploiting Bispectral Features for Single-Channel Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-024", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-024.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
