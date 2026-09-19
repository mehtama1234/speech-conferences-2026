#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "zezario25_interspeech": (
        "confirmed-current-boundary",
        "The abstract improves non-intrusive intelligibility prediction for hearing aids by weighting spectral, temporal, and Whisper-derived features according to their frame-level importance. The evidence supports accessibility-fit, bounded by FiDo/MBI-Net+, the Clarity challenge comparison, RMSE results, and the hearing-aid assessment setting.",
        ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit",
    ),
    "zgorzynski25_interspeech": (
        "confirmed-current-boundary",
        "The abstract jointly classifies emotion categories and predicts continuous emotional attributes from naturalistic speech using multiple encoders and a shared fusion/training setup. The evidence supports paralinguistic-state, bounded by the INTERSPEECH challenge, classification/regression tasks, multimodal encoders, ablation, and placement/results.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "zhang25_interspeech": (
        "confirmed-current-boundary",
        "The abstract supplies precisely timed acoustic-landmark annotations, an open extraction toolkit, and baselines so events can be located consistently relative to phoneme boundaries. The evidence supports alignment, bounded by TIMIT, manual/phoneme-informed annotation, landmark detection, and the dataset/toolkit scope.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "zhang25b_interspeech": (
        "confirmed-current-boundary",
        "The paper measures how listeners perceive the four tones of Changde Mandarin and finds that some contrasts are non-categorical. The evidence supports dialect-and-variety, bounded by Changde Mandarin, tone continua, production/perception cues, and the reported T1–T4 perceptual patterns.",
        ["title", "abstract", "full_paper"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
    ),
    "zhang25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract imposes monotonic text-to-speech attention so generated speech follows the input sequence without repetitions, omissions, or misalignment. The evidence supports text-to-speech-planning, bounded by the stepwise attention algorithm, VALL-E R comparison, no forced aligner, out-of-domain testing, and scaling claims.",
        ["title", "abstract"], "voice-generation-and-control", "content-planning", "text-to-speech-planning",
    ),
    "zhang25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates audio encoders across 22 tasks and multiple domains rather than treating one downstream score as general representation quality. The evidence supports calibration-and-selective-use, bounded by X-ARES, linear and unparameterized evaluation, speech/environment/music tasks, and the reported cross-task variation.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use",
    ),
    "zhang25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether noise in measured room impulse responses changes how faithfully spherical-harmonic reproduction recreates speech perception in real rooms. The evidence supports reverberant-mixture, bounded by measured RIRs, spatial reproduction, listening tests, distance and reverberation conditions, and the low-noise-floor finding.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "reverberant-mixture",
    ),
    "zhang25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract introduces partially edited speech examples and tests both whether the edit is detected and where it occurs, exposing a gap in detectors trained on wholly spoofed speech. The evidence supports spoofing-and-deepfake, bounded by PartialEdit, neural speech editing/codecs, detection/localization tasks, PartialSpoof transfer failure, and artifact analysis.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
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
