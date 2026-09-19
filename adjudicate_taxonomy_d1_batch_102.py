#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "han25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use a wavelet and time-frequency model for multichannel speech enhancement while preserving spatial cues. The evidence supports spectral masking, without proving separation of all overlapping sources.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "han25d_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly separate overlapping in-car speech using array channels, impulse responses, and spatial localization. The evidence supports target-conditioned separation, without proving every cabin condition.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "hannan25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly produce compact ASR models through representation learning and report training speed and WER under device constraints. This is latency and resource budget, not few-shot adaptation.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "hao25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly cancel acoustic feedback caused by the hearing-aid receiver and microphone path, with closed-loop fine tuning and low latency. This belongs under acoustic echo cancellation, not generic channel coloration.", ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation"),
    "harrington25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly compare generations of automatic speaker-recognition systems and analyze persistent speaker-level difficulty. The evidence supports speaker verification, without reducing performance variation to identity alone.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "hartanto25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly separate speech mixtures while estimating speaker and microphone locations and room parameters, without a target enrollment condition. This is blind source separation, not channel coloration.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "hartuv25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly tokenize speech into phonetic-acoustic units while reconstructing the signal and testing the tokens in speech language models. This is acoustic-to-token mapping, not perceptual enhancement alone.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "hasumi25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly create a cinematic dataset whose speech stem contains laughter and screams for source separation. The governing task is separating a human-vocal speech stem, not generating style or emotion.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": sections, "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
