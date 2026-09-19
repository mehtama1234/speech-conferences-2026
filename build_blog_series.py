#!/usr/bin/env python3
"""Build standalone, plain-language blog essays from the first-principles atlas."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
BLOGS = REPORTS / "blogs"

THEME_LEADS = {
    "sound-and-production": "Before a machine can recognize speech, a body and an environment have to produce a pressure pattern. This essay follows that pattern from vocal activity through the room and recording device, asking what each description preserves and what it throws away.",
    "listening-and-separation": "A recording can contain the requested voice, other voices, music, echo, and device noise at the same time. This essay asks how a system can recover useful speech without pretending that missing evidence was cleanly observed.",
    "recognition-and-alignment": "Speech does not arrive as ready-made words with neat boundaries. This essay follows the work of turning changing sound into reusable units, pronunciations, timed alignments, and context-sensitive words without letting context invent what was not heard.",
    "meaning-and-interaction": "The same words can do different work when their emphasis, emotion, timing, and shared situation change. This essay follows the path from audible variation to intent, participation, and action.",
    "voice-generation-and-control": "Making speech is not one decision. A system must decide what to say, when to say it, whose voice to use, and how the delivery should sound. This essay separates those controls so a gain in one does not hide a loss in another.",
    "people-variation-and-health": "A speaker is a person, not a nuisance variable. Age, identity, health, disability, hearing ability, and interaction needs change both the signal and the cost of failure. This essay treats those differences as part of the problem definition.",
    "languages-accents-and-resources": "Speech technology is trained from uneven evidence. Languages, accents, dialects, speakers, and recording conditions do not receive equal data or equal evaluation. This essay follows what can be shared, what must remain local, and how missing evidence is made.",
    "evaluation-deployment-and-consequence": "A score is an observation, not a complete account of usefulness. This essay connects measurements to human goals, changing conditions, hardware limits, privacy, and the ability to inspect and challenge a claim.",
}

THEME_ORDER = [
    "sound-and-production", "listening-and-separation", "recognition-and-alignment", "meaning-and-interaction",
    "voice-generation-and-control", "people-variation-and-health", "languages-accents-and-resources", "evaluation-deployment-and-consequence",
]


def compact(value: object, limit: int = 520) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0] + "…"


def slug(index: int, name: str) -> str:
    return f"{index:02d}-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") + ".md"


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    syntheses = json.loads((DATA / "speech-subtheme-syntheses.json").read_text())
    papers = json.loads((DATA / "interspeech-2025-papers.json").read_text())
    paper_by_id = {p["paper_id"]: p for p in papers.get("papers", [])}
    by_subtheme = {r["subtheme_id"]: r for r in syntheses.get("records", [])}
    theme_by_id = {t["id"]: t for t in taxonomy.get("themes", [])}
    BLOGS.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# The Speech Atlas: eight first-principles essays", "",
        "This series starts with Fant's 1967 account of the speech communication chain and follows the ordinary pressures that recur in the reviewed INTERSPEECH papers. Each essay is self-contained. The essays explain a problem before naming a method, define unavoidable technical terms, and mark what the evidence cannot prove.", "",
        "**Evidence rule.** D2 means the official abstract supports the bounded problem and stated approach. D3 means the official paper text was captured and supports the reported mechanism and evaluation, but not independent reproduction. Counts are not prevalence estimates.", "",
        "## Reading order", "",
    ]
    built = []
    for number, theme_id in enumerate(THEME_ORDER, 1):
        theme = theme_by_id[theme_id]
        filename = slug(number, theme["name"])
        path = BLOGS / filename
        lines = [
            f"# {theme['name']}", "",
            f"*Essay {number} of 8 in The Speech Atlas.*", "",
            THEME_LEADS[theme_id], "",
            "## Start with the baseline", "",
            f"Fant's speech-chain account places this theme at the following point in communication: {theme.get('baseline_anchor_text', '')}", "",
            f"The ordinary problem is simple to state: {theme.get('ordinary_problem', '')}", "",
            f"A tempting shortcut is to {theme.get('naive_failure', '').rstrip('.')}. That shortcut fails because it hides the distinction this essay needs to keep visible.", "",
            f"The recurring move across this theme is to {theme.get('recurring_move', '').rstrip('.')}. The cost is equally important: {theme.get('tradeoff', '')}", "",
            "## The boundaries", "",
            "Each section below uses the same test: what pressure is being handled, what shortcut fails, what move recurs, and where the evidence stops.", "",
        ]
        for subtheme in theme.get("subthemes", []):
            row = by_subtheme.get(subtheme["id"], {})
            family = row.get("family_synthesis", {}) or {}
            concepts = subtheme.get("concepts", [])
            lines += [f"## {subtheme['name']}", "", f"**The question.** {subtheme.get('question', '')}", "", f"**How this boundary is derived.** {subtheme.get('derivation_evidence', '')}", "", f"**What the papers share.** {family.get('ordinary_pressure', '')}", "", f"**Why the shortcut fails.** {family.get('naive_shortcut', '')}", "", f"**The recurring move.** {family.get('recurring_move', '')}", ""]
            lines += ["### Words used in this section", ""]
            for concept in concepts:
                lines += [f"**{concept['name']}.** {concept.get('definition', '')}", f"*Boundary:* {concept.get('boundary', '')}", ""]
            lines += ["### What the papers show", ""]
            matrix = family.get("d3_comparison_matrix", []) or []
            evidence_ids = [p.get("paper_id") for p in matrix[:4]] or row.get("paper_ids", [])[:4]
            if matrix:
                matrix_by_id = {p.get("paper_id"): p for p in matrix}
            else:
                matrix_by_id = {}
            for pid in evidence_ids:
                paper = paper_by_id.get(pid, {})
                detail = matrix_by_id.get(pid, {})
                title = paper.get("title") or detail.get("title") or pid
                url = paper.get("paper_url") or f"https://www.isca-archive.org/interspeech_2025/{pid}.html"
                depth = "D3" if detail else "D2"
                if detail:
                    lines.append(f"- [{title}]({url}) ({depth}): {compact(detail.get('central_move'))} **Measured or tested:** {compact(detail.get('evaluation_object'), 300)} **Limit:** {compact(detail.get('evidence_limit'), 300)}")
                else:
                    lines.append(f"- [{title}]({url}) ({depth}): This paper is part of the reviewed evidence for this boundary. The available evidence is limited to the recorded abstract-level account.")
            if not evidence_ids:
                lines.append(f"- The reviewed record contains {row.get('reviewed_paper_count', 0)} papers, including {row.get('d3_paper_count', 0)} D3 papers and {row.get('d2_paper_count', 0)} D2 papers.")
            lines += ["", f"**Where this boundary stops.** {'; '.join(family.get('subtheme_boundary', []))}", "", f"**What this evidence does not establish.** {family.get('evidence_boundary', '')}", "", f"**Question left open.** {family.get('unresolved_question', '')}", ""]
        lines += ["## Closing note", "", "This essay is a map of recurring problems and research moves, not a leaderboard or a claim that these categories cover every speech study. The paper links and depth labels show what was actually checked; they do not turn reported results into independent facts.", ""]
        path.write_text("\n".join(lines))
        built.append({"theme_id": theme_id, "title": theme["name"], "path": str(path.relative_to(ROOT)), "subtheme_count": len(theme.get("subthemes", []))})
        index_lines.append(f"{number}. [{theme['name']}]({path.relative_to(REPORTS)}) — {THEME_LEADS[theme_id]}")
        index_lines.append("")
    index_lines += ["## Series boundary", "", "The baseline is Fant, Gunnar, *Sound, features, and perception* (1967). The taxonomy is an analyst-authored proposal derived from that chain and the reviewed paper evidence. It is not an official conference classification, a prevalence estimate, a clinical conclusion, or an independent replication study.", ""]
    (REPORTS / "SPEECH_BLOG_SERIES_INDEX.md").write_text("\n".join(index_lines))
    (DATA / "speech-blog-series-manifest.json").write_text(json.dumps({"series_title": "The Speech Atlas: eight first-principles essays", "theme_count": len(built), "subtheme_count": sum(x["subtheme_count"] for x in built), "essays": built}, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"essays": len(built), "subthemes": sum(x["subtheme_count"] for x in built), "output": "reports/SPEECH_BLOG_SERIES_INDEX.md"}))


if __name__ == "__main__":
    main()
