#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "whetten25_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates self-supervised model quality during pretraining from embedding cluster quality and rank instead of relying on poorly predictive loss. The evidence supports calibration-and-selective-use, bounded by the unsupervised measures, downstream correlations, GPU/labeled-data savings, and model-evaluation setting.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use",
    ),
    "white25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures intervocalic /t/ variants in 183 Australian English speakers and relates them to exposure to community linguistic diversity. The evidence supports dialect-and-variety, bounded by the Voices of Sydney corpus, phonetic contexts, social/community comparison, and tap-variant result.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
    ),
    "white25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds typical speech reference intervals and tests deviations from them for depression symptom severity prediction, emphasizing interpretability. The evidence supports clinical-speech-marker, bounded by three reference datasets, demographic models, MDD participants, interval-derived deviations, and prediction comparisons.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "woszczyk25_interspeech": (
        "confirmed-current-boundary",
        "The abstract obfuscates dementia-related speech by transcribing, altering text, and resynthesizing it while measuring identity retention, adversarial recognition, quality, and WER. The evidence supports voice-privacy, bounded by ClaritySpeech, ADReSS/ADReSSo, zero-shot TTS, low-data operation, and reported tradeoffs.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
    ),
    "wu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract creates a challenge and dataset for detecting current suicide risk from natural speech of adolescents, with the aim of supporting early intervention. The evidence supports clinical-speech-marker, bounded by 600 participants aged 10–18, natural tasks, challenge design, and the stated correlation/health-risk aim; it does not establish clinical diagnosis or safe deployment.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "wu25d_interspeech": (
        "confirmed-current-boundary",
        "The archive abstract controls correlated acoustic feedback in multichannel devices with a recurrent model that combines spatial and temporal processing and several in-the-loop training strategies. The evidence supports nonstationary-noise, bounded by feedback/howling suppression, multichannel Wiener filtering, training variants, and stated low-compute enhancement.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "nonstationary-noise",
    ),
    "wu25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases a large open-domain video, speech, and transcript corpus across 16 domains and tests it for multimodal speech recognition. The evidence supports speech-data-collection, bounded by GALAXY, 8,270 hours, data-creation pipeline, transcription quality, domain/volume baselines, and stated multimodal uses.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "wu25f_interspeech": (
        "confirmed-current-boundary",
        "The abstract removes convolution from a streaming neural codec, using transformer and linear layers and measuring computation, bitrate, and quality against convolutional codecs. The evidence supports sampling-and-quantization, bounded by TS3-Codec, streaming operation, resource ratios, and the reported comparable/superior performance.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "sampling-and-quantization",
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
