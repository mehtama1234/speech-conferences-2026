#!/usr/bin/env python3
"""Record an evidence-bounded ICASSP batch on spoken interaction."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

RULES = {
    "Leveraging Speaker and Listener Personalities and Their Interactions for Speech Emotion Recognition": (
        "meaning-and-interaction", "prosody-and-intent", "paralinguistic-state",
        "The title models both speaker and listener personalities in speech emotion recognition; the ordinary problem is that emotional interpretation depends on who expresses, who hears, and how their interaction shapes the signal's meaning.",
    ),
    "Stress Prediction from Temporal Emotion Trajectories in Clinical Patient-Physician Conversations": (
        "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker",
        "The title predicts stress over time in clinical conversations; the ordinary problem is using changing conversational speech as health evidence without collapsing a situated interaction into a static diagnosis.",
    ),
    "Unit-Based Agent for Semi-Cascaded Full-Duplex Dialogue Systems": (
        "meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary",
        "The title explicitly targets full-duplex dialogue and a semi-cascaded agent, matching the ordinary problem of listening and speaking concurrently while deciding when a turn has begun, yielded, or been interrupted.",
    ),
    "Toward Conversational User Interface via Voice Command Correction": (
        "meaning-and-interaction", "dialogue-and-turn-taking", "repair-and-clarification",
        "The title explicitly corrects voice commands in a conversational interface; the ordinary problem is recovering from a misunderstood request through a repair exchange rather than silently executing the wrong action.",
    ),
    "The RL-R Chat Dataset: Egocentric Conversations among Familiar Interlocutors for Multi-Modal Hearing Augmentation Technology": (
        "people-variation-and-health", "human-centered-evaluation", "accessibility-fit",
        "The title provides familiar-person conversations for hearing augmentation, matching the ordinary accessibility problem of preserving useful conversational context for a listener whose hearing access is incomplete.",
    ),
    "QFOCUS: Controllable Synthesis for Automated Speech Stress Editing to Deliver Human-Like Emphatic Intent": (
        "meaning-and-interaction", "prosody-and-intent", "prosodic-meaning",
        "The title edits speech stress to deliver emphatic intent, matching the ordinary problem of changing what a listener understands as emphasis without changing the words themselves.",
    ),
    "Human-Machine Full-Duplex Dialogue System with Left-Right Brain Division of Labor and Collaboration": (
        "meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary",
        "The title explicitly builds a full-duplex human-machine dialogue system; the conceptual challenge is coordinating listening, speaking, interruption, and response timing when both sides may act at once.",
    ),
    "A Personalized Real-Time Proactive Voice Memory Assistant": (
        "meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state",
        "The title explicitly describes a personalized proactive voice assistant with memory; the ordinary problem is maintaining conversational and user context while deciding when an assistant should speak without being asked.",
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
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-031",
    "status": "analyst-reviewed-title-bounded-speech-assignments",
    "claim_boundary": "These records are analyst-supported speech assignments using title-only or abstract evidence; they do not claim full-paper mechanism or outcome analysis.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-031.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": len(rows)}))
