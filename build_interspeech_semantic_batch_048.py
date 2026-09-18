#!/usr/bin/env python3
"""Adjudicate a tenth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "MTSE: Multi-Target Speaker Extraction for Conversation Scenarios": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Assessment of the synthetic quality and controllability of laughing onset in speech-laugh synthesis": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "Alzheimer’s Disease Detection Using Co-Attention Mechanism for Acoustic and ASR-Transcribed Text Features": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Weakly Supervised Data Refinement and Flexible Sequence Compression for Efficient Thai LLM-based ASR": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "Boosting StoRM Convergence with Metric Guidance and Non-uniform State-Sampling for Optimal Dereverberation": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "Towards Secure User Authentication for Headphones via In-Ear or In-Earcup Microphones": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Scalable Spontaneous Speech Dataset (SSSD): Crowdsourcing Data Collection to Promote Dialogue Research": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "CLEP-DG: Contrastive Learning for Speech Emotion Domain Generalization via Soft Prompt Tuning": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "Who, When, and What: Leveraging the ``Three Ws'' Concept for Emotion Recognition in Conversation": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Generating Consistent Prosodic Patterns from Open-Source TTS Systems": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "Queer Waves: A German Speech Dataset Capturing Gender and Sexual Diversity from Podcasts and YouTube": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Language-Agnostic Speech Tokenizer for Spoken Term Detection with Efficient Retrieval": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Beyond Traditional Speech Modifications : Utilizing Self Supervised Features for Enhanced Zero-Shot Children ASR": ("people-variation-and-health", "speaker-characteristics", "age-and-development"),
    "Prompting Whisper for Improved Verbatim Transcription and End-to-end Miscue Detection": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation"),
    "Performance of Montreal Forced Aligner on Cantonese Spontaneous Speech": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "A Dataset for Automatic Assessment of TTS Quality in Spanish": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-048", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-048.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
