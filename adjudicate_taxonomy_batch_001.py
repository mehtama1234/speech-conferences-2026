#!/usr/bin/env python3
"""Record the first D3 current-taxonomy adjudication batch.

These decisions are bounded to the captured paper text and the named current
concept boundaries. They are not claims that the papers' results reproduce.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "data/speech-taxonomy-adjudication-queue.json"

DECISIONS = {
    "a25_interspeech": {
        "decision": "confirmed-current-boundary",
        "note": "Sections 1-2 and the reported parameterized acoustic simulations support a source/tract physical-production question. The vocalizer is avian rather than human, so the membership is retained only as a physical vocal-production analogue, not evidence about human speech transfer.",
        "sections": "1. Introduction; 2. Experimental Framework; reported simulation/evaluation sections",
    },
    "abdullah25_interspeech": {
        "decision": "reassigned-to-neighbor",
        "note": "The paper uses voice conversion as augmentation, but the object being protected and evaluated is dialect evidence across domains. The current identity-and-conversion boundary is not the paper's main target; the current-taxonomy destination should be accent-robustness under accent-dialect-and-cultural-meaning.",
        "sections": "Introduction; method; cross-domain dialect-identification experiments; conclusion",
        "final_theme_id": "languages-accents-and-resources",
        "final_subtheme_id": "accent-dialect-and-cultural-meaning",
        "final_concept_id": "accent-robustness",
    },
    "aboeitta25_interspeech": {
        "decision": "confirmed-current-boundary",
        "note": "The benchmark compares acoustic encoders and language-aware decoding for dysarthric speech. The paper's central question is mapping damaged continuous acoustics to linguistic units; the clinical population is a boundary condition, not the main mechanism.",
        "sections": "1. Introduction; benchmark/method sections; results on TORGO and UASpeech",
    },
    "acevedo25_interspeech": {
        "decision": "confirmed-current-boundary",
        "note": "The paper changes audio-side representations under background-sound domain shift while retaining an open-vocabulary label target. That is a context/domain resolution problem, not pronunciation variation or waveform enhancement.",
        "sections": "1. Introduction; 2. Impact of Background Sounds; adaptation method and results",
    },
    "aggarwal25_interspeech": {
        "decision": "confirmed-current-boundary",
        "note": "The paper evaluates whether a system uses conversational/task context to judge the intended completeness of an answer. The target is an interactional interpretation, not prosodic state or acoustic alignment.",
        "sections": "1. Introduction; task and prompting method; class-wise evaluation",
    },
    "agrawal25_interspeech": {
        "decision": "confirmed-current-boundary",
        "note": "The paper tests speech-language understanding on unseen tasks using demonstrations and label/task context. The central evidence is context-dependent intended-task interpretation, so intent-and-dialogue-state is the closer boundary than acoustic-unit learning.",
        "sections": "1. Introduction; 3. Fine-Tuning Strategies; unseen-task evaluation",
    },
    "agrawal25b_interspeech": {
        "decision": "confirmed-current-boundary",
        "note": "The paper identifies rare or out-of-vocabulary bias phrases and merges them with the base recognition output. Its central problem is using context without replacing the observed acoustic sequence with an arbitrary word, which matches context-and-open-vocabulary.",
        "sections": "1. Introduction; proposed Spot and Merge method; biasing and recognition results",
    },
    "ahadzi25_interspeech": {
        "decision": "confirmed-current-boundary",
        "note": "The paper adapts a child-speech recognizer over sequential speaker batches while protecting earlier mappings from forgetting. Speaker-specific adaptation is the mechanism and context/continual recognition is the boundary; it is not a claim about age as a clinical marker.",
        "sections": "Introduction; continual-learning method; sequential MyST experiments and ablations",
    },
}


def main() -> None:
    payload = json.loads(PATH.read_text())
    by_id = {row["paper_id"]: row for row in payload["rows"]}
    changed = []
    for paper_id, decision in DECISIONS.items():
        row = by_id[paper_id]
        row["taxonomy_review_state"] = "taxonomy-adjudicated"
        row["final_decision"] = decision["decision"]
        row["reviewer_note"] = decision["note"]
        row["reviewed_sections"] = decision["sections"]
        if decision.get("final_theme_id"):
            row["final_theme_id"] = decision["final_theme_id"]
            row["final_subtheme_id"] = decision["final_subtheme_id"]
            row["final_concept_id"] = decision["final_concept_id"]
        else:
            row["final_theme_id"] = row["current_theme_id"]
            row["final_subtheme_id"] = row["current_subtheme_id"]
            row["final_concept_id"] = row["inherited_concept_id"]
        changed.append(paper_id)
    payload["adjudicated_count"] = sum(row.get("taxonomy_review_state") == "taxonomy-adjudicated" for row in payload["rows"])
    payload["open_count"] = sum(row.get("taxonomy_review_state") != "taxonomy-adjudicated" for row in payload["rows"])
    payload["decision_counts"] = {}
    for row in payload["rows"]:
        key = row.get("final_decision") or row.get("taxonomy_review_state")
        payload["decision_counts"][key] = payload["decision_counts"].get(key, 0) + 1
    PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"adjudicated": len(changed), "open": payload["open_count"], "decisions": payload["decision_counts"]}))


if __name__ == "__main__":
    main()
