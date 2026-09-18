#!/usr/bin/env python3
"""Record a curated D2 semantic-adjudication batch from official abstracts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

# Four non-D3 papers per conceptual theme. Each assignment was selected from
# the title and abstract, with the rationale stating the problem/mechanism
# distinction being used. It is not promoted to D3 without PDF review.
ASSIGNMENTS = {
    "ankita25_interspeech": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal", "The abstract ties children's recognition to limited data and acoustic features; this is a measurement/variation problem, not evidence of a new physical production model."),
    "arai25_interspeech": ("sound-and-production", "source-filter-production", "vocal-tract-filter", "The paper models vocal-tract geometry for a speaking machine, directly connecting physical shape to the produced sound."),
    "bandekar25_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination", "Acoustic-to-articulatory inversion asks which coordinated movements could have produced the observed speech, with low-resource learning as a boundary."),
    "bao25_interspeech": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal", "The frequency-domain bandwidth-extension method reconstructs missing high-frequency evidence; its core issue is what a representation preserves across scales."),
    "alizadeh25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation", "Recursive separation is proposed because the number of concurrent speakers is unknown; the assignment is about recovering sources from a mixture."),
    "b25_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "The paper reduces non-stationary noise with a structured codebook, trading compact computation against faithful speech recovery."),
    "behera25_interspeech": ("listening-and-separation", "noise-enhancement", "nonstationary-noise", "Test-time training responds to noise and domain conditions that change after deployment, rather than assuming a fixed noise distribution."),
    "bashir25_interspeech": ("listening-and-separation", "noise-enhancement", "perceptual-enhancement", "The paper predicts intelligibility after time modification using spectro-temporal cues, making listener understanding the target rather than waveform similarity alone."),
    "ahadzi25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "Online children's ASR must learn new speech without erasing earlier knowledge; the assignment concerns mapping changing acoustics to words under continual updates."),
    "ahn25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "The model regularizes learned speech representations so clean/noisy acoustics retain useful structure for recognition; the abstract does not establish all unit behavior."),
    "altwlkany25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "channel-microphone", "The study examines how codecs and channel changes interact with language and gender patterns, making the recording path part of recognition evidence."),
    "attia25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "Noisy classroom transcripts provide weak supervision; the central move is learning word mappings while separating unreliable labels from a small accurate set."),
    "baihaqi25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary", "Proactive behavior, personalization, and backchannels are timing choices that determine whether a dialogue partner yields, continues, or repairs."),
    "bokkahallisatish25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "intent-in-context", "The interactive platform evaluates conversational speech-to-speech systems for bias and user experience, connecting affective interpretation to human judgment."),
    "cavalcanti25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary", "The paper studies how speaker and demographic differences affect turn-taking timing, rather than treating pauses as universal turn boundaries."),
    "chen25g_interspeech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning", "Prosodic patterns in rhetorical questions add communicative meaning beyond the words, so pitch and timing are evidence about intent."),
    "ali25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "spoofing-and-deepfake", "A curated public-figure deepfake dataset treats voice identity as a security and consent problem, not simply a synthesis-quality benchmark."),
    "alradhi25_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "The system reconstructs speech from neural signals and predicts prosody, separating intended linguistic content from the details needed for audible output."),
    "berger25_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning", "Non-standard accent TTS must transfer pronunciation knowledge without forcing the speaker into a majority accent norm."),
    "chen25b_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "Human feedback is used to tune diffusion TTS toward preferred outputs, making the listener's judgment part of the generation target."),
    "baumann25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech", "Pathology-aware encoding and augmentation treat dysarthric articulation as structured variation that must be represented, not discarded as noise."),
    "choi25h_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "The comparison of acoustic feature tools asks whether a measured speech property is stable enough for clinical analysis, not whether it diagnoses by itself."),
    "dindart25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Ultrasound observes vocal-fold vibration directly, offering a physical health-related signal that differs from airborne acoustic proxies."),
    "dumpala25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Depression detection from speech tests whether a voice pattern correlates with a clinical state, with confounding by speaker and context as a central boundary."),
    "alam25_interspeech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching", "Everyday multilingual spoken queries test whether a language model handles language choice and meaning together instead of translating an artificial sentence list."),
    "alumae25_interspeech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "The challenge system shares recognition and language-identification structure across languages, with unequal data and task coverage as the key limit."),
    "bhattacharya25_interspeech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching", "The study relates code-switching to language proficiency and conversation, treating a switch as communicative behavior rather than an error label."),
    "blaschke25_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety", "A multi-dialect dataset makes German variety differences part of the recognition and translation target instead of normalizing them away."),
    "ahmed25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "listener-effort", "Visual cues are added to non-intrusive speech-quality assessment because a no-reference score must predict what listeners understand without a clean signal."),
    "ahn25b_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness", "Optimizing an automated audio-captioning reward raises the question of whether a metric rewards semantic coverage or merely reference style."),
    "bhattacharya25b_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use", "Confidence evaluation tests whether a spoken temporal-reasoning system knows when its answer is uncertain, not only whether its average score is high."),
    "bolanos25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness", "Time-localized explanations are evaluated as evidence about why an audio classifier decided, so explanation quality must be measured separately from classification accuracy."),
}


def main() -> None:
    papers = {row["paper_id"]: row for row in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
    rows = []
    for paper_id, (theme, subtheme, concept, rationale) in ASSIGNMENTS.items():
        paper = papers[paper_id]
        abstract = paper.get("abstract") or ""
        rows.append({
            "paper_id": paper_id,
            "title": paper["title"],
            "decision": "supported",
            "confidence": "analyst-reviewed-D2",
            "theme_id": theme,
            "subtheme_id": subtheme,
            "concept_id": concept,
            "semantic_reasoning": rationale,
            "evidence_excerpt": abstract[:900],
            "source_location": paper["paper_url"],
            "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
            "evidence_depth": "D2",
            "review_state": "analyst-reviewed",
            "claim_boundary": "Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed.",
        })
    payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-001", "status": "analyst-reviewed-d2-seed-batch", "claim_boundary": "These 32 assignments are analyst-reviewed from official abstracts. They do not establish full-paper mechanism or venue-wide prevalence.", "reviewed_count": len(rows), "rows": rows}
    (DATA / "interspeech-2025-semantic-reviewed-d2-batch-001.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows)}))


if __name__ == "__main__":
    main()
