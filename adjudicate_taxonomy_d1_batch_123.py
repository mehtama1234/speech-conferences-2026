#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "lahtinen25_interspeech": ("reassigned-to-neighbor", "The abstract's main deliverable is a spontaneous Finnish affective speech corpus and a sampling procedure for obtaining varied affective annotations. Affect is the corpus property; data creation is the governing research boundary.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "lalay25_interspeech": ("confirmed-current-boundary", "The abstract estimates room impulse responses from dry and reverberant speech and models decay and microphone effects for dereverberation. The evidence supports reverberant room mixture, bounded by the proof-of-concept speech signals and objective tests.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "reverberant-room-mixture"),
    "lameris25_interspeech": ("reassigned-to-neighbor", "The abstract directly manipulates voice-quality features and measures their perceived intimacy, valence, and investment. The governing operation is controllable vocal style and affect, not changing speaker identity through voice conversion.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "langman25_interspeech": ("confirmed-current-boundary", "The abstract constructs a large, metadata-rich speech dataset and describes segmentation, bandwidth estimation, and speaker detection for high-bandwidth speech synthesis. The evidence supports speech-data collection, bounded by LibriVox provenance and English coverage.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "laquatra25_interspeech": ("confirmed-current-boundary", "The abstract addresses recognition of dysarthric speech and combines ASR with generative error correction on structured and spontaneous clinical speech. The evidence supports atypical articulation and dysarthria, without claiming equal performance across disorders or speakers.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "lay25_interspeech": ("confirmed-current-boundary", "The abstract performs online speech enhancement under changing noise and explicitly trades denoising performance against buffer delay. The evidence supports changing and adverse noise, bounded by the reported GPU and latency conditions.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "lay25b_interspeech": ("confirmed-current-boundary", "The abstract demonstrates real-time diffusion speech enhancement on a laptop and makes sub-second latency, reverberant noise, and speech quality the deployment constraints. The evidence supports latency and resource budget, bounded by the demonstration setting.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "le25_interspeech": ("confirmed-current-boundary", "The abstract develops a multilingual speech-translation system across six language directions and measures the tradeoff between translation quality and inference efficiency. The evidence supports cross-lingual transfer, bounded by the evaluated languages and translation benchmark.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
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
