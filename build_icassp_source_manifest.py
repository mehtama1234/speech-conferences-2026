#!/usr/bin/env python3
"""Describe the preserved ICASSP 2026 discovery capture and its limits."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE / "data/icassp-2026-papers.json"
raw = path.read_bytes()
data = json.loads(raw)
supplement_path = HERE / "data/icassp-2026-official-metadata-supplement.json"
supplement = json.loads(supplement_path.read_text()) if supplement_path.exists() else {"records": []}
payload = {
    "venue": "ICASSP 2026",
    "source_type": "discovery-index-preserved-input",
    "source_name": "Semantic Scholar Graph API",
    "source_endpoint": "https://api.semanticscholar.org/graph/v1/paper/search/bulk",
    "query": {"venue": "ICASSP", "year": "2026", "fields": "title,abstract,externalIds,openAccessPdf,url"},
    "input_sha256": hashlib.sha256(raw).hexdigest(),
    "paper_count": data["n_papers"],
    "abstract_count": data["with_abstract"],
    "arxiv_count": data["with_arxiv"],
    "official_source_boundary": "IEEE Xplore/proceedings access was not available to the existing capture; Semantic Scholar is discovery metadata, not the official proceedings record.",
    "official_metadata_supplement": {"path": str(supplement_path.relative_to(HERE)), "record_count": len(supplement.get("records", [])), "boundary": supplement.get("coverage_boundary")},
    "title_evidence_status": "usable-for-cautious-topic-membership",
    "mechanism_evidence_status": "not-established-for-title-only-records",
    "deduplication_rule": "case-insensitive normalized title, first preserved record",
}
out = HERE / "data/icassp-2026-source-manifest.json"
out.write_text(json.dumps(payload, indent=2) + "\n")
print(json.dumps({"output": str(out), "paper_count": payload["paper_count"], "input_sha256": payload["input_sha256"]}))
