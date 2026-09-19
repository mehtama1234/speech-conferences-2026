#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "nguyen25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether linguistic content changes the judgments of humans and deepfake detectors, treating synthetic speech and impersonation as the threat. The evidence supports spoofing and deepfake security, bounded by the gamified prototype and stated linguistic conditions.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "niculescu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures segmental prolongation as disfluent hesitation in spontaneous Romanian speech and reports its timing, frequency, and phonetic distribution. The evidence supports disfluency preservation, bounded by the four-speaker corpus and Romanian monologue recordings.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation",
    ),
    "nie25_interspeech": (
        "rejected-out-of-scope",
        "The abstract estimates heart rate from phonocardiogram recordings and compares acoustic foundation-model representations. It does not study spoken speech or spoken-language communication, so assigning it to clinical speech markers would overstate the evidence.",
        ["title", "abstract"], None, None, None,
    ),
    "niebuhr25_interspeech": (
        "confirmed-current-boundary",
        "The abstract relates prosodic, verbal, and visual properties to perceived charisma in CEO video speeches and identifies a role for prosody. The evidence supports paralinguistic state, bounded by expert ratings, DAX-40 field data, and the reported cross-modal analysis.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "niizumi25_interspeech": (
        "rejected-out-of-scope",
        "The abstract concerns respiratory sounds and foundation-model pretraining for a respiratory-audio benchmark, not spoken speech or spoken-language communication. A clinical-speech-marker assignment would therefore exceed the evidence boundary.",
        ["title", "abstract"], None, None, None,
    ),
    "nilsson25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract predicts speech quality in streaming conditions with spiking networks whose stated value is lower computation and energy on constrained devices. The governing boundary is latency and resource budget, not quality measurement alone.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "novitasari25_interspeech": (
        "confirmed-current-boundary",
        "The abstract aligns voice-activity-based text segmentation with ASR output segmentation so capitalization and punctuation recovery sees compatible units. The evidence supports alignment, bounded by pseudo-VAD segmentation and the reported formatting errors.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "novitasari25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract trains mixed-case end-to-end ASR with knowledge distillation and voice-activity cues while measuring formatted and unformatted recognition performance. The evidence supports acoustic-to-token mapping, bounded by the mixed-case task, teacher-student training, and comparable decoding cost.",
        ["title", "abstract", "full_paper_excerpt"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token",
    ),
}


def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({
            "taxonomy_review_state": "taxonomy-adjudicated",
            "final_decision": decision,
            "reviewer_note": note,
            "reviewed_sections": sections,
            "final_theme_id": theme,
            "final_subtheme_id": subtheme,
            "final_concept_id": concept,
        })
    adjudicated = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["adjudicated_count"] = adjudicated
    payload["open_count"] = len(rows) - adjudicated
    decisions = sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in decisions}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": adjudicated, "open": payload["open_count"]}))


if __name__ == "__main__": main()
