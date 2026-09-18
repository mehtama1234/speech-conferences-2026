#!/usr/bin/env python3
"""Record the fifth D3 semantic review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
ASSIGNMENTS={
 "chao25b_interspeech":("sound-and-production","time-frequency-measurement","multi-resolution-signal","The paper handles changing time-frequency evidence across distortions, using regression where content is present and generation where it is missing."),
 "dai25c_interspeech":("sound-and-production","room-channel-and-sensing","microphone-channel","The dataset and baseline preserve the room, vehicle, microphone-array, and multi-speaker path that transforms speech before recognition."),
 "byun25_interspeech":("listening-and-separation","echo-and-reconstruction","generative-restoration","The system reconstructs missing or damaged speech with a speaker-agnostic stage followed by identity-guided diffusion restoration."),
 "chao25_interspeech":("meaning-and-interaction","prosody-and-intent","affective-intent","The method makes valence, arousal, and dominance part of response generation so prosodic affect can change the dialogue action."),
 "roychowdhury25_interspeech":("voice-generation-and-control","text-to-speech-and-content","content-intelligibility","The paper tests whether synthesized mathematical speech preserves relations and symbols for listeners, separating intelligibility from naturalness."),
 "li25ea_interspeech":("people-variation-and-health","clinical-and-assistive-speech","human-in-the-loop-annotation","The contribution makes bilingual clinical annotation usable by keeping human correction inside the transcription, speaker, language, and timestamp pipeline."),
 "bokkahallisatish25_interspeech":("people-variation-and-health","human-centered-evaluation","counterfactual-voice-evaluation","The platform changes perceived speaker characteristics while holding the prompt fixed, making speaker-dependent model behavior inspectable."),
}
papers={x["paper_id"]:x for x in json.loads((DATA/"interspeech-2025-fifth-d3-papers.json").read_text())["papers"]}
notes={x["paper_id"]:x for x in json.loads((DATA/"interspeech-2025-fifth-d3-notes.json").read_text())["notes"]}
rows=[]
for pid,a in ASSIGNMENTS.items():
 n=notes[pid]; p=DATA/"interspeech-2025-text"/f"{pid}.txt"
 rows.append({"paper_id":pid,"title":papers[pid]["title"],"decision":"supported","confidence":"analyst-reviewed-D3","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_fields":["bp","wh","naive","ap","mech","math","ww","limits"],"evidence_excerpt":"Problem: "+n["bp"]+" Mechanism: "+n["mech"]+" Reported result: "+n["ww"]+" Boundary: "+n["limits"],"source_location":str(p.relative_to(HERE)),"source_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"evidence_depth":"D3","review_state":"analyst-reviewed"})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d3-batch-003","status":"analyst-reviewed-seed-batch","claim_boundary":"These seven assignments are full-paper analyst judgments targeted at previously uncovered taxonomy subthemes; they do not close the whole-corpus queue.","reviewed_count":len(rows),"rows":rows}
(DATA/"interspeech-2025-semantic-reviewed-d3-batch-003.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows)}))
