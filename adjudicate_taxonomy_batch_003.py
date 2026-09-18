#!/usr/bin/env python3
"""Record the third small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "alizadeh25_interspeech": ("confirmed-current-boundary", "ReSepNet makes the unknown number of simultaneous speakers part of recursive separation: it extracts one source, tests whether another remains, and repeats. Synthetic mixtures and bounded counts limit the claim.", "listening-and-separation", "source-separation", "blind-source-separation"),
    "alradhi25_interspeech": ("reassigned-to-neighbor", "The paper reconstructs speech from intracranial neural recordings for people who cannot produce speech normally. Its central problem is assistive communication, not improving an acoustic signal already heard by a listener.", "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication"),
    "alumae25_interspeech": ("confirmed-current-boundary", "The challenge system joins language identification with multilingual recognition and evaluates routing and recognition performance. The language mix and challenge conditions bound the result.", "languages-accents-and-resources", "crosslingual-structure", "language-identification"),
    "ambikairajah25_interspeech": ("confirmed-current-boundary", "The study compares speech-embedding similarities involving Australian Aboriginal and high-resource languages. Similarity is treated as a bounded clue about shared structure, not as proof of transfer or language identity.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "amoniyan25_interspeech": ("confirmed-current-boundary", "The measured /s/ differences across Nigerian English groups concern dialect and variety variation; the corpus and phoneme-specific analysis do not establish social identity from acoustics.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "arai25_interspeech": ("confirmed-current-boundary", "The static and dynamic vocal-tract models make geometry and articulation visible as causes of sound. The demonstration does not claim human-speech equivalence or a shared benchmark.", "sound-and-production", "source-generation", "vocal-tract-filter"),
    "ariga25_interspeech": ("confirmed-current-boundary", "Controlled Japanese word-recognition experiments test how segmental and lexical pitch-accent cues combine when they disagree. The laboratory materials and language-specific accent system limit generalization.", "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "arora25_interspeech": ("confirmed-current-boundary", "The spoken dialogue system predicts a response using intermediate dialogue-state supervision. The traces are training artifacts and do not prove faithful internal reasoning, but conversational state is the evaluated mechanism.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
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
