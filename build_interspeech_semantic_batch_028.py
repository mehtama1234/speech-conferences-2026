#!/usr/bin/env python3
"""Adjudicate a thirteenth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "Tungnaá In Live Performance: An Implementation Of Interactive Artistic Text-To-Voice": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "Advancing Emotion Recognition via Ensemble Learning: Integrating Speech, Context, and Text Representations": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "75-Speaker Annot-16: A benchmark dataset for speech articulatory rt-MRI annotation with articulator contours and phonetic alignment": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Examining Test-Time Adaptation for Personalized Child Speech Recognition": ("people-variation-and-health", "speaker-characteristics", "age-and-development"),
    "J-SPAW: Japanese speaker verification and spoofing attacks recorded in-the-wild dataset": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "Probing Prosodic Differences Between Two Regional Varieties of Brazilian Portuguese": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "Self-supervised Optimality-Guided Learning of Speech Articulation": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Count Your Speakers! Multitask Learning for Multimodal Speaker Diarization": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "EmoJudge: LLM Based Post-Hoc Refinement for Multimodal Speech Emotion Recognition": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "H-QuEST: Accelerating Query-by-Example Spoken Term Detection with Hierarchical Indexing": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "GoP2Vec: A few shot learning for pronunciation assessment with goodness of pronunciation (GoP) based representations from an i-vector framework and augmentation": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
    "Context-Driven Dynamic Pruning for Large Speech Foundation Models": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "Leveraging Self-Supervised Learning Based Speaker Diarization for MISP 2025 AVSD Challenge": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "J-j-j-just Stutter: Benchmarking Whisper's Performance Disparities on Different Stuttering Patterns": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "TADA: Training-free Attribution and Out-of-Domain Detection of Audio Deepfakes": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "DiffEmotionVC: A Dual-Granularity Disentangled Diffusion Framework for Any-to-Any Emotional Voice Conversion": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-028", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-028.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
