#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "reuter25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures how language similarity changes non-target speaker-verification scores across multilingual and unseen-language trials. The evidence supports speaker verification, bounded by ECAPA-TDNN, VoxCeleb training variants, and Globalphone/LDC CTS analyses.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
    ),
    "rittergutierrez25_interspeech": (
        "confirmed-current-boundary",
        "The abstract distills speech and music self-supervised encoders into a unified representation and evaluates the result on both domains. The evidence supports self-supervised speech units, bounded by task arithmetic, adjustable domain emphasis, and the speech/music benchmarks.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "rolland25_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates weight sharing in ASR architectures to reduce parameters while preserving accuracy and tests low-resource children’s ASR. The evidence supports latency and resource budget, bounded by Shared-Conformer, the 63% reduction, and WER/low-resource comparisons.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "roman25_interspeech": (
        "confirmed-current-boundary",
        "The abstract describes a Whisper-based Catalan transcription and translation tool adapted to dialectal varieties and academic terminology for higher education. The evidence supports alignment, bounded by Catalan, the transcription/translation workflow, and the stated accessibility use.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "rommel25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures pre-aspiration duration and noise in Icelandic speakers and relates the production pattern to gender/sex. The evidence supports articulatory coordination, bounded by the 20-speaker picture-naming task and the measured breathiness/voiceless-pre-aspiration outcomes.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "roquefort25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses anonymized speech transcripts to classify suicide risk in Chinese adolescents and reports prompt and model comparisons. The evidence supports clinical speech markers, bounded by transcript-only linguistic features, the SW1 challenge, and the reported held-out results.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "rosero25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts ASR to pediatric speech sound disorders and tests TTS/voice-conversion synthesis under data scarcity and privacy constraints. The evidence supports atypical and assistive speech, bounded by the 77-minute dataset, synthetic pretraining, and the reported zero-shot/finetuned comparisons.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "ross25_interspeech": (
        "confirmed-current-boundary",
        "The abstract analyzes context-dependent pitch, vowel, and /s/ changes in trans men’s speech and connects them to gender perception, self-monitoring, and authenticity. The evidence supports within-speaker state variation, bounded by seven participants, imagined listeners, recordings, and interviews.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation",
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
