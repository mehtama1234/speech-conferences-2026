#!/usr/bin/env python3
"""Record the thirteenth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ho25_interspeech": ("confirmed-current-boundary", "Streaming inverse text normalization must use context available at each point in the utterance while respecting latency. The Vietnamese benchmark bounds the long-context decoding claim.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "hoffner25_interspeech": ("confirmed-current-boundary", "The study compares ASR and human error thresholds on anechoic and spatial speech-in-noise conditions. It makes model fit to real hearing conditions inspectable, while laboratory languages and noises bound the result.", "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
    "hope25_interspeech": ("reassigned-to-neighbor", "The study asks nonbinary speech-generating-device users what control over breathiness, tension, vocal-tract length, and voice blending would support self-expression. The central issue is user control and consent around generated identity, not a generic speaker embedding.", "people-variation-and-health", "human-centered-accessibility", "user-control-and-consent"),
    "huang25k_interspeech": ("confirmed-current-boundary", "The challenge system adapts diarization to overlap and adds ASR-aware observations before recognition. Its main problem is separating and assigning concurrent sources from mixed meeting audio.", "listening-and-separation", "source-separation", "blind-source-separation"),
    "inoue25b_interspeech": ("confirmed-current-boundary", "EEG and EMG decoding supports communication without vocalization across heterogeneous electrode layouts. The patient count and calibration limits prevent treating the reported accuracy as clinical deployment evidence.", "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication"),
    "itani25_interspeech": ("confirmed-current-boundary", "Human preference supplies a target-selection signal for neural extraction from mixtures. The paper directly concerns which source to preserve, bounded by its feedback population and mixtures.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "jeon25_interspeech": ("confirmed-current-boundary", "Knowledge anchoring and curriculum learning personalize TTS for dysarthric speakers from scarce recordings while testing identity and intelligibility. The groups and metrics bound the assistive claim.", "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice"),
    "kamper25_interspeech": ("confirmed-current-boundary", "LinearVC studies how transformations of self-supervised features can change speaker realization while retaining linguistic content. Feature choice and target-data conditions bound voice-conversion transfer.", "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract", "method", "experiments", "results", "limits"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
