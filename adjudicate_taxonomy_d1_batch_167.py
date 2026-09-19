#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "sheikh25_interspeech": (
        "confirmed-current-boundary",
        "The abstract presents a large crowdsourced collection of spontaneous two-person speech conversations, with qualification and recording procedures. The evidence supports speech-data-collection, bounded by the English MTurk conversations, task design, quality checks, and stated dataset uses.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "shen25_interspeech": (
        "confirmed-current-boundary",
        "The abstract enhances noisy-reverberant multi-channel speech by feeding previous target estimates and beamformed mixtures into an autoregressive model. The evidence supports speech-prior-denoising, bounded by the frame-online setting, the proposed parallel training, and the reported noisy-reverberant tests.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "shen25b_interspeech": (
        "reassigned-to-neighbor",
        "The paper studies whether feature-attribution explanations for speech classifiers are reliable under different input types, aggregation choices, and perturbation spans. This is a boundary on when model outputs may be trusted or selectively used, not a human speech-quality target; the evidence supports calibration-and-selective-use, bounded by the speech classification tasks and attribution methods examined.",
        ["title", "abstract", "full_paper"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use",
    ),
    "shepardson25_interspeech": (
        "confirmed-current-boundary",
        "The abstract demonstrates an interactive text-conditional voice-generation system for live artistic performance, including training, real-time inference, and a control interface. The evidence supports text-to-speech-planning, bounded by the low-resource IATV task, the Tungnaá implementation, and the described performance application.",
        ["title", "abstract"], "voice-generation-and-control", "content-planning", "text-to-speech-planning",
    ),
    "shi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract targets emotion recognition across acoustic domains and introduces prompt tuning and contrastive training to reduce domain shift. The governing boundary is performance under changed acoustic conditions, so the evidence supports distribution-shift, bounded by the five benchmark datasets and the supervised/domain-generalization experiments.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "shi25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts pairwise listener preference between generated speech samples by combining two absolute MOS estimates into a relative score and tests this on in- and out-of-domain data. The evidence supports quality-and-naturalness, bounded by the preference model, MOS-derived pairwise data, and reported prediction comparisons.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness",
    ),
    "shi25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes emotion in conversation by combining who is speaking, when the context occurred, and what was said, with a speaker-similarity loss. The evidence supports paralinguistic-state, bounded by the historical interactions, speaker/content/context inputs, and single-modal and multimodal tests.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "shi25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract models speaker-specific and emotion-specific representations jointly and explicitly disentangles them for speech emotion recognition. The evidence supports paralinguistic-state, bounded by speaker-dependent and speaker-independent SER settings and the reported multi-task and disentanglement comparisons.",
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
