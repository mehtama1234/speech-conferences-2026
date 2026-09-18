#!/usr/bin/env python3
"""Record the eighth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "chen25b_interspeech": ("reassigned-to-neighbor", "The paper optimizes TTS naturalness and intelligibility with human-feedback rewards; it does not change a requested style or emotion. Its proper boundary is waveform generation quality.", "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness"),
    "chen25j_interspeech": ("confirmed-current-boundary", "Codec taxonomy is used to trace fake speech back toward generator families rather than only detect that it is fake. The dataset and 46.45% F1 bound any attribution claim.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "cho25b_interspeech": ("confirmed-current-boundary", "DiEmo-TTS transfers emotion while preserving speaker-related properties through disentangled representations. Emotion categories and subjective measures limit the result, but the control target is correctly placed here.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "choi25f_interspeech": ("rejected-out-of-scope", "The captured paper is general audio captioning and retrieval on AudioCaps, Clotho, and Auto-ACD; it does not establish a speech or spoken-language object for this speech taxonomy.", None, None, None),
    "cohen25_interspeech": ("confirmed-current-boundary", "Speech inpainting has multiple plausible completions, and the paper represents uncertainty through principal directions whose alternatives can change words and pitch. The benchmark does not establish calibration for user decisions.", "listening-and-separation", "echo-reconstruction", "packet-loss-concealment"),
    "combei25_interspeech": ("confirmed-current-boundary", "The study treats real-world deepfake data coverage as a distribution-shift problem and tests data-centric filtering and augmentation. EER on the selected datasets is not a safety guarantee.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "cordlandwehr25_interspeech": ("confirmed-current-boundary", "TDOA supplies spatial timing while speaker embeddings cluster identities in overlapping meetings. The central evidence is spatial filtering and diarization under microphone-layout limits.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "dai25b_interspeech": ("reassigned-to-neighbor", "The paper uses relative language, gender, emotion, pitch, timing, and distance cues to select a requested speaker from a mixture. Its central operation is target-conditioned extraction, not variation within one speaker.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
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
