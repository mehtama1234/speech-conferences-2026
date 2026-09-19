#!/usr/bin/env python3
"""Record the third abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "0f4083d8f5440a1891c6baf5f24a4f7db319382a": ("reassigned-to-neighbor", "The abstract explicitly concerns Whisper ASR memory use, long-form audio, and GPU efficiency. The contribution is a resource-budget change, not a learned acoustic-unit question.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "0f5109dc24b6cf8dc0dc0715ca5057dde161540c": ("rejected-out-of-scope", "The abstract concerns active noise control and generic acoustic paths, without a speech or spoken-language object; noise control alone is insufficient for this speech taxonomy.", None, None, None),
    "0fd6674c828f0fdaa4da1ff78b7fcf411dd7f769": ("reassigned-to-neighbor", "The abstract explicitly includes acoustic speech-related information in multimodal sentiment analysis. The target is affective state, not literal intent in context.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "10908f287b34b7b35b8939a41101bf97951e7194": ("rejected-out-of-scope", "The abstract benchmarks compositionality in general audio sound scenes and synthetic acoustic attributes, without establishing a speech or spoken-language object.", None, None, None),
    "11303a06ceaffe7797c7617cf893255fb38f02d4": ("confirmed-current-boundary", "The abstract explicitly concerns multimodal emotion recognition in conversations and models uncertainty and context around emotion. D2 supports paralinguistic-state membership without full-paper verification.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "11f0ad96bd0778465f27494719146dee41d0fcef": ("reassigned-to-neighbor", "The abstract explicitly concerns neural speaker diarization and speaker consistency over long speech sequences. The task is assigning concurrent speaker sources, not measuring word understanding.", "listening-and-separation", "source-separation", "blind-source-separation"),
    "14649513fd5736f0c48e841f94506ee95b85e408": ("rejected-out-of-scope", "The abstract concerns weakly supervised audio-visual segmentation of general sounding objects and image regions, without a speech or spoken-language object.", None, None, None),
    "148e6a28a06a65325013c433111101010eb14bf4": ("reassigned-to-neighbor", "The abstract explicitly concerns streaming acoustic echo cancellation with near-end speech and a microphone/reference alignment objective. Echo reconstruction is the central operation, not generic channel coloration.", "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation"),
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
