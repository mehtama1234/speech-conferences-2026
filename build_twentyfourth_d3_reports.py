"""Write no-jargon notes for D3 batch 024."""
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D, R = H / "data", H / "reports"
C = {x["paper_id"]: x for x in json.loads((D / "interspeech-2025-twentyfourth-d3-papers.json").read_text())["papers"]}
P = {x["paper_id"]: x for x in json.loads((D / "interspeech-2025-papers.json").read_text())["papers"]}

N = {
"kwon25b_interspeech": (
    "A speaker can pronounce the same category differently across sounds and contexts, yet listeners still need the category to remain recognizable.",
    "Variation that looks random in one measurement may be coordinated with variation in another, and context can change both measurements at once.",
    "Average across speakers and treat the remaining variation as noise.",
    "Measure several phonetic dimensions jointly within each speaker and test whether their covariation preserves category contrasts across phonological and morphological contexts.",
    "Seoul Korean word-medial stops are analyzed through speaker-specific distributions and covariation patterns across contexts.",
    "The object is a structured distribution, not one canonical pronunciation; correlations and category separation test whether variation is organized.",
    "The paper reports systematic speaker-specific covariation that keeps stop categories distinct despite contextual variability, supporting a phonetic-uniformity account.",
    "The language, stop system, contexts, speaker sample, and chosen phonetic measures bound the result; other languages and interactional settings require separate evidence.",
),
"mcguire25_interspeech": (
    "To explain an implosive consonant, a researcher must connect its proposed airflow mechanism to the visible movements of the lips and timing of closure and release.",
    "A voiced stop can resemble an implosive in a broad label, so a movement difference may be caused by voicing rather than implosivity.",
    "Describe both sounds as voiced stops and assume the same articulatory timing.",
    "Track lip-aperture trajectories with electromagnetic articulography and compare Vietnamese implosives against voiced and voiceless controls in another language.",
    "EMA measures movement amplitude, velocity, and plateau timing during Central Vietnamese bilabial implosives; Taiwanese Southern Min controls the voicing explanation.",
    "The signal is a time course of gestures; mixed-effects comparisons separate a property of implosivity from a generic property of voicing.",
    "Implosives show greater peak velocity away from closure, while voiceless plosives have a longer gestural plateau; the voiced-plosive control does not reproduce the rapid movement.",
    "The languages, speakers, consonant inventory, EMA measures, and statistical model bound the result; laryngeal airflow itself was not directly measured.",
),
"oh25_interspeech": (
    "An assessment system should predict several aspects of second-language speaking ability while respecting that speech and words reveal different parts of performance.",
    "A single score hides trait differences, while simply concatenating audio and text features can make one modality dominate or ignore relationships among traits.",
    "Train one unimodal predictor or combine embeddings without modeling how the traits depend on each other.",
    "Use cross-modal attention to exchange information between speech and text and a joint loss that treats the five proficiency traits as related but distinct targets.",
    "MFCC, wav2vec 2.0, GloVe, and BERT embeddings are compared on five L2 English scores with a trait-aware loss and mean Pearson correlation as the main measure.",
    "The prediction target is a vector of human-assigned traits; cross-modal attention and the joint loss encode dependencies that a single aggregate score discards.",
    "The wav2vec 2.0 plus BERT configuration reports the best mean PCC, 0.734 with standard deviation 0.0129 across the five criteria, above unimodal and baseline multimodal systems.",
    "The learner dataset, rubric, rater scores, split, and correlation metric bound the result; correlation is not agreement or evidence that the model understands proficiency.",
),
"ke25_interspeech": (
    "A clinical speech detector may need to use pauses as signs of cognitive change without assuming that one duration threshold works for every language or recording protocol.",
    "Pause meaning depends on where the pause occurs and how its duration is represented to a language model; the same insertion rule can help one task and hurt another.",
    "Add every pause as a fixed token or use a threshold borrowed from another corpus.",
    "Insert between-segment pause context into automatic transcripts and tune the pause-duration representation for each classification task.",
    "Cantonese elderly speech from CU-Marvel is transcribed, pause context is fused into transformer input, and binary dementia tasks are compared under alternative pause groupings.",
    "The pause is treated as structured context attached to a linguistic boundary; classification accuracy and F1 test whether that context adds clinically useful signal.",
    "The paper reports that optimized between-segment pause patterns improve detection and that different tasks prefer different pause representations.",
    "The corpus, language, age group, transcription quality, diagnostic labels, and pause definitions bound the result; this is not a validated clinical biomarker or a causal account of dementia.",
),
"pepino25_interspeech": (
    "One audio representation should support speech, music, and environmental sounds even though the useful information is different in each task.",
    "A pretext target can make a representation good at reconstructing one signal while discarding information needed by another task.",
    "Assume a larger model or a single input representation will be uniformly best everywhere.",
    "Use discrete targets from a neural codec in a masked autoencoder and test the representation across tasks, model sizes, input forms, self-training, and data mixtures.",
    "EnCodecMAE is pretrained on diverse audio and evaluated on pitch, genre, speech commands, emotion, sound events, and environmental sound tasks.",
    "Transfer performance is the test of usefulness; the representation is judged by how task, input, model size, and pretraining diversity change downstream accuracy or error.",
    "The paper reports average gains over prior audio representations and finds that larger models, task-dependent inputs, self-training, and diverse data each matter.",
    "The task suite, pretraining mixture, labels, model comparisons, and aggregate averages bound the claim; average transfer does not prove universal suitability for speech.",
),
"shen25b_interspeech": (
    "An explanation of a speech classifier should identify evidence that genuinely changes the decision, not merely highlight plausible-looking waveform regions.",
    "Speech unfolds in time, so the reliability of an attribution depends on the input representation, the size of the perturbed region, and whether the task is word-based or acoustic.",
    "Apply a standard saliency map and interpret the highlighted frames as causal evidence.",
    "Vary input type, aggregation, and perturbation timespan, then compare attribution stability, faithfulness, and agreement across speech classification tasks.",
    "Experiments use TIMIT and Common Voice with gradient-based saliency and integrated gradients; word-aligned and fixed-timespan perturbations are compared.",
    "Attribution is an intervention-dependent measurement; agreement and error-based scores test whether highlighted regions are reliable under controlled perturbations.",
    "Standard approaches are generally unreliable in speech, except that word-aligned perturbations are more reliable for word-based classification tasks.",
    "The models, tasks, datasets, attribution methods, and reliability definitions bound the result; no explanation method becomes a causal proof from these tests alone.",
),
"vukovic25_interspeech": (
    "Researchers need to ask questions that connect speech, text, video, gesture, and annotation layers without rebuilding a separate tool for each corpus.",
    "Multimodal data are time-aligned but stored and queried in different systems, so a text-only search can miss the speech or gesture event that gives a segment meaning.",
    "Keep each modality in a separate application and manually synchronize results.",
    "Provide one corpus platform with a shared query language, synchronized audiovisual views, and layered annotation that can be queried across modalities.",
    "The LiRI Corpus Platform stores and explores multimodal corpora through DQD queries and time-aligned frontends for text, audio, video, gesture, and spoken transcripts.",
    "The central object is a cross-modal query over aligned annotation intervals; the platform is evaluated by the operations it makes expressible rather than by a classifier score.",
    "The paper demonstrates integrated storage, synchronized querying, layered annotation, and modality-specific frontends for multimodal corpus analysis.",
    "This is an infrastructure demonstration, not evidence that every corpus can be aligned or that research conclusions improve; supported formats, annotations, and user workflows are the boundary.",
),
"zhao25j_interspeech": (
    "An infant must learn tonal categories even when the acoustic cues change with speaker, syllable, and surrounding context rather than repeating one stable value.",
    "Complex tone contrasts may have no single invariant cue, so category learning must use how distributions change across contexts.",
    "Search for one fixed acoustic threshold for each tone and treat contextual variation as noise.",
    "Compare the amount of contextual variation in naturalistic Cantonese speech with which tone contrasts are easier or harder to acquire.",
    "Naturalistic Cantonese productions are analyzed across six tonal contrasts and compared with existing acquisition findings under the Distributional Learning Across Contexts proposal.",
    "The learning signal is a distribution over contexts, not a single token; variation and acquisition difficulty are related at the contrast level.",
    "The paper reports that contextual variation can predict which Cantonese contrasts are easier or harder to learn when invariant cues are absent.",
    "The naturalistic corpus, tone system, acquisition comparison, and distributional measures bound the inference; a prediction from correspondence is not a direct infant-learning experiment.",
),
}
keys = ["bp", "wh", "naive", "ap", "mech", "math", "ww", "limits"]
notes, claims = [], []
md = ["# INTERSPEECH 2025 twenty-fourth-pass full-paper notes", "", "Eight official-PDF readings deepen variation, clinical context, representation, interpretability, multimodal resources, and category learning. Results are author-reported and not independently reproduced.", ""]
for i, (pid, values) in enumerate(N.items(), 1):
    d = dict(zip(keys, values))
    c = C[pid]
    d.update({"paper_id": pid, "title": P[pid]["title"], "subtheme": c["subtheme_label"]})
    notes.append(d)
    md += [f"## {i}. {d['subtheme']}", "", f"**Paper:** [{d['title']}]({P[pid]['paper_url']})", f"**Evidence:** D3; PDF SHA-256 `{c['pdf_sha256']}`; full text captured.", ""]
    md += [f"- **{label}:** {d[key]}" for label, key in zip(["Ordinary problem", "Why hard", "Naive attempt", "Central move", "Mechanism", "Conceptual structure", "What paper reports", "Limits"], keys)] + [""]
    claims.append({"claim_id": f"IS25-D3C24-{i:02d}", "paper_id": pid, "subtheme": d["subtheme"], "claim": d["ww"], "evidence_depth": "D3", "pdf_sha256": c["pdf_sha256"], "full_text_sha256": c["full_text_sha256"], "support_status": "paper-reported-not-independently-verified", "independent_support_status": "not-established", "limitations": d["limits"]})
(D / "interspeech-2025-twentyfourth-d3-notes.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "evidence_depth": "D3", "notes": notes}, indent=2, ensure_ascii=False) + "\n")
(D / "interspeech-2025-twentyfourth-claim-ledger.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "claim_count": len(claims), "claims": claims}, indent=2, ensure_ascii=False) + "\n")
R.mkdir(exist_ok=True)
(R / "INTERSPEECH_2025_TWENTYFOURTH_D3_NOTES.md").write_text("\n".join(md) + "\n")
print(json.dumps({"notes": len(notes), "claims": len(claims)}))
