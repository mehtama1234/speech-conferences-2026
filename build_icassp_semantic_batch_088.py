"""Close three ICASSP records with explicit non-speech program evidence."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"data"
OUT=DATA/"icassp-2026-semantic-reviewed-batch-088.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
REASONS={
"7c4730aa7ff501bbdecd52ca3481792ad72c03c4":"ASRC-SNN is listed in ICASSP's MLSP session for advanced neural architectures and signal/vision processing. The title names only a generic spiking-network architecture; it identifies no spoken-speech object, speaker, language, or speech evaluation.",
"b3be7236def85744c30b3954b8d7a4e5579564ec":"pMoE is listed in the BISP session on brain structure and function, alongside intracranial and fMRI work. The title identifies emotion recognition but no spoken-speech input or speech target, so it is not assignable to the speech taxonomy from the preserved evidence.",
"d3cfc0dfb96dfe74817b78e371035965a4d45122":"CAF-Mamba is multimodal depression detection on LMVD and D-Vlog. Its preserved abstract describes modality fusion but does not identify speech or voice as an input, target, or evaluation object; this is a clinical affect-prediction record rather than a speech record.",
}
q=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,reasoning in REASONS.items():
 candidate=next(r for r in q["rows"] if r["paper_id"]==pid)
 if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP program/discovery evidence resolves taxonomy membership only; it does not characterize scientific quality or the full-paper mechanism."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-088","status":"analyst-reviewed-explicit-program-boundary-batch","claim_boundary":"These records are excluded because the preserved ICASSP program or abstract evidence identifies a generic architecture, brain-signal emotion task, or clinical affect task without a speech object. The four remaining multimodal-emotion/sentiment cases stay unresolved.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"unsupported":len(rows)}))
