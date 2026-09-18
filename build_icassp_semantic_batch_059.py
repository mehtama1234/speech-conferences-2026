#!/usr/bin/env python3
"""Reject a bounded slice of clearly non-audio ICASSP ambiguity cases."""
import hashlib,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
if (DATA/"icassp-2026-semantic-reviewed-batch-059.json").exists():
 print(json.dumps({"batch_id":"icassp-2026-semantic-batch-059","status":"preserved-input","reviewed_count":json.loads((DATA/"icassp-2026-semantic-reviewed-batch-059.json").read_text())["reviewed_count"]})); raise SystemExit(0)
audio=re.compile(r"audio|speech|voice|sound|acoustic|auditory|music|pitch|vocal|microphone|noise|room|echo|asv|spoof|spectrogram|mel[- ]",re.I)
queue=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text()); papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}; already=set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"): already|={r["paper_id"] for r in json.loads(path.read_text()).get("rows",[])}
selected=[r for r in queue["rows"] if r.get("review_state")!="analyst-reviewed" and r.get("decision")=="ambiguous" and not audio.search(r.get("title", "")) and r["paper_id"] not in already][:32]
if len(selected)!=32: raise SystemExit(f"expected 32 rows, found {len(selected)}")
rows=[]
for c in selected:
 p=papers[c["paper_id"]]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":"The preserved title and abstract do not identify speech, voice, or an audio object; the ambiguous proposal is a non-speech machine-learning, vision, biomedical, communications, or text task.","evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; rejection resolves speech-taxonomy membership only and does not characterize scientific quality."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-059","status":"analyst-reviewed-non-audio-boundary-batch","claim_boundary":"These records are explicit unsupported decisions based on preserved title/abstract evidence; they remain in the full ICASSP denominator.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-059.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D1":sum(r["evidence_depth"]=="D1" for r in rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
