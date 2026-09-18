#!/usr/bin/env python3
"""Record a fifth balanced analyst-reviewed INTERSPEECH D2 batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "bakkouche25b_interspeech": ("sound-and-production", "time-frequency-measurement", "windowed-spectrum", "L2 listeners and speakers weight changing spectral cues differently; the paper treats the measured spectrum as evidence whose usefulness depends on experience and task."),
    "berthommier25_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination", "The S-shaped formant trajectory is a physical consequence of coordinated articulator movement, not an arbitrary curve in a feature plot."),
    "birkholz25b_interspeech": ("sound-and-production", "source-filter-production", "vocal-tract-filter", "Wall materials in a physical vocal-tract model alter measured transfer functions, showing that the modeled filter includes radiation and construction choices."),
    "bodur25_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination", "French vowel reduction links shorter or weaker vowel targets to changing articulation dynamics, so fluent speech cannot be modeled as isolated canonical vowels."),
    "chen25l_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering", "Direction and semantic target cues let an ambisonic system extract one sound from a spatial mixture instead of amplifying the entire scene."),
    "das25b_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Dysarthric speech enhancement must improve intelligibility without smoothing away atypical but meaningful speech cues."),
    "dasilva25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "Neural and speech-envelope evidence guide extraction of a target speaker when the mixture itself does not identify which voice matters."),
    "ding25_interspeech": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement", "Linguistic masking in simulated electric-acoustic hearing asks which missing or distorted speech cues matter to a listener, not merely which samples differ."),
    "alderete25_interspeech": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation", "Spontaneous speech errors test whether ASR preserves repairs and atypical forms or silently normalizes them into fluent text."),
    "ariga25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation", "Spoken-word recognition must reconcile segmental evidence with prosodic evidence when the two point toward different lexical interpretations."),
    "bentum25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "Cross-linguistic stress probing tests what a self-supervised representation preserves about prominence rather than assuming learned units have the same linguistic meaning everywhere."),
    "chang25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "A speaker-invariant speech tokenizer tries to discard identity variation while retaining units useful to a spoken-language model."),
    "araizaillan25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Emotion recognition for cochlear-implant users asks which vocal cues remain meaningful when the listener's access to acoustic detail is altered."),
    "baihaqi25b_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "interactional-feedback", "A virtual agent must turn dialogue context into a timed body action; primitive selection makes the response an explicit interactional choice."),
    "charuau25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary", "Hand gestures and pauses provide joint timing evidence for multiparty turns, so a participant's next action cannot be inferred from words alone."),
    "chandra25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning", "Ordinal emotion and natural-language speaking style are related but not identical; ranking them exposes degrees of perceived affect instead of forcing one universal label."),
    "cho25c_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion", "Human-to-non-human voice conversion changes identity and vocal character while attempting to retain a recognizable utterance."),
    "choi25c_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning", "Dual-modality alignment gives diffusion TTS a shared text-and-speech target so linguistic content can guide waveform generation."),
    "francis25_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency", "Augmentative communication needs a voice that can be controlled quickly and personally, so generation quality is constrained by interaction time and user agency."),
    "franzreb25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice", "Private voice conversion tries to change speaker identity without requiring parallel recordings, making privacy and controllable identity part of the conversion problem."),
    "botelho25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Cognitive-impairment detection asks which acoustic and linguistic changes are health-relevant rather than merely differences between speakers."),
    "braun25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Pitfalls in automatic dementia assessment expose how dataset composition and proxy features can make a clinical score look more meaningful than it is."),
    "cao25_interspeech": ("people-variation-and-health", "speaker-characteristics", "age-and-development", "Children from dialect-speaking regions realize tone targets through both development and language background, so age cannot be treated as a nuisance independent of variety."),
    "chowdhury25_interspeech": ("people-variation-and-health", "human-centered-evaluation", "user-control-and-consent", "Reliability of open-source speech features matters because downstream users may treat a convenient tool as a trustworthy measurement instrument."),
    "bafna25_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness", "Language-identification systems can mistake accent for language, revealing that a label may encode listener expectations about a variety rather than the spoken language itself."),
    "bai25_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness", "Accent normalization changes how speech is heard without parallel recordings, forcing a tradeoff between intelligibility, identity, and cultural variation."),
    "damianos25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels", "Unsupervised ASR adaptation uses pseudo-labels and self-supervision when target transcripts are scarce, but must filter errors before they reinforce themselves."),
    "dewhurst25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection", "An open acoustic-nasalance device changes what can be collected about speech, connecting low-cost hardware to new clinical and language resources."),
    "alexos25_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "end-to-end-recovery", "Speech-enabled language systems must be evaluated as an end-to-end interaction because an acoustic request can become a harmful action through later reasoning and tool use."),
    "baser25b_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "spoofing-and-deepfake", "Segment-level manipulation tests whether deepfake realism is judged from linguistic content and phonetic detail rather than one global acoustic score."),
    "broughton25_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "end-to-end-recovery", "End-to-end diarization removes hand-built intermediate labels, making the evaluation sensitive to how speaker boundaries and identities fail together."),
    "chandra25b_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Attack-agnostic fake-speech detection asks whether a detector recognizes the underlying provenance problem instead of memorizing a known manipulation family."),
}

source = json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]
by_id = {p["paper_id"]: p for p in source}
rows = []
for paper_id, assignment in ASSIGNMENTS.items():
    if paper_id not in by_id:
        raise SystemExit(f"missing paper: {paper_id}")
    paper = by_id[paper_id]
    abstract = paper.get("abstract", "")
    rows.append({
        "paper_id": paper_id, "title": paper["title"], "decision": "supported",
        "confidence": "analyst-reviewed-D2", "theme_id": assignment[0],
        "subtheme_id": assignment[1], "concept_id": assignment[2],
        "semantic_reasoning": assignment[3],
        "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "eval", "ww", "limits"],
        "evidence_excerpt": abstract[:1200], "source_location": paper["paper_url"],
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": "D2", "review_state": "analyst-reviewed",
        "claim_boundary": "Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed.",
    })
payload = {
    "schema_version": 1,
    "batch_id": "interspeech-2025-semantic-d2-batch-004",
    "status": "analyst-reviewed-D2-batch",
    "claim_boundary": "These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-004.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D2": len(rows)}))
