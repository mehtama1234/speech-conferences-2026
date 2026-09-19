#!/usr/bin/env python3
"""Record the seventh abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "2aa7d97b928fe996b38dadf25451433a44c380ae": ("confirmed-current-boundary", "The abstract explicitly concerns target speaker extraction from mixtures and schedules SNR, speaker count, overlap, and data realism. D2 supports target-conditioned separation membership.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "2b40f524c897766036c221593fe9c6ec7cc13250": ("reassigned-to-neighbor", "The abstract evaluates how close speech super-resolution output is to real wideband speech using embeddings, objective metrics, and listening tests. This is a quality/naturalness evaluation rather than listener-effort measurement.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "2cd5b5a38e31a9141415ca81f7859c12cbb2d60e": ("reassigned-to-neighbor", "The abstract explicitly concerns diffusion speech enhancement, phonetic accuracy, intelligibility, and efficient inference. Codec tokens are the mechanism; speech-prior denoising is the task boundary.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "2cdabc58f8557330a76116e1b9dfe03889297536": ("rejected-out-of-scope", "The abstract concerns general spatial audio and microphone-array encoding under simulated sound sources, without a speech or spoken-language object.", None, None, None),
    "2d5ec692660b218e12ccf87fc93f4e7517a90ea8": ("rejected-out-of-scope", "The abstract concerns MIDI-to-drum music synthesis and percussive audio, not speech or spoken-language generation.", None, None, None),
    "2e136c64ecad6bca958622bd640ee00d3aa38311": ("reassigned-to-neighbor", "The abstract explicitly concerns speech quality assessment and MOS prediction across sampling rates. High-frequency features are the input issue, but the evaluated target is quality and naturalness.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "2e70c2af8e17fc0c7e50629a53ed08e594ce053a": ("confirmed-current-boundary", "The abstract explicitly concerns speech enhancement and preserving phonetic information in noisy speech representations. Its information-theoretic analysis supports speech-prior denoising membership at D2.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "2e870d5a3ceb5d46486c2ca2634f8c523fc6c16c": ("reassigned-to-neighbor", "The abstract explicitly concerns parameter-efficient ASR adaptation under domain shift and the tradeoff between learning and forgetting. The core boundary is measured distribution shift, not accent robustness.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
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
