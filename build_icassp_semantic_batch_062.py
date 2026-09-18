"""Review a bounded, evidence-safe slice of clearly non-speech ICASSP records."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-062.json"

if OUT.exists():
    payload = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": payload["batch_id"], "status": "preserved-input", "reviewed_count": payload["reviewed_count"]}))
    raise SystemExit(0)

speech_or_signal = re.compile(
    r"audio|speech|voice|sound|acoustic|auditory|music|pitch|vocal|microphone|noise|room|"
    r"echo|asv|asr|spoof|spectrogram|mel[- ]|spoken|phon|dysarth|stutter|keyword spotting|"
    r"speaker|singing|prosod|esdd|sign language|emotion recognition|vocoder|lingu|reverb|"
    r"waveform|biosignal|beamform|array|direction[- ]of[- ]arrival|\bdoa\b|ecg|ppg|bci|"
    r"basecaller|clinical|depression",
    re.I,
)
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
already = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    already |= {row["paper_id"] for row in json.loads(path.read_text()).get("rows", [])}

selected = []
for candidate in queue["rows"]:
    if candidate.get("review_state") == "analyst-reviewed" or candidate.get("decision") != "unsupported":
        continue
    if candidate["paper_id"] in already:
        continue
    paper = papers[candidate["paper_id"]]
    text = f"{paper.get('title', '')}. {paper.get('abstract') or ''}"
    if speech_or_signal.search(text):
        continue
    selected.append(candidate)
    if len(selected) == 100:
        break
if len(selected) != 100:
    raise SystemExit(f"expected 100 safe non-speech records, found {len(selected)}")

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
        "semantic_reasoning": "Neither the preserved title nor abstract identifies speech, voice, an audio object, or a speech-relevant signal-processing task; this is a non-speech machine-learning, vision, biomedical, communications, text, or sensing task.",
        "evidence_excerpt": abstract[:1200] if abstract else paper["title"],
        "source_location": paper.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": depth,
        "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP discovery metadata; rejection resolves speech-taxonomy membership only and does not characterize scientific quality.",
    })

payload = {
    "schema_version": 1,
    "batch_id": "icassp-2026-semantic-batch-062",
    "status": "analyst-reviewed-non-speech-boundary-batch",
    "claim_boundary": "These records are explicit unsupported decisions based on preserved title/abstract evidence; they remain in the full ICASSP denominator.",
    "reviewed_count": len(rows),
    "rows": rows,
}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
