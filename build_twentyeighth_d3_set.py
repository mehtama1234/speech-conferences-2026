"""Capture an eight-paper D3 reading set from the remaining supported queue."""
import hashlib,json,subprocess,sys,urllib.request
from pathlib import Path
H=Path(__file__).resolve().parent;D=H/"data"
SELECTED={"human-centered-evaluation":"ahmed25_interspeech","multilingual-and-crosslingual":"alam25_interspeech","acoustic-to-token-1":"attia25_interspeech","self-supervised-speech-units":"bentum25_interspeech","noise-enhancement":"cappellazzo25_interspeech","metrics-and-targets":"chang25b_interspeech","prosody-and-intent":"chen25g_interspeech","speaker-characteristics":"cheng25d_interspeech"}
papers={p["paper_id"]:p for p in json.loads((D/"interspeech-2025-papers.json").read_text())["papers"]};rows=[]
for label,pid in SELECTED.items():
 p=papers[pid];pdf=D/"interspeech-2025-pdfs"/f"{pid}.pdf";txt=D/"interspeech-2025-text"/f"{pid}.txt";pdf.parent.mkdir(exist_ok=True);txt.parent.mkdir(exist_ok=True)
 if not pdf.exists():
  with urllib.request.urlopen(p["pdf_url"],timeout=30) as r:pdf.write_bytes(r.read())
 if not txt.exists():
  o=subprocess.run([sys.executable,"-c","import fitz,sys;print('\\n'.join(p.get_text() for p in fitz.open(sys.argv[1])))",str(pdf)],capture_output=True,text=True,timeout=30,check=True);txt.write_text(o.stdout)
 raw=pdf.read_bytes();text=txt.read_text();rows.append({"subtheme_label":label,"paper_id":pid,"title":p["title"],"paper_url":p["paper_url"],"pdf_url":p["pdf_url"],"abstract":p["abstract"],"pdf_sha256":hashlib.sha256(raw).hexdigest(),"full_text_sha256":hashlib.sha256(text.encode()).hexdigest(),"full_text_path":str(txt.relative_to(H)),"evidence_depth":"D3"})
(D/"interspeech-2025-twentyeighth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-028","papers":rows,"failures":[]},indent=2,ensure_ascii=False)+"\n");print(json.dumps({"papers":len(rows)}))
