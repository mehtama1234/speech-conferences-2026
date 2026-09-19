#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "dey25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study short-utterance spoken language identification and its cross-corpus behavior. The evidence supports language identification under crosslingual structure; it does not establish universal language coverage.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "language-identification"),
    "ding25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study linguistic masking in simulated electric-acoustic hearing and speech recognition under competing-language conditions. The evidence supports perceptual recovery; it does not establish general hearing-aid benefit.", ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "dinh25_interspeech": ("reassigned-to-neighbor", "The abstract explicitly studies acoustic echo cancellation with short frames and retained long context. The paper belongs under acoustic echo cancellation, not packet-loss concealment.", ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation"),
    "do25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly detect toxic spans in Vietnamese speech for content moderation. This is a speech-act and content-meaning problem, not cultural meaning or accent variation.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "speech-act"),
    "doan25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly trace the source of generated or deepfake audio. The paper belongs under spoofing and deepfake security, not waveform generation.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "dong25b_interspeech": ("reassigned-to-neighbor", "The title and abstract evaluate accentedness and comprehensibility with acoustic and ASR measures. The central boundary is the difference between machine error measures and human understanding, not prosodic meaning.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "dong25d_interspeech": ("reassigned-to-neighbor", "The title and abstract analyze neutral-tone realization in Beijing Mandarin and whether it carries phonological specification. This belongs under dialect and variety structure, not word-error evaluation.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "dong25e_interspeech": ("rejected-out-of-scope", "The title and abstract concern respiratory-sound classification and contain no speech or spoken-language object. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
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
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {
        d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated")
        for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})
    }
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
