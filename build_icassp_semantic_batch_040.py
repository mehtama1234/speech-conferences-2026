#!/usr/bin/env python3
"""Assign eight further unambiguous speech cases from the ICASSP queue."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
A={
"Attention2Probability: Attention-Driven Terminology Probability Estimation for Robust Speech-to-text System":("recognition-and-alignment","adaptation-and-open-vocabulary","domain-and-context-biasing"),
"Adversarial Defense via Generative Speech Enhancement Module":("evaluation-deployment-and-consequence","robustness-and-system-boundary","distribution-shift"),
"Progressive Refinement Training for Low-Resource Neural Speech Coding and Enhancement":("listening-and-separation","echo-and-reconstruction","perceptual-enhancement"),
"Flexi-LoRA with Input-Adaptive Ranks: Efficient Finetuning for Speech and Reasoning Tasks":("languages-accents-and-resources","low-resource-and-data-creation","few-shot-adaptation"),
"ZSV2C-MLLM: Zero-Shot Visual Voice Cloning Via Multimodal Large Language Models":("voice-generation-and-control","voice-identity-and-conversion","zero-shot-voice"),
"Eosign: Edge-Efficient One-Shot ISL Video Synthesis from Code-Mixed Speech with Signer Consistency and Temporal Stability":("languages-accents-and-resources","multilingual-and-crosslingual","code-switching"),
"VT-Heads: Voice Cloning and Talking Head Generation from Text Based on V-DiT":("voice-generation-and-control","voice-identity-and-conversion","voice-conversion"),
"PoemCraft: Multimodal Poetry Generation with Prosody-Guided Refinement and Biased Attention":("voice-generation-and-control","prosody-and-interactive-control","prosody-control"),
}
q=json.loads((DATA/'icassp-2026-semantic-review-queue.json').read_text()); papers={p['paperId']:p for p in json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']}; by={r['title']:r for r in q['rows']}; already=set()
for path in DATA.glob('icassp-2026-semantic-reviewed-batch-*.json'):
 if path.name!='icassp-2026-semantic-reviewed-batch-040.json': already|={r['paper_id'] for r in json.loads(path.read_text()).get('rows',[])}
missing=[t for t in A if t not in by or by[t]['paper_id'] in already]
if missing: raise SystemExit(f'missing or already reviewed: {missing}')
rows=[]
for title,(theme,subtheme,concept) in A.items():
 p=papers[by[title]['paper_id']]; abstract=p.get('abstract') or ''; depth='D2' if abstract else 'D1'
 rows.append({'paper_id':p['paperId'],'title':title,'decision':'supported','confidence':f'analyst-reviewed-{depth}','theme_id':theme,'subtheme_id':subtheme,'concept_id':concept,'semantic_reasoning':f'The title and preserved abstract identify a speech task and a mechanism that directly instantiates {concept} under {subtheme}.','evidence_excerpt':abstract[:1200] if abstract else title,'source_location':p.get('url'),'source_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance or prevalence claim.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-040','status':'analyst-reviewed-explicit-speech-assignment-batch','claim_boundary':'These records are explicit speech-taxonomy assignments supported by title and, where available, abstract evidence; D2 does not imply full-paper verification.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-040.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D1':sum(r['evidence_depth']=='D1' for r in rows),'D2':sum(r['evidence_depth']=='D2' for r in rows)}))
