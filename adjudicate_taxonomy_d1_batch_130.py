#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "liang25c_interspeech": ("rejected-out-of-scope", "The title and abstract study Mandarin singing transcription and segmentation, not ordinary spoken speech or spoken-language communication. Singing audio processing is outside this speech taxonomy boundary.", ["title", "abstract"], None, None, None),
    "liang25d_interspeech": ("reassigned-to-neighbor", "The abstract generates speech from visual lip information and emphasizes the missing acoustic channel and edge deployment. The closest boundary is alternate sensing of speech production, not augmentative communication, since no impaired-user communication setting is established.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "liang25e_interspeech": ("reassigned-to-neighbor", "The abstract unifies speech synthesis, editing, and continuation and evaluates acoustic quality and voice preservation without making text planning the central object. The closer boundary is waveform synthesis.", ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "lim25_interspeech": ("reassigned-to-neighbor", "The abstract's governing problem is making keyword spotting accurate on low-power edge devices and reports a large energy reduction. The deployment cost boundary is more direct than open-vocabulary recognition, which normally concerns words outside a fixed list.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "lin25_interspeech": ("confirmed-current-boundary", "The abstract detects a pre-enrolled speaker under domain mismatch and reduces false acceptance from similar voices through enrollment updating and hard examples. The evidence supports speaker adaptation, bounded by personal VAD and the tested domains.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
    "lin25b_interspeech": ("reassigned-to-neighbor", "The abstract uses acoustic echo cancellation to prevent a device's own TTS playback from entering directional ASR and evaluates residual echo effects. The governing operation is cancellation of a known acoustic copy, not target-speaker separation.", ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation"),
    "lin25c_interspeech": ("reassigned-to-neighbor", "The abstract measures and reduces race and age disparities in speech emotion recognition without requiring explicit demographic labels. The central consequence is whether a speech system's evidence and outcomes can be inspected across groups, so auditability and contestability is closer than emotion classification alone.", ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability"),
    "lin25d_interspeech": ("reassigned-to-neighbor", "The abstract defends voice-authentication watermarks against self-vocoding attacks that can enable unauthorized synthetic speech. The governing boundary is resisting synthetic-voice misuse, not general provenance inspection.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": sections, "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
