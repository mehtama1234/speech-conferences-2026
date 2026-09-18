#!/usr/bin/env python3
"""Build the human-readable first-pass INTERSPEECH report from JSON outputs."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
papers = json.loads((HERE / "data/interspeech-2025-papers.json").read_text())
themes = json.loads((HERE / "data/interspeech-2025-themes.json").read_text())
rows = []
for item in themes["taxonomy"]:
    rows.append(
        f"| {item['label']} | {item['paper_count']:,} | {item['percent_of_corpus']:.1f}% | {item['first_principles']} |"
    )

report = f"""# INTERSPEECH 2025 first-pass speech atlas

## What this establishes

This report is a deterministic abstract-aware map of the official ISCA Archive
for INTERSPEECH 2025. The archive contains **{papers['n_papers']:,} papers**;
**{papers['with_abstract']:,}** have abstracts in the captured corpus, and there
were **{papers['source_failures']}** source-page failures.

The assignment method matches transparent patterns against each official title
and abstract. It is useful for discovering field structure, but it is not a
full-paper semantic judgment. Every assignment is therefore marked D2 (abstract
evidence), and the report must not be read as evidence that the paper's detailed
mechanism or result has been independently checked.

Source: [{papers['source_manifest']['index_url']}]({papers['source_manifest']['index_url']})

## First-principles themes

| Theme | Papers | Share of corpus | Why this pressure exists |
|---|---:|---:|---|
{chr(10).join(rows)}

Membership is overlapping: a paper can address more than one pressure. The map
therefore measures theme mentions/assignments, not a partition of the conference.
{themes['method']['unmatched_papers']} papers received no current conceptual
assignment and remain an explicit review queue rather than being forced into a
theme.

## Evidence boundaries

- D0/D1 metadata and title evidence are not used to claim a mechanism.
- D2 abstracts support the broad problem, method family, and stated result only
  when the abstract says them explicitly.
- D3 full-paper analysis, D4 artifact inspection, and D5 independent execution
  have not yet been completed by this first pass.
- Theme counts are corpus-local and should not be interpreted as prevalence in
  speech research as a whole.
- Abstract claims remain author-reported claims until full-paper and artifact
  corroboration are performed.

## Next depth pass

1. Resolve the 54 unmatched records and review ambiguous multi-theme assignments.
2. Add paper-level `bp`, `wh`, `naive`, `ap`, `mech`, `math`, `dots`, `ww`,
   `po`, and `limits` records for the highest-yield themes.
3. Inspect official PDFs for mechanism, assumptions, baselines, denominators,
   and limitations.
4. Audit linked code, data, checkpoints, and run instructions.
5. Compare the resulting speech taxonomy with the existing ICASSP 2026 map.
"""

out = HERE / "reports/INTERSPEECH_2025_FIRST_PASS.md"
out.parent.mkdir(exist_ok=True)
out.write_text(report)
print(f"wrote {out}")
