#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ugan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts a multilingual ASR model without replaying original data and addresses catastrophic forgetting through factorization and centralization of low-rank adapters. The evidence supports distribution-shift, bounded by the rehearsal-free code-switching sequence, two training phases, and reported forgetting results.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "uniyal25_interspeech": (
        "confirmed-current-boundary",
        "The abstract benchmarks self-supervised representations and training choices for emotion recognition under naturalistic variability and imbalance. The evidence supports paralinguistic-state, bounded by the MSP-Podcast corpus, challenge setting, fine-tuning/layer-freezing/loss comparisons, and the stated robustness aim.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "urai25_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases a large Thai bona-fide/spoof corpus covering TTS systems, ages, speaking styles, and telephony, then tests anti-spoofing models under unseen conditions. The evidence supports spoofing-and-deepfake, bounded by CSS, 1,332,120 utterances, five TTS systems, baselines, and the reported style/attack limitations.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "vaessen25_interspeech": (
        "confirmed-current-boundary",
        "The abstract turns noisy Dutch archival television into self-supervised pretraining data through quality analysis and preprocessing, then compares monolingual and multilingual training. The evidence supports speech-data-collection, bounded by the 55,000-hour archive, music/noise/overlap effects, Whisper/WhisperX preprocessing, and downstream comparisons.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "valente25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adds clinician-created multimodal stuttering annotations and an expert-consensus test set for training and evaluating severity models. The evidence supports clinical-speech-marker, bounded by FluencyBank, annotation categories, clinician labeling, consensus reliability, and the stated model-training implications.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "vanbemmel25_interspeech": (
        "confirmed-current-boundary",
        "The abstract describes a Dutch COPD speech-collection study designed to support remote respiratory assessment, including task-quality checks and planned data release. The evidence supports clinical-speech-marker, bounded by SPEAKtoCOPD, the flashmob methodology, COPD participants, Dutch speech tasks, and the stated quality-control goal.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "vandalen25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts a recognizer to a new speaker from little unlabeled data by minimizing entropy over multiple hypotheses and estimating a compact speaker code. The evidence supports distribution-shift, bounded by one/f ten-minute adaptation, far-field noise-augmented Common Voice, the two adaptation components, and WER changes.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "vangysel25_interspeech": (
        "confirmed-current-boundary",
        "The abstract recovers rare voice-search titles by generating phonetic alternatives and rescoring them with the ASR output. The evidence supports domain-and-context-biasing, bounded by movie-title search, phonetic correction and rescoring, benchmark baselines, and reported WER improvements.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing",
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
