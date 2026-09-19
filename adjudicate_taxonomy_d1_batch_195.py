#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "yu25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses synchronized visual and acoustic input to extract a requested speaker while operating causally and in real time. The evidence supports target-conditioned-separation, bounded by online AV-CrossNet, one-frame look-ahead, audio/visual compression, adverse acoustic conditions, and the reported latency/size results.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "yu25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract actively changes a speaker's speech so voice-conversion systems cannot reliably extract identity, while keeping the result natural and defending against white-box and black-box attacks. The evidence supports spoofing-and-deepfake, bounded by Mimic Blocker, self-supervised adversarial training, pretrained feature extractors, and the stated privacy/quality results.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "yuan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract makes a speech-enhancement discriminator aware of the acoustic scenario and frequency regions so it can judge reconstructed speech more appropriately across conditions. The evidence supports speech-prior-denoising, bounded by SaD, scenario-aware discrimination, frequency-domain division, three generator models, two public datasets, and the reported gains.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "yue25_interspeech": (
        "confirmed-current-boundary",
        "The abstract documents how atypical-speech projects collect, annotate, use, and share data, then proposes common practices so results can be compared and reproduced. The evidence supports speech-data-collection, bounded by seven academic/clinical projects, atypical speech, standardization/harmonization, and the practical-guideline scope.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "yuen25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures speech-initiation time as phonological and syntactic complexity change the amount of structure a speaker must plan, including how many prosodic words are held in context. The evidence supports long-context-decoding, bounded by the reading-aloud task, prosodic-word and noun-phrase manipulations, and the reported interaction.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding",
    ),
    "zapata25_interspeech": (
        "confirmed-current-boundary",
        "The abstract treats speech-based text entry as an accessibility problem shaped by language, user needs, writing process, and interaction context. The evidence supports accessibility-fit, bounded by the emerging multimodal text-entry project, diverse languages/users/use cases, inclusion, and preservation of linguistic heritage.",
        ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit",
    ),
    "zeng25_interspeech": (
        "confirmed-current-boundary",
        "The abstract recovers longer audio from shared training gradients by segmenting spectrograms dynamically, exposing that distributed-learning updates can contain reconstructable speech. The evidence supports perceptual-enhancement, bounded by gradient inversion, long sequences, spectrogram segmentation, diverse acoustic features, and the abstract-level recovery claim.",
        ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement",
    ),
    "zevallos25_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares a state-space ASR model with a Transformer across nine languages and differing data amounts, focusing on performance and resource use when data are scarce. The evidence supports few-shot-adaptation, bounded by ConMamba versus Conformer, short/long context, WER, training time, memory, inference speed, and language coverage.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation",
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
