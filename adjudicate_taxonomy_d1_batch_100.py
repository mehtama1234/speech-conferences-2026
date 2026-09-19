#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "gu25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly pre-train speaker-verification representations for domain shifts across styles and languages. The evidence supports speaker verification, without proving domain-independent identity decisions.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "guillaume25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly model adaptation in speech production and the effect of interaction on a speaker's articulatory behavior. This is articulatory coordination, not adaptation of an ASR speaker model.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "gulzar25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly generate spoken-style task-oriented dialogue data to improve dialogue-state tracking under disfluencies and recognition errors. The evidence supports dialogue state, without proving general spoken interaction.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "guo25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly design a low-bitrate speech codec and measure intelligibility, quality, and codec efficiency. The governing boundary is bandwidth and resource budget, not voice conversion itself.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "guo25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use visual information to improve decoded speech quality and noise robustness in a neural codec. The evidence supports perceptual enhancement, without proving recovery of every original sample.", ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "guo25d_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly transcribe and detect dysfluency events, including context-dependent repetitions and disruptions. The precise boundary is preserving and locating disfluencies, not generic atypical articulation.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation"),
    "gupta25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly equalize an earbud's hear-through transfer function to approximate open-ear listening under user and fitting variation. This belongs under microphone and channel coloration, not multiple time scales.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "microphone-channel"),
    "gupta25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly design adaptive hear-through equalization for sound arriving from different directions while controlling filter stability and delay. The evidence supports microphone and channel coloration.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "microphone-channel"),
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
