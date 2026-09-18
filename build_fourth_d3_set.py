#!/usr/bin/env python3
"""Capture a fourth balanced INTERSPEECH D3 batch from official PDFs."""
from __future__ import annotations
import hashlib, json, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
papers = json.loads((HERE / "data/interspeech-2025-papers.json").read_text())["papers"]
by_id = {row["paper_id"]: row for row in papers}
SELECTED = {
    "sound-and-production": "benway25_interspeech",
    "listening-and-separation": "dang25_interspeech",
    "recognition-and-alignment": "he25_interspeech",
    "meaning-and-interaction": "peng25b_interspeech",
    "voice-generation-and-control": "biyani25_interspeech",
    "people-variation-and-health": "buker25_interspeech",
    "languages-accents-and-resources": "nguyen25_interspeech",
    "evaluation-deployment-and-consequence": "combei25_interspeech",
}
OUT = HERE / "data/interspeech-2025-fourth-d3-papers.json"
PDF_DIR = HERE / "data/interspeech-2025-pdfs"
TEXT_DIR = HERE / "data/interspeech-2025-text"

def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "speech-conferences-2026/1.0"})
    with urlopen(req, timeout=60) as response:
        return response.read()

def clean(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()

rows = []
PDF_DIR.mkdir(exist_ok=True)
TEXT_DIR.mkdir(exist_ok=True)
for theme, paper_id in SELECTED.items():
    paper = by_id[paper_id]
    pdf_path = PDF_DIR / f"{paper_id}.pdf"
    text_path = TEXT_DIR / f"{paper_id}.txt"
    if not pdf_path.exists():
        pdf_path.write_bytes(fetch(paper["pdf_url"]))
        time.sleep(0.2)
    raw = pdf_path.read_bytes()
    reader = PdfReader(str(pdf_path))
    text = clean("\n\n".join(page.extract_text() or "" for page in reader.pages))
    text_path.write_text(text + "\n")
    rows.append({"theme": theme, "paper_id": paper_id, "title": paper["title"],
                 "paper_url": paper["paper_url"], "pdf_url": paper["pdf_url"],
                 "abstract": paper["abstract"], "pdf_sha256": hashlib.sha256(raw).hexdigest(),
                 "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
                 "page_count": len(reader.pages), "full_text_chars": len(text),
                 "full_text_path": str(text_path.relative_to(HERE)), "evidence_depth": "D3"})
    print(f"{theme}: {paper_id} ({len(reader.pages)} pages, {len(text):,} chars)")
OUT.write_text(json.dumps({"venue":"INTERSPEECH 2025", "batch_id":"interspeech-2025-d3-batch-004", "papers":rows}, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {OUT}")
