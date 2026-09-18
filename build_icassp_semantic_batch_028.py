#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on voice privacy and provenance."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "ZK-VSA: Zero-Knowledge Verifiable Speaker Anonymization Leveraging Phase Vocoder with Time-Scale Modification": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy",
        "The title explicitly anonymizes and verifies a speaker identity with a zero-knowledge design; the ordinary problem is making speech useful while preventing listeners or systems from recovering who spoke.",
    ),
    "AURA: A Stegaformer-Based Scalable Deep Audio Watermark with Extreme Robustness": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability",
        "The title explicitly embeds a robust watermark in audio; the ordinary accountability problem is leaving evidence about origin or ownership that survives ordinary transformations without being confused with proof of truth.",
    ),
    "A Feature-Optimized Audio Watermarking Algorithm with Adaptive Embedding Strength": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability",
        "The title explicitly watermarks audio and adapts embedding strength; the conceptual tradeoff is making provenance evidence detectable while limiting audible change and surviving processing.",
    ),
    "Fake Speech Wild: Detecting Deepfake Speech on Social Media Platform": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title explicitly detects deepfake speech in social-media conditions; the ordinary security problem is deciding whether a convincing voice recording is genuine when compression, context, and attackers vary.",
    ),
    "Generalizable Detection of Audio Deepfakes": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title explicitly targets generalizable audio-deepfake detection; the core problem is finding manipulation cues that remain useful when the generator, speaker, channel, or attack is new.",
    ),
    "Subgraph Localization in the Subbands for Partially Spoofed Speech Detection": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title detects speech that is only partly spoofed and localizes evidence in frequency subbands; the ordinary problem is identifying which portion was manipulated instead of forcing an entire recording into one label.",
    ),
    "ECSA: Dual-Branch Emotion Compensation for Emotion-Consistent Speaker Anonymization": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy",
        "The title anonymizes speaker identity while compensating for emotion, matching the ordinary privacy problem of hiding who spoke without erasing what emotional state the speech communicates.",
    ),
    "PRSA: Preventing Malicious Speaker Recognition and Speech Synthesis Simultaneously with Adversarial Examples": (
        "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake",
        "The title protects against both malicious speaker recognition and speech synthesis, matching the coupled risk that a voice can identify a person and be reused to impersonate them.",
    ),
}

papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
rows = []
for paper in papers.values():
    if paper["title"] not in RULES:
        continue
    theme, subtheme, concept, reasoning = RULES[paper["title"]]
    abstract = paper.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({
        "paper_id": paper["paperId"], "title": paper["title"], "decision": "supported",
        "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme,
        "concept_id": concept, "semantic_reasoning": reasoning,
        "evidence_excerpt": abstract[:1200] if abstract else paper["title"],
        "source_location": paper.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": depth, "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP title/abstract evidence supports broad conceptual membership; full-paper mechanism and outcomes are not captured.",
    })

if len(rows) != len(RULES):
    missing = sorted(set(RULES) - {row["title"] for row in rows})
    raise SystemExit(f"expected {len(RULES)} exact titles, missing: {missing}")
payload = {
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-028",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-028.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
