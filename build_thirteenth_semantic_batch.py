#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/'data'
A={'rong25_interspeech':('listening-and-separation','echo-and-reconstruction','packet-loss-concealment','Packet loss is missing acoustic evidence that requires explicit reconstruction before ordinary enhancement.'),'kim25d_interspeech':('recognition-and-alignment','adaptation-and-open-vocabulary','open-vocabulary-recognition','Open-vocabulary spotting integrates word alignment into end-to-end streaming recognition instead of relying on fixed keyword lists.'),'inoue25b_interspeech':('people-variation-and-health','clinical-and-assistive-speech','augmentative-communication','Silent-speech decoding treats heterogeneous EEG/EMG sensing and patient transfer as central to assistive communication.')}
P={p['paper_id']:p for p in json.loads((D/'interspeech-2025-papers.json').read_text())['papers']}; N={n['paper_id']:n for n in json.loads((D/'interspeech-2025-thirteenth-d3-notes.json').read_text())['notes']}; C={p['paper_id']:p for p in json.loads((D/'interspeech-2025-thirteenth-d3-papers.json').read_text())['papers']}
rows=[]
for pid,a in A.items():
 p,n,cap=P[pid],N[pid],C[pid]
 rows.append({'paper_id':pid,'title':p['title'],'decision':'supported','confidence':'analyst-reviewed-D3','theme_id':a[0],'subtheme_id':a[1],'concept_id':a[2],'semantic_reasoning':a[3],'evidence_fields':['bp','wh','naive','ap','mech','math','dots','ww','limits'],'evidence_excerpt':'Problem: '+n['bp']+' Mechanism: '+n['mech']+' Result: '+n['ww']+' Boundary: '+n['limits'],'source_location':p['paper_url'],'source_sha256':hashlib.sha256(p['abstract'].encode()).hexdigest(),'evidence_depth':'D3','review_state':'analyst-reviewed','claim_boundary':'Captured official PDF supports the structured note; results remain author-reported and were not independently reproduced.'})
payload={'schema_version':1,'batch_id':'interspeech-2025-semantic-d3-batch-011','status':'analyst-reviewed-D3-batch','claim_boundary':'Three assignments are analyst-reviewed from captured official PDFs and structured notes; claims are not independent reproductions.','reviewed_count':len(rows),'rows':rows}
(D/'interspeech-2025-semantic-reviewed-d3-batch-011.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n'); print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D3':len(rows)}))
