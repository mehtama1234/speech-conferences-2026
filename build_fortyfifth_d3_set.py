"""Capture an eight-paper D3 reading set."""
import hashlib,json,subprocess,sys,urllib.request
from pathlib import Path
H=Path(__file__).resolve().parent
D=H/"data"
SELECTED_IDS=["alexos25_interspeech","battula25_interspeech","bhattacharya25b_interspeech","bressensdorf25_interspeech","burkhardt25_interspeech","chae25_interspeech","chae25b_interspeech","chan25_interspeech"]
papers={p["paper_id"]:p for p in json.loads((D/"interspeech-2025-papers.json").read_text())["papers"]}
rows=[]
for pid in SELECTED_IDS:
    p=papers[pid]
    pdf=D/"interspeech-2025-pdfs"/f"{pid}.pdf"
    txt=D/"interspeech-2025-text"/f"{pid}.txt"
    pdf.parent.mkdir(exist_ok=True)
    if not pdf.exists():
        with urllib.request.urlopen(p["pdf_url"],timeout=30) as r: pdf.write_bytes(r.read())
    if not txt.exists():
        o=subprocess.run([sys.executable,"-c","import fitz,sys;print('\\n'.join(p.get_text() for p in fitz.open(sys.argv[1])))",str(pdf)],capture_output=True,text=True,timeout=30,check=True)
        txt.write_text(o.stdout)
    raw=pdf.read_bytes();text=txt.read_text()
    rows.append({"paper_id":pid,"title":p["title"],"paper_url":p["paper_url"],"pdf_url":p["pdf_url"],"abstract":p["abstract"],"pdf_sha256":hashlib.sha256(raw).hexdigest(),"full_text_sha256":hashlib.sha256(text.encode()).hexdigest(),"full_text_path":str(txt.relative_to(H)),"evidence_depth":"D3"})
(D/"interspeech-2025-fortyfifth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-045","papers":rows,"failures":[]},indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"papers":len(rows)}))
