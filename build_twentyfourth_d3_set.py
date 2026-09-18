"""Capture an eight-paper D3 reading set for variation, representations, evaluation, and resources."""
import hashlib, json, subprocess, sys
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "data"
SELECTED = {
    "source-filter-production": "kwon25b_interspeech",
    "source-filter-production-2": "mcguire25_interspeech",
    "metrics-and-targets-1": "oh25_interspeech",
    "clinical-and-assistive-speech": "ke25_interspeech",
    "acoustic-unit-mapping": "pepino25_interspeech",
    "metrics-and-targets-2": "shen25b_interspeech",
    "low-resource-and-data-creation": "vukovic25_interspeech",
    "accent-and-cultural-boundaries": "zhao25j_interspeech",
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
        result = subprocess.run(
            [sys.executable, "-c", "import fitz,sys;print('\\n'.join(p.get_text() for p in fitz.open(sys.argv[1])))", str(pdf)],
            capture_output=True, text=True, timeout=30, check=True,
        )
        txt.write_text(result.stdout)
    raw = pdf.read_bytes()
    text = txt.read_text()
    rows.append({
        "subtheme_label": label,
        "paper_id": pid,
        "title": p["title"],
        "paper_url": p["paper_url"],
        "pdf_url": p["pdf_url"],
        "abstract": p["abstract"],
        "pdf_sha256": hashlib.sha256(raw).hexdigest(),
        "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "full_text_path": str(txt.relative_to(H)),
        "evidence_depth": "D3",
    })
(D / "interspeech-2025-twentyfourth-d3-papers.json").write_text(
    json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-024", "papers": rows, "failures": []}, indent=2, ensure_ascii=False) + "\n"
)
print(json.dumps({"papers": len(rows), "subthemes": len(SELECTED)}))
