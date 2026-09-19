#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "oconnorrussell25_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts hold/shift turn-taking decisions under noise and uses visual cues to recover performance. The evidence supports turn boundary, bounded by the multimodal predictor, noise conditions, and reported accuracy changes.",
        ["title", "abstract"], "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary",
    ),
    "ofaolain25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract replaces ordinary acoustic inputs with auditory-transduction features and studies their effect on phoneme recognition under noise. The governing boundary is time-frequency signal measurement, not learned speech-unit discovery; the evidence is bounded by IHCograms, SNR conditions, and the AFE experiments.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "multi-resolution-signal",
    ),
    "ogura25_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts fundamental frequency, energy, and duration for expressive multi-speaker TTS without accent labels, using speaker-aware style embeddings. The evidence supports prosody control, bounded by the Japanese multi-speaker corpus and reported synthesis comparisons.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "oh25_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts five human-rated L2 speech proficiency scores with a multimodal multitask model and trait-aware loss. The evidence supports calibration and selective use, bounded by the five criteria, embeddings, and reported correlation results.",
        ["title", "abstract", "full_paper_excerpt"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use",
    ),
    "oh25b_interspeech": (
        "reassigned-to-neighbor",
        "The abstract trains one speech-assessment system across English, German, and French and compares seen and unseen language data. The governing boundary is cross-lingual transfer, not accent robustness, because the central question is sharing assessment structure across languages.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "oh25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses CTC-derived alignment positions to mask decoder cross-attention and improve long-form ASR. The evidence supports long-context decoding, bounded by concatenated LibriSpeech utterances, the attention intervention, and reported error reduction.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding",
    ),
    "ohashi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract develops a Japanese full-duplex dialogue model that handles overlap and backchannels while listening and speaking simultaneously. The evidence supports turn boundary, bounded by the Japanese data, two-stage training, synthetic dialogue, and naturalness/meaningfulness evaluation.",
        ["title", "abstract"], "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary",
    ),
    "ohnaka25_interspeech": (
        "confirmed-current-boundary",
        "The abstract constrains phonemic and prosodic labels to align with graphemes and measures the resulting consistency and downstream accent estimation. The evidence supports alignment, bounded by implicit/explicit grapheme conditioning and the created parallel labels.",
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


if __name__ == "__main__": main()
