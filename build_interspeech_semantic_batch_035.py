#!/usr/bin/env python3
"""Adjudicate a twentieth clear, speech-specific INTERSPEECH ambiguity slice."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "SpeechMLC: Speech Multi-label Classification": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Bridging Audio and Vision: Zero-Shot Audiovisual Segmentation by Connecting Pretrained Models": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "Concurrent Speech and Auditory Tag Clouds for Non-Visual Web Interaction": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "MADUV: The 1st INTERSPEECH Mice Autism Detection via Ultrasound Vocalization Challenge": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Label-Context-Dependent Internal Language Model Estimation for CTC": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "On Retrieval of Long Audios with Complex Text Queries": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "Flexible VAD-PVAD Transition: A Detachable PVAD Module for Dynamic Encoder RNN VAD": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "How do both phonological and syntactic complexity influence speech planning?": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "Text Entry for All: Towards Speech-based Multimodal Interaction for Inclusion, Accessibility and the Preservation of the World’s Linguistic Heritage": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "Assessing the Performance and Efficiency of Mamba ASR in Low-Resource Scenarios": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "Feature Importance across Domains for Improving Non-Intrusive Speech Intelligibility Prediction in Hearing Aids": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit"),
    "Multi-task learning for speech emotion recognition in naturalistic conditions": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "Effect of Noise Floor in Room Impulse Response on Speech Perception Under Spherical Harmonics-based Spatial Sound Reproduction": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "PartialEdit: Identifying Partial Deepfakes in the Era of Neural Speech Editing": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "GraphemeAug: A Systematic Approach to Synthesized Hard Negative Keyword Spotting Examples": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "Unlocking Temporal Flexibility: Neural Speech Codec with Variable Frame Rate": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-035", "status": "analyst-reviewed-explicit-speech-assignment-batch", "claim_boundary": "These records resolve clear speech-specific ambiguous cases using title and abstract evidence; they do not establish full-paper mechanism or performance.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-035.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
