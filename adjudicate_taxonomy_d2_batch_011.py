#!/usr/bin/env python3
"""Record the eleventh abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "4a964c86c015577ecd5ba1c8992e72660a14f0f5": ("rejected-out-of-scope", "The abstract concerns distributed active noise control for general acoustic fields; it does not establish a human-speech or spoken-language task.", None, None, None),
    "4c29ff8d5dc5dbf70edfd7a15fc89aed700b7dae": ("rejected-out-of-scope", "The abstract evaluates controllable music generation representations and singing-free music audio models, not human speech or spoken-language evidence.", None, None, None),
    "4c589eb3c34e0392a3a48628968622729c2863d6": ("rejected-out-of-scope", "The abstract concerns long-form kitchen activity recognition and captioning from general audio, not speech or spoken-language evidence.", None, None, None),
    "4e2277ac4c784e9160a7a2be1ad4a2d96d9f5420": ("rejected-out-of-scope", "The abstract concerns singing voice style conversion; the contribution is singing/music generation rather than ordinary human speech or spoken-language evidence.", None, None, None),
    "4ee203fff1f9320565d56faad3953ae137fd56d8": ("rejected-out-of-scope", "The abstract studies sampling-frequency mismatch in audio source separation and reports music-source experiments; it does not establish a speech task.", None, None, None),
    "4fcfd39662d5cfc1f2cebc993ec26a8e25818573": ("confirmed-current-boundary", "The abstract explicitly studies continual multilingual expansion of self-supervised speech models using ASR and language identification. D2 supports cross-lingual transfer membership.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "4fefa1205b52a1f2f7293341ae89374bd200695e": ("confirmed-current-boundary", "The abstract explicitly applies the proposed stable audio architecture to speech dereverberation. D2 supports reverberant-room-mixture membership.", "sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "50bb514fcea96ad5e0f8474fcc57e43bc3c15e6a": ("confirmed-current-boundary", "The abstract explicitly probes prosodic and lexical cues for human-robot speech turn-taking and predicts turn boundaries. D2 supports turn-boundary prediction membership.", "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
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
