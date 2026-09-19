#!/usr/bin/env python3
"""Record the fifth abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "1e2e8252ebe4b1e4e4c49d21351b6eeb62cb0dfb": ("reassigned-to-neighbor", "CREMA-D and RAVDESS are emotional speech resources, and the abstract's target is audio-visual emotion recognition. The central object is affective/paralinguistic state, not prosodic meaning in a linguistic message.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "1e5c84848c9d71233080a3cbeb0926cd20dfe8b3": ("reassigned-to-neighbor", "The abstract explicitly studies attribution of synthetic speech to its generating model and tests prompt, vocoder, speaker, and checkpoint effects. This is spoofing and provenance, not within-speaker state variation.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "20b79816bb8e42f80d3cbf001a6f74c09cae8434": ("rejected-out-of-scope", "The abstract describes sketch-to-audio generation for sound design and live jamming, without a speech or spoken-language object.", None, None, None),
    "21fff85b5e9fd31c25b499c14e34a1c9d53cc441": ("confirmed-current-boundary", "The abstract explicitly concerns acoustic and linguistic speech embeddings for cognitive-status classification on DementiaBank-derived recordings. D2 supports a clinical speech-marker assignment without establishing diagnosis validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "221e2ec1853803a6e9d67bb33a3069b5f922db28": ("confirmed-current-boundary", "The abstract explicitly concerns zero-shot keyword spotting, utterance/phoneme alignment, false alarms, and real-time voice-interface use. Open-vocabulary recognition is supported at D2.", "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition"),
    "2230d48501d1a3c823ddbec57210807f437b9a4e": ("rejected-out-of-scope", "The abstract concerns controllable bandwidth extension for historical music recordings, not speech or spoken-language audio.", None, None, None),
    "223a9bfefeff18c4f5d78fa988eda2ce16235b8e": ("confirmed-current-boundary", "The abstract explicitly concerns domain-specific ASR, decoder prompts, named entities, and jargon in spoken basketball commentary. Context and domain biasing is the supported D2 boundary.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "225b0647776efa2a3670145ccafa5995ccceddc1": ("confirmed-current-boundary", "The abstract explicitly concerns ASR domain adaptation and synthetic pronunciation variation through phonetic respelling. It supports pronunciation-variation membership while full robustness remains unreviewed.", "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
