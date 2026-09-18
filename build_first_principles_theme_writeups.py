#!/usr/bin/env python3
"""Build the unified plain-language theme and subtheme teaching document."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"


def first_sentence(value: object, limit: int = 420) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0] + "…"


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    syntheses = json.loads((DATA / "speech-subtheme-syntheses.json").read_text())
    by_subtheme = {row["subtheme_id"]: row for row in syntheses.get("records", [])}

    lines = [
        "# First-principles speech themes and subthemes",
        "",
        "This is the teaching layer of the atlas. It starts with the baseline speech-chain account, then explains why each boundary exists in ordinary language and names the papers that make the boundary useful. Counts are not prevalence estimates, and author-reported results are not independent reproductions.",
        "",
        f"Baseline: {taxonomy.get('baseline_source', {}).get('citation', 'baseline source not recorded')}.",
        "",
        "## How to read each section",
        "",
        "Each subtheme follows the same path: baseline stage or distinction → ordinary pressure → tempting shortcut → why it fails → recurring paper move → evidence and evaluation → boundary and limit.",
        "",
    ]

    for theme in taxonomy.get("themes", []):
        lines += [
            f"## {theme['name']}",
            "",
            f"**Baseline connection:** {theme.get('baseline_anchor_text', taxonomy.get('baseline_source', {}).get('citation', ''))}",
            f"**Ordinary problem:** {theme.get('ordinary_problem', '')}",
            f"**Why the first shortcut fails:** {theme.get('naive_failure', '')}",
            f"**Recurring move across this theme:** {theme.get('recurring_move', '')}",
            f"**Theme limit:** {theme.get('tradeoff', '')}",
            "",
        ]
        for subtheme in theme.get("subthemes", []):
            row = by_subtheme.get(subtheme["id"], {})
            family = row.get("family_synthesis", {}) or {}
            concepts = subtheme.get("concepts", [])
            matrix = family.get("d3_comparison_matrix", []) or []
            lines += [
                f"### {subtheme['name']}",
                "",
                f"**Baseline link:** {subtheme.get('baseline_anchor_text', subtheme.get('baseline_anchor', 'not recorded'))}",
                f"**Question:** {subtheme.get('question', '')}",
                f"**Derivation:** {subtheme.get('derivation_evidence', '')}",
                "",
                f"**What the papers share:** {family.get('ordinary_pressure', '')}",
                f"**The shortcut they outgrow:** {family.get('naive_shortcut', '')}",
                f"**The repeated mechanism:** {family.get('recurring_move', '')}",
                "",
                "#### Concepts inside this boundary",
                "",
            ]
            for concept in concepts:
                lines += [
                    f"**{concept['name']}.** {concept.get('definition', '')}",
                    f"Boundary: {concept.get('boundary', '')}",
                    "",
                ]
            lines += ["#### Named evidence", ""]
            if matrix:
                for paper in matrix[:4]:
                    lines += [
                        f"- **{paper.get('title', paper.get('paper_id', 'unnamed paper'))}** (`{paper.get('paper_id', '')}`; D3): {first_sentence(paper.get('central_move'))} Evaluation: {first_sentence(paper.get('evaluation_object'), 300)} Limit: {first_sentence(paper.get('evidence_limit'), 300)}",
                    ]
            else:
                variation = family.get("reviewed_variation", "")
                if variation:
                    lines.append(f"- Reviewed evidence examples: {first_sentence(variation, 900)}")
                lines.append(f"- Reviewed paper count: {row.get('reviewed_paper_count', 0)}; D3 full-paper count: {row.get('d3_paper_count', 0)}; D2 abstract-bounded count: {row.get('d2_paper_count', 0)}.")
            lines += [
                "",
                f"**Boundary from neighboring subthemes:** {'; '.join(family.get('subtheme_boundary', []))}",
                f"**What this evidence does not establish:** {family.get('evidence_boundary', '')}",
                f"**Open question:** {family.get('unresolved_question', '')}",
                "",
            ]

    (REPORTS / "SPEECH_FIRST_PRINCIPLES_THEME_WRITEUPS.md").write_text("\n".join(lines).rstrip() + "\n")
    print(json.dumps({"themes": len(taxonomy.get("themes", [])), "subthemes": sum(len(t.get("subthemes", [])) for t in taxonomy.get("themes", [])), "output": "reports/SPEECH_FIRST_PRINCIPLES_THEME_WRITEUPS.md"}))


if __name__ == "__main__":
    main()
