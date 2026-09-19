#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "jin25d_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly perform text-driven voice conversion with independent control of target timbre and environment while retaining source content. This is voice conversion, not prosody control alone.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "jing25_interspeech": ("rejected-out-of-scope", "The title and abstract concern singing melody extraction from polyphonic music rather than ordinary human speech or spoken-language evidence. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
    "jing25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly extract a target speaker from multi-talker speech using direction of arrival and beamwidth conditioning. This is target-conditioned separation, not spatial filtering alone.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "johnson25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use human-in-the-loop annotation and LLM assistance to improve speech transcripts and named-entity labels while reducing annotation effort. The evidence supports speech data collection and curation.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "jon25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly recognize emotion and emotional attributes in natural speech using acoustic, textual, and uncertainty-aware representations. The evidence supports paralinguistic state, without resolving all annotator disagreement.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "jones25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly introduce a multilingual multi-modal corpus for speaker recognition with repeated recordings and audio-visual baselines. The evidence supports speaker verification, without proving identity certainty.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "joshi25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly create a rural Bhojpuri women speech benchmark and test synthetic augmentation for inclusive ASR. The evidence supports speech data collection, without proving equal performance across all marginalized groups.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "joubaud25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly evaluate body-conducted speech enhancement using forehead, in-ear, and throat sensors and separate intelligibility, quality, and identity outcomes. The evidence supports non-airborne speech sensing, without proving every sensor or speaker condition.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
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
