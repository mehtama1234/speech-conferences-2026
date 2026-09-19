#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "francis25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly describe augmentative and alternative communication for minimally verbal children, with personalized symbols and voices. The central boundary is augmentative communication, not only generation latency.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication"),
    "franzreb25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly anonymize converted speech and test which prosodic cues leak speaker identity. This is voice privacy, not unseen-speaker synthesis.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "fu25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly localize overlapping speakers from binaural cues in azimuth and elevation. This belongs under spatial filtering, not microphone and channel coloration.", ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "fucci25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly use feature attribution to reveal which acoustic cues an ASR model relies on. The central issue is auditability of model reasoning, not merely local frequency measurement.", ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability"),
    "fukunaga25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly predict listener backchannels and their surface forms in spoken dialogue. This is interactional feedback, not prediction of the speaker's turn boundary.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "interactional-feedback"),
    "funfgeld25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly study how intonation changes whether an utterance is heard as ironic or sincere. The central object is intent in context, not cultural meaning alone.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "intent-in-context"),
    "funk25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study prepubertal children's speech perception and the age-linked interpretation of acoustic gender cues. The evidence supports age and developmental speech, without establishing universal gender perception.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "futami25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly train a speech-to-speech translation system by interleaving text and speech units to improve modality planning. The evidence supports text-to-speech planning, without proving translation quality in every language.", ["title", "abstract"], "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
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
