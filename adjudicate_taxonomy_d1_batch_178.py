#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "tran25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects generated speech by selecting and combining self-supervised representations, with a sequence model for short- and long-range patterns and tests across datasets. The evidence supports spoofing-and-deepfake, bounded by the gated feature selection, Mamba module, in/out-of-domain comparison, and stated code release.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "tripathi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects speech boundaries by combining hand-designed MFCCs with pretrained representations and compares simple fusion against cross-attention. The evidence supports alignment, bounded by FusionVAD, the listed pretrained models, multiple datasets, efficiency comparison, and the reported improvement over Pyannote.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "tseng25_interspeech": (
        "confirmed-current-boundary",
        "The abstract probes neural codecs under changing noise conditions and relates robustness differences to nonlinearity and frequency response. The evidence supports distribution-shift, bounded by the codec set, noise conditions, linearity analysis, fidelity measures, and the stated real-world integration question.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "tuckute25_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts audio through a cochlea-inspired time-frequency representation into discrete tokens, predicts them autoregressively, and tests the resulting representation and reconstruction. The evidence supports windowed-spectrum, bounded by AuriStream's cochlear tokenization, SUPERB tasks, spectrogram/audio continuation, and stated phoneme/word results.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "windowed-spectrum",
    ),
    "turavecino25_interspeech": (
        "confirmed-current-boundary",
        "The abstract separates speech into a semantically rich representation and residual speaker/acoustic information so content and paralinguistics can remain while identity is reduced. The evidence supports voice-privacy, bounded by USC, reconstruction tradeoffs, codec comparisons, and the proposed privacy evaluation method.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
    ),
    "turnbull25_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares listeners' cross-language similarity judgments with acoustic-distance measures and shows effects of language background and presentation order. The evidence supports accent-robustness, bounded by English/French listener groups, proficiency, word pairs, six acoustic metrics, and the perceptual judgments.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
    ),
    "tzeng25_interspeech": (
        "confirmed-current-boundary",
        "The abstract improves naturalistic speech emotion recognition through balancing, activation, fine-tuning, and multimodal fusion rather than larger architectures. The evidence supports paralinguistic-state, bounded by the challenge task, RoBERTa/WavLM setup, valence CCC, and reported training-strategy comparisons.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "ueda25_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes emotion in imbalanced natural speech by aligning modalities, weighting classes, and stacking multiple models. The evidence supports paralinguistic-state, bounded by the 2025 naturalistic SER challenge, 12-model ensemble, eight classes, loss designs, and reported Macro-F1/accuracy.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
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
