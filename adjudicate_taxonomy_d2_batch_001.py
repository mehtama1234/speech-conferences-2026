#!/usr/bin/env python3
"""Record the first abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "001d5225ef43f21ea65844aa6ecab2e628ea09f6": ("rejected-out-of-scope", "The abstract targets dysphagia screening from swallowing-related neck signals, not a speech or spoken-language object. The non-airborne sensing label would overstate the speech evidence available at D2.", None, None, None),
    "008ffaf570fbe5e64104ce36985024670a0a5cde": ("rejected-out-of-scope", "The title and abstract identify vocals separation, but do not establish speech or spoken-language sources; music-vocal separation is outside this speech taxonomy.", None, None, None),
    "0170388633269ae1f3c8c47d58fad1dd2ec4e657": ("confirmed-current-boundary", "The abstract explicitly concerns streaming automatic speech recognition and learned chunkwise label alignment. D2 evidence supports alignment membership, but not full-paper mechanism or generalization claims.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "03131c31bab6928bca2901d03519c841e4dca84d": ("rejected-out-of-scope", "The abstract describes general audio coding and does not establish a speech or spoken-language object; efficient audio codec work alone is insufficient for this speech taxonomy.", None, None, None),
    "036b21f2e7000e3b4b6d1875c95aa0dca52d70af": ("rejected-out-of-scope", "The abstract presents a Chinese dialogue satisfaction and emotion dataset but does not identify speech, audio, or spoken interaction evidence. Text dialogue alone is outside this speech taxonomy.", None, None, None),
    "038fb68ee9e308e13c125e66b71cafef48eb7174": ("rejected-out-of-scope", "The abstract concerns visual deepfake images or videos and MLLM explanation, not synthetic speech or spoken audio; privacy/security speech membership is not established.", None, None, None),
    "03e18de3236a26e8fcda5afa70f19e855725a676": ("confirmed-current-boundary", "The abstract explicitly concerns short-utterance speaker verification and duration-aware speaker embeddings. D2 supports identity membership but leaves full mechanism and deployment limits unreviewed.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "050635ffb58be0408255845d4ad98798b8929ba6": ("confirmed-current-boundary", "The abstract explicitly concerns speech emotion recognition and a generative representation of emotion classes. D2 supports paralinguistic-state membership without establishing full-paper results.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
