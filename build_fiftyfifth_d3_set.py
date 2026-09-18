"""Capture eight official-PDF INTERSPEECH papers for D3 reading."""
import hashlib, json, subprocess, sys, urllib.request
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
IDS=['gu25_interspeech','guillaume25_interspeech','ahmed25_interspeech','kamo25_interspeech','dasilva25_interspeech','chang25d_interspeech','chen25m_interspeech','chuang25_interspeech']
papers={x['paper_id']:x for x in json.loads((DATA/'interspeech-2025-papers.json').read_text())['papers']}; rows=[]
for pid in IDS:
 p=papers[pid]; pdf=DATA/'interspeech-2025-pdfs'/f'{pid}.pdf'; txt=DATA/'interspeech-2025-text'/f'{pid}.txt'; pdf.parent.mkdir(exist_ok=True)
 if not pdf.exists():
  with urllib.request.urlopen(p['pdf_url'],timeout=60) as r: pdf.write_bytes(r.read())
 if not txt.exists():
  o=subprocess.run([sys.executable,'-c',"import fitz,sys;print('\\n'.join(p.get_text() for p in fitz.open(sys.argv[1])))",str(pdf)],capture_output=True,text=True,timeout=60,check=True); txt.write_text(o.stdout)
 rows.append({'paper_id':pid,'title':p['title'],'paper_url':p['paper_url'],'pdf_url':p['pdf_url'],'abstract':p.get('abstract'),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'full_text_sha256':hashlib.sha256(txt.read_bytes()).hexdigest(),'full_text_path':str(txt.relative_to(HERE)),'evidence_depth':'D3'})
(DATA/'interspeech-2025-fiftyfifth-d3-papers.json').write_text(json.dumps({'venue':'INTERSPEECH 2025','batch_id':'interspeech-2025-d3-batch-055','papers':rows,'failures':[]},indent=2,ensure_ascii=False)+'\n'); print(json.dumps({'papers':len(rows)}))
