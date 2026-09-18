#!/usr/bin/env python3
"""Capture a D3 batch targeted at the seven subthemes lacking full-paper evidence."""
from __future__ import annotations
import hashlib, json, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
papers = json.loads((HERE / "data/interspeech-2025-papers.json").read_text())["papers"]
by_id = {p["paper_id"]: p for p in papers}
SELECTED = {
    "sound-and-production/time-frequency-measurement": "chao25b_interspeech",
    "sound-and-production/room-channel-and-sensing": "dai25c_interspeech",
    "listening-and-separation/echo-and-reconstruction": "byun25_interspeech",
    "meaning-and-interaction/prosody-and-intent": "chao25_interspeech",
    "voice-generation-and-control/text-to-speech-and-content": "roychowdhury25_interspeech",
    "people-variation-and-health/clinical-and-assistive-speech": "li25ea_interspeech",
    "people-variation-and-health/human-centered-evaluation": "bokkahallisatish25_interspeech",
}
PDF_DIR, TEXT_DIR = HERE / "data/interspeech-2025-pdfs", HERE / "data/interspeech-2025-text"
PDF_DIR.mkdir(exist_ok=True); TEXT_DIR.mkdir(exist_ok=True)
def fetch(url):
    req = Request(url, headers={"User-Agent":"speech-conferences-2026/1.0"})
    with urlopen(req, timeout=60) as response: return response.read()
def clean(text): return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()
rows=[]
for subtheme, paper_id in SELECTED.items():
    p=by_id[paper_id]; pdf=PDF_DIR/f"{paper_id}.pdf"; txt=TEXT_DIR/f"{paper_id}.txt"
    if not pdf.exists(): pdf.write_bytes(fetch(p["pdf_url"])); time.sleep(.2)
    raw=pdf.read_bytes(); reader=PdfReader(str(pdf)); text=clean("\n\n".join(page.extract_text() or "" for page in reader.pages)); txt.write_text(text+"\n")
    rows.append({"subtheme":subtheme,"paper_id":paper_id,"title":p["title"],"paper_url":p["paper_url"],"pdf_url":p["pdf_url"],"abstract":p["abstract"],"pdf_sha256":hashlib.sha256(raw).hexdigest(),"full_text_sha256":hashlib.sha256(text.encode()).hexdigest(),"page_count":len(reader.pages),"full_text_chars":len(text),"full_text_path":str(txt.relative_to(HERE)),"evidence_depth":"D3"})
    print(f"{subtheme}: {paper_id} ({len(reader.pages)} pages, {len(text):,} chars)")
(HERE/"data/interspeech-2025-fifth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-005","papers":rows},indent=2,ensure_ascii=False)+"\n")
print("wrote data/interspeech-2025-fifth-d3-papers.json")
