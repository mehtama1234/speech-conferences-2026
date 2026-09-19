#!/usr/bin/env python3
"""Record the eleventh title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "3def9cb8f015c81f6a44378551a1c94613376f9c": ("rejected-out-of-scope", "The title names an X-to-audio alignment challenge but does not establish human speech or spoken-language evidence. With title-only evidence, speech membership is not supported.", None, None, None),
    "3f75d05059d3992131f35fa8a0d391c7c573230f": ("rejected-out-of-scope", "The title concerns envelope separation, source counting, and localization without identifying speech. With title-only evidence, speech separation membership is not supported.", None, None, None),
    "3faeca88c30da020507ec08f801840828383262b": ("confirmed-current-boundary", "The title explicitly concerns audio-visual speaker diarization. Title-only evidence supports blind/source separation rather than temporal alignment.", "listening-and-separation", "source-separation", "blind-source-separation"),
    "40aa5944f6fb2455caef5a6948c337d6baa6d047": ("rejected-out-of-scope", "The title concerns continuous sign-language recognition and does not establish spoken speech or a speech signal. With title-only evidence, augmentative speech membership is not supported.", None, None, None),
    "419a8abb2e1337a1d7c1d4d9fc5b6d4fdf69a552": ("confirmed-current-boundary", "The title explicitly concerns speaker verification. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "4289ae6a4f5682e99b56efafe94b7f5ad8166784": ("rejected-out-of-scope", "The title concerns continuous reconstruction of room impulse responses and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech membership is not supported.", None, None, None),
    "436671e5ff05430b992bb3066e32dbbbc037d2fb": ("reassigned-to-neighbor", "The title explicitly concerns stress detection in L2 spoken English using speech recognition adaptation. Stress is a prosodic property; title-only evidence supports prosodic meaning more directly than accent robustness.", "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "439e5824d51567971972cda0d403e35dc2cb32e8": ("confirmed-current-boundary", "The title explicitly concerns detection of partially spoofed speech. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
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
