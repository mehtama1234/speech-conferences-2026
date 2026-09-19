#!/usr/bin/env python3
"""Record the twenty-fourth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "94bff5f797912a5fbceb1f1bfdf3f86a7d939233": ("confirmed-current-boundary", "The title explicitly concerns radar acoustic speech enhancement. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "9526f8b58aaaef40e6bbc85e835731c17403fb3c": ("confirmed-current-boundary", "The title explicitly concerns controllable editing of speech stress to express emphatic intent. Title-only evidence supports prosodic meaning.", "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "956c5a2961ac5d0cd05773d0f2bb9ea5803fd8a0": ("confirmed-current-boundary", "The title explicitly names a non-verbal speech dataset with word-level annotation. Title-only evidence supports speech data collection.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "9862889a562e2a2896cfca777aad486f876a6221": ("confirmed-current-boundary", "The title explicitly concerns synthesized-data selection for Te Reo Māori automatic speech recognition. Title-only evidence supports self-training and pseudo-labels.", "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels"),
    "9a748868c41227c414c764726a988713ca38aa8a": ("reassigned-to-neighbor", "The title explicitly concerns slot filling as reasoning for speech-language models. The semantic grounding task is more direct than speech acts; title-only evidence supports referential grounding.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "9bb64481817fbd737529a300d60c8cc815957ab5": ("rejected-out-of-scope", "The title concerns active noise cancellation and secondary-path estimation but does not establish a human-speech or spoken-language task. With title-only evidence, acoustic echo cancellation membership is not supported.", None, None, None),
    "9c0f4abccf4a964e8ab275a350b2ec54314db2f2": ("confirmed-current-boundary", "The title explicitly concerns multimodal foundation models for hearing aids. Title-only evidence supports accessibility fit, without establishing user benefit.", "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "9ca4f2af9528d32da9919de5ee1bbf5d49729f16": ("confirmed-current-boundary", "The title explicitly concerns phoneme-conditioned bandwidth extension for body-conducted speech. Title-only evidence supports perceptual enhancement.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
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
