"""Targeted adjudication of clear non-speech technical tasks."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"data"
OUT=DATA/"icassp-2026-semantic-reviewed-batch-082.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
REASONS={
"a0cea5dc6f1e73b5ea79b7b15e0c6a3c901c7a1c":"Range-dependent matched-field geoacoustic inversion estimates underwater acoustic environments, not spoken speech.",
"a36581b39060548c5b5f29243559f8abf30165ae":"Graph-regularized image denoising is visual image processing, not speech.",
"a396da02e5f670c13294268dddba2bb09cfae059":"Movable-antenna placement for angle-of-departure estimation is wireless localization, not speech.",
"a415b9ab7134fbb4f6d6202b571af043a2e2cc1c":"A vertical-motion circular-array design is spatial array engineering, not speech.",
"a58670493e7b52b518c93b39377c84d2af7a288f":"Contextual-bandit DOA estimation with backscatter tags is wireless spatial sensing, not speech.",
"a816e396701e1ef7877dfe906c83f82c8b340f0f":"EEG-based emotion recognition is neural-signal analysis, not speech.",
"a8c4707eaf1a9a6d43547ac22d82d56a185f2720":"Differential beamformer analysis concerns microphone-array design in general; the title does not identify spoken speech.",
"a90d20de980a08a4da992157083ada853eb130bc":"Clinical-data standardization with LLMs is healthcare data integration, not speech.",
"a9bb9fa0219a4451c41cdae2eb2424b6cbf45527":"ECG generation is biomedical waveform synthesis, not speech generation.",
"aad1736ae2cc7a93bc8158421213d667fb0ec51f":"ECG representation learning for heart-disease detection is cardiac analysis, not speech.",
"af079a5a118c7df0aa1484af276af54d784dd2e3":"EEG emotion recognition is brain-signal analysis, not speech.",
"b1b92ff681bb08fdb9051335424354b653f33f50":"Fine-grained DOA representation learning is spatial sound-source estimation, not speech.",
"b3225442d068e7563c60303b95a85b71a7f12f90":"Object grounding against visual occlusion is computer vision, not speech.",
"b61f55bff699dbf1ab1062327347316c3b5b2c79":"Cross-subject EEG emotion recognition is neural-signal analysis, not speech.",
"b63fb76b5040fe681f557de4b75e1b91f410c573":"Geometry-aware multilingual text editing is text processing, not spoken speech.",
"b76826ae4ce7e39ce88fdd65189d0719f8bdb29b":"Wearable PPG learning with clinical labels is cardiovascular sensing, not speech.",
"b7a28cf3c7b7ed00eac34946c4e27b00693eba7e":"Ultrasound-aware detection is medical imaging, not speech.",
"b919ef1ef91295f60aaa48903dd5d076999394e0":"fNIRS-guided EEG BCI enhancement is brain-computer-interface signal processing, not speech.",
"bdc8eb134a5868417e2deeec7c8de48a3c15df0b":"Wideband DOA estimation is array spatial processing, not speech.",
"bea1b0465770b952710a130cd042ff5a08222a5c":"Prompted DOA estimation matches semantic and spatial signals for localization, not speech.",
"bee4eb9b8475b9924b6f954a97238a4b59d56044":"Analog beamformer design for ISAC is wireless sensing and communications, not speech.",
"bf7d18520464de2ad4f20e3c07d0cee72c032390":"Passive-radar target-echo detection is radar sensing, not speech.",
"c01e7da08d5ed2b2d3b8921f8b1ce5559d917166":"Random-matrix analysis of echo-state networks is general machine-learning theory, not a speech task.",
"c48e11f938799ad6e6347c2fe800eb00ca1cd89d":"Magnetic-sensor-array tracking is object localization, not speech.",
"c4d89d91e00ba4f956a678683cdef5945503498e":"Cognitive-ultrasound transmit beamforming is medical sensing, not speech.",
"c8c25a9ae96b260ad46dc57c17d11a4c8d102e9f":"Ultrasound image segmentation is medical computer vision, not speech.",
"c8d75b2fb11098f0a0bb02011bb4927473be2613":"MIMO channel calibration is wireless communications engineering, not speech.",
"cfc98ad47c3a42ffc52e3a0fe23ee43b4593eb78":"Cross-subject EEG emotion recognition is neural-signal analysis, not speech.",
"cfe41dec15ddf04fbd768fbee1fb26498e0cc4a2":"Large-array beamforming without CSI is wireless signal processing, not speech.",
"d28bbce573f5132835c0a3eafa8cbda75ad040b2":"Power optimization in ELAA-assisted ISAC systems is wireless systems engineering, not speech.",
}
q=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,reasoning in REASONS.items():
 candidate=next(r for r in q["rows"] if r["paper_id"]==pid)
 if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-082","status":"analyst-reviewed-targeted-non-speech-technical-batch","claim_boundary":"These decisions exclude explicit biomedical, wireless, array, vision, localization, and text-only tasks from the spoken-speech taxonomy using preserved title/abstract evidence.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"unsupported":len(rows)}))

