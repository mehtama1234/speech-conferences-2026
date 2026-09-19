#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "song25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract combines a skin-attached accelerometer with a microphone to enhance noisy speech while controlling phase and computation. The evidence supports non-airborne-sensing, bounded by the TAPS data, ACC/MIC fusion, LAU-Net, PESQ result, and stated real-time efficiency.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
    ),
    "sosawelford25_interspeech": (
        "confirmed-current-boundary",
        "The abstract creates a Spanish TTS naturalness dataset from human ratings and validates it with automatic prediction models. The evidence supports quality-and-naturalness, bounded by 4,326 samples, 52 systems and human voices, 92 raters, the P.807-based test, and the reported MAE.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness",
    ),
    "sridhar25_interspeech": (
        "confirmed-current-boundary",
        "The abstract benchmarks Whisper on fluent and stuttered speech, separating sound repetitions and measuring transcription errors and hallucinations. The evidence supports dysarthria-and-atypical-speech, bounded by the podcast samples, stuttering patterns, Whisper evaluation, and the disability-led study framing.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "srinivasavaradhan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates TTS by whether listeners mistake generated speech for human speech and argues that ordinary parity scores can set a weak bar. The evidence supports spoofing-and-deepfake, bounded by the Human Fooling Rate, tested commercial and open-source systems, speech data, and human deception protocol.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "srinivasmenon25_interspeech": (
        "confirmed-current-boundary",
        "The abstract separates language information from speaker embeddings so recognition remains effective across languages and language switches. The evidence supports speaker-verification, bounded by the prefix-tuned cross-attention method, multilingual and unseen-language tests, and reported equal-error-rate comparisons.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
    ),
    "stan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract traces the source model of an audio deepfake and detects samples from unseen generators using a training-free nearest-neighbor method. The evidence supports spoofing-and-deepfake, bounded by the pretrained SSL representation, five datasets, reported F1 scores, and the stated out-of-domain protocol.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "stein25_interspeech": (
        "confirmed-current-boundary",
        "The abstract models probabilistic reduction as shortened acoustic word duration under contextual predictability and compares information-theoretic and discriminative predictors. The evidence supports pronunciation-variation, bounded by the Buckeye corpus, three model families, duration outcome, and the reported predictor comparisons.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "stucki25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts a voice model to Swiss German dialects using weakly labeled podcast speech and evaluates whether the generated voice renders the desired dialect. The evidence supports dialect-and-variety, bounded by the 5,000-hour corpus, automatic dialect labels, XTTSv2 adaptation, and human/automatic scores.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
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
