"""Targeted adjudication of clear non-speech technical tasks."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"data"
OUT=DATA/"icassp-2026-semantic-reviewed-batch-083.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
REASONS={
"d8a90f13a1896b282d2dcd744cc945571f95d3e8":"Perturbation-resistant transmit beamforming is wireless array engineering, not speech.",
"d9e20f648883b145b03cb1d8f3602a61a2da7b81":"Antenna selection and hybrid beamforming for ISAC is wireless communications, not speech.",
"db20f92811649ba8c03d3d5121da854df82473a0":"Medical vision-language reasoning concerns clinical imaging and reports, not speech.",
"dc095a0424b6e7d7810dfe850e115fbe80cfab53":"Biosignal personalization is general clinical signal learning, not a speech task.",
"dc7eb669348b55ed6dad195260f83280ef4c5b0a":"EEG emotion recognition is neural-signal analysis, not speech.",
"dde6489f43b7c93591c6666329755108366d9bde":"ECG lead reconstruction is biomedical waveform reconstruction, not speech.",
"e0b14b7f94f5ddb05cd4b10f197def46872cddac":"Cone-beam CT reconstruction is medical imaging, not speech.",
"e0dc4226b2d91ec6c5ea9e85b32a6aba1ac55642":"Generic image super-resolution does not identify a spoken-speech object.",
"e22fffdfacddd15490c1d346d0a76514ac011c3c":"Radar detection from spectrograms is radar sensing, not speech.",
"e2564dfe999a221fd51503421069b36c1c7fe78b":"RIS beamforming for multiuser MIMO is wireless communications, not speech.",
"e57916cd16646c558838d8d94b8b5235f96735f7":"Note tracking and multi-pitch estimation concern musical audio, not spoken speech.",
"e7c60c5933cf435be546d00f256c6c6c1b5b34c5":"RIS-enabled waveform diversity in radar is radar engineering, not speech.",
"e7d69ca234824da26618e7c59bb65ea6225a303b":"Recovery of radar waveforms from ADC measurements is radar signal processing, not speech.",
"e81754b75af5821b782c524d3546fd256dd89b5a":"ECG-based emotion recognition is biomedical signal analysis, not speech.",
"e89eff06f76121cefd941657de3c9bb83837a179":"Decomposing multilingual representations is text or language-model analysis without a spoken-speech task.",
"e8d324173f616d11c6aa636b222ce0a5ba369bc6":"Left-ventricle segmentation and echocardiographic analysis are medical imaging, not speech.",
"e8d69938790ad879b7a9b3dcce3a5992edea9471":"Flexible sparse-array design for DOA is spatial signal processing, not speech.",
"e9e917a169d51362218df44e762346406974a240":"Gridless DOA estimation is array localization, not speech.",
"ea2de96b4f53a4a9ef5879c436a7d5ce34ed64c2":"Cross-subject emotion recognition is a physiological or neural-signal task, not speech.",
"ea3c01ebb75b9b7d8e5390b1449599e0039b73a2":"EEG-eye emotion recognition is neural and eye-movement analysis, not speech.",
"eb2c0c9a7fb7cbfe2d745a886adfcd326dc725ef":"Wideband gridless DOA estimation is spatial signal processing, not speech.",
"eca66134da515c7956dfed569d79c0f4e0b04160":"Photodiode-array orientation for optical wireless reception is communications hardware, not speech.",
"ed18417864c8474f5a206976612e61ee8fbcfa79":"ECG-to-diagnostic-report generation is cardiac clinical reporting, not speech.",
"ed3c302eb38dd816d0ab5fb8edebb77170618001":"Breast-ultrasound diagnosis is medical imaging, not speech.",
"ee003c2bd4502ccc1de1329796e78737d762fc86":"Sparse-array covariance reconstruction is array signal processing, not speech.",
"ef1bc94b80bd68ca2571752c58f1fde8be1e7de7":"Eye tracking for clinical digital biomarkers is visual behavioral sensing, not speech.",
"ef76db122bfeae6c42efc2ad24786bb19e3cca7f":"Video-based heart-rate estimation is physiological video sensing, not speech.",
"f0ce94897a1a603c9139f9ec026294afa8a917cf":"Radar micro-Doppler denoising is radar signal processing, not speech.",
"f183ec7fad8dcd5489725cbcd54bb04d4f6a4bc1":"EEG and eye-movement depression detection is clinical biosignal analysis, not speech.",
"f2366ca8265e29b3ca9a797d3370f1d31412576f":"Traffic-transformer pretraining uses traffic data, not speech.",
"f326f2d2622f1183ab4a804e45d419cd66640263":"Multilingual mathematical reasoning is text reasoning, not spoken speech.",
"f604ff63e5f5cdee9b63a2e69f2bf7082fed118b":"Near-field wideband beamforming for ISAC is wireless sensing, not speech.",
"f68d2aac9452f32ffbb0665a48bd6a6b82834ff8":"Blood-pressure waveform generation is cardiovascular signal synthesis, not speech.",
"f7463cc801cd07f5ad930ff6808a9b3b29b188c1":"MVDR beamforming is spatial filtering, not a speech-specific task.",
"f883e5e85ba043c3c312daf2515fb2fcea88b94e":"PTSD effects of virtual nature immersion are clinical neuroscience, not speech.",
"fb543eb47059f0f4ac67f7ea094b8331c48cc699":"Multimodal healthcare representation learning is clinical data modeling, not speech.",
"fb9f194a44c40cabfa5548d8608399b8063b3428":"Ultrasound image despeckling is medical image processing, not speech.",
"fecc32551534a692cd2866f876ba88554afc1fc8":"EEG forecasting is neural-signal prediction, not speech.",
"feee811ac6292b6e45fcfa80547eaef38f6715cb":"Photovoltaic arc detection is electrical-fault sensing, not speech.",
"ffa339472e85f2225c1c1930dc0a9ed5fdf14c06":"Cognitive FDA radar waveform design is radar engineering, not speech.",
"fffaaa569dcbf8e16171654d0de16966b7cdd5f7":"KV-cache compression is language-model systems engineering without a speech-specific task.",
}
q=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,reasoning in REASONS.items():
 candidate=next(r for r in q["rows"] if r["paper_id"]==pid)
 if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"unsupported","confidence":f"analyst-reviewed-{depth}","theme_id":None,"subtheme_id":None,"concept_id":None,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-083","status":"analyst-reviewed-targeted-non-speech-technical-batch","claim_boundary":"These decisions exclude explicit biomedical, wireless, radar, medical-imaging, music, traffic, and systems tasks from the spoken-speech taxonomy using preserved title/abstract evidence.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"unsupported":len(rows)}))
