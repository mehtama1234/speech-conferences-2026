#!/usr/bin/env python3
"""Record the first full-paper semantic review batch.

These decisions are anchored in the existing D3 notes and captured PDF/text
artifacts.  They are deliberately a small, auditable seed batch, not a claim
that the 1,179-paper queue is complete.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "azzouz25_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination", "The paper infers coordinated vocal-tract movement from acoustic evidence; it is about the physical source/filter relationship, not ordinary word recognition."),
    "aboeitta25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "The central comparison is how acoustic encoders and language-aware decoders map dysarthric speech to words; the clinical population is an important boundary, not the main mechanism."),
    "aggarwal25_interspeech": ("meaning-and-interaction", "grounding-and-action", "intent-in-context", "The study tests whether language models use context and domain knowledge to interpret spoken questions; it concerns intended meaning rather than waveform recovery."),
    "akti25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion", "The model separates multilingual content units from expressive voice controls so a new speaker/style can be produced without changing the requested content."),
    "alcalapadilla25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering", "The target is selected using direction of arrival for a hearing-aid microphone array; the decisive cue is spatial structure, not generic denoising."),
    "ai25_interspeech": ("people-variation-and-health", "identity-and-life-stage", "age-and-development", "The longitudinal recordings ask how speaker verification changes as a person ages; aging is the phenomenon being measured, not voice conversion."),
    "amoniyan25_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety", "The paper measures /s/ variation across a multilingual Nigerian population and treats ethnicity, age, gender, and phonological context as boundaries on interpretation."),
    "lemaguer25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness", "The contribution is a reproducible perceptual-evaluation procedure; it belongs to the problem of what a listener score establishes and how to report it."),
    "ashihara25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "The paper studies what discrete audio tokens preserve and how token predictability changes across domains; it is a representation question, not a claim of universal semantic units."),
    "agrawal25b_interspeech": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing", "The method finds bias phrases in cross-attention and merges them with ASR output, using task context to resolve otherwise difficult terms."),
    "agrawal25_interspeech": ("meaning-and-interaction", "grounding-and-action", "intent-in-context", "The paper probes whether speech-language models rely on label semantics and context when answering tasks; the conceptual issue is intended task meaning, not only transcription."),
    "abdullah25_interspeech": ("languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness", "Voice conversion is used as augmentation, but the paper's evaluated object is cross-domain dialect identification; the current question is whether dialect evidence survives changes in speaker realization."),
    "alip25_interspeech": ("listening-and-separation", "noise-enhancement", "spectral-mask", "The three-stage system estimates acoustic structure, reduces full-band noise, and refines the spectrum; its boundary is enhancement quality versus faithful speech recovery."),
    "akinrintoyo25_interspeech": ("recognition-and-alignment", "boundaries-and-sequence-structure", "disfluency-preservation", "The explicit filler-inclusion analysis makes preservation of disfluencies part of the target rather than treating them as transcription noise; the dementia population is the evaluation boundary."),
    "biswas25_interspeech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching", "The method combines language prompts and code-mixed augmentation, so the core problem is switching language systems within speech rather than generic multilingual scaling."),
    "giraldo25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "listener-effort", "The paper compares enhancement on multilingual crowdsourced speech and measures content retention and information loss across people; the evaluation target is human-useful recovery, not only a signal score."),
    "a25_interspeech": ("sound-and-production", "source-filter-production", "vocal-tract-filter", "The paper models a dual avian sound source and upper vocal tract to explain how physical geometry produces biphonic spectral structure."),
    "alabi25_interspeech": ("languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer", "The paper's central object is a shared multilingual speech representation across African languages; scarce labels motivate the work but are not its main mechanism."),
    "arora25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state", "The paper adds intermediate reasoning supervision to an end-to-end spoken dialogue system, making conversational state part of the response decision."),
    "bakkouche25_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "The paper separates listener judgments of clone naturalness and target similarity and studies prosodic variation as a reason they diverge."),
    "avidan25_interspeech": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation", "The paper addresses multichannel separation when the number of simultaneous speakers is not fixed, using mixture structure rather than a known source count."),
    "asali25_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "The SASV system combines claimed-speaker evidence with anti-spoofing evidence because a voice match alone does not establish an authentic speaker."),
    "ambikairajah25_interspeech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "The paper studies whether learned speech geometry relates Australian Aboriginal languages to high-resource languages, while testing the limits of interpreting similarity as transfer."),
    "balasubramanian25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness", "The paper predicts subjective audio-quality judgments for real-time use, directly addressing the gap between a cheap proxy and what listeners actually report."),
}


def main() -> None:
    note_files = [DATA / "interspeech-2025-d3-notes.json", DATA / "interspeech-2025-second-d3-notes.json", DATA / "interspeech-2025-third-d3-notes.json"]
    notes = {}
    for path in note_files:
        for row in json.loads(path.read_text())["notes"]:
            notes[row["paper_id"]] = row
    reviewed = []
    for paper_id, assignment in ASSIGNMENTS.items():
        note = notes[paper_id]
        text_path = DATA / "interspeech-2025-text" / f"{paper_id}.txt"
        reviewed.append({
            "paper_id": paper_id,
            "title": note.get("title", paper_id),
            "decision": "supported",
            "confidence": "analyst-reviewed-D3",
            "theme_id": assignment[0],
            "subtheme_id": assignment[1],
            "concept_id": assignment[2],
            "semantic_reasoning": assignment[3],
            "evidence_fields": ["bp", "wh", "naive", "ap", "mech", "math", "ww", "limits"],
            "evidence_excerpt": "Problem: " + note["bp"] + " Mechanism: " + note["mech"] + " Reported result: " + note["ww"] + " Boundary: " + note["limits"],
            "source_location": str(text_path.relative_to(HERE)),
            "source_sha256": hashlib.sha256(text_path.read_bytes()).hexdigest(),
            "evidence_depth": "D3",
            "review_state": "analyst-reviewed",
        })
    payload = {
        "schema_version": 1,
        "batch_id": "interspeech-2025-semantic-d3-batch-001",
        "status": "analyst-reviewed-seed-batch",
        "claim_boundary": "These 24 assignments are full-paper analyst judgments anchored in captured D3 notes and text. They do not close the whole-corpus queue.",
        "reviewed_count": len(reviewed),
        "rows": reviewed,
    }
    (DATA / "interspeech-2025-semantic-reviewed-batch-001.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(reviewed)}))


if __name__ == "__main__":
    main()
