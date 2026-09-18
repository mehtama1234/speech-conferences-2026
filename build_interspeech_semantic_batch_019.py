#!/usr/bin/env python3
"""Adjudicate a fourth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Language-Guided Contrastive Audio-Visual Masked Autoencoder with Automatically Generated Audio-Visual-Text Triplets from Videos": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "A Joint Network for Singing Melody Extraction from Polyphonic Music with Attention Aggregation and Self-Consistency Training": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "Adversarial Deep Metric Learning for Cross-Modal Audio-Text Alignment in Open-Vocabulary Keyword Spotting": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech": ("meaning-and-interaction", "dialogue-and-turn-taking", "interactional-feedback"),
    "Who knows best? Effects of speech disfluencies on incentivized decision-making": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation"),
    "Leveraging Unlabeled Audio for Audio-Text Contrastive Learning via Audio-Composed Text Features": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Can Multimodal Foundation Models Help Analyze Child-Inclusive Autism Diagnostic Videos?": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Leveraging Text and Speech Processing for Suicide Risk Classification in Chinese Adolescents": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "DRI-GAN: A Novel Dual Real Input GAN with Triplet Loss for Cross-Lingual and Noisy SLU": ("meaning-and-interaction", "prosody-and-intent", "intent-in-context"),
    "Unified Variational and Physics-aware Model for Room Impulse Response Estimation": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "Novel Parasitic Dual-Scale Modeling for Efficient and Accurate Multilingual Speech Translation": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "CAMER: Contribution-Aware Multimodal Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Synthetic Data Generation for Phrase Break Prediction with Large Language Model": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Leveraging Information Retrieval to Enhance Spoken Language Understanding Prompts in Few-Shot Learning": ("meaning-and-interaction", "prosody-and-intent", "intent-in-context"),
    "Explainable Speech Emotion Recognition Through Attentive Pooling: Insights from Attention-Based Temporal Localization": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-019", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-019.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
