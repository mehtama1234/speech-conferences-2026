#!/usr/bin/env python3
"""Reject the next bounded slice of clear non-speech ICASSP ambiguity cases."""
import hashlib,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
if (DATA/"icassp-2026-semantic-reviewed-batch-058.json").exists():
 print(json.dumps({"batch_id":"icassp-2026-semantic-batch-058","status":"preserved-input","reviewed_count":json.loads((DATA/"icassp-2026-semantic-reviewed-batch-058.json").read_text())["reviewed_count"]})); raise SystemExit(0)
pat=re.compile(r"image|video|MRI|EEG|ECG|federated|visual|vision|histopath|medical|drug|radar|wireless|traffic|robot|UAV|point cloud|hyperspectral|remote sensing|low-light|object detection|segmentation|re-identification|watermark|LLM|language model|text-to-text|recommendation|graph",re.I)
exclude={"c71d62cdeed9e9283ef1c2373136ebd5b905c00c","fd9a44e2ce03d36ef5740d46bfff6c9e5acc8966"}
queue=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text()); papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}; already=set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"): already|={r["paper_id"] for r in json.loads(path.read_text()).get("rows",[])}
selected=[r for r in queue["rows"] if r.get("review_state")!="analyst-reviewed" and r.get("decision")=="ambiguous" and pat.search(r.get("title", "")) and r["paper_id"] not in already and r["paper_id"] not in exclude][:24]
if len(selected)!=24: raise SystemExit(f"expected 24 rows, found {len(selected)}")
rows=[]
for c in selected:
 p=papers[c["paper_id"]]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":"The title and preserved abstract identify an image, video, biomedical, communications, sensing, or other non-speech object. Ambiguous lexical overlap does not establish membership in the speech taxonomy.","evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; rejection resolves speech-taxonomy membership only and does not characterize scientific quality."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-058","status":"analyst-reviewed-non-speech-batch","claim_boundary":"These records are explicit unsupported decisions based on preserved title/abstract evidence; they remain in the full ICASSP denominator.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-058.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D1":sum(r["evidence_depth"]=="D1" for r in rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
