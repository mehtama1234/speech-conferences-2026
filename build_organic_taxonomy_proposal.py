#!/usr/bin/env python3
"""Derive a variable subtheme proposal from first-principles boundaries.

This is intentionally a proposal, not an automatic replacement for the
canonical taxonomy.  Existing concept assignments supply evidence counts; the
proposal changes a subtheme only when the ordinary pressure, failure, or
evaluation target changes.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent; DATA=ROOT/"data"; REPORTS=ROOT/"reports"

P=[
 {"theme_id":"sound-and-production","theme":"Sound, bodies, rooms, and recording","reason":"The corpus separates the act of making sound from the act of measuring a changing signal and from the channel that carries it.","subthemes":[
  ("source-generation","Making a physical sound",["periodic-source","vocal-tract-filter"],"The source and tract shape the pressure wave before a device records it."),
  ("articulatory-dynamics","Coordinating moving speech parts",["articulatory-coordination"],"Gesture overlap and timing are the object; a static source/filter description is not enough."),
  ("time-frequency-measurement","Representing a changing signal",["windowed-spectrum","multi-resolution-signal","sampling-and-quantization"],"The question is what a digital representation keeps or loses across time, frequency, and precision."),
  ("room-channel-and-sensing","Changing the path from source to sensor",["reverberant-mixture","microphone-channel","non-airborne-sensing"],"Room reflections, device coloration, and alternate sensors change the evidence before recognition."),
 ]},
 {"theme_id":"listening-and-separation","theme":"Listening through noise, overlap, and missing sound","reason":"The papers distinguish suppressing nuisance, recovering a chosen source, using space to choose it, and repairing information that is absent or perceptually damaged.","subthemes":[
  ("noise-enhancement","Suppressing changing interference",["spectral-mask","speech-prior-denoising","nonstationary-noise"],"The target is one speech stream and the failure is removing speech along with noise."),
  ("source-separation","Recovering several hidden sources",["blind-source-separation","target-conditioned-separation"],"The mixture contains multiple sources and the system must infer source identity or count."),
  ("spatial-listening","Using location to select sound",["spatial-filtering"],"Microphone geometry and direction are the evidence; a single-channel separator has a different limit."),
  ("echo-reconstruction","Canceling copies and filling gaps",["acoustic-echo-cancellation","packet-loss-concealment"],"The unwanted signal is a known delayed copy or missing frame, not an arbitrary background."),
  ("perceptual-recovery","Optimizing what a listener can use",["perceptual-enhancement"],"This boundary is for methods whose target is what a listener can understand or tolerate; it is separate from noise removal, separation, and packet repair, which target a signal or source before the listener judges it."),
 ]},
 {"theme_id":"recognition-and-alignment","theme":"From sound to words and structured speech","reason":"Recognition papers separate learning sound units, handling pronunciation variation, locating sequence boundaries, and using context to resolve open vocabulary.","subthemes":[
  ("acoustic-unit-learning","Learning reusable sound units",["acoustic-to-token","self-supervised-speech-units"],"The system first decides what reusable evidence can be extracted from continuous sound."),
  ("pronunciation-and-variation","Allowing different realizations of words",["pronunciation-variation"],"The same intended unit has multiple acoustic paths; this is distinct from learning a unit representation."),
  ("boundaries-and-alignment","Locating units in time",["alignment","disfluency-preservation"],"The output must preserve or locate timing, hesitation, repair, or sequence boundaries."),
  ("context-and-open-vocabulary","Using context without inventing words",["long-context-decoding","domain-and-context-biasing","speaker-adaptation","open-vocabulary-recognition"],"Context, speaker evidence, and new words resolve ambiguity but can override what was actually said."),
 ]},
 {"theme_id":"meaning-and-interaction","theme":"From spoken form to meaning and coordinated action","reason":"The corpus distinguishes information carried by voice, state carried across turns, timing of participation, and grounding language in people or actions.","subthemes":[
  ("prosody-and-paralinguistics","Meaning carried by how speech sounds",["prosodic-meaning","paralinguistic-state"],"This boundary covers information carried by pitch, timing, loudness, voice quality, or effort beyond the words; it is separate from dialogue action because the cue is in how an utterance sounds, not in the conversational state alone."),
  ("intent-and-dialogue-state","Inferring what a speaker is trying to do",["intent-in-context","dialogue-state"],"The system tracks goals, commitments, and situation rather than only classifying acoustic style."),
  ("turn-taking-and-repair","Coordinating participation under uncertainty",["turn-boundary","repair-and-clarification"],"The problem is when to speak, yield, interrupt, or ask for clarification."),
  ("grounding-and-action","Connecting language to a shared world",["referential-grounding","speech-act","interactional-feedback"],"A phrase must identify a referent or authorized action and remain corrigible through feedback."),
 ]},
 {"theme_id":"voice-generation-and-control","theme":"Creating speech while keeping the right things fixed","reason":"Generation papers separate planning content, producing fine waveform detail, changing identity, and controlling expression or interaction.","subthemes":[
  ("content-planning","Turning language into a timed speech plan",["text-to-speech-planning"],"This boundary covers the step from intended text or meaning to pronunciation, duration, pitch targets, and sequence; it is separate from waveform generation, which realizes an already chosen plan as samples."),
  ("waveform-and-codec-generation","Producing or compressing audible detail",["neural-vocoder","intelligibility-naturalness"],"The issue is sample-level detail and the tradeoff between faithful content and natural sound."),
  ("identity-and-conversion","Changing who sounds like the speaker",["speaker-identity","voice-conversion","zero-shot-voice"],"This boundary covers changing or measuring who the voice sounds like while keeping the message stable; it is separate from expression control, which changes emotion or style, and from content planning, which changes the speech plan."),
  ("expression-and-interactive-control","Changing style, timing, and response behavior",["prosody-control","style-and-emotion-control","interactive-latency"],"The system must obey expressive controls quickly without breaking continuity or meaning."),
 ]},
 {"theme_id":"people-variation-and-health","theme":"Speakers as changing people, not nuisance variables","reason":"The papers separate identity and within-person change, clinical measurement, atypical/assistive communication, and whether a system fits a person's real life.","subthemes":[
  ("identity-and-life-stage","Identity, age, and changing voice",["speaker-verification","age-and-development","style-and-state-variation"],"The evidence concerns who is speaking and how that person's voice changes across time and state."),
  ("clinical-markers","Speech measurements associated with health",["clinical-speech-marker"],"A measurable speech property is evaluated as a possible health signal, with clinical limits kept explicit."),
  ("atypical-and-assistive-speech","Communicating with atypical or impaired speech",["dysarthria-and-atypical-speech","augmentative-communication"],"The goal is recognition or expression for people whose speech does not match majority training data."),
  ("human-centered-accessibility","Whether the system actually helps a person",["listener-effort","user-control-and-consent","accessibility-fit"],"The target is effort, control, access, and fit in a real activity rather than model accuracy alone."),
 ]},
 {"theme_id":"languages-accents-and-resources","theme":"Many languages, accents, and unequal evidence","reason":"The papers distinguish sharing structure across languages, learning with little data, creating missing evidence, and interpreting varieties without treating them as errors.","subthemes":[
  ("crosslingual-structure","Sharing structure across languages",["crosslingual-transfer","language-identification","code-switching"],"The central question is what can be shared while retaining language-specific distinctions."),
  ("low-resource-learning","Learning from sparse labels",["self-training-and-pseudo-labels","few-shot-adaptation"],"The method changes how a model learns when labeled examples are scarce."),
  ("data-creation","Making missing speech evidence",["speech-data-collection"],"The work creates speakers, prompts, labels, or recordings needed by a community or task."),
  ("accent-dialect-and-cultural-meaning","Respecting variation and local meaning",["accent-robustness","dialect-and-variety","cultural-meaning"],"This boundary covers differences in pronunciation, variety, and local meaning that affect who is understood and how speech is interpreted; it is separate from generic low-resource learning because more data alone cannot decide whether a social or cultural distinction was represented correctly."),
 ]},
 {"theme_id":"evaluation-deployment-and-consequence","theme":"Evidence, practical systems, and consequences","reason":"The corpus separates what a score stands for, what changes outside the test set, what a device can afford, and what voice technology can expose or harm.","subthemes":[
  ("metric-and-human-targets","Connecting scores to human goals",["word-error-versus-understanding","quality-and-naturalness","calibration-and-selective-use"],"A metric is a proxy and must be tied to the human or engineering property it represents."),
  ("robustness-and-shift","Changing speakers, rooms, and conditions",["distribution-shift","end-to-end-recovery"],"The question is whether failures are detected and recovered when conditions differ from training."),
  ("deployment-cost","Meeting time, memory, and hardware limits",["latency-and-resource"],"The system must operate within a device or interaction budget without hiding cost elsewhere."),
  ("privacy-and-security","Protecting voice and resisting misuse",["voice-privacy","spoofing-and-deepfake"],"This boundary covers harm from exposing voice identity or accepting imitation, replay, or generated speech as genuine; it is separate from ordinary robustness because the failure is unauthorized inference or deception, not merely a lower score in a changed condition."),
  ("auditability-and-accountability","Keeping claims inspectable and contestable",["auditability-and-contestability"],"A person must be able to trace evidence, uncertainty, and correction when a speech system matters."),
 ]},
]

def main():
    taxonomy=json.loads((DATA/"speech-first-principles-taxonomy.json").read_text())
    queue=json.loads((DATA/"interspeech-2025-semantic-review-queue.json").read_text())
    old_to_count={}
    for row in queue["rows"]:
        review=row.get("analyst_review",{})
        if row.get("decision")=="supported":
            old_to_count[review.get("concept_id")]=old_to_count.get(review.get("concept_id"),0)+1
    old_concepts={c["id"] for t in taxonomy["themes"] for s in t["subthemes"] for c in s["concepts"]}
    records=[]
    for theme in P:
        subs=[]
        for sid,name,concepts,boundary in theme["subthemes"]:
            subs.append({"id":sid,"name":name,"supporting_current_concepts":concepts,"supported_paper_count":sum(old_to_count.get(c,0) for c in concepts),"boundary":boundary,"derivation":"Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups."})
        records.append({"theme_id":theme["theme_id"],"theme":theme["theme"],"derivation_reason":theme["reason"],"subtheme_count":len(subs),"subthemes":subs})
    payload={"status":"proposal-not-canonical","method":"baseline first-principles pressure -> failed simple solution -> recurring paper move -> boundary test","fixed_cardinality_detected":all(len(t["subthemes"])==3 for t in taxonomy["themes"]),"canonical_concept_count":len(old_concepts),"proposed_theme_count":len(records),"proposed_subtheme_count":sum(r["subtheme_count"] for r in records),"records":records,"decision_rule":"Do not merge or split solely to equalize counts; reassign papers only after each boundary has named evidence."}
    (DATA/"speech-organic-taxonomy-proposal.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
    md=["# Organic taxonomy proposal","","This is a derivation proposal, not yet the canonical taxonomy. It records why each proposed boundary exists and which reviewed concept families motivate it.","",f"Proposed subthemes: **{payload['proposed_subtheme_count']}**; current fixed subthemes: **24**.",""]
    for r in records:
        md += [f"## {r['theme']} — {r['subtheme_count']} proposed subthemes","",r["derivation_reason"],""]
        for s in r["subthemes"]:
            md += [f"### {s['name']}","",f"- Supported-paper evidence inherited from current concepts: **{s['supported_paper_count']}**","- Current concepts: `"+"`, `".join(s["supporting_current_concepts"])+"`",f"- Boundary: {s['boundary']}",""]
    (REPORTS/"SPEECH_ORGANIC_TAXONOMY_PROPOSAL.md").write_text("\n".join(md)+"\n")
    print(json.dumps({"proposed_subthemes":payload["proposed_subtheme_count"],"current_subthemes":24,"status":payload["status"]}))
if __name__=="__main__": main()
