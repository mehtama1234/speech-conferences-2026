#!/usr/bin/env python3
"""Record the eighteenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "69f839dd5dd7ca282bbe569be8c0517a6d332b03": ("confirmed-current-boundary", "The title explicitly concerns multichannel speech enhancement. Title-only evidence supports time-frequency masking within noise enhancement.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "6a3b096e625acdd8d4873ac9de35c66d316f6428": ("reassigned-to-neighbor", "The title explicitly concerns audio-guided alignment and boundary modeling in active-speaker detection. Title-only evidence supports temporal alignment more directly than conversational turn-boundary prediction.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "6cfea1f4e985754dc1fa8ec28e7482aa89308291": ("reassigned-to-neighbor", "The title explicitly concerns multi-channel, multi-speaker speech recognition and serialized sentence output. Title-only evidence supports context and decoding control more directly than temporal alignment.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "6d9a5ef0787a943874d526028258717d96e51a8e": ("rejected-out-of-scope", "The title concerns co-speech gesture generation; the generated object is gesture rather than speech. With title-only evidence, speech prosody membership is not supported.", None, None, None),
    "6e49385da2225edc2f8ab3a7582dc218f22d015e": ("confirmed-current-boundary", "The title explicitly concerns reducing target-speech extraction errors. Title-only evidence supports target-conditioned separation.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "6f359baa8790aa0da4d0e9b8e87bb0a41f11a174": ("confirmed-current-boundary", "The title explicitly concerns dementia detection from speech. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "6fcfdeee23572542fac5afcaf3ffdd950a65e320": ("confirmed-current-boundary", "The title explicitly concerns verifiable speaker anonymization. Title-only evidence supports voice privacy, without establishing a privacy guarantee.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "6ff5eef157077a5dfee1454e817dba8353c19c4b": ("rejected-out-of-scope", "The title concerns large audio-language models under emotional speaker variation but does not establish a human-speech or spoken-language task. With title-only evidence, speech distribution-shift membership is not supported.", None, None, None),
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
