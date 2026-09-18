# Speech conferences 2026 — toward a reproducible speech research atlas

**Live:** https://mehtama1234.github.io/speech-conferences-2026/

This is an evidence-bounded conceptual atlas of **ICASSP 2026** and **INTERSPEECH 2025**.
ICASSP publishes through IEEE Xplore, so most preserved ICASSP records are still D1
title-only; the atlas labels that boundary rather than presenting title matches as paper
analysis.

The repository also contains the official ISCA **INTERSPEECH 2025** corpus: 1,179
paper pages, 1,179 abstracts, and zero source failures. It now has 1,179 structured
first-principles records, 1,179 analyst-reviewed semantic dispositions (1,129 confirmed
speech assignments and 50 explicit scope rejections), and 469 captured
full-paper D3 analyses. ICASSP has 3,864 D1/D2 paper records, 3,864 analyst-reviewed
semantic dispositions (609 confirmed speech assignments, 3,254 explicit rejections,
and one unresolved metadata-only case).

Key finding: ICASSP is "Acoustics, **Speech**, and Signal Processing" — a *broad* conference.
Speech is only ~15% of it (image & video is larger). Within the speech slice, ASR leads,
then music/sound-events, enhancement, self-supervised, speaker-verification/anti-spoofing.

Pipelines:

- ICASSP: `ingest_icassp.py -> mine_themes.py -> build_page.py`
- INTERSPEECH: `ingest_interspeech.py -> mine_interspeech.py -> build_interspeech_report.py`
- Validation: `verify_speech_atlas.py`
- Rebuild from preserved inputs: `rebuild_speech_atlas.py`

The full end-to-end target is in `GOAL.md`; the plain-language depth standard is in
`FIRST_PRINCIPLES_GOAL.md`.

The current release includes 469 D3 full-paper records, a 710-paper D2 analysis queue,
an artifact-link ledger, a point-in-time reachability audit, and an
ICASSP/INTERSPEECH crosswalk. It also contains claim ledgers whose claims
are linked to captured PDF/text hashes and marked as paper-reported rather than
independently verified. Link reachability is recorded separately from code
execution or scientific reproduction.

The deep-analysis layer is now being built explicitly rather than inferred from
the broad keyword map. The first-principles taxonomy has 8 themes, 24
subthemes, and 72 concepts with ordinary-problem definitions and boundaries
([taxonomy report](reports/SPEECH_FIRST_PRINCIPLES_TAXONOMY.md)). Every
INTERSPEECH paper now has canonical `bp`/`wh`/`naive`/`ap`/`mech`/`math`/`eval`/
`limits` fields in the evidence JSONL at its actual D2 or D3 depth
([paper analysis report](reports/INTERSPEECH_2025_DEEP_PAPER_ANALYSES.md)).
All 1,179 INTERSPEECH papers have analyst-reviewed semantic
dispositions: 1,129 confirmed speech assignments and 50 explicit scope rejections. There
are no provisional or unresolved INTERSPEECH rows; the bounded release is complete with
explicit source, artifact, and independent-reproduction boundaries preserved.
The corpus-wide assignment files make that boundary explicit for every record: each paper is
analyst-confirmed, a provisional title/abstract candidate, or unresolved with preserved evidence
and a reason for further adjudication.

The explanatory entry point is [the first-principles reading
paths](reports/SPEECH_FIRST_PRINCIPLES_READING_PATHS.md), which walks from
ordinary speech problems through failed shortcuts, conceptual moves, paper
families, and evidence limits.

The [normalized D3 notes](reports/INTERSPEECH_2025_NORMALIZED_D3_NOTES.md) provide a
single reader-facing report with taxonomy paths, mechanisms, reported results, and
limitations for the taxonomy-valid full-paper seed.

The compact [atlas index](reports/SPEECH_ATLAS_INDEX.md) links the taxonomy,
subtheme syntheses, paper analyses, unresolved cases, and cross-venue comparison.
The [concept-family crosswalk](reports/SPEECH_CONCEPT_FAMILY_CROSSWALK.md) compares all
72 concepts across both venues while keeping reviewed evidence separate from open candidates.

ICASSP now has the same explicit boundary queue across all 3,864 captured
records: 683 are D2 abstract records, the rest are D1 title-only records, and
non-speech papers remain visible as unsupported rows rather than being removed
from the denominator ([ICASSP semantic queue](reports/ICASSP_2026_SEMANTIC_REVIEW_QUEUE.md)).

`FIRST_PRINCIPLES_GOAL.md` defines the no-jargon, first-principles standard for
paper, theme, subtheme, mathematical-concept, and paper-family explanations. The
current reports preserve the distinction between title, abstract, full-paper,
artifact, and independent-execution evidence; optional future readings do not
change the bounded-release status.
