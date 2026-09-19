#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kuhlmann25_interspeech": ("confirmed-current-boundary", "The abstract evaluates frame-level predictors of synthetic-speech quality and their ability to localize artificial distortions. The evidence supports quality and naturalness measurement, including its relation to human judgments, without making the predictor a universal perceptual standard.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "kuhne25_interspeech": ("confirmed-current-boundary", "The abstract explicitly develops and compares a single-channel speech-enhancement system and reports architecture and complexity ablations. The evidence supports speech-prior denoising, bounded by the VoiceBank+DEMAND experiments.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "kulkarni25_interspeech": ("confirmed-current-boundary", "The abstract traces the originating system of synthetic speech and evaluates in-domain and out-of-domain source tracing. The evidence supports spoofing and synthetic-voice misuse, bounded by the tested source-tracing scenarios.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "kulkarni25b_interspeech": ("confirmed-current-boundary", "The abstract evaluates voice anonymization for children across several datasets and measures both privacy protection and utility loss. The evidence supports voice privacy, with child speech and evaluation mismatch as explicit boundaries.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "kumar25_interspeech": ("confirmed-current-boundary", "The abstract jointly models dialect identification and ASR across Indian languages and thirty-three dialects. The evidence supports dialect and variety, bounded by the languages, dialects, and multimodal fusion tested.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "kumar25b_interspeech": ("confirmed-current-boundary", "The abstract explicitly detects spoken intent under noise and zero-shot cross-lingual conditions and evaluates gains from labeled and unlabeled data. The evidence supports intent in context, with the reported languages and datasets limiting transfer claims.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "intent-in-context"),
    "kumar25c_interspeech": ("confirmed-current-boundary", "The abstract performs direct speech-to-speech translation across languages through a language-agnostic articulatory representation and evaluates French-English and German-English pairs. The evidence supports cross-lingual transfer, bounded by those language pairs and the CVSS data.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "kumar25d_interspeech": ("confirmed-current-boundary", "The abstract probes ASR decoder and aligner evidence for spoken grammar-error detection and compares speaking conditions. The evidence supports temporal alignment as a bounded source of speech-to-text timing or confidence evidence, without claiming the aligner is error-free.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
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
