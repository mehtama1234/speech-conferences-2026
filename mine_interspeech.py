#!/usr/bin/env python3
"""Create a transparent, abstract-aware INTERSPEECH theme map.

This is a first corpus pass, not a semantic model: membership is deterministic
regular-expression matching over official title and abstract text.  The output
keeps the evidence depth visible so a D2 abstract match is not mistaken for a
full-paper mechanism analysis.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "data" / "interspeech-2025-papers.json"
OUTPUT = HERE / "data" / "interspeech-2025-themes.json"
data = json.loads(INPUT.read_text())
papers = data["papers"]


TAXONOMY = {
    "signal_and_acoustics": {
        "label": "Sound, acoustics, and speech production",
        "why": "Speech begins as changing air pressure shaped by bodies, rooms, microphones, and channels.",
        "patterns": [r"acoustic", r"waveform", r"spectr", r"phonetic", r"phonolog", r"prosod", r"articul", r"vocal tract", r"voice quality"],
    },
    "recognition_and_transcription": {
        "label": "Recognizing and transcribing speech",
        "why": "A system must turn a continuous, variable sound stream into words, boundaries, and aligned text.",
        "patterns": [r"speech recogn", r"automatic speech", r"\basr\b", r"transcri", r"whisper", r"forced align", r"keyword spot", r"wake word", r"phoneme recogn"],
    },
    "understanding_and_translation": {
        "label": "Understanding, translating, and dialoguing",
        "why": "Recognized words are not yet an interpretation of intent, context, or a response in another language.",
        "patterns": [r"spoken language understand", r"speech translation", r"spoken dialog", r"spoken dialogue", r"intent", r"slot filling", r"conversational", r"dialogue", r"translation"],
    },
    "generation_and_voice": {
        "label": "Generating, converting, and controlling voice",
        "why": "A generated voice must preserve linguistic content while controlling identity, timing, expressiveness, and naturalness.",
        "patterns": [r"text[- ]to[- ]speech", r"speech synthes", r"voice conversion", r"voice clon", r"zero[- ]shot tts", r"vocoder", r"expressive speech", r"speech generation"],
    },
    "separation_and_enhancement": {
        "label": "Separating and repairing sound",
        "why": "A microphone records mixtures, echoes, and noise; useful speech must be preserved while unwanted sound is removed.",
        "patterns": [r"speech enhancement", r"denois", r"noise suppress", r"dereverber", r"echo cancell", r"source separat", r"target speaker", r"beamform", r"far[- ]field", r"diariz"],
    },
    "speaker_and_paralinguistics": {
        "label": "Speaker identity and beyond-the-words information",
        "why": "Voice carries information about who is speaking and how they are speaking, but that evidence changes with context.",
        "patterns": [r"speaker recogn", r"speaker verific", r"speaker ident", r"diariz", r"emotion", r"affect", r"paraling", r"prosod", r"stress", r"depress", r"spoof", r"deepfake"],
    },
    "languages_and_people": {
        "label": "Languages, accents, people, and access",
        "why": "Speech systems meet variation in language, dialect, age, disability, health, culture, and available data.",
        "patterns": [r"multilingual", r"cross[- ]lingual", r"low[- ]resource", r"under[- ]resourced", r"code[- ]switch", r"dialect", r"accent", r"child", r"elder", r"dysarth", r"aphas", r"clinical", r"disab"],
    },
    "evaluation_and_deployment": {
        "label": "Evaluation, robustness, privacy, and deployment",
        "why": "A benchmark score is only useful if it stands for a real listening failure and survives new speakers, rooms, languages, and devices.",
        "patterns": [r"robust", r"domain adapt", r"out[- ]of[- ]domain", r"generaliz", r"privacy", r"federated", r"on[- ]device", r"real[- ]time", r"stream", r"efficient", r"quantiz", r"benchmark", r"challenge", r"evaluation"],
    },
}

COMPILED = {key: [re.compile(pattern, re.I) for pattern in spec["patterns"]] for key, spec in TAXONOMY.items()}

for paper in papers:
    haystack = f"{paper.get('title') or ''} {paper.get('abstract') or ''}"
    hits = [key for key, patterns in COMPILED.items() if any(pattern.search(haystack) for pattern in patterns)]
    paper["conceptual_themes"] = hits
    paper["theme_evidence_depth"] = "D2" if paper.get("abstract") else "D1"

counts = Counter(theme for paper in papers for theme in paper["conceptual_themes"])
examples = {theme: [] for theme in TAXONOMY}
for paper in papers:
    for theme in paper["conceptual_themes"]:
        if len(examples[theme]) < 8:
            examples[theme].append({"paper_id": paper["paper_id"], "title": paper["title"]})

output = {
    "venue": data["venue"],
    "source": data["source_manifest"],
    "method": {
        "type": "deterministic-abstract-theme-map",
        "input": "official title and abstract text",
        "evidence_depth": "D2 when abstract is present; membership is not full-paper corroboration",
        "unmatched_papers": sum(not paper["conceptual_themes"] for paper in papers),
    },
    "taxonomy": [
        {
            "id": theme,
            "label": spec["label"],
            "first_principles": spec["why"],
            "paper_count": counts[theme],
            "percent_of_corpus": round(100 * counts[theme] / len(papers), 1),
            "examples": examples[theme],
        }
        for theme, spec in TAXONOMY.items()
    ],
    "paper_count": len(papers),
    "theme_membership_total": sum(counts.values()),
}
OUTPUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
INPUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {OUTPUT}")
for theme, count in counts.most_common():
    print(f"{count:4} {theme}")
print(f"unmatched: {output['method']['unmatched_papers']}")
