#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "b8a5252be9fe294d23daccd78f63d930f0788eda": ("confirmed-current-boundary", "The title explicitly concerns multichannel speech enhancement in a cocktail-party speech-emotion task. Title-only evidence supports target-conditioned separation, without establishing separation or emotion-recognition performance.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "b9cfa81c19fe036a685912d449d076aa0bce10bd": ("confirmed-current-boundary", "The title explicitly concerns reconstruction of speech envelopes from EEG. Title-only evidence supports augmentative communication, without establishing intelligibility or user benefit.", "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication"),
    "ba429f7fc80bf2907669a75ab53d0febae47f482": ("confirmed-current-boundary", "The title explicitly concerns a universal speech-enhancement system. Title-only evidence supports speech-prior denoising, without establishing robustness across degradations.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "bab92391b7f85cba53ae716f07227f84f6bf5573": ("confirmed-current-boundary", "The title explicitly concerns ambiguity-aware emotion recognition from speech and text. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "bad275e401ee3a3be85c7a873d54eb71c84b3ff1": ("reassigned-to-neighbor", "The title explicitly concerns acoustic and facial markers of perceived conversational success in spontaneous speech. Title-only evidence places it under interactional feedback rather than dialogue state.", "meaning-and-interaction", "grounding-and-action", "interactional-feedback"),
    "bb7ab71e29a5af246baa10c5f11b0bd7ff0061fc": ("confirmed-current-boundary", "The title explicitly concerns a phonological tokenizer using prosody-aware phonetic tokens. Title-only evidence supports learned speech units, without establishing token quality or linguistic usefulness.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "bbe8d31e39bc4b603818979d19218b01d103070b": ("rejected-out-of-scope", "The title concerns a song-aesthetics evaluation challenge rather than a human-speech or spoken-language task. With title-only evidence, listener effort membership is not supported.", None, None, None),
    "bc910f279b719376c53e0df3c9eeeb5479f4fe38": ("reassigned-to-neighbor", "The title explicitly concerns speech-quality evaluation with large language models. Title-only evidence places it under quality and naturalness rather than calibration and selective use.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
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
