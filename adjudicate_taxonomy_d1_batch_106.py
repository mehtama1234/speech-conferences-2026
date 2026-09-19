#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "hsiao25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly study adapting a spoken-language model across ASR, TTS, and spoken question-answering tasks while retaining earlier capabilities. This is model adaptation under scarce or shifting task data, not text-to-speech planning.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "hsieh25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly recognize dysarthric speech and address heterogeneous intelligibility groups with curriculum and multi-stream modeling. The evidence supports atypical speech recognition, without proving clinical benefit.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "hsieh25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly introduce an annotated corpus and baseline for non-native Mandarin pronunciation assessment. The primary contribution is speech data collection, not dialect classification.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "hsu25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly link time-varying acoustic and articulatory changes to syllable progression across languages. This is timed articulatory coordination, not prosodic meaning in interaction.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "hu25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly align audio and transcripts while producing phonemic and prosodic labels for Japanese TTS data. The evidence supports temporal alignment, without proving fully manual-quality annotations.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "hu25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly bridge audio and text representations for multimodal retrieval and test matching across long and complex inputs. The evidence supports referential grounding, without proving semantic understanding of every retrieved item.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "hu25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use emotion-label semantics to learn speech representations and distinguish subtle affective boundaries. The evidence supports paralinguistic state, without proving universal emotion categories.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "hu25d_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly perform zero-shot speaker adaptation of speech foundation models for dysarthric recognition, with routing conditioned on speaker attributes and data quantity. This belongs under speaker adaptation, not atypical speech alone.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
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
