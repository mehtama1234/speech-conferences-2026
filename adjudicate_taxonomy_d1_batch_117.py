#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kim25j_interspeech": ("confirmed-current-boundary", "The abstract explicitly detects synthetic speech and uses perceived naturalness to improve robustness across deepfake examples. The evidence supports spoofing and synthetic-voice misuse, bounded by the ASVspoof 2021 DF evaluation.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "kim25k_interspeech": ("reassigned-to-neighbor", "The abstract combines role labels, speaker-change timing, diarization, and ASR for professional conversations. Its central operation is aligning speakers and turns with recognized words, not inferring an unobserved dialogue state.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "kim25l_interspeech": ("reassigned-to-neighbor", "The abstract studies end-to-end speaker diarization, including overlapping speech and speaker transitions. The task assigns concurrent speech to hidden sources over time, so blind source separation is closer than speaker verification.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "kim25m_interspeech": ("reassigned-to-neighbor", "The abstract generates speech responses conditioned on conversation mood and responsive style, with voice descriptions carrying paralinguistic information. The governing speech operation is controllable prosody and style, rather than merely measuring interactional feedback.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "kim25n_interspeech": ("confirmed-current-boundary", "The abstract jointly enhances noisy speech and extracts noise while preserving speaker-relevant features for speaker verification. Speaker verification remains the target evidence, with the enhancement path serving that identity decision.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "kim25o_interspeech": ("rejected-out-of-scope", "The title and abstract describe a general neural audio codec and do not establish a human-speech or spoken-language object. Low delay and reconstruction quality alone do not support membership in this speech taxonomy.", ["title", "abstract"], None, None, None),
    "kim25p_interspeech": ("confirmed-current-boundary", "The abstract detects suicidal risk from speech-derived transcripts and evaluates cross-language risk assessment. This supports a clinical speech marker, while the reported model results do not establish clinical safety or diagnosis.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "kim25q_interspeech": ("confirmed-current-boundary", "The abstract explicitly enhances noisy speech by modeling temporal and spectral context and reports objective speech-enhancement results. The evidence supports speech-prior denoising, without proving recovery of every signal detail.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
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
