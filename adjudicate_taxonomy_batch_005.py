#!/usr/bin/env python3
"""Record the fifth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "balasubramanian25_interspeech": ("confirmed-current-boundary", "SMARTMOS predicts human audio-quality judgments under real-time constraints. The target is what listeners report, while annotator bias and unseen distortions limit the predictor.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "bandekar25_interspeech": ("confirmed-current-boundary", "The model infers moving vocal-tract trajectories from acoustic features and tests low-resource and unseen-speaker settings. Predicted movement is not direct imaging, but articulatory dynamics is the central object.", "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "bao25_interspeech": ("confirmed-current-boundary", "Bandwidth extension reconstructs missing high-frequency detail using local and global spectral context. The frequency representation and its time-scale tradeoffs make multi-resolution measurement the right boundary.", "sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "baser25_interspeech": ("confirmed-current-boundary", "WavShape tries to retain task information while reducing sensitive information in speech embeddings. The paper's central object is privacy leakage and its measurement, not generic fairness or recognition robustness.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "bashir25_interspeech": ("confirmed-current-boundary", "The proposed quality metric aligns time-modified speech before comparing modulation features and tests correlation with listening scores. Correlation under the stated degradations is not a complete model of understanding.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "bataev25_interspeech": ("confirmed-current-boundary", "NGPU-LM adds rare domain words during greedy decoding through a fast context-biasing lookup. The paper directly tests the accuracy-versus-compute boundary rather than broad language modeling.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "baumann25_interspeech": ("confirmed-current-boundary", "Pathology-aware pretraining adapts recognition to speech altered by medical conditions, with synthetic and selected data tested as alternatives. Etiology and corpus differences prevent treating one gain as universal clinical performance.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "behera25_interspeech": ("confirmed-current-boundary", "Test-time training adapts enhancement using the current noisy signal and an auxiliary objective without labeled target data. The adaptation cost and noise conditions bound claims about listener benefit.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
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
