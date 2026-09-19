#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "chiang25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns speech dereverberation for cochlear-implant users. Title-only evidence supports perceptual enhancement, without establishing dereverberation quality or user benefit.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "cho25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns speech-emotion recognition. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "cho25c_interspeech": ("rejected-out-of-scope", "The title concerns conversion from human to non-human voices and does not establish a human-speech or spoken-language target within this taxonomy. It is outside this speech scope.", None, None, None),
    "chochlakis25_interspeech": ("rejected-out-of-scope", "The title concerns general multimodal emotion recognition but does not establish a human-speech or spoken-language task. With title-only evidence, perceptual speech enhancement membership is not supported.", None, None, None),
    "choi25_interspeech": ("rejected-out-of-scope", "The title concerns temporally aligned automated audio captioning but does not establish a human-speech or spoken-language task. With title-only evidence, word error versus understanding membership is not supported.", None, None, None),
    "choi25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns on-device streaming discrete speech units. Title-only evidence supports learned speech units, without establishing unit quality or streaming tradeoffs.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "choi25c_interspeech": ("confirmed-current-boundary", "The title explicitly concerns diffusion text-to-speech training and modality alignment. Title-only evidence supports text-to-speech planning, without establishing training acceleration or synthesis quality.", "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "choi25d_interspeech": ("rejected-out-of-scope", "The title concerns neural spectral-band generation for general audio coding and does not establish a human-speech or spoken-language task. With title-only evidence, sampling and quantization for speech is not supported.", None, None, None),
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
