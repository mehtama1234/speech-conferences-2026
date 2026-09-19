#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "negroni25_interspeech": (
        "confirmed-current-boundary",
        "The abstract defines source verification for synthetic speech and tests whether a track came from the same generator as reference signals, including open-set and post-processing vulnerabilities. The evidence supports spoofing and deepfake security, bounded by the reported attribution embeddings and forensic scenarios.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "nethil25_interspeech": (
        "confirmed-current-boundary",
        "The abstract multiplexes segmented command-style dictation across parallel ASR processes to reduce latency as concurrency grows, with courtroom deployment evidence. The governing boundary is latency and resource budget, bounded by the open-source framework and live-data evaluation.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "netzorg25_interspeech": (
        "confirmed-current-boundary",
        "The abstract varies pitch, resonance, and weight within a gender-affirming voice dataset and studies how acoustic measures relate to perceived gender, naturalness, and realness. The evidence supports within-speaker state variation, bounded by the DSFD configurations, EGG measures, and perception studies.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation",
    ),
    "neumann25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures speech, orofacial, and linguistic features against schizophrenia symptoms and clinical ratings, with speech features contributing to classification and correlations. The evidence supports clinical speech markers, bounded by the 94/100 participant groups, symptom scales, and reported correlations/classification.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "ng25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts a self-supervised speech representation with a small fraction of weights to improve recognition in noisy conditions and describes catastrophic forgetting and noise adaptation. The evidence supports distribution shift, bounded by noisy environments and the DFT fine-tuning comparison.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "nguyen25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses audio-visual information to recognize a target speaker in cocktail-party conditions and contributes talking-face and silent-face data for that setting. The evidence supports target-conditioned separation, bounded by the audio-visual cues, extreme-noise benchmark, and reported WER change.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "nguyen25c_interspeech": (
        "reassigned-to-neighbor",
        "The abstract transforms non-native speech toward a native-like accent while preserving speaker identity and prosody, using a streaming conversion model. The governing boundary is voice conversion, not accent robustness, because the system changes the acoustic realization rather than measuring recognition across accents.",
        ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion",
    ),
    "nguyen25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract presents automated collection and refinement of Vietnamese audio-visual speech data from raw video and evaluates a resulting baseline. The evidence supports speech-data collection, bounded by Vietnamese AVSR, automatic extraction, and clean/noisy evaluations.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
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
