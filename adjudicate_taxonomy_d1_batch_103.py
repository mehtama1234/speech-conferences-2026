#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "havard25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly compare monolingual, multilingual, and French-based self-supervised models for Haitian Creole ASR and discuss transfer to related Creoles. The evidence supports cross-lingual transfer, without proving broad transfer.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "havras25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly analyze filled pauses as recurring speech events with acoustic and contextual variation. This belongs under disfluency and event preservation, not multiple time scales alone.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation"),
    "he25b_interspeech": ("rejected-out-of-scope", "The title and abstract concern text-to-multisource binaural general-audio generation and do not establish a human-speech or spoken-language object. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
    "he25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly recognize emotion from speech, text, and visual modalities and model shared affective information. The evidence supports paralinguistic state, without proving emotion inference across contexts.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "hegde25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study in-context learning for task-oriented dialogue-state tracking and how retrieved demonstrations change performance. The evidence supports dialogue state, without proving spoken-audio grounding.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "heo25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly predict turn taking in triadic conversations using gaze and speaker localization, with hearing assistance as an application. The evidence supports turn-boundary prediction, without proving all conversational cultures.", ["title", "abstract"], "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "hermes25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly compare acoustic and articulatory production in speakers with congenital lip paralysis and show compensatory tongue movement. The evidence supports articulatory coordination, without generalizing from the small cohort.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "hidalgojulia25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly associate vocal and linguistic features with depression severity across repeated remote recordings. The evidence supports a clinical speech marker, without establishing diagnosis or clinical decision validity.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
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
