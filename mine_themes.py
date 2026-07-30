"""
Theme-mine ICASSP 2026 from titles alone — HONESTLY.

ICASSP is "Acoustics, Speech, AND Signal Processing" — a broad conference where
speech is one large slice among image/video, biomedical, remote sensing, comms,
time-series and general ML. So we do two levels:
  1. PRIMARY DOMAIN — assign each paper to one best domain (priority-ordered,
     specific keywords) so we get an honest landscape of the whole conference.
  2. SPEECH & AUDIO ZOOM — within the speech/audio papers, the research sub-themes.
Deterministic keyword rules: transparent, reproducible, no LLM guessing on titles.
"""
import json, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "data", "icassp-2026-papers.json")))
papers = data["papers"]

# --- LEVEL 1: primary domain (priority order — first match wins) --------------
DOMAINS = [
 ("Speech & Spoken Language", [r"\bspeech\b", r"\basr\b", r"\btts\b", r"text[- ]to[- ]speech", r"speaker", r"diariz", r"\bvoice\b", r"spoken", r"phonem", r"prosod", r"vocoder", r"wav2vec", r"hubert", r"wavlm", r"utterance", r"pronunciation", r"\basv\b", r"voice conversion", r"keyword spotting", r"\bkws\b", r"dysarth", r"accent"]),
 ("Audio & Music", [r"\baudio\b", r"\bmusic\b", r"sound event", r"acoustic scene", r"\bdcase\b", r"singing", r"instrument", r"sound source", r"\bmir\b", r"environmental sound", r"audio caption", r"sound classif", r"acoustic event"]),
 ("Medical & Biomedical", [r"medical", r"clinical", r"\bmri\b", r"\bct\b", r"\becg\b", r"\beeg\b", r"\bemg\b", r"tumor", r"cancer", r"disease", r"diagnos", r"healthcare", r"lesion", r"patholog", r"biomedical", r"\bfmri\b", r"electrocardio", r"sleep stage", r"seizure", r"retinal", r"histopath"]),
 ("Remote Sensing & Radar", [r"remote sensing", r"\bsar\b", r"\bradar\b", r"hyperspectral", r"satellite", r"\blidar\b", r"\bsonar\b", r"geoscience", r"earth observation", r"synthetic aperture"]),
 ("Image & Video", [r"\bimage\b", r"\bvideo\b", r"visual", r"object detection", r"segmentation", r"gaussian splatting", r"super[- ]?resolution", r"\bface\b", r"optical flow", r"tracking", r"re[- ]?identification", r"point cloud", r"3d reconstruction", r"\bdepth\b", r"scene", r"frame", r"pose estimation", r"neural radiance", r"\bnerf\b"]),
 ("Communications & Wireless", [r"communication", r"wireless", r"\bmimo\b", r"channel estimation", r"\bofdm\b", r"modulation", r"\b5g\b", r"\b6g\b", r"beamforming.*(wireless|comm)", r"\bcsi\b", r"spectrum sensing", r"network coding", r"antenna"]),
 ("Time Series & Sensing", [r"time series", r"forecasting", r"anomaly detection", r"sensor", r"\biot\b", r"fault diagnos", r"predictive maintenance", r"wearable", r"activity recognition", r"traffic"]),
 ("Graph, Learning & Theory", [r"graph neural", r"\bgnn\b", r"federated", r"contrastive", r"reinforcement learning", r"optimization", r"sparse recovery", r"compressed sensing", r"tensor", r"matrix completion", r"bayesian", r"generative model", r"diffusion model"]),
]
COMPILED_D = [(name, [re.compile(p, re.I) for p in pats]) for name, pats in DOMAINS]

def domain_of(title):
    for name, pats in COMPILED_D:
        if any(p.search(title) for p in pats):
            return name
    return "Other Signal Processing"

for p in papers:
    p["domain"] = domain_of(p["title"])

domain_counts = Counter(p["domain"] for p in papers)
domain_examples = {d: [] for d, _ in domain_counts.most_common()}
for p in papers:
    if len(domain_examples[p["domain"]]) < 6:
        domain_examples[p["domain"]].append(p["title"])

# --- LEVEL 2: speech & audio sub-themes (only over that subset) ---------------
SPEECH_SET = {"Speech & Spoken Language", "Audio & Music"}
speech_papers = [p for p in papers if p["domain"] in SPEECH_SET]

