#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "escobargrisales25_interspeech": ("reassigned-to-neighbor", "The title and abstract jointly analyze acoustic and linguistic patterns in Parkinson's speech to model motor and cognitive symptoms. This is a clinical speech marker problem, not separation of sound sources.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "espywilson25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly recover articulator movements from acoustic speech and relate them to speech production. The evidence supports articulatory coordination, without establishing clinical validity.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "falez25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly trace audio-deepfake sources in open-set identification and verification protocols. The evidence supports spoofing and synthetic-voice misuse, without proving reliable attribution in deployment.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "fan25_interspeech": ("rejected-out-of-scope", "The title and abstract concern infant-centered general audio tagging and family recordings, without establishing a human-speech or spoken-language task. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
    "fan25b_interspeech": ("reassigned-to-neighbor", "The title and abstract study creaky phonation as a voice cue in Mandarin tone processing. The relevant speech object is the periodic vocal source, not articulatory coordination.", ["title", "abstract"], "sound-and-production", "source-generation", "periodic-source"),
    "fang25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly perform multimodal speech emotion recognition and model emotional expression. This is paralinguistic state, not dialogue state.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "fang25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly personalize speech emotion recognition to listener-specific interpretations of emotion. The evidence supports paralinguistic state, without making listener labels universal.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "fang25d_interspeech": ("rejected-out-of-scope", "The title and abstract concern few-shot class-incremental general audio classification and do not establish a human-speech or spoken-language task. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
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
