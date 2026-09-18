#!/usr/bin/env python3
"""Supersede the metadata-only LETPAV row with an official-session boundary."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUTPUT = DATA / "icassp-2026-semantic-reviewed-batch-090.json"
if OUTPUT.exists():
    existing = json.loads(OUTPUT.read_text())
    print(json.dumps({"batch_id": existing["batch_id"], "status": "preserved-input", "reviewed_count": existing["reviewed_count"]}))
    raise SystemExit(0)

paper_id = "c71d62cdeed9e9283ef1c2373136ebd5b905c00c"
title = "LETPAV: Lexicon-Enhanced Text with Progressive Audio-Visual Fusion for Multimodal Sentiment Analysis"
source = "https://www.cmsworkshops.com/ICASSP2026/view_session.php?SessionID=1469&bare=1"
evidence = (
    "Official ICASSP 2026 session page places LETPAV in ‘Multimodal Fusion for "
    "Sentiment and Emotion Recognition’ and lists its title as audio-visual "
    "multimodal sentiment analysis; no abstract or speech-specific audio object "
    "is available in the preserved ICASSP input."
)
row = {
    "paper_id": paper_id,
    "title": title,
    "decision": "insufficient-evidence",
    "confidence": "analyst-reviewed-D1",
    "theme_id": None,
    "subtheme_id": None,
    "concept_id": None,
    "semantic_reasoning": "The official session confirms an audio-visual sentiment paper, but the available evidence does not establish that its audio is speech or identify a speech mechanism; retain it as insufficient evidence rather than force a speech-taxonomy assignment.",
    "evidence_excerpt": evidence,
    "source_location": source,
    "source_sha256": hashlib.sha256(evidence.encode()).hexdigest(),
    "evidence_depth": "D1",
    "review_state": "analyst-reviewed",
    "claim_boundary": "Official session metadata resolves the evidence boundary only; it does not characterize the audio input, method, result, or scientific quality.",
}
payload = {
    "schema_version": 1,
    "batch_id": "icassp-2026-semantic-batch-090",
    "status": "analyst-reviewed-insufficient-evidence-boundary",
    "claim_boundary": "This later adjudication supersedes the earlier title-only ambiguity for LETPAV while preserving the row in the full ICASSP denominator.",
    "reviewed_count": 1,
    "rows": [row],
}
OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": 1, "decision": row["decision"]}))
