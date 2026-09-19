#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "c6ce642fd44a3f70c0d14d21665cf73f3d0f55aa": ("rejected-out-of-scope", "The title concerns structured metadata for audio language models in sound design and does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
    "c91dffb73ca94e785cdbe002ef99106045e43127": ("confirmed-current-boundary", "The title explicitly concerns contextual speech language models and biasing rewards. Title-only evidence supports domain and context biasing, without establishing recognition gains or generalization.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "c92d0c92d4c00e0e9d8a14c0d72ef26d81f92cbc": ("confirmed-current-boundary", "The title explicitly concerns open-vocabulary instruct text-to-speech. Title-only evidence supports text-to-speech planning, without establishing open-vocabulary coverage or synthesis quality.", "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "cac70ccdb14e412559b291b12a6440fb4231d1de": ("rejected-out-of-scope", "The title explicitly concerns music source restoration rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "cb3409d64edcf270597ab76df73b0c0080d0264f": ("rejected-out-of-scope", "The title concerns cross-domain bioacoustic learning and does not establish a human-speech or spoken-language task. With title-only evidence, few-shot speech adaptation is not supported.", None, None, None),
    "cd3019a89f4f838d160016e095a6f601fef985a1": ("confirmed-current-boundary", "The title explicitly concerns robust extraction of closely moving speakers. Title-only evidence supports target-conditioned separation, without establishing extraction quality in dynamic scenes.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "cebaec8acc70e6390a269b4e2d456e318ef1a4ab": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition in conversations. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "ced118e9aa8647763324db203766f4742a18e2f0": ("reassigned-to-neighbor", "The title explicitly concerns universal speech enhancement. Title-only evidence places it under speech-prior denoising rather than multiple-time-scale measurement.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
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
