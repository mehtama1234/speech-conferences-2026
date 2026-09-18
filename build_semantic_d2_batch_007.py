#!/usr/bin/env python3
"""Record a seventh balanced analyst-reviewed INTERSPEECH D2 batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

A = {
    "franz25_interspeech": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture", "Room acoustics change the signal used for objective voice assessment, so a vocal measure may reflect the room as well as the speaker."),
    "fucci25_interspeech": ("sound-and-production", "time-frequency-measurement", "windowed-spectrum", "Feature attribution for ASR asks which acoustic regions actually support a recognized phonetic decision instead of treating every input feature as equally meaningful."),
    "gogoi25_interspeech": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal", "AM and FM rhythm spectrograms represent slow and fast changes in speech, testing whether dementia-related information lives in the rhythm structure rather than one static spectrum."),
    "grinberg25_interspeech": ("sound-and-production", "time-frequency-measurement", "windowed-spectrum", "Explanations for audio deepfake detection ask which measurable signal changes distinguish generated audio from genuine speech."),
    "goswami25_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Universal speech enhancement must remove varied interference without assuming one fixed noise type, so the central pressure is preserving speech while the nuisance changes."),
    "guzik25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering", "Beamforming in a spatially aliased array asks how to recover a useful direction when microphone spacing makes the spatial measurements ambiguous."),
    "han25b_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Generative speech enhancement fills in a clean-sounding signal from noisy evidence, creating a direct tradeoff between intelligibility and fidelity."),
    "han25d_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "In-car separation uses room responses and spatial cues to preserve speech in a moving vehicle while suppressing competing sound."),
    "cm25_interspeech": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing", "Loudspeaker-emitted speech tests whether ASR mistakes playback and acoustic feedback for a person speaking directly to the system."),
    "coppietersdegibson25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "Auditory feedback mechanisms ask how a listener's own speech recognition system uses expected sound to interpret the incoming signal."),
    "ducorroy25_interspeech": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "speaker-adaptation", "Disordered speech requires adapting recognition models to atypical pronunciation and motor patterns without treating the disorder as random noise."),
    "elkheir25b_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation", "Arabic pronunciation assessment needs a reference that respects recitation and variety-specific pronunciation instead of measuring every deviation against one narrow norm."),
    "feng25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Naturalistic emotion recognition must identify affective meaning when speakers and situations vary, rather than relying on acted, isolated labels."),
    "fujita25b_interspeech": ("meaning-and-interaction", "grounding-and-action", "referential-grounding", "Dialogue continuation asks whether an audio-language model can use the current exchange to choose a meaningful next turn instead of producing a locally fluent sentence."),
    "fukunaga25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary", "Backchannel prediction models when a listener should respond, treating conversation as coordinated timing rather than a sequence of independent utterances."),
    "gogoi25b_interspeech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning", "Tone recognition in a low-resource language asks whether learned representations preserve language-specific pitch meaning instead of importing categories from better-resourced languages."),
    "hirano25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "speaker-identity", "Diarization-guided overlap handling conditions the decoder on who is speaking so generated or selected speech preserves speaker identity in a mixture."),
    "hope25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "speaker-identity", "AI voices used for nonbinary gender expression raise the question of whether generated voice identity can be controlled without collapsing a person's expression into a fixed binary label."),
    "horiguchi25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "speaker-identity", "Guided speaker embeddings must target the intended voice without letting non-target speakers in the mixture bias the identity representation."),
    "hou25b_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency", "A voice-assistant benchmark tests conversation ability as an interaction over turns, not just isolated speech recognition or response quality."),
    "gao25b_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "A longitudinal public-figure corpus asks whether speech changes over time can support early Alzheimer detection while separating health signals from topic and recording changes."),
    "gao25e_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Suicide-risk detection from spontaneous speech must distinguish clinically relevant patterns from what a person happens to discuss or how the recording was made."),
    "gimenogomez25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Parkinson detection depends on whether an automatic task measures a meaningful clinical ability rather than a convenient but unrelated speech correlate."),
    "gohider25_interspeech": ("people-variation-and-health", "human-centered-evaluation", "accessibility-fit", "Inclusive ASR for disordered speech asks whether improvement is shared across speakers instead of optimizing an average that hides people with the greatest impairment."),
    "do25b_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "cultural-meaning", "Toxic-span detection in Vietnamese speech must identify harmful meaning in a particular language rather than assume that an English-trained boundary transfers directly."),
    "fort25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation", "Computer-assisted pronunciation training for isiZulu tests whether a pretrained speech model can provide useful feedback when labeled language-specific data are scarce."),
    "funfgeld25_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "cultural-meaning", "Irony perception depends on prosodic and cultural expectations, so the same words cannot be treated as having one fixed intention across speakers."),
    "fong25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection", "Low-resource speech language models ask how much data is needed before a model learns a language's structure rather than memorizing a small set of examples."),
    "choi25f_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use", "Audio caption retrieval needs evaluation of whether a generated query finds the right evidence, not only whether its wording sounds fluent."),
    "cumlin25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness", "Speech quality assessment combines several uncertain measures, asking how to represent perceived quality without pretending one score is the whole listening experience."),
    "das25_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Generalizable spoof detection must recognize manipulation across attacks it has not seen, separating evidence of fakery from a memorized generator signature."),
    "deoliveira25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness", "Non-intrusive quality assessment predicts degradation from the received signal alone, so the central question is whether a quality judgment can be made without the clean reference."),
}

source = json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]
by_id = {p["paper_id"]: p for p in source}
rows = []
for paper_id, (theme, subtheme, concept, reasoning) in A.items():
    paper = by_id[paper_id]
    abstract = paper.get("abstract", "")
    rows.append({
        "paper_id": paper_id, "title": paper["title"], "decision": "supported",
        "confidence": "analyst-reviewed-D2", "theme_id": theme, "subtheme_id": subtheme,
        "concept_id": concept, "semantic_reasoning": reasoning,
        "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "eval", "ww", "limits"],
        "evidence_excerpt": abstract[:1200], "source_location": paper["paper_url"],
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": "D2",
        "review_state": "analyst-reviewed",
        "claim_boundary": "Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed.",
    })
payload = {
    "schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-007",
    "status": "analyst-reviewed-D2-batch",
    "claim_boundary": "These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-007.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D2": len(rows)}))
