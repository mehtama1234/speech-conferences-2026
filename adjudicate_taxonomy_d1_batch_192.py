#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "yang25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract adds visual speech information to Whisper through cross-attention and lightweight adapters, improving recognition in difficult acoustic conditions. The evidence supports acoustic-to-token, bounded by AVWhisper-LoRA, the frozen Whisper backbone, LRS3-TED, visual guidance, and reported ASR comparisons.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token",
    ),
    "yang25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates whether audio-language models can retrieve and combine facts across multiple speech or audio inputs, rather than merely extract each fact. The evidence supports referential-grounding, bounded by the SAKURA benchmark, multi-hop questions, the tested LALMs, and the reported failure to integrate correctly extracted information.",
        ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding",
    ),
    "yang25i_interspeech": (
        "confirmed-current-boundary",
        "The paper measures the timing of prenuclear glides and neighboring segments in Hefei Mandarin to infer how those gestures are coordinated within the syllable. The evidence supports articulatory-coordination, bounded by CjV/CwV syllables, acoustic measurements, glide status, and the comparison with prior Mandarin analyses.",
        ["title", "abstract", "full_paper"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "yang25j_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates the internal language model learned by CTC with label-context-dependent distillation and tests it across domains. The evidence supports domain-and-context-biasing, bounded by CTC, the proposed regularizers, LibriSpeech and TED-LIUM, cross-domain evaluation, and reported WER improvement.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing",
    ),
    "yang25k_interspeech": (
        "confirmed-current-boundary",
        "The abstract enhances multichannel speech by compressing spectral and spatial microphone information into Mel representations and producing enhanced LogMel spectra online. The evidence supports spatial-filtering, bounded by Mel-McNet, STFT-to-Mel processing, CHiME-3, waveform/ASR use, complexity reduction, and enhancement results.",
        ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering",
    ),
    "yang25l_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects spoofed audio while addressing shifts among attack types and domains through hierarchical representations and feature whitening. The evidence supports spoofing-and-deepfake, bounded by Poin-HierNet, the Poincare-space prototypes, four ASVspoof/In-the-Wild datasets, and reported EER comparisons.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "yang25m_interspeech": (
        "confirmed-current-boundary",
        "The abstract expands a multilingual ASR model to unseen languages with language-aware soft prompts that encode shared and language-specific features while limiting new computation. The evidence supports crosslingual-transfer, bounded by LAPT/SPT-Whisper, FLEURS languages, continual expansion, interference risk, and reported WER gains.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "yang25n_interspeech": (
        "confirmed-current-boundary",
        "The abstract retrieves long audio for complex text queries by matching multiple events through chunk aggregation, captions, and language-model refinement, and introduces matching benchmarks. The evidence supports open-vocabulary-recognition, bounded by LARCQ, Clotho-LARCQ and SoundDescs-LARCQ, long-audio chunking, caption refinement, and reported recall results.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition",
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
