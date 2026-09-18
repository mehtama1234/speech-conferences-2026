"""Targeted adjudication of clear non-speech technical tasks."""
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-081.json"
if OUT.exists():
    p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
REASONS = {
"6bf5c70aad72893c4af33ad857d7d10b58713545":"Through-obstacle human-activity recognition is sensing and activity analysis, not speech.",
"6c0fce3c2f4083bc4c5c5a58fc3bd29b022e1d37":"EEG emotion recognition in an olfactory paradigm is neural-signal analysis, not speech.",
"6d5903d53047d9ce2094e1c2c86e69c1fd325a8d":"Face anti-spoofing is visual biometric security, not speech anti-spoofing.",
"6edac9d4277b93f28856372da4c667b4fe4abd7f":"Near-field SWIPT with phased arrays is wireless power and communications engineering, not speech.",
"704e0eb745587225d98b3f9751de920a5b6e3595":"Mapping spaces from echoes and multipaths is spatial sensing, not speech.",
"7130c2bc491052436bb4d43e94d78fa266ee49ec":"ECG and electronic-health-record prognosis is clinical decision support, not speech.",
"71fbb197031ff30c503e3e2cbc98fc180fda23f4":"DOA spectrum reconstruction is array sensing, not speech.",
"7216e3bb0830d11210353aceb39dc4f4959860b3":"Tooth segmentation is dental image analysis, not speech.",
"729711a235b0501f7419298a4ffc7b1ff6026535":"ECG synthesis is biomedical waveform generation, not speech generation.",
"745c77f7c38700819ef23f5961715b909524d689":"Block-sparse signal recovery is mathematical signal processing without a speech object.",
"757605013d8bf8a6acdf05d848b73708c442a15a":"Joint compression and DOA estimation in sensor networks is spatial sensing, not speech.",
"7809e1363d8d1cd197028b7864211efb7309614c":"Lung-cancer screening from biomarkers and clinical text is medical diagnosis, not speech.",
"798f81b083386a121d5a7825f30cf8094a672d60":"Breast-ultrasound segmentation is medical image analysis, not speech.",
"799a3d01a4f4f27d40a8ce523d729c94ae0bc9d5":"Rotating-array DOA estimation is spatial signal processing, not speech.",
"7b3d28344303013cc88f68def024189701497d06":"PPG foundation-model learning is cardiovascular waveform analysis, not speech.",
"7b5acea5f35cc466deede814b0cbc595fd02c4d0":"Covariance estimation for a rectangular array is spatial signal processing, not speech.",
"7fe41d9a197bfb180c59b9c6f5f43aaf07c858c1":"Radar-communications waveform design is wireless engineering, not speech.",
"806162aab5c40506d5b6a7ac46f696bfe1054ee6":"Lung-ultrasound measurement is clinical imaging, not speech.",
"81376b3429343a046dfe814921ee9ed21bbc27c2":"EEG-fNIRS emotion recognition is brain-signal analysis, not speech.",
"8168655e53352b9045e0904c0ecd787de96126e8":"UAV communications spoofing detection is network security, not speech anti-spoofing.",
"818355353bef8aa998fbc8f69b9c53bd58688eea":"Near-field channel estimation with coprime arrays is wireless sensing, not speech.",
"8363c1a955fd86a2991907281dbfe3e970a229e1":"Echocardiographic cardiac-function assessment is medical imaging, not speech.",
"84999d1153d626415628ebdfb83ebef6cc195f20":"12-lead ECG generation is biomedical waveform synthesis, not speech generation.",
"853b86d8910efd21b0998467cb30568cfeeac43d":"Personalized EEG emotion recognition is neural-signal analysis, not speech.",
"869ac364e6c5daed1efa6efbf735a90bd191af71":"Antenna-spacing effects on DOA error are array-design analysis, not speech.",
"87898bbdd5eb490d5fde736ba20993116e0e223c":"Dynamic imaging with Kalman smoothing is image reconstruction, not speech.",
"887ae909319bc6b50424ed9dc2ba8f595b54981b":"Quasi-clique detection is a graph-optimization problem, not speech.",
"892f6c069ca27d883317e47940fd7a66161a6f2a":"Multi-organ ultrasound segmentation is medical image analysis, not speech.",
"89640f1fbabc9099d9084800cdf3e6f4c6c18988":"Underwater DOA estimation is acoustic spatial sensing, not a spoken-speech task.",
"89bf985d10baea15bda00d1b39353e4b491979b4":"mmWave radar liquid-level tracking is industrial sensing, not speech.",
"8aa28cde14d9ad8f46813b02695b3c9e0df73886":"Endoscopic image restoration and segmentation is medical vision, not speech.",
"8ac0c4cf11f5baf2f6040b58beb42d104b82c3d5":"Adapting DOA estimators for downstream tracking is spatial sensing, not speech.",
"8e892f4bb1a0fbb9b1d650eab16434376f1a6b73":"ECG denoising is biomedical waveform processing, not speech enhancement.",
"8e91a4f6972f5fd790282a14cd7b76d36792ce27":"The title gives generic audio question answering but no spoken-speech object; it remains outside the confirmed speech slice on available evidence.",
"920451a198ef0f520188fa1312327fc694845b5e":"Surgical-video understanding is medical vision, not speech.",
"96fb21afc43fb2042a5e84161a063696c15f66d5":"mmWave beam prediction is wireless communications, not speech.",
"97c89e414d443e03b758966c58906f8e920f7526":"Massive-MIMO beamformer design is wireless communications, not speech.",
"97e2f7b719e400777b49674f831436ffee15eb90":"Radar-based blood-pressure estimation is physiological sensing, not speech.",
"9800ea30f8414d4772199f184f0c5e243a0d00dd":"Eye-tracking depression assessment is clinical behavioral sensing, not speech.",
}
queue=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,reasoning in REASONS.items():
    candidate=next(r for r in queue["rows"] if r["paper_id"]==pid)
    if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
    p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
    rows.append({"paper_id":pid,"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-081","status":"analyst-reviewed-targeted-non-speech-technical-batch","claim_boundary":"These decisions exclude explicit biomedical, wireless, array-sensing, medical-vision, industrial-sensing, and graph-optimization tasks from the spoken-speech taxonomy using preserved title/abstract evidence.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"unsupported":len(rows)}))

