#!/usr/bin/env python3
"""Create the first explainable semantic-review queue.

This does not pretend that lexical scoring is human semantic judgment.  It
uses the old broad map only to propose likely first-principles destinations,
preserves exact evidence excerpts, and leaves every proposal visibly awaiting
analyst confirmation or rejection.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from taxonomy_normalization import normalize_review_row

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


# Candidate rules are intentionally small and readable.  They discover review
# work; they are not the final semantic decision.
RULES = [
    ("sound-and-production", "source-filter-production", ["vocal fold", "laryng", "articulat", "phonat", "vocal tract", "formant"]),
    ("sound-and-production", "time-frequency-measurement", ["spectrogram", "waveform", "frequency", "acoustic feature", "time-frequency", "sampling"]),
    ("sound-and-production", "room-channel-and-sensing", ["reverber", "microphone", "far-field", "acoustic sensing", "radar", "ultrasound", "neck"]),
    ("listening-and-separation", "noise-enhancement", ["noise", "denois", "enhancement", "speech intelligibility"]),
    ("listening-and-separation", "source-separation-and-spatial-listening", ["separation", "separat", "beamform", "overlap", "multi-speaker", "spatial"]),
    ("listening-and-separation", "echo-and-reconstruction", ["echo cancellation", "dereverb", "packet loss", "reconstruct", "inpaint"]),
    ("recognition-and-alignment", "acoustic-unit-mapping", ["automatic speech recognition", "speech recognition", "phoneme", "self-supervised speech", "speech representation"]),
    ("recognition-and-alignment", "boundaries-and-sequence-structure", ["alignment", "forced align", "disfluenc", "word boundary", "segmentation", "prosod"]),
    ("recognition-and-alignment", "adaptation-and-open-vocabulary", ["adaptation", "biasing", "rare word", "open vocabulary", "domain adaptation", "personaliz"]),
    ("meaning-and-interaction", "prosody-and-intent", ["emotion", "intent", "paraling", "prosody", "affect", "sentiment"]),
    ("meaning-and-interaction", "dialogue-and-turn-taking", ["dialogue", "conversation", "turn-taking", "turn taking", "spoken interaction"]),
    ("meaning-and-interaction", "grounding-and-action", ["grounding", "spoken command", "speech act", "referring expression", "embodied"]),
    ("voice-generation-and-control", "text-to-speech-and-content", ["text-to-speech", "text to speech", "tts", "vocoder", "speech synthesis"]),
    ("voice-generation-and-control", "voice-identity-and-conversion", ["voice conversion", "speaker conversion", "voice cloning", "speaker embedding", "target speaker"]),
    ("voice-generation-and-control", "prosody-and-interactive-control", ["controllable", "prosody control", "style", "expressive", "zero-shot synthesis"]),
    ("people-variation-and-health", "speaker-characteristics", ["speaker recognition", "speaker verification", "speaker identification", "age", "gender", "identity"]),
    ("people-variation-and-health", "clinical-and-assistive-speech", ["clinical", "dysarth", "aphasi", "patholog", "health", "assistive"]),
    ("people-variation-and-health", "human-centered-evaluation", ["user study", "listener", "accessib", "human evaluation", "subjective"]),
    ("languages-accents-and-resources", "multilingual-and-crosslingual", ["multilingual", "cross-lingual", "crosslingual", "code-switch", "language identification"]),
    ("languages-accents-and-resources", "low-resource-and-data-creation", ["low-resource", "low resource", "few-shot", "pseudo-label", "data collection", "unlabeled"]),
    ("languages-accents-and-resources", "accent-and-cultural-boundaries", ["accent", "dialect", "underrepresented", "inclusive", "fairness"]),
    ("evaluation-deployment-and-consequence", "metrics-and-targets", ["benchmark", "evaluation", "metric", "intelligibility", "naturalness", "quality"]),
    ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", ["robust", "real-time", "latency", "on-device", "edge", "deployment"]),
    ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", ["privacy", "spoof", "deepfake", "security", "anonym", "audit"]),
]


def term_pattern(term: str) -> str:
    """Match a term at a word boundary; many rules intentionally use prefixes."""
    return rf"\b{re.escape(term)}"


def excerpt(text: str, term: str) -> str:
    match = re.search(term_pattern(term), text, re.IGNORECASE)
    if not match:
        return text[:280].strip()
    start = max(0, match.start() - 110)
    end = min(len(text), match.end() + 170)
    return text[start:end].strip()


def main() -> None:
    source = json.loads((DATA / "interspeech-2025-papers.json").read_text())
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    canonical_triples = {
        (theme["id"], subtheme["id"], concept["id"])
        for theme in taxonomy["themes"]
        for subtheme in theme["subthemes"]
        for concept in subtheme["concepts"]
    }
    valid_concepts = {triple[2] for triple in canonical_triples}
    old = json.loads((DATA / "interspeech-2025-themes.json").read_text())
    batch_path = DATA / "interspeech-2025-semantic-reviewed-batch-001.json"
    batch = json.loads(batch_path.read_text()) if batch_path.exists() else {"rows": []}
    d2_batch_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-001.json"
    d2_batch = json.loads(d2_batch_path.read_text()) if d2_batch_path.exists() else {"rows": []}
    d2_batch_2_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-002.json"
    d2_batch_2 = json.loads(d2_batch_2_path.read_text()) if d2_batch_2_path.exists() else {"rows": []}
    d2_batch_3_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-003.json"
    d2_batch_3 = json.loads(d2_batch_3_path.read_text()) if d2_batch_3_path.exists() else {"rows": []}
    d2_batch_4_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-004.json"
    d2_batch_4 = json.loads(d2_batch_4_path.read_text()) if d2_batch_4_path.exists() else {"rows": []}
    d2_batch_5_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-005.json"
    d2_batch_5 = json.loads(d2_batch_5_path.read_text()) if d2_batch_5_path.exists() else {"rows": []}
    d2_batch_6_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-006.json"
    d2_batch_6 = json.loads(d2_batch_6_path.read_text()) if d2_batch_6_path.exists() else {"rows": []}
    d2_batch_7_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-007.json"
    d2_batch_7 = json.loads(d2_batch_7_path.read_text()) if d2_batch_7_path.exists() else {"rows": []}
    d2_batch_8_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-008.json"
    d2_batch_8 = json.loads(d2_batch_8_path.read_text()) if d2_batch_8_path.exists() else {"rows": []}
    d2_batch_9_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-009.json"
    d2_batch_9 = json.loads(d2_batch_9_path.read_text()) if d2_batch_9_path.exists() else {"rows": []}
    d2_batch_10_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-010.json"
    d2_batch_10 = json.loads(d2_batch_10_path.read_text()) if d2_batch_10_path.exists() else {"rows": []}
    d2_batch_11_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-011.json"
    d2_batch_11 = json.loads(d2_batch_11_path.read_text()) if d2_batch_11_path.exists() else {"rows": []}
    d2_batch_12_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-012.json"
    d2_batch_12 = json.loads(d2_batch_12_path.read_text()) if d2_batch_12_path.exists() else {"rows": []}
    d2_batch_13_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-013.json"
    d2_batch_13 = json.loads(d2_batch_13_path.read_text()) if d2_batch_13_path.exists() else {"rows": []}
    d2_batch_14_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-014.json"
    d2_batch_14 = json.loads(d2_batch_14_path.read_text()) if d2_batch_14_path.exists() else {"rows": []}
    d2_batch_15_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-015.json"
    d2_batch_15 = json.loads(d2_batch_15_path.read_text()) if d2_batch_15_path.exists() else {"rows": []}
    d2_batch_16_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-016.json"
    d2_batch_16 = json.loads(d2_batch_16_path.read_text()) if d2_batch_16_path.exists() else {"rows": []}
    d2_batch_17_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-017.json"
    d2_batch_17 = json.loads(d2_batch_17_path.read_text()) if d2_batch_17_path.exists() else {"rows": []}
    d2_batch_18_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-018.json"
    d2_batch_18 = json.loads(d2_batch_18_path.read_text()) if d2_batch_18_path.exists() else {"rows": []}
    d2_batch_19_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-019.json"
    d2_batch_19 = json.loads(d2_batch_19_path.read_text()) if d2_batch_19_path.exists() else {"rows": []}
    d2_batch_20_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-020.json"
    d2_batch_20 = json.loads(d2_batch_20_path.read_text()) if d2_batch_20_path.exists() else {"rows": []}
    d2_batch_21_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-021.json"
    d2_batch_21 = json.loads(d2_batch_21_path.read_text()) if d2_batch_21_path.exists() else {"rows": []}
    d2_batch_22_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-022.json"
    d2_batch_22 = json.loads(d2_batch_22_path.read_text()) if d2_batch_22_path.exists() else {"rows": []}
    d2_batch_23_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-023.json"
    d2_batch_23 = json.loads(d2_batch_23_path.read_text()) if d2_batch_23_path.exists() else {"rows": []}
    d2_batch_24_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-024.json"
    d2_batch_24 = json.loads(d2_batch_24_path.read_text()) if d2_batch_24_path.exists() else {"rows": []}
    d2_batch_25_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-025.json"
    d2_batch_25 = json.loads(d2_batch_25_path.read_text()) if d2_batch_25_path.exists() else {"rows": []}
    d2_batch_26_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-026.json"
    d2_batch_26 = json.loads(d2_batch_26_path.read_text()) if d2_batch_26_path.exists() else {"rows": []}
    d2_batch_27_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-027.json"
    d2_batch_27 = json.loads(d2_batch_27_path.read_text()) if d2_batch_27_path.exists() else {"rows": []}
    d2_batch_28_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-028.json"
    d2_batch_28 = json.loads(d2_batch_28_path.read_text()) if d2_batch_28_path.exists() else {"rows": []}
    d2_batch_29_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-029.json"
    d2_batch_29 = json.loads(d2_batch_29_path.read_text()) if d2_batch_29_path.exists() else {"rows": []}
    d2_batch_30_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-030.json"
    d2_batch_30 = json.loads(d2_batch_30_path.read_text()) if d2_batch_30_path.exists() else {"rows": []}
    d2_batch_31_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-031.json"
    d2_batch_31 = json.loads(d2_batch_31_path.read_text()) if d2_batch_31_path.exists() else {"rows": []}
    d2_batch_32_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-032.json"
    d2_batch_32 = json.loads(d2_batch_32_path.read_text()) if d2_batch_32_path.exists() else {"rows": []}
    d2_batch_33_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-033.json"
    d2_batch_33 = json.loads(d2_batch_33_path.read_text()) if d2_batch_33_path.exists() else {"rows": []}
    d2_batch_34_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-034.json"
    d2_batch_34 = json.loads(d2_batch_34_path.read_text()) if d2_batch_34_path.exists() else {"rows": []}
    d2_batch_35_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-035.json"
    d2_batch_35 = json.loads(d2_batch_35_path.read_text()) if d2_batch_35_path.exists() else {"rows": []}
    d2_batch_36_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-036.json"
    d2_batch_36 = json.loads(d2_batch_36_path.read_text()) if d2_batch_36_path.exists() else {"rows": []}
    d2_batch_37_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-037.json"
    d2_batch_37 = json.loads(d2_batch_37_path.read_text()) if d2_batch_37_path.exists() else {"rows": []}
    d2_batch_38_path = DATA / "interspeech-2025-semantic-reviewed-d2-batch-038.json"
    d2_batch_38 = json.loads(d2_batch_38_path.read_text()) if d2_batch_38_path.exists() else {"rows": []}
    out_scope_38_path = DATA / "interspeech-2025-semantic-reviewed-out-of-scope-batch-038.json"
    out_scope_38 = json.loads(out_scope_38_path.read_text()) if out_scope_38_path.exists() else {"rows": []}
    provisional_39_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-039.json"
    provisional_39 = json.loads(provisional_39_path.read_text()) if provisional_39_path.exists() else {"rows": []}
    provisional_40_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-040.json"
    provisional_40 = json.loads(provisional_40_path.read_text()) if provisional_40_path.exists() else {"rows": []}
    provisional_41_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-041.json"
    provisional_41 = json.loads(provisional_41_path.read_text()) if provisional_41_path.exists() else {"rows": []}
    provisional_42_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-042.json"
    provisional_42 = json.loads(provisional_42_path.read_text()) if provisional_42_path.exists() else {"rows": []}
    provisional_43_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-043.json"
    provisional_43 = json.loads(provisional_43_path.read_text()) if provisional_43_path.exists() else {"rows": []}
    provisional_44_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-044.json"
    provisional_44 = json.loads(provisional_44_path.read_text()) if provisional_44_path.exists() else {"rows": []}
    provisional_45_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-045.json"
    provisional_45 = json.loads(provisional_45_path.read_text()) if provisional_45_path.exists() else {"rows": []}
    provisional_46_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-046.json"
    provisional_46 = json.loads(provisional_46_path.read_text()) if provisional_46_path.exists() else {"rows": []}
    provisional_47_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-047.json"
    provisional_47 = json.loads(provisional_47_path.read_text()) if provisional_47_path.exists() else {"rows": []}
    provisional_48_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-048.json"
    provisional_48 = json.loads(provisional_48_path.read_text()) if provisional_48_path.exists() else {"rows": []}
    provisional_49_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-049.json"
    provisional_49 = json.loads(provisional_49_path.read_text()) if provisional_49_path.exists() else {"rows": []}
    provisional_50_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-050.json"
    provisional_50 = json.loads(provisional_50_path.read_text()) if provisional_50_path.exists() else {"rows": []}
    provisional_51_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-051.json"
    provisional_51 = json.loads(provisional_51_path.read_text()) if provisional_51_path.exists() else {"rows": []}
    provisional_52_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-052.json"
    provisional_52 = json.loads(provisional_52_path.read_text()) if provisional_52_path.exists() else {"rows": []}
    provisional_53_path = DATA / "interspeech-2025-semantic-reviewed-provisional-d2-batch-053.json"
    provisional_53 = json.loads(provisional_53_path.read_text()) if provisional_53_path.exists() else {"rows": []}
    d3_batch_2_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-002.json"
    d3_batch_2 = json.loads(d3_batch_2_path.read_text()) if d3_batch_2_path.exists() else {"rows": []}
    d3_batch_3_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-003.json"
    d3_batch_3 = json.loads(d3_batch_3_path.read_text()) if d3_batch_3_path.exists() else {"rows": []}
    d3_batch_4_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-004.json"
    d3_batch_4 = json.loads(d3_batch_4_path.read_text()) if d3_batch_4_path.exists() else {"rows": []}
    d3_batch_5_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-005.json"
    d3_batch_5 = json.loads(d3_batch_5_path.read_text()) if d3_batch_5_path.exists() else {"rows": []}
    d3_batch_6_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-006.json"
    d3_batch_6 = json.loads(d3_batch_6_path.read_text()) if d3_batch_6_path.exists() else {"rows": []}
    d3_batch_7_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-007.json"
    d3_batch_7 = json.loads(d3_batch_7_path.read_text()) if d3_batch_7_path.exists() else {"rows": []}
    d3_batch_8_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-008.json"
    d3_batch_8 = json.loads(d3_batch_8_path.read_text()) if d3_batch_8_path.exists() else {"rows": []}
    d3_batch_9_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-009.json"
    d3_batch_9 = json.loads(d3_batch_9_path.read_text()) if d3_batch_9_path.exists() else {"rows": []}
    d3_batch_10_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-010.json"
    d3_batch_10 = json.loads(d3_batch_10_path.read_text()) if d3_batch_10_path.exists() else {"rows": []}
    d3_batch_11_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-011.json"
    d3_batch_11 = json.loads(d3_batch_11_path.read_text()) if d3_batch_11_path.exists() else {"rows": []}
    d3_batch_12_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-012.json"
    d3_batch_12 = json.loads(d3_batch_12_path.read_text()) if d3_batch_12_path.exists() else {"rows": []}
    d3_batch_13_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-013.json"
    d3_batch_13 = json.loads(d3_batch_13_path.read_text()) if d3_batch_13_path.exists() else {"rows": []}
    d3_batch_14_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-014.json"
    d3_batch_14 = json.loads(d3_batch_14_path.read_text()) if d3_batch_14_path.exists() else {"rows": []}
    d3_batch_15_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-015.json"
    d3_batch_15 = json.loads(d3_batch_15_path.read_text()) if d3_batch_15_path.exists() else {"rows": []}
    d3_batch_16_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-016.json"
    d3_batch_16 = json.loads(d3_batch_16_path.read_text()) if d3_batch_16_path.exists() else {"rows": []}
    d3_batch_17_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-017.json"
    d3_batch_17 = json.loads(d3_batch_17_path.read_text()) if d3_batch_17_path.exists() else {"rows": []}
    d3_batch_18_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-018.json"
    d3_batch_18 = json.loads(d3_batch_18_path.read_text()) if d3_batch_18_path.exists() else {"rows": []}
    d3_batch_19_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-019.json"
    d3_batch_19 = json.loads(d3_batch_19_path.read_text()) if d3_batch_19_path.exists() else {"rows": []}
    d3_batch_20_path = DATA / "interspeech-2025-semantic-reviewed-d3-batch-020.json"
    d3_batch_20 = json.loads(d3_batch_20_path.read_text()) if d3_batch_20_path.exists() else {"rows": []}
    boundary_batch_25_path = DATA / "interspeech-2025-semantic-reviewed-batch-025.json"
    boundary_batch_25 = json.loads(boundary_batch_25_path.read_text()) if boundary_batch_25_path.exists() else {"rows": []}
    semantic_batch_26_path = DATA / "interspeech-2025-semantic-reviewed-batch-026.json"
    semantic_batch_26 = json.loads(semantic_batch_26_path.read_text()) if semantic_batch_26_path.exists() else {"rows": []}
    reviewed_by_id = {row["paper_id"]: row for row in d2_batch.get("rows", [])}
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_2.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_3.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_4.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_5.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_6.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_7.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_8.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_9.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_10.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_11.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_12.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_13.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_14.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_15.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_16.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_17.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_18.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_19.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_20.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_21.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_22.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_23.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_24.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_25.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_26.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_27.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_28.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_29.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_30.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_31.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_32.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_33.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_34.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_35.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_36.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_37.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d2_batch_38.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in out_scope_38.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_39.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_40.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_41.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_42.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_43.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_44.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_45.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_46.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_47.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_48.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_49.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_50.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_51.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_52.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in provisional_53.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_2.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_3.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_4.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_5.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_6.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_7.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_8.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_9.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_10.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_11.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_12.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_13.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_14.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_15.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_16.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_17.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_18.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_19.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in d3_batch_20.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in boundary_batch_25.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in semantic_batch_26.get("rows", [])})
    reviewed_by_id = {
        paper_id: normalize_review_row(row, valid_concepts, canonical_triples)
        for paper_id, row in reviewed_by_id.items()
    }
    old_by_id = {row["paper_id"]: row for row in old.get("papers", [])}
    rows = []
    for paper in source["papers"]:
        text = f"{paper.get('title', '')}. {paper.get('abstract', '')}".strip()
        candidates = []
        for theme_id, subtheme_id, terms in RULES:
            hits = [term for term in terms if re.search(term_pattern(term), text, re.IGNORECASE)]
            if hits:
                candidates.append({
                    "theme_id": theme_id,
                    "subtheme_id": subtheme_id,
                    "matched_terms": hits,
                    "score": len(hits),
                    "evidence_excerpt": excerpt(text, hits[0]),
                })
        candidates.sort(key=lambda x: (-x["score"], x["theme_id"], x["subtheme_id"]))
        top_score = candidates[0]["score"] if candidates else 0
        tied = [x for x in candidates if x["score"] == top_score]
        if not candidates:
            decision = "insufficient-evidence"
            confidence = "low"
        elif top_score >= 2 and len(tied) == 1:
            decision = "supported"
            confidence = "machine-proposed"
        else:
            decision = "ambiguous"
            confidence = "machine-proposed"
        row = {
            "paper_id": paper["paper_id"],
            "title": paper["title"],
            "paper_url": paper["paper_url"],
            "source": "official-isca-archive",
            "evidence_depth": "D2",
            "old_keyword_themes": old_by_id.get(paper["paper_id"], {}).get("conceptual_themes", []),
            "candidate_assignments": candidates[:5],
            "decision": decision,
            "confidence": confidence,
            "alternative_assignment": candidates[1]["subtheme_id"] if len(candidates) > 1 else None,
            "review_state": "needs-analyst-semantic-review",
            "review_rule": "Explainable title+abstract candidate generation; lexical match is not accepted as final membership.",
        }
        if paper["paper_id"] in reviewed_by_id:
            reviewed = reviewed_by_id[paper["paper_id"]]
            row["decision"] = reviewed["decision"]
            row["confidence"] = reviewed["confidence"]
            row["review_state"] = reviewed["review_state"]
            row["evidence_depth"] = reviewed["evidence_depth"]
            row["analyst_review"] = reviewed
        rows.append(row)
    counts = {key: sum(row["decision"] == key for row in rows) for key in ("supported", "ambiguous", "insufficient-evidence", "unsupported")}
    payload = {
        "schema_version": 1,
        "status": "machine-assisted-proposals-awaiting-semantic-review",
        "claim_boundary": "These are review proposals, not completed semantic judgments. Exact excerpts and unresolved alternatives are preserved so an analyst can confirm or reject each assignment.",
        "source": "data/interspeech-2025-papers.json",
        "taxonomy": "data/speech-first-principles-taxonomy.json",
        "paper_count": len(rows),
        "decision_counts": counts,
        "reviewed_count": len(reviewed_by_id),
        "reviewed_batch_ids": [f"interspeech-2025-semantic-d2-batch-{index:03d}" for index in range(1, 39)] + [f"interspeech-2025-semantic-d3-batch-{index:03d}" for index in range(1, 21)] + ["interspeech-2025-semantic-batch-025", "interspeech-2025-semantic-batch-026"],
        "rows": rows,
    }
    (DATA / "interspeech-2025-semantic-review-queue.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    summary = ["# INTERSPEECH 2025 semantic review queue", "", payload["claim_boundary"], "", f"Papers: **{len(rows)}**; analyst-reviewed: **{payload['reviewed_count']}**", "", "| Proposal state | Count |", "|---|---:|"]
    summary += [f"| {key} | {value} |" for key, value in counts.items()]
    summary += ["", "## Review rule", "", "The old keyword themes are shown only as a discovery comparison. A final reviewer must decide whether the excerpt supports the first-principles theme/subtheme, reject it, or mark the evidence insufficient. A paper can belong to multiple concepts, but each membership needs its own excerpt and boundary reasoning.", ""]
    (REPORTS / "INTERSPEECH_2025_SEMANTIC_REVIEW_QUEUE.md").write_text("\n".join(summary))
    print(json.dumps({"paper_count": len(rows), "decision_counts": counts, "reviewed_count": payload["reviewed_count"]}))


if __name__ == "__main__":
    main()
