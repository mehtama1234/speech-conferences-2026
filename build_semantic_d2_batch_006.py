#!/usr/bin/env python3
"""Record a sixth balanced analyst-reviewed INTERSPEECH D2 batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

A = {
    "chen25c_interspeech": ("sound-and-production", "source-filter-production", "voice-quality", "Emotional speech from people with borderline personality features tests how voice quality and listener response interact rather than treating emotion as words alone."),
    "dong25e_interspeech": ("sound-and-production", "time-frequency-measurement", "spectral-shape", "Respiratory-sound classification asks which changing frequency patterns carry evidence of a medical condition."),
    "du25c_interspeech": ("sound-and-production", "source-filter-production", "source-dynamics", "Adductor spasmodic dysphonia changes the physical source of speech; the paper tests whether learned acoustic patterns can expose that change."),
    "duraisamy25_interspeech": ("sound-and-production", "time-frequency-measurement", "temporal-dynamics", "Covert-speech EEG varies over time and across people, so the analysis asks whether hidden articulation leaves a measurable temporal signature."),
    "fan25_interspeech": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal", "Infant-centered audio contains events at different time scales; a band-split model tests whether separating those scales preserves useful sound evidence."),
    "fan25b_interspeech": ("sound-and-production", "source-filter-production", "prosodic-production", "Creaky voice changes how Mandarin tone is produced and heard, linking a voice-quality cue to phonological processing."),
    "fernandez25_interspeech": ("sound-and-production", "echo-and-reconstruction", "spectrogram-inversion", "Spectrogram inversion asks what information is lost when a time-frequency picture is turned back into a waveform, and which numerical or learned assumptions fill the gap."),
    "fischbach25_interspeech": ("sound-and-production", "room-channel-and-sensing", "channel-variation", "Voice conversion is used to vary speakers and dialect conditions, testing whether a classifier learns dialect evidence or the recording and speaker mix."),
    "arisoy25_interspeech": ("listening-and-separation", "echo-and-reconstruction", "synthetic-data", "Low-resource speech generation asks whether artificial examples teach a recognizer the missing variation or merely repeat the generator's assumptions."),
    "biswas25b_interspeech": ("listening-and-separation", "noise-enhancement", "efficient-enhancement", "Quantized distillation tests how much speech-understanding quality survives when an audio-language system is made smaller and cheaper."),
    "chan25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "cue-weighting", "Multilingual stop voicing provides a controlled case where listeners and speakers must weight competing acoustic timing cues differently."),
    "dinh25_interspeech": ("listening-and-separation", "echo-and-reconstruction", "long-context-recovery", "Short audio windows can hide long-range context; the paper asks whether adding broader context restores information needed for the decision."),
    "elkheir25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "spectro-temporal-separation", "Deepfake detection must separate artifact patterns from ordinary speech variation across time and frequency."),
    "escobargrisales25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "clinical-signal-separation", "Parkinsonian speech contains acoustic and linguistic changes together; synchronized analysis asks which signal belongs to which kind of impairment."),
    "espywilson25_interspeech": ("listening-and-separation", "echo-and-reconstruction", "articulatory-inference", "Acoustic recordings are used to infer speech movement, testing how much physical articulation can be recovered from an indirect signal."),
    "fathan25b_interspeech": ("listening-and-separation", "noise-enhancement", "label-noise", "Automatic correction of noisy labels treats training annotations as a source of contamination that must be separated from genuine speech patterns."),
    "barahona25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "speaker-role", "A speaker-recognition evaluation exposes how front-end choices affect identity judgments before a downstream system ever sees the speech."),
    "bn25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "claim-grounding", "Hallucination diagnosis asks whether a model's answer is supported by the source rather than merely fluent, making evidence and intended meaning the central issue."),
    "chen25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "speaker-variation", "Robust speaker recognition tests whether identity survives intrinsic changes in a person's voice instead of being confused with a fixed acoustic profile."),
    "cho25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "emotion-representation", "A spherical representation for emotion recognition tests whether affective states are better organized by relative relationships than by independent class boundaries."),
    "dutta25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "naturalistic-emotion", "Emotion recognition in natural settings asks whether affective meaning survives changes in context, speakers, and recording conditions."),
    "fang25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "multitask-memory", "Parameter-efficient multimodal tuning asks which shared and task-specific information can be retained when one model must handle several affective judgments."),
    "christodoulidou25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "child-speech-segmentation", "Transcribing and segmenting child speech requires interaction-aware boundaries because pauses, turn changes, and immature articulation do not follow adult assumptions."),
    "eom25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "temporal-alignment", "Monotonic alignment tests whether speech representations can preserve the order between an acoustic event and the label or content it expresses."),
    "falez25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "deepfake-provenance", "Open-set deepfake tracing asks whether a system can identify an unfamiliar generating source rather than only recognize examples seen during training."),
    "firc25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "deepfake-variation", "A systematic deepfake corpus varies how synthetic speech is made, making it possible to separate generator-specific artifacts from general evidence of manipulation."),
    "geng25b_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "brain-to-voice", "EEG-based voice conversion asks whether neural activity can control the identity or content of a generated voice without an ordinary microphone signal."),
    "glazer25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "few-shot-adaptation", "Few-shot deepfake detection tests whether a detector can adapt to a new attack from very little evidence without mistaking speaker or channel variation for fakery."),
    "gogate25_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "personalized-enhancement", "Personalized audio-visual enhancement asks whether a system can preserve the intended speaker while suppressing competing sound and visual uncertainty."),
    "gourav25_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "multilingual-generation", "Code-mixed text-to-speech must generate one coherent voice while switching languages, exposing the tension between linguistic content and stable vocal identity."),
    "guo25_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "speaker-content-disentanglement", "A low-bitrate codec tries to keep what was said separate from who said it, so rate reduction does not destroy controllable speaker identity."),
    "hasumi25_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "nonverbal-generation", "A cinematic nonverbal-sound corpus broadens generation beyond words and asks what data are needed to model meaningful vocal and environmental events."),
}

source = json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]
by_id = {p["paper_id"]: p for p in source}
rows = []
for paper_id, (theme, subtheme, concept, reasoning) in A.items():
    paper = by_id[paper_id]
    abstract = paper.get("abstract", "")
    rows.append({
        "paper_id": paper_id,
        "title": paper["title"],
        "decision": "supported",
        "confidence": "analyst-reviewed-D2",
        "theme_id": theme,
        "subtheme_id": subtheme,
        "concept_id": concept,
        "semantic_reasoning": reasoning,
        "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "eval", "ww", "limits"],
        "evidence_excerpt": abstract[:1200],
        "source_location": paper["paper_url"],
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": "D2",
        "review_state": "analyst-reviewed",
        "claim_boundary": "Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed.",
    })

payload = {
    "schema_version": 1,
    "batch_id": "interspeech-2025-semantic-d2-batch-006",
    "status": "analyst-reviewed-D2-batch",
    "claim_boundary": "These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.",
    "reviewed_count": len(rows),
    "rows": rows,
}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-006.json").write_text(
    json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
)
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D2": len(rows)}))

