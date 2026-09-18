#!/usr/bin/env python3
"""Capture eight official INTERSPEECH PDFs for a balanced D3 pass."""
import hashlib, json, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

H = Path(__file__).resolve().parent; D = H / "data"
PDF = D / "interspeech-2025-pdfs"; TXT = D / "interspeech-2025-text"
PDF.mkdir(exist_ok=True); TXT.mkdir(exist_ok=True)
PIDS = {
    "listening-and-separation/noise-enhancement": "behera25_interspeech",
    "people-and-variation/clinical-and-assistive-speech": "braun25_interspeech",
    "voice-generation-and-control/text-to-speech-and-content": "berger25_interspeech",
    "recognition-and-alignment/adaptation-and-open-vocabulary": "bataev25_interspeech",
    "evaluation-deployment-and-consequence/metrics-and-targets": "bashir25_interspeech",
    "languages-accents-and-resources/low-resource-and-data-creation": "carofilis25_interspeech",
    "recognition-and-alignment/boundaries-and-sequence-structure": "cai25_interspeech",
    "evaluation-deployment-and-consequence/privacy-security-and-accountability": "das25_interspeech",
}
papers = {p["paper_id"]: p for p in json.loads((D / "interspeech-2025-papers.json").read_text())["papers"]}
def clean(x): return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", x)).strip()
rows = []
for subtheme, pid in PIDS.items():
    p = papers[pid]; f = PDF / f"{pid}.pdf"; t = TXT / f"{pid}.txt"
    if not f.exists():
        with urlopen(Request(p["pdf_url"], headers={"User-Agent": "speech-conferences-2026/1.0"}), timeout=90) as r: f.write_bytes(r.read())
        time.sleep(.3)
    raw = f.read_bytes(); reader = PdfReader(str(f))
    text = clean("\n\n".join(page.extract_text() or "" for page in reader.pages)); t.write_text(text + "\n")
    rows.append({"subtheme": subtheme, "paper_id": pid, "title": p["title"], "paper_url": p["paper_url"], "pdf_url": p["pdf_url"], "abstract": p["abstract"], "pdf_sha256": hashlib.sha256(raw).hexdigest(), "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(), "page_count": len(reader.pages), "full_text_chars": len(text), "full_text_path": str(t.relative_to(H)), "evidence_depth": "D3"})
    print(subtheme, pid, len(reader.pages), len(text))
(D / "interspeech-2025-fifteenth-d3-papers.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-015", "papers": rows}, indent=2, ensure_ascii=False) + "\n")
