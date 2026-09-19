#!/usr/bin/env python3
"""Record the fourteenth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kibria25_interspeech": ("confirmed-current-boundary", "AttentiveMOS predicts listener quality ratings across domain shifts with a small model. The out-of-domain drop shows why a quality score needs its target and population stated.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "kim25d_interspeech": ("confirmed-current-boundary", "W-CTC forced alignment lets a streaming keyword spotter find arbitrary target words without separately prepared word alignments. The Libriphrase setting bounds the open-vocabulary claim.", "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition"),
    "lee25h_interspeech": ("confirmed-current-boundary", "The streaming TTS acoustic model trades codec decoding depth, quality, speaker similarity, and latency in a zero-shot speaker-conditioned setup. Its central object is waveform-generation efficiency and quality.", "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
    "lemaguer25_interspeech": ("confirmed-current-boundary", "The paper turns speech-synthesis listening studies into an inspectable protocol covering participants, bias, analysis, and limitations. It directly defines what a naturalness or quality claim does and does not establish.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "leschanowsky25_interspeech": ("reassigned-to-neighbor", "SITool measures whether codec output preserves intelligible words through diagnostic and modified rhyme tests. The main boundary is word understanding versus pleasant sound, not a waveform restoration intervention.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "li25ea_interspeech": ("confirmed-current-boundary", "SAFA creates a bilingual clinical annotation workflow that combines machine drafts with human correction and structured exports. It is data creation infrastructure, though no controlled time or agreement study is reported.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "makishima25b_interspeech": ("confirmed-current-boundary", "The audio-visual model assigns words and time intervals to visible speakers in overlap, making the speaker referent part of recognition. Constructed mixtures and visible faces bound the grounding claim.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "nguyen25_interspeech": ("confirmed-current-boundary", "Synthetic phrase mixing supplies code-switched examples for three under-resourced language pairs and tests ASR transfer. The method addresses language switching, while synthetic naturalness and community coverage remain limits.", "languages-accents-and-resources", "crosslingual-structure", "code-switching"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract", "method", "experiments", "results", "limits"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
