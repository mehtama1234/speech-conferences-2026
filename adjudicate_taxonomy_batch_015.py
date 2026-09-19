#!/usr/bin/env python3
"""Record the fifteenth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "peng25b_interspeech": ("confirmed-current-boundary", "FD-Bench makes interruption, backchannel, and simultaneous listening part of full-duplex turn behavior. Its generated conversations and proxy metrics limit claims about real users.", "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "phukon25_interspeech": ("confirmed-current-boundary", "The metric learns from human judgments of disordered-speech transcript intelligibility rather than treating every word difference equally. One dataset and six annotators bound the understanding claim.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "puhach25_interspeech": ("confirmed-current-boundary", "The study makes speaker-assignment choices in a speech model inspectable and counts gender alignment and inclinations under controlled prompts. It is interactional accountability, not a general fairness guarantee.", "meaning-and-interaction", "grounding-and-action", "interactional-feedback"),
    "rong25_interspeech": ("confirmed-current-boundary", "TS-URGENet first fills missing waveform evidence and then handles noise, reverberation, bandwidth, codec, and remaining loss. Packet-loss concealment is the central reconstruction problem.", "listening-and-separation", "echo-reconstruction", "packet-loss-concealment"),
    "roychowdhury25_interspeech": ("confirmed-current-boundary", "The study tests whether TTS preserves the exact structure of mathematical expressions through trained-listener transcription and ratings. Intelligibility and naturalness are separate targets, bounded by the expressions and listeners.", "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness"),
    "tian25_interspeech": ("rejected-out-of-scope", "The captured paper studies general automated audio captioning and audio tokenizers on Clotho; it does not establish a speech or spoken-language object for this speech taxonomy.", None, None, None),
    "wen25b_interspeech": ("confirmed-current-boundary", "Individualized enhancement uses a particular hearing-impaired listener's constraints as the target instead of optimizing only an average waveform score. Listener profiles and fitting protocol bound the accessibility claim.", "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "yan25c_interspeech": ("confirmed-current-boundary", "CS-FLEURS controls language pairs and switching conditions and tests synthetic training for code-switched recognition. Controlled read speech and synthetic voices limit natural-conversation generalization.", "languages-accents-and-resources", "crosslingual-structure", "code-switching"),
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
