#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "loweimi25_interspeech": ("confirmed-current-boundary", "The abstract predicts depression and anxiety scores from spontaneous speech and tests the effect of transcript quality on those predictions. The evidence supports a clinical speech marker, bounded by the PsyVoiD recordings, HADS scores, and zero-shot LLM setting.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "lu25_interspeech": ("confirmed-current-boundary", "The abstract develops a hierarchical deep-filtering model for real-time single-channel speech enhancement and reports quality and resource comparisons. The evidence supports speech-prior denoising, bounded by the stated enhancement experiments.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "lu25b_interspeech": ("reassigned-to-neighbor", "The abstract denoises discrete acoustic tokens from noisy reference speech so a zero-shot TTS system can synthesize cleaner speech. The governing operation is speech-prior denoising, not text-to-speech content planning.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "lu25c_interspeech": ("confirmed-current-boundary", "The abstract benchmarks instruction following in speech-aware language models and separates speech perception from following a supplied instruction. The evidence supports speech act interpretation, bounded by the benchmark prompts and tested models.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "speech-act"),
    "lu25d_interspeech": ("confirmed-current-boundary", "The abstract aligns structured linguistic and acoustic representations for Mandarin end-to-end ASR and evaluates the resulting knowledge transfer. The evidence supports acoustic-to-token mapping, bounded by the graph-matching formulation and Mandarin experiments.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "lu25e_interspeech": ("confirmed-current-boundary", "The abstract predicts phoneme positions jointly with acoustic codes in zero-shot TTS to reduce skipped and repeated content. The evidence supports text-to-speech planning, bounded by the phoneme-position mechanism and reported zero-shot tests.", ["title", "abstract"], "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "lu25f_interspeech": ("reassigned-to-neighbor", "The abstract analyzes tone-sandhi directionality as a function of syntactic structure and generation in Tianjin Mandarin. The governing boundary is prosodic meaning and structure, rather than cultural meaning alone.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "lu25g_interspeech": ("reassigned-to-neighbor", "The abstract tests how listeners normalize talker-specific variation while identifying Mandarin and Cantonese words. The governing operation is adapting recognition to a speaker, rather than a within-speaker production state.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
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
