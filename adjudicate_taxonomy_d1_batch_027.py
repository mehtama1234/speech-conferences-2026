#!/usr/bin/env python3
"""Record the sixteenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "5eff851615b5df3fc5356ef7ae01fde3559875c1": ("confirmed-current-boundary", "The title explicitly concerns lightweight speech enhancement. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "5f993544b3607f0c819297f710985bf7bf671b93": ("confirmed-current-boundary", "The title explicitly concerns voice conversion intended to preserve mental-health information. Title-only evidence supports voice privacy, without establishing a privacy guarantee.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "6075575aabc2e17bfa07b4309de4ab59129d75e1": ("rejected-out-of-scope", "The title concerns singing-voice deepfake detection rather than ordinary human speech or spoken-language evidence. With title-only evidence, speech spoofing membership is not supported.", None, None, None),
    "6085dee4e4708f1869166388e4bc6ff3867f0f15": ("confirmed-current-boundary", "The title explicitly concerns monaural speech enhancement. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "60d255bd00b63837339b03c74ab44e4a7691653f": ("confirmed-current-boundary", "The title explicitly concerns speaker-image separation. Title-only evidence supports target-conditioned separation, without claims about visual identity reliability.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "61aba23dd5c58f25ac58fefaf21e5f3962325023": ("confirmed-current-boundary", "The title explicitly concerns Parkinson's detection from voice and age-balanced validation. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "634b8acf944b6589aef0d3b31aa98ab8971db47f": ("confirmed-current-boundary", "The title explicitly concerns joint speech-text topic modeling. Title-only evidence supports speech-language semantic grounding, without establishing reference resolution.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "6378654996a8453cc9a436ccad7f2f20821f1a93": ("confirmed-current-boundary", "The title explicitly concerns open-set speaker identification. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
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
