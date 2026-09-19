#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "choi25e_interspeech": ("rejected-out-of-scope", "The title explicitly concerns singing voice conversion rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "choi25g_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns conversion between spoken and written text using language models. Title-only evidence places it under alignment rather than long-context decoding.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "choi25h_interspeech": ("confirmed-current-boundary", "The title explicitly concerns acoustic feature extraction tools for clinical speech analysis. Title-only evidence supports clinical speech marker membership, without establishing clinical validity or tool reliability.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "chou25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns zero-shot emotional voice conversion. Title-only evidence supports unseen-speaker synthesis, without establishing conversion quality or emotional control.", "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice"),
    "chowdhury25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns reliability of features from open-source speech analysis tools. Title-only evidence places it under auditability and contestability rather than user control and consent.", "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability"),
    "christodoulidou25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns transcription and segmentation of child speech. Title-only evidence places it under age and developmental speech rather than temporal alignment.", "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "chuang25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns tonal variation and word meaning in Taiwanese. Title-only evidence supports cultural meaning, without establishing the linguistic interpretation or community coverage.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "cultural-meaning"),
    "chung25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns generative restoration of speech using acoustic context. Title-only evidence supports perceptual enhancement, without establishing restoration quality.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
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
