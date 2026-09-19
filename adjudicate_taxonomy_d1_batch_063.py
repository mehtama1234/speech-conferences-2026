#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "cf9fe558334f69f7a2525b3c9ecf786d27565b63": ("confirmed-current-boundary", "The title explicitly concerns speculative decoding for autoregressive speech synthesis. Title-only evidence supports interactive generation latency, without establishing speed or quality tradeoffs.", "voice-generation-and-control", "expression-and-interactive-control", "interactive-latency"),
    "cfb40c957353851cdccc0497f9e6c1696f0f020e": ("confirmed-current-boundary", "The title explicitly concerns speech and non-verbal emotion recognition. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "d02fafa19a3ca6416c1cb66d42bcad99c167ca5e": ("confirmed-current-boundary", "The title explicitly concerns automatic speaker verification and countermeasure tasks in a spoofing challenge. Title-only evidence supports spoofing and deepfake detection, without establishing challenge performance.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "d08a22a2ece219c8cf61d0372c8d895f8dc1f648": ("confirmed-current-boundary", "The title explicitly concerns speech-quality prediction across domains and datasets. Title-only evidence supports quality and naturalness, without establishing generalization.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "d0c53dfab969742a85df4ddbfec08e147ffed239": ("confirmed-current-boundary", "The title explicitly concerns streaming speech-to-text with chunk-wise attention. Title-only evidence supports long-context decoding, without establishing streaming accuracy or latency.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "d1020efad23da47c04e3dca1696fc0cb95601bda": ("confirmed-current-boundary", "The title explicitly concerns real-time on-phone text-to-speech. Title-only evidence supports interactive generation latency, without establishing real-time quality or resource use.", "voice-generation-and-control", "expression-and-interactive-control", "interactive-latency"),
    "d1189ffafd42775c9453b9141866dfd65ea76c3e": ("reassigned-to-neighbor", "The title explicitly concerns a variable-frame-rate neural speech codec and device-oriented segmentation. Title-only evidence places it under latency and resource budget rather than interactive generation latency.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "d15fea3c805289fc1d6e0dbfb634ea3f83f570b9": ("rejected-out-of-scope", "The title concerns general audio understanding and caption training but does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
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
