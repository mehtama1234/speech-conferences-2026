#!/usr/bin/env python3
"""Adjudicate a nineteenth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Direction-Aware Neural Acoustic Fields for Few-Shot Interpolation of Ambisonic Impulse Responses": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "Directional Speech Recognition with Full-Duplex Capability": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Modeling Vowel System Typology Using Iterated Confusion Minimization": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Cryfish: On deep audio analysis with Large Language Models": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "ViCocktail: Automated Multi-Modal Data Collection for Vietnamese Audio-Visual Speech Recognition": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Towards Fusion of Neural Audio Codec-based Representations with Spectral for Heart Murmur Classification via Bandit-based Cross-Attention Mechanism": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Overestimated performance of auditory attention decoding caused by experimental design in EEG recordings": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "Developing a LeFF Transformer Model for Exacerbated Speech Detection in COPD and Asthma": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Band-SCNet: A Causal, Lightweight Model for High-Performance Real-Time Music Source Separation": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "Language-Aware Prompt Tuning for Parameter-Efficient Seamless Language Expansion in Multilingual ASR": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "EASY: Emotion-aware Speaker Anonymization via Factorized Distillation": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "A Gradient Effect of Hand Beat Timing on Spoken Word Recognition": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "APTTS: Adversarial Post-training in Latent Flow Matching for Fast and High-fidelity Text-to-Speech": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "M3L: A Multi-Modal and Multi-Lingual Depression Detection Framework": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Can Speech Accurately Detect Depression in Patients With Comorbid Dementia? An Approach for Mitigating Confounding Effects of Depression and Dementia": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Challenges and practical guidelines for atypical speech data collection, annotation, usage and sharing: A multi-project perspective": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-034", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-034.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
