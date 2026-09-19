#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "f5e4f41e1b459fd296cd5a45e80375a4a50aeab2": ("confirmed-current-boundary", "The title explicitly concerns knowledge distillation for lightweight speaker verification. Title-only evidence supports speaker verification, without establishing verification performance or distillation benefit.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "f5ec0c9842e98d05fc40c3c9fa24dec1f0c6f222": ("rejected-out-of-scope", "The title concerns noise-aware audio-language embeddings but does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
    "f65d74bf58f68ec4f982955d7ad863c30f64ed8d": ("confirmed-current-boundary", "The title explicitly concerns voiced and unvoiced detection and fundamental-frequency estimation. Title-only evidence supports the periodic vocal-fold source, without establishing F0 or voicing accuracy.", "sound-and-production", "source-generation", "periodic-source"),
    "f6840c06e94a0b01e5ce1182a2fafadd05d4d5ec": ("confirmed-current-boundary", "The title explicitly concerns room-impulse-response generation from reverberant speech. Title-only evidence supports reverberant mixture, without establishing room-simulation fidelity.", "sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "f690ba7f54e1b6a949f489e28526128a416dcec0": ("rejected-out-of-scope", "The title concerns audio-effect estimation for general audio and does not establish a human-speech or spoken-language task. With title-only evidence, multiple-time-scale speech measurement is not supported.", None, None, None),
    "f764695fe9f3086c00bf0503517506a7a3666374": ("confirmed-current-boundary", "The title explicitly concerns noise-robust speech inversion together with speech enhancement. Title-only evidence supports speech-prior denoising, without establishing inversion or enhancement quality.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "f76b8e5bf1828e1a59fd362967dff8ccfb4b5521": ("confirmed-current-boundary", "The title explicitly concerns multilingual low-resource speech recognition. Title-only evidence supports few-shot adaptation, without establishing adaptation efficiency or recognition quality.", "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "f81fa194ade81067b617e35304194dd3e9884ff5": ("confirmed-current-boundary", "The title explicitly concerns binaural speech enhancement and preservation of spatial cues. Title-only evidence supports spatial filtering, without establishing spatial or enhancement quality.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
