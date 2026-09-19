#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "park25_interspeech": (
        "confirmed-current-boundary",
        "The abstract selects untranscribed target-domain speech for semi-supervised ASR using estimated word error and acoustic domain similarity. The evidence supports self-training and pseudo-label expansion, bounded by the two selection signals and the reported fraction of supervised improvement.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "park25b_interspeech": (
        "reassigned-to-neighbor",
        "The abstract reduces TTS generation steps while preserving high-fidelity speech through consistency-constrained flow matching. The governing boundary is latency and resource budget, not a vocoder architecture, because inference speed is the central claimed tradeoff.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "park25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates dysarthric speech clarity and locates and classifies mispronunciations with therapist-annotated temporal markers. The evidence supports atypical and assistive speech, bounded by six speakers, two passages, the staged assessment, and the ASR analysis.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "park25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract combines ASR, speech-language modeling, and supervised classification to detect Alzheimer’s disease from speech and reports a comparison with non-chain-of-thought methods. The evidence supports clinical speech markers, bounded by the stated speech-to-text pipeline and AD/non-AD classification.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "park25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract generates multi-speaker audiobooks with speaker personas and expressive, consistent prosody without additional training and evaluates naturalness and quality. The evidence supports intelligibility and naturalness, bounded by the zero-shot audiobook setting and human/MLLM comparisons.",
        ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness",
    ),
    "park25f_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates character error on nearly 4,000 hours of untranscribed Arabic dialect speech to select reliable segments for pseudo-transcript training. The evidence supports self-training and pseudo-label expansion, bounded by the Arabic dialect data and CER-based selection.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "park25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts Whisper to Korean autistic speech and compares full, selective, adapter, and LoRA fine-tuning under limited data. The evidence supports atypical and assistive speech, bounded by the ASD dataset, ASR CER, and tested adaptation strategies.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "parsons25_interspeech": (
        "confirmed-current-boundary",
        "The abstract studies which prosodic cues distinguish closely related dialects and tests low-pass filtering and F0 monotonization in Norwegian dialect identification. The evidence supports dialect and variety, bounded by Norwegian data, the signal manipulations, and the DID evaluation.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
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
