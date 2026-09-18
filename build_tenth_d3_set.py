#!/usr/bin/env python3
"""Capture an eighth-theme-targeted INTERSPEECH D3 review set from official PDFs."""
from __future__ import annotations
import hashlib, json, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SELECTED = {
    "sound-and-production/time-frequency-measurement": "guo25b_interspeech",
    "listening-and-separation/echo-and-reconstruction": "zhao25b_interspeech",
    "recognition-and-alignment/boundaries-and-sequence-structure": "freisinger25_interspeech",
    "voice-generation-and-control/text-to-speech-and-content": "lee25h_interspeech",
    "people-variation-and-health/human-centered-evaluation": "harmsen25_interspeech",
    "evaluation-deployment-and-consequence/robustness-and-system-boundary": "do25_interspeech",
    "evaluation-deployment-and-consequence/metrics-and-targets": "kibria25_interspeech",
    "listening-and-separation/noise-enhancement": "leschanowsky25_interspeech",
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
PDF_DIR, TEXT_DIR = DATA / "interspeech-2025-pdfs", DATA / "interspeech-2025-text"
PDF_DIR.mkdir(exist_ok=True); TEXT_DIR.mkdir(exist_ok=True)
def fetch(url):
    with urlopen(Request(url, headers={"User-Agent":"speech-conferences-2026/1.0"}), timeout=90) as r: return r.read()
def clean(text): return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()
rows=[]
for subtheme, pid in SELECTED.items():
    p = papers[pid]; pdf = PDF_DIR / f"{pid}.pdf"; txt = TEXT_DIR / f"{pid}.txt"
    if not pdf.exists(): pdf.write_bytes(fetch(p["pdf_url"])); time.sleep(.3)
    raw = pdf.read_bytes(); reader = PdfReader(str(pdf)); text = clean("\n\n".join(page.extract_text() or "" for page in reader.pages)); txt.write_text(text + "\n")
    rows.append({"subtheme":subtheme,"paper_id":pid,"title":p["title"],"paper_url":p["paper_url"],"pdf_url":p["pdf_url"],"abstract":p["abstract"],"pdf_sha256":hashlib.sha256(raw).hexdigest(),"full_text_sha256":hashlib.sha256(text.encode()).hexdigest(),"page_count":len(reader.pages),"full_text_chars":len(text),"full_text_path":str(txt.relative_to(HERE)),"evidence_depth":"D3"})
    print(f"{subtheme}: {pid} ({len(reader.pages)} pages, {len(text):,} chars)")
(DATA / "interspeech-2025-tenth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-010","papers":rows},indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":"interspeech-2025-d3-batch-010","papers":len(rows)}))
