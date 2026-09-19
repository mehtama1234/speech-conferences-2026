#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "rai25_interspeech": (
        "confirmed-current-boundary",
        "The abstract benchmarks subgroup disparities in ASR and combines WER with a fairness-adjusted score across demographic groups. The evidence supports auditability and contestability, bounded by Fair-Speech, mixed-effects scoring, and the ASR-FAIRBENCH leaderboard.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability",
    ),
    "raju25_interspeech": (
        "confirmed-current-boundary",
        "The abstract performs Indian-language dubbing while preserving speaker characteristics across accent, age, and gender through zero-shot synthesis. The evidence supports zero-shot voice, bounded by the ASR/MT/TTS platform and stated deployment context.",
        ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice",
    ),
    "ram25_interspeech": (
        "confirmed-current-boundary",
        "The abstract curates annotated bilingual speech disfluencies and studies filled pauses and repairs associated with cognitive fatigue. The evidence supports disfluency preservation, bounded by the 20-plus-hour dataset, bilingual speakers, and the reported fatigue pattern.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation",
    ),
    "raman25_interspeech": (
        "confirmed-current-boundary",
        "The abstract analyzes oral-reading errors in 595 Grade 3 children across English and Hindi and links the patterns to reading assessment and phone recognition. The evidence supports age and development, bounded by the grade, languages, reading passages, and error categories.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "rangappa25_interspeech": (
        "confirmed-current-boundary",
        "The abstract filters pseudo-labeled call-center speech with WER, NER, and CER signals before domain adaptation and retains performance using only 100 of 7,500 hours. The evidence supports self-training and pseudo-label expansion, bounded by the Whisper/Zipformer pipelines and Fisher comparison.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "ranjan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract creates a multilingual dataset distinguishing real/fake and normal/hate speech in synthetic audio and evaluates detector generalization across languages. The evidence supports spoofing and deepfake security, bounded by 37 languages, the four classes, and cross-dataset results.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "ranjan25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects hate speech in deepfake audio with a multimodal cross-lingual representation and tests unseen languages. The evidence supports spoofing and deepfake security, bounded by 127,290 paired samples, six languages, and the two multilingual test sets.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "raokoluguri25_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases recognition and translation data for 25 European languages, cleans pseudo-labels, and evaluates models on high- and low-resource conditions. The evidence supports speech-data collection, bounded by Granary, its filtering pipeline, and the reported data-efficiency comparison.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
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


if __name__ == "__main__": main()
