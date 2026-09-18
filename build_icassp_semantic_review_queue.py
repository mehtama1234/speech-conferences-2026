#!/usr/bin/env python3
"""Create an evidence-bound semantic review queue for all ICASSP records.

ICASSP is broader than speech.  Non-speech records remain in the denominator
and are explicitly marked unsupported for this speech taxonomy rather than
silently disappearing from the cross-venue comparison.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from build_semantic_review_queue import RULES, excerpt, term_pattern
from taxonomy_normalization import normalize_review_row

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

SPEECH_SCOPE = [
    "speech", "spoken", "speaker", "voice", "audio", "acoustic", "phon", "vocal",
    "asr", "tts", "diar", "vocoder", "prosod", "utterance", "sound", "music",
    "microphone", "listening", "hearing", "noise", "separation", "enhancement",
]


def main() -> None:
    source = json.loads((DATA / "icassp-2026-papers.json").read_text())
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    canonical_triples = {
        (theme["id"], subtheme["id"], concept["id"])
        for theme in taxonomy["themes"]
        for subtheme in theme["subthemes"]
        for concept in subtheme["concepts"]
    }
    valid_concepts = {triple[2] for triple in canonical_triples}
    batch_path = DATA / "icassp-2026-semantic-reviewed-batch-001.json"
    batch = json.loads(batch_path.read_text()) if batch_path.exists() else {"rows": []}
    batch_2_path = DATA / "icassp-2026-semantic-reviewed-batch-002.json"
    batch_2 = json.loads(batch_2_path.read_text()) if batch_2_path.exists() else {"rows": []}
    batch_3_path = DATA / "icassp-2026-semantic-reviewed-batch-003.json"
    batch_3 = json.loads(batch_3_path.read_text()) if batch_3_path.exists() else {"rows": []}
    batch_4_path = DATA / "icassp-2026-semantic-reviewed-batch-004.json"
    batch_4 = json.loads(batch_4_path.read_text()) if batch_4_path.exists() else {"rows": []}
    batch_5_path = DATA / "icassp-2026-semantic-reviewed-batch-005.json"
    batch_5 = json.loads(batch_5_path.read_text()) if batch_5_path.exists() else {"rows": []}
    batch_6_path = DATA / "icassp-2026-semantic-reviewed-batch-006.json"
    batch_6 = json.loads(batch_6_path.read_text()) if batch_6_path.exists() else {"rows": []}
    batch_7_path = DATA / "icassp-2026-semantic-reviewed-batch-007.json"
    batch_7 = json.loads(batch_7_path.read_text()) if batch_7_path.exists() else {"rows": []}
    batch_8_path = DATA / "icassp-2026-semantic-reviewed-batch-008.json"
    batch_8 = json.loads(batch_8_path.read_text()) if batch_8_path.exists() else {"rows": []}
    batch_9_path = DATA / "icassp-2026-semantic-reviewed-batch-009.json"
    batch_9 = json.loads(batch_9_path.read_text()) if batch_9_path.exists() else {"rows": []}
    batch_10_path = DATA / "icassp-2026-semantic-reviewed-batch-010.json"
    batch_10 = json.loads(batch_10_path.read_text()) if batch_10_path.exists() else {"rows": []}
    batch_11_path = DATA / "icassp-2026-semantic-reviewed-batch-011.json"
    batch_11 = json.loads(batch_11_path.read_text()) if batch_11_path.exists() else {"rows": []}
    batch_12_path = DATA / "icassp-2026-semantic-reviewed-batch-012.json"
    batch_12 = json.loads(batch_12_path.read_text()) if batch_12_path.exists() else {"rows": []}
    batch_13_path = DATA / "icassp-2026-semantic-reviewed-batch-013.json"
    batch_13 = json.loads(batch_13_path.read_text()) if batch_13_path.exists() else {"rows": []}
    batch_14_path = DATA / "icassp-2026-semantic-reviewed-batch-014.json"
    batch_14 = json.loads(batch_14_path.read_text()) if batch_14_path.exists() else {"rows": []}
    batch_15_path = DATA / "icassp-2026-semantic-reviewed-batch-015.json"
    batch_15 = json.loads(batch_15_path.read_text()) if batch_15_path.exists() else {"rows": []}
    batch_16_path = DATA / "icassp-2026-semantic-reviewed-batch-016.json"
    batch_16 = json.loads(batch_16_path.read_text()) if batch_16_path.exists() else {"rows": []}
    batch_17_path = DATA / "icassp-2026-semantic-reviewed-batch-017.json"
    batch_17 = json.loads(batch_17_path.read_text()) if batch_17_path.exists() else {"rows": []}
    batch_18_path = DATA / "icassp-2026-semantic-reviewed-batch-018.json"
    batch_18 = json.loads(batch_18_path.read_text()) if batch_18_path.exists() else {"rows": []}
    batch_19_path = DATA / "icassp-2026-semantic-reviewed-batch-019.json"
    batch_19 = json.loads(batch_19_path.read_text()) if batch_19_path.exists() else {"rows": []}
    batch_20_path = DATA / "icassp-2026-semantic-reviewed-batch-020.json"
    batch_20 = json.loads(batch_20_path.read_text()) if batch_20_path.exists() else {"rows": []}
    batch_21_path = DATA / "icassp-2026-semantic-reviewed-batch-021.json"
    batch_21 = json.loads(batch_21_path.read_text()) if batch_21_path.exists() else {"rows": []}
    batch_22_path = DATA / "icassp-2026-semantic-reviewed-batch-022.json"
    batch_22 = json.loads(batch_22_path.read_text()) if batch_22_path.exists() else {"rows": []}
    batch_23_path = DATA / "icassp-2026-semantic-reviewed-batch-023.json"
    batch_23 = json.loads(batch_23_path.read_text()) if batch_23_path.exists() else {"rows": []}
    batch_24_path = DATA / "icassp-2026-semantic-reviewed-batch-024.json"
    batch_24 = json.loads(batch_24_path.read_text()) if batch_24_path.exists() else {"rows": []}
    batch_25_path = DATA / "icassp-2026-semantic-reviewed-batch-025.json"
    batch_25 = json.loads(batch_25_path.read_text()) if batch_25_path.exists() else {"rows": []}
    batch_26_path = DATA / "icassp-2026-semantic-reviewed-batch-026.json"
    batch_26 = json.loads(batch_26_path.read_text()) if batch_26_path.exists() else {"rows": []}
    batch_27_path = DATA / "icassp-2026-semantic-reviewed-batch-027.json"
    batch_27 = json.loads(batch_27_path.read_text()) if batch_27_path.exists() else {"rows": []}
    batch_28_path = DATA / "icassp-2026-semantic-reviewed-batch-028.json"
    batch_28 = json.loads(batch_28_path.read_text()) if batch_28_path.exists() else {"rows": []}
    batch_29_path = DATA / "icassp-2026-semantic-reviewed-batch-029.json"
    batch_29 = json.loads(batch_29_path.read_text()) if batch_29_path.exists() else {"rows": []}
    batch_30_path = DATA / "icassp-2026-semantic-reviewed-batch-030.json"
    batch_30 = json.loads(batch_30_path.read_text()) if batch_30_path.exists() else {"rows": []}
    batch_31_path = DATA / "icassp-2026-semantic-reviewed-batch-031.json"
    batch_31 = json.loads(batch_31_path.read_text()) if batch_31_path.exists() else {"rows": []}
    batch_32_path = DATA / "icassp-2026-semantic-reviewed-batch-032.json"
    batch_32 = json.loads(batch_32_path.read_text()) if batch_32_path.exists() else {"rows": []}
    batch_33_path = DATA / "icassp-2026-semantic-reviewed-batch-033.json"
    batch_33 = json.loads(batch_33_path.read_text()) if batch_33_path.exists() else {"rows": []}
    batch_34_path = DATA / "icassp-2026-semantic-reviewed-batch-034.json"
    batch_34 = json.loads(batch_34_path.read_text()) if batch_34_path.exists() else {"rows": []}
    batch_35_path = DATA / "icassp-2026-semantic-reviewed-batch-035.json"
    batch_35 = json.loads(batch_35_path.read_text()) if batch_35_path.exists() else {"rows": []}
    batch_36_path = DATA / "icassp-2026-semantic-reviewed-batch-036.json"
    batch_36 = json.loads(batch_36_path.read_text()) if batch_36_path.exists() else {"rows": []}
    batch_37_path = DATA / "icassp-2026-semantic-reviewed-batch-037.json"
    batch_37 = json.loads(batch_37_path.read_text()) if batch_37_path.exists() else {"rows": []}
    batch_38_path = DATA / "icassp-2026-semantic-reviewed-batch-038.json"
    batch_38 = json.loads(batch_38_path.read_text()) if batch_38_path.exists() else {"rows": []}
    batch_39_path = DATA / "icassp-2026-semantic-reviewed-batch-039.json"
    batch_39 = json.loads(batch_39_path.read_text()) if batch_39_path.exists() else {"rows": []}
    batch_40_path = DATA / "icassp-2026-semantic-reviewed-batch-040.json"
    batch_40 = json.loads(batch_40_path.read_text()) if batch_40_path.exists() else {"rows": []}
    batch_41_path = DATA / "icassp-2026-semantic-reviewed-batch-041.json"
    batch_41 = json.loads(batch_41_path.read_text()) if batch_41_path.exists() else {"rows": []}
    batch_42_path = DATA / "icassp-2026-semantic-reviewed-batch-042.json"
    batch_42 = json.loads(batch_42_path.read_text()) if batch_42_path.exists() else {"rows": []}
    batch_43_path = DATA / "icassp-2026-semantic-reviewed-batch-043.json"
    batch_43 = json.loads(batch_43_path.read_text()) if batch_43_path.exists() else {"rows": []}
    batch_44_path = DATA / "icassp-2026-semantic-reviewed-batch-044.json"
    batch_44 = json.loads(batch_44_path.read_text()) if batch_44_path.exists() else {"rows": []}
    batch_45_path = DATA / "icassp-2026-semantic-reviewed-batch-045.json"
    batch_45 = json.loads(batch_45_path.read_text()) if batch_45_path.exists() else {"rows": []}
    batch_46_path = DATA / "icassp-2026-semantic-reviewed-batch-046.json"
    batch_46 = json.loads(batch_46_path.read_text()) if batch_46_path.exists() else {"rows": []}
    batch_47_path = DATA / "icassp-2026-semantic-reviewed-batch-047.json"
    batch_47 = json.loads(batch_47_path.read_text()) if batch_47_path.exists() else {"rows": []}
    batch_48_path = DATA / "icassp-2026-semantic-reviewed-batch-048.json"
    batch_48 = json.loads(batch_48_path.read_text()) if batch_48_path.exists() else {"rows": []}
    batch_49_path = DATA / "icassp-2026-semantic-reviewed-batch-049.json"
    batch_49 = json.loads(batch_49_path.read_text()) if batch_49_path.exists() else {"rows": []}
    batch_50_path = DATA / "icassp-2026-semantic-reviewed-batch-050.json"
    batch_50 = json.loads(batch_50_path.read_text()) if batch_50_path.exists() else {"rows": []}
    batch_51_path = DATA / "icassp-2026-semantic-reviewed-batch-051.json"
    batch_51 = json.loads(batch_51_path.read_text()) if batch_51_path.exists() else {"rows": []}
    batch_52_path = DATA / "icassp-2026-semantic-reviewed-batch-052.json"
    batch_52 = json.loads(batch_52_path.read_text()) if batch_52_path.exists() else {"rows": []}
    batch_53_path = DATA / "icassp-2026-semantic-reviewed-batch-053.json"
    batch_53 = json.loads(batch_53_path.read_text()) if batch_53_path.exists() else {"rows": []}
    batch_54_path = DATA / "icassp-2026-semantic-reviewed-batch-054.json"
    batch_54 = json.loads(batch_54_path.read_text()) if batch_54_path.exists() else {"rows": []}
    batch_55_path = DATA / "icassp-2026-semantic-reviewed-batch-055.json"
    batch_55 = json.loads(batch_55_path.read_text()) if batch_55_path.exists() else {"rows": []}
    batch_56_path = DATA / "icassp-2026-semantic-reviewed-batch-056.json"
    batch_56 = json.loads(batch_56_path.read_text()) if batch_56_path.exists() else {"rows": []}
    batch_57_path = DATA / "icassp-2026-semantic-reviewed-batch-057.json"
    batch_57 = json.loads(batch_57_path.read_text()) if batch_57_path.exists() else {"rows": []}
    batch_58_path = DATA / "icassp-2026-semantic-reviewed-batch-058.json"
    batch_58 = json.loads(batch_58_path.read_text()) if batch_58_path.exists() else {"rows": []}
    batch_59_path = DATA / "icassp-2026-semantic-reviewed-batch-059.json"
    batch_59 = json.loads(batch_59_path.read_text()) if batch_59_path.exists() else {"rows": []}
    batch_60_path = DATA / "icassp-2026-semantic-reviewed-batch-060.json"
    batch_60 = json.loads(batch_60_path.read_text()) if batch_60_path.exists() else {"rows": []}
    batch_61_path = DATA / "icassp-2026-semantic-reviewed-batch-061.json"
    batch_61 = json.loads(batch_61_path.read_text()) if batch_61_path.exists() else {"rows": []}
    batch_62_path = DATA / "icassp-2026-semantic-reviewed-batch-062.json"
    batch_62 = json.loads(batch_62_path.read_text()) if batch_62_path.exists() else {"rows": []}
    batch_63_path = DATA / "icassp-2026-semantic-reviewed-batch-063.json"
    batch_63 = json.loads(batch_63_path.read_text()) if batch_63_path.exists() else {"rows": []}
    batch_64_path = DATA / "icassp-2026-semantic-reviewed-batch-064.json"
    batch_64 = json.loads(batch_64_path.read_text()) if batch_64_path.exists() else {"rows": []}
    batch_65_path = DATA / "icassp-2026-semantic-reviewed-batch-065.json"
    batch_65 = json.loads(batch_65_path.read_text()) if batch_65_path.exists() else {"rows": []}
    batch_66_path = DATA / "icassp-2026-semantic-reviewed-batch-066.json"
    batch_66 = json.loads(batch_66_path.read_text()) if batch_66_path.exists() else {"rows": []}
    batch_67_path = DATA / "icassp-2026-semantic-reviewed-batch-067.json"
    batch_67 = json.loads(batch_67_path.read_text()) if batch_67_path.exists() else {"rows": []}
    batch_68_path = DATA / "icassp-2026-semantic-reviewed-batch-068.json"
    batch_68 = json.loads(batch_68_path.read_text()) if batch_68_path.exists() else {"rows": []}
    batch_69_path = DATA / "icassp-2026-semantic-reviewed-batch-069.json"
    batch_69 = json.loads(batch_69_path.read_text()) if batch_69_path.exists() else {"rows": []}
    batch_70_path = DATA / "icassp-2026-semantic-reviewed-batch-070.json"
    batch_70 = json.loads(batch_70_path.read_text()) if batch_70_path.exists() else {"rows": []}
    batch_71_path = DATA / "icassp-2026-semantic-reviewed-batch-071.json"
    batch_71 = json.loads(batch_71_path.read_text()) if batch_71_path.exists() else {"rows": []}
    batch_72_path = DATA / "icassp-2026-semantic-reviewed-batch-072.json"
    batch_72 = json.loads(batch_72_path.read_text()) if batch_72_path.exists() else {"rows": []}
    batch_73_path = DATA / "icassp-2026-semantic-reviewed-batch-073.json"
    batch_73 = json.loads(batch_73_path.read_text()) if batch_73_path.exists() else {"rows": []}
    batch_74_path = DATA / "icassp-2026-semantic-reviewed-batch-074.json"
    batch_74 = json.loads(batch_74_path.read_text()) if batch_74_path.exists() else {"rows": []}
    batch_75_path = DATA / "icassp-2026-semantic-reviewed-batch-075.json"
    batch_75 = json.loads(batch_75_path.read_text()) if batch_75_path.exists() else {"rows": []}
    batch_76_path = DATA / "icassp-2026-semantic-reviewed-batch-076.json"
    batch_76 = json.loads(batch_76_path.read_text()) if batch_76_path.exists() else {"rows": []}
    batch_77_path = DATA / "icassp-2026-semantic-reviewed-batch-077.json"
    batch_77 = json.loads(batch_77_path.read_text()) if batch_77_path.exists() else {"rows": []}
    batch_78_path = DATA / "icassp-2026-semantic-reviewed-batch-078.json"
    batch_78 = json.loads(batch_78_path.read_text()) if batch_78_path.exists() else {"rows": []}
    batch_79_path = DATA / "icassp-2026-semantic-reviewed-batch-079.json"
    batch_79 = json.loads(batch_79_path.read_text()) if batch_79_path.exists() else {"rows": []}
    batch_80_path = DATA / "icassp-2026-semantic-reviewed-batch-080.json"
    batch_80 = json.loads(batch_80_path.read_text()) if batch_80_path.exists() else {"rows": []}
    batch_81_path = DATA / "icassp-2026-semantic-reviewed-batch-081.json"
    batch_81 = json.loads(batch_81_path.read_text()) if batch_81_path.exists() else {"rows": []}
    batch_82_path = DATA / "icassp-2026-semantic-reviewed-batch-082.json"
    batch_82 = json.loads(batch_82_path.read_text()) if batch_82_path.exists() else {"rows": []}
    batch_83_path = DATA / "icassp-2026-semantic-reviewed-batch-083.json"
    batch_83 = json.loads(batch_83_path.read_text()) if batch_83_path.exists() else {"rows": []}
    batch_84_path = DATA / "icassp-2026-semantic-reviewed-batch-084.json"
    batch_84 = json.loads(batch_84_path.read_text()) if batch_84_path.exists() else {"rows": []}
    batch_85_path = DATA / "icassp-2026-semantic-reviewed-batch-085.json"
    batch_85 = json.loads(batch_85_path.read_text()) if batch_85_path.exists() else {"rows": []}
    batch_86_path = DATA / "icassp-2026-semantic-reviewed-batch-086.json"
    batch_86 = json.loads(batch_86_path.read_text()) if batch_86_path.exists() else {"rows": []}
    batch_87_path = DATA / "icassp-2026-semantic-reviewed-batch-087.json"
    batch_87 = json.loads(batch_87_path.read_text()) if batch_87_path.exists() else {"rows": []}
    batch_88_path = DATA / "icassp-2026-semantic-reviewed-batch-088.json"
    batch_88 = json.loads(batch_88_path.read_text()) if batch_88_path.exists() else {"rows": []}
    batch_89_path = DATA / "icassp-2026-semantic-reviewed-batch-089.json"
    batch_89 = json.loads(batch_89_path.read_text()) if batch_89_path.exists() else {"rows": []}
    batch_90_path = DATA / "icassp-2026-semantic-reviewed-batch-090.json"
    batch_90 = json.loads(batch_90_path.read_text()) if batch_90_path.exists() else {"rows": []}
    reviewed_by_id = {row["paper_id"]: row for row in batch.get("rows", [])}
    reviewed_by_id.update({row["paper_id"]: row for row in batch_2.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_3.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_4.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_5.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_6.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_7.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_8.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_9.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_10.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_11.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_12.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_13.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_14.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_15.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_16.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_17.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_18.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_19.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_20.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_21.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_22.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_23.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_24.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_25.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_26.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_27.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_28.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_29.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_30.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_31.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_32.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_33.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_34.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_35.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_36.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_37.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_38.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_39.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_40.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_41.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_42.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_43.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_44.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_45.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_46.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_47.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_48.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_49.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_50.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_51.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_52.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_53.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_54.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_55.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_56.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_57.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_58.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_59.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_60.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_61.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_62.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_63.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_64.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_65.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_66.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_67.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_68.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_69.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_70.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_71.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_72.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_73.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_74.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_75.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_76.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_77.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_78.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_79.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_80.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_81.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_82.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_83.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_84.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_85.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_86.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_87.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_88.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_89.get("rows", [])})
    reviewed_by_id.update({row["paper_id"]: row for row in batch_90.get("rows", [])})
    reviewed_by_id = {
        paper_id: normalize_review_row(row, valid_concepts, canonical_triples)
        for paper_id, row in reviewed_by_id.items()
    }
    rows = []
    for paper in source["papers"]:
        text = f"{paper.get('title', '')}. {paper.get('abstract') or ''}".strip()
        in_scope = any(re.search(rf"\b{re.escape(term)}", text, re.I) for term in SPEECH_SCOPE)
        candidates = []
        for theme_id, subtheme_id, terms in RULES:
            hits = [term for term in terms if re.search(term_pattern(term), text, re.I)]
            if hits:
                candidates.append({
                    "theme_id": theme_id,
                    "subtheme_id": subtheme_id,
                    "matched_terms": hits,
                    "score": len(hits),
                    "evidence_excerpt": excerpt(text, hits[0]),
                })
        candidates.sort(key=lambda x: (-x["score"], x["theme_id"], x["subtheme_id"]))
        top = candidates[0]["score"] if candidates else 0
        tied = [x for x in candidates if x["score"] == top]
        if not in_scope:
            decision, confidence = "unsupported", "out-of-scope-for-speech-taxonomy"
        elif not candidates:
            decision, confidence = "insufficient-evidence", "low"
        elif top >= 2 and len(tied) == 1:
            decision, confidence = "supported", "machine-proposed"
        else:
            decision, confidence = "ambiguous", "machine-proposed"
        depth = "D2" if paper.get("abstract") else "D1"
        row = {
            "paper_id": paper["paperId"],
            "title": paper["title"],
            "source_url": paper.get("url"),
            "doi": paper.get("doi"),
            "evidence_depth": depth,
            "in_speech_audio_scope": in_scope,
            "candidate_assignments": candidates[:5],
            "decision": decision,
            "confidence": confidence,
            "alternative_assignment": candidates[1]["subtheme_id"] if len(candidates) > 1 else None,
            "review_state": "needs-analyst-semantic-review",
            "review_rule": "Title plus abstract candidate generation; ICASSP abstracts are unavailable for most records, and lexical presence is not final semantic membership.",
            "evidence_excerpt": excerpt(text, candidates[0]["matched_terms"][0]) if candidates and candidates[0].get("matched_terms") else paper["title"],
        }
        if paper["paperId"] in reviewed_by_id:
            reviewed = reviewed_by_id[paper["paperId"]]
            row.update({"decision": reviewed["decision"], "confidence": reviewed["confidence"], "review_state": reviewed["review_state"], "evidence_depth": reviewed["evidence_depth"], "analyst_review": reviewed})
        rows.append(row)
    counts = {key: sum(row["decision"] == key for row in rows) for key in ("supported", "unsupported", "ambiguous", "insufficient-evidence")}
    payload = {
        "schema_version": 1,
        "status": "analyst-reviewed-with-evidence-boundaries" if len(reviewed_by_id) == len(rows) else "machine-assisted-proposals-awaiting-semantic-review",
        "claim_boundary": "All 3,864 ICASSP records remain in the denominator. Non-speech records are explicit unsupported rows; title-only rows are D1 and cannot support abstract-level mechanism claims.",
        "source": "data/icassp-2026-papers.json",
        "taxonomy": "data/speech-first-principles-taxonomy.json",
        "paper_count": len(rows),
        "with_abstract": sum(row["evidence_depth"] == "D2" for row in rows),
        "decision_counts": counts,
        "reviewed_count": len(reviewed_by_id),
        "reviewed_batch_ids": [f"icassp-2026-semantic-batch-{index:03d}" for index in range(1, 90)],
        "rows": rows,
    }
    (DATA / "icassp-2026-semantic-review-queue.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    report = ["# ICASSP 2026 semantic review queue", "", payload["claim_boundary"], "", f"Records: **{len(rows)}**; abstracts: **{payload['with_abstract']}**; analyst-reviewed: **{payload['reviewed_count']}**", "", "| Decision | Count |", "|---|---:|"]
    report += [f"| {key} | {value} |" for key, value in counts.items()]
    report += ["", "The queue is deliberately broader than the speech slice so cross-venue denominators cannot silently drop non-speech ICASSP papers. ICASSP discovery metadata is not equivalent to official proceedings evidence.", ""]
    (HERE / "reports/ICASSP_2026_SEMANTIC_REVIEW_QUEUE.md").write_text("\n".join(report))
    print(json.dumps({"paper_count": len(rows), "with_abstract": payload["with_abstract"], "decision_counts": counts}))


if __name__ == "__main__":
    main()
