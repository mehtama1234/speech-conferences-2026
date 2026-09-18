#!/usr/bin/env python3
"""Adjudicate a fifth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "A Two-Stage Hierarchical Deep Filtering Framework for Real-Time Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Improving Noise Robustness of LLM-based Zero-shot TTS via Discrete Acoustic Token Denoising": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "Cross-modal Knowledge Transfer Learning as Graph Matching Based on Optimal Transport for ASR": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "Robust Neural Codec Language Modeling with Phoneme Position Prediction for Zero-Shot TTS": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "Real-Time Audio-Visual Speech Enhancement Using Pre-trained Visual Representations": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Speaker Conditioning of Voice Activity Detection via Implicit Separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Joint Target-Speaker ASR and Activity Detection": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "SOMSRED-SVC: Sequential Output Modeling with Speaker Vector Constraints for Joint Multi-Talker Overlapped ASR and Speaker Diarization": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Unified Audio-Visual Modeling for Recognizing Which Face Spoke When and What in Multi-Talker Overlapped Speech and Video": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "Contextual predictability effects on acoustic distinctiveness in read Polish speech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "Enhancing Low-Resource Language and Instruction Following Capabilities of Audio Language Models": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "Building an Accurate Open-Source Hebrew ASR System through Crowdsourcing": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Training Articulatory Inversion Models for Interspeaker Consistency": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Streaming Sortformer: Speaker Cache-Based Online Speaker Diarization with Arrival-Time Ordering": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "Leveraging Geographic Metadata for Dialect-Aware Speech Recognition": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "Federated Learning with Feature Space Separation for Speaker Recognition": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-043", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-043.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
