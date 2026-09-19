#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ou25_interspeech": (
        "confirmed-current-boundary",
        "The abstract purifies speech representations and aligns them with text for end-to-end translation across English, German, and French. The evidence supports cross-lingual transfer, bounded by the CMSP-ST method and MuST-C/CoVoST-2 evaluations.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "ozer25_interspeech": (
        "rejected-out-of-scope",
        "The abstract benchmarks watermarking for a mixed collection of speech, environmental sounds, and music and does not identify a spoken-speech or spoken-language-specific threat or mechanism. Generic audio watermarking is outside this speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "ozyilmaz25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts ASR across five Arabic dialects and compares dialect-specific with pooled models under data scarcity. The evidence supports dialect and variety, bounded by the named dialects, datasets, Whisper fine-tuning, and reported pooling comparison.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
    ),
    "pahuja25_interspeech": (
        "rejected-out-of-scope",
        "The abstract tracks unspecified sound sources from EEG signals in cocktail-party scenes and does not establish spoken speech or a spoken-language task. Generic auditory scene analysis is outside this speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "paierl25_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts when a conversational partner will produce a backchannel from continuously extracted acoustic features for real-time human-robot interaction. The evidence supports turn boundary, bounded by the timing prediction task and reported latency/accuracy.",
        ["title", "abstract"], "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary",
    ),
    "pallala25_interspeech": (
        "confirmed-current-boundary",
        "The abstract extracts an enrolled target speaker from mixtures with a compact low-latency model for constrained devices. The evidence supports target-conditioned separation, bounded by the three-second enrollment, model budgets, and streaming extraction setting.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "palzer25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract assigns and separates multiple speakers through diarization, attractor representations, and permutation-invariant detection without selecting one enrolled target. The governing boundary is blind source separation, not target-conditioned separation.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation",
    ),
    "pan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract extracts a selected speaker from audio-visual mixtures using visual and acoustic cues in an online setting and tests changes in the attended target. The evidence supports target-conditioned separation, bounded by LRS3, streaming constraints, and SI-SNRi results.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
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
