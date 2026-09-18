#!/usr/bin/env python3
"""Reject an explicit adjacent-audio boundary slice from the speech taxonomy."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
if (DATA/"icassp-2026-semantic-reviewed-batch-056.json").exists():
 print(json.dumps({"batch_id":"icassp-2026-semantic-batch-056","status":"preserved-input","reviewed_count":json.loads((DATA/"icassp-2026-semantic-reviewed-batch-056.json").read_text())["reviewed_count"]})); raise SystemExit(0)
IDS=['1c85d8da835479b6bbfc86e762e7a735b91d6913','807726e004c0b81c403705a6f271f6a2a3?','aa5f983adfcb5532c52e75abf5bdae5ffb340149','b3e4a7d63fad2c1a4594d762c03d530e62e77bfe','bcb278ecf8cc350dfa0dc8c17b37f2210e63beae','c25f70c36cae6cc8b7e0d2551eeceb69a617a299','e360777a680287844d5593dad0570bd4759421a3','e422d04b71478c0e?','eb78332d9bec53cecd6877ec3d373791989659fa','f1ad0807ce564e96d3418481352731c05de64f7a','f5f3f6e76bf89a151cae0c7bc211137f12298c31','fa99ef8ce45916e7d843ac52e175c7339f1f470e','55fe457194f7dc62b01ebc0abf1612e1a8112ad0']
# Resolve two IDs by exact title because preserved identifiers are easy to mistype.
source=json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]
wanted=['USVexplorer','Testing The Efficient Coding','WaveSpikeNet','ViTex:','StyHarmo','Constructing Composite','Learnable Mel-Frontend','Enhance, Then Separate','UMV:','A Unified Multi-Encoder','Compression meets Sampling','Spectrogram Event']
by_title={p["title"]:p for p in source}; selected=[]
for prefix in wanted:
 p=next((p for p in source if p["title"].startswith(prefix)),None)
 if p is None: raise SystemExit(f"missing title prefix: {prefix}")
 selected.append(p)
queue=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text()); q={r["paper_id"]:r for r in queue["rows"]}
rows=[]
for p in selected:
 c=q[p["paperId"]]
 if c.get("review_state")=="analyst-reviewed" or c.get("decision") not in {"ambiguous","supported"}: raise SystemExit(f"not unresolved adjacent-audio case: {p['title']}")
 abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":"The preserved title and abstract identify music generation/restoration/tagging, animal vocalization, underwater/ship acoustics, or another non-speech audio object. The broad audio match does not establish membership in this speech taxonomy.","evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; rejection resolves speech-taxonomy membership only and does not characterize scientific quality."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-056","status":"analyst-reviewed-adjacent-audio-boundary-batch","claim_boundary":"These records are explicit unsupported decisions based on preserved title/abstract evidence; they remain in the full ICASSP denominator.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-056.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D1":sum(r["evidence_depth"]=="D1" for r in rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
