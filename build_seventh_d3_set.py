#!/usr/bin/env python3
"""Capture eight official INTERSPEECH PDFs for a seventh D3 review set."""
from __future__ import annotations
import hashlib, json, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SELECTED = {
    "sound-and-production/room-channel-and-sensing": "franz25_interspeech",
    "listening-and-separation/noise-enhancement": "goswami25_interspeech",
    "recognition-and-alignment/adaptation-and-open-vocabulary": "ducorroy25_interspeech",
    "meaning-and-interaction/prosody-and-intent": "feng25_interspeech",
    "voice-generation-and-control/voice-identity-and-conversion": "hope25_interspeech",
    "people-variation-and-health/clinical-and-assistive-speech": "gao25b_interspeech",
    "languages-accents-and-resources/low-resource-and-data-creation": "fort25_interspeech",
    "evaluation-deployment-and-consequence/metrics-and-targets": "choi25f_interspeech",
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
PDF_DIR = DATA / "interspeech-2025-pdfs"
TEXT_DIR = DATA / "interspeech-2025-text"
PDF_DIR.mkdir(exist_ok=True)
TEXT_DIR.mkdir(exist_ok=True)

def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "speech-conferences-2026/1.0"})
    with urlopen(req, timeout=90) as response:
        return response.read()

def clean(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()

rows = []
for subtheme, paper_id in SELECTED.items():
    paper = papers[paper_id]
    pdf = PDF_DIR / f"{paper_id}.pdf"
    text_path = TEXT_DIR / f"{paper_id}.txt"
    if not pdf.exists():
        pdf.write_bytes(fetch(paper["pdf_url"]))
        time.sleep(0.3)
    raw = pdf.read_bytes()
    reader = PdfReader(str(pdf))
    text = clean("\n\n".join(page.extract_text() or "" for page in reader.pages))
    text_path.write_text(text + "\n")
    rows.append({
        "subtheme": subtheme, "paper_id": paper_id, "title": paper["title"],
        "paper_url": paper["paper_url"], "pdf_url": paper["pdf_url"],
        "abstract": paper["abstract"], "pdf_sha256": hashlib.sha256(raw).hexdigest(),
        "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "page_count": len(reader.pages), "full_text_chars": len(text),
        "full_text_path": str(text_path.relative_to(HERE)), "evidence_depth": "D3",
    })
    print(f"{subtheme}: {paper_id} ({len(reader.pages)} pages, {len(text):,} chars)")
(DATA / "interspeech-2025-seventh-d3-papers.json").write_text(
    json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-007", "papers": rows}, indent=2, ensure_ascii=False) + "\n"
)
print(json.dumps({"batch_id": "interspeech-2025-d3-batch-007", "papers": len(rows)}))

