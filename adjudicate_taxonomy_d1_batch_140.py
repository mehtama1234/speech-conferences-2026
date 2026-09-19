#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "mcghee25_interspeech": ("confirmed-current-boundary", "The abstract models acoustic-to-articulatory inversion and tests whether articulatory targets remain consistent across speakers and languages. The evidence supports articulatory coordination, bounded by the English and Russian data and inversion evaluation.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "mcguire25_interspeech": ("confirmed-current-boundary", "The abstract measures lip trajectories and gestural timing for Vietnamese implosives with electromagnetic articulography and compares them across languages. The evidence supports articulatory coordination, bounded by the Central Vietnamese and Taiwanese Southern Min samples.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "medennikov25_interspeech": ("reassigned-to-neighbor", "The abstract tracks all arriving speakers in streaming diarization with a cache of speaker embeddings and does not require a selected target enrollment. The governing boundary is assigning hidden concurrent sources, so blind source separation is closer than target-conditioned separation.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "mehralian25_interspeech": ("confirmed-current-boundary", "The abstract uses geographic metadata to adapt ASR across dialect regions and interpolate to unseen locations. The evidence supports dialect and variety, bounded by the regions, coordinates, and ASR tests.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "mena25_interspeech": ("confirmed-current-boundary", "The abstract improves Catalan-Spanish ASR under alternating-language speech using synthetic, concatenated, and real code-switched data. The evidence supports code-switching, bounded by the language pair and Whisper fine-tuning experiments.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "code-switching"),
    "menezes25_interspeech": ("confirmed-current-boundary", "The abstract recognizes silent phonemes from radar and optopalatographic articulatory signals and evaluates their combination as a silent-speech interface. The evidence supports non-airborne speech sensing, bounded by the three German speakers and 26-phoneme corpus.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "meng25_interspeech": ("confirmed-current-boundary", "The abstract trains speaker-recognition models across private clients with federated feature anchors and evaluates VoxCeleb and CN-Celeb performance. The evidence supports speaker verification, bounded by the federated setup and two benchmarks.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "meng25b_interspeech": ("confirmed-current-boundary", "The abstract measures how much temporal context speech models actually use for pitch, phone, and word tasks and tests streaming HuBERT operation. The evidence supports long-context decoding, bounded by the models and effective-context measurements.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
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
