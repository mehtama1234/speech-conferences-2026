#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "shams25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reconstructs perceived-speech semantics from intracranial EEG through neural/text alignment and a text generator for brain-computer-interface use. The evidence supports non-airborne sensing, bounded by iEEG, the low-data setting, and the reported neural-decoding results.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
    ),
    "shao25_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects Alzheimer’s disease by fusing acoustic and ASR-transcribed text features and reports performance on ADReSSo. The evidence supports clinical speech markers, bounded by the co-attention features, dataset, and 83.15% accuracy result.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "shao25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract refines weak labels for Thai ASR with a self-evolving process and compresses speech sequences to reduce computation, releasing refined transcripts. The evidence supports self-training and pseudo-label expansion, bounded by EThai-ASR and its Thai datasets.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "shao25c_interspeech": (
        "reassigned-to-neighbor",
        "The abstract measures stress-conditioned deaffrication and articulatory timing in Italian varieties, a pronunciation change rather than a meaning-bearing prosodic cue. The governing boundary is pronunciation variation, bounded by 15 speakers, nonce words, EMA/acoustic measures, and the stress positions.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "sharma25_interspeech": (
        "confirmed-current-boundary",
        "The abstract improves diffusion-based dereverberation with metric guidance and non-uniform state sampling and evaluates speech quality, distortion, and ASR effects. The evidence supports perceptual enhancement, bounded by StoRM, the stated losses, convergence changes, and reverberant-speech tests.",
        ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement",
    ),
    "sharma25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures the extent and speed of velum lowering and raising during nasal VCV production from real-time MRI across 68 speakers. The evidence supports articulatory coordination, bounded by the three vowels, two nasals, MRI measures, and observed asymmetries.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "sharon25_interspeech": (
        "confirmed-current-boundary",
        "The abstract decodes imagined and perceived speech from EEG, models non-activity periods as cognitive pauses, and measures syllabic-recognition gains. The evidence supports non-airborne sensing, bounded by EEG phases, continuous/isolated datasets, and the reported improvements.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
    ),
    "shashaank25_interspeech": (
        "confirmed-current-boundary",
        "The abstract verifies headphone users from inside-microphone speech under noise and spoofing risks and evaluates cross-device adaptation. The evidence supports speaker verification, bounded by 195 speakers, four devices, inside-mic data, and the single-device evaluation.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
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
