#!/usr/bin/env python3
"""Adjudicate a second provisional INTERSPEECH D2 speech slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Recreating Neural Activity During Speech Production with Language and Speech Model Embeddings": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Cross-Modal Watermarking for Authentic Audio Recovery and Tamper Localization in Synthesized Audiovisual Forgeries": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "Enhancing Audio Deepfake Detection by Improving Representation Similarity of Bonafide Speech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Naturalness-Aware Curriculum Learning with Dynamic Temperature for Speech Deepfake Detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "DLF-EEND: Dynamic Layer Fusion for End-to-End Speaker Diarization": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "ParaNoise-SV: Integrated Approach for Noise-Robust Speaker Verification with Parallel Joint Learning of Speech Enhancement and Noise Extraction": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Learning Phonetic Context-Dependent Viseme for Enhancing Speech-Driven 3D Facial Animation": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "FairASR: Fair Audio Contrastive Learning for Automatic Speech Recognition": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "Data Augmentation using Speech Synthesis for Speaker-Independent Dysarthria Severity Classification": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Improving Generalization of End-to-End ASR through Diversity and Independence Regularization": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "JIS: A Speech Corpus of Japanese Idol Speakers with Various Speaking Styles": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "GLCLAP: A Novel Contrastive Learning Pre-trained Model for Contextual Biasing in ASR": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "Synthetic Speech Source Tracing using Metric Learning": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Extending the Fongbe to French Speech Translation Corpus:  resources, models and benchmark": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Children's Voice Privacy: First Steps and Emerging Challenges": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "ArticulateX: End-to-End Monolingual Speech Translation in Articulator Space": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-040", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-040.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
