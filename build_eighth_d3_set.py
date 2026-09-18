#!/usr/bin/env python3
"""Capture eight official INTERSPEECH PDFs for an eighth D3 review set."""
from __future__ import annotations
import hashlib, json, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SELECTED = {
    "listening-and-separation/source-separation-and-spatial-listening": "alizadeh25_interspeech",
    "sound-and-production/source-filter-production": "arai25_interspeech",
    "languages-accents-and-resources/accent-and-cultural-boundaries": "bafna25_interspeech",
    "people-variation-and-health/clinical-and-assistive-speech": "baumann25_interspeech",
    "voice-generation-and-control/prosody-and-interactive-control": "chen25b_interspeech",
    "meaning-and-interaction/grounding-and-action": "fujita25b_interspeech",
    "evaluation-deployment-and-consequence/privacy-security-and-accountability": "chandra25b_interspeech",
    "recognition-and-alignment/acoustic-unit-mapping": "ahadzi25_interspeech",
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
PDF_DIR, TEXT_DIR = DATA / "interspeech-2025-pdfs", DATA / "interspeech-2025-text"
PDF_DIR.mkdir(exist_ok=True); TEXT_DIR.mkdir(exist_ok=True)

def fetch(url):
    with urlopen(Request(url, headers={"User-Agent": "speech-conferences-2026/1.0"}), timeout=90) as r:
        return r.read()

def clean(text):
    return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()

rows = []
for subtheme, paper_id in SELECTED.items():
    paper = papers[paper_id]; pdf = PDF_DIR / f"{paper_id}.pdf"; text_path = TEXT_DIR / f"{paper_id}.txt"
    if not pdf.exists(): pdf.write_bytes(fetch(paper["pdf_url"])); time.sleep(.3)
    raw = pdf.read_bytes(); reader = PdfReader(str(pdf)); text = clean("\n\n".join(p.extract_text() or "" for p in reader.pages)); text_path.write_text(text + "\n")
    rows.append({"subtheme": subtheme, "paper_id": paper_id, "title": paper["title"], "paper_url": paper["paper_url"], "pdf_url": paper["pdf_url"], "abstract": paper["abstract"], "pdf_sha256": hashlib.sha256(raw).hexdigest(), "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(), "page_count": len(reader.pages), "full_text_chars": len(text), "full_text_path": str(text_path.relative_to(HERE)), "evidence_depth": "D3"})
    print(f"{subtheme}: {paper_id} ({len(reader.pages)} pages, {len(text):,} chars)")
(DATA / "interspeech-2025-eighth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025", "batch_id":"interspeech-2025-d3-batch-008", "papers":rows}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id":"interspeech-2025-d3-batch-008", "papers":len(rows)}))
