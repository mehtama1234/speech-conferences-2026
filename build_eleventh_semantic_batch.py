#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
ASSIGNMENTS={
"bao25_interspeech":("sound-and-production","time-frequency-measurement","spectral-reconstruction","Frequency-domain bandwidth extension reconstructs missing high-frequency structure under perceptual and signal constraints."),
"alradhi25_interspeech":("listening-and-separation","echo-and-reconstruction","neural-reconstruction","Neural-signal speech reconstruction separates content/prosody prediction from waveform phase reconstruction."),
"acevedo25_interspeech":("recognition-and-alignment","adaptation-and-open-vocabulary","domain-adaptation","Audio-side adaptation tests whether an audio-text representation preserves open-vocabulary labels across acoustic domains."),
"ariga25_interspeech":("meaning-and-interaction","prosody-and-intent","prosodic-recognition","Controlled incongruity experiments test how lexical pitch accent and segments jointly shape word recognition."),
"jeon25_interspeech":("voice-generation-and-control","text-to-speech-and-content","personalized-synthesis","Teacher anchoring and curriculum learning adapt TTS to dysarthric speakers while separating identity retention from intelligibility."),
"hoffner25_interspeech":("people-variation-and-health","human-centered-evaluation","human-machine-gap","Speech-reception thresholds compare ASR and human recognition under hearing-relevant noise and spatial conditions."),
"alumae25_interspeech":("languages-accents-and-resources","multilingual-and-crosslingual","language-routing","Language identification and specialized multilingual decoding allocate recognition capacity across languages."),
"alderete25_interspeech":("evaluation-deployment-and-consequence","robustness-and-system-boundary","speech-error-robustness","Annotated spontaneous speech errors map where ASR crosses failure boundaries by error type and position.")}
papers={p["paper_id"]:p for p in json.loads((DATA/"interspeech-2025-papers.json").read_text())["papers"]}
notes={n["paper_id"]:n for n in json.loads((DATA/"interspeech-2025-eleventh-d3-notes.json").read_text())["notes"]}
rows=[]
for pid,a in ASSIGNMENTS.items():
 p,n=papers[pid],notes[pid]
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D3","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_fields":["bp","wh","naive","ap","mech","math","dots","ww","limits"],"evidence_excerpt":"Problem: "+n["bp"]+" Mechanism: "+n["mech"]+" Result: "+n["ww"]+" Boundary: "+n["limits"],"source_location":p["paper_url"],"source_sha256":hashlib.sha256(p["abstract"].encode()).hexdigest(),"evidence_depth":"D3","review_state":"analyst-reviewed","claim_boundary":"Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d3-batch-009","status":"analyst-reviewed-D3-batch","claim_boundary":"Eight assignments are analyst-reviewed from captured official PDFs and structured notes; claims are not independent reproductions.","reviewed_count":len(rows),"rows":rows}
(DATA/"interspeech-2025-semantic-reviewed-d3-batch-009.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D3":len(rows)}))
