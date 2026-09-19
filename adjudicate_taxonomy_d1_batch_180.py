#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "vauquier25_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates voice anonymization with legal privacy concepts translated into linkability and singling-out measures, exposing residual risk that EER misses. The evidence supports voice-privacy, bounded by the legal definitions, French authority validation, attack scenarios, and metric comparison.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
    ),
    "verdini25_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares adapters, speech foundation models, and language models for mapping speech representations into an LLM space for recognition and translation. The evidence supports acoustic-to-token, bounded by the five adapters, two SFMs, two LLMs, two tasks, and reported component effects.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token",
    ),
    "vesterbacka25_interspeech": (
        "confirmed-current-boundary",
        "The abstract fine-tunes Swedish ASR models on a large, varied corpus to improve performance for a mid-resourced language. The evidence supports speech-data-collection, bounded by Swedish Whisper models, the corpus scale and variability, three evaluation corpora, and reported WER reduction.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "vidal25_interspeech": (
        "confirmed-current-boundary",
        "The abstract makes disfluencies part of Spanish children’s reading-ASR decoding through synthetic disfluent text and in-domain acoustic adaptation. The evidence supports disfluency-preservation, bounded by the children’s reading dataset, disfluentES generation, language-model comparisons, and ASR/fluency outcomes.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation",
    ),
    "vieting25_interspeech": (
        "confirmed-current-boundary",
        "The abstract regularizes learnable ASR front ends against overfitting with audio perturbations and STFT-domain masking. The evidence supports distribution-shift, bounded by learnable versus fixed features, the two regularization approaches, SpecAugment limitations, and reported gap closure.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "villani25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reshapes clean speech before playback under an energy limit so it remains more intelligible in noise, using long-term noise statistics and optional compression. The evidence supports perceptual-enhancement, bounded by the SII-based method, noise fractiles, simulations, comparator methods, and stated listening benefit.",
        ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement",
    ),
    "visser25_interspeech": (
        "confirmed-current-boundary",
        "The abstract studies how the size and duration of discretized self-supervised speech units affect spoken-language modeling and resynthesis. The evidence supports self-supervised-speech-units, bounded by DPDP, codebook/coarseness comparisons, phone/word/sentence tasks, and bitrate/accuracy findings.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "vlasenko25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether multilingual acoustic and linguistic representations preserve sentence-mode information such as suprasegmental distinctions across languages. The evidence supports prosodic-meaning, bounded by Italian/French/German and EMO-DB data, intra/inter-language protocols, fusion choices, and WHISPER transcript comparison.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
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
