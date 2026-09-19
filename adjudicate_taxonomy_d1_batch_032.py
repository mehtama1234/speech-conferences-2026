#!/usr/bin/env python3
"""Record the twenty-first title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "7cba329305bc054a6ad2565a83a98b963f9883cf": ("confirmed-current-boundary", "The title explicitly concerns Alzheimer's disease detection from disentangled speech features. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "7cc3243cdaee92d6c7d65a21bcc2761ac3e2685f": ("rejected-out-of-scope", "The title concerns urban aircraft noise auralization and perceptual impact, not human speech or spoken-language evidence. With title-only evidence, listener-effort membership is not supported.", None, None, None),
    "7f0a39945edd0b8f3dc7060389300d06d7a93ead": ("confirmed-current-boundary", "The title explicitly concerns a speech-driven physical model of coupled micro-speakers. Title-only evidence supports non-airborne speech sensing or production, without claims about acoustic fidelity.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "7ffe20657d03f2e520c2368b5d262a64a59ca3ee": ("rejected-out-of-scope", "The title concerns speech-driven body-motion generation; the generated object is body motion rather than speech. With title-only evidence, prosody-control membership is not supported.", None, None, None),
    "8038a3853dfdd9cd126eb3c07838edb71fce1cbc": ("confirmed-current-boundary", "The title explicitly concerns speech emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "80f97dfe4226f84e6e3ac744f0c739cf1ff1c88d": ("rejected-out-of-scope", "The title concerns information loss in the human auditory system and sentence syntax but does not establish a speech-system or spoken-language task. With title-only evidence, long-context decoding membership is not supported.", None, None, None),
    "8113872b69701af8aaeadbd9db1af15ba29371cc": ("rejected-out-of-scope", "The title concerns spatial audio-text embeddings under multi-source conditions but does not establish human speech or spoken-language evidence. With title-only evidence, speech grounding membership is not supported.", None, None, None),
    "813d412c3a68a707adfd60c8e9a98d1f415f79c4": ("confirmed-current-boundary", "The title explicitly concerns voice-command correction in a conversational user interface. Title-only evidence supports repair and clarification.", "meaning-and-interaction", "turn-taking-and-repair", "repair-and-clarification"),
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
