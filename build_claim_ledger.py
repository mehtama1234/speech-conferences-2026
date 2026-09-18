#!/usr/bin/env python3
"""Build a bounded claim ledger for the D3 representative papers."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
notes = json.loads((HERE / "data/interspeech-2025-d3-notes.json").read_text())["notes"]
papers = {row["paper_id"]: row for row in json.loads((HERE / "data/interspeech-2025-representative-papers.json").read_text())["papers"]}

rows = []
for i, note in enumerate(notes, 1):
    paper = papers[note["paper_id"]]
    rows.append({
        "claim_id": f"IS25-C{i:02d}",
        "paper_id": note["paper_id"],
        "theme": note["theme"],
        "claim": note["ww"],
        "evidence_depth": "D3",
        "evidence_source": {
            "paper_url": paper["paper_url"],
            "pdf_sha256": paper["pdf_sha256"],
            "full_text_sha256": paper["full_text_sha256"],
            "local_text": paper["full_text_path"],
        },
        "support_status": "paper-reported-not-independently-verified",
        "independent_support_status": "not-established",
        "denominator_or_scope": "the datasets, speakers, utterances, and evaluation protocol reported by this paper",
        "limitations": note["limits"],
        "next_action": "inspect tables and artifacts, then attempt a bounded reproduction if data and environment are available",
    })

out = HERE / "data/interspeech-2025-claim-ledger.json"
out.write_text(json.dumps({"venue": "INTERSPEECH 2025", "claim_count": len(rows), "claims": rows}, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {out} ({len(rows)} claims)")
