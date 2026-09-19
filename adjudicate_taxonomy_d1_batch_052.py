#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "8495cf197ceeb211cf6154b8a83aaf59d8cbe964": ("reassigned-to-neighbor", "The title explicitly concerns continual learning in automatic speech recognition. Title-only evidence places it under distribution shift rather than domain and context biasing.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "85e15a20e92914e2e27a16c77e5e902fc88a74c2": ("confirmed-current-boundary", "The title explicitly concerns dysarthric speech recognition and post-recognition correction evaluated beyond word error rate. Title-only evidence supports word error versus understanding, without establishing the relationship between the measures.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "8615344206e920c54da4aa8b38e819ccca260032": ("rejected-out-of-scope", "The title concerns singing voice conversion rather than a human-speech or spoken-language task. With title-only evidence, voice-conversion membership is not supported for this speech taxonomy.", None, None, None),
    "862b4c47558097540ed6e396031d6da6d6cf7557": ("confirmed-current-boundary", "The title explicitly concerns audio-visual speaker extraction using gesture and lip cues. Title-only evidence supports target-conditioned separation, without establishing extraction quality.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "8690f2f5bc211ccb3ca9b5f75549b3fef005dc2f": ("confirmed-current-boundary", "The title explicitly concerns child automatic speech recognition. Title-only evidence supports age and developmental speech, without establishing performance across child ages.", "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "86d6df6de433c91055dd11b7c904fbbfd8101fc0": ("rejected-out-of-scope", "The title concerns a general vision-language model and does not establish a human-speech or spoken-language task. With title-only evidence, interactional feedback membership is not supported.", None, None, None),
    "889896508123af9e564d6b7caa252c3616d28c19": ("rejected-out-of-scope", "The title concerns fetal-head segmentation in medical imaging and does not establish a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "88b3595ca9974c1ad3cac521e8ff3e85f4c3ce5c": ("rejected-out-of-scope", "The title concerns sound morphing from noisy mixtures but does not establish a human-speech or spoken-language task. With title-only evidence, voice-conversion membership is not supported.", None, None, None),
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
