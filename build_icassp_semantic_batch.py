#!/usr/bin/env python3
"""Record a balanced ICASSP abstract-level semantic review batch."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "001d5225ef43f21ea65844aa6ecab2e628ea09f6": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing", "Neck acoustic sensing observes swallowing-related body vibration when ordinary airborne speech/audio is not the only useful signal; the sensing path is the conceptual center."),
    "06a45d5a7f24ca8a38dfc43d42033bc77ad32089": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "The method purifies noisy audio before visual/audio fusion so a recognizer receives speech evidence rather than treating every corrupted mixture as content."),
    "0170388633269ae1f3c8c47d58fad1dd2ec4e657": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment", "Chunkwise alignment addresses the tension between streaming latency and enough future context to place speech units correctly."),
    "1a0ad427c5f5480248c9b1cc7f5f09a702202b8d": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state", "StyleBench evaluates whether speech-language models can interpret and control conversational speaking style, where the same words can carry different interactional intent."),
    "353486bfb0c6f393f228880e50e484e9c9b12b45": ("voice-generation-and-control", "voice-identity-and-conversion", "speaker-identity", "Speaker drift detection asks whether a generated voice remains the intended identity over time rather than treating a plausible waveform as sufficient."),
    "3ac4c8f39bd3092d1fcc4d3d301aa709e481df81": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Clinical voice disease classification tests whether acoustic variation carries a health-related signal while domain shift threatens shortcut learning."),
    "1581712456d6dae2df3db44289a8f9e4fa4a5a87": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "MiLorE-SSL expands multilingual speech representations while trying not to forget earlier languages; sharing structure and preserving distinctions are both part of the problem."),
    "098f4e21120d05b0acb4c15705c1ba37e2a8e467": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use", "A perturbation-based faithfulness metric asks whether an acoustic anomaly explanation points to evidence that actually changes the decision, rather than merely producing a plausible highlight."),
}


def main() -> None:
    source = json.loads((DATA / "icassp-2026-papers.json").read_text())
    papers = {row["paperId"]: row for row in source["papers"]}
    rows = []
    for paper_id, (theme, subtheme, concept, rationale) in ASSIGNMENTS.items():
        paper = papers[paper_id]
        abstract = paper.get("abstract") or ""
        depth = "D2" if abstract else "D1"
        rows.append({
            "paper_id": paper_id,
            "title": paper["title"],
            "decision": "supported",
            "confidence": f"analyst-reviewed-{depth}",
            "theme_id": theme,
            "subtheme_id": subtheme,
            "concept_id": concept,
            "semantic_reasoning": rationale,
            "evidence_excerpt": abstract[:1000] if abstract else paper["title"],
            "source_location": paper.get("url"),
            "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
            "evidence_depth": depth,
            "review_state": "analyst-reviewed",
            "claim_boundary": "ICASSP Semantic Scholar/discovery record; title-only or abstract evidence is not official proceedings/full-paper evidence.",
        })
    payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-001", "status": "analyst-reviewed-seed-batch", "claim_boundary": "These eight assignments are analyst-reviewed from preserved ICASSP discovery records. They do not establish full-paper mechanisms or venue-wide prevalence.", "reviewed_count": len(rows), "rows": rows}
    (DATA / "icassp-2026-semantic-reviewed-batch-001.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D2": sum(row["evidence_depth"] == "D2" for row in rows), "D1": sum(row["evidence_depth"] == "D1" for row in rows)}))


if __name__ == "__main__":
    main()
