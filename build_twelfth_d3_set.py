#!/usr/bin/env python3
"""Capture a concept-targeted twelfth INTERSPEECH D3 set from official PDFs."""
import hashlib,json,re,time
from pathlib import Path
from urllib.request import Request,urlopen
from pypdf import PdfReader
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
SELECTED={
"sound-and-production/source-filter-production":"dindart25_interspeech",
"listening-and-separation/echo-and-reconstruction":"cohen25_interspeech",
"recognition-and-alignment/acoustic-unit-mapping":"deheerkloots25_interspeech",
"meaning-and-interaction/dialogue-and-turn-taking":"cavalcanti25_interspeech",
"voice-generation-and-control/text-to-speech-and-content":"zalkow25_interspeech",
"people-variation-and-health/speaker-characteristics":"griot25_interspeech",
"languages-accents-and-resources/multilingual-and-crosslingual":"yan25c_interspeech",
"evaluation-deployment-and-consequence/metrics-and-targets":"phukon25_interspeech"}
papers={p["paper_id"]:p for p in json.loads((DATA/"interspeech-2025-papers.json").read_text())["papers"]}
PDF_DIR,TEXT_DIR=DATA/"interspeech-2025-pdfs",DATA/"interspeech-2025-text"; PDF_DIR.mkdir(exist_ok=True); TEXT_DIR.mkdir(exist_ok=True)
def fetch(url):
 with urlopen(Request(url,headers={"User-Agent":"speech-conferences-2026/1.0"}),timeout=90) as r:return r.read()
def clean(x):return re.sub(r"\n{3,}","\n\n",re.sub(r"[ \t]+"," ",x)).strip()
rows=[]
for sub,pid in SELECTED.items():
 p=papers[pid]; pdf=PDF_DIR/f"{pid}.pdf"; txt=TEXT_DIR/f"{pid}.txt"
 if not pdf.exists():pdf.write_bytes(fetch(p["pdf_url"]));time.sleep(.3)
 raw=pdf.read_bytes(); reader=PdfReader(str(pdf)); text=clean("\n\n".join(page.extract_text() or "" for page in reader.pages)); txt.write_text(text+"\n")
 rows.append({"subtheme":sub,"paper_id":pid,"title":p["title"],"paper_url":p["paper_url"],"pdf_url":p["pdf_url"],"abstract":p["abstract"],"pdf_sha256":hashlib.sha256(raw).hexdigest(),"full_text_sha256":hashlib.sha256(text.encode()).hexdigest(),"page_count":len(reader.pages),"full_text_chars":len(text),"full_text_path":str(txt.relative_to(HERE)),"evidence_depth":"D3"})
 print(f"{sub}: {pid} ({len(reader.pages)} pages, {len(text):,} chars)")
(DATA/"interspeech-2025-twelfth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-012","papers":rows},indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":"interspeech-2025-d3-batch-012","papers":len(rows)}))
