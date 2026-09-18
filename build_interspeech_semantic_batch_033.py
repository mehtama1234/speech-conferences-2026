#!/usr/bin/env python3
"""Adjudicate an eighteenth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "TS3-Codec: Transformer-Based Simple Streaming Single Codec": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "MPE-TTS: Customized Emotion Zero-Shot Text-To-Speech Using Multi-Modal Prompt": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "A Watermark for Auto-Regressive Speech Generation Models": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "CrossPhon: An Auto Phone Mapping Tool to Streamline Cross-language Modeling for Phone Alignment of Low-resource Languages": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
    "Evaluating Automatic Speech Recognition Pipelines for Mandarin-English Bilingual Child Language Assessment in Telehealth": ("people-variation-and-health", "speaker-characteristics", "age-and-development"),
    "Speech Mutil-label Emotion Recognition Using Asymmetric Class Loss Function Based on Effective Samples": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Layer-Wise Decision Fusion for Fake Audio Detection Using XLS-R": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Alzheimer’s Dementia Detection Using Perplexity from Paired Large Language Models": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Thinking in Directivity: Speech Large Language Model for Multi-Talker Directional Speech Recognition": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Enhancing Generalization of Speech Large Language Models with Multi-Task Behavior Imitation and Speech-Text Interleaving": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "WAKE: Watermarking Audio with Key Enrichment": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "When focus shapes the flow: prosodic restructuring in Mandarin complex nominals": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Leveraging LLM and Self-Supervised Training Models for Speech Recognition in Chinese Dialects: A Comparative Analysis": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "The Effect of Word Predictability on Spoken Cross-Language Intelligibility": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "AxLSTMs: learning self-supervised audio representations with xLSTMs": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Towards Pre-training an Effective Respiratory Audio Foundation Model": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-033", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-033.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
