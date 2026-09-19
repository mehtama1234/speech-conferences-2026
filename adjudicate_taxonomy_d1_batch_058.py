#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "b3691734002256b1c4ca5e6efbf0af4eece19c83": ("confirmed-current-boundary", "The title explicitly concerns speech-to-speech translation in language models. Title-only evidence supports cross-lingual transfer, without establishing translation quality or language coverage.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "b4222770f45136895f3504be166ed1165a2a9e7e": ("rejected-out-of-scope", "The title concerns exterior sound-field estimation and does not establish a human-speech or spoken-language task. With title-only evidence, microphone and channel coloration for speech is not supported.", None, None, None),
    "b61c2e96738de828504e0268c63d4741f8d32c98": ("rejected-out-of-scope", "The title concerns emotion encoding from eye-movement reconstruction and does not establish a human-speech or spoken-language task. With title-only evidence, paralinguistic state membership is not supported.", None, None, None),
    "b66fd8a567973dfb4b60733b52f3e18f0ad93a83": ("reassigned-to-neighbor", "The title explicitly concerns a Portuguese speech dataset collected from podcasts. Title-only evidence places it under speech data collection rather than pronunciation variation.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "b6b6bce799b302f90e5f159fc79178ed595bbfeb": ("confirmed-current-boundary", "The title explicitly concerns speech deepfake detection at frame level. Title-only evidence supports spoofing and deepfake detection, without establishing detection reliability.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "b744bdb980fe28a3c8a996f09601bd8a7e34132f": ("confirmed-current-boundary", "The title explicitly concerns style-prompt adherence for prompt-based text-to-speech. Title-only evidence supports style and emotion control, without establishing the metric's validity.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "b7efe85da9a2014f7cf2bb510dcaf5e730327609": ("confirmed-current-boundary", "The title explicitly concerns human perception of AI-dubbed content, which is a spoken-content evaluation question. Title-only evidence supports intent in context, without establishing the perceptual findings.", "meaning-and-interaction", "intent-and-dialogue-state", "intent-in-context"),
    "b82356b06dc19d6aa274d96650079b9c5028e6d9": ("confirmed-current-boundary", "The title explicitly concerns an ultra-low-bitrate neural speech codec. Title-only evidence supports quality and naturalness, without establishing the codec's perceptual quality.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
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
