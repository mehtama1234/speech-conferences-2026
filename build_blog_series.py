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

PLAIN_LANGUAGE_DICTIONARY = [
    ("Fant's speech chain", "a practical way to follow speech from a speaker's body, through the air and a recording device, to a listener and an interpretation"),
    ("D2", "evidence checked in the official paper abstract; it supports the paper's stated problem and approach, but not details that appear only in the full paper"),
    ("D3", "evidence checked in the official full paper text; it supports what the authors report about their method and tests, but it is still not an independent reproduction"),
    ("ASR", "automatic speech recognition: software that turns speech recordings into written words"),
    ("TTS", "text-to-speech: software that turns written words into a spoken signal"),
    ("speaker embedding", "a compact numerical description intended to preserve characteristics of a voice or speaker"),
    ("self-supervised learning", "training in which the recording supplies part of its own teaching signal, so hand-written labels are needed less often"),
    ("voice activity detection", "a decision about whether a signal segment contains speech"),
    ("word error rate", "the number of word substitutions, insertions, and deletions divided by the reference word count"),
    ("equal error rate", "the point at which two kinds of biometric decision error—false acceptance and false rejection—are equal"),
    ("interaural", "between the two ears; an interaural difference is a difference in timing or level between left and right channels"),
    ("MRI", "magnetic resonance imaging, used here to observe anatomy or movement without cutting into the body"),
    ("EEG", "electroencephalography, a measurement of electrical activity at the scalp"),
    ("MFCC", "a compact description of the broad shape of a sound spectrum, often used as an input feature"),
    ("F0", "the rate of vocal-fold vibration, commonly heard as the main component of pitch"),
]


def compact(value: object, limit: int = 520) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0] + "…"


def lower_initial(value: object) -> str:
    text = str(value or "").strip()
    return text[:1].lower() + text[1:] if text else text


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
            f"One tempting shortcut is: {theme.get('naive_failure', '').rstrip('.')}. It fails because it hides the distinction this essay needs to keep visible.", "",
            f"The recurring move across this theme is to {lower_initial(theme.get('recurring_move', '')).rstrip('.')}. The cost is equally important: {theme.get('tradeoff', '')}", "",
            "## The boundaries", "",
            "Each section below uses the same test: what pressure is being handled, what shortcut fails, what move recurs, and where the evidence stops.", "",
            "## Plain-language dictionary", "",
            "The papers use specialized names because they measure specialized things. These are the terms that recur in this essay, translated before they do argumentative work:", "",
        ]
        for term, definition in PLAIN_LANGUAGE_DICTIONARY:
            lines.append(f"**{term}.** {definition}.")
        lines += ["", "This is a map of distinctions, not a ranking of methods. A paper can be useful while still answering only one narrow question.", ""]
        for subtheme in theme.get("subthemes", []):
            row = by_subtheme.get(subtheme["id"], {})
            family = row.get("family_synthesis", {}) or {}
            concepts = subtheme.get("concepts", [])
            lines += [f"## {subtheme['name']}", "", f"This boundary follows from the baseline account: {lower_initial(subtheme.get('derivation_evidence', ''))}", "", f"**The question.** {subtheme.get('question', '')}", "", f"**The pressure.** {family.get('ordinary_pressure', '')}", "", f"**Why the easy answer breaks.** {family.get('naive_shortcut', '')}", "", f"**The move that recurs.** {family.get('recurring_move', '')}", ""]
            lines += ["### Words used in this section", ""]
            for concept in concepts:
                lines += [f"**{concept['name']}.** {concept.get('definition', '')}", f"*Boundary:* {concept.get('boundary', '')}", ""]
            lines += ["### What the evidence shows", ""]
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
