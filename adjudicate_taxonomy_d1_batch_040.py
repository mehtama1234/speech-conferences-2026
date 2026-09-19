#!/usr/bin/env python3
"""Record the twenty-ninth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "b3fb63852e7054a894168d220324bd4148249207": ("confirmed-current-boundary", "The title explicitly concerns low-resource speech recognition. Title-only evidence supports few-shot adaptation.", "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "b3fb69b7c671c266abe3f90b0db6b06c9617acab": ("rejected-out-of-scope", "The title concerns beamforming for a smart-glasses audio front end but does not establish a human-speech or spoken-language task. With title-only evidence, speech spatial-filtering membership is not supported.", None, None, None),
    "b4f10f94080be8b8d0b084faa3423822defcd911": ("confirmed-current-boundary", "The title explicitly concerns end-to-end flow-matching speech enhancement. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "b552fde861cf6a9a24c02ff9fbf0010165a12aea": ("reassigned-to-neighbor", "The title explicitly concerns test-time adaptation of generative spoken-language models. The direct boundary is adapting under distribution shift rather than domain-context biasing.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "b5c385f66048432475ec096077e111934ee2efce": ("confirmed-current-boundary", "The title explicitly concerns robust speech recognition under adversarial fine-tuning. Title-only evidence supports distribution-shift robustness.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "b755d2dfd70a82b967565c805ade5850dbda0a84": ("confirmed-current-boundary", "The title explicitly concerns zero-shot visual voice cloning. Title-only evidence supports unseen-speaker synthesis.", "voice-generation-and-control", "identity-and-conversion", "unseen-speaker-synthesis"),
    "b79cec720f1d85878b8aba254c543ba40d367a4e": ("confirmed-current-boundary", "The title explicitly concerns multimodal conversational emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "b825e59147fc9302e536389263e599c492ff5746": ("confirmed-current-boundary", "The title explicitly concerns autoregressive target-speaker extraction. Title-only evidence supports target-conditioned separation.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
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
