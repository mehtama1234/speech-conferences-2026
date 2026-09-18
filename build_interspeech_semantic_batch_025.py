"""Close explicit non-speech INTERSPEECH records without upgrading weak evidence."""
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"data"; OUT=D/"interspeech-2025-semantic-reviewed-batch-025.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
REASONS={
"li25o_interspeech":"Dog2vec represents canine vocalizations, not human spoken speech; the title identifies an animal-vocalization object outside this atlas's spoken-speech taxonomy.",
"patakis25_interspeech":"Semantic-aware multimodal music auto-tagging studies music labels rather than a spoken-speech signal, speaker, language, or speech task.",
"uehara25_interspeech":"Zero-shot acoustic event classification targets general environmental/acoustic events; the title identifies no spoken-speech object or speech-specific target.",
"ren25_interspeech":"Audio descriptions inferred from silent video are a vision-to-audio reasoning task; the title identifies no observed spoken speech or speech-specific output.",
}
q=json.loads((D/"interspeech-2025-semantic-review-queue.json").read_text()); papers={p["paper_id"]:p for p in json.loads((D/"interspeech-2025-papers.json").read_text())["papers"]}; rows=[]
for pid,reason in REASONS.items():
 p=papers[pid]; rows.append({"paper_id":pid,"title":p["title"],"decision":"unsupported","confidence":"analyst-reviewed-D1","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":reason,"evidence_excerpt":p["title"],"source_location":p["paper_url"],"source_sha256":hashlib.sha256((p.get("abstract") or "").encode()).hexdigest(),"evidence_depth":"D1","review_state":"analyst-reviewed","claim_boundary":"Title-level official archive evidence resolves taxonomy membership only; it does not characterize the full paper's mechanism or quality."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-batch-025","status":"analyst-reviewed-explicit-non-speech-boundary-batch","claim_boundary":"These four records explicitly name animal vocalization, music tagging, general acoustic events, or audio-from-silent-video reasoning rather than spoken speech. Other insufficient-evidence records remain open.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows)}))
