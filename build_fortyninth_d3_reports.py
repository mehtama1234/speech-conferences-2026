"""Write first-principles notes for D3 batch 049."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"
captured = {x["paper_id"]: x for x in json.loads((DATA / "interspeech-2025-fortyninth-d3-papers.json").read_text())["papers"]}
papers = {x["paper_id"]: x for x in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}

N = {
"shabtay25_interspeech": {
 "subtheme": "grounding-and-action", "concept": "referential-grounding",
 "bp": "A person wants to ask about an image using speech, while the answer must depend on what is visible rather than on the words alone.",
 "wh": "Speech must be mapped to language while the image supplies the referent; an ASR error can change the question before the visual model sees it.",
 "naive": "Transcribe the question first and hand the text to a text-only visual QA system, assuming speech contains no useful information beyond words.",
 "ap": "Align speech and image encoders directly into a VQA language model so spoken queries and visual evidence can jointly condition the answer.",
 "mech": "Whisper encodes speech and CLIP encodes images; modality-specific projectors align both representations with LLaVA's language space, with speech-only pretraining followed by joint spoken-VQA fine-tuning.",
 "math": "The model predicts an answer from a fused representation. Accuracy, ANLS, and MME scores compare the answer with the task-specific reference; WER separately exposes speech-to-text failure.",
 "ww": "Synthetic speech training approaches the text-trained VQA upper bound on several benchmarks; the paper reports 62% SEED-Bench accuracy for its strongest spoken variants, with TTS choice having a small effect.",
 "limits": "Most training speech is synthesized, the spoken models remain below the text model, prompt format changes performance sharply, and transcription failures can be confused with visual-reasoning failures. No independent reproduction was performed.",
},
"sasu25b_interspeech": {
 "subtheme": "grounding-and-action", "concept": "speech-act",
 "bp": "A robot can hear the same words but need different physical plans depending on which object or relation the speaker emphasizes.",
 "wh": "ASR preserves much of the lexical content but discards stress, rhythm, pauses, and intonation that distinguish competing interpretations.",
 "naive": "Transcribe the instruction, parse the text, and let a language model choose a plan from the words alone.",
 "ap": "Predict token-level goal/detail referents from prosody, then inject those intent cues into an LLM that selects the robot task plan.",
 "mech": "Prosodic and raw-audio features feed Transformer or BiLSTM sequence models trained with cross-entropy; predicted referents are placed in prompts for GPT-4o, o1-mini, or o3-mini to choose among plans.",
 "math": "The sequence model estimates a label distribution for each token; accuracy, precision, recall, and F1 measure referent detection, while plan accuracy measures the final discrete action choice.",
 "ww": "On 1,540 recordings from 22 participants, the best BiLSTM reaches 95.79% overall referent accuracy, and Prosody-Transformer plus GPT-4o reaches 71.96% task-plan accuracy versus 50% for the ASR-only prompt.",
 "limits": "The dataset is small and participants are 18–22; recorded ambiguity and candidate plans are controlled rather than open-world robot interaction. Prosody helps the tested task but does not establish safe execution in physical environments.",
},
"mori25_interspeech": {
 "subtheme": "human-centered-evaluation", "concept": "listener-effort",
 "bp": "A dialogue system needs the words that matter for its response, not necessarily a verbatim transcript of every utterance.",
 "wh": "WER weights function words and content words alike, while people selectively attend to content during response generation; a low WER can therefore hide a consequential miss.",
 "naive": "Evaluate the front-end ASR with ordinary WER, treating every token as equally important.",
 "ap": "Observe selective listening in 297 human participants, estimate part-of-speech importance, and use those weights to form Human-WWER/H-WCER for dialogue-oriented ASR evaluation.",
 "mech": "Participants generate a response and then recall/transcribe the speech; multiple regression estimates POS weights, which are inserted into the edit-distance costs used by weighted WER.",
 "math": "A regression predicts the remembered POS counts from the full transcript; the resulting coefficients weight insertions, deletions, and substitutions in a minimum-edit-distance score. Five-fold validation compares MAE and R².",
 "ww": "Humans attend more to content words than function words; the proposed H-WWER gives lower scores to human than Whisper transcriptions in the reported comparison and is offered as a dialogue-relevant complement to WER.",
 "limits": "Transcription follows response generation rather than occurring simultaneously, and the displayed weight comparison is partly optimized on test data. The metric is a proposal, not validated against downstream response success or diverse dialogue settings.",
},
"mcallister25b_interspeech": {
 "subtheme": "human-centered-evaluation", "concept": "accessibility-fit",
 "bp": "A child practicing a difficult speech sound needs immediate, interpretable feedback that does not require a specialist or expensive equipment at every trial.",
 "wh": "The learner must connect a changing acoustic spectrum to a vocal-tract target, while remote audio processing can add delay, lose frequency detail, or be distorted by browser processing.",
 "naive": "Show a generic waveform or send audio through a video-call pipeline and expect the child to infer which articulatory change is needed.",
 "ap": "Make the source-filter structure visible: display a real-time LPC spectrum alongside a target resonance, with adaptive practice and clinician-mediated feedback.",
 "mech": "JavaScript computes LPC coefficients with Levinson-Durbin recursion, renders the spectral envelope and peaks, and supports randomized word/syllable routines, clinician scoring, gamification, and local-device WebRTC processing.",
 "math": "LPC models the signal as X(z)=H(z)E(z), with an all-pole vocal-tract filter H(z)=1/A(z); peak locations approximate formant resonances used as the feedback target.",
 "ww": "The staRt iOS/web system provides real-time visual-acoustic biofeedback for /r/ training and reports broad uptake; local processing avoids telepractice loss of frequency resolution and latency.",
 "limits": "The current target is mainly English /r/, peak-picking and formant tracking are not yet stable enough for automated feedback across vocal-tract sizes, and clinical efficacy is not established by this technical description.",
},
"ivucic25_interspeech": {
 "subtheme": "room-channel-and-sensing", "concept": "non-airborne-sensing",
 "bp": "In a real conversation, a listener must switch between speakers while background talkers continue, and a neural interface would need to track the attended stream through those switches.",
 "wh": "EEG responses are weak and delayed relative to acoustic envelopes; multiple speakers and changing attention make a static decoder an unsafe assumption.",
 "naive": "Train one decoder on a fixed attended speaker and assume it remains valid when attention moves.",
 "ap": "Reconstruct each speech envelope from EEG with a time-lagged ridge model and identify the attended speaker by whichever reconstructed envelope correlates best.",
 "mech": "A multivariate linear model maps 62 EEG channels over 0–200 ms lags to speech-envelope samples; leave-one-trial-out validation compares Pearson correlations for target and distractor streams before and after exogenous switches.",
 "math": "The weights minimize squared reconstruction error plus λ||w||². Target selection is an argmax over envelope correlations; chance is 33% for the three-speaker comparison.",
 "ww": "Across 36 trials, target-speaker decoding averages 76% ± 12%; performance remains above chance as windows shrink from 20 seconds to 2 seconds, and reconstruction briefly rises after attention switches.",
 "limits": "The experiment uses controlled speakers and exogenous switches, short windows still perform poorly, EEG signal-to-noise limits real-time use, and neural decoding is not equivalent to robust everyday source separation.",
},
"joubaud25_interspeech": {
 "subtheme": "room-channel-and-sensing", "concept": "microphone-channel",
 "bp": "Body-conduction sensors survive loud environmental noise but remove or reshape spectral information, so an enhancement system must improve speech without changing who is speaking.",
 "wh": "Intelligibility, perceived quality, and speaker identity are different targets; a bandwidth-extension model can improve one while damaging another, and objective metrics may not predict listeners.",
 "naive": "Trust a single objective enhancement score as evidence that a sensor signal is intelligible, natural, and identity-preserving.",
 "ap": "Evaluate EBEN with separate listening tasks for intelligibility, quality, and identity, then correlate each human measure with candidate objective metrics across sensor types and sex.",
 "mech": "Forehead-accelerometer, rigid-in-ear, and throat-microphone signals from Vibravox are enhanced by EBEN; French Modified Rhyme Tests, MUSHRA, and A/B identification are compared with STOI, N-MOS, and ECAPA2 similarity.",
 "math": "Pearson correlation links metric values to listener outcomes; the test uses IQR outlier filtering, Shapiro-Wilk normality checks, and 95% significance thresholds.",
 "ww": "EBEN improves reported quality and intelligibility but slightly harms female throat-microphone identity; STOI correlates strongly with MUSHRA quality (ρ=.87) and ECAPA2 with identification (ρ=.90), while no tested metric reliably predicts intelligibility change.",
 "limits": "The study uses quiet recordings, selected sensors and speakers, one enhancement model, and finite listening tests. Correlation with a perceptual proxy does not establish general clinical or operational usefulness.",
},
"gupta25b_interspeech": {
 "subtheme": "time-frequency-measurement", "concept": "multi-resolution-signal",
 "bp": "Transparent earbuds should reproduce the outside world while keeping processing delay low enough that the user does not hear a mismatch between direct and replayed sound.",
 "wh": "Adaptive filtering must track changing source directions and room paths, but high-order FIR or neural filters cost delay; IIR filters are compact but can become unstable during adaptation.",
 "naive": "Use a fixed filter or a large adaptive FIR and accept poor tracking, computational cost, or latency.",
 "ap": "Adapt a low-order sub-band IIR equalizer and enforce stability with a biquad/all-pass constraint based on the least-mean-square fourth criterion.",
 "mech": "The reference microphone signal is split into sub-bands; feedforward FxLMS/F adaptation updates IIR paths, while cascaded biquads compensate phase/group delay and constrain poles during changing indoor/outdoor conditions.",
 "math": "The filter minimizes an error criterion in sub-bands; the fourth-order LMS constraint penalizes unstable coefficient behavior. MSE, SNR, convergence, and multiply-accumulate counts expose the accuracy/latency/complexity trade-off.",
 "ww": "The paper reports up to 13 dB improvement over compared adaptive methods in simulated scenarios, with stable behavior and similar complexity in dynamic indoor/outdoor tests.",
 "limits": "The evidence is simulation-based and depends on acoustic paths, filter orders, and stability settings; user perception, individualized ears, and end-to-end hardware latency are not established.",
},
"halpern25_interspeech": {
 "subtheme": "metrics-and-targets", "concept": "quality-and-naturalness",
 "bp": "Clinical speech monitoring needs measurements that are repeatable yet still mean what listeners experience as intelligibility, articulation, or voice quality.",
 "wh": "Subjective ratings are expensive and variable, while objective acoustic measures can correlate with a broad severity factor rather than the specific speech dimension they claim to measure.",
 "naive": "Validate one objective metric against one listener rating and treat a high correlation as proof that the metric isolates that percept.",
 "ap": "Measure several perceptual dimensions and objective proxies in longitudinal head-and-neck-cancer speech, then inspect their correlation structure for common-cause confounding.",
 "mech": "Trained listeners rate intelligibility, articulation, voice quality, phonation, rate, nasality, and noise; objective measures such as NAD, PCX, PER, SPEED, and SNR are compared using Pearson correlations across 53 Dutch participants.",
 "math": "The study treats Pearson r as alignment between a computational proxy and a perceptual target, but interprets correlated targets cautiously because shared treatment severity can induce multiple correlations.",
 "ww": "Subjective intelligibility correlates strongly with articulation (r=.95) and voice quality (r=.92); NAD correlates .90 with intelligibility, while phonation and nasality lack reliable objective counterparts in this cohort.",
 "limits": "The population is Dutch readers with head-and-neck cancer, not general speech; neural features are not fully interpretable, running spontaneous speech is absent, and correlation does not prove clinical decision validity.",
},
}

notes = []
claims = []
md = ["# INTERSPEECH 2025 forty-ninth-pass full-paper notes", "", "Eight official-PDF readings deepen grounding/action, human-centered evaluation, room/channel sensing, time-frequency measurement, and metric-target alignment.", ""]
for i, (paper_id, n) in enumerate(N.items(), 1):
    p = papers[paper_id]; c = captured[paper_id]
    note = {"paper_id": paper_id, "title": p["title"], "theme_id": {
        "grounding-and-action": "meaning-and-interaction", "human-centered-evaluation": "people-variation-and-health",
        "room-channel-and-sensing": "sound-and-production", "time-frequency-measurement": "sound-and-production",
        "metrics-and-targets": "evaluation-deployment-and-consequence",
    }[n["subtheme"]], "subtheme_id": n["subtheme"], "concept_id": n["concept"],
        **{k: n[k] for k in ("bp", "wh", "naive", "ap", "mech", "math", "ww", "limits")},
        "eval": n["math"], "dots": {"theme_id": {"grounding-and-action": "meaning-and-interaction", "human-centered-evaluation": "people-variation-and-health", "room-channel-and-sensing": "sound-and-production", "time-frequency-measurement": "sound-and-production", "metrics-and-targets": "evaluation-deployment-and-consequence"}[n["subtheme"]], "subtheme_id": n["subtheme"], "concept_id": n["concept"], "sibling_family": "batch-049"},
        "source": {"kind": "official-isca-archive-paper-page-plus-captured-pdf-text", "pdf_sha256": c["pdf_sha256"], "full_text_sha256": c["full_text_sha256"], "pdf_path": f"data/interspeech-2025-pdfs/{paper_id}.pdf", "text_path": c["full_text_path"]},
        "depth": "D3", "evidence_boundary": "D3 structured analyst note backed by captured PDF/text; result remains author-reported and was not independently reproduced."}
    notes.append(note)
    claims.append({"claim_id": f"IS25-D3C49-{i:02d}", "paper_id": paper_id, "subtheme": n["subtheme"], "claim": n["ww"], "evidence_depth": "D3", "pdf_sha256": c["pdf_sha256"], "full_text_sha256": c["full_text_sha256"], "support_status": "paper-reported-not-independently-verified", "independent_support_status": "not-established", "limitations": n["limits"]})
    md += [f"## {i}. {n['subtheme']}", "", f"**Paper:** [{p['title']}]({p['paper_url']})", f"**Evidence:** D3; PDF SHA-256 `{c['pdf_sha256']}`; full text captured.", ""]
    md += [f"- **{label}:** {note[key]}" for label, key in zip(["Ordinary problem", "Why hard", "Naive attempt", "Central move", "Mechanism", "Mathematical/conceptual structure", "What paper reports", "Limits"], ["bp", "wh", "naive", "ap", "mech", "math", "ww", "limits"])] + [""]

(DATA / "interspeech-2025-fortyninth-d3-notes.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "evidence_depth": "D3", "notes": notes}, indent=2, ensure_ascii=False) + "\n")
(DATA / "interspeech-2025-fortyninth-claim-ledger.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "claim_count": len(claims), "claims": claims}, indent=2, ensure_ascii=False) + "\n")
REPORTS.mkdir(exist_ok=True)
(REPORTS / "INTERSPEECH_2025_FORTYNINTH_D3_NOTES.md").write_text("\n".join(md) + "\n")
print(json.dumps({"notes": len(notes), "claims": len(claims)}))
