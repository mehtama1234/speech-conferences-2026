#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "da02d9998c528c02e8189fc418f45beee9e5c4c1": ("reassigned-to-neighbor", "The title explicitly concerns consistency regularization in dual-mode automatic speech recognition. Title-only evidence places it under alignment rather than long-context decoding.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "da499a36c67d0c484ce0a7f0962c0cd176290208": ("confirmed-current-boundary", "The title explicitly concerns voice cloning and talking-head generation from text. Title-only evidence supports voice conversion, without establishing cloning quality or identity preservation.", "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "da98ee6a79aa7c87332bbbc13dd6c1bef89f1108": ("confirmed-current-boundary", "The title explicitly concerns open-vocabulary keyword spotting. Title-only evidence supports open-vocabulary recognition, without establishing coverage or false-alarm behavior.", "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition"),
    "dab4d746066207fd1627bdaf5be41ce61e0c8468": ("confirmed-current-boundary", "The title explicitly concerns audio-based depression detection. Title-only evidence supports clinical speech marker membership, without establishing clinical validity or diagnostic utility.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "db0ff89b489a91f54d0e90b6f7acf961bfa058c5": ("confirmed-current-boundary", "The title explicitly concerns data selection for pretraining self-supervised speech models. Title-only evidence supports speech data collection, without establishing data quality or downstream benefit.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "db2b51133ec78012205df0c3608342ac3d759bc3": ("confirmed-current-boundary", "The title explicitly concerns residual tokens for speech modeling. Title-only evidence supports learned speech units, without establishing token quality or modeling benefit.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "db86008dd7082db94dd33b4c11524e5c159d24d2": ("rejected-out-of-scope", "The title concerns active noise control and does not establish a human-speech or spoken-language task. With title-only evidence, microphone and channel coloration for speech is not supported.", None, None, None),
    "dc1810f9d50caae5b640504cc9fb0f8b04ec65f4": ("confirmed-current-boundary", "The title explicitly concerns few-shot keyword spotting. Title-only evidence supports open-vocabulary recognition, without establishing few-shot generalization or false-alarm behavior.", "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition"),
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
