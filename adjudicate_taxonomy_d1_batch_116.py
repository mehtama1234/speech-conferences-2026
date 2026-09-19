#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kim25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study an audio language model for vocal-health disorder classification and include safety and cross-lingual evaluation. The evidence supports a clinical speech marker, without establishing diagnosis or clinical deployment.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "kim25b_interspeech": ("reassigned-to-neighbor", "The abstract makes face-conditioned voice identity and controllable voice characteristics the central problem; text is used to control the generated speech rather than to plan its linguistic content. The closer boundary is speaker-identity representation, not text-to-speech planning.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "speaker-identity"),
    "kim25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly classify multiple speaking styles and analyze the effect of human agreement on those labels. The evidence supports paralinguistic state, without implying that the labels capture every stable speaker characteristic.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "kim25e_interspeech": ("reassigned-to-neighbor", "The abstract addresses voice cloning and lip-synchronization forgeries by embedding authentic audio for later recovery and tamper localization. The central consequence is detecting and resisting synthetic-voice misuse, more directly than general auditability of model decisions.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "kim25f_interspeech": ("confirmed-current-boundary", "The abstract studies progressive refinement of noisy speech and evaluates an efficient speech-enhancement architecture. The evidence supports speech-prior denoising, while the reported efficiency and enhancement results do not establish exact signal recovery.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "kim25g_interspeech": ("confirmed-current-boundary", "The abstract explicitly separates bona fide speech from generated spoofed speech and tests the method across synthetic-voice attack scenarios. The evidence supports spoofing and synthetic-voice misuse, bounded by the ASVspoof conditions.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "kim25h_interspeech": ("confirmed-current-boundary", "The abstract separates concurrent speech streams in continuous streaming mixtures and addresses speaker permutation across chunks. The central problem is inferring hidden sources from a mixture, which supports blind source separation.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "kim25i_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly develop layer aggregation for speaker verification and evaluate speaker embeddings on VoxCeleb. The evidence supports speaker verification, without treating the reported benchmark result as universal identity reliability.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
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
