#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "a964b07db3f902cd4429c55981417bc044461dd6": ("reassigned-to-neighbor", "The title explicitly concerns diarization-conditioned automatic speech recognition. Title-only evidence places it under speaker adaptation rather than target-conditioned source separation.", "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
    "aa3482b669f412fca13087a86194d3d69d3f4725": ("confirmed-current-boundary", "The title explicitly concerns unsupervised speech-emotion recognition. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "ad02a616209b6653bd313f958b0921ea8b92dd0a": ("rejected-out-of-scope", "The title concerns neural audio coding but does not establish a human-speech or spoken-language task. With title-only evidence, waveform synthesis membership for speech is not supported.", None, None, None),
    "ad4f1b53ae96523ae3b08378f537139cd471d127": ("reassigned-to-neighbor", "The title explicitly concerns speech-emotion recognition with audio-language models. Title-only evidence places it under paralinguistic state rather than accessibility fit.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "aea106410b217fd7f2344ce26a3650c8c94d14a8": ("rejected-out-of-scope", "The title explicitly concerns sound-effect compression rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "afaf6879042a57d87c6d28bd0563165e62eb83bc": ("reassigned-to-neighbor", "The title explicitly concerns voice and role control in full-duplex conversational speech models. Title-only evidence places it under style and emotion control rather than interactive generation latency.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "b301ede7dc6fe1c050314ed5bfe5a460259304c3": ("confirmed-current-boundary", "The title explicitly concerns vocal-tract area and radiation modeling. Title-only evidence supports vocal-tract filtering, without establishing the physics model's accuracy.", "sound-and-production", "source-generation", "vocal-tract-filter"),
    "b32bfec9debaa6dd37f7c09b3df017e3c3fbe365": ("confirmed-current-boundary", "The title explicitly concerns phonetic analysis of speech reproduction in modern speech generators. Title-only evidence supports intelligibility versus naturalness, without establishing the generators' quality ranking.", "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
