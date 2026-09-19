#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "efe12b9be500170b4441691f784a08eb6aab9a95": ("reassigned-to-neighbor", "The title explicitly concerns accent cues in voice anonymisation and the risk of identity leakage. Title-only evidence places it under voice privacy rather than within-speaker state variation.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "eff379d6545c6ed72544a72932676e3c90849bd0": ("reassigned-to-neighbor", "The title explicitly concerns speech-recognition evaluation across Indian languages. Title-only evidence places it under cross-lingual transfer rather than domain and context biasing.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "f029a2feba6282850dda13ba6d32e6b0224d4780": ("reassigned-to-neighbor", "The title explicitly concerns robust evaluation of speech-quality estimation models under dataset concealment. Title-only evidence places it under quality and naturalness rather than calibration and selective use.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "f05330e1e98c24c3e89a734e3e9f454439ab7fc8": ("rejected-out-of-scope", "The title concerns speaker orientation and direction-of-arrival estimation but does not establish a human-speech or spoken-language task. With title-only evidence, microphone and channel coloration membership is not supported.", None, None, None),
    "f0556f0e9a554c6cbf114ea04659792c4d3a15e7": ("confirmed-current-boundary", "The title explicitly concerns generative speech enhancement and separation. Title-only evidence supports blind source separation, without establishing separation or enhancement quality.", "listening-and-separation", "source-separation", "blind-source-separation"),
    "f055e70a53e3f09ceb592427159e000554c0f6a6": ("confirmed-current-boundary", "The title explicitly concerns malicious speaker recognition and speech synthesis under adversarial examples. Title-only evidence supports spoofing and deepfake detection, without establishing security protection.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "f05884d7d29f9638836ac2787ddf9d4c4ec1aa44": ("confirmed-current-boundary", "The title explicitly concerns code-mixed speech in a sign-language video-synthesis system. Title-only evidence supports code-switching, without establishing synthesis quality or signer consistency.", "languages-accents-and-resources", "crosslingual-structure", "code-switching"),
    "f0855377153ed857c099d62cf84a0bdedeb3db2d": ("confirmed-current-boundary", "The title explicitly concerns flow-matching text-to-speech. Title-only evidence supports waveform synthesis, without establishing synthesis quality or the effect of neighborhood consistency.", "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness"),
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
