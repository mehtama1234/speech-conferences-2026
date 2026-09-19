#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "phaye25_interspeech": (
        "confirmed-current-boundary",
        "The abstract trains speech enhancement with the model encoder serving as a task-relevant loss and evaluates perceptual quality and generalization. The evidence supports speech-prior denoising, bounded by the speech-enhancement benchmarks and clean-reference consistency objective.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "phukan25_interspeech": (
        "rejected-out-of-scope",
        "The abstract studies source attribution for singing-voice deepfakes and multimodal/music foundation models, not spoken speech or spoken-language communication. Singing-voice source attribution is outside this speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "phukan25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract fuses neural-codec and speech-representation features to recognize emotion and reports comparative SER performance. The evidence supports paralinguistic state, bounded by the HYFuse representation types and stated emotion-recognition evaluations.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "phukan25c_interspeech": (
        "rejected-out-of-scope",
        "The abstract classifies heart murmurs from heart-sound audio and does not establish spoken speech or spoken-language communication. Heart-sound classification is outside this speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "phukan25d_interspeech": (
        "rejected-out-of-scope",
        "The abstract predicts mean opinion scores for synthesized singing voices using speaker and music models, not quality of spoken speech. Singing-voice quality prediction is outside this spoken-speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "phukan25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract fuses Mamba and attention-based speech models for speech emotion recognition and compares heterogeneous representation combinations. The evidence supports paralinguistic state, bounded by the PARROT fusion method and SER evaluations.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "phukan25f_interspeech": (
        "rejected-out-of-scope",
        "The abstract detects harmful content in online videos by aligning generic audio and visual cues, without establishing spoken speech or a spoken-language task. Generic audio-visual content moderation is outside this speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "phukan25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract studies machine unlearning for speech emotion and depression detection and measures retained performance after removing learned information. The evidence supports voice privacy, bounded by SISA++ and the CREMA-D/E-DAIC evaluations.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
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
