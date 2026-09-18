#!/usr/bin/env python3
"""Adjudicate a second clear audio/speech-specific ICASSP ambiguity slice."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
if (DATA/"icassp-2026-semantic-reviewed-batch-055.json").exists():
 print(json.dumps({"batch_id":"icassp-2026-semantic-batch-055","status":"preserved-input","reviewed_count":json.loads((DATA/"icassp-2026-semantic-reviewed-batch-055.json").read_text())["reviewed_count"]})); raise SystemExit(0)
ASSIGNMENTS={
 "47d2baf4376dc54a7adb8073904be2d7fe75d3c6":("meaning-and-interaction","grounding-and-action","referential-grounding"),
 "676675c7bb94470d53620f8a14da4535906bc471":("meaning-and-interaction","grounding-and-action","referential-grounding"),
 "9bb64481817fbd737529a300d60c8cc815957ab5":("listening-and-separation","echo-and-reconstruction","acoustic-echo-cancellation"),
 "9f333419971c9db1df8c114ddde6a48da53caa87":("sound-and-production","room-channel-and-sensing","microphone-channel"),
 "aae3d291d8018c414104c4e4c4917e65bdaf0f92":("sound-and-production","room-channel-and-sensing","reverberant-mixture"),
 "b0f4b9718fb0b578cc7236c65a2a742e83931dea":("listening-and-separation","noise-enhancement","nonstationary-noise"),
 "c89067b31a2e42cffabf0f03fb510b84bd50cb9b":("voice-generation-and-control","text-to-speech-and-content","neural-vocoder"),
 "cd1e64eda4d040b38742ad61f24392dff7615ea8":("recognition-and-alignment","adaptation-and-open-vocabulary","open-vocabulary-recognition"),
 "ecdfa2f086c876480a52026dbb07c1f727c624dc":("people-variation-and-health","human-centered-evaluation","listener-effort"),
 "f5ec0c9842e98d05fc40c3c9fa24dec1f0c6f222":("meaning-and-interaction","grounding-and-action","referential-grounding"),
}
queue=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text()); papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}; rows=[]
for pid,(theme,subtheme,concept) in ASSIGNMENTS.items():
 c=next(r for r in queue["rows"] if r["paper_id"]==pid)
 if c.get("review_state")=="analyst-reviewed" or c.get("decision")!="ambiguous": raise SystemExit(f"not unresolved ambiguous: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":f"analyst-reviewed-{depth}","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":f"The title{(' and preserved abstract' if abstract else '')} names an audio/speech object and bounded intervention that instantiate {concept} under {subtheme}; this resolves taxonomy membership only.","evidence_excerpt":abstract[:1400] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"Title/abstract evidence supports taxonomy membership only; full-paper mechanism, failure analysis, and independent reproduction remain unestablished."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-055","status":"analyst-reviewed-explicit-audio-speech-assignment-batch","claim_boundary":"These records resolve clear audio/speech-specific ambiguous cases using preserved title/abstract evidence; they do not establish full-paper mechanism or performance.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-055.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D1":sum(r["evidence_depth"]=="D1" for r in rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
