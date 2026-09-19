#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "liu25n_interspeech": ("confirmed-current-boundary", "The abstract measures how sentence-final particles change speech rate and interactional form in child-directed versus adult-directed Mandarin. The evidence supports prosodic meaning, bounded by the mothers, task, and Mandarin particle categories.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "liu25o_interspeech": ("confirmed-current-boundary", "The abstract learns language-independent speech tokens with IPA targets and evaluates multilingual and cross-lingual speech synthesis. The evidence supports cross-lingual transfer, bounded by the languages and zero-shot synthesis tests.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "liu25p_interspeech": ("confirmed-current-boundary", "The abstract uses neural codec representations to denoise and expand speech bandwidth and evaluates quality and intelligibility on noisy narrow-band speech. The evidence supports perceptual enhancement, bounded by the codec and Valentini-Botinhao tests.", ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "ljubesic25_interspeech": ("confirmed-current-boundary", "The abstract identifies primary stress across Croatian, Serbian, a dialect, and Slovenian and explicitly treats stress as a meaning and comprehension cue. The evidence supports prosodic meaning, bounded by the languages, dialect, and word-level data.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "lo25_interspeech": ("confirmed-current-boundary", "The abstract tests whether tongue-shape and size patterns in vowel production distinguish speakers and evaluates them with likelihood ratios. The evidence supports speaker verification, bounded by the 40 English speakers and articulatory measurements.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "lobashev25_interspeech": ("confirmed-current-boundary", "The abstract performs training-free any-to-any cross-lingual voice conversion from a short reference and evaluates content preservation and robustness. The evidence supports voice conversion, bounded by the LibriSpeech and FLEURS experiments.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "lobato25_interspeech": ("confirmed-current-boundary", "The abstract changes TTS speaker embeddings to add graded Lombard characteristics as background noise increases while measuring identity and perceptual plausibility. The evidence supports within-speaker state variation, bounded by the Lombard corpus and listening tests.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation"),
    "lodagala25_interspeech": ("reassigned-to-neighbor", "The abstract's main contribution is a curated Arabic-English TTS corpus covering dialects, standard Arabic, and code-switching, with baseline evaluation. The closer boundary is speech-data collection rather than transfer alone.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
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
