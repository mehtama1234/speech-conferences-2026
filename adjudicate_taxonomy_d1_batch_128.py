#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "li25k_interspeech": ("reassigned-to-neighbor", "The abstract performs speaker diarization by clustering and assigning overlapping speaker communities, not by deciding whether two enrollment recordings share an identity. The governing boundary is assigning hidden concurrent sources, so blind source separation is closer than speaker verification.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "li25l_interspeech": ("reassigned-to-neighbor", "The abstract develops audio-visual speaker diarization and improves timestamp predictions through multimodal attention and label refinement. The task assigns overlapping speaker sources over time, so blind source separation is closer than identity verification.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "li25m_interspeech": ("confirmed-current-boundary", "The abstract applies GR-KAN layers to time-frequency and time-domain speech enhancement and evaluates quality and parameter cost. The evidence supports speech-prior denoising, bounded by VoiceBank-DEMAND and the tested architectures.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "li25n_interspeech": ("confirmed-current-boundary", "The abstract evaluates whether synthesized Chinese dysarthric speech supplements authentic data for dysarthric recognition and identifies acoustic mismatches. The evidence supports atypical articulation and dysarthria, including the explicit limit that synthetic speech is not a substitute.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "li25p_interspeech": ("confirmed-current-boundary", "The abstract adapts multilingual ASR with language-specific LoRA experts and evaluates language-aware and language-agnostic recognition. The evidence supports cross-lingual transfer, bounded by the target languages and Whisper-based experiments.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "li25q_interspeech": ("reassigned-to-neighbor", "The abstract compresses and prunes an audiovisual ASR encoder and reports reduced computation alongside recognition quality under noise. The governing deployment pressure is latency and resource budget, rather than the existence of acoustic-to-token mapping alone.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "li25r_interspeech": ("confirmed-current-boundary", "The abstract uses explicit text modeling inside voice conversion and evaluates preservation of linguistic content and target-speaker characteristics. The evidence supports voice conversion, bounded by the reported autoregressive framework and metrics.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "li25s_interspeech": ("confirmed-current-boundary", "The abstract refines denoised, dereverberated, and separated speech for listener-perceived quality and evaluates generalization across impairment sources. The evidence supports perceptual enhancement, bounded by the internal front-end pipeline and quality tests.", ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
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
