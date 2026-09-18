"""Capture an eight-paper D3 reading set for meaning, access, variation, and security."""
import hashlib, json, subprocess, sys
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "data"
SELECTED = {
    "metrics-and-targets": "istaiteh25_interspeech",
    "grounding-and-action": "kano25_interspeech",
    "speaker-characteristics": "kunze25_interspeech",
    "privacy-security-and-accountability": "li25aa_interspeech",
    "clinical-and-assistive-speech": "li25j_interspeech",
    "prosody-and-intent": "lin25e_interspeech",
    "acoustic-unit-mapping": "novitasari25b_interspeech",
    "accent-and-cultural-boundaries": "zhang25b_interspeech",
}
papers = {p["paper_id"]: p for p in json.loads((D / "interspeech-2025-papers.json").read_text())["papers"]}
rows = []
for label, pid in SELECTED.items():
    p = papers[pid]
    pdf = D / "interspeech-2025-pdfs" / f"{pid}.pdf"
    txt = D / "interspeech-2025-text" / f"{pid}.txt"
    if not pdf.exists():
        import urllib.request
        with urllib.request.urlopen(p["pdf_url"], timeout=30) as response:
            pdf.write_bytes(response.read())
    if not txt.exists():
        result = subprocess.run([sys.executable, "-c", "import fitz,sys;print('\\n'.join(p.get_text() for p in fitz.open(sys.argv[1])))", str(pdf)], capture_output=True, text=True, timeout=30, check=True)
        txt.write_text(result.stdout)
    raw = pdf.read_bytes(); text = txt.read_text()
    rows.append({"subtheme_label": label, "paper_id": pid, "title": p["title"], "paper_url": p["paper_url"], "pdf_url": p["pdf_url"], "abstract": p["abstract"], "pdf_sha256": hashlib.sha256(raw).hexdigest(), "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(), "full_text_path": str(txt.relative_to(H)), "evidence_depth": "D3"})
(D / "interspeech-2025-twentyfifth-d3-papers.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-025", "papers": rows, "failures": []}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"papers": len(rows), "subthemes": len(SELECTED)}))
