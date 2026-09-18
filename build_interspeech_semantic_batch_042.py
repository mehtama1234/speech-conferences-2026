#!/usr/bin/env python3
"""Adjudicate a fourth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "TF-SkiMNet: Speech Enhancement Based on Inplace Modeling and Skipping Memory in Time-Frequency Domain": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "REAL-T: Real Conversational Mixtures for Target Speaker Extraction": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "From KAN to GR-KAN: Advancing Speech Enhancement with KAN-Based Methodology": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Efficient Multilingual ASR Finetuning via LoRA Language Experts": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "StarVC: A Unified Auto-Regressive Framework for Joint Text and Speech Generation in Voice Conversion": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "SpeechRefiner: Towards Perceptual Quality Refinement for Front-End Algorithms": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "SIDC-KWS: Efficient Spiking Inception-Dilated Conformer with Self-Attention for Keyword Spotting": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "Contextualized Automatic Speech Recognition with Dynamic Vocabulary Prediction and Activation": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "Accelerating Autoregressive Speech Synthesis Inference With Speech Speculative Decoding": ("voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency"),
    "Context is all you need? Low-resource conversational ASR profits from context, coming from the same or from the other speaker": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "Unlearning LLM-Based Speech Recognition Models": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "Towards Emotionally Consistent Text-Based Speech Editing: Introducing EmoCorrector and The ECD-TSE Dataset": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "Augment Mandarin to Cantonese Speech Databases via Retrieval-Augmented Generation and Speech Synthesis": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Beyond Manual Transcripts: The Potential of Automated Speech Recognition Errors in Improving Alzheimer’s Disease Detection": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Gradual modeling of the Lombard effect by modifying speaker embeddings from a Text-To-Speech model": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation"),
    "Face2VoiceSync: Lightweight Face-Voice Consistency for Text-Driven Talking Face Generation": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
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
    if c["decision"] != "supported" or c["review_state"] != "needs-analyst-semantic-review":
        raise SystemExit(f"not provisional supported: {title}")
    p = papers[c["paper_id"]]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paper_id"], "title": title, "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": f"The preserved abstract identifies a speech object and bounded intervention that instantiate {concept} under {subtheme}; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.", "evidence_excerpt": abstract[:1400] if abstract else title, "source_location": p.get("paper_url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "Official INTERSPEECH abstract evidence supports taxonomy membership; full-paper mechanism, failure analysis, and independent reproduction remain unestablished."})
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-042", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-042.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
