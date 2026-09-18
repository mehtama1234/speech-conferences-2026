#!/usr/bin/env python3
"""Record the fourth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "asali25_interspeech": ("confirmed-current-boundary", "SASV must combine claimed-speaker evidence with evidence that the signal is genuine. The score-aware gated modules directly address spoof resistance, while unseen attacks and thresholds limit the claim.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "ashihara25_interspeech": ("confirmed-current-boundary", "The paper studies what discrete audio tokens preserve across speech, music, and general audio and how token use changes by domain. It is a representation question, not proof that the tokens are universal linguistic units.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "avidan25_interspeech": ("confirmed-current-boundary", "Deep-Simplex separates multichannel mixtures while treating source count and computation as part of the problem. Microphone geometry, rooms, and synthetic mixtures bound the evidence.", "listening-and-separation", "source-separation", "blind-source-separation"),
    "azzouz25_interspeech": ("confirmed-current-boundary", "Acoustic-to-articulatory inversion reconstructs hidden vocal-tract movement from sound, so the central object is coordinated physical motion rather than source/filter description alone. MRI speakers and protocol bound the result.", "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "b25_interspeech": ("confirmed-current-boundary", "The structured codebook is a speech prior used to make enhancement cheaper while retaining quality on VoiceBank-DEMAND. It does not establish downstream recognition or broad perceptual benefit.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "bafna25_interspeech": ("confirmed-current-boundary", "The paper tests whether language identification shortcuts on accent and first language, then measures and reduces that confusion. Its corpus and accent categories bound the fairness interpretation.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "bai25_interspeech": ("confirmed-current-boundary", "Accent normalization changes pronunciation while trying to preserve the speaker, making accent evidence the central boundary. High post-conversion WER and subjective accent definitions limit the claim.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "bakkouche25_interspeech": ("confirmed-current-boundary", "The listening study separates naturalness from speaker similarity and links their ratings to prosodic variation in generated clones. Listener and prompt choices prevent treating one acoustic change as a universal fix.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
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
