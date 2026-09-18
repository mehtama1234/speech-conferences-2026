#!/usr/bin/env python3
"""Audit per-paper depth, source capture, and evidence-boundary honesty."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
FIELDS = ["bp", "wh", "naive", "ap", "mech", "math", "dots", "eval", "ww", "po", "limits", "source", "depth"]


def main() -> None:
    rows = [json.loads(line) for line in (DATA / "interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines() if line.strip()]
    failures = []
    counts = {}
    for row in rows:
        depth = row.get("depth", "missing")
        counts[depth] = counts.get(depth, 0) + 1
        missing = [field for field in FIELDS if not row.get(field)]
        source = row.get("source") or {}
        if depth == "D3":
            if not source.get("pdf_path") or not (ROOT / source["pdf_path"]).exists():
                missing.append("captured PDF")
            if not source.get("text_path") or not (ROOT / source["text_path"]).exists():
                missing.append("captured text")
            if "abstract" in str(row.get("math", "")).lower() and "does not" in str(row.get("math", "")).lower():
                missing.append("math field still relies on abstract-only wording")
        elif depth == "D2":
            if "abstract-only boundary" not in str(row.get("limits", "")).lower():
                missing.append("explicit abstract-only boundary")
        if missing:
            failures.append({"paper_id": row.get("paper_id"), "depth": depth, "missing": sorted(set(missing))})

    payload = {
        "status": "pass" if not failures else "incomplete",
        "paper_count": len(rows),
        "depth_counts": counts,
        "complete_count": len(rows) - len(failures),
        "failures": failures,
        "claim_boundary": "This is a structural and provenance audit. It does not prove that an analyst's interpretation is scientifically correct.",
    }
    (DATA / "speech-paper-analysis-quality-audit.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# Paper analysis quality audit",
        "",
        f"**Status:** `{payload['status']}`",
        "",
        f"Records: **{len(rows)}**; depth counts: **{counts}**; records passing structural and source checks: **{payload['complete_count']}**.",
        "",
        "D3 requires captured PDF and text. D2 requires an explicit abstract-only boundary. This audit does not certify the analyst's interpretation or reproduce any result.",
        "",
    ]
    if failures:
        lines += ["## Failures", ""] + [f"- `{x['paper_id']}` ({x['depth']}): {', '.join(x['missing'])}" for x in failures]
    else:
        lines += ["No structural or depth-boundary failures detected.", ""]
    (REPORTS / "SPEECH_PAPER_ANALYSIS_QUALITY_AUDIT.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"status": payload["status"], "papers": len(rows), "failures": len(failures), "depth_counts": counts}))


if __name__ == "__main__":
    main()
