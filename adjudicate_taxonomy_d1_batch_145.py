#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "murata25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract generates diverse unseen speaker voices by sampling a learned eigenvoice space and reports controllable speaker attributes. The governing boundary is zero-shot voice generation, bounded by the DNN model-editing method and generated-speaker experiments.",
        ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice",
    ),
    "naini25_interspeech": (
        "confirmed-current-boundary",
        "The abstract organizes a naturalistic speech-emotion-recognition challenge with categorical and dimensional emotion labels and speaker-independent evaluation. The governing boundary is paralinguistic state, bounded by the challenge data, tracks, and reported systems.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "nakagome25_interspeech": (
        "confirmed-current-boundary",
        "The abstract biases a CTC recognizer toward rare and unknown words at inference time using wildcard keyword spotting and intermediate-layer biasing. The evidence supports domain and context biasing, bounded by Japanese recognition and the reported unknown-word F1 result.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing",
    ),
    "nam25_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts a streaming ASR model to non-streaming operation with a full-context adapter while limiting added parameters. The evidence supports latency and resource budget, bounded by the Conformer RNN-T setting and the reported parameter/performance comparison.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "nam25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract refines speaker embeddings under clean/noisy environmental mismatch without changing the recognition pipeline. The evidence supports speaker verification, bounded by diffusion-based embedding repair and the simulated mismatch evaluations.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
    ),
    "narain25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract models interpretable voice-quality dimensions across atypical and affective speech and tests transfer across speakers, languages, and tasks. The governing boundary is speaker and state variation, not a generic quality metric, because the dimensions describe speech variation itself.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation",
    ),
    "naseem25_interspeech": (
        "confirmed-current-boundary",
        "The abstract develops Punjabi Shahmukhi speech resources, a phonetic lexicon, text analysis, and Urdu/Punjabi TTS models, with script and pronunciation comparisons. The evidence supports speech-data collection, bounded by the stated languages, scripts, resources, and evaluations.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "navon25_interspeech": (
        "confirmed-current-boundary",
        "The abstract extracts a chosen speaker from a mixture using enrollment audio and conditional flow matching, with a vocoder for phase reconstruction. The evidence supports target-conditioned separation, bounded by the enrollment-plus-mixture input and standard TSE benchmarks.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
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
