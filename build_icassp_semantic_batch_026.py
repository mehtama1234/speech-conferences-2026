#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on language and speech access."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Unsupervised Sentence Stress Detection in L2 Spoken English Via Iterative Adaptation of Whisper ASR Framework": (
        "languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness",
        "The title detects sentence stress in second-language English and adapts a speech recognizer without supervision; the ordinary problem is interpreting prosodic structure when a learner's pronunciation differs from native training speech.",
    ),
    "Align2speak: Improving TTS for Low Resource Languages via ASR-Guided Online Preference Optimization": (
        "languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation",
        "The title explicitly improves text-to-speech for low-resource languages using an ASR-guided preference signal; the conceptual problem is producing usable speech when language-specific data and judgments are scarce.",
    ),
    "Mixtures of Lightweight Articulatory Experts for Multilingual Asr": (
        "languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer",
        "The title explicitly shares lightweight articulatory experts across multilingual ASR, matching the problem of transferring speech recognition knowledge while languages differ in sound inventories and articulation patterns.",
    ),
    "QE-XVC: Zero-Shot Cross-Lingual Voice Conversion via Query-Enhancement and Conditional Flow Matching": (
        "languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer",
        "The title explicitly converts a voice across languages without a target-language example; the ordinary problem is preserving speaker identity while changing the linguistic and phonetic content available to the system.",
    ),
    "SLM-TTA: A Framework for Test-Time Adaptation of Generative Spoken Language Models": (
        "recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing",
        "The title adapts a spoken language model at test time, matching the problem of handling a new speaker, domain, or context after deployment rather than assuming training and use conditions are identical.",
    ),
    "Dynamic Kalman Fusion for Robust Continuous Sign Language Recognition": (
        "people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication",
        "The title recognizes continuous sign language and emphasizes robust multimodal fusion; the ordinary communication problem is decoding a visual language when movement and timing vary across signers.",
    ),
    "When Children Talk and Machines Listen: Toward an Interpretable Speech-Based Screener for Dutch Developmental Language Disorder": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title explicitly screens developmental language disorder from children's Dutch speech and seeks interpretability; the conceptual problem is extracting developmental evidence without treating a screening score as a diagnosis.",
    ),
    "Cross-Lingual Alzheimer’s Disease Detection with Multimodal LLMs via Speech Cue-Augmented Prompting and Instruction Tuning": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title explicitly detects Alzheimer’s across languages using speech cues and multimodal prompting; the ordinary problem is separating health-related speech evidence from language-specific expression and data differences.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-026",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-026.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
