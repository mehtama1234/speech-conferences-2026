#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "mitsumori25_interspeech": ("reassigned-to-neighbor", "The abstract selects acoustically relevant donor clips across languages to improve low-resource ASR transfer. The governing boundary is cross-lingual transfer, not few-shot adaptation from a small target support set.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "mittal25_interspeech": ("reassigned-to-neighbor", "The abstract synchronizes ASR and language-model decoder states across differing tokenizations and evaluates low-resource languages. The central operation is aligning acoustic and linguistic sequences, not simply using longer context.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "miyahara25_interspeech": ("reassigned-to-neighbor", "The abstract detects stuttering from temporal acoustic structure and explicitly targets monitoring of people who stutter. The governing boundary is atypical speech, rather than a general clinical marker detached from the speech condition.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "mizumoto25_interspeech": ("confirmed-current-boundary", "The abstract compares synthetic and real data for training speech language models and measures the quality and distribution tradeoffs. The evidence supports speech-data collection and creation, bounded by ASR and speech-translation experiments.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "mohamedismailyasararafath25_interspeech": ("reassigned-to-neighbor", "The abstract introduces a naturally elicited multimodal stress database and derives speech-breathing measures for stress detection. The principal resource contribution is speech-data collection, while stress is the annotated state.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "mohammadamini25_interspeech": ("confirmed-current-boundary", "The abstract pseudo-labels thousands of hours of Kurdish speech with recognition and translation pipelines for low-resource speech translation. The evidence supports self-training and pseudo-label expansion, bounded by the component quality and FLEURS evaluation.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels"),
    "mojarad25_interspeech": ("confirmed-current-boundary", "The abstract studies ASR errors on African American English phonological and lexical patterns and compares language-model context effects. The evidence supports dialect and variety, bounded by CORAAL, the two variables, and tested ASR systems.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "mondal25_interspeech": ("confirmed-current-boundary", "The abstract compares word prominence and its acoustic and lexical correlates across English and Malayalam bilingual speech while preserving expressive prompts. The evidence supports prosodic meaning, bounded by the IViE prompts and bilingual recordings.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": sections, "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
