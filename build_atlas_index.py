#!/usr/bin/env python3
"""Build the plain-language entry point for the first-principles speech atlas."""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
taxonomy = json.loads((HERE / "data/speech-first-principles-taxonomy.json").read_text())
inter = json.loads((HERE / "data/interspeech-2025-semantic-review-queue.json").read_text())
icassp = json.loads((HERE / "data/icassp-2026-semantic-review-queue.json").read_text())
audit = json.loads((HERE / "data/speech-atlas-completion-audit.json").read_text())
concept_gaps = json.loads((HERE / "data/speech-concept-evidence-gaps.json").read_text())

def decisions(queue: dict) -> str:
    return ", ".join(f"{k}: {v}" for k, v in sorted(queue.get("decision_counts", {}).items()))

lines = [
    "# Speech research atlas", "",
    "This is the working entry point for an evidence-bounded, first-principles analysis of speech research.",
    "The goal is to explain the ordinary problem, why the obvious shortcut fails, what conceptual move replaces it, how that move works, and where the evidence stops.", "",
    "## Start here", "",
    "1. [Reading paths](SPEECH_FIRST_PRINCIPLES_READING_PATHS.md) — ordinary problems, broken shortcuts, conceptual moves, paper families, and limits.",
    "2. [Taxonomy](SPEECH_FIRST_PRINCIPLES_TAXONOMY.md) — 8 themes, 24 subthemes, and 72 bounded concepts.",
    "3. [Subtheme syntheses](SPEECH_SUBTHEME_SYNTHESES.md) — what reviewed papers agree on, how they differ, and what remains unreviewed.",
    "4. [Concept-family crosswalk](SPEECH_CONCEPT_FAMILY_CROSSWALK.md) — all 72 concepts compared across both venues with reviewed evidence and open candidates.",
    "5. [Concept evidence gaps](SPEECH_CONCEPT_EVIDENCE_GAPS.md) — concepts with no analyst-reviewed ICASSP example, with ordinary-problem boundaries and next evidence needed.",
    "6. [Paper analyses](INTERSPEECH_2025_DEEP_PAPER_ANALYSES.md) — every INTERSPEECH record at its actual evidence depth.",
    "7. [Normalized D3 notes](INTERSPEECH_2025_NORMALIZED_D3_NOTES.md) — a consolidated full-paper reading set with authoritative taxonomy paths.",
    "8. [Semantic gaps](SPEECH_SEMANTIC_REVIEW_GAPS.md) — ambiguous, insufficient, and out-of-scope cases.",
    "9. [ICASSP/INTERSPEECH crosswalk](ICASSP_2026_INTERSPEECH_2025_CROSSWALK.md) — a bounded comparison with denominators and evidence warnings.", "",
    "## Current evidence boundary", "",
    f"- INTERSPEECH 2025: {inter['paper_count']} records; {inter.get('reviewed_count', 0)} analyst-reviewed semantic assignments.",
    f"- ICASSP 2026: {icassp['paper_count']} records; {icassp.get('with_abstract', 0)} abstract-backed D2 records; {icassp.get('reviewed_count', 0)} analyst-reviewed seed assignments.",
    f"- Semantic decisions — INTERSPEECH: {decisions(inter)}.",
    f"- Semantic decisions — ICASSP: {decisions(icassp)}.",
    f"- Concept evidence gaps: {concept_gaps.get('gap_count', 0)} concepts currently lack an analyst-reviewed ICASSP example.",
    f"- Release status: `{audit['overall_status']}`. The bounded release is complete; open evidence boundaries remain explicit.", "",
    "## Rebuild", "", "```bash", "python3 rebuild_speech_atlas.py", "python3 verify_speech_atlas.py", "```", "",
    "The rebuild uses preserved inputs and keeps title-only, abstract, full-paper, artifact, and independent-execution evidence separate.",
]
(HERE / "reports/SPEECH_ATLAS_INDEX.md").write_text("\n".join(lines) + "\n")
print(json.dumps({"output": "reports/SPEECH_ATLAS_INDEX.md", "themes": taxonomy["theme_count"], "status": "written"}))
