#!/usr/bin/env python3
"""Adjudicate a twelfth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Voice Reconstruction through Large-Scale TTS Models: Comparing Zero-Shot and Fine-tuning Approaches to Personalise TTS in Assistive Communication": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "Enhancing Acoustic-to-Articulatory Speech Inversion by Incorporating Nasality": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "CBA-Whisper: Curriculum Learning-Based AdaLoRA Fine-Tuning on Whisper for Low-Resource Dysarthric Speech Recognition": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Enhanced Hybrid Transducer and Attention Encoder Decoder with Text Data": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Articulatory Vowel Distinctiveness in Spanish": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "SLASH: Self-Supervised Speech Pitch Estimation Leveraging DSP-derived Absolute Pitch": ("sound-and-production", "source-filter-production", "periodic-source"),
    "Articulatory clarity and variability before and after surgery for tongue cancer": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Exploiting Context-dependent Duration Features for Voice Anonymization Attack Systems": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "ArVoice: A Multi-Speaker Dataset for Arabic Speech Synthesis": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Amplifying Artifacts with Speech Enhancement in Voice Anti-spoofing": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "R2S: Real-to-Synthetic Representation Learning for Training Speech Recognition Models on Synthetic Data": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Leveraging SSL Speech Features and Mamba for Enhanced DeepFake Detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Weight Factorization and Centralization for Continual Learning in Speech Recognition": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "Thai Speech Spoofing Detection Dataset with Variations in Speaking Styles": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Clinical Annotations for Automatic Stuttering Severity Assessment": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "How to Connect Speech Foundation Models and Large Language Models? What Matters and What Does Not": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-050", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-050.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
