#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "jun25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly condition generative speech enhancement on estimated SNR and evaluate perceptual quality across noise levels. The evidence supports speech-prior denoising, without proving every noise condition.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "jung25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly align text and audio embeddings for open-vocabulary keyword spotting without a fixed enrolled phrase list. The evidence supports open-vocabulary recognition, without proving all languages or keywords.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition"),
    "jung25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly introduce an in-the-wild speech dataset for TTS training and assess its quality and deepfake-detection uses. The evidence supports speech data collection, without proving that automated selection removes all bias.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "kakouros25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use word informativeness to select acoustic segments for speech emotion recognition and model fine-grained affective cues. The evidence supports paralinguistic state, without proving all emotional categories.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "kakouros25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly classify winning and losing from prosodic cues linked to emotional states in post-match interviews. This is within-speaker paralinguistic state, not prosodic meaning such as an utterance's intent.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "kalda25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly learn speaker embeddings for multi-speaker diarization and evaluate their identity usefulness and efficiency. The evidence supports speaker verification, without proving identity decisions in every mixture.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "kamo25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly combine diarization and ASR hypotheses through speaker, segment, word, and timing alignment. The governing operation is alignment, not long-context decoding.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "kanamori25_interspeech": ("rejected-out-of-scope", "The title and abstract concern text-to-audio relevance for general synthesized sound categories and do not establish a human-speech or spoken-language object. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
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
