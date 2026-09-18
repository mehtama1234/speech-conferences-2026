#!/usr/bin/env python3
import hashlib,json,re,time
from pathlib import Path
from urllib.request import Request,urlopen
from pypdf import PdfReader
H=Path(__file__).resolve().parent; D=H/'data'; PDF=D/'interspeech-2025-pdfs'; TXT=D/'interspeech-2025-text'; PDF.mkdir(exist_ok=True); TXT.mkdir(exist_ok=True)
PIDS={'recognition-and-alignment/boundaries-and-sequence-structure':'ho25_interspeech','listening-and-separation/source-separation-and-spatial-listening':'huang25k_interspeech'}
papers={p['paper_id']:p for p in json.loads((D/'interspeech-2025-papers.json').read_text())['papers']}
def fetch(url):
    with urlopen(Request(url,headers={'User-Agent':'speech-conferences-2026/1.0'}),timeout=90) as r:return r.read()
def clean(x):return re.sub(r'\n{3,}','\n\n',re.sub(r'[ \t]+',' ',x)).strip()
rows=[]
for sub,pid in PIDS.items():
    p=papers[pid]; f=PDF/f'{pid}.pdf'; t=TXT/f'{pid}.txt'
    if not f.exists(): f.write_bytes(fetch(p['pdf_url'])); time.sleep(.3)
    raw=f.read_bytes(); reader=PdfReader(str(f)); text=clean('\n\n'.join(x.extract_text() or '' for x in reader.pages)); t.write_text(text+'\n')
    rows.append({'subtheme':sub,'paper_id':pid,'title':p['title'],'paper_url':p['paper_url'],'pdf_url':p['pdf_url'],'abstract':p['abstract'],'pdf_sha256':hashlib.sha256(raw).hexdigest(),'full_text_sha256':hashlib.sha256(text.encode()).hexdigest(),'page_count':len(reader.pages),'full_text_chars':len(text),'full_text_path':str(t.relative_to(H)),'evidence_depth':'D3'})
    print(sub,pid,len(reader.pages),len(text))
(D/'interspeech-2025-fourteenth-d3-papers.json').write_text(json.dumps({'venue':'INTERSPEECH 2025','batch_id':'interspeech-2025-d3-batch-014','papers':rows},indent=2,ensure_ascii=False)+'\n')
