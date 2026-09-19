#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "phuong25_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects synthetic speech and spoofing attacks against speaker verification with a self-supervised model and reports ASVspoof results. The evidence supports spoofing and deepfake security, bounded by the KAN/XLSR-Conformer method and LA/DF/21LA conditions.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "pierotti25_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts clinician-rated speech impairment in ALS from acoustic and kinematic audio-visual features. The evidence supports clinical speech markers, bounded by the small dataset, speech tasks, regression scale, and bulbar-dysfunction target.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "piyadasa25_interspeech": (
        "confirmed-current-boundary",
        "The abstract morphs vocal-tract shapes under real-time MRI constraints and demonstrates the transformation on a vowel-consonant-vowel sequence. The evidence supports articulatory coordination, bounded by LDDMM, MRI constraints, and the demonstrated sequence.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "polle25_interspeech": (
        "confirmed-current-boundary",
        "The abstract models within-speaker voice changes associated with fatigue over a longitudinal shift-worker dataset and compares speaker-dependent meta-learning methods. The evidence supports within-speaker state variation, bounded by sleep-time prediction, 1,185 speakers, and 10,286 recordings.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation",
    ),
    "popescu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses forced alignment and large French corpora to measure pronounced and deleted /r/ variants and their phonetic and social conditioning. The evidence supports pronunciation variation, bounded by final post-obstruent /r/, 390-plus speakers, and 14,167 tokens.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "portes25_interspeech": (
        "confirmed-current-boundary",
        "The abstract embeds frame-level F0 and energy jointly for downstream prosody use and reports embedding quality on LibriTTS. The evidence supports prosody control, bounded by VQ-VAE embeddings, the F0/energy features, and the stated error evaluation.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "postma25_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates pretrained audio embeddings for Parkinson’s disease classification from speech tasks and reports speaker/gender and atypical-speech failure patterns. The evidence supports clinical speech markers, bounded by NeuroVoz, DDK/listen-and-repeat tasks, and tested embeddings.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "pothula25_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds weakly labeled speech-translation datasets for four low-resource language pairs through bitext mining and compares data quality and quantity. The evidence supports cross-lingual transfer, bounded by the Shrutilipi-derived language pairs and weak-label experiments.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
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
