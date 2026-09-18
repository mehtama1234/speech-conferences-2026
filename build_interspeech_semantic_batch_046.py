#!/usr/bin/env python3
"""Adjudicate an eighth provisional INTERSPEECH D2 speech slice."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
    "MultiActor-Audiobook: Zero-Shot Audiobook Generation with Faces and Voices of  Multiple Speakers": ("voice-generation-and-control", "text-to-speech-and-content", "intelligibility-naturalness"),
    "Character Error Rate Estimation for Semi-Supervised Training of Speech Recognition for Arabic Dialects": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "MSFNet: A Nested Model for Multi-Sampling-Frequency Speech Enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "Towards Domain-Specific Spoken Language Understanding for a Catalan Voice-Controlled Video Game": ("meaning-and-interaction", "grounding-and-action", "intent-in-context"),
    "Automatic Detection and Sub-typing of Primary Progressive Aphasia from Speech: Integrating Task-Specific Features and Spatio-Semantic Graphs": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "Fifteen Years of Child-Centered Long-Form Recordings: Promises, Resources, and Remaining Challenges to Validity": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "Towards Machine Unlearning for Paralinguistic Speech Processing": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "Constrained LDDMM for Dynamic Vocal Tract Morphing: Integrating Volumetric and Real-Time MRI": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "Causal Structure Discovery for Error Diagnostics of Children's ASR": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "Multimodal Biomarkers for Schizophrenia: Towards Individual Symptom Severity Estimation": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "An approach to measuring the performance of Automatic Speech Recognition(ASR) models in the context of Large Language Model(LLM) powered applications": ("evaluation-deployment-and-consequence", "metrics-and-targets", "word-error-versus-understanding"),
    "PromptEVC: Controllable Emotional Voice Conversion with Natural Language Prompts": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "VisualSpeech: Enhancing Prosody Modeling in TTS Using Video": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "Rollback Speech: Smart Feedback Prompts for Lost Utterances in Unstable Online Calls": ("listening-and-separation", "echo-and-reconstruction", "packet-loss-concealment"),
    "End-to-End Indian Language Dubbing with Zero-Shot Speaker Preservation": ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice"),
    "Granary: Speech Recognition and Translation Dataset in 25 European Languages": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
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
payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-provisional-d2-batch-046", "status": "analyst-reviewed-explicit-provisional-upgrade-batch", "claim_boundary": "These records upgrade clear provisional D2 candidates using preserved abstract evidence; they do not establish full-paper mechanism or independent reproduction.", "reviewed_count": len(rows), "rows": rows}
(DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-046.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
