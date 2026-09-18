"""Capture a second full-paper contrast set across the 24 speech subthemes."""
import hashlib,json,urllib.request,subprocess,sys
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"data"
SELECTED={
"accent-and-cultural-boundaries":"chen25h_interspeech",
"acoustic-unit-mapping":"balajishankar25_interspeech",
"adaptation-and-open-vocabulary":"cm25_interspeech",
"boundaries-and-sequence-structure":"christodoulidou25_interspeech",
"clinical-and-assistive-speech":"choi25h_interspeech",
"dialogue-and-turn-taking":"baihaqi25_interspeech",
"echo-and-reconstruction":"chung25_interspeech",
"grounding-and-action":"baihaqi25b_interspeech",
"human-centered-evaluation":"chowdhury25_interspeech",
"low-resource-and-data-creation":"damianos25_interspeech",
"metrics-and-targets":"ahn25b_interspeech",
"multilingual-and-crosslingual":"elleuch25_interspeech",
"noise-enhancement":"biswas25b_interspeech",
"privacy-security-and-accountability":"ali25_interspeech",
"prosody-and-intent":"araizaillan25_interspeech",
"prosody-and-interactive-control":"francis25_interspeech",
"robustness-and-system-boundary":"broughton25_interspeech",
"room-channel-and-sensing":"deluca25_interspeech",
"source-filter-production":"birkholz25_interspeech",
"source-separation-and-spatial-listening":"chen25l_interspeech",
"speaker-characteristics":"cao25_interspeech",
"text-to-speech-and-content":"chen25q_interspeech",
"time-frequency-measurement":"bendom25_interspeech",
"voice-identity-and-conversion":"chou25_interspeech",
}
papers={p["paper_id"]:p for p in json.loads((D/"interspeech-2025-papers.json").read_text())["papers"]}
rows=[]; failures=[]
for subtheme,pid in SELECTED.items():
 p=papers[pid]; pdf=D/"interspeech-2025-pdfs"/f"{pid}.pdf"; txt=D/"interspeech-2025-text"/f"{pid}.txt"; pdf.parent.mkdir(exist_ok=True); txt.parent.mkdir(exist_ok=True)
 try:
  if not pdf.exists():
   with urllib.request.urlopen(p["pdf_url"],timeout=30) as response: pdf.write_bytes(response.read())
  raw=pdf.read_bytes(); out=subprocess.run([sys.executable,"-c","import fitz,sys; doc=fitz.open(sys.argv[1]); print('\\n'.join(page.get_text() for page in doc))",str(pdf)],capture_output=True,text=True,timeout=30,check=True); text=out.stdout; txt.write_text(text)
  rows.append({"subtheme":subtheme,"paper_id":pid,"title":p["title"],"paper_url":p["paper_url"],"pdf_url":p["pdf_url"],"abstract":p["abstract"],"pdf_sha256":hashlib.sha256(raw).hexdigest(),"full_text_sha256":hashlib.sha256(text.encode()).hexdigest(),"page_count":None,"full_text_chars":len(text),"full_text_path":str(txt.relative_to(H)),"evidence_depth":"D3"})
 except Exception as exc:
  failures.append({"paper_id":pid,"subtheme":subtheme,"error":f"{type(exc).__name__}: {exc}"})
(D/"interspeech-2025-nineteenth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-019","papers":rows,"failures":failures},indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":"interspeech-2025-d3-batch-019","papers":len(rows),"subthemes":len({x['subtheme'] for x in rows}),"failures":failures}))
