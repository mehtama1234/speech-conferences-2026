#!/usr/bin/env python3
"""Adjudicate a first provisional INTERSPEECH D2 speech slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "FaiST: A Benchmark Dataset for Fairness in Speech Technology": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Beyond Hard Sharing: Efficient Multi-Task Speech-to-Text Modeling with Supervised Mixture of Experts": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "VoiceNet: Multilingual On-Device Phoneme-To-Audio Alignment": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "SNR-Aligned Consistent Diffusion for Adaptive Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "The Text-to-speech in the Wild (TITW) Database": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "MOVER: Combining Multiple Meeting Recognition Systems": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "LinearVC: Linear Transformations of Self-Supervised Features Through the Lens of Voice Conversion": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "RELATE: Subjective evaluation dataset for automatic evaluation of relevance between text and audio": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "Exploring the Effect of Segmentation and Vocabulary Size on Speech Tokenization for Speech Language Models": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Frozen Large Language Models Can Perceive Paralinguistic Aspects of Speech": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "BitTTS: Highly Compact Text-to-Speech Using 1.58-bit Quantization and Weight Indexing": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "Improving User Impression of Spoken Dialogue Systems by Controlling Para-linguistic Expression Based on Intimacy": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "A Siamese Network-Based Framework for Voice Mimicry Proficiency Assessment Using X-Vector Embeddings": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Factorized RVQ-GAN For Disentangled Speech Tokenization": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "Quadruple Path Modeling with Latent Feature Transfer for Permutation-free Continuous Speech Separation": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-039", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-039.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
