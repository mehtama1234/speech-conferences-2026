# Speech research atlas

This is the working entry point for an evidence-bounded, first-principles analysis of speech research.
The goal is to explain the ordinary problem, why the obvious shortcut fails, what conceptual move replaces it, how that move works, and where the evidence stops.

## Start here

1. [Reading paths](SPEECH_FIRST_PRINCIPLES_READING_PATHS.md) — ordinary problems, broken shortcuts, conceptual moves, paper families, and limits.
2. [Taxonomy](SPEECH_FIRST_PRINCIPLES_TAXONOMY.md) — 8 themes, 24 subthemes, and 72 bounded concepts.
3. [Subtheme syntheses](SPEECH_SUBTHEME_SYNTHESES.md) — what reviewed papers agree on, how they differ, and what remains unreviewed.
4. [Concept-family crosswalk](SPEECH_CONCEPT_FAMILY_CROSSWALK.md) — all 72 concepts compared across both venues with reviewed evidence and open candidates.
5. [Concept evidence gaps](SPEECH_CONCEPT_EVIDENCE_GAPS.md) — concepts with no analyst-reviewed ICASSP example, with ordinary-problem boundaries and next evidence needed.
6. [Paper analyses](INTERSPEECH_2025_DEEP_PAPER_ANALYSES.md) — every INTERSPEECH record at its actual evidence depth.
7. [Normalized D3 notes](INTERSPEECH_2025_NORMALIZED_D3_NOTES.md) — a consolidated full-paper reading set with authoritative taxonomy paths.
8. [Semantic gaps](SPEECH_SEMANTIC_REVIEW_GAPS.md) — ambiguous, insufficient, and out-of-scope cases.
9. [ICASSP/INTERSPEECH crosswalk](ICASSP_2026_INTERSPEECH_2025_CROSSWALK.md) — a bounded comparison with denominators and evidence warnings.

## Current evidence boundary

- INTERSPEECH 2025: 1179 records; 1179 analyst-reviewed semantic assignments.
- ICASSP 2026: 3864 records; 682 abstract-backed D2 records; 3864 analyst-reviewed seed assignments.
- Semantic decisions — INTERSPEECH: ambiguous: 0, insufficient-evidence: 0, supported: 1130, unsupported: 49.
- Semantic decisions — ICASSP: ambiguous: 0, insufficient-evidence: 1, supported: 609, unsupported: 3254.
- Concept evidence gaps: 4 concepts currently lack an analyst-reviewed ICASSP example.
- Release status: `bounded-release-complete-with-explicit-boundaries`. The bounded release is complete; open evidence boundaries remain explicit.

## Rebuild

```bash
python3 rebuild_speech_atlas.py
python3 verify_speech_atlas.py
```

The rebuild uses preserved inputs and keeps title-only, abstract, full-paper, artifact, and independent-execution evidence separate.
