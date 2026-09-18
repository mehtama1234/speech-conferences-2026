#!/usr/bin/env python3
"""Record the seventh small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "buker25_interspeech": ("confirmed-current-boundary", "Parameter sharing is evaluated inside spoofing-aware speaker verification across attacks and codecs. The system proxy and benchmark conditions do not establish safe authentication in the wild.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "byun25_interspeech": ("confirmed-current-boundary", "Voice-ENHANCE restores damaged recordings by combining acoustic correction with content- and speaker-conditioned generation. Its target is listener-useful repair, while word correctness and identity-faithful repair remain unproven.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "cai25_interspeech": ("confirmed-current-boundary", "The study measures whether an adult-trained aligner places vowel boundaries like human annotators in child speech. The evidence supports caution about semi-automatic temporal alignment within the stated corpus.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "carofilis25_interspeech": ("confirmed-current-boundary", "Incremental retraining and transcript filtering decide which pseudo-labels enter the next round when labeled target-domain speech is scarce. The mechanism is self-training, bounded by the two English corpora and filters.", "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels"),
    "cavalcanti25_interspeech": ("confirmed-current-boundary", "The paper separates speaker and dyad effects in the timing of turn exchange. Its central object is when a turn yields, with age, sex, topic, and relationship limits on generalization.", "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "chandra25b_interspeech": ("confirmed-current-boundary", "Attack-agnostic fake-speech detection is tested across changed attacks, codecs, and language conditions using representation suppression and shared projection. High residual error and benchmark coverage limit the security claim.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "chao25_interspeech": ("reassigned-to-neighbor", "The model predicts affective state variables such as valence, arousal, and dominance from speech and uses them to shape dialogue responses. That is evidence about a nonliteral speaker state, not primarily about pitch or timing marking linguistic meaning.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "chao25b_interspeech": ("confirmed-current-boundary", "USEMamba represents changing and damaged speech at multiple time and frequency scales, with regression and generation selected by distortion type. Challenge conditions and occasional wrong phonemes bound the result.", "sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
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