SUBTHEMES = {
 "Speech Recognition (ASR)": [r"\basr\b", r"speech recognition", r"acoustic model", r"transducer", r"\bctc\b", r"rnn[- ]?t\b", r"whisper", r"transcription", r"\bwer\b", r"end[- ]to[- ]end speech"],
 "Speech Synthesis / TTS": [r"\btts\b", r"text[- ]to[- ]speech", r"speech synthesis", r"vocoder", r"voice cloning", r"\bvits\b", r"zero[- ]?shot tts"],
 "Speaker Verification / Anti-Spoofing": [r"speaker verification", r"speaker recognition", r"speaker embedding", r"\bx[- ]?vector", r"ecapa", r"anti[- ]?spoof", r"\bspoof", r"deepfake", r"\basv\b", r"voiceprint"],
 "Speaker Diarization": [r"diariz", r"speaker segmentation", r"\beend\b", r"who spoke"],
 "Speech Enhancement / Denoising": [r"enhancement", r"denois", r"noise suppress", r"noise reduction", r"dereverber", r"echo cancel", r"\baec\b", r"restoration"],
 "Source / Target Separation": [r"separation", r"tasnet", r"target speaker extraction", r"cocktail"],
 "Emotion / Paralinguistics": [r"emotion", r"\bser\b", r"paralinguistic", r"affect", r"depression", r"stress"],
 "Self-Supervised / Foundation": [r"self[- ]?supervis", r"\bssl\b", r"foundation model", r"pre[- ]?train", r"wav2vec", r"hubert", r"wavlm", r"representation"],
 "Speech LLM / Speech-to-Speech": [r"large language model", r"\bllm\b", r"speech[- ]?to[- ]?speech", r"spoken (llm|dialogue)", r"audio language model", r"in[- ]?context"],
 "Voice Conversion": [r"voice conversion", r"accent conversion", r"singing voice conversion"],
 "Spoken Language Understanding": [r"spoken language understanding", r"\bslu\b", r"intent", r"slot", r"speech translation", r"voice assistant"],
 "Keyword Spotting / Wake Word": [r"keyword spotting", r"\bkws\b", r"wake[- ]?word", r"spoken term"],
 "Multilingual / Low-Resource": [r"multilingual", r"low[- ]?resource", r"cross[- ]?lingual", r"code[- ]?switch", r"dialect"],
 "Audio-Visual Speech": [r"audio[- ]?visual", r"lip read", r"talking (face|head)", r"visual speech"],
 "Music & Sound Events": [r"\bmusic\b", r"sound event", r"acoustic scene", r"singing", r"instrument", r"\bdcase\b"],
 "Speech Health / Clinical": [r"patholog", r"dysarth", r"parkinson", r"alzheimer", r"aphasia", r"clinical", r"disorder", r"cough"],
}
COMPILED_S = {t: [re.compile(p, re.I) for p in pats] for t, pats in SUBTHEMES.items()}
sub_counts = Counter(); sub_examples = {t: [] for t in SUBTHEMES}
for p in speech_papers:
    hits = [t for t, pats in COMPILED_S.items() if any(x.search(p["title"]) for x in pats)]
    p["subthemes"] = hits
    for t in hits:
        sub_counts[t] += 1
        if len(sub_examples[t]) < 8:
            sub_examples[t].append(p["title"])

# --- cross-cutting methods (measured WITHIN speech, honestly labelled) --------
METHODS = {
 "diffusion / flow-based": [r"diffusion", r"flow matching", r"flow[- ]based"],
 "efficiency / on-device": [r"efficient", r"quantiz", r"pruning", r"distill", r"on[- ]?device", r"lightweight", r"streaming", r"real[- ]?time", r"low[- ]?latency"],
 "self-supervised / pretrained": [r"self[- ]?supervis", r"pre[- ]?train", r"foundation"],
 "LLM-based": [r"\bllm\b", r"large language model", r"gpt"],
 "adversarial / robust / privacy": [r"adversarial", r"robust", r"privacy", r"federated", r"watermark"],
}
COMPILED_M = {m: [re.compile(p, re.I) for p in pats] for m, pats in METHODS.items()}
method_counts = Counter()
for p in speech_papers:
    for m, pats in COMPILED_M.items():
        if any(x.search(p["title"]) for x in pats):
            method_counts[m] += 1

OUT = {
 "venue": data["venue"], "location": data["location"], "dates": data["dates"],
 "n_papers": len(papers), "n_speech_audio": len(speech_papers),
 "with_abstract": data["with_abstract"], "with_arxiv": data.get("with_arxiv", 0),
 "domains": [{"domain": d, "n": n, "pct": round(n*100/len(papers), 1), "examples": domain_examples[d]}
             for d, n in domain_counts.most_common()],
 "speech_subthemes": [{"theme": t, "n": n, "pct": round(n*100/max(len(speech_papers),1), 1), "examples": sub_examples[t]}
                      for t, n in sub_counts.most_common()],
 "speech_methods": [{"method": m, "n": n, "pct": round(n*100/max(len(speech_papers),1), 1)}
                    for m, n in method_counts.most_common()],
}
json.dump(OUT, open(os.path.join(HERE, "data", "icassp-2026-themes.json"), "w"), indent=1)

print(f"{len(papers)} papers · {len(speech_papers)} speech/audio ({len(speech_papers)*100//len(papers)}%)")
print("\nPRIMARY DOMAINS:")
for d, n in domain_counts.most_common():
    print(f"  {n:>4} ({n*100//len(papers):>2}%)  {d}")
print("\nSPEECH & AUDIO SUB-THEMES:")
for t, n in sub_counts.most_common():
    print(f"  {n:>4}  {t}")
print("\nMETHODS within speech:", ", ".join(f"{m} {n}" for m, n in method_counts.most_common()))
print("wrote data/icassp-2026-themes.json")
