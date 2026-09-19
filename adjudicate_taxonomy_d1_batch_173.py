#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "suen25_interspeech": (
        "confirmed-current-boundary",
        "The abstract restores punctuation in naturally spoken Cantonese by creating annotations from an LLM and fine-tuning smaller language models. The evidence supports alignment, bounded by the low-resource Cantonese transcripts, YouTube source, LLM annotations, benchmark comparison, and public data/code.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "sun25_interspeech": (
        "confirmed-current-boundary",
        "The abstract learns pronunciation knowledge for words absent from a fixed TTS lexicon by adding transcribed speech audio to a multi-task frontend. The evidence supports pronunciation-variation, bounded by the Seq2Seq baseline, multi-task design, uncovered word types, and reported accuracy comparison.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "sun25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects Alzheimer’s disease from spontaneous speech while preserving phonetic events such as hesitations, repetitions, pauses, and mispronunciations in phoneme sequences. The evidence supports clinical-speech-marker, bounded by the phoneme recognizer, PPGs-BERT pipeline, cross-lingual aim, and stated diagnostic evaluation.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "sun25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract retrieves speech by emotional speaking style and aligns audio with natural-language descriptions using relation-aware contrastive learning. The evidence supports paralinguistic-state, bounded by ESSR/ESSD, ESS-CLAP and RA-CLAP, local matching, self-distillation, and reported retrieval tests.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "sun25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds one enhancement system for several realistic degradations rather than only fixed noise, using time-frequency dual paths and progressive scaling. The evidence supports speech-prior-denoising, bounded by the URGENT Challenge setting, architecture, limited-GPU training strategy, and Track 1 result.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "sun25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract explains Mandarin neutral-tone realization through neighboring tones, duration, syllable structure, and grammatical function in spontaneous conversation. The evidence supports prosodic-meaning, bounded by 8,550 phrase-medial tokens, the two neutral-tone subtypes, tonal context, and reported F0/duration patterns.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "sun25f_interspeech": (
        "confirmed-current-boundary",
        "The abstract proposes a score-learning criterion for energy-based TTS models so first-order inference uses a more suitable gradient of the likelihood. The evidence supports neural-vocoder, bounded by the comparison with NCE and sliced score matching, the energy-based training setting, and reported experiments.",
        ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder",
    ),
    "sun25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract denoises noisy-speech embeddings with a compact network and synthesizes clean speech through a vocoder, then tests enhancement and speaker fidelity. The evidence supports speech-prior-denoising, bounded by the pretrained generative audioencoder, denoise encoder, vocoder, ablation, listening tests, and reported fidelity results.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
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
