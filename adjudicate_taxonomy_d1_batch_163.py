#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "sakuma25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract assigns speaker labels to all frames in overlapping speech and improves serialized multi-talker ASR without an enrolled target. The governing boundary is blind source separation, not target-conditioned separation, because no selected source cue is required.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation",
    ),
    "saladukha25_interspeech": (
        "confirmed-current-boundary",
        "The abstract combines multichannel inputs and attention to choose useful channels for keyword spotting under laboratory and natural noise, while measuring denoising, KWS, and compute. The evidence supports nonstationary-noise handling, bounded by the two datasets and channel-selection comparisons.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "nonstationary-noise",
    ),
    "salihs25_interspeech": (
        "confirmed-current-boundary",
        "The abstract presents community-led collection practices and an open Akan impaired-speech dataset, then tunes ASR models on it. The evidence supports speech-data collection, bounded by the cookbook, Akan proof of concept, participants, and released tools/data.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "sanchez25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reconstructs a dysarthric speaker’s pre-condition voice with TTS for communication assistance and measures intelligibility and identity control. The evidence supports augmentative communication, bounded by Parler TTS, the curated annotations, and the reported controllability limits.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication",
    ),
    "sanders25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract changes discrete codebook segmentation to preserve prosodic and paralinguistic information in compressed speech representations and tests resynthesis. The governing boundary is self-supervised speech units, not calibration, bounded by SVC streams, probing, and resynthesis results.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "sanguedolce25_interspeech": (
        "confirmed-current-boundary",
        "The abstract classifies post-stroke impaired speech using acoustic and physiologically informed glottal features and reports SHAP-supported clinical analysis. The evidence supports clinical speech markers, bounded by the stroke database, pathological/healthy comparison, and reported F1 result.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "sankala25_interspeech": (
        "confirmed-current-boundary",
        "The abstract constructs realistic adversarial noise attacks against text-dependent speaker verification without the spoken password and measures bypass success. The evidence supports spoofing and deepfake security, bounded by the TD-SV threat model and reported attack rate.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "sankar25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract introduces a 13,000-hour, 23-language resource with 24 million attribute descriptions and trains an open multilingual expressive TTS model. The governing boundary is speech-data collection, not accent robustness alone, bounded by RASMALAI and its TTS evaluations.",
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
