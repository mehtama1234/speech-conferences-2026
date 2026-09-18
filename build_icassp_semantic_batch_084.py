"""Targeted adjudication of final clear speech and non-speech boundary cases."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"data"
OUT=DATA/"icassp-2026-semantic-reviewed-batch-084.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
ASSIGNMENTS={
"06a9e45523b1b67eda62ac12b6db46c06167f30e":("supported","evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","The title names AASIST anti-spoofing; the conference session identifies this as audio deepfake/spoofing work, and the associated description evaluates synthetic speech attacks.","speech deepfake detection"),
"80f97dfe4226f84e6e3ac744f0c739cf1ff1c88d":("supported","recognition-and-alignment","boundaries-and-sequence-structure","long-context-decoding","The paper studies how sentence syntax changes human recognition of Danish speech in noise; the ordinary problem is using sentence structure to recover words when the acoustic signal is damaged.","speech recognition in noise"),
"74e891487f652eced65ffd4f5e000cb6cf697238":("unsupported",None,None,None,"Singing-skill evaluation from semitone pitch histograms is musical performance analysis, not spoken speech.","music"),
"9acf7d9c6c549d2651dfaf75201f504f8f888c89":("unsupported",None,None,None,"Machine translation between low-resource language and Chinese is text translation; the title does not identify spoken speech or speech audio.","text-only translation"),
"a0924a0098ad0decdf0de771c46a71a5308599ff":("unsupported",None,None,None,"Irregular clinical time-series modeling is a general medical prediction problem; the title does not identify speech as its signal or target.","clinical time series"),
"a894e9fb2e7adc60ce5d03f1fc1d8a03f2ce5cf4":("unsupported",None,None,None,"The title and abstract describe multimodal multilingual retrieval with NLU integration, not a spoken-speech task.","multimodal retrieval"),
}
q=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,(decision,theme,subtheme,concept,reasoning,family) in ASSIGNMENTS.items():
 candidate=next(r for r in q["rows"] if r["paper_id"]==pid)
 if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 excerpt=abstract[:1200] if abstract else p["title"]
 rows.append({"paper_id":pid,"title":p["title"],"decision":decision,"confidence":f"analyst-reviewed-{depth}","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":reasoning,"evidence_excerpt":excerpt,"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":f"ICASSP discovery metadata plus targeted boundary evidence; this resolves taxonomy membership as {family} only and does not characterize scientific quality or full-paper mechanism."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-084","status":"analyst-reviewed-targeted-speech-and-non-speech-boundary-batch","claim_boundary":"These decisions make two evidence-backed speech assignments and four clear exclusions; they do not close generic audio, multimodal-emotion, or auditory-attention records whose speech object is not established by preserved corpus evidence.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"supported":sum(r["decision"]=="supported" for r in rows),"unsupported":sum(r["decision"]=="unsupported" for r in rows)}))

