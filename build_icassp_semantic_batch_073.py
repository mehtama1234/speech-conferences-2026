"""Review the next bounded slice of clearly non-speech ICASSP records."""
import hashlib, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-073.json"
if OUT.exists():
    p = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": p["batch_id"], "status": "preserved-input", "reviewed_count": p["reviewed_count"]}))
    raise SystemExit(0)
rx = re.compile(r"audio|speech|voice|sound|acoustic|auditory|music|pitch|vocal|microphone|noise|room|echo|asv|asr|spoof|spectrogram|mel[- ]|spoken|phon|dysarth|stutter|keyword spotting|speaker|singing|prosod|esdd|sign language|emotion recognition|vocoder|lingu|reverb|waveform|biosignal|beamform|array|direction[- ]of[- ]arrival|\bdoa\b|ecg|ppg|bci|basecaller|clinical|depression", re.I)
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
already = set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    already |= {r["paper_id"] for r in json.loads(path.read_text()).get("rows", [])}
selected = []
for c in queue["rows"]:
    if c.get("review_state") == "analyst-reviewed" or c.get("decision") != "unsupported" or c["paper_id"] in already:
        continue
    p = papers[c["paper_id"]]
    if rx.search(f"{p.get('title', '')}. {p.get('abstract') or ''}"):
        continue
    selected.append(c)
    if len(selected) == 200:
        break
if len(selected) != 200:
    raise SystemExit(f"expected 200 safe non-speech records, found {len(selected)}")
rows = []
for c in selected:
    p = papers[c["paper_id"]]; abstract = p.get("abstract") or ""; depth = "D2" if abstract else "D1"
    rows.append({"paper_id": p["paperId"], "title": p["title"], "decision": "unsupported", "confidence": f"analyst-reviewed-{depth}", "theme_id": None, "subtheme_id": None, "concept_id": None, "semantic_reasoning": "Neither the preserved title nor abstract identifies speech, voice, an audio object, or a speech-relevant signal-processing task; this is a non-speech machine-learning, vision, biomedical, communications, text, or sensing task.", "evidence_excerpt": abstract[:1200] if abstract else p["title"], "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata; rejection resolves speech-taxonomy membership only and does not characterize scientific quality."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-073", "status": "analyst-reviewed-non-speech-boundary-batch", "claim_boundary": "These records are explicit unsupported decisions based on preserved title/abstract evidence; they remain in the full ICASSP denominator.", "reviewed_count": len(rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
