#!/usr/bin/env python3
"""Capture one official INTERSPEECH paper for the speaker-characteristics gap."""
import hashlib
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
PDF = DATA / "interspeech-2025-pdfs"
TXT = DATA / "interspeech-2025-text"
PDF.mkdir(exist_ok=True)
TXT.mkdir(exist_ok=True)
pid = "fathan25_interspeech"
paper = next(p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"] if p["paper_id"] == pid)
pdf = PDF / f"{pid}.pdf"
if not pdf.exists():
    with urlopen(Request(paper["pdf_url"], headers={"User-Agent": "speech-conferences-2026/1.0"}), timeout=90) as response:
        pdf.write_bytes(response.read())
reader = PdfReader(str(pdf))
text = re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", "\n\n".join(page.extract_text() or "" for page in reader.pages))).strip()
txt = TXT / f"{pid}.txt"
txt.write_text(text + "\n")
row = {
    "subtheme": "people-variation-and-health/speaker-characteristics",
    "paper_id": pid, "title": paper["title"], "paper_url": paper["paper_url"], "pdf_url": paper["pdf_url"],
    "abstract": paper["abstract"], "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
    "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(), "page_count": len(reader.pages),
    "full_text_chars": len(text), "full_text_path": str(txt.relative_to(HERE)), "evidence_depth": "D3",
}
(DATA / "interspeech-2025-sixteenth-d3-papers.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-016", "papers": [row]}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"paper_id": pid, "pages": len(reader.pages), "chars": len(text), "pdf_sha256": row["pdf_sha256"]}))
