"""Capture eight official-PDF INTERSPEECH papers for D3 reading."""
import hashlib
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
IDS = [
    "chen25l_interspeech", "guzik25_interspeech",
    "kim25b_interspeech", "kaneko25b_interspeech",
    "blaschke25_interspeech", "gutscher25_interspeech",
    "jung25b_interspeech", "hu25e_interspeech",
]
papers = {x["paper_id"]: x for x in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
rows = []
for paper_id in IDS:
    paper = papers[paper_id]
    pdf = DATA / "interspeech-2025-pdfs" / f"{paper_id}.pdf"
    text = DATA / "interspeech-2025-text" / f"{paper_id}.txt"
    pdf.parent.mkdir(exist_ok=True)
    if not pdf.exists():
        with urllib.request.urlopen(paper["pdf_url"], timeout=60) as response:
            pdf.write_bytes(response.read())
    if not text.exists():
        extracted = subprocess.run([sys.executable, "-c", "import fitz,sys;print('\\n'.join(p.get_text() for p in fitz.open(sys.argv[1])))", str(pdf)], capture_output=True, text=True, timeout=60, check=True)
        text.write_text(extracted.stdout)
    rows.append({"paper_id": paper_id, "title": paper["title"], "paper_url": paper["paper_url"], "pdf_url": paper["pdf_url"], "abstract": paper.get("abstract"), "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(), "full_text_sha256": hashlib.sha256(text.read_bytes()).hexdigest(), "full_text_path": str(text.relative_to(HERE)), "evidence_depth": "D3"})
(DATA / "interspeech-2025-fiftyfirst-d3-papers.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-051", "papers": rows, "failures": []}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"papers": len(rows)}))
