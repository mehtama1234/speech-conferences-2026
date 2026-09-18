#!/usr/bin/env python3
"""Adjudicate a sixth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Sentence-Final Particles in Mandarin Child-Directed Speech: Frequency and Impact on Speech Rate": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Identifying Primary Stress Across Related Languages and Dialects with Transformer-based Speech Encoder Models": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Articulatory Strategy in Vowel Production as a Basis for Speaker Discrimination": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Training-Free Voice Conversion with Factorized Optimal Transport": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "Zero-Shot Speech-Based Depression and Anxiety Assessment with LLMs": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "The Role of Syntactic Structures in Shaping Directionality in Trisyllabic Tone Sandhi: Evidence from Tianjin Mandarin": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "cultural-meaning"),
    "Talker Normalization in Chinese Bilinguals: A Comparative Study": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation"),
    "Towards a dynamical model of transitions between fluent and stuttered speech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "ToxicTone: A Mandarin Audio Dataset Annotated for Toxicity and Toxic Utterance Tonality": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "SuPseudo: A Pseudo-supervised Learning Method for Neural Speech Enhancement in Far-field Speech Recognition": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Temporal Modeling of Room Impulse Response Generation via Multi-Scale Autoregressive Learning": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "Fairness in Dysarthric Speech Synthesis: Understanding Intrinsic Bias in Dysarthric Speech Cloning using F5-TTS": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Assessment of L2 Oral Proficiency using Speech Large Language Models": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "Multi-lingual and Zero-Shot Speech Recognition by Incorporating Classification of Language-Independent Articulatory Features": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "AA-SLLM: An Acoustically Augmented Speech Large Language Model for Speech Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "A Study on The Impact of Foundation Models on Automatic Depression Detection from Speech Signals": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-021", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-021.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
