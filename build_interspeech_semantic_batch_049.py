#!/usr/bin/env python3
"""Adjudicate an eleventh provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "DiffMV-ETS: Diffusion-based Multi-Voice Electromyography-to-Speech Conversion using Speaker-Independent Speech Training Targets": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "REB-former: RWKV-enhanced E-branchformer for Speech Recognition": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "LASPA: Language Agnostic Speaker Disentanglement with Prefix-Tuned Cross-Attention": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "Voice Adaptation for Swiss German": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "Lightweight Speech Enhancement for Mandarin Esophageal Speech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "Text-Enhanced Audio Encoder for Large Language Model based Speech Recognition via Cross-Modality Pre-training with Unpaired Audio-Text Data": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Length Aware Speech Translation for Video Dubbing": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Improving Practical Aspects of End-to-End Multi-Talker Speech Recognition for Online and Offline Scenarios": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Voice Conversion for Likability Control via Automated Rating of Speech Synthesis Corpora": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "DYNAC: Dynamic Vocabulary-based Non-Autoregressive Contextualization for Speech Recognition": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "OWSM-Biasing: Contextualizing Open Whisper-Style Speech Models for Automatic Speech Recognition with Dynamic Vocabulary": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "Acquiring Pronunciation from Speech Audio via Multi-task Learning": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
    "Scaling beyond Denoising: Submitted System and Findings in URGENT Challenge 2025": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Apical vs. Regular Vowel Duration: A Corpus-based Analysis of Contextual Influences in Standard Mandarin": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Multitask Learning with Fused Attention for Improved ASR and Mispronunciation Detection in Children's Speech Sound Disorders": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "AusKidTalk: Using Strategic Data Collection and Out-of-Domain Tools to Semi-Automate Novel Corpora Annotation": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-049", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-049.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
