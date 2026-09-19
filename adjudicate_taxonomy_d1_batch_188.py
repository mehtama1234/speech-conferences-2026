#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "xiang25_interspeech": (
        "confirmed-current-boundary",
        "The abstract recovers clean speech by separately modeling semantic and acoustic information with a factorized codec and diffusion model, then tests downstream TTS. The evidence supports speech-prior-denoising, bounded by the hierarchical SE method, difficult acoustic conditions, quality/SOTA comparisons, and TTS results.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "xiang25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract models Mandarin /ai/ formant trajectories across duration and speaking style to separate speech clarity from speech rate. The evidence supports vocal-tract-filter, bounded by conversational/read corpora, F1/F2 measures, GAMMs, duration range, and style comparison.",
        ["title", "abstract"], "sound-and-production", "source-generation", "vocal-tract-filter",
    ),
    "xiang25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes multiple simultaneous emotions by reweighting long-tail classes and modeling relationships among labels. The evidence supports paralinguistic-state, bounded by ER-ASCL, CMU-MOSEI and CNSCED, audio modality, accuracy comparisons, and class-imbalance setting.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "xiao25_interspeech": (
        "confirmed-current-boundary",
        "The abstract localizes sound sources from multichannel audio by fusing time and frequency features with bidirectional sequence processing. The evidence supports spatial-filtering, bounded by TF-Mamba, simulated and real datasets, spatial-feature extraction, and reported localization comparisons.",
        ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering",
    ),
    "xiao25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts keyword-spotting models at test time to unseen environments and noise using entropy confidence selection, normalization updates, and pseudo-keyword consistency. The evidence supports distribution-shift, bounded by AdaKWS, Gaussian/real noises, no original-training-data assumption, and reported robustness comparisons.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "xiao25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract traces newly appearing deepfake attack families while retaining old source classes without storing exemplars, using a fixed extractor and one-epoch analytical classifier update. The evidence supports auditability-and-contestability, bounded by AnaST, class-incremental source tracing, privacy/memory constraints, and baseline experiments.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability",
    ),
    "xiao25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects fake audio by making decisions per XLS-R layer and fusing those decisions instead of collapsing all representations first. The evidence supports spoofing-and-deepfake, bounded by layer-wise fusion, cross-dataset In-the-Wild evaluation, EER, transparency aim, and baseline comparisons.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "xiao25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects Alzheimer’s dementia from language-model perplexity and examines an interpretable decision boundary and generated-response differences. The evidence supports clinical-speech-marker, bounded by paired Mistral-7B models, ADReSS 2020 comparison, reported accuracy gains, and the language-pattern analysis.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
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


if __name__ == "__main__":
    main()
