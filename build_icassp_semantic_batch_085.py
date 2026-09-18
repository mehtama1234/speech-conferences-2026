"""Targeted adjudication of speech-adjacent multimodal and auditory-attention papers."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"data"
OUT=DATA/"icassp-2026-semantic-reviewed-batch-085.json"
if OUT.exists():
 p=json.loads(OUT.read_text()); print(json.dumps({"batch_id":p["batch_id"],"status":"preserved-input","reviewed_count":p["reviewed_count"]})); raise SystemExit(0)
ASSIGNMENTS={
"0510abedf28ab2ff580cde1a691e1189cc53fe73":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","The title identifies heterogeneous multimodal emotion recognition. The audio/voice emotion component makes this a speech-adjacent paralinguistic problem, while the record is not evidence that every modality or result is speech-specific.","multimodal speech emotion"),
"24c48679e5b5b9c0f7326cb5edb70880365a0f6e":("meaning-and-interaction","dialogue-and-turn-taking","interactional-feedback","Auditory-attention decoding asks which competing speaker or stream a listener is selecting. The record places it in the ICASSP brain/HCI auditory-attention track; the assignment is to listener selection in mixed speech, not ordinary ASR.","auditory attention in mixed speech"),
"5333a836a46f3b563dcdc5e9dedd98af93698b59":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Multimodal emotion recognition in conversations treats affect carried across conversational turns and audio-visual-text channels; this belongs to speech paralinguistics when the audio channel is spoken interaction.","conversational speech emotion"),
"68edcdb1a7eeeb95d1b3cef31da62bd72ac5bad7":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","The external record describes Clue2Emo as integrating audio, video, and text for open-vocabulary emotion recognition. Audio affect is a speech-paralinguistic signal, although the assignment does not claim all modalities are speech.","multimodal speech emotion"),
"916fc9493e71e7ab8bd6d8bb738923d276447efe":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Modality-heterogeneous emotion recognition concerns affective information carried by conversational audio and other modalities; it is assigned to paralinguistic state with a multimodal evidence boundary.","multimodal speech emotion"),
"918f732e16d886a9034de5dcb511ec0f2233f100":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Emotion recognition in conversation concerns how affect is expressed and interpreted across turns; multimodal conversational records include the spoken channel, so the speech contribution is paralinguistic rather than word recognition.","conversational speech emotion"),
"b79cec720f1d85878b8aba254c543ba40d367a4e":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Multimodal conversational emotion recognition models affect across turns and modalities, including spoken interaction; its speech role is paralinguistic state rather than lexical decoding.","conversational speech emotion"),
"bccd76bb5f248e0565b9b76458ea2fdde31dabee":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Fine-grained conversational emotion recognition studies emotional change and contagion across turns, a speech-paralinguistic problem when the conversation audio is used.","conversational speech emotion"),
"cebaec8acc70e6390a269b4e2d456e318ef1a4ab":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Fine-grained modality alignment for emotion in conversations aligns affective evidence across spoken and non-spoken channels; the speech membership is paralinguistic and multimodal.","conversational speech emotion"),
"e45510076a027f702edb742c8752c28cb223dc6b":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Emotion inertia and contagion in conversations concern affective state carried through successive spoken turns, not just word identity.","conversational speech emotion"),
"e5cfa34259fb4eed3c2d7c3aacde858b19d0cc43":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Graph-based modality alignment for conversational emotion recognition concerns affective meaning across spoken interaction and companion modalities.","conversational speech emotion"),
"f2abc333ac4fd78e1783e0a3d0cd0a7afa852630":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Inter-dialog contrastive learning compares affective states across conversations; the speech contribution is conversational paralinguistic meaning, not transcription.","conversational speech emotion"),
}
q=json.loads((DATA/"icassp-2026-semantic-review-queue.json").read_text())
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]
for pid,(theme,subtheme,concept,reasoning,family) in ASSIGNMENTS.items():
 candidate=next(r for r in q["rows"] if r["paper_id"]==pid)
 if candidate.get("review_state")=="analyst-reviewed": raise SystemExit(f"already reviewed: {pid}")
 p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":f"analyst-reviewed-{depth}","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1200] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":f"Title plus targeted conference/source evidence supports broad conceptual membership as {family}; the record does not establish that every modality, dataset, or reported result is speech-specific."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-085","status":"analyst-reviewed-targeted-speech-adjacent-multimodal-batch","claim_boundary":"These records are assigned to speech paralinguistics or listener selection with an explicit multimodal boundary; they are not treated as ordinary ASR or as proof that every modality is speech.","reviewed_count":len(rows),"rows":rows}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"supported":len(rows)}))
