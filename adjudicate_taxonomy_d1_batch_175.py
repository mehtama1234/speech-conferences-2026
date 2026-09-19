#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "tadevosyan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract makes unlabeled speech usable for ASR through an open pipeline for collection, pseudo-labeling, and training, including low-resource languages. The evidence supports self-training-and-pseudo-labels, bounded by Portuguese, Armenian, and Spanish experiments, TopIPL, public-data licensing, and reported WER changes.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "takagi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract makes fundamental frequency directly controllable in a neural audio codec by adding periodic signals to the decoder, then tests singing-voice synthesis. The evidence supports prosody-control, bounded by the codec architecture, F0 manipulation, singing-voice training data, and reported quality comparisons.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "takahashi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract fine-tunes a pretrained ASR model for dysarthric speech with preprocessing, augmentation, and faster decoding, and reports a challenge result. The evidence supports dysarthria-and-atypical-speech, bounded by the SAP challenge, Parakeet-TDT system, baseline Whisper comparison, and reported WER.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "talkar25_interspeech": (
        "confirmed-current-boundary",
        "The abstract derives a cross-language articulatory-precision measure from phonetic outputs and relates it to pronunciation, clinical, and intelligibility measures. The evidence supports articulatory-coordination, bounded by 12 languages, Wav2Vec 2.0 outputs, ALS speech data, correlation tests, and the stated clinical use.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "tam25_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases a longitudinal, clinically annotated speech corpus linking recordings to disease, cognitive, clinical, and blood-based measures, then tests benchmark models. The evidence supports clinical-speech-marker, bounded by 780 participants, 5,169 recordings, 1,033 assessments, listed disorders, and preliminary prediction results.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "tamir25_interspeech": (
        "confirmed-current-boundary",
        "The abstract segments a conversation into changing emotional states by synchronizing word-level text and frame-level audio representations and evaluating emotion boundaries. The evidence supports paralinguistic-state, bounded by WavLM/EmoBERTa inputs, temporal smoothing, EDER, and the reported multimodal comparison.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "tan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract aligns serialized multi-speaker ASR output with utterance timestamps and speaker-change points through a soft monotonic constraint. The evidence supports alignment, bounded by SMA-SOT, AliMeeting, CER, speaker-change accuracy, and comparisons with SOT and BA-SOT.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "tan25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts Whisper to low-resource dysarthric speech through parameter-efficient fine-tuning, curriculum filtering, and postprocessing for stuttering and hallucination. The evidence supports dysarthria-and-atypical-speech, bounded by the three datasets, reduced training data, SAP challenge test, WER/SemScore, and baseline comparison.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
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
