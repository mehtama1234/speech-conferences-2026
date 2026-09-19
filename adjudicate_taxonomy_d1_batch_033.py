#!/usr/bin/env python3
"""Record the twenty-second title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "8275f297b2313f31fd65c6575c3a94397c195fe2": ("confirmed-current-boundary", "The title explicitly concerns conversations collected for multimodal hearing-augmentation technology. Title-only evidence supports accessibility fit, without establishing user benefit.", "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "82a3da1717daccf026d9bfe2017feed5777efaf2": ("confirmed-current-boundary", "The title explicitly concerns content and channel factors in speaker-verification models. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "834c6c9aa5de738060ebf7e41deb082e5c23e7ae": ("confirmed-current-boundary", "The title explicitly concerns audiovisual speech enhancement and voice activity detection. Title-only evidence supports time-frequency masking within speech enhancement.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "85e5ce5a810c14e5d938d3d84b630468ea8a9797": ("confirmed-current-boundary", "The title explicitly concerns multilingual automatic speech recognition with articulatory experts. Title-only evidence supports cross-lingual transfer.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "881a4df4063ea083a8022d31dc9d3f2c61a1389b": ("reassigned-to-neighbor", "The title explicitly concerns beamforming with virtual microphones for hearing aids. The signal operation is spatial filtering, while title-only evidence does not establish broader accessibility fit.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "884a398170cf1e3ea9b63a455db42b433a5b4162": ("rejected-out-of-scope", "The title concerns spherical sound-source radiation reconstruction and does not establish a human-speech or spoken-language task. With title-only evidence, speech microphone membership is not supported.", None, None, None),
    "8b7e2132083c3aad254a6207cb4b7a29bf80fd3a": ("confirmed-current-boundary", "The title explicitly concerns production-scale dynamic vocabulary biasing for automatic speech recognition. Title-only evidence supports domain and context biasing.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "8b91884ff16133bdcfff32e9603382a16e131143": ("confirmed-current-boundary", "The title explicitly concerns domain-aware scheduling for automatic speech recognition fine-tuning. Title-only evidence supports domain and context biasing.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
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
