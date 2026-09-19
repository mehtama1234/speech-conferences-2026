#!/usr/bin/env python3
"""Record the sixth abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "240230b87b7787f6291812ef5d42bcd25e1848f2": ("rejected-out-of-scope", "The abstract concerns controllable latent audio diffusion for Stable Audio, with intensity, pitch, and beats, but does not establish speech or spoken-language output.", None, None, None),
    "266bb3efdcaad92e310cbd6ca03cd33b2a99f98e": ("rejected-out-of-scope", "The abstract concerns stereo sound-event localization and detection in video, not speech or spoken-language sources.", None, None, None),
    "26776d22965ecc2ffb9597a0236a8adb00e56837": ("rejected-out-of-scope", "The abstract concerns mono-to-binaural general audio and music/video datasets, without a speech or spoken-language object.", None, None, None),
    "26ad929e3cfdc85cfe2776c18d31a5f3a43b9cae": ("confirmed-current-boundary", "The abstract explicitly concerns speech emotion recognition and recovery of paralinguistic cues lost through tokenization. D2 supports paralinguistic-state membership without full-paper verification.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "27bac793b2069d70bf0647d9d4e5ef10bd41e276": ("reassigned-to-neighbor", "The abstract explicitly concerns generative speech enhancement across noise and other distortions. Codec tokenization is the mechanism; enhancement quality is the task boundary.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "27bb0504e76395bf6ca8106929cc7b34f7c0ae06": ("rejected-out-of-scope", "The abstract concerns music captioning and music metadata, not speech or spoken-language audio.", None, None, None),
    "28017a19068a1c3689f41654551529b6c8c09350": ("rejected-out-of-scope", "The abstract concerns general neural audio codecs and semantic audio reconstruction without establishing a speech object.", None, None, None),
    "29ca7953fa676856885bb02de1fae27546be8a74": ("reassigned-to-neighbor", "The abstract explicitly concerns LLM-based speech recognition and instability caused by fixed prompts. The central move changes contextual conditioning, not acoustic-unit learning.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
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
