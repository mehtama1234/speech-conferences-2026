#!/usr/bin/env python3
"""Record the ninth abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "396086a780ffd204b1a467bae77c39ad2885d0fd": ("rejected-out-of-scope", "The abstract concerns robust steganography for general audio diffusion and hidden messages, not speech or spoken-language evidence.", None, None, None),
    "39725966a2b75a4274a821bd6b7299794059e464": ("rejected-out-of-scope", "The abstract concerns personalized talking-face video synthesis and facial motion control conditioned on speech; the contribution is video avatar generation rather than a speech object or speech output.", None, None, None),
    "3a4364bbb5ad323940eb26c191336f1c18d40a45": ("confirmed-current-boundary", "The abstract explicitly concerns ASR with word-level timestamp alignment predicted jointly with transcripts. D2 supports temporal alignment membership.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "3ac4c8f39bd3092d1fcc4d3d301aa709e481df81": ("confirmed-current-boundary", "The abstract explicitly concerns clinical voice-based disease classification and domain-adaptive self-supervised learning on pathological voices. D2 supports clinical speech-marker membership without medical validation.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "3b9021143ff728a6cf7b3092c418c0ff60c1a85e": ("confirmed-current-boundary", "The abstract explicitly studies neural speech enhancement specialized to speaker, noise, language, and SNR contexts. Changing/adverse acoustic conditions are the evaluated boundary.", "listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "3c121afc5b615b8c5b4313e8cbb408d30773acd1": ("reassigned-to-neighbor", "The abstract explicitly concerns audio-visual speech recognition using subtitles and visual context to improve English and Chinese ASR. The visual stream is contextual evidence for recognition, not a crosslingual-transfer study.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "3cbf795dc7c05f7868348d9711e730ab2c01e380": ("rejected-out-of-scope", "The abstract concerns enhancement of animal vocalizations and biodiversity recordings, not human speech or spoken-language evidence.", None, None, None),
    "3eb2375221ef0a1352b192d43e73fff287cdb0b0": ("confirmed-current-boundary", "The abstract explicitly concerns Alzheimer's detection via pathological speech, with federated learning, augmentation, and acoustic-text fusion. D2 supports clinical speech-marker membership without diagnostic validation.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
