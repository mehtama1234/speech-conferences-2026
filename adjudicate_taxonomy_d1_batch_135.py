#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "lu25h_interspeech": ("confirmed-current-boundary", "The abstract models transitions between fluent and stuttered speech with articulatory dynamics and tests predictions against real-time MRI. The evidence supports atypical articulation and dysarthria as the broader atypical-speech boundary, without equating stuttering with dysarthria.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "luan25_interspeech": ("rejected-out-of-scope", "The abstract restores generic degraded mel spectrograms with a visual model and does not establish a human-speech or spoken-language object. Audio restoration alone is insufficient for speech-taxonomy membership.", ["title", "abstract"], None, None, None),
    "luo25_interspeech": ("reassigned-to-neighbor", "The abstract's main deliverable is a Mandarin audio corpus with annotations for toxicity and toxic tone, followed by a detection baseline. The closer boundary is speech-data collection, while the annotations preserve prosodic and culturally situated meaning.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "luo25b_interspeech": ("confirmed-current-boundary", "The abstract develops enhancement and pseudo-labeling for far-field meeting speech with overlapping speakers and guided source separation, then evaluates ASR. The evidence supports target-conditioned separation, bounded by the MISP meeting setting and guided signals.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "luo25c_interspeech": ("confirmed-current-boundary", "The abstract estimates direct sound in real far-field recordings and uses those estimates as pseudo-labels to train speech enhancement. The evidence supports speech-prior denoising, bounded by the MISP2023 corpus and real-recording adaptation.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "lyu25_interspeech": ("confirmed-current-boundary", "The abstract models room impulse responses and their temporal sound-propagation structure for downstream speech synthesis. The evidence supports reverberant room mixture, bounded by the two real-world RIR datasets and reported T60 errors.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "reverberant-room-mixture"),
    "m25_interspeech": ("reassigned-to-neighbor", "The abstract evaluates fairness across dysarthric severity levels in cloned speech and finds a tradeoff among intelligibility, speaker similarity, and prosody. The central consequence is whether a speech system's claims hold across affected groups, so auditability and contestability is closer than atypical speech alone.", ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability"),
    "ma25_interspeech": ("confirmed-current-boundary", "The abstract maps speech to phonemes and then graphemes with an LLM decoder and evaluates cross-lingual ASR. The evidence supports acoustic-to-token mapping, bounded by the Polish and German experiments and the cascade's information loss.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
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
