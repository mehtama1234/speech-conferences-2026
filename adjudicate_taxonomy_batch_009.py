#!/usr/bin/env python3
"""Record the ninth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "dai25c_interspeech": ("confirmed-current-boundary", "AISHELL-5 is a vehicle recording resource whose main value is preserving the talker-to-microphone path under reflections, road noise, and multiple speakers. Its Mandarin car setup bounds the channel claim.", "sound-and-production", "room-channel-and-sensing", "microphone-channel"),
    "dang25_interspeech": ("confirmed-current-boundary", "The analyzer chooses whether separation, denoising, or dereverberation is needed and avoids processing clean speech unnecessarily. Changing mixtures and simulated rooms make nonstationary adverse conditions the right boundary.", "listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "das25_interspeech": ("confirmed-current-boundary", "TRILL and TRILLsson representations are tested for spoof detection under in-domain and public-domain shifts. The central claim is resistance to synthetic voice misuse, bounded by the tested generators and corpora.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "deheerkloots25_interspeech": ("confirmed-current-boundary", "Layer probes and Dutch recognition tests ask what self-supervised representations encode and whether language-specific pretraining helps. Probe decodability is not causal proof, but learned speech units are the central object.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "dindart25_interspeech": ("confirmed-current-boundary", "M-mode ultrasound observes vocal-fold motion directly enough to compare its harmonics with acoustic f0. The study concerns a periodic physical source, with sampling and probe limits.", "sound-and-production", "source-generation", "periodic-source"),
    "do25_interspeech": ("confirmed-current-boundary", "PruneSLU reduces vocabulary and network structure so spoken intent and slot decisions fit on a constrained device. Reported model size and task scores do not establish energy or open-world performance.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "dong25_interspeech": ("reassigned-to-neighbor", "The paper trains or evaluates speech perception in multitalker babble by comparing human and neural responses; it does not enhance or denoise the waveform. Its evidence concerns listener effort and perceptual use under interference.", "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
    "du25_interspeech": ("confirmed-current-boundary", "The paper measures tonal contrasts in a specific Mienic variety and asks which acoustic differences carry linguistic information. Its language-specific contrast and speaker sample define the boundary.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
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
