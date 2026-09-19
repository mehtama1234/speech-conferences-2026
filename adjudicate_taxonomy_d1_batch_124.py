#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "le25b_interspeech": ("reassigned-to-neighbor", "The abstract restores speech across several transmission failures, including packet loss and missing spectral regions, as well as separation and declipping. Packet-loss concealment is the clearest governing boundary rather than ordinary noise-only denoising.", ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "packet-loss-concealment"),
    "lechler25_interspeech": ("reassigned-to-neighbor", "The abstract compares expert and crowdsourced MUSHRA judgments and objective measures of generative speech quality. The central issue is whether metrics track human quality and naturalness targets, not listener effort as a user burden.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "lee25_interspeech": ("confirmed-current-boundary", "The abstract recognizes emotion from speech, facial expression, and text and analyzes each modality's contribution to the prediction. The evidence supports paralinguistic state, bounded by the IEMOCAP and CMU-MOSEI evaluations.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "lee25b_interspeech": ("rejected-out-of-scope", "The abstract segments visual regions corresponding to sound sources but does not establish a human-speech or spoken-language object. Audiovisual sound-source localization alone is not sufficient for this speech taxonomy.", ["title", "abstract"], None, None, None),
    "lee25c_interspeech": ("confirmed-current-boundary", "The abstract predicts phrase-break annotations for text-to-speech across languages and treats phrase structure as the prosodic target. The evidence supports prosodic meaning, bounded by the synthetic labels and languages tested.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "lee25d_interspeech": ("confirmed-current-boundary", "The abstract predicts articulatory features from surface EMG during speech production and decodes them into speech waveforms. The evidence supports non-airborne speech sensing, bounded by surface-EMG placement and the reported reconstruction results.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "lee25e_interspeech": ("confirmed-current-boundary", "The abstract proposes an interpretable voice embedding for speaker-identity similarity evaluation and relates its dimensions to explicit voice attributes. The evidence supports speaker identity representation, without making the vector a complete account of identity.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "speaker-identity"),
    "lee25f_interspeech": ("confirmed-current-boundary", "The abstract edits internal TTS activations after training to change prosody and correct pronunciation while preserving synthesis quality. The evidence supports prosody control, bounded by the tested TTS models and correction cases.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
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
