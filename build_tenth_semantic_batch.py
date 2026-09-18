#!/usr/bin/env python3
"""Record semantic assignments for the tenth full-paper D3 set."""
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
 "guo25b_interspeech": ("sound-and-production","time-frequency-measurement","multi-resolution-signal","Extended high-frequency cues are tested as an acoustic factor in phoneme recognition under masking."),
 "zhao25b_interspeech": ("listening-and-separation","echo-and-reconstruction","acoustic-echo-cancellation","Room impulse response prompts condition echo cancellation on the physical echo path to improve mismatch generalization."),
 "freisinger25_interspeech": ("recognition-and-alignment","boundaries-and-sequence-structure","alignment","Hierarchical transcript segmentation treats topic boundaries as nested sequence structure rather than flat cuts."),
 "lee25h_interspeech": ("voice-generation-and-control","text-to-speech-and-content","neural-vocoder","Depthwise codec decoding trades cross-level synthesis quality against streaming latency and model size."),
 "harmsen25_interspeech": ("people-variation-and-health","human-centered-evaluation","accessibility-fit","ASR-derived child reading measures are checked against human-transcript measures to test whether automation preserves the educational construct."),
 "do25_interspeech": ("evaluation-deployment-and-consequence","robustness-and-system-boundary","latency-and-resource","Vocabulary-first and structural pruning preserve spoken-language-understanding task structure under device resource limits."),
 "kibria25_interspeech": ("evaluation-deployment-and-consequence","metrics-and-targets","quality-and-naturalness","A small attention model predicts listener quality while exposing how MOS prediction fails under domain shift."),
 "leschanowsky25_interspeech": ("listening-and-separation","noise-enhancement","perceptual-enhancement","Subjective intelligibility testing separates whether a codec preserves identifiable speech from whether it merely scores well on quality or WER."),
}
papers={p["paper_id"]:p for p in json.loads((DATA/"interspeech-2025-papers.json").read_text())["papers"]}
notes={n["paper_id"]:n for n in json.loads((DATA/"interspeech-2025-tenth-d3-notes.json").read_text())["notes"]}
rows=[]
for pid,a in ASSIGNMENTS.items():
 p,n=papers[pid],notes[pid]
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D3","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_fields":["bp","wh","naive","ap","mech","math","eval","ww","limits"],"evidence_excerpt":"Problem: "+n["bp"]+" Mechanism: "+n["mech"]+" Result: "+n["ww"]+" Boundary: "+n["limits"],"source_location":p["paper_url"],"source_sha256":hashlib.sha256(p["abstract"].encode()).hexdigest(),"evidence_depth":"D3","review_state":"analyst-reviewed","claim_boundary":"Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d3-batch-008","status":"analyst-reviewed-D3-batch","claim_boundary":"Eight assignments are analyst-reviewed from captured official PDFs and structured notes; claims are not independent reproductions.","reviewed_count":len(rows),"rows":rows}
(DATA/"interspeech-2025-semantic-reviewed-d3-batch-008.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D3":len(rows)}))
