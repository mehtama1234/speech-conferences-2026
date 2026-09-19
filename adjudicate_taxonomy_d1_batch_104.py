#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "higuchi25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly use an LLM to guide speech-to-text translation across speech recognition and translation stages. The governing pressure is cross-lingual transfer, not long-context decoding alone.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "hilmes25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly study CTC blank handling in ASR knowledge distillation and its effect on unlabeled-audio training. This is acoustic-to-token mapping, not a claim about learned speech units themselves.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "hirano25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly condition overlapped-speech recognition on speaker embeddings and activity to suppress non-target talkers. This is target-conditioned separation, not speaker identity representation alone.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "hiruta25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly select diverse and uncertain speech examples to reduce annotation cost and improve ASR training. The evidence supports speech data collection and curation, without proving a universal sampling rule.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "ho25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly transcribe laughter and speech-laugh as conversational non-lexical events instead of discarding them from ASR. This belongs under disfluency and event preservation, not repair and clarification.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation"),
    "hojo25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly adapt Japanese ASR for individuals with organic speech disorders using limited patient speech and synthetic data. The evidence supports atypical speech recognition, without proving broad clinical transfer.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "holler25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly study how gesture, face, and head movement identify and enrich meaning in face-to-face conversation and affect comprehension. This is referential grounding in a shared scene, not feedback from a user's correction.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "hopponen25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly provide Finnish and Russian L1, L2, and imitated-accent speech data and analyze language and accent variation. The evidence supports dialect and variety, without proving speaker-verification robustness.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
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
