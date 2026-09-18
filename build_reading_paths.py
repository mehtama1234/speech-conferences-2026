#!/usr/bin/env python3
"""Render explanatory first-principles reading paths through the speech atlas."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
    deep_by_id = {json.loads(line)["paper_id"]: json.loads(line) for line in (DATA / "interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines() if line.strip()}
    batch = {"rows": []}
    for row in queue.get("rows", []):
        if row.get("review_state") == "analyst-reviewed" and deep_by_id.get(row.get("paper_id"), {}).get("depth") == "D3":
            review = row.get("analyst_review", {})
            if not review:
                review = deep_by_id[row["paper_id"]].get("semantic_review", {})
            batch["rows"].append({
                "title": row.get("title"),
                "theme_id": review.get("theme_id"),
                "subtheme_id": review.get("subtheme_id"),
                "concept_id": review.get("concept_id"),
                "semantic_reasoning": review.get("semantic_reasoning", ""),
            })
    by_theme = defaultdict(list)
    for row in batch["rows"]:
        by_theme[row["theme_id"]].append(row)
    out = [
        "# First-principles reading paths through speech research",
        "",
        f"This guide is the conceptual front door to the atlas. Each path starts with an ordinary speech problem, names the intuitive solution that breaks, then follows the recurring research moves and the papers currently carrying evidence. The paper list is a {len(batch['rows'])}-paper D3 seed, not a prevalence ranking.",
        "",
        "## How to read the paths",
        "",
        "Start with the physical or human pressure. Ask what information is missing or mixed together. Then ask what the paper keeps, throws away, aligns, separates, or generates. Only after that ask whether the evaluation measures the property a person actually needs.",
        "",
    ]
    for index, theme in enumerate(taxonomy["themes"], 1):
        papers = by_theme.get(theme["id"], [])
        out += [f"## Path {index}: {theme['name']}", "", f"### 1. The ordinary problem", "", theme["ordinary_problem"], "", f"### 2. The tempting but broken shortcut", "", theme["naive_failure"], "", f"### 3. The recurring conceptual move", "", theme["recurring_move"], "", "### 4. Follow the problem through the subthemes", ""]
        for subtheme in theme["subthemes"]:
            concepts = "; ".join(f"**{c['name']}** — {c['definition']}" for c in subtheme["concepts"])
            out += [f"#### {subtheme['name']}", "", f"Ask: {subtheme['question']}", "", concepts, ""]
        out += ["### 5. Papers carrying the current evidence", ""]
        if papers:
            for paper in papers:
                out += [f"- **{paper['title']}** — assigned to `{paper['subtheme_id']}/{paper['concept_id']}`. {paper['semantic_reasoning']}"]
        else:
            out += ["No reviewed D3 seed paper is assigned here yet."]
        out += ["", "### 6. What not to conclude", "", theme["tradeoff"], "", "The current evidence supports a conceptual connection, not a venue-wide frequency claim, causal ranking, or independent reproduction.", ""]
    out += ["## Cross-path lesson", "", "Speech research repeatedly faces the same deeper problem: the signal available to a system is a partial, mixed, changing trace of a person and situation. Stronger systems do not simply add a larger model; they decide which distinctions matter—source versus room, target versus interferer, sound versus word, word versus intent, identity versus style, and benchmark proxy versus human goal. Each distinction introduces a new failure mode, so the atlas keeps the mechanism and its boundary together.", ""]
    (REPORTS / "SPEECH_FIRST_PRINCIPLES_READING_PATHS.md").write_text("\n".join(out) + "\n")
    print(json.dumps({"paths": len(taxonomy["themes"]), "reviewed_papers": len(batch["rows"])}))


if __name__ == "__main__":
    main()
