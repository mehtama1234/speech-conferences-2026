#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "tian25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds open speech-language models by tokenizing speech, mixing speech and text streams, and training on paired speech-text plus text-only data. The evidence supports self-supervised-speech-units, bounded by the OpusLM family, released materials, stated scale, recognition/synthesis tests, and reported model-size/data-selection findings.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "tienkamp25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures articulatory clarity and variability before and six months after tongue-cancer surgery through vowel indices and formant dispersion. The evidence supports dysarthria-and-atypical-speech, bounded by 11 patients, matched controls, sentence reading, the two measures, and the observed post-surgery changes.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "titeux25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses ASR log-probability uncertainty as an automatic intelligibility measure and relates it to Huntington’s disease clinical scores. The evidence supports clinical-speech-marker, bounded by spontaneous pathological speech, ASR uncertainty, clinical-score linkage, and the stated noninvasive biomarker aim.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "toikkanen25_interspeech": (
        "confirmed-current-boundary",
        "The abstract distills an ensemble for respiratory-sound classification into a cheaper student using soft labels and tests architecture-independent gains. The evidence supports clinical-speech-marker, bounded by the ICHBI dataset, teacher/student variants, inference-cost motivation, and reported score comparisons.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "tomashenko25_interspeech": (
        "confirmed-current-boundary",
        "The abstract extracts context-dependent duration patterns that reveal speaker identity and uses them to attack speaker-verification and voice-anonymization systems. The evidence supports voice-privacy, bounded by the temporal embeddings, original and anonymized speech, attack models, and reported verification gains.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
    ),
    "toyin25_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases a multi-speaker Modern Standard Arabic corpus combining professional recordings, an adapted existing corpus, and synthetic speech, then demonstrates TTS and voice-conversion uses. The evidence supports speech-data-collection, bounded by 83.52 hours, 11 voices, diacritized text, corpus components, and research-use release.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "trachu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract exposes artifacts in spoofed speech by adding noise, extracting entangled artifacts with enhancement, and amplifying them before countermeasure detection. The evidence supports spoofing-and-deepfake, bounded by the model-agnostic pipeline, ASVspoof2019/2021 tests, enhancement variants, and reported detection gains.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "tran25_interspeech": (
        "confirmed-current-boundary",
        "The abstract aligns real and synthetic speech representations so controlled synthetic data can train ASR while reducing speaker-specific variation. The evidence supports speech-data-collection, bounded by R2S, gradient reversal, residual-vector pseudo-labels, three datasets, and reported ASR gains.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
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
