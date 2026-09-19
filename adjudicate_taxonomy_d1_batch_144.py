#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "mousavi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts language-model-style systems to speech and audio through learned soft prompts and reports reduced dependence on ASR or captioning data. The governing taxonomy boundary is learned speech units and representations, bounded by the multitask LiSTEN experiments.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "moussa25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract studies pretrained self-supervised speech-model representations, brain-tuning, and the progression from acoustic to semantic layers. The governing boundary is learned speech representations, not room, microphone, or non-airborne sensing.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "mujtaba25_interspeech": (
        "confirmed-current-boundary",
        "The abstract targets stuttered speech, whose disfluencies produce ASR errors and accessibility barriers, and compares generalized with personalized adaptation. The evidence supports atypical and assistive speech, bounded by stuttering, speaker personalization, and the reported voice-AI scenarios.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "muller25_interspeech": (
        "confirmed-current-boundary",
        "The abstract demonstrates that replaying and re-recording synthetic audio can defeat deepfake detectors and introduces a multilingual replay dataset. The evidence supports spoofing and deepfake security, bounded by the six languages, four TTS models, detector set, and replay conditions.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "mun25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses glottal and spectrogram properties as speech biomarkers for chronic kidney disease diagnosis and reports an interpretable classifier. The evidence supports clinical speech markers, bounded by CKD, the fused acoustic features, and the reported diagnostic evaluation.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "mun25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates autism-spectrum social-communication severity from acoustic and linguistic speech features and compares the output with human ratings. The evidence supports clinical speech markers, bounded by children with ASD, the multimodal cascade, and the reported correlation.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "mun25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract compresses speaker-recognition models for on-device use while preserving performance on hard boundary cases. The evidence supports latency and resource budget, bounded by channel pruning, memory/parameter reduction, and hard-set speaker recognition.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "murata25_interspeech": (
        "confirmed-current-boundary",
        "The abstract proposes a speaker-agnostic emotion vector for controlling emotion intensity across target speakers while preserving identity and quality. The evidence supports style and emotion control, bounded by neutral-source speech, unseen speakers, and the reported control evaluation.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
}


def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({
            "taxonomy_review_state": "taxonomy-adjudicated",
            "final_decision": decision,
            "reviewer_note": note,
            "reviewed_sections": sections,
            "final_theme_id": theme,
            "final_subtheme_id": subtheme,
            "final_concept_id": concept,
        })
    adjudicated = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["adjudicated_count"] = adjudicated
    payload["open_count"] = len(rows) - adjudicated
    decisions = sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in decisions}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": adjudicated, "open": payload["open_count"]}))


if __name__ == "__main__":
    main()
