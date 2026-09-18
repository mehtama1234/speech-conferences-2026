#!/usr/bin/env python3
"""Capture four additional official INTERSPEECH papers for full-paper analysis."""
import hashlib, json, re
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent; DATA = HERE / "data"
PDF = DATA / "interspeech-2025-pdfs"; TXT = DATA / "interspeech-2025-text"
PDF.mkdir(exist_ok=True); TXT.mkdir(exist_ok=True)
ids = {
    "dai25b_interspeech": "speaker-characteristics",
    "fujita25_interspeech": "prosody-and-interactive-control",
    "hannan25_interspeech": "speaker-characteristics",
    "makishima25b_interspeech": "grounding-and-action",
}
source = json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]
rows = []
for pid, subtheme in ids.items():
    paper = next(p for p in source if p["paper_id"] == pid)
    pdf = PDF / f"{pid}.pdf"
    if not pdf.exists():
        with urlopen(Request(paper["pdf_url"], headers={"User-Agent": "speech-conferences-2026/1.0"}), timeout=90) as r:
            pdf.write_bytes(r.read())
    reader = PdfReader(str(pdf))
    text = re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", "\n\n".join(p.extract_text() or "" for p in reader.pages))).strip()
    txt = TXT / f"{pid}.txt"; txt.write_text(text + "\n")
    rows.append({"subtheme": subtheme, "paper_id": pid, "title": paper["title"], "paper_url": paper["paper_url"], "pdf_url": paper["pdf_url"], "abstract": paper["abstract"], "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(), "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(), "page_count": len(reader.pages), "full_text_chars": len(text), "full_text_path": str(txt.relative_to(HERE)), "evidence_depth": "D3"})
(DATA / "interspeech-2025-seventeenth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-017","papers":rows}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"papers": len(rows), "pages": sum(r["page_count"] for r in rows)}))
