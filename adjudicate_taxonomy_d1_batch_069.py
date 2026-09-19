#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "e65a730cec7f585fc8aca755c2b19470c1833614": ("confirmed-current-boundary", "The title explicitly concerns recorded doctor-patient and robot-patient medical dialogues for spoken-language processing. Title-only evidence supports speech data collection, without establishing dataset coverage or conversational quality.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "e6ecebcdaaebec99fdd11b8e6574469092ca2628": ("confirmed-current-boundary", "The title explicitly concerns a human-machine full-duplex dialogue system. Title-only evidence supports turn-boundary prediction, without establishing turn-taking or collaboration performance.", "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "e72eae582cd331df83d870bd11204aea7a896c83": ("confirmed-current-boundary", "The title explicitly concerns a curated multilingual speech dataset for speaker verification. Title-only evidence supports speech data collection, without establishing speaker coverage or verification performance.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "e94f98a316ccba4ec09e890e7cbcbc8f0c89c064": ("rejected-out-of-scope", "The title concerns general audio variational autoencoders and does not establish a human-speech or spoken-language task. With title-only evidence, waveform synthesis for speech is not supported.", None, None, None),
    "e9e185e3bf6b09df4f46488aa8e32a9523ce367a": ("rejected-out-of-scope", "The title concerns video-to-audio generation but does not establish a human-speech or spoken-language task. With title-only evidence, style and emotion control for speech is not supported.", None, None, None),
    "ea6f4e24aedef987b73c53cb293b2d591b947e13": ("rejected-out-of-scope", "The title explicitly concerns music source restoration rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "ea768741d49d91543ade5e922f0ba1ae227d9ad8": ("confirmed-current-boundary", "The title explicitly concerns speaker authentication and spoofing in a WildSpoof challenge. Title-only evidence supports spoofing and deepfake detection, without establishing challenge performance.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "ec65408836c71dd6bc75b0c2fbedd0fc9adf8928": ("reassigned-to-neighbor", "The title explicitly concerns prosody-guided neural vocoding. Title-only evidence places it under neural vocoder rather than the broader waveform-synthesis label.", "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
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
