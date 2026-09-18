#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"data"
A={
"dindart25_interspeech":("sound-and-production","source-filter-production","periodic-vocal-source","Ultrasound measures vocal-fold vibration as a physical source rather than inferring it only from the recorded waveform."),
"cohen25_interspeech":("listening-and-separation","echo-and-reconstruction","uncertainty-aware-inpainting","Speech inpainting represents multiple plausible repairs so missing evidence is not mistaken for known content."),
"deheerkloots25_interspeech":("recognition-and-alignment","acoustic-unit-mapping","self-supervised-speech-units","Language-specific self-supervised representations are tested by linguistic probes and downstream recognition across speech styles."),
"cavalcanti25_interspeech":("meaning-and-interaction","dialogue-and-turn-taking","turn-boundary-prediction","Turn timing is modeled as a property of a speaking pair, not only an isolated speaker or local acoustic cue."),
"zalkow25_interspeech":("voice-generation-and-control","text-to-speech-and-content","intelligibility-naturalness","Generative postprocessing improves low-resource TTS naturalness while checking objective proxies against listener judgments."),
"griot25_interspeech":("people-variation-and-health","speaker-characteristics","speaker-verification","A unified self-supervised representation separates lexical validation from speaker identity across text-dependent and independent trials."),
"yan25c_interspeech":("languages-accents-and-resources","multilingual-and-crosslingual","code-switching","A controlled 52-language code-switched corpus exposes language-pair and script failures and tests synthetic-data transfer."),
"phukon25_interspeech":("evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding","An intelligibility metric combines semantic, logical, and phonetic similarity because exact word error is not the human target.")}
P={p["paper_id"]:p for p in json.loads((D/"interspeech-2025-papers.json").read_text())["papers"]}; N={n["paper_id"]:n for n in json.loads((D/"interspeech-2025-twelfth-d3-notes.json").read_text())["notes"]}; C={p["paper_id"]:p for p in json.loads((D/"interspeech-2025-twelfth-d3-papers.json").read_text())["papers"]}
rows=[]
for pid,a in A.items():
 p,n=P[pid],N[pid]; cap=C[pid]
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D3","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_fields":["bp","wh","naive","ap","mech","math","dots","ww","limits"],"evidence_excerpt":"Problem: "+n["bp"]+" Mechanism: "+n["mech"]+" Result: "+n["ww"]+" Boundary: "+n["limits"],"source_location":p["paper_url"],"source_sha256":hashlib.sha256(p["abstract"].encode()).hexdigest(),"evidence_depth":"D3","review_state":"analyst-reviewed","claim_boundary":"Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d3-batch-010","status":"analyst-reviewed-D3-batch","claim_boundary":"Eight assignments are analyst-reviewed from captured official PDFs and structured notes; claims are not independent reproductions.","reviewed_count":len(rows),"rows":rows}
(D/"interspeech-2025-semantic-reviewed-d3-batch-010.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D3":len(rows)}))
