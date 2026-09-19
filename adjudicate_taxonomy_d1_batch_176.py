#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "tang25_interspeech": (
        "confirmed-current-boundary",
        "The abstract trains one ASR model on speech and text so text can supply linguistic information and domain adaptation without speech data at adaptation time. The evidence supports acoustic-to-token, bounded by J-TAED, LibriSpeech and two out-of-domain sets, and reported WER changes.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token",
    ),
    "tannander25_interspeech": (
        "confirmed-current-boundary",
        "The abstract controls how English insertions sound inside Swedish TTS and measures listeners' preferred degree of English-accentedness. The evidence supports accent-robustness, bounded by the bilingual TTS conditioning scale, psychometric mapping, perception tests, and insertion-specific preferences.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
    ),
    "tanner25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses wav2vec2.0 to classify stop-burst realization and reproduce variation found by manual annotation in English and Japanese. The evidence supports articulatory-coordination, bounded by the two languages, curated and unprepared corpora, burst presence, and automatic/manual annotation comparisons.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "tao25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates source power statistics from a spherical microphone array in noise, then uses them for spatial beamforming and post-filtering. The evidence supports spatial-filtering, bounded by spherical harmonics, the multi-source noisy setting, simulation and experiment, and baseline comparisons.",
        ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering",
    ),
    "taylor25_interspeech": (
        "confirmed-current-boundary",
        "The abstract replaces noisy text descriptions with a few labeled audio examples for class-aware audio embeddings and compares this with zero-shot classification. The evidence supports few-shot-adaptation, bounded by contrastive audio-text embeddings, class grouping, and the reported few-shot versus zero-shot results.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation",
    ),
    "teleki25_interspeech": (
        "confirmed-current-boundary",
        "The abstract studies how whole-word substitution disfluencies alter conversational recommender performance and creates controlled synthetic examples at different rates. The evidence supports disfluency-preservation, bounded by Syn-WSSE, genre-based substitutions, tested LLMs, and the model-specific performance changes.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation",
    ),
    "teplansky25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures tongue and lip movement to compare Spanish and English vowel configurations in bilingual speakers. The evidence supports articulatory-coordination, bounded by isolated vowels, wearable electromagnetic articulography, five Spanish vowels, and the classification and cross-language comparisons.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "terashima25_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates speech pitch by combining a DSP-derived absolute-pitch prior with self-supervised learning and differentiable spectrograms. The evidence supports periodic-source, bounded by the SLASH losses and stabilization method, aperiodic-component prediction, and comparisons with DSP and SSL baselines.",
        ["title", "abstract"], "sound-and-production", "source-generation", "periodic-source",
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
