#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "zhang25p_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects when a selected speaker is active using variable microphone-array channels and masked cross-channel attention, including missing or failed channels. The evidence supports target-conditioned-separation, bounded by SCA-TSVAD, simulated array topologies, Ali-Meeting, speaker diarization, and the reported robustness claims.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "zhang25r_interspeech": (
        "confirmed-current-boundary",
        "The abstract classifies child vocalizations by developmental maturity across children acquiring more than 25 languages, including cry, laughter, mature, and immature speech. The evidence supports age-and-development, bounded by SpeechMaturity, 242,004 labels, self-supervised models, human comparison, and rural/urban robustness.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "zhang25s_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether one Common Voice client identifier actually groups one speaker, using voice embeddings and a discrimination threshold to reduce mixed-speaker records. The evidence supports speech-data-collection, bounded by Common Voice, anonymous client IDs, ResNet embeddings, threshold selection, and phonetic-analysis use.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "zhang25t_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts an LLM-based ASR system across read, meeting, and post-stroke aphasic speech, comparing transfer direction, phoneme input, and instruction fine-tuning. The evidence supports dysarthria-and-atypical-speech, bounded by LibriSpeech, AMI, AphasiaBank, word/phoneme transcription, and cross-domain results.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "zhang25u_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds synthetic dysfluency data with language-model-guided simulation to cover 11 word- and phoneme-level categories, addressing scarce annotated clinical data and unnatural prior synthesis. The evidence supports clinical-speech-marker, bounded by LLM-Dys, dysfluency detection, prosody/context limitations, and reported framework results.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "zhao25_interspeech": (
        "confirmed-current-boundary",
        "The abstract aligns speech and electroglottographic voice offset to measure whether glottal-stop closure is present across generations during sound change. The evidence supports periodic-source, bounded by Shengzhou Wu checked syllables, older/younger speakers, EGG timing, and the reported coda-loss pattern.",
        ["title", "abstract"], "sound-and-production", "source-generation", "periodic-source",
    ),
    "zhao25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract designs a multi-ring, three-dimensional microphone array and a robust superdirective beamformer to steer beyond a planar sensor and control white-noise gain. The evidence supports spatial-filtering, bounded by frustum topology, quadratic-eigenvalue optimization, particle-swarm topology search, simulation, directivity, and noise-gain results.",
        ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering",
    ),
    "zhao25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract performs zero-shot voice conversion with a prosody-aware codec component that changes delivery while retaining speaker timbre. The evidence supports zero-shot-voice, bounded by VALLE-X, PACE, in-context speaker adaptation, prosody/timbre/naturalness measures, and baseline comparisons.",
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


if __name__ == "__main__":
    main()
