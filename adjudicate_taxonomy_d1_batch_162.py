#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "rossenbach25_interspeech": (
        "confirmed-current-boundary",
        "The abstract simulates memristor execution of a Conformer ASR model and measures quantization-related WER degradation for energy-efficient hardware. The evidence supports latency and resource budget, bounded by TED-LIUMv2, 3-bit weights, and the simulated analog-computation setting.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "rouas25_interspeech": (
        "confirmed-current-boundary",
        "The abstract prunes transformer weight tiles for speech recognition and translation and reports systolic-array speedups and energy reduction. The evidence supports latency and resource budget, bounded by MuST-C, pruning rates, performance loss, and hardware acceleration.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "rustagi25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract provides Hindi computer-assisted pronunciation training that detects phonemic mispronunciations and gives personalized feedback, including synthetic error speech. The governing boundary is pronunciation variation, not clinical speech markers.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "ryu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adds pitch-contour features to speech emotion recognition and measures valence, arousal, and dominance across datasets. The evidence supports paralinguistic state, bounded by PCM, pitch normalization, and MSP-Podcast/IEMOCAP results.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "ryu25b_interspeech": (
        "rejected-out-of-scope",
        "The abstract converts microphone characteristics for generic sound-event classification and does not establish a spoken-speech or spoken-language task. Generic sound-event device conversion is outside this speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "sadok25_interspeech": (
        "confirmed-current-boundary",
        "The abstract explains how neural audio-codec tokens encode speech content, identity, and pitch and trains a post-hoc extractor for those attributes. The evidence supports sampling and quantization, bounded by codec tokens, the two-stage analysis/synthesis process, and speech attributes.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "sampling-and-quantization",
    ),
    "sage25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures visual articulator features in 189 children’s Polish sibilants and relates them to sibilance patterns for computer-aided speech diagnosis. The evidence supports atypical and assistive speech, bounded by age range, sibilant contrasts, visual features, and mixed-effects analysis.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "saijo25_interspeech": (
        "confirmed-current-boundary",
        "The abstract presents a universal speech-enhancement challenge spanning distortions, languages, noisy training, and subjective/objective evaluation. The evidence supports speech-prior denoising, bounded by 32 submissions, challenge conditions, and the reported generative/hybrid findings.",
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


if __name__ == "__main__": main()
