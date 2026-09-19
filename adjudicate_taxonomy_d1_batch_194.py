#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "yong25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests how speaker count, per-speaker duration, and accent diversity affect recognition of unseen accents when training data are limited. The evidence supports speaker-adaptation, bounded by the low-resource ASR setting, controlled speaker/hour comparisons, unseen accents, and the reported finding that more speakers matter most.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation",
    ),
    "yong25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses locally generated visual scenes to elicit speech for cognitive assessment, testing whether changing prompts preserves assessment performance while broadening data collection. The evidence supports clinical-speech-marker, bounded by HK-GenSpeech, 423 Cantonese samples from 141 participants, HK-MoCA scores, image conditions, and regression/lexical results.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "yoon25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reduces the sampling steps needed by a flow-matching TTS model through adversarial post-training while retaining high-fidelity speech. The evidence supports neural-vocoder, bounded by APTTS and Matcha-TTS, reconstruction/adversarial objectives, multi-speaker evaluation, sampling reduction, and reported quality/inference-time results.",
        ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder",
    ),
    "yosha25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adds sentence-stress labels to transcription so the output records which words carry emphasis and therefore contributes to speaker intent. The evidence supports prosodic-meaning, bounded by WHISTRESS, synthetic TINYSTRESS-15K training data, alignment-free inference, zero-shot benchmarks, and the reported stress-detection comparison.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "you25_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects depression from audio and text across English and Chinese while adapting the model to the target language with multilingual and multimodal representations. The evidence supports clinical-speech-marker, bounded by M3L/LAFT, DAIC-WOZ and EATD, Whisper/XLM-RoBERTa inputs, low-resource transfer, and the reported gains.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "young25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests depression detection when dementia creates overlapping clinical speech signals, then reweights features to emphasize depression-related information. The evidence supports clinical-speech-marker, bounded by the comorbidity dataset, dementia/no-decline comparison, Wasserstein weighting, and the reported F1 result.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "ys25_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares acoustic and transcript embeddings for grading dysarthria severity in ALS and tests whether combining both reflects finer severity levels. The evidence supports clinical-speech-marker, bounded by 47 ALS subjects, two/three/five-class settings, MFCC and text features, human/ASR transcripts, and reported mean F1 scores.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "yu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract makes one recurrent model switch between ordinary voice activity detection and speaker-conditioned detection by detaching the personalization module and skipping unnecessary non-speech computation. The evidence supports alignment, bounded by FDE-RNN, VAD/PVAD modes, gating, parameter use, and the reported efficiency/performance results.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
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
