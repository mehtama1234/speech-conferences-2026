#!/usr/bin/env python3
"""Record the fourth full-paper semantic review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ASSIGNMENTS = {
 "benway25_interspeech": ("sound-and-production","source-filter-production","clinical-articulation","The paper uses acoustic-to-articulatory inversion to distinguish clinically meaningful speech-sound error subtypes."),
 "dang25_interspeech": ("listening-and-separation","noise-enhancement","degradation-aware-routing","The central move is to identify the degradation before choosing separation, denoising, or dereverberation, rather than treating all mixtures alike."),
 "he25_interspeech": ("recognition-and-alignment","adaptation-and-open-vocabulary","multi-talker-contextual-asr","The paper jointly handles speaker-overlap transcription and rare-word contextual biasing; the relevant concept is resolving acoustic and lexical uncertainty together."),
 "peng25b_interspeech": ("meaning-and-interaction","dialogue-and-turn-taking","full-duplex-interruption","The paper evaluates interruption and overlap behavior directly because ordinary turn-based benchmarks hide the failures of full-duplex dialogue."),
 "biyani25_interspeech": ("voice-generation-and-control","voice-identity-and-conversion","speaker-content-disentanglement","The method uses time reversal to destroy much linguistic order while retaining speaker-related cues, then uses those representations for voice conversion."),
 "buker25_interspeech": ("people-variation-and-health","speaker-characteristics","spoof-aware-identity","The study treats speaker verification and spoof detection as coupled identity decisions whose shared parameters must be tested across attacks and codecs."),
 "nguyen25_interspeech": ("languages-accents-and-resources","low-resource-and-data-creation","synthetic-code-switching","The paper creates phrase-level mixed-language training examples to reduce the need for costly real code-switching transcripts."),
 "combei25_interspeech": ("evaluation-deployment-and-consequence","robustness-and-system-boundary","real-world-deepfake-shift","The paper treats real-world data coverage and curation as the intervention needed to test whether deepfake detection survives distribution shift."),
}
fourth = json.loads((DATA / "interspeech-2025-fourth-d3-papers.json").read_text())["papers"]
papers = {x["paper_id"]: x for x in fourth}
notes = {x["paper_id"]: x for x in json.loads((DATA / "interspeech-2025-fourth-d3-notes.json").read_text())["notes"]}
rows = []
for paper_id, assignment in ASSIGNMENTS.items():
    note, paper = notes[paper_id], papers[paper_id]
    path = DATA / "interspeech-2025-text" / f"{paper_id}.txt"
    rows.append({"paper_id":paper_id,"title":paper["title"],"decision":"supported","confidence":"analyst-reviewed-D3","theme_id":assignment[0],"subtheme_id":assignment[1],"concept_id":assignment[2],"semantic_reasoning":assignment[3],"evidence_fields":["bp","wh","naive","ap","mech","math","ww","limits"],"evidence_excerpt":"Problem: "+note["bp"]+" Mechanism: "+note["mech"]+" Reported result: "+note["ww"]+" Boundary: "+note["limits"],"source_location":str(path.relative_to(HERE)),"source_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"evidence_depth":"D3","review_state":"analyst-reviewed"})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d3-batch-002","status":"analyst-reviewed-seed-batch","claim_boundary":"These eight assignments are full-paper analyst judgments anchored in captured D3 notes and text. They do not close the whole-corpus queue.","reviewed_count":len(rows),"rows":rows}
(DATA / "interspeech-2025-semantic-reviewed-d3-batch-002.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows)}))
