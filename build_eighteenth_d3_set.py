"""Capture one additional official INTERSPEECH paper per conceptual subtheme."""
import hashlib,json,urllib.request,subprocess,sys
from pathlib import Path
from pypdf import PdfReader
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
SELECTED={
"source-filter-production":"du25c_interspeech",
"time-frequency-measurement":"ankita25_interspeech",
"room-channel-and-sensing":"hartanto25_interspeech",
"source-separation-and-spatial-listening":"dasilva25_interspeech",
"echo-and-reconstruction":"chiang25_interspeech",
"acoustic-unit-mapping":"bagat25_interspeech",
"adaptation-and-open-vocabulary":"gong25b_interspeech",
"multilingual-and-crosslingual":"javed25_interspeech",
"low-resource-and-data-creation":"emezue25_interspeech",
"boundaries-and-sequence-structure":"ghosh25_interspeech",
"dialogue-and-turn-taking":"fukunaga25_interspeech",
"grounding-and-action":"hu25b_interspeech",
"prosody-and-intent":"chandra25_interspeech",
"prosody-and-interactive-control":"jacquelin25_interspeech",
"voice-identity-and-conversion":"franzreb25_interspeech",
"text-to-speech-and-content":"gourav25_interspeech",
"clinical-and-assistive-speech":"dumpala25_interspeech",
"human-centered-evaluation":"lechler25_interspeech",
"privacy-security-and-accountability":"baser25b_interspeech",
"metrics-and-targets":"cumlin25_interspeech",
"noise-enhancement":"das25b_interspeech",
"robustness-and-system-boundary":"gu25b_interspeech",
"speaker-characteristics":"chen25_interspeech",
"accent-and-cultural-boundaries":"blaschke25_interspeech",
}
papers={p["paper_id"]:p for p in json.loads((DATA/"interspeech-2025-papers.json").read_text())["papers"]}
rows=[]
failures=[]
for subtheme,pid in SELECTED.items():
 p=papers[pid]; pdf=DATA/"interspeech-2025-pdfs"/f"{pid}.pdf"; txt=DATA/"interspeech-2025-text"/f"{pid}.txt"
 pdf.parent.mkdir(exist_ok=True); txt.parent.mkdir(exist_ok=True)
 try:
  if not pdf.exists():
   with urllib.request.urlopen(p["pdf_url"],timeout=30) as response: pdf.write_bytes(response.read())
  raw=pdf.read_bytes()
  extracted=subprocess.run([sys.executable,"-c","from pypdf import PdfReader; import sys; print('\\n'.join(p.extract_text() or '' for p in PdfReader(sys.argv[1]).pages))",str(pdf)],capture_output=True,text=True,timeout=10,check=True)
  text=extracted.stdout
 except Exception as exc:
  failures.append({"paper_id":pid,"subtheme":subtheme,"error":f"{type(exc).__name__}: {exc}"})
  continue
 txt.write_text(text)
 rows.append({"subtheme":subtheme,"paper_id":pid,"title":p["title"],"paper_url":p["paper_url"],"pdf_url":p["pdf_url"],"abstract":p["abstract"],"pdf_sha256":hashlib.sha256(raw).hexdigest(),"full_text_sha256":hashlib.sha256(text.encode()).hexdigest(),"page_count":None,"full_text_chars":len(text),"full_text_path":str(txt.relative_to(HERE)),"evidence_depth":"D3"})
(DATA/"interspeech-2025-eighteenth-d3-papers.json").write_text(json.dumps({"venue":"INTERSPEECH 2025","batch_id":"interspeech-2025-d3-batch-018","papers":rows,"failures":failures},indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":"interspeech-2025-d3-batch-018","papers":len(rows),"subthemes":len({x['subtheme'] for x in rows}),"failures":failures}))
