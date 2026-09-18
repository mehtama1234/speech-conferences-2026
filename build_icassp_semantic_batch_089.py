#!/usr/bin/env python3
"""Record the remaining ICASSP metadata-only case with an explicit boundary."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUTPUT = DATA / "icassp-2026-semantic-reviewed-batch-089.json"
if OUTPUT.exists():
    existing = json.loads(OUTPUT.read_text())
    print(json.dumps({"batch_id": existing["batch_id"], "status": "preserved-input", "reviewed_count": existing["reviewed_count"]}))
    raise SystemExit(0)
PAPER_ID = "c71d62cdeed9e9283ef1c2373136ebd5b905c00c"
SESSION = "https://www.cmsworkshops.com/ICASSP2026/view_session.php?SessionID=1469&bare=1"
EVIDENCE = (
    "Official ICASSP 2026 session page lists LETPAV in the session "
    "‘Multimodal Fusion for Sentiment and Emotion Recognition’ and gives its "
    "title as ‘Lexicon-Enhanced Text with Progressive Audio-Visual Fusion for "
    "Multimodal Sentiment Analysis’; no abstract or speech-specific audio object "
    "is available in the preserved ICASSP input."
)
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
candidate = next(row for row in queue["rows"] if row["paper_id"] == PAPER_ID)
if candidate.get("review_state") == "analyst-reviewed" and candidate.get("decision") != "ambiguous":
    raise SystemExit("unexpected prior resolution")
row = {
    "paper_id": PAPER_ID,
    "title": candidate["title"],
    "decision": "insufficient-evidence",
    "confidence": "analyst-reviewed-D1",
    "theme_id": None,
    "subtheme_id": None,
    "concept_id": None,
    "semantic_reasoning": "The official session confirms an audio-visual sentiment paper, but the available title/session metadata does not establish that its audio is speech or identify a speech mechanism; retain as insufficient evidence rather than assign it to the speech taxonomy.",
    "evidence_excerpt": EVIDENCE,
    "source_location": SESSION,
    "source_sha256": hashlib.sha256(EVIDENCE.encode()).hexdigest(),
    "evidence_depth": "D1",
    "review_state": "analyst-reviewed",
    "claim_boundary": "Official session metadata resolves the evidence boundary only; it does not characterize the paper's audio input, method, result, or scientific quality.",
}
payload = {
    "schema_version": 1,
    "batch_id": "icassp-2026-semantic-batch-089",
    "status": "analyst-reviewed-insufficient-evidence-boundary",
    "claim_boundary": "This row remains in the full ICASSP denominator and is deliberately not counted as speech-taxonomy membership.",
    "reviewed_count": 1,
    "rows": [row],
}
OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": 1, "decision": row["decision"]}))
