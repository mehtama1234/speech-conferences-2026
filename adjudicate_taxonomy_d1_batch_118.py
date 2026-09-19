#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kim25r_interspeech": ("reassigned-to-neighbor", "The abstract models phonetic context and coarticulation in viseme transitions for speech-driven facial animation. The physical object is coordinated articulatory movement, not text-to-speech planning.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "kim25s_interspeech": ("reassigned-to-neighbor", "The abstract makes body-conduction and acoustic microphones complementary sensing paths and reconstructs speech while suppressing noise. The alternate sensor path is the governing boundary, more directly than generic speech-prior denoising.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "kim25t_interspeech": ("confirmed-current-boundary", "The abstract explicitly extracts and adjusts voiced-region style representations for expressive text-to-speech and reports style transfer and naturalness results. The evidence supports style and emotion control, bounded by the tested references and speakers.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "kim25u_interspeech": ("confirmed-current-boundary", "The abstract explicitly measures and reduces demographic performance disparities in automatic speech recognition. The evidence supports auditability and contestability of consequential speech systems, without proving fairness for every group or deployment.", ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability"),
    "kim25v_interspeech": ("confirmed-current-boundary", "The abstract localizes incoming speech with multichannel phase and spatial cues and evaluates angular error. The evidence supports spatial filtering and localization, bounded by the microphone setup and tested speech scenes.", ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "kim25w_interspeech": ("confirmed-current-boundary", "The abstract classifies dysarthria severity and uses synthesized speech to address speaker-independent clinical assessment. The evidence supports a clinical speech marker, without establishing clinical validity beyond the reported data.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "kirkland25_interspeech": ("reassigned-to-neighbor", "The abstract tests how disfluencies alter listeners' real decisions about whom or what to believe. The central object is a paralinguistic social cue and its effect on interpretation, not recognition-time preservation of disfluency events.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "klein25_interspeech": ("confirmed-current-boundary", "The abstract traces audio deepfake sources in an open-set setting and tests detection of unseen systems and distortions. The evidence supports spoofing and synthetic-voice misuse, bounded by the stated source-tracing protocol and augmentations.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
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
