#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ecdfa2f086c876480a52026dbb07c1f727c624dc": ("rejected-out-of-scope", "The title concerns an auditory-illusion benchmark for general audio language models and does not establish a human-speech or spoken-language task. With title-only evidence, listener effort membership is not supported.", None, None, None),
    "ed51d396663ea46f8289c81017b2691320dca106": ("rejected-out-of-scope", "The title concerns stereophonic acoustic echo cancellation and does not establish a human-speech or spoken-language task. With title-only evidence, speech echo-cancellation membership is not supported.", None, None, None),
    "edf62145e97da07b3228b410df780646b08c96c4": ("confirmed-current-boundary", "The title explicitly concerns terminology probability estimation for a robust speech-to-text system. Title-only evidence supports domain and context biasing, without establishing recognition gains.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "ee23390bce550a66ac8f70c20b65b3d9884e88f5": ("confirmed-current-boundary", "The title explicitly concerns perceptual and algorithmic assessment of vocal charisma in text-to-speech. Title-only evidence supports style and emotion control, without establishing perceptual validity.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "ee679d36127c0e3f08eed4428f8171f4324d1b94": ("confirmed-current-boundary", "The title explicitly concerns multi-dialectal Arabic speech representation learning. Title-only evidence supports dialect and variety, without establishing dialect coverage or transfer quality.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "eeb002d55758577c6fea97304ea9d8db8d3e0b55": ("confirmed-current-boundary", "The title explicitly concerns end-to-end automatic speech recognition and a generative reconstruction pathway. Title-only evidence supports acoustic-to-token mapping, without establishing recognition gains.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "eeeda17592489a89d4293eeb05c692378ee9a7a2": ("confirmed-current-boundary", "The title explicitly concerns visually driven speech synthesis with scene awareness. Title-only evidence supports text-to-speech planning, without establishing scene grounding or synthesis quality.", "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "ef4601c8283d6358d9c810cf7659922019326458": ("confirmed-current-boundary", "The title explicitly concerns post-recognition correction for disordered speech. Title-only evidence supports atypical articulation and dysarthria, without establishing clinical or user benefit.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
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
