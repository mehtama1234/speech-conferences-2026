#!/usr/bin/env python3
"""Record the nineteenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "70b0b370785d331d9c422baf0710ee17d4085747": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition with signal-noise separation. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "728e0b7eb54095f05540b88dc87ff2a5bbe69bb5": ("confirmed-current-boundary", "The title explicitly concerns EEG-based silent-speech decoding. Title-only evidence supports non-airborne speech sensing, without claims about neural decoding quality or communication benefit.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "72ba7ce0f45de6486710d5da65930e47dedc1177": ("confirmed-current-boundary", "The title explicitly concerns prediction of sleep-apnea endotypes from voice biomarkers. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "739a94579900ab649d013b8ab63418cb181ef2c8": ("rejected-out-of-scope", "The title concerns speech-driven holistic motion generation; the generated object is motion rather than speech. With title-only evidence, prosody-control membership is not supported.", None, None, None),
    "73d69ca576dc8e65e0f4826f6f6c3db3d0e8a2f2": ("confirmed-current-boundary", "The title explicitly names a Japanese dysarthric speech corpus. Title-only evidence supports speech data collection.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "76027423d418665db7a133787c6b817143a9112f": ("confirmed-current-boundary", "The title explicitly concerns text-to-speech generation, spoofing, and spoofing-aware speaker verification. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "76563a65a7a290db0475ee3ed91838d452df688c": ("confirmed-current-boundary", "The title explicitly concerns text-to-speech for low-resource languages using online preference optimization. Title-only evidence supports few-shot adaptation.", "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "765834ec04759b64d6b3d3f74a522133f63eef3b": ("confirmed-current-boundary", "The title explicitly concerns speech intelligibility in open-ear headphones. Title-only evidence supports listener effort, without establishing hearing-aid or clinical benefit.", "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
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
