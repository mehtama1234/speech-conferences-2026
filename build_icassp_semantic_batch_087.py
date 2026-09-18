"""Targeted closure of generic audio records without an identified speech object."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"data"
OUT=DATA/"icassp-2026-semantic-reviewed-batch-087.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
REASONS={
"4ca920bc8999fefccebb89b101ef86156bbc5027":"Transferable audio lottery-ticket sparsity is a general audio-model compression problem; the title does not identify spoken speech, a speaker, or a speech benchmark.",
"66d2a42d1b58a11f671c6fd136fb839829011e1a":"Zero-shot audio-visual learning is a general multimodal learning problem; no spoken-speech object or speech-specific target is identified.",
"6b5ce16ed4b54a1679c41eff31e88d927b414c19":"Segmentwise pruning in audio-language models is a general model-efficiency problem; the title does not establish speech or a speech task.",
"f2206a139d59c8375344eed155f11b4020ec2469":"An audio-text jailbreak attack studies model security broadly; the title does not identify spoken speech or a speech-specific model/evaluation.",
"f464a2306d4bac38d7a5ba54b88c5b06e842a007":"Low-complexity audio intelligence is a broad systems label without a named speech task, speaker, language, or speech evaluation.",
"f52df5546a9f90507d60534630a9328e07f25704":"Audio-visual inference with token clustering is a general multimodal efficiency problem; the title does not establish spoken speech.",
}
q=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,reasoning in REASONS.items():
 candidate=next(r for r in q["rows"] if r["paper_id"]==pid)
 if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-087","status":"analyst-reviewed-targeted-generic-audio-boundary-batch","claim_boundary":"These records are excluded from the spoken-speech taxonomy because preserved evidence identifies only generic audio/audio-visual/model-security work and names no speech object or speech evaluation.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"unsupported":len(rows)}))

