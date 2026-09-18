"""Capture an eight-paper cross-family D3 reading set."""
import hashlib, json, subprocess, sys, urllib.request
from pathlib import Path

H = Path(__file__).resolve().parent; D = H / "data"
SELECTED = {
    "acoustic-unit-mapping": "chang25_interspeech",
    "adaptation-and-open-vocabulary": "gong25_interspeech",
    "boundaries-and-sequence-structure": "gao25g_interspeech",
    "clinical-and-assistive-speech": "chen25o_interspeech",
    "dialogue-and-turn-taking": "chang25c_interspeech",
    "echo-and-reconstruction": "ding25_interspeech",
    "grounding-and-action": "ishikawa25_interspeech",
    "human-centered-evaluation": "gohider25_interspeech",
}
papers = {p["paper_id"]: p for p in json.loads((D / "interspeech-2025-papers.json").read_text())["papers"]}
rows = []
for subtheme, pid in SELECTED.items():
    p = papers[pid]; pdf = D / "interspeech-2025-pdfs" / f"{pid}.pdf"; txt = D / "interspeech-2025-text" / f"{pid}.txt"
    if not pdf.exists():
        with urllib.request.urlopen(p["pdf_url"], timeout=30) as r: pdf.write_bytes(r.read())
    raw = pdf.read_bytes()
    if not txt.exists():
        out = subprocess.run([sys.executable, "-c", "import fitz,sys; print('\\n'.join(p.get_text() for p in fitz.open(sys.argv[1])))", str(pdf)], capture_output=True, text=True, timeout=30, check=True)
        txt.write_text(out.stdout)
    text = txt.read_text()
    rows.append({"subtheme": subtheme, "paper_id": pid, "title": p["title"], "paper_url": p["paper_url"], "pdf_url": p["pdf_url"], "abstract": p["abstract"], "pdf_sha256": hashlib.sha256(raw).hexdigest(), "full_text_sha256": hashlib.sha256(text.encode()).hexdigest(), "full_text_path": str(txt.relative_to(H)), "evidence_depth": "D3"})
(D / "interspeech-2025-twentieth-d3-papers.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "batch_id": "interspeech-2025-d3-batch-020", "papers": rows, "failures": []}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": "interspeech-2025-d3-batch-020", "papers": len(rows), "subthemes": len(SELECTED)}))
