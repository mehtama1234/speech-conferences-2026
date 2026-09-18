#!/usr/bin/env python3
"""Adjudicate a fourteenth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Variability in Intervocalic /t/ and Community Diversity in Australian English": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "Speech Reference Intervals: An Assessment of Feasibility in Depression Symptom Severity Prediction": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "ClaritySpeech: Dementia Obfuscation in Speech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "Incorporating Linguistic Constraints from External Knowledge Source for Audio-Visual Target Speech Extraction": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "A Comparative Study on Proactive and Passive Detection  of Deepfake Speech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "A Semantic Information-based Hierarchical Speech Enhancement Method Using Factorized Codec and Diffusion Model": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "AdaKWS: Towards Robust Keyword Spotting with Test-Time Adaptation": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "Mitigating Overfitting During Speech Foundation Model Fine-tuning: Applications to Dysarthric Speech Detection": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Large Language Models based ASR Error Correction for Child Conversations": ("people-variation-and-health", "speaker-characteristics", "age-and-development"),
    "Non-Intrusive Binaural Speech Intelligibility Prediction Using Mamba for Hearing-Impaired Listeners": ("evaluation-deployment-and-consequence", "metrics-and-targets", "word-error-versus-understanding"),
    "LLM-based Generative Error Correction for Rare Words with Synthetic Data and Phonetic Context": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "Visually-Adaptive Guided Robust Speech Recognition with Parameter-Efficient Adaptation": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Generalizable Audio Deepfake Detection via Hierarchical Structure Learning and Feature Whitening in Poincaré sphere": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "HK-GenSpeech: A Generative AI Scene Creation Framework for Speech Based Cognitive Assessment": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Online AV-CrossNet: a Causal and Efficient Audiovisual System for Speech Enhancement and Target Speaker Extraction": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Mimic Blocker: Self-Supervised Adversarial Training for Voice Conversion Defense with Pretrained Feature Extractors": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-052", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-052.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
