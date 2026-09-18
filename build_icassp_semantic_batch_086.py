"""Targeted closure of explicit non-speech records in the final boundary set."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"data"
OUT=DATA/"icassp-2026-semantic-reviewed-batch-086.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
REASONS={
"21e048a7204c9bd820106cdf91313e6954832bba":"Audio-visual zero-shot learning is a general multimodal recognition problem; the title does not identify spoken speech, a speech speaker, or a speech-specific target.",
"690ed32b7d3ddeb8a7127788e6380f0cd1015857":"Multi-view depression detection is a clinical prediction problem; the title does not identify speech or voice as an input or target.",
"97163fb4d7970c9dd459c416f909641383944eb7":"Sarcasm-robust multimodal depression detection is a clinical affect-prediction problem, not a speech-specific task on the preserved evidence.",
"a050dcc43388163f5d75153d8e020e39700aea9f":"Depression detection from gait and physiological signals is clinical biosignal analysis, not spoken speech.",
"b0bf09aa25b7d20ea0107b7be975b2afb5981afe":"Auditory spatial-attention detection identifies sound direction or neural attention, but the title does not establish spoken speech or a speech-specific object.",
"cf5b70ac93fe0912ace69517e01dced442d23979":"MIDI- and composer-conditioned orchestration is music generation, not spoken-speech generation.",
}
q=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,reasoning in REASONS.items():
 candidate=next(r for r in q["rows"] if r["paper_id"]==pid)
 if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-086","status":"analyst-reviewed-targeted-final-non-speech-boundary-batch","claim_boundary":"These explicit clinical, generic-audiovisual, auditory-spatial, and music tasks are excluded from the spoken-speech taxonomy; generic audio-language and multimodal-emotion cases remain unresolved.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"unsupported":len(rows)}))
