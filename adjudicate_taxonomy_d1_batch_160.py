#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "rastogi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract decodes imagined speech from non-invasive EEG for people with speech or motor impairments and demonstrates sentence-level generation. The evidence supports non-airborne sensing, bounded by EEG, the Spanish dataset, mixed-subject evaluation, and the reported accuracy.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
    ),
    "ratajczak25_interspeech": (
        "confirmed-current-boundary",
        "The abstract replaces quadratic attention with recurrent attention for short- and long-form ASR and measures throughput/accuracy tradeoffs. The evidence supports long-context decoding, bounded by limited-context baselines, direction dropout, and the reported throughput results.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding",
    ),
    "raut25_interspeech": (
        "confirmed-current-boundary",
        "The abstract classifies micro-behaviors attached to turns in team conversations using transcript-based language models. The evidence supports dialogue state, bounded by simulated space-mission transcripts, underrepresented behavior classes, and the reported F1 results.",
        ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state",
    ),
    "rautenberg25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract controls localized creaky voice in TTS through a speaker-attribute manipulation block and evaluates the generated probe speech. The governing boundary is prosody control, not within-speaker variation, because the paper's intervention is controllable speech generation.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "ravenscroft25_interspeech": (
        "confirmed-current-boundary",
        "The abstract filters in-the-wild speech corpora for speakers, languages, music, and other undesired samples and releases annotations for corpus subsets. The evidence supports speech-data collection, bounded by Whilter’s five classifiers, annotated corpora, and reported filtering performance.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "ravi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates calibrated ASR confidence with a continuous lexical-similarity target that reflects the degree of transcription error. The evidence supports calibration and selective use, bounded by TruCLeS, CTC/RNN-T experiments, and comparison to supervised confidence methods.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use",
    ),
    "reinders25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures voice changes before and after exercise in people with COPD and relates features to disease severity, while explicitly calling for larger confirmation studies. The evidence supports clinical speech markers, bounded by the vowel/reading tasks, sex adjustment, and exploratory sample.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "ren25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract performs high-fidelity speech conversion with rectified flow, optimizes speaker features using content and pitch, and reports small-data and zero-shot results. The evidence supports zero-shot voice, bounded by ReFlow-VC, the speaker-feature design, and the stated conversion scenarios.",
        ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice",
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
