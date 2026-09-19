#!/usr/bin/env python3
"""Record the thirtieth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "b92560a40b9ab39486284f9d578d4ba30d3555d5": ("confirmed-current-boundary", "The title explicitly concerns target-speaker extraction. Title-only evidence supports target-conditioned separation.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "b9dcd43b1085fa35e0d58c5444c572974f09a54a": ("confirmed-current-boundary", "The title explicitly concerns low-power speech bandwidth extension. Title-only evidence supports perceptual enhancement.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "b9de5cbb0261db4ee3532d10a13d5abed578ab94": ("confirmed-current-boundary", "The title explicitly concerns visual speech recognition across languages. Title-only evidence supports non-airborne speech sensing.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "bb31aa4d39f252722b88a9ab77b093ce636ef7ff": ("rejected-out-of-scope", "The title concerns general sound-source localization and prediction intervals but does not establish a human-speech or spoken-language task. With title-only evidence, speech spatial filtering membership is not supported.", None, None, None),
    "bb50db60215ca0d171752ee09cb48b9dda10873b": ("confirmed-current-boundary", "The title explicitly concerns conversational emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "bba13f58f9c9f543a280dc22f2fb27cf7b4986f3": ("confirmed-current-boundary", "The title explicitly concerns multi-talker overlapped speech recognition and translation. Title-only evidence supports long-context and multi-stream decoding.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "bbf024a804b9674211e8acb0a9e9ce20e822b5f5": ("confirmed-current-boundary", "The title explicitly concerns speech-language models generating multi-speaker dialogues. Title-only evidence supports dialogue-state membership, without claims about conversational quality.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "bbf0c363a0d39e661839c675e2a2b983b3cfbbfb": ("confirmed-current-boundary", "The title explicitly concerns estimating hand-related features from speech. Title-only evidence supports non-airborne speech sensing, without claims about sensing reliability.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
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
