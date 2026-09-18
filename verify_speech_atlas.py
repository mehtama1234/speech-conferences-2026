#!/usr/bin/env python3
"""Structural checks for the first speech-atlas release."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
errors: list[str] = []


def load(name: str):
    try:
        return json.loads((HERE / name).read_text())
    except Exception as exc:
        errors.append(f"{name}: {type(exc).__name__}: {exc}")
        return None


papers = load("data/interspeech-2025-papers.json")
icassp_data = load("data/icassp-2026-papers.json")
themes = load("data/interspeech-2025-themes.json")
representatives = load("data/interspeech-2025-representative-papers.json")
d3_notes = load("data/interspeech-2025-d3-notes.json")
artifact_ledger = load("data/interspeech-2025-artifact-ledger.json")
release_manifest = load("data/speech-atlas-release-manifest.json")
review_queue = load("data/interspeech-2025-review-queue.json")
execution_audit = load("data/interspeech-2025-execution-audit.json")
paper_evidence_path = HERE / "data/interspeech-2025-paper-evidence.jsonl"
paper_evidence = []
if paper_evidence_path.exists():
    try:
        paper_evidence = [json.loads(line) for line in paper_evidence_path.read_text().splitlines() if line.strip()]
    except Exception as exc:
        errors.append(f"paper evidence JSONL: {type(exc).__name__}: {exc}")
claim_ledger = load("data/interspeech-2025-claim-ledger.json")
icassp_source_manifest = load("data/icassp-2026-source-manifest.json")
completion_audit = load("data/speech-atlas-completion-audit.json")
taxonomy = load("data/speech-first-principles-taxonomy.json")
semantic_queue = load("data/interspeech-2025-semantic-review-queue.json")
interspeech_assignments_path = HERE / "data/interspeech-2025-semantic-assignments.jsonl"
interspeech_assignments = []
if interspeech_assignments_path.exists():
    interspeech_assignments = [json.loads(line) for line in interspeech_assignments_path.read_text().splitlines() if line.strip()]
semantic_batch = load("data/interspeech-2025-semantic-reviewed-batch-001.json")
semantic_d2_batch = load("data/interspeech-2025-semantic-reviewed-d2-batch-001.json")
semantic_d2_batch_2 = load("data/interspeech-2025-semantic-reviewed-d2-batch-002.json")
semantic_d2_batch_3 = load("data/interspeech-2025-semantic-reviewed-d2-batch-003.json")
semantic_d2_batch_4 = load("data/interspeech-2025-semantic-reviewed-d2-batch-004.json")
semantic_d2_batch_5 = load("data/interspeech-2025-semantic-reviewed-d2-batch-005.json")
semantic_d2_batch_6 = load("data/interspeech-2025-semantic-reviewed-d2-batch-006.json")
semantic_d2_batch_7 = load("data/interspeech-2025-semantic-reviewed-d2-batch-007.json")
semantic_d2_batch_8 = load("data/interspeech-2025-semantic-reviewed-d2-batch-008.json")
semantic_d2_batch_9 = load("data/interspeech-2025-semantic-reviewed-d2-batch-009.json")
semantic_d2_batch_10 = load("data/interspeech-2025-semantic-reviewed-d2-batch-010.json")
semantic_d2_batch_11 = load("data/interspeech-2025-semantic-reviewed-d2-batch-011.json")
semantic_d2_batch_12 = load("data/interspeech-2025-semantic-reviewed-d2-batch-012.json")
semantic_d2_batch_13 = load("data/interspeech-2025-semantic-reviewed-d2-batch-013.json")
semantic_d2_batch_14 = load("data/interspeech-2025-semantic-reviewed-d2-batch-014.json")
semantic_d2_batch_15 = load("data/interspeech-2025-semantic-reviewed-d2-batch-015.json")
semantic_d2_batch_16 = load("data/interspeech-2025-semantic-reviewed-d2-batch-016.json")
semantic_d2_batch_17 = load("data/interspeech-2025-semantic-reviewed-d2-batch-017.json")
semantic_d2_batch_18 = load("data/interspeech-2025-semantic-reviewed-d2-batch-018.json")
semantic_d2_batch_19 = load("data/interspeech-2025-semantic-reviewed-d2-batch-019.json")
semantic_d2_batch_20 = load("data/interspeech-2025-semantic-reviewed-d2-batch-020.json")
semantic_d2_batch_21 = load("data/interspeech-2025-semantic-reviewed-d2-batch-021.json")
semantic_d2_batch_22 = load("data/interspeech-2025-semantic-reviewed-d2-batch-022.json")
semantic_d2_batch_23 = load("data/interspeech-2025-semantic-reviewed-d2-batch-023.json")
semantic_d2_batch_24 = load("data/interspeech-2025-semantic-reviewed-d2-batch-024.json")
semantic_d2_batch_25 = load("data/interspeech-2025-semantic-reviewed-d2-batch-025.json")
semantic_d2_batch_26 = load("data/interspeech-2025-semantic-reviewed-d2-batch-026.json")
semantic_d2_batch_27 = load("data/interspeech-2025-semantic-reviewed-d2-batch-027.json")
semantic_d2_batch_28 = load("data/interspeech-2025-semantic-reviewed-d2-batch-028.json")
semantic_d2_batch_29 = load("data/interspeech-2025-semantic-reviewed-d2-batch-029.json")
semantic_d2_batch_30 = load("data/interspeech-2025-semantic-reviewed-d2-batch-030.json")
semantic_d2_batch_31 = load("data/interspeech-2025-semantic-reviewed-d2-batch-031.json")
semantic_d2_batch_32 = load("data/interspeech-2025-semantic-reviewed-d2-batch-032.json")
semantic_d2_batch_33 = load("data/interspeech-2025-semantic-reviewed-d2-batch-033.json")
semantic_d2_batch_34 = load("data/interspeech-2025-semantic-reviewed-d2-batch-034.json")
semantic_d2_batch_35 = load("data/interspeech-2025-semantic-reviewed-d2-batch-035.json")
semantic_d2_batch_36 = load("data/interspeech-2025-semantic-reviewed-d2-batch-036.json")
semantic_d2_batch_37 = load("data/interspeech-2025-semantic-reviewed-d2-batch-037.json")
semantic_d2_batch_38 = load("data/interspeech-2025-semantic-reviewed-d2-batch-038.json")
semantic_batch_26 = load("data/interspeech-2025-semantic-reviewed-batch-026.json")
semantic_out_scope_batch_38 = load("data/interspeech-2025-semantic-reviewed-out-of-scope-batch-038.json")
semantic_provisional_batch_39 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-039.json")
semantic_provisional_batch_40 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-040.json")
semantic_provisional_batch_41 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-041.json")
semantic_provisional_batch_42 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-042.json")
semantic_provisional_batch_43 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-043.json")
semantic_provisional_batch_44 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-044.json")
semantic_provisional_batch_45 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-045.json")
semantic_provisional_batch_46 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-046.json")
semantic_provisional_batch_47 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-047.json")
semantic_provisional_batch_48 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-048.json")
semantic_provisional_batch_49 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-049.json")
semantic_provisional_batch_50 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-050.json")
semantic_provisional_batch_51 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-051.json")
semantic_provisional_batch_52 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-052.json")
semantic_provisional_batch_53 = load("data/interspeech-2025-semantic-reviewed-provisional-d2-batch-053.json")
semantic_d3_batch_2 = load("data/interspeech-2025-semantic-reviewed-d3-batch-002.json")
semantic_d3_batch_3 = load("data/interspeech-2025-semantic-reviewed-d3-batch-003.json")
semantic_d3_batch_4 = load("data/interspeech-2025-semantic-reviewed-d3-batch-004.json")
semantic_d3_batch_5 = load("data/interspeech-2025-semantic-reviewed-d3-batch-005.json")
semantic_d3_batch_6 = load("data/interspeech-2025-semantic-reviewed-d3-batch-006.json")
semantic_d3_batch_7 = load("data/interspeech-2025-semantic-reviewed-d3-batch-007.json")
semantic_d3_batch_8 = load("data/interspeech-2025-semantic-reviewed-d3-batch-008.json")
semantic_d3_batch_9 = load("data/interspeech-2025-semantic-reviewed-d3-batch-009.json")
semantic_d3_batch_10 = load("data/interspeech-2025-semantic-reviewed-d3-batch-010.json")
semantic_d3_batch_11 = load("data/interspeech-2025-semantic-reviewed-d3-batch-011.json")
semantic_d3_batch_12 = load("data/interspeech-2025-semantic-reviewed-d3-batch-012.json")
semantic_d3_batch_13 = load("data/interspeech-2025-semantic-reviewed-d3-batch-013.json")
semantic_d3_batch_14 = load("data/interspeech-2025-semantic-reviewed-d3-batch-014.json")
semantic_d3_batch_15 = load("data/interspeech-2025-semantic-reviewed-d3-batch-015.json")
semantic_boundary_batch_25 = load("data/interspeech-2025-semantic-reviewed-batch-025.json")
seed_synthesis = load("data/speech-first-principles-seed-synthesis.json")
subtheme_synthesis = load("data/speech-subtheme-syntheses.json")
concept_family_crosswalk = load("data/speech-concept-family-crosswalk.json")
cross_venue_crosswalk = load("data/icassp-interspeech-crosswalk.json")
concept_evidence_gaps = load("data/speech-concept-evidence-gaps.json")
reading_paths = HERE / "reports/SPEECH_FIRST_PRINCIPLES_READING_PATHS.md"
semantic_gaps = HERE / "reports/SPEECH_SEMANTIC_REVIEW_GAPS.md"
atlas_index = HERE / "reports/SPEECH_ATLAS_INDEX.md"
icassp_semantic = load("data/icassp-2026-semantic-review-queue.json")
icassp_assignments_path = HERE / "data/icassp-2026-semantic-assignments.jsonl"
icassp_assignments = []
if icassp_assignments_path.exists():
    icassp_assignments = [json.loads(line) for line in icassp_assignments_path.read_text().splitlines() if line.strip()]
icassp_semantic_batch = load("data/icassp-2026-semantic-reviewed-batch-001.json")
icassp_semantic_batch_2 = load("data/icassp-2026-semantic-reviewed-batch-002.json")
icassp_semantic_batch_3 = load("data/icassp-2026-semantic-reviewed-batch-003.json")
icassp_semantic_batch_4 = load("data/icassp-2026-semantic-reviewed-batch-004.json")
icassp_semantic_batch_5 = load("data/icassp-2026-semantic-reviewed-batch-005.json")
icassp_semantic_batch_6 = load("data/icassp-2026-semantic-reviewed-batch-006.json")
icassp_semantic_batch_7 = load("data/icassp-2026-semantic-reviewed-batch-007.json")
icassp_semantic_batch_8 = load("data/icassp-2026-semantic-reviewed-batch-008.json")
icassp_semantic_batch_9 = load("data/icassp-2026-semantic-reviewed-batch-009.json")
icassp_semantic_batch_10 = load("data/icassp-2026-semantic-reviewed-batch-010.json")
icassp_semantic_batch_11 = load("data/icassp-2026-semantic-reviewed-batch-011.json")
icassp_semantic_batch_12 = load("data/icassp-2026-semantic-reviewed-batch-012.json")
icassp_semantic_batch_13 = load("data/icassp-2026-semantic-reviewed-batch-013.json")
icassp_semantic_batch_14 = load("data/icassp-2026-semantic-reviewed-batch-014.json")
icassp_semantic_batch_15 = load("data/icassp-2026-semantic-reviewed-batch-015.json")
icassp_semantic_batch_16 = load("data/icassp-2026-semantic-reviewed-batch-016.json")
icassp_semantic_batch_17 = load("data/icassp-2026-semantic-reviewed-batch-017.json")
icassp_semantic_batch_18 = load("data/icassp-2026-semantic-reviewed-batch-018.json")
icassp_semantic_batch_19 = load("data/icassp-2026-semantic-reviewed-batch-019.json")
icassp_semantic_batch_20 = load("data/icassp-2026-semantic-reviewed-batch-020.json")
icassp_semantic_batch_21 = load("data/icassp-2026-semantic-reviewed-batch-021.json")
icassp_semantic_batch_22 = load("data/icassp-2026-semantic-reviewed-batch-022.json")
icassp_semantic_batch_23 = load("data/icassp-2026-semantic-reviewed-batch-023.json")
icassp_semantic_batch_24 = load("data/icassp-2026-semantic-reviewed-batch-024.json")
icassp_semantic_batch_25 = load("data/icassp-2026-semantic-reviewed-batch-025.json")
icassp_semantic_batch_26 = load("data/icassp-2026-semantic-reviewed-batch-026.json")
icassp_semantic_batch_27 = load("data/icassp-2026-semantic-reviewed-batch-027.json")
icassp_semantic_batch_28 = load("data/icassp-2026-semantic-reviewed-batch-028.json")
icassp_semantic_batch_29 = load("data/icassp-2026-semantic-reviewed-batch-029.json")
icassp_semantic_batch_30 = load("data/icassp-2026-semantic-reviewed-batch-030.json")
icassp_semantic_batch_31 = load("data/icassp-2026-semantic-reviewed-batch-031.json")
icassp_semantic_batch_32 = load("data/icassp-2026-semantic-reviewed-batch-032.json")
icassp_semantic_batch_33 = load("data/icassp-2026-semantic-reviewed-batch-033.json")
icassp_semantic_batch_34 = load("data/icassp-2026-semantic-reviewed-batch-034.json")
icassp_semantic_batch_35 = load("data/icassp-2026-semantic-reviewed-batch-035.json")
icassp_semantic_batch_36 = load("data/icassp-2026-semantic-reviewed-batch-036.json")
icassp_semantic_batch_37 = load("data/icassp-2026-semantic-reviewed-batch-037.json")
icassp_semantic_batch_38 = load("data/icassp-2026-semantic-reviewed-batch-038.json")
icassp_semantic_batch_39 = load("data/icassp-2026-semantic-reviewed-batch-039.json")
icassp_semantic_batch_40 = load("data/icassp-2026-semantic-reviewed-batch-040.json")
icassp_semantic_batch_41 = load("data/icassp-2026-semantic-reviewed-batch-041.json")
icassp_semantic_batch_42 = load("data/icassp-2026-semantic-reviewed-batch-042.json")
icassp_semantic_batch_43 = load("data/icassp-2026-semantic-reviewed-batch-043.json")
icassp_semantic_batch_44 = load("data/icassp-2026-semantic-reviewed-batch-044.json")
icassp_semantic_batch_45 = load("data/icassp-2026-semantic-reviewed-batch-045.json")
icassp_semantic_batch_46 = load("data/icassp-2026-semantic-reviewed-batch-046.json")
icassp_semantic_batch_47 = load("data/icassp-2026-semantic-reviewed-batch-047.json")
icassp_semantic_batch_48 = load("data/icassp-2026-semantic-reviewed-batch-048.json")
icassp_semantic_batch_49 = load("data/icassp-2026-semantic-reviewed-batch-049.json")
icassp_semantic_batch_50 = load("data/icassp-2026-semantic-reviewed-batch-050.json")
icassp_semantic_batch_51 = load("data/icassp-2026-semantic-reviewed-batch-051.json")
icassp_semantic_batch_52 = load("data/icassp-2026-semantic-reviewed-batch-052.json")
icassp_semantic_batch_53 = load("data/icassp-2026-semantic-reviewed-batch-053.json")
icassp_semantic_batch_54 = load("data/icassp-2026-semantic-reviewed-batch-054.json")
icassp_semantic_batch_55 = load("data/icassp-2026-semantic-reviewed-batch-055.json")
icassp_semantic_batch_56 = load("data/icassp-2026-semantic-reviewed-batch-056.json")
icassp_semantic_batch_57 = load("data/icassp-2026-semantic-reviewed-batch-057.json")
icassp_semantic_batch_58 = load("data/icassp-2026-semantic-reviewed-batch-058.json")
icassp_semantic_batch_59 = load("data/icassp-2026-semantic-reviewed-batch-059.json")
icassp_semantic_batch_60 = load("data/icassp-2026-semantic-reviewed-batch-060.json")
icassp_semantic_batch_61 = load("data/icassp-2026-semantic-reviewed-batch-061.json")
icassp_semantic_batch_62 = load("data/icassp-2026-semantic-reviewed-batch-062.json")
icassp_semantic_batch_63 = load("data/icassp-2026-semantic-reviewed-batch-063.json")
icassp_semantic_batch_64 = load("data/icassp-2026-semantic-reviewed-batch-064.json")
icassp_semantic_batch_65 = load("data/icassp-2026-semantic-reviewed-batch-065.json")
icassp_semantic_batch_66 = load("data/icassp-2026-semantic-reviewed-batch-066.json")
icassp_semantic_batch_67 = load("data/icassp-2026-semantic-reviewed-batch-067.json")
icassp_semantic_batch_68 = load("data/icassp-2026-semantic-reviewed-batch-068.json")
icassp_semantic_batch_69 = load("data/icassp-2026-semantic-reviewed-batch-069.json")
icassp_semantic_batch_70 = load("data/icassp-2026-semantic-reviewed-batch-070.json")
icassp_semantic_batch_71 = load("data/icassp-2026-semantic-reviewed-batch-071.json")
icassp_semantic_batch_72 = load("data/icassp-2026-semantic-reviewed-batch-072.json")
icassp_semantic_batch_73 = load("data/icassp-2026-semantic-reviewed-batch-073.json")
icassp_semantic_batch_74 = load("data/icassp-2026-semantic-reviewed-batch-074.json")
icassp_semantic_batch_75 = load("data/icassp-2026-semantic-reviewed-batch-075.json")
icassp_semantic_batch_76 = load("data/icassp-2026-semantic-reviewed-batch-076.json")
icassp_semantic_batch_77 = load("data/icassp-2026-semantic-reviewed-batch-077.json")
icassp_semantic_batch_78 = load("data/icassp-2026-semantic-reviewed-batch-078.json")
icassp_semantic_batch_79 = load("data/icassp-2026-semantic-reviewed-batch-079.json")
icassp_semantic_batch_80 = load("data/icassp-2026-semantic-reviewed-batch-080.json")
icassp_semantic_batch_81 = load("data/icassp-2026-semantic-reviewed-batch-081.json")
icassp_semantic_batch_82 = load("data/icassp-2026-semantic-reviewed-batch-082.json")
icassp_semantic_batch_83 = load("data/icassp-2026-semantic-reviewed-batch-083.json")
icassp_semantic_batch_84 = load("data/icassp-2026-semantic-reviewed-batch-084.json")
icassp_semantic_batch_85 = load("data/icassp-2026-semantic-reviewed-batch-085.json")
icassp_semantic_batch_86 = load("data/icassp-2026-semantic-reviewed-batch-086.json")
icassp_semantic_batch_87 = load("data/icassp-2026-semantic-reviewed-batch-087.json")
icassp_semantic_batch_88 = load("data/icassp-2026-semantic-reviewed-batch-088.json")
icassp_semantic_batch_89 = load("data/icassp-2026-semantic-reviewed-batch-089.json")
icassp_evidence_path = HERE / "data/icassp-2026-paper-evidence.jsonl"
icassp_evidence = []
if icassp_evidence_path.exists():
    try:
        icassp_evidence = [json.loads(line) for line in icassp_evidence_path.read_text().splitlines() if line.strip()]
    except Exception as exc:
        errors.append(f"ICASSP paper evidence JSONL: {type(exc).__name__}: {exc}")
deep_analysis_path = HERE / "data/interspeech-2025-deep-paper-analyses.jsonl"
deep_analysis = []
if deep_analysis_path.exists():
    try:
        deep_analysis = [json.loads(line) for line in deep_analysis_path.read_text().splitlines() if line.strip()]
    except Exception as exc:
        errors.append(f"deep paper analyses JSONL: {type(exc).__name__}: {exc}")
evaluation_path = HERE / "data/interspeech-2025-evaluation-audit.jsonl"
evaluation_rows = []
if evaluation_path.exists():
    try:
        evaluation_rows = [json.loads(line) for line in evaluation_path.read_text().splitlines() if line.strip()]
    except Exception as exc:
        errors.append(f"evaluation audit JSONL: {type(exc).__name__}: {exc}")
second_papers = load("data/interspeech-2025-second-d3-papers.json")
second_notes = load("data/interspeech-2025-second-d3-notes.json")
second_claims = load("data/interspeech-2025-second-claim-ledger.json")
sixth_papers = load("data/interspeech-2025-sixth-d3-papers.json")
sixth_notes = load("data/interspeech-2025-sixth-d3-notes.json")
sixth_claims = load("data/interspeech-2025-sixth-claim-ledger.json")
seventh_papers = load("data/interspeech-2025-seventh-d3-papers.json")
seventh_notes = load("data/interspeech-2025-seventh-d3-notes.json")
seventh_claims = load("data/interspeech-2025-seventh-claim-ledger.json")
eighth_papers = load("data/interspeech-2025-eighth-d3-papers.json")
eighth_notes = load("data/interspeech-2025-eighth-d3-notes.json")
eighth_claims = load("data/interspeech-2025-eighth-claim-ledger.json")
ninth_papers = load("data/interspeech-2025-ninth-d3-papers.json")
ninth_notes = load("data/interspeech-2025-ninth-d3-notes.json")
ninth_claims = load("data/interspeech-2025-ninth-claim-ledger.json")
tenth_papers = load("data/interspeech-2025-tenth-d3-papers.json")
tenth_notes = load("data/interspeech-2025-tenth-d3-notes.json")
tenth_claims = load("data/interspeech-2025-tenth-claim-ledger.json")
twelfth_papers = load("data/interspeech-2025-twelfth-d3-papers.json")
twelfth_notes = load("data/interspeech-2025-twelfth-d3-notes.json")
twelfth_claims = load("data/interspeech-2025-twelfth-claim-ledger.json")
thirteenth_papers = load("data/interspeech-2025-thirteenth-d3-papers.json")
thirteenth_notes = load("data/interspeech-2025-thirteenth-d3-notes.json")
thirteenth_claims = load("data/interspeech-2025-thirteenth-claim-ledger.json")
fourteenth_papers = load("data/interspeech-2025-fourteenth-d3-papers.json")
fourteenth_notes = load("data/interspeech-2025-fourteenth-d3-notes.json")
fourteenth_claims = load("data/interspeech-2025-fourteenth-claim-ledger.json")
fifteenth_papers = load("data/interspeech-2025-fifteenth-d3-papers.json")
fifteenth_notes = load("data/interspeech-2025-fifteenth-d3-notes.json")
fifteenth_claims = load("data/interspeech-2025-fifteenth-claim-ledger.json")
sixteenth_papers = load("data/interspeech-2025-sixteenth-d3-papers.json")
sixteenth_notes = load("data/interspeech-2025-sixteenth-d3-notes.json")
sixteenth_claims = load("data/interspeech-2025-sixteenth-claim-ledger.json")
seventeenth_papers = load("data/interspeech-2025-seventeenth-d3-papers.json")
seventeenth_notes = load("data/interspeech-2025-seventeenth-d3-notes.json")
seventeenth_claims = load("data/interspeech-2025-seventeenth-claim-ledger.json")
eighteenth_papers = load("data/interspeech-2025-eighteenth-d3-papers.json")
eighteenth_notes = load("data/interspeech-2025-eighteenth-d3-notes.json")
eighteenth_claims = load("data/interspeech-2025-eighteenth-claim-ledger.json")
nineteenth_papers = load("data/interspeech-2025-nineteenth-d3-papers.json")
nineteenth_notes = load("data/interspeech-2025-nineteenth-d3-notes.json")
nineteenth_claims = load("data/interspeech-2025-nineteenth-claim-ledger.json")
twentieth_papers = load("data/interspeech-2025-twentieth-d3-papers.json")
twentieth_notes = load("data/interspeech-2025-twentieth-d3-notes.json")
twentieth_claims = load("data/interspeech-2025-twentieth-claim-ledger.json")
twentyfirst_papers = load("data/interspeech-2025-twentyfirst-d3-papers.json")
twentyfirst_notes = load("data/interspeech-2025-twentyfirst-d3-notes.json")
twentyfirst_claims = load("data/interspeech-2025-twentyfirst-claim-ledger.json")
twentisecond_papers = load("data/interspeech-2025-twentisecond-d3-papers.json")
twentisecond_notes = load("data/interspeech-2025-twentisecond-d3-notes.json")
twentisecond_claims = load("data/interspeech-2025-twentisecond-claim-ledger.json")
twentythird_papers = load("data/interspeech-2025-twentythird-d3-papers.json")
twentythird_notes = load("data/interspeech-2025-twentythird-d3-notes.json")
twentythird_claims = load("data/interspeech-2025-twentythird-claim-ledger.json")
twentyfourth_papers = load("data/interspeech-2025-twentyfourth-d3-papers.json")
twentyfourth_notes = load("data/interspeech-2025-twentyfourth-d3-notes.json")
twentyfourth_claims = load("data/interspeech-2025-twentyfourth-claim-ledger.json")
twentyfifth_papers = load("data/interspeech-2025-twentyfifth-d3-papers.json")
twentyfifth_notes = load("data/interspeech-2025-twentyfifth-d3-notes.json")
twentyfifth_claims = load("data/interspeech-2025-twentyfifth-claim-ledger.json")
twentysixth_papers = load("data/interspeech-2025-twentysixth-d3-papers.json")
twentysixth_notes = load("data/interspeech-2025-twentysixth-d3-notes.json")
twentysixth_claims = load("data/interspeech-2025-twentysixth-claim-ledger.json")
twentyseventh_papers = load("data/interspeech-2025-twentyseventh-d3-papers.json")
twentyseventh_notes = load("data/interspeech-2025-twentyseventh-d3-notes.json")
twentyseventh_claims = load("data/interspeech-2025-twentyseventh-claim-ledger.json")
twentyeighth_papers = load("data/interspeech-2025-twentyeighth-d3-papers.json")
twentyeighth_notes = load("data/interspeech-2025-twentyeighth-d3-notes.json")
twentyeighth_claims = load("data/interspeech-2025-twentyeighth-claim-ledger.json")
twentyninth_papers = load("data/interspeech-2025-twentyninth-d3-papers.json")
twentyninth_notes = load("data/interspeech-2025-twentyninth-d3-notes.json")
twentyninth_claims = load("data/interspeech-2025-twentyninth-claim-ledger.json")
thirtieth_papers = load("data/interspeech-2025-thirtieth-d3-papers.json")
thirtieth_notes = load("data/interspeech-2025-thirtieth-d3-notes.json")
thirtieth_claims = load("data/interspeech-2025-thirtieth-claim-ledger.json")
thirtyfirst_papers = load("data/interspeech-2025-thirtyfirst-d3-papers.json")
thirtyfirst_notes = load("data/interspeech-2025-thirtyfirst-d3-notes.json")
thirtyfirst_claims = load("data/interspeech-2025-thirtyfirst-claim-ledger.json")
thirtysecond_papers = load("data/interspeech-2025-thirtysecond-d3-papers.json")
thirtysecond_notes = load("data/interspeech-2025-thirtysecond-d3-notes.json")
thirtysecond_claims = load("data/interspeech-2025-thirtysecond-claim-ledger.json")
thirtythird_papers = load("data/interspeech-2025-thirtythird-d3-papers.json")
thirtythird_notes = load("data/interspeech-2025-thirtythird-d3-notes.json")
thirtythird_claims = load("data/interspeech-2025-thirtythird-claim-ledger.json")
thirtyfourth_papers = load("data/interspeech-2025-thirtyfourth-d3-papers.json")
thirtyfourth_notes = load("data/interspeech-2025-thirtyfourth-d3-notes.json")
thirtyfourth_claims = load("data/interspeech-2025-thirtyfourth-claim-ledger.json")
thirtyfifth_papers = load("data/interspeech-2025-thirtyfifth-d3-papers.json")
thirtyfifth_notes = load("data/interspeech-2025-thirtyfifth-d3-notes.json")
thirtyfifth_claims = load("data/interspeech-2025-thirtyfifth-claim-ledger.json")
thirtysixth_papers = load("data/interspeech-2025-thirtysixth-d3-papers.json")
thirtysixth_notes = load("data/interspeech-2025-thirtysixth-d3-notes.json")
thirtysixth_claims = load("data/interspeech-2025-thirtysixth-claim-ledger.json")
thirtyseventh_papers = load("data/interspeech-2025-thirtyseventh-d3-papers.json")
thirtyseventh_notes = load("data/interspeech-2025-thirtyseventh-d3-notes.json")
thirtyseventh_claims = load("data/interspeech-2025-thirtyseventh-claim-ledger.json")
thirtyeighth_papers = load("data/interspeech-2025-thirtyeighth-d3-papers.json")
thirtyeighth_notes = load("data/interspeech-2025-thirtyeighth-d3-notes.json")
thirtyeighth_claims = load("data/interspeech-2025-thirtyeighth-claim-ledger.json")
thirtyninth_papers = load("data/interspeech-2025-thirtyninth-d3-papers.json")
thirtyninth_notes = load("data/interspeech-2025-thirtyninth-d3-notes.json")
thirtyninth_claims = load("data/interspeech-2025-thirtyninth-claim-ledger.json")
fortieth_papers = load("data/interspeech-2025-fortieth-d3-papers.json")
fortieth_notes = load("data/interspeech-2025-fortieth-d3-notes.json")
fortieth_claims = load("data/interspeech-2025-fortieth-claim-ledger.json")
fortyfirst_papers = load("data/interspeech-2025-fortyfirst-d3-papers.json")
fortyfirst_notes = load("data/interspeech-2025-fortyfirst-d3-notes.json")
fortyfirst_claims = load("data/interspeech-2025-fortyfirst-claim-ledger.json")
fortysecond_papers = load("data/interspeech-2025-fortysecond-d3-papers.json")
fortysecond_notes = load("data/interspeech-2025-fortysecond-d3-notes.json")
fortysecond_claims = load("data/interspeech-2025-fortysecond-claim-ledger.json")
fortythird_papers = load("data/interspeech-2025-fortythird-d3-papers.json")
fortythird_notes = load("data/interspeech-2025-fortythird-d3-notes.json")
fortythird_claims = load("data/interspeech-2025-fortythird-claim-ledger.json")
fortyfourth_papers = load("data/interspeech-2025-fortyfourth-d3-papers.json")
fortyfourth_notes = load("data/interspeech-2025-fortyfourth-d3-notes.json")
fortyfourth_claims = load("data/interspeech-2025-fortyfourth-claim-ledger.json")
fortyfifth_papers = load("data/interspeech-2025-fortyfifth-d3-papers.json")
fortyfifth_notes = load("data/interspeech-2025-fortyfifth-d3-notes.json")
fortyfifth_claims = load("data/interspeech-2025-fortyfifth-claim-ledger.json")
fortysixth_papers = load("data/interspeech-2025-fortysixth-d3-papers.json")
fortysixth_notes = load("data/interspeech-2025-fortysixth-d3-notes.json")
fortysixth_claims = load("data/interspeech-2025-fortysixth-claim-ledger.json")
fortyseventh_papers = load("data/interspeech-2025-fortyseventh-d3-papers.json")
fortyseventh_notes = load("data/interspeech-2025-fortyseventh-d3-notes.json")
fortyseventh_claims = load("data/interspeech-2025-fortyseventh-claim-ledger.json")
fortyeighth_papers = load("data/interspeech-2025-fortyeighth-d3-papers.json")
fortyeighth_notes = load("data/interspeech-2025-fortyeighth-d3-notes.json")
fortyeighth_claims = load("data/interspeech-2025-fortyeighth-claim-ledger.json")
fortyninth_papers = load("data/interspeech-2025-fortyninth-d3-papers.json")
fortyninth_notes = load("data/interspeech-2025-fortyninth-d3-notes.json")
fortyninth_claims = load("data/interspeech-2025-fortyninth-claim-ledger.json")
fiftieth_papers = load("data/interspeech-2025-fiftieth-d3-papers.json")
fiftieth_notes = load("data/interspeech-2025-fiftieth-d3-notes.json")
fiftieth_claims = load("data/interspeech-2025-fiftieth-claim-ledger.json")
fiftyfirst_papers = load("data/interspeech-2025-fiftyfirst-d3-papers.json")
fiftyfirst_notes = load("data/interspeech-2025-fiftyfirst-d3-notes.json")
fiftyfirst_claims = load("data/interspeech-2025-fiftyfirst-claim-ledger.json")
fiftysecond_papers = load("data/interspeech-2025-fiftysecond-d3-papers.json")
fiftysecond_notes = load("data/interspeech-2025-fiftysecond-d3-notes.json")
fiftysecond_claims = load("data/interspeech-2025-fiftysecond-claim-ledger.json")
fiftythird_papers = load("data/interspeech-2025-fiftythird-d3-papers.json")
fiftythird_notes = load("data/interspeech-2025-fiftythird-d3-notes.json")
fiftythird_claims = load("data/interspeech-2025-fiftythird-claim-ledger.json")
fiftyfourth_papers = load("data/interspeech-2025-fiftyfourth-d3-papers.json")
fiftyfourth_notes = load("data/interspeech-2025-fiftyfourth-d3-notes.json")
fiftyfourth_claims = load("data/interspeech-2025-fiftyfourth-claim-ledger.json")
fiftyfifth_papers = load("data/interspeech-2025-fiftyfifth-d3-papers.json")
fiftyfifth_notes = load("data/interspeech-2025-fiftyfifth-d3-notes.json")
fiftyfifth_claims = load("data/interspeech-2025-fiftyfifth-claim-ledger.json")
fiftysixth_papers = load("data/interspeech-2025-fiftysixth-d3-papers.json")
fiftysixth_notes = load("data/interspeech-2025-fiftysixth-d3-notes.json")
fiftysixth_claims = load("data/interspeech-2025-fiftysixth-claim-ledger.json")
fiftyseventh_papers = load("data/interspeech-2025-fiftyseventh-d3-papers.json")
fiftyseventh_notes = load("data/interspeech-2025-fiftyseventh-d3-notes.json")
fiftyseventh_claims = load("data/interspeech-2025-fiftyseventh-claim-ledger.json")
fiftyeighth_papers = load("data/interspeech-2025-fiftyeighth-d3-papers.json")
fiftyeighth_notes = load("data/interspeech-2025-fiftyeighth-d3-notes.json")
fiftyeighth_claims = load("data/interspeech-2025-fiftyeighth-claim-ledger.json")
fiftyninth_papers = load("data/interspeech-2025-fiftyninth-d3-papers.json")
fiftyninth_notes = load("data/interspeech-2025-fiftyninth-d3-notes.json")
fiftyninth_claims = load("data/interspeech-2025-fiftyninth-claim-ledger.json")
sixtieth_papers = load("data/interspeech-2025-sixtieth-d3-papers.json")
sixtieth_notes = load("data/interspeech-2025-sixtieth-d3-notes.json")
sixtieth_claims = load("data/interspeech-2025-sixtieth-claim-ledger.json")
sixtyfirst_papers = load("data/interspeech-2025-sixtyfirst-d3-papers.json")
sixtyfirst_notes = load("data/interspeech-2025-sixtyfirst-d3-notes.json")
sixtyfirst_claims = load("data/interspeech-2025-sixtyfirst-claim-ledger.json")
sixtysecond_papers = load("data/interspeech-2025-sixtysecond-d3-papers.json")
sixtysecond_notes = load("data/interspeech-2025-sixtysecond-d3-notes.json")
sixtysecond_claims = load("data/interspeech-2025-sixtysecond-claim-ledger.json")
sixtythird_papers = load("data/interspeech-2025-sixtythird-d3-papers.json")
sixtythird_notes = load("data/interspeech-2025-sixtythird-d3-notes.json")
sixtythird_claims = load("data/interspeech-2025-sixtythird-claim-ledger.json")
fiftyeighth_papers = load("data/interspeech-2025-fiftyeighth-d3-papers.json")
fiftyeighth_notes = load("data/interspeech-2025-fiftyeighth-d3-notes.json")
fiftyeighth_claims = load("data/interspeech-2025-fiftyeighth-claim-ledger.json")
third_papers = load("data/interspeech-2025-third-d3-papers.json")
fourth_papers = load("data/interspeech-2025-fourth-d3-papers.json")
fifth_papers = load("data/interspeech-2025-fifth-d3-papers.json")
eleventh_papers = load("data/interspeech-2025-eleventh-d3-papers.json")
d3_paper_payloads = [representatives, second_papers, third_papers, fourth_papers, fifth_papers, sixth_papers, seventh_papers, eighth_papers, ninth_papers, tenth_papers, eleventh_papers, twelfth_papers, thirteenth_papers, fourteenth_papers, fifteenth_papers, sixteenth_papers, seventeenth_papers, eighteenth_papers, nineteenth_papers, twentieth_papers, twentyfirst_papers, twentisecond_papers, twentythird_papers, twentyfourth_papers, twentyfifth_papers, twentysixth_papers, twentyseventh_papers, twentyeighth_papers, twentyninth_papers, thirtieth_papers, thirtyfirst_papers, thirtysecond_papers, thirtythird_papers, thirtyfourth_papers, thirtyfifth_papers, thirtysixth_papers, thirtyseventh_papers, thirtyeighth_papers, thirtyninth_papers, fortieth_papers, fortyfirst_papers, fortysecond_papers, fortythird_papers, fortyfourth_papers, fortyfifth_papers, fortysixth_papers, fortyseventh_papers, fortyeighth_papers, fortyninth_papers, fiftieth_papers, fiftyfirst_papers, fiftysecond_papers, fiftythird_papers, fiftyfourth_papers, fiftyfifth_papers, fiftysixth_papers, fiftyseventh_papers, fiftyeighth_papers, fiftyninth_papers, sixtieth_papers, sixtyfirst_papers, sixtysecond_papers, sixtythird_papers]
d3_paper_ids = {row.get("paper_id") for payload in d3_paper_payloads for row in (payload or {}).get("papers", [])}
eleventh_papers = load("data/interspeech-2025-eleventh-d3-papers.json")
eleventh_notes = load("data/interspeech-2025-eleventh-d3-notes.json")
eleventh_claims = load("data/interspeech-2025-eleventh-claim-ledger.json")
if papers and themes:
    rows = papers.get("papers", [])
    ids = [row.get("paper_id") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("paper IDs are not unique")
    if papers.get("n_papers") != len(rows):
        errors.append("paper count mismatch")
    if papers.get("source_failures") != 0:
        errors.append("official source failures remain")
    if any(not row.get("title") or not row.get("paper_url") for row in rows):
        errors.append("paper is missing title or source URL")
    if any(row.get("source") != "official-isca-archive" for row in rows):
        errors.append("paper has non-official source label")
    if any(row.get("evidence_depth") != "D2" for row in rows):
        errors.append("not every captured paper has abstract evidence")
    theme_ids = {item.get("id") for item in themes.get("taxonomy", [])}
    for row in rows:
        unknown = set(row.get("conceptual_themes", [])) - theme_ids
        if unknown:
            errors.append(f"{row.get('paper_id')} has unknown themes: {sorted(unknown)}")
            break
    if themes.get("paper_count") != len(rows):
        errors.append("theme paper count mismatch")
    if themes.get("method", {}).get("unmatched_papers") != sum(not row.get("conceptual_themes") for row in rows):
        errors.append("unmatched-paper count mismatch")

if representatives and d3_notes:
    rep_rows = representatives.get("papers", [])
    note_rows = d3_notes.get("notes", [])
    if len(rep_rows) != 8 or len(note_rows) != len(rep_rows):
        errors.append("representative D3 set must contain eight aligned papers")
    rep_ids = {row.get("paper_id") for row in rep_rows}
    if rep_ids != {row.get("paper_id") for row in note_rows}:
        errors.append("D3 notes do not align with captured representative papers")
    required = {"bp", "wh", "naive", "ap", "mech", "math", "dots", "ww", "limits"}
    for row in note_rows:
        if set(row) < required:
            errors.append(f"D3 note incomplete: {row.get('paper_id')}")
            break
    if any(row.get("evidence_depth") != "D3" for row in rep_rows):
        errors.append("representative paper missing D3 evidence depth")

if representatives and artifact_ledger:
    rep_ids = {row.get("paper_id") for payload in d3_paper_payloads for row in (payload or {}).get("papers", [])}
    ledger_ids = set(artifact_ledger.get("papers_with_links", []))
    if not ledger_ids <= rep_ids:
        errors.append("artifact ledger contains paper outside representative set")
    for row in artifact_ledger.get("rows", []):
        if row.get("execution_status") != "not-attempted":
            errors.append("artifact ledger execution boundary changed unexpectedly")
            break

if release_manifest:
    for artifact in release_manifest.get("artifacts", []):
        path = HERE / artifact.get("path", "")
        if not path.exists():
            errors.append(f"release manifest missing: {artifact.get('path')}")
            continue
        import hashlib
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != artifact.get("sha256"):
            errors.append(f"release hash mismatch: {artifact.get('path')}")
    if release_manifest.get("artifact_count") != len(release_manifest.get("artifacts", [])):
        errors.append("release manifest count mismatch")

if papers and representatives and review_queue:
    third_papers = load("data/interspeech-2025-third-d3-papers.json")
    fourth_papers = load("data/interspeech-2025-fourth-d3-papers.json")
    fifth_papers = load("data/interspeech-2025-fifth-d3-papers.json")
    expected = papers["n_papers"] - len(d3_paper_ids)
    if review_queue.get("queue_count") != expected:
        errors.append("review queue count mismatch")
    if review_queue.get("unresolved_count") != len(review_queue.get("rows", [])):
        errors.append("review queue unresolved count mismatch")
    if any(row.get("review_status") != "queued-for-full-paper-review" for row in review_queue.get("rows", [])):
        errors.append("review queue row missing unresolved status")

if second_papers and second_notes and second_claims:
    if len(second_papers.get("papers", [])) != 8 or len(second_notes.get("notes", [])) != 8:
        errors.append("second D3 set must contain eight papers and notes")
    if second_claims.get("claim_count") != len(second_claims.get("claims", [])) != 8:
        errors.append("second D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in second_claims.get("claims", [])):
        errors.append("second D3 claims overstate independent support")

if sixth_papers and sixth_notes and sixth_claims:
    if len(sixth_papers.get("papers", [])) != 4 or len(sixth_notes.get("notes", [])) != 4:
        errors.append("sixth D3 set must contain four papers and notes")
    if sixth_claims.get("claim_count") != len(sixth_claims.get("claims", [])) != 4:
        errors.append("sixth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in sixth_claims.get("claims", [])):
        errors.append("sixth D3 claims overstate independent support")

if seventh_papers and seventh_notes and seventh_claims:
    if len(seventh_papers.get("papers", [])) != 8 or len(seventh_notes.get("notes", [])) != 8:
        errors.append("seventh D3 set must contain eight papers and notes")
    if seventh_claims.get("claim_count") != len(seventh_claims.get("claims", [])) or seventh_claims.get("claim_count") != 8:
        errors.append("seventh D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in seventh_claims.get("claims", [])):
        errors.append("seventh D3 claims overstate independent support")

if eighth_papers and eighth_notes and eighth_claims:
    if len(eighth_papers.get("papers", [])) != 8 or len(eighth_notes.get("notes", [])) != 8:
        errors.append("eighth D3 set must contain eight papers and notes")
    if eighth_claims.get("claim_count") != len(eighth_claims.get("claims", [])) or eighth_claims.get("claim_count") != 8:
        errors.append("eighth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in eighth_claims.get("claims", [])):
        errors.append("eighth D3 claims overstate independent support")

if ninth_papers and ninth_notes and ninth_claims:
    if len(ninth_papers.get("papers", [])) != 8 or len(ninth_notes.get("notes", [])) != 8:
        errors.append("ninth D3 set must contain eight papers and notes")
    if ninth_claims.get("claim_count") != len(ninth_claims.get("claims", [])) or ninth_claims.get("claim_count") != 8:
        errors.append("ninth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in ninth_claims.get("claims", [])):
        errors.append("ninth D3 claims overstate independent support")

if tenth_papers and tenth_notes and tenth_claims:
    if len(tenth_papers.get("papers", [])) != 8 or len(tenth_notes.get("notes", [])) != 8:
        errors.append("tenth D3 set must contain eight papers and notes")
    if tenth_claims.get("claim_count") != len(tenth_claims.get("claims", [])) or tenth_claims.get("claim_count") != 8:
        errors.append("tenth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in tenth_claims.get("claims", [])):
        errors.append("tenth D3 claims overstate independent support")

if eleventh_papers and eleventh_notes and eleventh_claims:
    if len(eleventh_papers.get("papers", [])) != 8 or len(eleventh_notes.get("notes", [])) != 8:
        errors.append("eleventh D3 set must contain eight papers and notes")
    if eleventh_claims.get("claim_count") != len(eleventh_claims.get("claims", [])) or eleventh_claims.get("claim_count") != 8:
        errors.append("eleventh D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in eleventh_claims.get("claims", [])):
        errors.append("eleventh D3 claims overstate independent support")

if twelfth_papers and twelfth_notes and twelfth_claims:
    if len(twelfth_papers.get("papers", [])) != 8 or len(twelfth_notes.get("notes", [])) != 8:
        errors.append("twelfth D3 set must contain eight papers and notes")
    if twelfth_claims.get("claim_count") != len(twelfth_claims.get("claims", [])) or twelfth_claims.get("claim_count") != 8:
        errors.append("twelfth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twelfth_claims.get("claims", [])):
        errors.append("twelfth D3 claims overstate independent support")

if thirteenth_papers and thirteenth_notes and thirteenth_claims:
    if len(thirteenth_papers.get("papers", [])) != 3 or len(thirteenth_notes.get("notes", [])) != 3:
        errors.append("thirteenth D3 set must contain three papers and notes")
    if thirteenth_claims.get("claim_count") != len(thirteenth_claims.get("claims", [])) or thirteenth_claims.get("claim_count") != 3:
        errors.append("thirteenth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirteenth_claims.get("claims", [])):
        errors.append("thirteenth D3 claims overstate independent support")

if fourteenth_papers and fourteenth_notes and fourteenth_claims:
    if len(fourteenth_papers.get("papers", [])) != 2 or len(fourteenth_notes.get("notes", [])) != 2:
        errors.append("fourteenth D3 set must contain two papers and notes")
    if fourteenth_claims.get("claim_count") != len(fourteenth_claims.get("claims", [])) or fourteenth_claims.get("claim_count") != 2:
        errors.append("fourteenth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fourteenth_claims.get("claims", [])):
        errors.append("fourteenth D3 claims overstate independent support")

if fifteenth_papers and fifteenth_notes and fifteenth_claims:
    if len(fifteenth_papers.get("papers", [])) != 8 or len(fifteenth_notes.get("notes", [])) != 8:
        errors.append("fifteenth D3 set must contain eight papers and notes")
    if fifteenth_claims.get("claim_count") != len(fifteenth_claims.get("claims", [])) or fifteenth_claims.get("claim_count") != 8:
        errors.append("fifteenth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fifteenth_claims.get("claims", [])):
        errors.append("fifteenth D3 claims overstate independent support")

if sixteenth_papers and sixteenth_notes and sixteenth_claims:
    if len(sixteenth_papers.get("papers", [])) != 1 or len(sixteenth_notes.get("notes", [])) != 1:
        errors.append("sixteenth D3 set must contain one paper and note")
    if sixteenth_claims.get("claim_count") != len(sixteenth_claims.get("claims", [])) or sixteenth_claims.get("claim_count") != 1:
        errors.append("sixteenth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in sixteenth_claims.get("claims", [])):
        errors.append("sixteenth D3 claims overstate independent support")

if eighteenth_papers and eighteenth_notes and eighteenth_claims:
    if len(eighteenth_papers.get("papers", [])) != 24 or len(eighteenth_notes.get("notes", [])) != 24:
        errors.append("eighteenth D3 set must contain 24 papers and notes")
    if eighteenth_claims.get("claim_count") != len(eighteenth_claims.get("claims", [])) or eighteenth_claims.get("claim_count") != 24:
        errors.append("eighteenth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in eighteenth_claims.get("claims", [])):
        errors.append("eighteenth D3 claims overstate independent support")

if nineteenth_papers and nineteenth_notes and nineteenth_claims:
    if len(nineteenth_papers.get("papers", [])) != 24 or len(nineteenth_notes.get("notes", [])) != 24:
        errors.append("nineteenth D3 set must contain 24 papers and notes")
    if nineteenth_claims.get("claim_count") != len(nineteenth_claims.get("claims", [])) or nineteenth_claims.get("claim_count") != 24:
        errors.append("nineteenth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in nineteenth_claims.get("claims", [])):
        errors.append("nineteenth D3 claims overstate independent support")

if twentieth_papers and twentieth_notes and twentieth_claims:
    if len(twentieth_papers.get("papers", [])) != 8 or len(twentieth_notes.get("notes", [])) != 8:
        errors.append("twentieth D3 set must contain 8 papers and notes")
    if twentieth_claims.get("claim_count") != len(twentieth_claims.get("claims", [])) or twentieth_claims.get("claim_count") != 8:
        errors.append("twentieth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentieth_claims.get("claims", [])):
        errors.append("twentieth D3 claims overstate independent support")

if twentyfirst_papers and twentyfirst_notes and twentyfirst_claims:
    if len(twentyfirst_papers.get("papers", [])) != 8 or len(twentyfirst_notes.get("notes", [])) != 8:
        errors.append("twenty-first D3 set must contain 8 papers and notes")
    if twentyfirst_claims.get("claim_count") != len(twentyfirst_claims.get("claims", [])) or twentyfirst_claims.get("claim_count") != 8:
        errors.append("twenty-first D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentyfirst_claims.get("claims", [])):
        errors.append("twenty-first D3 claims overstate independent support")

if twentisecond_papers and twentisecond_notes and twentisecond_claims:
    if len(twentisecond_papers.get("papers", [])) != 8 or len(twentisecond_notes.get("notes", [])) != 8:
        errors.append("twenty-second D3 set must contain 8 papers and notes")
    if twentisecond_claims.get("claim_count") != len(twentisecond_claims.get("claims", [])) or twentisecond_claims.get("claim_count") != 8:
        errors.append("twenty-second D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentisecond_claims.get("claims", [])):
        errors.append("twenty-second D3 claims overstate independent support")

if twentythird_papers and twentythird_notes and twentythird_claims:
    if len(twentythird_papers.get("papers", [])) != 8 or len(twentythird_notes.get("notes", [])) != 8:
        errors.append("twenty-third D3 set must contain 8 papers and notes")
    if twentythird_claims.get("claim_count") != len(twentythird_claims.get("claims", [])) or twentythird_claims.get("claim_count") != 8:
        errors.append("twenty-third D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentythird_claims.get("claims", [])):
        errors.append("twenty-third D3 claims overstate independent support")

if twentyfourth_papers and twentyfourth_notes and twentyfourth_claims:
    if len(twentyfourth_papers.get("papers", [])) != 8 or len(twentyfourth_notes.get("notes", [])) != 8:
        errors.append("twenty-fourth D3 set must contain 8 papers and notes")
    if twentyfourth_claims.get("claim_count") != len(twentyfourth_claims.get("claims", [])) or twentyfourth_claims.get("claim_count") != 8:
        errors.append("twenty-fourth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentyfourth_claims.get("claims", [])):
        errors.append("twenty-fourth D3 claims overstate independent support")

if twentyfifth_papers and twentyfifth_notes and twentyfifth_claims:
    if len(twentyfifth_papers.get("papers", [])) != 8 or len(twentyfifth_notes.get("notes", [])) != 8:
        errors.append("twenty-fifth D3 set must contain 8 papers and notes")
    if twentyfifth_claims.get("claim_count") != len(twentyfifth_claims.get("claims", [])) or twentyfifth_claims.get("claim_count") != 8:
        errors.append("twenty-fifth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentyfifth_claims.get("claims", [])):
        errors.append("twenty-fifth D3 claims overstate independent support")

if twentysixth_papers and twentysixth_notes and twentysixth_claims:
    if len(twentysixth_papers.get("papers", [])) != 8 or len(twentysixth_notes.get("notes", [])) != 8:
        errors.append("twenty-sixth D3 set must contain 8 papers and notes")
    if twentysixth_claims.get("claim_count") != len(twentysixth_claims.get("claims", [])) or twentysixth_claims.get("claim_count") != 8:
        errors.append("twenty-sixth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentysixth_claims.get("claims", [])):
        errors.append("twenty-sixth D3 claims overstate independent support")

if twentyseventh_papers and twentyseventh_notes and twentyseventh_claims:
    if len(twentyseventh_papers.get("papers", [])) != 6 or len(twentyseventh_notes.get("notes", [])) != 6:
        errors.append("twenty-seventh D3 set must contain 6 papers and notes")
    if twentyseventh_claims.get("claim_count") != len(twentyseventh_claims.get("claims", [])) or twentyseventh_claims.get("claim_count") != 6:
        errors.append("twenty-seventh D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentyseventh_claims.get("claims", [])):
        errors.append("twenty-seventh D3 claims overstate independent support")

if twentyeighth_papers and twentyeighth_notes and twentyeighth_claims:
    if len(twentyeighth_papers.get("papers", [])) != 8 or len(twentyeighth_notes.get("notes", [])) != 8:
        errors.append("twenty-eighth D3 set must contain 8 papers and notes")
    if twentyeighth_claims.get("claim_count") != len(twentyeighth_claims.get("claims", [])) or twentyeighth_claims.get("claim_count") != 8:
        errors.append("twenty-eighth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentyeighth_claims.get("claims", [])):
        errors.append("twenty-eighth D3 claims overstate independent support")

if twentyninth_papers and twentyninth_notes and twentyninth_claims:
    if len(twentyninth_papers.get("papers", [])) != 8 or len(twentyninth_notes.get("notes", [])) != 8:
        errors.append("twenty-ninth D3 set must contain 8 papers and notes")
    if twentyninth_claims.get("claim_count") != len(twentyninth_claims.get("claims", [])) or twentyninth_claims.get("claim_count") != 8:
        errors.append("twenty-ninth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in twentyninth_claims.get("claims", [])):
        errors.append("twenty-ninth D3 claims overstate independent support")

if thirtieth_papers and thirtieth_notes and thirtieth_claims:
    if len(thirtieth_papers.get("papers", [])) != 8 or len(thirtieth_notes.get("notes", [])) != 8:
        errors.append("thirtieth D3 set must contain 8 papers and notes")
    if thirtieth_claims.get("claim_count") != len(thirtieth_claims.get("claims", [])) or thirtieth_claims.get("claim_count") != 8:
        errors.append("thirtieth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtieth_claims.get("claims", [])):
        errors.append("thirtieth D3 claims overstate independent support")

if thirtyfirst_papers and thirtyfirst_notes and thirtyfirst_claims:
    if len(thirtyfirst_papers.get("papers", [])) != 8 or len(thirtyfirst_notes.get("notes", [])) != 8:
        errors.append("thirty-first D3 set must contain 8 papers and notes")
    if thirtyfirst_claims.get("claim_count") != len(thirtyfirst_claims.get("claims", [])) or thirtyfirst_claims.get("claim_count") != 8:
        errors.append("thirty-first D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtyfirst_claims.get("claims", [])):
        errors.append("thirty-first D3 claims overstate independent support")

if thirtysecond_papers and thirtysecond_notes and thirtysecond_claims:
    if len(thirtysecond_papers.get("papers", [])) != 8 or len(thirtysecond_notes.get("notes", [])) != 8:
        errors.append("thirty-second D3 set must contain 8 papers and notes")
    if thirtysecond_claims.get("claim_count") != len(thirtysecond_claims.get("claims", [])) or thirtysecond_claims.get("claim_count") != 8:
        errors.append("thirty-second D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtysecond_claims.get("claims", [])):
        errors.append("thirty-second D3 claims overstate independent support")

if thirtythird_papers and thirtythird_notes and thirtythird_claims:
    if len(thirtythird_papers.get("papers", [])) != 8 or len(thirtythird_notes.get("notes", [])) != 8:
        errors.append("thirty-third D3 set must contain 8 papers and notes")
    if thirtythird_claims.get("claim_count") != len(thirtythird_claims.get("claims", [])) or thirtythird_claims.get("claim_count") != 8:
        errors.append("thirty-third D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtythird_claims.get("claims", [])):
        errors.append("thirty-third D3 claims overstate independent support")

if thirtyfourth_papers and thirtyfourth_notes and thirtyfourth_claims:
    if len(thirtyfourth_papers.get("papers", [])) != 8 or len(thirtyfourth_notes.get("notes", [])) != 8:
        errors.append("thirty-fourth D3 set must contain 8 papers and notes")
    if thirtyfourth_claims.get("claim_count") != len(thirtyfourth_claims.get("claims", [])) or thirtyfourth_claims.get("claim_count") != 8:
        errors.append("thirty-fourth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtyfourth_claims.get("claims", [])):
        errors.append("thirty-fourth D3 claims overstate independent support")

if thirtyfifth_papers and thirtyfifth_notes and thirtyfifth_claims:
    if len(thirtyfifth_papers.get("papers", [])) != 8 or len(thirtyfifth_notes.get("notes", [])) != 8:
        errors.append("thirty-fifth D3 set must contain 8 papers and notes")
    if thirtyfifth_claims.get("claim_count") != len(thirtyfifth_claims.get("claims", [])) or thirtyfifth_claims.get("claim_count") != 8:
        errors.append("thirty-fifth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtyfifth_claims.get("claims", [])):
        errors.append("thirty-fifth D3 claims overstate independent support")

if thirtysixth_papers and thirtysixth_notes and thirtysixth_claims:
    if len(thirtysixth_papers.get("papers", [])) != 8 or len(thirtysixth_notes.get("notes", [])) != 8:
        errors.append("thirty-sixth D3 set must contain 8 papers and notes")
    if thirtysixth_claims.get("claim_count") != len(thirtysixth_claims.get("claims", [])) or thirtysixth_claims.get("claim_count") != 8:
        errors.append("thirty-sixth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtysixth_claims.get("claims", [])):
        errors.append("thirty-sixth D3 claims overstate independent support")

if thirtyseventh_papers and thirtyseventh_notes and thirtyseventh_claims:
    if len(thirtyseventh_papers.get("papers", [])) != 8 or len(thirtyseventh_notes.get("notes", [])) != 8:
        errors.append("thirty-seventh D3 set must contain 8 papers and notes")
    if thirtyseventh_claims.get("claim_count") != len(thirtyseventh_claims.get("claims", [])) or thirtyseventh_claims.get("claim_count") != 8:
        errors.append("thirty-seventh D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtyseventh_claims.get("claims", [])):
        errors.append("thirty-seventh D3 claims overstate independent support")

if thirtyeighth_papers and thirtyeighth_notes and thirtyeighth_claims:
    if len(thirtyeighth_papers.get("papers", [])) != 8 or len(thirtyeighth_notes.get("notes", [])) != 8:
        errors.append("thirty-eighth D3 set must contain 8 papers and notes")
    if thirtyeighth_claims.get("claim_count") != len(thirtyeighth_claims.get("claims", [])) or thirtyeighth_claims.get("claim_count") != 8:
        errors.append("thirty-eighth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtyeighth_claims.get("claims", [])):
        errors.append("thirty-eighth D3 claims overstate independent support")

if thirtyninth_papers and thirtyninth_notes and thirtyninth_claims:
    if len(thirtyninth_papers.get("papers", [])) != 8 or len(thirtyninth_notes.get("notes", [])) != 8:
        errors.append("thirty-ninth D3 set must contain 8 papers and notes")
    if thirtyninth_claims.get("claim_count") != len(thirtyninth_claims.get("claims", [])) or thirtyninth_claims.get("claim_count") != 8:
        errors.append("thirty-ninth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in thirtyninth_claims.get("claims", [])):
        errors.append("thirty-ninth D3 claims overstate independent support")

if fortieth_papers and fortieth_notes and fortieth_claims:
    if len(fortieth_papers.get("papers", [])) != 8 or len(fortieth_notes.get("notes", [])) != 8:
        errors.append("fortieth D3 set must contain 8 papers and notes")
    if fortieth_claims.get("claim_count") != len(fortieth_claims.get("claims", [])) or fortieth_claims.get("claim_count") != 8:
        errors.append("fortieth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortieth_claims.get("claims", [])):
        errors.append("fortieth D3 claims overstate independent support")

if fortyfirst_papers and fortyfirst_notes and fortyfirst_claims:
    if len(fortyfirst_papers.get("papers", [])) != 8 or len(fortyfirst_notes.get("notes", [])) != 8:
        errors.append("forty-first D3 set must contain 8 papers and notes")
    if fortyfirst_claims.get("claim_count") != len(fortyfirst_claims.get("claims", [])) or fortyfirst_claims.get("claim_count") != 8:
        errors.append("forty-first D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortyfirst_claims.get("claims", [])):
        errors.append("forty-first D3 claims overstate independent support")

if fortysecond_papers and fortysecond_notes and fortysecond_claims:
    if len(fortysecond_papers.get("papers", [])) != 8 or len(fortysecond_notes.get("notes", [])) != 8:
        errors.append("forty-second D3 set must contain 8 papers and notes")
    if fortysecond_claims.get("claim_count") != len(fortysecond_claims.get("claims", [])) or fortysecond_claims.get("claim_count") != 8:
        errors.append("forty-second D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortysecond_claims.get("claims", [])):
        errors.append("forty-second D3 claims overstate independent support")

if fortythird_papers and fortythird_notes and fortythird_claims:
    if len(fortythird_papers.get("papers", [])) != 8 or len(fortythird_notes.get("notes", [])) != 8:
        errors.append("forty-third D3 set must contain 8 papers and notes")
    if fortythird_claims.get("claim_count") != len(fortythird_claims.get("claims", [])) or fortythird_claims.get("claim_count") != 8:
        errors.append("forty-third D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortythird_claims.get("claims", [])):
        errors.append("forty-third D3 claims overstate independent support")

if fortyfourth_papers and fortyfourth_notes and fortyfourth_claims:
    if len(fortyfourth_papers.get("papers", [])) != 8 or len(fortyfourth_notes.get("notes", [])) != 8:
        errors.append("forty-fourth D3 set must contain 8 papers and notes")
    if fortyfourth_claims.get("claim_count") != len(fortyfourth_claims.get("claims", [])) or fortyfourth_claims.get("claim_count") != 8:
        errors.append("forty-fourth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortyfourth_claims.get("claims", [])):
        errors.append("forty-fourth D3 claims overstate independent support")

if fortyfifth_papers and fortyfifth_notes and fortyfifth_claims:
    if len(fortyfifth_papers.get("papers", [])) != 8 or len(fortyfifth_notes.get("notes", [])) != 8:
        errors.append("forty-fifth D3 set must contain 8 papers and notes")
    if fortyfifth_claims.get("claim_count") != len(fortyfifth_claims.get("claims", [])) or fortyfifth_claims.get("claim_count") != 8:
        errors.append("forty-fifth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortyfifth_claims.get("claims", [])):
        errors.append("forty-fifth D3 claims overstate independent support")

if fortysixth_papers and fortysixth_notes and fortysixth_claims:
    if len(fortysixth_papers.get("papers", [])) != 8 or len(fortysixth_notes.get("notes", [])) != 8:
        errors.append("forty-sixth D3 set must contain 8 papers and notes")
    if fortysixth_claims.get("claim_count") != len(fortysixth_claims.get("claims", [])) or fortysixth_claims.get("claim_count") != 8:
        errors.append("forty-sixth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortysixth_claims.get("claims", [])):
        errors.append("forty-sixth D3 claims overstate independent support")

if fortyseventh_papers and fortyseventh_notes and fortyseventh_claims:
    if len(fortyseventh_papers.get("papers", [])) != 8 or len(fortyseventh_notes.get("notes", [])) != 8:
        errors.append("forty-seventh D3 set must contain 8 papers and notes")
    if fortyseventh_claims.get("claim_count") != len(fortyseventh_claims.get("claims", [])) or fortyseventh_claims.get("claim_count") != 8:
        errors.append("forty-seventh D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortyseventh_claims.get("claims", [])):
        errors.append("forty-seventh D3 claims overstate independent support")

if fortyeighth_papers and fortyeighth_notes and fortyeighth_claims:
    if len(fortyeighth_papers.get("papers", [])) != 8 or len(fortyeighth_notes.get("notes", [])) != 8:
        errors.append("forty-eighth D3 set must contain 8 papers and notes")
    if fortyeighth_claims.get("claim_count") != len(fortyeighth_claims.get("claims", [])) or fortyeighth_claims.get("claim_count") != 8:
        errors.append("forty-eighth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortyeighth_claims.get("claims", [])):
        errors.append("forty-eighth D3 claims overstate independent support")

if fortyninth_papers and fortyninth_notes and fortyninth_claims:
    if len(fortyninth_papers.get("papers", [])) != 8 or len(fortyninth_notes.get("notes", [])) != 8:
        errors.append("forty-ninth D3 set must contain 8 papers and notes")
    if fortyninth_claims.get("claim_count") != len(fortyninth_claims.get("claims", [])) or fortyninth_claims.get("claim_count") != 8:
        errors.append("forty-ninth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fortyninth_claims.get("claims", [])):
        errors.append("forty-ninth D3 claims overstate independent support")

if fiftieth_papers and fiftieth_notes and fiftieth_claims:
    if len(fiftieth_papers.get("papers", [])) != 8 or len(fiftieth_notes.get("notes", [])) != 8:
        errors.append("fiftieth D3 set must contain 8 papers and notes")
    if fiftieth_claims.get("claim_count") != len(fiftieth_claims.get("claims", [])) or fiftieth_claims.get("claim_count") != 8:
        errors.append("fiftieth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftieth_claims.get("claims", [])):
        errors.append("fiftieth D3 claims overstate independent support")

if fiftyfirst_papers and fiftyfirst_notes and fiftyfirst_claims:
    if len(fiftyfirst_papers.get("papers", [])) != 8 or len(fiftyfirst_notes.get("notes", [])) != 8:
        errors.append("fifty-first D3 set must contain 8 papers and notes")
    if fiftyfirst_claims.get("claim_count") != len(fiftyfirst_claims.get("claims", [])) or fiftyfirst_claims.get("claim_count") != 8:
        errors.append("fifty-first D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftyfirst_claims.get("claims", [])):
        errors.append("fifty-first D3 claims overstate independent support")

if fiftysecond_papers and fiftysecond_notes and fiftysecond_claims:
    if len(fiftysecond_papers.get("papers", [])) != 8 or len(fiftysecond_notes.get("notes", [])) != 8:
        errors.append("fifty-second D3 set must contain 8 papers and notes")
    if fiftysecond_claims.get("claim_count") != len(fiftysecond_claims.get("claims", [])) or fiftysecond_claims.get("claim_count") != 8:
        errors.append("fifty-second D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftysecond_claims.get("claims", [])):
        errors.append("fifty-second D3 claims overstate independent support")

if fiftythird_papers and fiftythird_notes and fiftythird_claims:
    if len(fiftythird_papers.get("papers", [])) != 8 or len(fiftythird_notes.get("notes", [])) != 8:
        errors.append("fifty-third D3 set must contain 8 papers and notes")
    if fiftythird_claims.get("claim_count") != len(fiftythird_claims.get("claims", [])) or fiftythird_claims.get("claim_count") != 8:
        errors.append("fifty-third D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftythird_claims.get("claims", [])):
        errors.append("fifty-third D3 claims overstate independent support")

if fiftyfourth_papers and fiftyfourth_notes and fiftyfourth_claims:
    if len(fiftyfourth_papers.get("papers", [])) != 8 or len(fiftyfourth_notes.get("notes", [])) != 8:
        errors.append("fifty-fourth D3 set must contain 8 papers and notes")
    if fiftyfourth_claims.get("claim_count") != len(fiftyfourth_claims.get("claims", [])) or fiftyfourth_claims.get("claim_count") != 8:
        errors.append("fifty-fourth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftyfourth_claims.get("claims", [])):
        errors.append("fifty-fourth D3 claims overstate independent support")

if fiftyfifth_papers and fiftyfifth_notes and fiftyfifth_claims:
    if len(fiftyfifth_papers.get("papers", [])) != 8 or len(fiftyfifth_notes.get("notes", [])) != 8:
        errors.append("fifty-fifth D3 set must contain 8 papers and notes")
    if fiftyfifth_claims.get("claim_count") != len(fiftyfifth_claims.get("claims", [])) or fiftyfifth_claims.get("claim_count") != 8:
        errors.append("fifty-fifth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftyfifth_claims.get("claims", [])):
        errors.append("fifty-fifth D3 claims overstate independent support")

if fiftysixth_papers and fiftysixth_notes and fiftysixth_claims:
    if len(fiftysixth_papers.get("papers", [])) != 8 or len(fiftysixth_notes.get("notes", [])) != 8:
        errors.append("fifty-sixth D3 set must contain 8 papers and notes")
    if fiftysixth_claims.get("claim_count") != len(fiftysixth_claims.get("claims", [])) or fiftysixth_claims.get("claim_count") != 8:
        errors.append("fifty-sixth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftysixth_claims.get("claims", [])):
        errors.append("fifty-sixth D3 claims overstate independent support")

if fiftyseventh_papers and fiftyseventh_notes and fiftyseventh_claims:
    if len(fiftyseventh_papers.get("papers", [])) != 8 or len(fiftyseventh_notes.get("notes", [])) != 8:
        errors.append("fifty-seventh D3 set must contain 8 papers and notes")
    if fiftyseventh_claims.get("claim_count") != len(fiftyseventh_claims.get("claims", [])) or fiftyseventh_claims.get("claim_count") != 8:
        errors.append("fifty-seventh D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftyseventh_claims.get("claims", [])):
        errors.append("fifty-seventh D3 claims overstate independent support")

if fiftyeighth_papers and fiftyeighth_notes and fiftyeighth_claims:
    if len(fiftyeighth_papers.get("papers", [])) != 8 or len(fiftyeighth_notes.get("notes", [])) != 8:
        errors.append("fifty-eighth D3 set must contain 8 papers and notes")
    if fiftyeighth_claims.get("claim_count") != len(fiftyeighth_claims.get("claims", [])) or fiftyeighth_claims.get("claim_count") != 8:
        errors.append("fifty-eighth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftyeighth_claims.get("claims", [])):
        errors.append("fifty-eighth D3 claims overstate independent support")

if fiftyninth_papers and fiftyninth_notes and fiftyninth_claims:
    if len(fiftyninth_papers.get("papers", [])) != 9 or len(fiftyninth_notes.get("notes", [])) != 9:
        errors.append("fifty-ninth D3 set must contain 9 papers and notes")
    if fiftyninth_claims.get("claim_count") != len(fiftyninth_claims.get("claims", [])) or fiftyninth_claims.get("claim_count") != 9:
        errors.append("fifty-ninth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in fiftyninth_claims.get("claims", [])):
        errors.append("fifty-ninth D3 claims overstate independent support")

if sixtieth_papers and sixtieth_notes and sixtieth_claims:
    if len(sixtieth_papers.get("papers", [])) != 3 or len(sixtieth_notes.get("notes", [])) != 3:
        errors.append("sixtieth D3 set must contain 3 papers and notes")
    if sixtieth_claims.get("claim_count") != len(sixtieth_claims.get("claims", [])) or sixtieth_claims.get("claim_count") != 3:
        errors.append("sixtieth D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in sixtieth_claims.get("claims", [])):
        errors.append("sixtieth D3 claims overstate independent support")

if sixtyfirst_papers and sixtyfirst_notes and sixtyfirst_claims:
    if len(sixtyfirst_papers.get("papers", [])) != 3 or len(sixtyfirst_notes.get("notes", [])) != 3:
        errors.append("sixty-first D3 set must contain 3 papers and notes")
    if sixtyfirst_claims.get("claim_count") != len(sixtyfirst_claims.get("claims", [])) or sixtyfirst_claims.get("claim_count") != 3:
        errors.append("sixty-first D3 claim count mismatch")
    if any(row.get("independent_support_status") != "not-established" for row in sixtyfirst_claims.get("claims", [])):
        errors.append("sixty-first D3 claims overstate independent support")

if execution_audit:
    if not execution_audit.get("records"):
        errors.append("execution audit has no records")
    if any(row.get("execution_status") != "not-attempted" for row in execution_audit.get("records", [])):
        errors.append("execution audit overstates artifact execution")

if papers:
    if len(paper_evidence) != papers.get("n_papers"):
        errors.append("paper evidence record count mismatch")
    if len({row.get("paper_id") for row in paper_evidence}) != len(paper_evidence):
        errors.append("paper evidence IDs are not unique")
    evidence_counts = Counter(row.get("evidence_depth") for row in paper_evidence)
    expected_d3 = len(d3_paper_ids)
    if evidence_counts.get("D3") != expected_d3 or evidence_counts.get("D2") != papers.get("n_papers") - expected_d3:
        errors.append(f"paper evidence depth counts mismatch: {dict(evidence_counts)}")
    if any(row.get("artifact_execution_status") != "not-attempted" for row in paper_evidence):
        errors.append("paper evidence overstates artifact execution")
    required_evidence_fields = {"bp", "wh", "naive", "ap", "mech", "math", "dots", "eval", "ww", "po", "limits", "source", "depth"}
    if any(set(row) < required_evidence_fields for row in paper_evidence):
        errors.append("canonical paper evidence row is missing first-principles fields")
    if any("evaluation_audit" not in row for row in paper_evidence):
        errors.append("canonical paper evidence row is missing evaluation audit")

if papers:
    if len(evaluation_rows) != papers.get("n_papers") or len({row.get("paper_id") for row in evaluation_rows}) != len(evaluation_rows):
        errors.append("evaluation audit count or IDs mismatch")
    required_eval = {"task", "metrics_or_measures", "denominator_or_dataset", "target_or_proxy", "claim_boundary"}
    if any(set(row) < required_eval for row in evaluation_rows):
        errors.append("evaluation audit row is incomplete")

if icassp_source_manifest:
    icassp_path = HERE / "data/icassp-2026-papers.json"
    import hashlib
    if icassp_source_manifest.get("input_sha256") != hashlib.sha256(icassp_path.read_bytes()).hexdigest():
        errors.append("ICASSP source manifest input hash mismatch")
    if not icassp_data or icassp_source_manifest.get("paper_count") != icassp_data.get("n_papers"):
        errors.append("ICASSP source manifest paper count invalid")

if taxonomy:
    themes_rows = taxonomy.get("themes", [])
    subthemes = [s for t in themes_rows for s in t.get("subthemes", [])]
    concepts = [c for s in subthemes for c in s.get("concepts", [])]
    canonical_triples = {
        (t.get("id"), s.get("id"), c.get("id"))
        for t in themes_rows
        for s in t.get("subthemes", [])
        for c in s.get("concepts", [])
    }
    if taxonomy.get("theme_count") != len(themes_rows) or taxonomy.get("subtheme_count") != len(subthemes) or taxonomy.get("concept_count") != len(concepts):
        errors.append("first-principles taxonomy count mismatch")
    if len(themes_rows) < 8 or any(len(t.get("subthemes", [])) < 3 for t in themes_rows) or any(len(s.get("concepts", [])) < 3 for s in subthemes):
        errors.append("first-principles taxonomy is structurally too shallow")
    required_concept = {"id", "name", "definition", "boundary"}
    if any(set(c) < required_concept for c in concepts):
        errors.append("first-principles concept is missing definition or boundary")

if semantic_queue and papers:
    if semantic_d2_batch_16:
        d2_rows = semantic_d2_batch_16.get("rows", [])
        if semantic_d2_batch_16.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 016 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 016 overstates or mislabels evidence")
    if semantic_d2_batch_17:
        d2_rows = semantic_d2_batch_17.get("rows", [])
        if semantic_d2_batch_17.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 017 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 017 overstates or mislabels evidence")
    if semantic_d2_batch_18:
        d2_rows = semantic_d2_batch_18.get("rows", [])
        if semantic_d2_batch_18.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 018 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 018 overstates or mislabels evidence")
    if semantic_d2_batch_19:
        d2_rows = semantic_d2_batch_19.get("rows", [])
        if semantic_d2_batch_19.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 019 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 019 overstates or mislabels evidence")
    if semantic_d2_batch_20:
        d2_rows = semantic_d2_batch_20.get("rows", [])
        if semantic_d2_batch_20.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 020 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 020 overstates or mislabels evidence")
    if semantic_d2_batch_21:
        d2_rows = semantic_d2_batch_21.get("rows", [])
        if semantic_d2_batch_21.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 021 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 021 overstates or mislabels evidence")
    if semantic_d2_batch_22:
        d2_rows = semantic_d2_batch_22.get("rows", [])
        if semantic_d2_batch_22.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 022 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 022 overstates or mislabels evidence")
    if semantic_d2_batch_23:
        d2_rows = semantic_d2_batch_23.get("rows", [])
        if semantic_d2_batch_23.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 023 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 023 overstates or mislabels evidence")
    if semantic_d2_batch_24:
        d2_rows = semantic_d2_batch_24.get("rows", [])
        if semantic_d2_batch_24.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 024 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 024 overstates or mislabels evidence")
    if semantic_d2_batch_25:
        d2_rows = semantic_d2_batch_25.get("rows", [])
        if semantic_d2_batch_25.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 025 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 025 overstates or mislabels evidence")
    if semantic_d2_batch_26:
        d2_rows = semantic_d2_batch_26.get("rows", [])
        if semantic_d2_batch_26.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 026 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 026 overstates or mislabels evidence")
    if semantic_d2_batch_27:
        d2_rows = semantic_d2_batch_27.get("rows", [])
        if semantic_d2_batch_27.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 027 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 027 overstates or mislabels evidence")
    if semantic_d2_batch_28:
        d2_rows = semantic_d2_batch_28.get("rows", [])
        if semantic_d2_batch_28.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 028 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 028 overstates or mislabels evidence")
    if semantic_d2_batch_29:
        d2_rows = semantic_d2_batch_29.get("rows", [])
        if semantic_d2_batch_29.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 029 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 029 overstates or mislabels evidence")
    if semantic_d2_batch_30:
        d2_rows = semantic_d2_batch_30.get("rows", [])
        if semantic_d2_batch_30.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 030 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 030 overstates or mislabels evidence")
    if semantic_d2_batch_31:
        d2_rows = semantic_d2_batch_31.get("rows", [])
        if semantic_d2_batch_31.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 031 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 031 overstates or mislabels evidence")
    if semantic_d2_batch_32:
        d2_rows = semantic_d2_batch_32.get("rows", [])
        if semantic_d2_batch_32.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 032 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 032 overstates or mislabels evidence")
    if semantic_d2_batch_33:
        d2_rows = semantic_d2_batch_33.get("rows", [])
        if semantic_d2_batch_33.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 033 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 033 overstates or mislabels evidence")
    if semantic_d2_batch_34:
        d2_rows = semantic_d2_batch_34.get("rows", [])
        if semantic_d2_batch_34.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 034 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 034 overstates or mislabels evidence")
    if semantic_d2_batch_35:
        d2_rows = semantic_d2_batch_35.get("rows", [])
        if semantic_d2_batch_35.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 035 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 035 overstates or mislabels evidence")
    if semantic_d2_batch_36:
        d2_rows = semantic_d2_batch_36.get("rows", [])
        if semantic_d2_batch_36.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 16:
            errors.append("semantic D2 batch 036 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 036 overstates or mislabels evidence")
    if semantic_d2_batch_37:
        d2_rows = semantic_d2_batch_37.get("rows", [])
        if semantic_d2_batch_37.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 10:
            errors.append("semantic D2 batch 037 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
            errors.append("semantic D2 batch 037 overstates or mislabels evidence")
    if semantic_d2_batch_38:
        d2_rows = semantic_d2_batch_38.get("rows", [])
        if semantic_d2_batch_38.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 26:
            errors.append("semantic D2 batch 038 count mismatch")
        if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" or row.get("decision") not in {"supported", "unsupported"} for row in d2_rows):
            errors.append("semantic D2 batch 038 overstates or mislabels evidence")
    if semantic_batch_26:
        batch_rows = semantic_batch_26.get("rows", [])
        if semantic_batch_26.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 31:
            errors.append("semantic batch 026 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") not in {"supported", "unsupported"} for row in batch_rows):
            errors.append("semantic batch 026 overstates or mislabels review")
    if semantic_out_scope_batch_38:
        out_scope_rows = semantic_out_scope_batch_38.get("rows", [])
        if semantic_out_scope_batch_38.get("reviewed_count") != len(out_scope_rows) or len(out_scope_rows) != 11:
            errors.append("semantic out-of-scope batch 038 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in out_scope_rows):
            errors.append("semantic out-of-scope batch 038 overstates or mislabels evidence")
    if semantic_provisional_batch_39:
        provisional_rows = semantic_provisional_batch_39.get("rows", [])
        if semantic_provisional_batch_39.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 039 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 039 overstates or mislabels evidence")
    if semantic_provisional_batch_40:
        provisional_rows = semantic_provisional_batch_40.get("rows", [])
        if semantic_provisional_batch_40.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 040 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 040 overstates or mislabels evidence")
    if semantic_provisional_batch_41:
        provisional_rows = semantic_provisional_batch_41.get("rows", [])
        if semantic_provisional_batch_41.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 041 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 041 overstates or mislabels evidence")
    if semantic_provisional_batch_42:
        provisional_rows = semantic_provisional_batch_42.get("rows", [])
        if semantic_provisional_batch_42.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 042 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 042 overstates or mislabels evidence")
    if semantic_provisional_batch_43:
        provisional_rows = semantic_provisional_batch_43.get("rows", [])
        if semantic_provisional_batch_43.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 043 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 043 overstates or mislabels evidence")
    if semantic_provisional_batch_44:
        provisional_rows = semantic_provisional_batch_44.get("rows", [])
        if semantic_provisional_batch_44.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 044 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 044 overstates or mislabels evidence")
    if semantic_provisional_batch_45:
        provisional_rows = semantic_provisional_batch_45.get("rows", [])
        if semantic_provisional_batch_45.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 045 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 045 overstates or mislabels evidence")
    if semantic_provisional_batch_46:
        provisional_rows = semantic_provisional_batch_46.get("rows", [])
        if semantic_provisional_batch_46.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 046 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 046 overstates or mislabels evidence")
    if semantic_provisional_batch_47:
        provisional_rows = semantic_provisional_batch_47.get("rows", [])
        if semantic_provisional_batch_47.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 047 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 047 overstates or mislabels evidence")
    if semantic_provisional_batch_48:
        provisional_rows = semantic_provisional_batch_48.get("rows", [])
        if semantic_provisional_batch_48.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 048 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 048 overstates or mislabels evidence")
    if semantic_provisional_batch_49:
        provisional_rows = semantic_provisional_batch_49.get("rows", [])
        if semantic_provisional_batch_49.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 049 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 049 overstates or mislabels evidence")
    if semantic_provisional_batch_50:
        provisional_rows = semantic_provisional_batch_50.get("rows", [])
        if semantic_provisional_batch_50.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 050 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 050 overstates or mislabels evidence")
    if semantic_provisional_batch_51:
        provisional_rows = semantic_provisional_batch_51.get("rows", [])
        if semantic_provisional_batch_51.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 051 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 051 overstates or mislabels evidence")
    if semantic_provisional_batch_52:
        provisional_rows = semantic_provisional_batch_52.get("rows", [])
        if semantic_provisional_batch_52.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 16:
            errors.append("semantic provisional batch 052 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 052 overstates or mislabels evidence")
    if semantic_provisional_batch_53:
        provisional_rows = semantic_provisional_batch_53.get("rows", [])
        if semantic_provisional_batch_53.get("reviewed_count") != len(provisional_rows) or len(provisional_rows) != 15:
            errors.append("semantic provisional batch 053 count mismatch")
        if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in provisional_rows):
            errors.append("semantic provisional batch 053 overstates or mislabels evidence")
    semantic_rows = semantic_queue.get("rows", [])
    if semantic_queue.get("paper_count") != len(semantic_rows) or semantic_queue.get("paper_count") != papers.get("n_papers"):
        errors.append("semantic review queue paper count mismatch")
    if len({row.get("paper_id") for row in semantic_rows}) != len(semantic_rows):
        errors.append("semantic review queue IDs are not unique")
    allowed = {"supported", "unsupported", "ambiguous", "insufficient-evidence"}
    if any(row.get("decision") not in allowed for row in semantic_rows):
        errors.append("semantic review queue contains invalid decision")
    if any(row.get("review_state") != "needs-analyst-semantic-review" for row in semantic_rows):
        expected_reviewed = {row.get("paper_id") for row in (semantic_batch or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_2 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_3 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_4 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_5 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_6 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_7 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_8 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_9 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_10 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_11 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_12 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_13 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_14 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_15 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_16 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d2_batch_17 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_2 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_3 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_4 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_5 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_6 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_7 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_8 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_9 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_10 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_11 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_12 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_13 or {}).get("rows", [])} | {row.get("paper_id") for row in (semantic_d3_batch_14 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_18 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_boundary_batch_25 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_19 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_20 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_21 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_22 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_23 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_24 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_25 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_26 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_27 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_28 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_29 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_30 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_31 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_32 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_33 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_34 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_35 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_36 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_37 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_d2_batch_38 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_batch_26 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_out_scope_batch_38 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_39 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_40 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_41 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_42 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_43 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_44 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_45 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_46 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_47 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_48 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_49 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_50 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_51 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_52 or {}).get("rows", [])}
        expected_reviewed |= {row.get("paper_id") for row in (semantic_provisional_batch_53 or {}).get("rows", [])}
        if any(row.get("review_state") not in {"needs-analyst-semantic-review", "analyst-reviewed"} for row in semantic_rows):
            errors.append("semantic review queue contains invalid review state")
        if {row.get("paper_id") for row in semantic_rows if row.get("review_state") == "analyst-reviewed"} != expected_reviewed:
            errors.append("semantic review queue reviewed batch mismatch")
        if any(
            row.get("review_state") == "analyst-reviewed"
            and row.get("decision") == "supported"
            and (reviewed := (row.get("analyst_review") or row))
            and (reviewed.get("theme_id"), reviewed.get("subtheme_id"), reviewed.get("concept_id")) not in canonical_triples
            for row in semantic_rows
        ):
            errors.append("INTERSPEECH reviewed assignment is outside the canonical taxonomy")

if papers:
    allowed_dispositions = {"analyst-confirmed", "analyst-rejected", "analyst-unresolved", "provisional-candidate", "unresolved"}
    if len(interspeech_assignments) != papers.get("n_papers") or len({row.get("paper_id") for row in interspeech_assignments}) != len(interspeech_assignments):
        errors.append("INTERSPEECH semantic assignment count or IDs mismatch")
    if any(row.get("semantic_disposition") not in allowed_dispositions for row in interspeech_assignments):
        errors.append("INTERSPEECH semantic assignment has invalid disposition")
    if any(row.get("semantic_disposition") in {"provisional-candidate", "unresolved", "analyst-unresolved"} and not row.get("unresolved_reason") for row in interspeech_assignments):
        errors.append("INTERSPEECH unresolved semantic assignment lacks a reason")

if icassp_semantic and icassp_data:
    rows = icassp_semantic.get("rows", [])
    if icassp_semantic.get("paper_count") != icassp_data.get("n_papers") or len(rows) != icassp_data.get("n_papers"):
        errors.append("ICASSP semantic queue paper count mismatch")
    if len({row.get("paper_id") for row in rows}) != len(rows):
        errors.append("ICASSP semantic queue IDs are not unique")
    if any(row.get("decision") not in {"supported", "unsupported", "ambiguous", "insufficient-evidence"} for row in rows):
        errors.append("ICASSP semantic queue contains invalid decision")
    if any(row.get("review_state") not in {"needs-analyst-semantic-review", "analyst-reviewed"} for row in rows):
        errors.append("ICASSP semantic queue contains invalid review state")
    if any(
        row.get("review_state") == "analyst-reviewed"
        and row.get("decision") == "supported"
        and (reviewed := (row.get("analyst_review") or row))
        and (reviewed.get("theme_id"), reviewed.get("subtheme_id"), reviewed.get("concept_id")) not in canonical_triples
        for row in rows
    ):
        errors.append("ICASSP reviewed assignment is outside the canonical taxonomy")
    expected_reviewed = {row.get("paper_id") for row in (icassp_semantic_batch or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_2 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_3 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_4 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_5 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_6 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_7 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_8 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_9 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_10 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_11 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_12 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_13 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_14 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_15 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_16 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_17 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_18 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_19 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_20 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_21 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_22 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_23 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_24 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_25 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_26 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_27 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_28 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_29 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_30 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_31 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_32 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_33 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_34 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_35 or {}).get("rows", [])} | {row.get("paper_id") for row in (icassp_semantic_batch_36 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_37 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_38 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_39 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_40 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_41 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_42 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_43 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_44 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_45 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_46 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_47 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_48 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_49 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_50 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_51 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_52 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_53 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_54 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_55 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_56 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_57 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_58 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_59 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_60 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_61 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_62 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_63 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_64 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_65 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_66 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_67 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_68 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_69 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_70 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_71 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_72 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_73 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_74 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_75 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_76 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_77 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_78 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_79 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_80 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_81 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_82 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_83 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_84 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_85 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_86 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_87 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_88 or {}).get("rows", [])}
    expected_reviewed |= {row.get("paper_id") for row in (icassp_semantic_batch_89 or {}).get("rows", [])}
    actual_reviewed = {row.get("paper_id") for row in rows if row.get("review_state") == "analyst-reviewed"}
    if actual_reviewed != expected_reviewed:
        errors.append("ICASSP semantic reviewed batch mismatch")
    allowed_dispositions = {"analyst-confirmed", "analyst-rejected", "analyst-unresolved", "provisional-candidate", "unresolved"}
    if len(icassp_assignments) != icassp_data.get("n_papers") or len({row.get("paper_id") for row in icassp_assignments}) != len(icassp_assignments):
        errors.append("ICASSP semantic assignment count or IDs mismatch")
    if any(row.get("semantic_disposition") not in allowed_dispositions for row in icassp_assignments):
        errors.append("ICASSP semantic assignment has invalid disposition")
    if any(row.get("semantic_disposition") in {"provisional-candidate", "unresolved", "analyst-unresolved"} and not row.get("unresolved_reason") for row in icassp_assignments):
        errors.append("ICASSP unresolved semantic assignment lacks a reason")
    reviewed_decisions = Counter(row.get("decision") for row in rows if row.get("review_state") == "analyst-reviewed")
    assignment_dispositions = Counter(row.get("semantic_disposition") for row in icassp_assignments)
    if assignment_dispositions.get("analyst-confirmed", 0) != reviewed_decisions.get("supported", 0) or assignment_dispositions.get("analyst-rejected", 0) != reviewed_decisions.get("unsupported", 0):
        errors.append("ICASSP corpus dispositions do not match reviewed queue decisions")

if icassp_semantic_batch:
    batch_rows = icassp_semantic_batch.get("rows", [])
    if icassp_semantic_batch.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in batch_rows):
        errors.append("ICASSP semantic batch overstates review")

if icassp_semantic_batch_2:
    batch_rows = icassp_semantic_batch_2.get("rows", [])
    if icassp_semantic_batch_2.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 002 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D2" for row in batch_rows):
        errors.append("ICASSP semantic batch 002 overstates review")

if icassp_semantic_batch_3:
    batch_rows = icassp_semantic_batch_3.get("rows", [])
    if icassp_semantic_batch_3.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 003 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D2" for row in batch_rows):
        errors.append("ICASSP semantic batch 003 overstates review")

if icassp_semantic_batch_4:
    batch_rows = icassp_semantic_batch_4.get("rows", [])
    if icassp_semantic_batch_4.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 004 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D2" for row in batch_rows):
        errors.append("ICASSP semantic batch 004 overstates review")

if icassp_semantic_batch_5:
    batch_rows = icassp_semantic_batch_5.get("rows", [])
    if icassp_semantic_batch_5.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 005 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D2" for row in batch_rows):
        errors.append("ICASSP semantic batch 005 overstates review")

if icassp_semantic_batch_6:
    batch_rows = icassp_semantic_batch_6.get("rows", [])
    if icassp_semantic_batch_6.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 006 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 006 overstates or mislabels review")

if icassp_semantic_batch_7:
    batch_rows = icassp_semantic_batch_7.get("rows", [])
    if icassp_semantic_batch_7.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 29:
        errors.append("ICASSP semantic batch 007 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 007 overstates or mislabels review")

if icassp_semantic_batch_8:
    batch_rows = icassp_semantic_batch_8.get("rows", [])
    if icassp_semantic_batch_8.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 008 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D2" for row in batch_rows):
        errors.append("ICASSP semantic batch 008 overstates or mislabels review")

if icassp_semantic_batch_9:
    batch_rows = icassp_semantic_batch_9.get("rows", [])
    if icassp_semantic_batch_9.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 009 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D2" for row in batch_rows):
        errors.append("ICASSP semantic batch 009 overstates or mislabels review")

if icassp_semantic_batch_10:
    batch_rows = icassp_semantic_batch_10.get("rows", [])
    if icassp_semantic_batch_10.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 010 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D2" for row in batch_rows):
        errors.append("ICASSP semantic batch 010 overstates or mislabels review")

if icassp_semantic_batch_11:
    batch_rows = icassp_semantic_batch_11.get("rows", [])
    if icassp_semantic_batch_11.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 011 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 011 overstates or mislabels review")

if icassp_semantic_batch_12:
    batch_rows = icassp_semantic_batch_12.get("rows", [])
    if icassp_semantic_batch_12.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 012 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 012 overstates or mislabels review")

if icassp_semantic_batch_13:
    batch_rows = icassp_semantic_batch_13.get("rows", [])
    if icassp_semantic_batch_13.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 013 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 013 overstates or mislabels review")

if icassp_semantic_batch_14:
    batch_rows = icassp_semantic_batch_14.get("rows", [])
    if icassp_semantic_batch_14.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 014 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 014 overstates or mislabels review")

if icassp_semantic_batch_15:
    batch_rows = icassp_semantic_batch_15.get("rows", [])
    if icassp_semantic_batch_15.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 015 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 015 overstates or mislabels review")

if icassp_semantic_batch_16:
    batch_rows = icassp_semantic_batch_16.get("rows", [])
    if icassp_semantic_batch_16.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 016 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") not in {"supported", "unsupported"} or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 016 overstates or mislabels review")

if icassp_semantic_batch_17:
    batch_rows = icassp_semantic_batch_17.get("rows", [])
    if icassp_semantic_batch_17.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 10:
        errors.append("ICASSP semantic batch 017 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") not in {"supported", "unsupported"} or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 017 overstates or mislabels review")

if icassp_semantic_batch_18:
    batch_rows = icassp_semantic_batch_18.get("rows", [])
    if icassp_semantic_batch_18.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 018 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 018 overstates or mislabels review")

if icassp_semantic_batch_19:
    batch_rows = icassp_semantic_batch_19.get("rows", [])
    if icassp_semantic_batch_19.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 019 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 019 overstates or mislabels review")

if icassp_semantic_batch_20:
    batch_rows = icassp_semantic_batch_20.get("rows", [])
    if icassp_semantic_batch_20.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 7:
        errors.append("ICASSP semantic batch 020 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 020 overstates or mislabels review")

if icassp_semantic_batch_21:
    batch_rows = icassp_semantic_batch_21.get("rows", [])
    if icassp_semantic_batch_21.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 021 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 021 overstates or mislabels review")

if icassp_semantic_batch_22:
    batch_rows = icassp_semantic_batch_22.get("rows", [])
    if icassp_semantic_batch_22.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 022 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 022 overstates or mislabels review")

if icassp_semantic_batch_23:
    batch_rows = icassp_semantic_batch_23.get("rows", [])
    if icassp_semantic_batch_23.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 023 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 023 overstates or mislabels review")

if icassp_semantic_batch_24:
    batch_rows = icassp_semantic_batch_24.get("rows", [])
    if icassp_semantic_batch_24.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 024 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 024 overstates or mislabels review")

if icassp_semantic_batch_25:
    batch_rows = icassp_semantic_batch_25.get("rows", [])
    if icassp_semantic_batch_25.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 025 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 025 overstates or mislabels review")

if icassp_semantic_batch_26:
    batch_rows = icassp_semantic_batch_26.get("rows", [])
    if icassp_semantic_batch_26.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 026 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 026 overstates or mislabels review")

if icassp_semantic_batch_27:
    batch_rows = icassp_semantic_batch_27.get("rows", [])
    if icassp_semantic_batch_27.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 027 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 027 overstates or mislabels review")

if icassp_semantic_batch_28:
    batch_rows = icassp_semantic_batch_28.get("rows", [])
    if icassp_semantic_batch_28.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 028 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 028 overstates or mislabels review")

if icassp_semantic_batch_29:
    batch_rows = icassp_semantic_batch_29.get("rows", [])
    if icassp_semantic_batch_29.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 029 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 029 overstates or mislabels review")

if icassp_semantic_batch_30:
    batch_rows = icassp_semantic_batch_30.get("rows", [])
    if icassp_semantic_batch_30.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 030 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 030 overstates or mislabels review")

if icassp_semantic_batch_31:
    batch_rows = icassp_semantic_batch_31.get("rows", [])
    if icassp_semantic_batch_31.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 031 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 031 overstates or mislabels review")

if icassp_semantic_batch_32:
    batch_rows = icassp_semantic_batch_32.get("rows", [])
    if icassp_semantic_batch_32.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 032 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 032 overstates or mislabels review")

if icassp_semantic_batch_33:
    batch_rows = icassp_semantic_batch_33.get("rows", [])
    if icassp_semantic_batch_33.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 033 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 033 overstates or mislabels review")

if icassp_semantic_batch_34:
    batch_rows = icassp_semantic_batch_34.get("rows", [])
    if icassp_semantic_batch_34.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 034 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 034 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 034 contains duplicate paper IDs")

if icassp_semantic_batch_35:
    batch_rows = icassp_semantic_batch_35.get("rows", [])
    if icassp_semantic_batch_35.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 035 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 035 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 035 contains duplicate paper IDs")

if icassp_semantic_batch_36:
    batch_rows = icassp_semantic_batch_36.get("rows", [])
    if icassp_semantic_batch_36.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 036 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 036 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 036 contains duplicate paper IDs")

if icassp_semantic_batch_37:
    batch_rows = icassp_semantic_batch_37.get("rows", [])
    if icassp_semantic_batch_37.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 037 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 037 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 037 contains duplicate paper IDs")

if icassp_semantic_batch_38:
    batch_rows = icassp_semantic_batch_38.get("rows", [])
    if icassp_semantic_batch_38.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 038 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 038 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 038 contains duplicate paper IDs")

if icassp_semantic_batch_39:
    batch_rows = icassp_semantic_batch_39.get("rows", [])
    if icassp_semantic_batch_39.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 039 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 039 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 039 contains duplicate paper IDs")

if icassp_semantic_batch_40:
    batch_rows = icassp_semantic_batch_40.get("rows", [])
    if icassp_semantic_batch_40.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 040 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 040 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 040 contains duplicate paper IDs")

if icassp_semantic_batch_41:
    batch_rows = icassp_semantic_batch_41.get("rows", [])
    if icassp_semantic_batch_41.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 041 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 041 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 041 contains duplicate paper IDs")

if icassp_semantic_batch_42:
    batch_rows = icassp_semantic_batch_42.get("rows", [])
    if icassp_semantic_batch_42.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 042 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 042 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 042 contains duplicate paper IDs")

if icassp_semantic_batch_43:
    batch_rows = icassp_semantic_batch_43.get("rows", [])
    if icassp_semantic_batch_43.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 043 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 043 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 043 contains duplicate paper IDs")

if icassp_semantic_batch_44:
    batch_rows = icassp_semantic_batch_44.get("rows", [])
    if icassp_semantic_batch_44.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 044 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 044 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 044 contains duplicate paper IDs")

if icassp_semantic_batch_45:
    batch_rows = icassp_semantic_batch_45.get("rows", [])
    if icassp_semantic_batch_45.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 045 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 045 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 045 contains duplicate paper IDs")

if icassp_semantic_batch_46:
    batch_rows = icassp_semantic_batch_46.get("rows", [])
    if icassp_semantic_batch_46.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 16:
        errors.append("ICASSP semantic batch 046 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") != "D1" for row in batch_rows):
        errors.append("ICASSP semantic batch 046 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 046 contains duplicate paper IDs")

if icassp_semantic_batch_47:
    batch_rows = icassp_semantic_batch_47.get("rows", [])
    if icassp_semantic_batch_47.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 4:
        errors.append("ICASSP semantic batch 047 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 047 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 047 contains duplicate paper IDs")

if icassp_semantic_batch_48:
    batch_rows = icassp_semantic_batch_48.get("rows", [])
    if icassp_semantic_batch_48.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 8:
        errors.append("ICASSP semantic batch 048 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 048 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 048 contains duplicate paper IDs")

if icassp_semantic_batch_49:
    batch_rows = icassp_semantic_batch_49.get("rows", [])
    if icassp_semantic_batch_49.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 6:
        errors.append("ICASSP semantic batch 049 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 049 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 049 contains duplicate paper IDs")

if icassp_semantic_batch_50:
    batch_rows = icassp_semantic_batch_50.get("rows", [])
    if icassp_semantic_batch_50.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 4:
        errors.append("ICASSP semantic batch 050 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 050 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 050 contains duplicate paper IDs")

if icassp_semantic_batch_51:
    batch_rows = icassp_semantic_batch_51.get("rows", [])
    if icassp_semantic_batch_51.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 051 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 051 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 051 contains duplicate paper IDs")

if icassp_semantic_batch_52:
    batch_rows = icassp_semantic_batch_52.get("rows", [])
    if icassp_semantic_batch_52.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 24:
        errors.append("ICASSP semantic batch 052 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 052 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 052 contains duplicate paper IDs")

if icassp_semantic_batch_53:
    batch_rows = icassp_semantic_batch_53.get("rows", [])
    if icassp_semantic_batch_53.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 053 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 053 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 053 contains duplicate paper IDs")

if icassp_semantic_batch_54:
    batch_rows = icassp_semantic_batch_54.get("rows", [])
    if icassp_semantic_batch_54.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 15:
        errors.append("ICASSP semantic batch 054 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 054 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 054 contains duplicate paper IDs")

if icassp_semantic_batch_55:
    batch_rows = icassp_semantic_batch_55.get("rows", [])
    if icassp_semantic_batch_55.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 10:
        errors.append("ICASSP semantic batch 055 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 055 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 055 contains duplicate paper IDs")

if icassp_semantic_batch_56:
    batch_rows = icassp_semantic_batch_56.get("rows", [])
    if icassp_semantic_batch_56.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 12:
        errors.append("ICASSP semantic batch 056 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 056 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 056 contains duplicate paper IDs")

if icassp_semantic_batch_57:
    batch_rows = icassp_semantic_batch_57.get("rows", [])
    if icassp_semantic_batch_57.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 057 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 057 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 057 contains duplicate paper IDs")

if icassp_semantic_batch_58:
    batch_rows = icassp_semantic_batch_58.get("rows", [])
    if icassp_semantic_batch_58.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 24:
        errors.append("ICASSP semantic batch 058 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 058 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 058 contains duplicate paper IDs")

if icassp_semantic_batch_59:
    batch_rows = icassp_semantic_batch_59.get("rows", [])
    if icassp_semantic_batch_59.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 059 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 059 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 059 contains duplicate paper IDs")

if icassp_semantic_batch_60:
    batch_rows = icassp_semantic_batch_60.get("rows", [])
    if icassp_semantic_batch_60.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 11:
        errors.append("ICASSP semantic batch 060 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 060 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 060 contains duplicate paper IDs")

if icassp_semantic_batch_61:
    batch_rows = icassp_semantic_batch_61.get("rows", [])
    if icassp_semantic_batch_61.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 16:
        errors.append("ICASSP semantic batch 061 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 061 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 061 contains duplicate paper IDs")

if icassp_semantic_batch_62:
    batch_rows = icassp_semantic_batch_62.get("rows", [])
    if icassp_semantic_batch_62.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 100:
        errors.append("ICASSP semantic batch 062 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 062 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 062 contains duplicate paper IDs")

if icassp_semantic_batch_63:
    batch_rows = icassp_semantic_batch_63.get("rows", [])
    if icassp_semantic_batch_63.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 063 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 063 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 063 contains duplicate paper IDs")

if icassp_semantic_batch_64:
    batch_rows = icassp_semantic_batch_64.get("rows", [])
    if icassp_semantic_batch_64.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 064 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 064 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 064 contains duplicate paper IDs")

if icassp_semantic_batch_65:
    batch_rows = icassp_semantic_batch_65.get("rows", [])
    if icassp_semantic_batch_65.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 065 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 065 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 065 contains duplicate paper IDs")

if icassp_semantic_batch_66:
    batch_rows = icassp_semantic_batch_66.get("rows", [])
    if icassp_semantic_batch_66.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 066 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 066 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 066 contains duplicate paper IDs")

if icassp_semantic_batch_67:
    batch_rows = icassp_semantic_batch_67.get("rows", [])
    if icassp_semantic_batch_67.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 067 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 067 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 067 contains duplicate paper IDs")

if icassp_semantic_batch_68:
    batch_rows = icassp_semantic_batch_68.get("rows", [])
    if icassp_semantic_batch_68.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 068 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 068 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 068 contains duplicate paper IDs")

if icassp_semantic_batch_69:
    batch_rows = icassp_semantic_batch_69.get("rows", [])
    if icassp_semantic_batch_69.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 069 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 069 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 069 contains duplicate paper IDs")

if icassp_semantic_batch_70:
    batch_rows = icassp_semantic_batch_70.get("rows", [])
    if icassp_semantic_batch_70.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 070 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 070 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 070 contains duplicate paper IDs")

if icassp_semantic_batch_71:
    batch_rows = icassp_semantic_batch_71.get("rows", [])
    if icassp_semantic_batch_71.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 071 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 071 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 071 contains duplicate paper IDs")

if icassp_semantic_batch_72:
    batch_rows = icassp_semantic_batch_72.get("rows", [])
    if icassp_semantic_batch_72.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 072 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 072 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 072 contains duplicate paper IDs")

if icassp_semantic_batch_73:
    batch_rows = icassp_semantic_batch_73.get("rows", [])
    if icassp_semantic_batch_73.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 073 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 073 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 073 contains duplicate paper IDs")

if icassp_semantic_batch_74:
    batch_rows = icassp_semantic_batch_74.get("rows", [])
    if icassp_semantic_batch_74.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 200:
        errors.append("ICASSP semantic batch 074 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 074 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 074 contains duplicate paper IDs")

if icassp_semantic_batch_75:
    batch_rows = icassp_semantic_batch_75.get("rows", [])
    if icassp_semantic_batch_75.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 96:
        errors.append("ICASSP semantic batch 075 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 075 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 075 contains duplicate paper IDs")

if icassp_semantic_batch_76:
    batch_rows = icassp_semantic_batch_76.get("rows", [])
    if icassp_semantic_batch_76.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 15:
        errors.append("ICASSP semantic batch 076 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") not in {"supported", "unsupported"} or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 076 overstates or mislabels review")
    if any(row.get("decision") == "supported" and any(row.get(k) is None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 076 supported row lacks taxonomy assignment")
    if any(row.get("decision") == "unsupported" and any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 076 unsupported row has taxonomy assignment")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 076 contains duplicate paper IDs")

if icassp_semantic_batch_77:
    batch_rows = icassp_semantic_batch_77.get("rows", [])
    if icassp_semantic_batch_77.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 19:
        errors.append("ICASSP semantic batch 077 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 077 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 077 contains duplicate paper IDs")

if icassp_semantic_batch_78:
    batch_rows = icassp_semantic_batch_78.get("rows", [])
    if icassp_semantic_batch_78.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 078 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 078 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 078 contains duplicate paper IDs")

if icassp_semantic_batch_79:
    batch_rows = icassp_semantic_batch_79.get("rows", [])
    if icassp_semantic_batch_79.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 19:
        errors.append("ICASSP semantic batch 079 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 079 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 079 contains duplicate paper IDs")

if icassp_semantic_batch_80:
    batch_rows = icassp_semantic_batch_80.get("rows", [])
    if icassp_semantic_batch_80.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 32:
        errors.append("ICASSP semantic batch 080 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 080 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 080 contains duplicate paper IDs")

if icassp_semantic_batch_81:
    batch_rows = icassp_semantic_batch_81.get("rows", [])
    if icassp_semantic_batch_81.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 39:
        errors.append("ICASSP semantic batch 081 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 081 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 081 contains duplicate paper IDs")

if icassp_semantic_batch_82:
    batch_rows = icassp_semantic_batch_82.get("rows", [])
    if icassp_semantic_batch_82.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 30:
        errors.append("ICASSP semantic batch 082 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 082 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 082 contains duplicate paper IDs")

if icassp_semantic_batch_83:
    batch_rows = icassp_semantic_batch_83.get("rows", [])
    if icassp_semantic_batch_83.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 41:
        errors.append("ICASSP semantic batch 083 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 083 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 083 contains duplicate paper IDs")

if icassp_semantic_batch_84:
    batch_rows = icassp_semantic_batch_84.get("rows", [])
    if icassp_semantic_batch_84.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 6:
        errors.append("ICASSP semantic batch 084 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") not in {"supported", "unsupported"} or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 084 overstates or mislabels review")
    if any(row.get("decision") == "supported" and any(row.get(k) is None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 084 supported row lacks taxonomy assignment")
    if any(row.get("decision") == "unsupported" and any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 084 unsupported row has taxonomy assignment")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 084 contains duplicate paper IDs")

if icassp_semantic_batch_85:
    batch_rows = icassp_semantic_batch_85.get("rows", [])
    if icassp_semantic_batch_85.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 12:
        errors.append("ICASSP semantic batch 085 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" or row.get("evidence_depth") not in {"D1", "D2"} for row in batch_rows):
        errors.append("ICASSP semantic batch 085 overstates or mislabels review")
    if any(any(row.get(k) is None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 085 supported row lacks taxonomy assignment")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 085 contains duplicate paper IDs")

if icassp_semantic_batch_86:
    batch_rows = icassp_semantic_batch_86.get("rows", [])
    if icassp_semantic_batch_86.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 6:
        errors.append("ICASSP semantic batch 086 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 086 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 086 contains duplicate paper IDs")

if icassp_semantic_batch_87:
    batch_rows = icassp_semantic_batch_87.get("rows", [])
    if icassp_semantic_batch_87.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 6:
        errors.append("ICASSP semantic batch 087 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 087 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 087 contains duplicate paper IDs")

if icassp_semantic_batch_88:
    batch_rows = icassp_semantic_batch_88.get("rows", [])
    if icassp_semantic_batch_88.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 3:
        errors.append("ICASSP semantic batch 088 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" or row.get("evidence_depth") not in {"D1", "D2"} or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 088 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 088 contains duplicate paper IDs")

if icassp_semantic_batch_89:
    batch_rows = icassp_semantic_batch_89.get("rows", [])
    if icassp_semantic_batch_89.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 4:
        errors.append("ICASSP semantic batch 089 count mismatch")
    if any(row.get("review_state") != "analyst-reviewed" or row.get("decision") not in {"unsupported", "ambiguous"} or row.get("evidence_depth") != "D1" or any(row.get(k) is not None for k in ("theme_id", "subtheme_id", "concept_id")) for row in batch_rows):
        errors.append("ICASSP semantic batch 089 overstates or mislabels review")
    if len({row.get("paper_id") for row in batch_rows}) != len(batch_rows):
        errors.append("ICASSP semantic batch 089 contains duplicate paper IDs")

if icassp_data:
    if len(icassp_evidence) != icassp_data.get("n_papers") or len({row.get("paper_id") for row in icassp_evidence}) != len(icassp_evidence):
        errors.append("ICASSP paper evidence count or IDs mismatch")
    if any(row.get("depth") not in {"D1", "D2"} for row in icassp_evidence):
        errors.append("ICASSP paper evidence has invalid depth")
    required_icassp = {"bp", "wh", "naive", "ap", "mech", "math", "dots", "eval", "ww", "po", "limits", "depth"}
    if any(set(row) < required_icassp for row in icassp_evidence):
        errors.append("ICASSP paper evidence row is missing first-principles fields")

if semantic_batch:
    batch_rows = semantic_batch.get("rows", [])
    if semantic_batch.get("reviewed_count") != len(batch_rows) or len(batch_rows) != 24:
        errors.append("semantic reviewed batch count mismatch")
    required_review = {"theme_id", "subtheme_id", "concept_id", "semantic_reasoning", "evidence_excerpt", "source_sha256"}
    if any(set(row) < required_review for row in batch_rows):
        errors.append("semantic reviewed batch row is incomplete")

if semantic_d2_batch:
    d2_rows = semantic_d2_batch.get("rows", [])
    if semantic_d2_batch.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 reviewed batch count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 reviewed batch overstates or mislabels evidence")

if semantic_d2_batch_2:
    d2_rows = semantic_d2_batch_2.get("rows", [])
    if semantic_d2_batch_2.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 002 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 002 overstates or mislabels evidence")

if semantic_d2_batch_3:
    d2_rows = semantic_d2_batch_3.get("rows", [])
    if semantic_d2_batch_3.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 003 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 003 overstates or mislabels evidence")

if semantic_d2_batch_4:
    d2_rows = semantic_d2_batch_4.get("rows", [])
    if semantic_d2_batch_4.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 004 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 004 overstates or mislabels evidence")

if semantic_d2_batch_5:
    d2_rows = semantic_d2_batch_5.get("rows", [])
    if semantic_d2_batch_5.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 005 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 005 overstates or mislabels evidence")

if semantic_d2_batch_6:
    d2_rows = semantic_d2_batch_6.get("rows", [])
    if semantic_d2_batch_6.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 006 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 006 overstates or mislabels evidence")

if semantic_d2_batch_7:
    d2_rows = semantic_d2_batch_7.get("rows", [])
    if semantic_d2_batch_7.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 007 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 007 overstates or mislabels evidence")

if semantic_d2_batch_8:
    d2_rows = semantic_d2_batch_8.get("rows", [])
    if semantic_d2_batch_8.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 008 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 008 overstates or mislabels evidence")

if semantic_d2_batch_9:
    d2_rows = semantic_d2_batch_9.get("rows", [])
    if semantic_d2_batch_9.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 009 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 009 overstates or mislabels evidence")

if semantic_d2_batch_10:
    d2_rows = semantic_d2_batch_10.get("rows", [])
    if semantic_d2_batch_10.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 010 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 010 overstates or mislabels evidence")

if semantic_d2_batch_11:
    d2_rows = semantic_d2_batch_11.get("rows", [])
    if semantic_d2_batch_11.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 011 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 011 overstates or mislabels evidence")

if semantic_d2_batch_12:
    d2_rows = semantic_d2_batch_12.get("rows", [])
    if semantic_d2_batch_12.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 012 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 012 overstates or mislabels evidence")

if semantic_d2_batch_13:
    d2_rows = semantic_d2_batch_13.get("rows", [])
    if semantic_d2_batch_13.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 013 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 013 overstates or mislabels evidence")

if semantic_d2_batch_14:
    d2_rows = semantic_d2_batch_14.get("rows", [])
    if semantic_d2_batch_14.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 31:
        errors.append("semantic D2 batch 014 count mismatch")
    if any(row.get("evidence_depth") != "D2" or row.get("review_state") != "analyst-reviewed" for row in d2_rows):
        errors.append("semantic D2 batch 014 overstates or mislabels evidence")

if semantic_d2_batch_15:
    d2_rows = semantic_d2_batch_15.get("rows", [])
    if semantic_d2_batch_15.get("reviewed_count") != len(d2_rows) or len(d2_rows) != 32:
        errors.append("semantic D2 batch 015 count mismatch")
    if any(row.get("evidence_depth") not in {"D1", "D2"} or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "supported" for row in d2_rows):
        errors.append("semantic D2 batch 015 overstates or mislabels evidence")

if semantic_d3_batch_2:
    d3_rows = semantic_d3_batch_2.get("rows", [])
    if semantic_d3_batch_2.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 002 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 002 overstates or mislabels evidence")

if semantic_d3_batch_3:
    d3_rows = semantic_d3_batch_3.get("rows", [])
    if semantic_d3_batch_3.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 7:
        errors.append("semantic D3 batch 003 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 003 overstates or mislabels evidence")

if semantic_d3_batch_4:
    d3_rows = semantic_d3_batch_4.get("rows", [])
    if semantic_d3_batch_4.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 4:
        errors.append("semantic D3 batch 004 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 004 overstates or mislabels evidence")

if semantic_d3_batch_5:
    d3_rows = semantic_d3_batch_5.get("rows", [])
    if semantic_d3_batch_5.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 005 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 005 overstates or mislabels evidence")

if semantic_d3_batch_6:
    d3_rows = semantic_d3_batch_6.get("rows", [])
    if semantic_d3_batch_6.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 006 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 006 overstates or mislabels evidence")

if semantic_d3_batch_7:
    d3_rows = semantic_d3_batch_7.get("rows", [])
    if semantic_d3_batch_7.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 007 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 007 overstates or mislabels evidence")

if semantic_d3_batch_8:
    d3_rows = semantic_d3_batch_8.get("rows", [])
    if semantic_d3_batch_8.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 008 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 008 overstates or mislabels evidence")

if semantic_d3_batch_9:
    d3_rows = semantic_d3_batch_9.get("rows", [])
    if semantic_d3_batch_9.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 009 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 009 overstates or mislabels evidence")

if semantic_d3_batch_10:
    d3_rows = semantic_d3_batch_10.get("rows", [])
    if semantic_d3_batch_10.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 010 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 010 overstates or mislabels evidence")

if semantic_d3_batch_11:
    d3_rows = semantic_d3_batch_11.get("rows", [])
    if semantic_d3_batch_11.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 3:
        errors.append("semantic D3 batch 011 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 011 overstates or mislabels evidence")

if semantic_d3_batch_12:
    d3_rows = semantic_d3_batch_12.get("rows", [])
    if semantic_d3_batch_12.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 2:
        errors.append("semantic D3 batch 012 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 012 overstates or mislabels evidence")

if semantic_d3_batch_13:
    d3_rows = semantic_d3_batch_13.get("rows", [])
    if semantic_d3_batch_13.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 8:
        errors.append("semantic D3 batch 013 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 013 overstates or mislabels evidence")

if semantic_d3_batch_14:
    d3_rows = semantic_d3_batch_14.get("rows", [])
    if semantic_d3_batch_14.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 1:
        errors.append("semantic D3 batch 014 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 014 overstates or mislabels evidence")

if semantic_d3_batch_15:
    d3_rows = semantic_d3_batch_15.get("rows", [])
    if semantic_d3_batch_15.get("reviewed_count") != len(d3_rows) or len(d3_rows) != 4:
        errors.append("semantic D3 batch 015 count mismatch")
    if any(row.get("evidence_depth") != "D3" or row.get("review_state") != "analyst-reviewed" for row in d3_rows):
        errors.append("semantic D3 batch 015 overstates or mislabels evidence")

if semantic_boundary_batch_25:
    boundary_rows = semantic_boundary_batch_25.get("rows", [])
    if semantic_boundary_batch_25.get("reviewed_count") != len(boundary_rows) or len(boundary_rows) != 4:
        errors.append("semantic boundary batch 025 count mismatch")
    if any(row.get("evidence_depth") != "D1" or row.get("review_state") != "analyst-reviewed" or row.get("decision") != "unsupported" for row in boundary_rows):
        errors.append("semantic boundary batch 025 overstates or mislabels evidence")

if seed_synthesis and taxonomy:
    seed_extra_notes = [eighteenth_notes, nineteenth_notes, twentieth_notes, twentyfirst_notes, twentisecond_notes, twentythird_notes, twentyfourth_notes, twentyfifth_notes, twentysixth_notes, twentyseventh_notes, twentyeighth_notes, twentyninth_notes, thirtieth_notes, thirtyfirst_notes, thirtysecond_notes, thirtythird_notes, thirtyfourth_notes, thirtyfifth_notes, thirtysixth_notes, thirtyseventh_notes, thirtyeighth_notes, thirtyninth_notes, fortieth_notes, fortyfirst_notes, fortysecond_notes, fortythird_notes, fortyfourth_notes, fortyfifth_notes, fortysixth_notes, fortyseventh_notes, fortyeighth_notes, fortyninth_notes, fiftieth_notes, fiftyfirst_notes, fiftysecond_notes, fiftythird_notes, fiftyfourth_notes, fiftyfifth_notes, fiftysixth_notes, fiftyseventh_notes, fiftyeighth_notes, fiftyninth_notes, sixtieth_notes, sixtyfirst_notes]
    seed_extra_ids = {row.get("paper_id") for payload in seed_extra_notes for row in (payload or {}).get("notes", [])}
    expected_seed_d3 = sum(1 for row in deep_analysis if row.get("depth") == "D3" and row.get("semantic_review", {}).get("theme_id"))
    if seed_synthesis.get("reviewed_d3_count") != expected_seed_d3:
        errors.append("seed synthesis D3 count mismatch")
    if len(seed_synthesis.get("theme_rows", [])) != taxonomy.get("theme_count"):
        errors.append("seed synthesis theme count mismatch")

if subtheme_synthesis and taxonomy:
    expected_subthemes = sum(len(t.get("subthemes", [])) for t in taxonomy.get("themes", []))
    if subtheme_synthesis.get("subtheme_count") != expected_subthemes or len(subtheme_synthesis.get("records", [])) != expected_subthemes:
        errors.append("subtheme synthesis count mismatch")
    if any(row.get("status") not in {"seed-family-evidence", "unestablished"} for row in subtheme_synthesis.get("records", [])):
        errors.append("subtheme synthesis has invalid status")
    required_family_fields = {"ordinary_pressure", "naive_shortcut", "recurring_move", "reviewed_variation", "d3_mechanism_evidence", "named_contrast", "mechanism_contrast", "evidence_contrast", "failure_boundary_contrast", "transfer_question", "evidence_boundary", "unresolved_question"}
    if any(set(row.get("family_synthesis", {})) < required_family_fields for row in subtheme_synthesis.get("records", [])):
        errors.append("subtheme family synthesis is incomplete")
    if any(row.get("d3_paper_count", 0) < 2 for row in subtheme_synthesis.get("records", [])):
        errors.append("subtheme family synthesis lacks two D3 comparison cases")
    comparison_rows = [item for row in subtheme_synthesis.get("records", []) for item in row.get("family_synthesis", {}).get("d3_comparison_matrix", [])]
    if any(not item.get("evaluation_object") or not item.get("reported_payoff") for item in comparison_rows):
        errors.append("D3 family comparison row lacks evaluation or payoff evidence")

if concept_family_crosswalk and taxonomy:
    expected_concepts = sum(len(subtheme.get("concepts", [])) for theme in taxonomy.get("themes", []) for subtheme in theme.get("subthemes", []))
    records = concept_family_crosswalk.get("records", [])
    if concept_family_crosswalk.get("concept_count") != expected_concepts or len(records) != expected_concepts:
        errors.append("concept family crosswalk count mismatch")
    required_concept_crosswalk = {"definition", "boundary", "ordinary_pressure", "interspeech_reviewed_count", "interspeech_paper_ids", "icassp_reviewed_count", "icassp_paper_ids", "family_claim", "cross_venue_reading", "unresolved_question", "evidence_boundary"}
    if any(set(row) < required_concept_crosswalk for row in records):
        errors.append("concept family crosswalk record is incomplete")
    if len({row.get("concept_id") for row in records}) != expected_concepts:
        errors.append("concept family crosswalk concept IDs are not unique")
    required_concept_family_fields = {"concept_id", "concept_name", "definition", "boundary", "reviewed_paper_count", "d3_paper_count", "paper_ids", "d3_paper_ids", "family_claim", "unresolved"}
    if any(len(row.get("concept_families", [])) != 3 or any(set(family) < required_concept_family_fields for family in row.get("concept_families", [])) for row in subtheme_synthesis.get("records", [])):
        errors.append("concept-family synthesis is incomplete")

if concept_evidence_gaps and concept_family_crosswalk:
    expected_gaps = {row.get("concept_id") for row in concept_family_crosswalk.get("records", []) if row.get("icassp_reviewed_count", 0) == 0}
    actual_gaps = {row.get("concept_id") for row in concept_evidence_gaps.get("gaps", [])}
    if concept_evidence_gaps.get("gap_count") != len(actual_gaps) or actual_gaps != expected_gaps:
        errors.append("concept evidence gap report does not match crosswalk")

if cross_venue_crosswalk:
    contrasts = cross_venue_crosswalk.get("conceptual_contrasts", [])
    required_contrast_fields = {"assignment_links", "denominator_statement", "evidence_boundary", "conceptual_difference"}
    if any(set(row) < required_contrast_fields for row in contrasts):
        errors.append("cross-venue contrast lacks assignment or denominator provenance")
    if any(not row.get("assignment_links", {}).get("interspeech_paper_id") or not row.get("assignment_links", {}).get("icassp_paper_id") for row in contrasts):
        errors.append("cross-venue contrast has incomplete paper assignment links")
    if any(not row.get("next_evidence_needed") or not row.get("boundary") for row in concept_evidence_gaps.get("gaps", [])):
        errors.append("concept evidence gap row is incomplete")

if not reading_paths.exists():
    errors.append("first-principles reading paths report is missing")
if not semantic_gaps.exists():
    errors.append("semantic review gaps report is missing")
if not atlas_index.exists():
    errors.append("atlas index report is missing")

if papers:
    if len(deep_analysis) != papers.get("n_papers"):
        errors.append("deep paper analysis count mismatch")
    if len({row.get("paper_id") for row in deep_analysis}) != len(deep_analysis):
        errors.append("deep paper analysis IDs are not unique")
    required_deep = {"bp", "wh", "naive", "ap", "mech", "math", "dots", "eval", "ww", "po", "limits", "source", "depth", "semantic_review"}
    if any(set(row) < required_deep for row in deep_analysis):
        errors.append("deep paper analysis row is missing a required field")
    if any(row.get("depth") not in {"D2", "D3"} for row in deep_analysis):
        errors.append("deep paper analysis has invalid evidence depth")
    if any(row.get("semantic_review", {}).get("decision") not in {"supported", "unsupported", "ambiguous", "insufficient-evidence"} for row in deep_analysis):
        errors.append("deep paper analysis is missing semantic queue linkage")
    d3_records = [row for row in deep_analysis if row.get("depth") == "D3"]
    required_d3_provenance = {"pdf_sha256", "full_text_sha256", "page_count", "source_note"}
    if len(d3_records) != len(d3_paper_ids):
        errors.append("deep analysis D3 count mismatch")
    if any(set(row.get("full_paper_evidence", {})) < required_d3_provenance for row in d3_records):
        errors.append("D3 deep analysis is missing captured-paper provenance")
    if any(not row.get("full_paper_evidence", {}).get("pdf_sha256") or not row.get("full_paper_evidence", {}).get("full_text_sha256") for row in d3_records):
        errors.append("D3 deep analysis has empty captured-paper hashes")
    deep_by_id = {row.get("paper_id"): row for row in d3_records}
    note_mismatches = []
    for note_path in sorted((HERE / "data").glob("interspeech-2025-*-d3-notes.json")):
        try:
            note_payload = json.loads(note_path.read_text())
        except Exception:
            continue
        for note in note_payload.get("notes", []):
            row = deep_by_id.get(note.get("paper_id"))
            assignment = (row or {}).get("semantic_review", {})
            if row and assignment.get("theme_id") and (note.get("theme_id"), note.get("subtheme_id"), note.get("concept_id")) != (assignment.get("theme_id"), assignment.get("subtheme_id"), assignment.get("concept_id")):
                note_mismatches.append(f"{note_path.name}:{note.get('paper_id')}")
    if note_mismatches:
        errors.append(f"D3 note taxonomy mismatch ({len(note_mismatches)}): {', '.join(note_mismatches[:5])}")

if completion_audit:
    if completion_audit.get("overall_status") not in {"complete-bounded-evidence-release", "bounded-release-complete-with-explicit-boundaries", "deep-analysis-in-progress"}:
        errors.append("completion audit status mismatch")
    if completion_audit.get("criterion_count") != len(completion_audit.get("checks", [])):
        errors.append("completion audit criterion count mismatch")
    if completion_audit.get("overall_status") in {"complete-bounded-evidence-release", "bounded-release-complete-with-explicit-boundaries"} and any(check.get("status") not in {"verified", "verified-with-boundaries"} for check in completion_audit.get("checks", [])):
        errors.append("completion audit contains unverified criterion")

if representatives and claim_ledger:
    claims = claim_ledger.get("claims", [])
    if claim_ledger.get("claim_count") != len(claims) or len(claims) != len(representatives.get("papers", [])):
        errors.append("claim ledger count mismatch")
    if any(row.get("evidence_depth") != "D3" for row in claims):
        errors.append("claim ledger contains non-D3 claim")
    if any(row.get("independent_support_status") != "not-established" for row in claims):
        errors.append("claim ledger overstates independent support")

if errors:
    print(json.dumps({"status": "fail", "error_count": len(errors), "errors": errors}, indent=2))
    raise SystemExit(1)
print(json.dumps({"status": "pass", "paper_count": papers["n_papers"], "theme_count": len(themes["taxonomy"]), "errors": []}, indent=2))
