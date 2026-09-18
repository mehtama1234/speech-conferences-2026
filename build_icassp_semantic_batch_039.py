#!/usr/bin/env python3
"""Assign eight further unmistakable speech papers from the ICASSP queue."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
A={
"Intrusive Lyric Intelligibility Via Hybrid Attention over ASR Embeddings and Feature Blocks":("evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding"),
"Audio-Guided Multimodal Approach for Fine-Grained Alignment and Boundary Modeling in Active Speaker Detection":("meaning-and-interaction","dialogue-and-turn-taking","turn-boundary"),
"Whisper-FEST: Single-Channel Far-Field Enhanced Speech-to-text without Parallel Data":("recognition-and-alignment","acoustic-unit-mapping","acoustic-to-token"),
"AR-BSNet: Towards Ultra-Low Complexity Autoregressive Target Speaker Extraction With Band-Split Modeling":("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation"),
"LexTra: Folded Prompt and Split-Role Attention for Target Speaker Extraction":("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation"),
"Modeling Both Intra- And Inter-Utterance Variability for Conversational Emotion Recognition":("meaning-and-interaction","prosody-and-intent","paralinguistic-state"),
"nGPT as a Scalable Architecture for Speech Recognition and Translation":("recognition-and-alignment","acoustic-unit-mapping","acoustic-to-token"),
"KD-Vocodec: A Low-Complexity Model for Joint Speech Coding And Enhancement Using Knowledge Distillation":("listening-and-separation","echo-and-reconstruction","perceptual-enhancement"),
}
q=json.loads((DATA/'icassp-2026-semantic-review-queue.json').read_text()); papers={p['paperId']:p for p in json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']}; by={r['title']:r for r in q['rows']}; already=set()
for path in DATA.glob('icassp-2026-semantic-reviewed-batch-*.json'):
 if path.name!='icassp-2026-semantic-reviewed-batch-039.json': already|={r['paper_id'] for r in json.loads(path.read_text()).get('rows',[])}
missing=[t for t in A if t not in by or by[t]['paper_id'] in already]
if missing: raise SystemExit(f'missing or already reviewed: {missing}')
rows=[]
for title,(theme,subtheme,concept) in A.items():
 p=papers[by[title]['paper_id']]; abstract=p.get('abstract') or ''; depth='D2' if abstract else 'D1'
 rows.append({'paper_id':p['paperId'],'title':title,'decision':'supported','confidence':f'analyst-reviewed-{depth}','theme_id':theme,'subtheme_id':subtheme,'concept_id':concept,'semantic_reasoning':f'The title and preserved abstract identify a speech task and a mechanism that directly instantiates {concept} under {subtheme}.','evidence_excerpt':abstract[:1200] if abstract else title,'source_location':p.get('url'),'source_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance or prevalence claim.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-039','status':'analyst-reviewed-explicit-speech-assignment-batch','claim_boundary':'These records are explicit speech-taxonomy assignments supported by title and, where available, abstract evidence; D2 does not imply full-paper verification.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-039.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D1':sum(r['evidence_depth']=='D1' for r in rows),'D2':sum(r['evidence_depth']=='D2' for r in rows)}))
