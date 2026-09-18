#!/usr/bin/env python3
"""Adjudicate a fifteenth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Towards Early Prediction of Self-Supervised Speech Model Performance": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use"),
    "SaD: A Scenario-Aware Discriminator for Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Auto-Landmark: Acoustic Landmark Dataset and Open-Source Toolkit for Landmark Extraction": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Lessons Learned from the URGENT 2024 Speech Enhancement Challenge": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "Mitigating Language Mismatch in SSL-Based Speaker Anonymization": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "Analysis and Evaluation of Synthetic Data Generation in Speech Dysfluency Detection": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Restoring Harmonics: Enhancing Speech Quality with Deep Mask and Harmonic Restoration Network": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Accelerating Flow-Matching-Based Text-to-Speech via Empirically Pruned Step Sampling": ("voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency"),
    "Pinyin-Guided Chinese Speech Recognition with Large Language Model": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
    "Evaluation of Three Automatic Alignment Tools for the Processing of Non-native French": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "Towards Accurate Phonetic Error Detection Through Phoneme Similarity Modeling": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
    "LLM-Synth4KWS: Scalable Automatic Generation and Synthesis of Confusable Data for Custom Keyword Spotting": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "LATE: Open Source Toolkit for Latvian and Latgalian Speech Transcription": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "The Speech Accessibility Project: Best Practices for Collection and Curation of Disordered Speech": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "SAKURA: On the Multi-hop Reasoning of Large Audio-Language Models Based on Speech and Audio Information": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-053", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-053.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
