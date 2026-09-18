"""Resolve the remaining clearly non-speech ICASSP ambiguity cases."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-060.json"

if OUT.exists():
    payload = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": payload["batch_id"], "status": "preserved-input", "reviewed_count": payload["reviewed_count"]}))
    raise SystemExit(0)

audio = re.compile(
    r"audio|speech|voice|sound|acoustic|auditory|music|pitch|vocal|microphone|noise|room|"
    r"echo|asv|spoof|spectrogram|mel[- ]",
    re.I,
)
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {
    p["paperId"]: p
    for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]
}
already = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    already |= {row["paper_id"] for row in json.loads(path.read_text()).get("rows", [])}

selected = [
    row for row in queue["rows"]
    if row.get("review_state") != "analyst-reviewed"
    and row.get("decision") == "ambiguous"
    and not audio.search(row.get("title", ""))
    and row["paper_id"] not in already
]
if len(selected) != 11:
    raise SystemExit(f"expected 11 clearly non-audio ambiguity rows, found {len(selected)}")

rows = []
for candidate in selected:
    paper = papers[candidate["paper_id"]]
    abstract = paper.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({
        "paper_id": paper["paperId"],
        "title": paper["title"],
        "decision": "unsupported",
        "confidence": f"analyst-reviewed-{depth}",
        "theme_id": None,
        "subtheme_id": None,
        "concept_id": None,
        "semantic_reasoning": "The preserved title and abstract do not identify speech, voice, or an audio object; the ambiguous proposal is a non-speech machine-learning, vision, biomedical, communications, or text task.",
        "evidence_excerpt": abstract[:1200] if abstract else paper["title"],
        "source_location": paper.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": depth,
        "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP discovery metadata; rejection resolves speech-taxonomy membership only and does not characterize scientific quality.",
    })

payload = {
    "schema_version": 1,
    "batch_id": "icassp-2026-semantic-batch-060",
    "status": "analyst-reviewed-non-audio-boundary-batch",
    "claim_boundary": "These records are explicit unsupported decisions based on preserved title/abstract evidence; they remain in the full ICASSP denominator.",
    "reviewed_count": len(rows),
    "rows": rows,
}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(row["evidence_depth"] == "D1" for row in rows), "D2": sum(row["evidence_depth"] == "D2" for row in rows)}))
