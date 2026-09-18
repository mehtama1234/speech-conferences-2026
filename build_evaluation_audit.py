#!/usr/bin/env python3
"""Separate task, metric, denominator, target, and evidence boundary."""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"

METRICS = [
    "WER", "MER", "F1", "RMSE", "SI-SDR", "HASPI", "MBSTOI", "PESQ", "MOS", "accuracy", "macro-F1", "EER", "perplexity", "SNR", "DER", "IoU", "BLEU", "CER", "FAR", "FRR"
]
DATASETS = [
    "LibriSpeech", "FLEURS", "DementiaBank", "TORGO", "UASpeech", "Switchboard", "VoiceBank-DEMAND", "CommonPhone", "VoxCeleb", "NIST", "Arabic", "English", "Mandarin", "Nigerian", "MRI", "in-house", "newly collected", "real-world"
]


def mentions(text: str, values: list[str]) -> list[str]:
    return [value for value in values if re.search(rf"\b{re.escape(value)}\b", text or "", re.I)]


def main() -> None:
    rows = [json.loads(line) for line in (DATA / "interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines() if line.strip()]
    out = []
    for row in rows:
        evidence = " ".join(str(row.get(key, "")) for key in ("eval", "math", "ww"))
        metrics = mentions(evidence, METRICS)
        datasets = mentions(evidence, DATASETS)
        if row["depth"] == "D3":
            denominator = "; ".join(datasets) if datasets else "not established in the structured note; inspect paper tables/protocol"
            boundary = row["limits"]
        else:
            denominator = "; ".join(datasets) if datasets else "not established from abstract"
            boundary = "Abstract does not establish the full denominator, split construction, comparison protocol, or human target."
        target = "human/listener usefulness" if any(x in evidence.lower() for x in ("listener", "intelligibility", "naturalness", "subjective", "quality", "human")) else "task score as reported by authors"
        out.append({
            "paper_id": row["paper_id"],
            "title": row["title"],
            "depth": row["depth"],
            "task": row["bp"],
            "metrics_or_measures": metrics or ["not established"],
            "denominator_or_dataset": denominator,
            "target_or_proxy": target,
            "reported_evaluation_evidence": row["eval"],
            "claim_boundary": boundary,
            "independent_execution": "not attempted",
        })
    out_path = DATA / "interspeech-2025-evaluation-audit.jsonl"
    with out_path.open("w") as handle:
        for row in out:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    report = REPORTS / "INTERSPEECH_2025_EVALUATION_AUDIT.md"
    report.write_text("\n".join([
        "# INTERSPEECH 2025 evaluation audit",
        "",
        "This audit separates what a paper evaluates from what its metric stands for. It does not fill missing denominators from intuition.",
        "",
        f"- Records: {len(out)}",
        f"- D3: {sum(row['depth'] == 'D3' for row in out)}",
        f"- D2: {sum(row['depth'] == 'D2' for row in out)}",
        f"- Records with an identified metric/measure: {sum(row['metrics_or_measures'] != ['not established'] for row in out)}",
        "",
        "The machine-readable rows preserve task, metric, denominator/dataset, target/proxy, reported evidence, and claim boundary. D2 rows remain abstract-bounded; D3 rows remain author-reported and were not independently executed.",
        "",
    ]) + "\n")
    print(json.dumps({"records": len(out), "D3": sum(row["depth"] == "D3" for row in out), "D2": sum(row["depth"] == "D2" for row in out)}))


if __name__ == "__main__":
    main()
