#!/usr/bin/env python3
"""Adjudicate a clear audio/speech-specific ICASSP ambiguity slice."""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
if (DATA/"icassp-2026-semantic-reviewed-batch-054.json").exists():
    print(json.dumps({"batch_id":"icassp-2026-semantic-batch-054","status":"preserved-input","reviewed_count":json.loads((DATA/"icassp-2026-semantic-reviewed-batch-054.json").read_text())["reviewed_count"]}))
    raise SystemExit(0)
ASSIGNMENTS={
 "23a2d1975dc0c7f9c93d8f60b4ea15d8e302d571":("meaning-and-interaction","grounding-and-action","referential-grounding"),
 "28bdc6f9e8de67c3fb8041755e60fa0ba9e9cf71":("sound-and-production","room-channel-and-sensing","non-airborne-sensing"),
 "2e629793880f57253fa78cb9e58eba5a866b2f06":("listening-and-separation","echo-and-reconstruction","acoustic-echo-cancellation"),
 "3def9cb8f015c81f6a44378551a1c94613376f9c":("meaning-and-interaction","grounding-and-action","referential-grounding"),
 "5dd522f2b7bd4e4bd512d307db75d988fe9e2cb5":("meaning-and-interaction","grounding-and-action","speech-act"),
 "64fba9c44a881e6a3ddfd9a8f41ea3b2a286fa42":("sound-and-production","room-channel-and-sensing","reverberant-mixture"),
 "78329b6217b8a008c04b46108b02f51dc6f09463":("sound-and-production","room-channel-and-sensing","microphone-channel"),
 "7cc3243cdaee92d6c7d65a21bcc2761ac3e2685f":("people-variation-and-health","human-centered-evaluation","listener-effort"),
 "8113872b69701af8aaeadbd9db1af15ba29371cc":("meaning-and-interaction","grounding-and-action","referential-grounding"),
 "884a398170cf1e3ea9b63a455db42b433a5b4162":("sound-and-production","room-channel-and-sensing","microphone-channel"),
 "bd2bacf64a664b31d493bd21ad3563b32fd89be6":("sound-and-production","source-filter-production","periodic-source"),
 "d02fafa19a3ca6416c1cb66d42bcad99c167ca5e":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake"),
 "dcf1cfac25f51e1490915903a948998d3be86a38":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake"),
 "faeec59c814a27f42e0869a5dd0781556a62105c":("meaning-and-interaction","grounding-and-action","referential-grounding"),
 "fde621abd515c9d0ec593beb4c863ff16bf82ce7":("sound-and-production","room-channel-and-sensing","reverberant-mixture"),
}
queue=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text()); papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,(theme,subtheme,concept) in ASSIGNMENTS.items():
 c=next(r for r in queue["rows"] if r["paper_id"]==pid)
 if c.get("review_state")=="analyst-reviewed" or c.get("decision")!="ambiguous": raise SystemExit(f"not unresolved ambiguous: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":f"analyst-reviewed-{depth}","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":f"The title{(' and preserved abstract' if abstract else '')} names an audio/speech object and bounded intervention that instantiate {concept} under {subtheme}; taxonomy membership is resolved, but full-paper mechanism and independent reproduction remain unestablished.","evidence_excerpt":abstract[:1400] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"Title/abstract evidence supports taxonomy membership only; full-paper mechanism, failure analysis, and independent reproduction remain unestablished."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-054","status":"analyst-reviewed-explicit-audio-speech-assignment-batch","claim_boundary":"These records resolve clear audio/speech-specific ambiguous cases using preserved title/abstract evidence; they do not establish full-paper mechanism or performance.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-054.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D1":sum(r["evidence_depth"]=="D1" for r in rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
