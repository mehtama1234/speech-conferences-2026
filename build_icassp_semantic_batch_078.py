"""Targeted adjudication of clear non-speech technical tasks."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-078.json"
if OUT.exists():
    p = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": p["batch_id"], "status": "preserved-input", "reviewed_count": p["reviewed_count"]}))
    raise SystemExit(0)

IDS = {
    "06b4ef93f1b3549d8fdf2d7d4ae262039ba2b5b3": "Oxford Nanopore basecalling reads sequencing signals; it is not a spoken-speech recognition or production task.",
    "0895197999a7d20f004a9f94ee296c14c81e634f": "SSVEP-BCI recognition uses visual-evoked brain responses, not spoken speech.",
    "140874c5879b770495d609e6b076101231083a34": "PPG-based blood-pressure waveform reconstruction is a cardiovascular sensing task, not speech.",
    "1465f6863b6291fb00cfd96bad257a38116061b1": "Direction-of-arrival estimation for sparse arrays is spatial signal processing, with no speech object identified.",
    "14add87d652091a650bbc84b085d42c7de7defeb": "Quantum image representation and compression concerns images, not spoken speech.",
    "15cde8da658f48b1bab0ce57d383e46cd04690cc": "The title identifies multimodal depression recognition but does not identify spoken speech as the input or target.",
    "1740109ae36021893d3410e8386d97f43999a7ae": "Depression recognition from graph and clinical priors is not established as a speech task by the title.",
    "176cefd7d80a2573f9321ce1c2dc72ff4a76094c": "DOA estimation and virtual-array beamforming estimate source direction, not a spoken-speech property.",
    "178709fec26cc8737f0f0c2b73c1b772527bc321": "EEG spectrogram feature extraction is a neural-signal task, not spoken-speech processing.",
    "18428319cc43d3d65811fbe077e093287e97425a": "Myocardial-infarction localization from 12-lead ECG is cardiac diagnosis, not speech.",
    "1849adc3ffb0dd0597e21b5537d8f11c1a2023ed": "EEG emotion recognition is neural-signal analysis and does not establish a spoken-speech task.",
    "197064a71ac4df2d5d268db2530aeb32203e691e": "TMS and online BCI motor control concern brain-computer interaction, not spoken speech.",
    "1ad1dfcf43730a91d884d5e25c8d6cb694f6ce07": "Classroom teaching-stage segmentation is video or activity analysis, not spoken-speech processing.",
    "1d1de6190e9f0a9a7cb2637e9ba077b0f6f03d7e": "ECG compression is biomedical waveform coding, not speech coding.",
    "1d78720907ce57610a6cfec0141e74b5198e1747": "Full-waveform inversion estimates subsurface or physical structure from sensing data, not speech.",
    "1f7f4b66fda7ef804bceab607937a7dc7968b55a": "Low-power dot-product arithmetic is a hardware computation problem, not a speech task.",
    "2236d7ede5703ced2385b53c391fe4f4ef7c68b6": "Depression detection from EEG signals is clinical neural-signal analysis, not spoken speech.",
    "225cf101c8b736b4c711d55b1f33f3093065b727": "Robust adaptive beamforming and SINR optimization concern wireless arrays, not speech.",
    "230031ddf8cfc524df1ac4bbff64928f156394fb": "Caption- and audio-guided video retrieval is a general audiovisual retrieval task; the title does not establish spoken speech.",
    "249733cd5137cc0dd5e31dca727ee118a93491f5": "Motor-imagery EEG classification is BCI signal decoding, not speech.",
    "24c14ce0ff15367e44ebade40ada8f54d31fb723": "Face anti-spoofing is a visual biometric-security task, not speech anti-spoofing.",
    "2a6b7f3dd9ff9fe1ea9356e796b5dfa71814d691": "Cognitive-load estimation from brain foundation models is BCI neural-signal analysis, not speech.",
    "2d1d3a3a9d8c1f20fa325f216666054abac18131": "Cross-lingual named-entity recognition is text-only language processing; no spoken-speech signal is identified.",
    "2d774b6a3eee83b2d4d655c4158dbab968ae1d75": "EEG emotion recognition is neural-signal analysis, not spoken speech.",
    "2eb0d6a7816eaceb182a907ea43b57b9b1e7dfe7": "Fetal ultrasound image segmentation is medical image analysis, not speech.",
    "2f2c9629f110cb4906f8a66a5ac674ef42d8daa3": "Spherical-harmonic DOA estimation is spatial acoustics or array processing without a speech-specific task.",
    "2f3847a946b10c9766693ee87e8d23bcbaca6a8a": "An ECG dialogue agent operates on cardiac records and signals; it is not a spoken-speech system.",
    "2fe5ec02dfb0bdda2195a7f6fde4a16664b3f70e": "Self-supervised EEG emotion recognition is neural-signal analysis, not speech.",
    "308a78ece1319fdbc5c94ce31f6122b65821fd6f": "GNSS spoofing detection is satellite-navigation security, not speech anti-spoofing.",
    "30f7b8aeb092465533b904c59759d0a4886d02d4": "Movement-disorder recognition from clinical video is visual clinical analysis, not speech.",
    "34401e9249b441eebc204ccecf8527f81a6758f9": "Adaptive transmit beamforming for ultrasound quantification is sensing and array control, not speech.",
    "356e27aa8156fbb0ad9d77eec12263f92f39e28c": "Knowledge-graph completion with multilingual text is text reasoning, not a spoken-speech task.",
}
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
rows = []
for pid, reasoning in IDS.items():
    candidate = next(r for r in queue["rows"] if r["paper_id"] == pid)
    if candidate.get("review_state") == "analyst-reviewed":
        raise SystemExit(f"already reviewed: {pid}")
    p = papers[pid]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": pid, "title": p["title"], "decision": "unsupported", "confidence": f"analyst-reviewed-{depth}", "theme_id": None, "subtheme_id": None, "concept_id": None, "semantic_reasoning": reasoning, "evidence_excerpt": abstract[:1200] if abstract else p["title"], "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-078", "status": "analyst-reviewed-targeted-non-speech-technical-batch", "claim_boundary": "These decisions exclude clear biomedical, BCI, array, vision, hardware, and text-only tasks from the spoken-speech taxonomy using preserved title/abstract evidence.", "reviewed_count": len(rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "unsupported": len(rows)}))

