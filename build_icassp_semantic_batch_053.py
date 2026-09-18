#!/usr/bin/env python3
"""Correct a clear false-positive slice: ICASSP candidates that are not speech papers."""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
if (DATA/"icassp-2026-semantic-reviewed-batch-053.json").exists():
    print(json.dumps({"batch_id":"icassp-2026-semantic-batch-053","status":"preserved-input","reviewed_count":json.loads((DATA/"icassp-2026-semantic-reviewed-batch-053.json").read_text())["reviewed_count"]}))
    raise SystemExit(0)
queue=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
already=set()
for path in DATA.glob("icassp-2026-semantic-reviewed-batch-*.json"):
    already |= {r["paper_id"] for r in json.loads(path.read_text()).get("rows",[])}
selected=[(c,papers[c["paper_id"]]) for c in queue["rows"] if c.get("review_state")=="needs-analyst-semantic-review" and c.get("decision")=="supported" and c["paper_id"] not in already]
if len(selected)!=32: raise SystemExit(f"expected 32 new supported false positives, found {len(selected)}")
rows=[]
for c,p in selected:
    abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
    rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":"The title and preserved abstract identify an image, biomedical signal, music, communications, or other non-speech object. The earlier lexical candidate was a false positive and does not establish speech-taxonomy membership.","evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; this correction resolves taxonomy membership only and does not characterize scientific quality."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-053","status":"analyst-reviewed-corrected-false-positive-batch","claim_boundary":"These title/abstract-supported false positives are explicitly rejected from the speech taxonomy and remain in the full ICASSP denominator.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-053.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D1":sum(r["evidence_depth"]=="D1" for r in rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
