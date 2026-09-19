#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "d18190bbefd1c4b3729d5ac36ee6aafefcad56d9": ("confirmed-current-boundary", "The title explicitly concerns a streamable diffusion model for speech separation. Title-only evidence supports target-conditioned separation, without establishing streamability or separation quality.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "d18fc2002429dcb8aa66ab092aa490e10fde3560": ("confirmed-current-boundary", "The title explicitly concerns unsupervised domain adaptation in speech recognition using ensemble updates. Title-only evidence supports self-training, without establishing adaptation quality.", "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels"),
    "d1f80d0a8a7e06fa00f09c414e8496935f435430": ("confirmed-current-boundary", "The title explicitly concerns matching reverberant speech through learned acoustic embeddings. Title-only evidence supports reverberant mixture, without establishing acoustic matching quality.", "sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "d287262678f9e25dc2d91d324751b88a270ce02c": ("confirmed-current-boundary", "The title explicitly concerns robust automatic speech recognition by linking front-end and back-end processing. Title-only evidence supports end-to-end recovery, without establishing robustness across degradations.", "evaluation-deployment-and-consequence", "robustness-and-shift", "end-to-end-recovery"),
    "d2d66a6da68b92f5bc7bcd40e119c790ca381868": ("confirmed-current-boundary", "The title explicitly concerns streaming grapheme-to-phoneme conversion and prosody for unsegmented languages. Title-only evidence supports prosodic meaning, without establishing prosody quality or language coverage.", "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "d36a5fd23cf5960cafba67f8f84b825ef4ca1fee": ("confirmed-current-boundary", "The title explicitly concerns joint speech coding and enhancement. Title-only evidence supports perceptual enhancement, without establishing perceptual quality or coding tradeoffs.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "d434cb2b975c321e138b608a86834cef5f4f8dfe": ("confirmed-current-boundary", "The title explicitly concerns low-bandwidth, high-fidelity speech transmission using generative source-channel coding. Title-only evidence supports latency and resource budget, without establishing transmission quality or deployment cost.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "d4de91d048a62fbdd4717dd33d2fcb47d7035923": ("confirmed-current-boundary", "The title explicitly concerns a long-speech benchmark for transcription, translation, and understanding. Title-only evidence supports long-context decoding, without establishing benchmark coverage or model performance.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
