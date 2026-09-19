#!/usr/bin/env python3
"""Record the twenty-third title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "8bb0a3187e680dd770ec55c68546d74ef05e8216": ("confirmed-current-boundary", "The title explicitly concerns ALS dysarthria severity estimation from syllable-level acoustic modeling. Title-only evidence supports a clinical speech marker, without establishing clinical validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "8c34befb5bf60724639cf82f2b05b5a52242a7d2": ("confirmed-current-boundary", "The title explicitly concerns lightweight rapid speech synthesis. Title-only evidence supports waveform synthesis.", "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "8d037e8b595bec358b0e82835b2090c9cc2e6bee": ("confirmed-current-boundary", "The title explicitly concerns speech spoofing detection. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "8f29c9401994870d518c2d61ee27c4b5d95cf57f": ("rejected-out-of-scope", "The title concerns recognition of general audio deepfake generators but does not establish synthetic speech or spoken-language evidence. With title-only evidence, speech spoofing membership is not supported.", None, None, None),
    "912db650c4cc9a3db2cf2c003c7a1b797ca7009e": ("confirmed-current-boundary", "The title explicitly concerns text-prompted multichannel speech separation. Title-only evidence supports target-conditioned separation.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "916fc9493e71e7ab8bd6d8bb738923d276447efe": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "918f732e16d886a9034de5dcb511ec0f2233f100": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition in conversation. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "92eb25d6b6cf98610af79a4f3045a8b5779f26a9": ("confirmed-current-boundary", "The title explicitly concerns speech super-resolution across sampling rates. Title-only evidence supports perceptual enhancement.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
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
