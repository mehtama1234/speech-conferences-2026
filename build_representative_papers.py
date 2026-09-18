#!/usr/bin/env python3
"""Capture a small, explicit D3 review set from official INTERSPEECH PDFs."""

from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from urllib.request import Request, urlopen

from pypdf import PdfReader


HERE = Path(__file__).resolve().parent
PAPER_DATA = json.loads((HERE / "data/interspeech-2025-papers.json").read_text())["papers"]
BY_ID = {paper["paper_id"]: paper for paper in PAPER_DATA}

SELECTED = {
    "signal_and_acoustics": "azzouz25_interspeech",
    "recognition_and_transcription": "aboeitta25_interspeech",
    "understanding_and_translation": "aggarwal25_interspeech",
    "generation_and_voice": "akti25_interspeech",
    "separation_and_enhancement": "alcalapadilla25_interspeech",
    "speaker_and_paralinguistics": "ai25_interspeech",
    "languages_and_people": "amoniyan25_interspeech",
    "evaluation_and_deployment": "lemaguer25_interspeech",
}

PDF_DIR = HERE / "data" / "interspeech-2025-pdfs"
TEXT_DIR = HERE / "data" / "interspeech-2025-text"
OUT = HERE / "data" / "interspeech-2025-representative-papers.json"


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "speech-conferences-2026/1.0"})
    with urlopen(req, timeout=60) as response:
        return response.read()


def clean(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for theme, paper_id in SELECTED.items():
        paper = BY_ID[paper_id]
        pdf_path = PDF_DIR / f"{paper_id}.pdf"
        text_path = TEXT_DIR / f"{paper_id}.txt"
        if not pdf_path.exists():
            pdf_path.write_bytes(fetch(paper["pdf_url"]))
            time.sleep(0.2)
        raw = pdf_path.read_bytes()
        reader = PdfReader(str(pdf_path))
        text = clean("\n\n".join(page.extract_text() or "" for page in reader.pages))
        text_path.write_text(text + "\n")
        rows.append({
            "theme": theme,
            "paper_id": paper_id,
            "title": paper["title"],
            "authors": paper["authors"],
            "paper_url": paper["paper_url"],
            "pdf_url": paper["pdf_url"],
            "abstract": paper["abstract"],
            "pdf_sha256": hashlib.sha256(raw).hexdigest(),
            "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "page_count": len(reader.pages),
            "full_text_chars": len(text),
            "full_text_path": str(text_path.relative_to(HERE)),
            "evidence_depth": "D3",
            "review_status": "full-text-captured; structured interpretation pending",
        })
        print(f"{theme}: {paper_id} ({len(reader.pages)} pages, {len(text):,} chars)")
    OUT.write_text(json.dumps({"venue": "INTERSPEECH 2025", "papers": rows}, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
