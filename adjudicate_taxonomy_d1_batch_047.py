#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "5f68aa1240bf0a8a28b8a81c59253d454244b7ee": ("confirmed-current-boundary", "The title explicitly concerns fine-tuning self-supervised models for low-resource speech recognition. Title-only evidence supports learned speech units, without establishing the quality or language coverage of those units.", "recognition-and-alignment", "acoustic-unit-learning", "learned-speech-units"),
    "6039bd6c9fb2e47714a644ef5b93caba242b38e2": ("rejected-out-of-scope", "The title concerns incremental learning for general audio classification and does not establish a human-speech or spoken-language task. With title-only evidence, changing and adverse noise membership is not supported.", None, None, None),
    "60546056096e26a47faf0342cb79c2d92013ac68": ("rejected-out-of-scope", "The title concerns acoustic magnitude-field reconstruction and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech-room membership is not supported.", None, None, None),
    "6071d47e9f399bfb7e23f1124baea01d1f61bac9": ("confirmed-current-boundary", "The title explicitly concerns dialectal automatic speech recognition for Arabic. Title-only evidence supports dialect and variety membership, without establishing coverage or robustness across dialects.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "616a1e4bc31e23239e591fd67c8c4375cdea9512": ("confirmed-current-boundary", "The title explicitly concerns contextual biasing for automatic speech recognition. Title-only evidence supports domain and context biasing, without establishing recognition gains in deployment.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "638ce57a537edd24f9f63577bb4cd9bc2deada58": ("rejected-out-of-scope", "The title concerns concept retrieval and description for general AudioLLMs but does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
    "63b0b73e17e45ae28aa513666b91238c373a7544": ("confirmed-current-boundary", "The title explicitly concerns adaptive speaker embeddings, enrollment speech, and personal voice activity detection. Title-only evidence supports speaker identity representation, without establishing identity-recognition accuracy.", "voice-generation-and-control", "identity-and-conversion", "speaker-identity-representation"),
    "64fba9c44a881e6a3ddfd9a8f41ea3b2a286fa42": ("rejected-out-of-scope", "The title concerns spatial room-impulse-response computation and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech-room membership is not supported.", None, None, None),
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
