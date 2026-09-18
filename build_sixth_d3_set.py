#!/usr/bin/env python3
"""Materialize four already-captured official PDFs as a new D3 set."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SELECTED = {
    "sound-and-production/source-filter-production": "bandekar25_interspeech",
    "evaluation-deployment-and-consequence/privacy-security-and-accountability": "baser25_interspeech",
    "languages-accents-and-resources/multilingual-and-crosslingual": "bhattacharya25_interspeech",
    "meaning-and-interaction/dialogue-and-turn-taking": "elmers25_interspeech",
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
rows = []
for subtheme, paper_id in SELECTED.items():
    paper = papers[paper_id]
    pdf = DATA / "interspeech-2025-pdfs" / f"{paper_id}.pdf"
    text_path = DATA / "interspeech-2025-text" / f"{paper_id}.txt"
    if not pdf.exists() or not text_path.exists():
        raise SystemExit(f"captured PDF/text missing for {paper_id}")
    raw = pdf.read_bytes()
    text = text_path.read_text()
    reader = PdfReader(str(pdf))
    rows.append({
        "subtheme": subtheme, "paper_id": paper_id, "title": paper["title"],
        "paper_url": paper["paper_url"], "pdf_url": paper["pdf_url"],
        "abstract": paper["abstract"], "pdf_sha256": hashlib.sha256(raw).hexdigest(),
        "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "page_count": len(reader.pages), "full_text_chars": len(text),
        "full_text_path": str(text_path.relative_to(HERE)), "evidence_depth": "D3",
    })
(DATA / "interspeech-2025-sixth-d3-papers.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-006", "papers": rows}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": "interspeech-2025-d3-batch-006", "papers": len(rows)}))
