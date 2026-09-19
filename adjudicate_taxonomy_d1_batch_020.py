#!/usr/bin/env python3
"""Record the ninth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "30a6b7b3036cf9c279f9b26bd5d535cd7e9a81b0": ("confirmed-current-boundary", "The title explicitly concerns generated spoken dialogues for dialogue-related speech tasks. Title-only evidence supports dialogue-state membership, without claims about conversational quality.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "30e8a66494d1e1e7ec936ccaec2906c2bfa51e3f": ("rejected-out-of-scope", "The title concerns sound-source localization using harmonic coefficients but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "31aee47fb91b8bcf6aebae528929c8a26e3328ba": ("confirmed-current-boundary", "The title explicitly concerns voice activity detection in dysarthric speech. Title-only evidence supports atypical-articulation and dysarthria membership.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "332f8f234226d44e2586064d5d69b6ec5d1eff15": ("confirmed-current-boundary", "The title explicitly concerns robust code-switching automatic speech recognition. Title-only evidence supports code-switching membership.", "languages-accents-and-resources", "crosslingual-structure", "code-switching"),
    "34951200bd03611f5ca5bf0309779af8cac29f97": ("confirmed-current-boundary", "The title explicitly concerns detection of audio deepfakes. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "352089123e1bd0373c317ff162afe29946d15b9d": ("reassigned-to-neighbor", "The title explicitly concerns authentication of speech recordings using recognition and watermarking. The central boundary is spoofing and provenance rather than voice privacy alone.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "36c5490ee2bb16eef209794008ae6bcae92a5c63": ("confirmed-current-boundary", "The title explicitly concerns synthetic speech detection. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "3898b7b791d23bf67dce2b08732f8e90d62a99f5": ("confirmed-current-boundary", "The title explicitly concerns speech intelligibility decoding and its listener-level consequence. Title-only evidence supports listener effort, without establishing a clinical or cognitive claim.", "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
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
