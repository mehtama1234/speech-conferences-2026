#!/usr/bin/env python3
"""Record the fourth abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "1581712456d6dae2df3db44289a8f9e4fa4a5a87": ("confirmed-current-boundary", "The abstract explicitly concerns multilingual self-supervised speech models, adding languages while limiting forgetting. D2 supports crosslingual transfer membership without full-paper validation.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "15d8dcdc31eb595bfcbe9afc625c0e58fef5c877": ("reassigned-to-neighbor", "The abstract explicitly concerns streaming ASR and questions transformer cost and latency under constrained deployment. The central pressure is resource budget, not long-context decoding itself.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "1a0ad427c5f5480248c9b1cc7f5f09a702202b8d": ("reassigned-to-neighbor", "StyleBench evaluates speech-language models controlling emotion, speed, volume, and pitch in dialogue. These are expressive delivery controls rather than dialogue-state prediction.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "1b7e4d682dce9825876280b45f3317f80d9bccbd": ("confirmed-current-boundary", "The abstract explicitly concerns spoken medical QA, ASR errors, and contextual correction of medical terms. Knowledge-guided domain biasing is the supported D2 boundary; full correction behavior remains unreviewed.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "1c2f7d77ed619dd8a3b40dc629777ba30d939b0f": ("rejected-out-of-scope", "The abstract concerns composed video retrieval with general audio and visual changes, not speech or spoken-language evidence.", None, None, None),
    "1c6d9829cb49bafa683cd2cfce1e1af06aae1d9b": ("confirmed-current-boundary", "The abstract uses audio and paralinguistic features to model graded emotion relationships across affective tasks. D2 supports paralinguistic-state membership, with the exact speech content of tasks still unreviewed.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "1cbb191e93366f884e689409fb3e7b6df42de9d4": ("confirmed-current-boundary", "The abstract explicitly evaluates front-end representations on speech recognition across tonal and non-tonal languages and measures cross-cultural performance gaps. The representation boundary is supported at D2.", "sound-and-production", "time-frequency-measurement", "windowed-spectrum"),
    "1d5b9c076d576ce6195793748ab20794afab84b8": ("rejected-out-of-scope", "The abstract concerns general room impulse-response simulation and reflector localization, without a speech or spoken-language object; room acoustics alone is insufficient for speech membership.", None, None, None),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
