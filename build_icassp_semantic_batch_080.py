"""Targeted adjudication of clear non-speech technical tasks."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-080.json"
if OUT.exists():
    p = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": p["batch_id"], "status": "preserved-input", "reviewed_count": p["reviewed_count"]}))
    raise SystemExit(0)

REASONS = {
"3629c9760ada3e72b6a97e2d8e41a175ff0acb69":"Beamforming optimization for XR communications is wireless-array engineering, not speech.",
"3d99931e664762747e460eaa5ed5e4f678de4041":"A moving-platform array scheme estimates signal structure for sensing; the title does not identify spoken speech.",
"41dfca0a24929ae8a8b3b577434feb8739734326":"Generic time-series representation learning does not identify speech as its input or target.",
"4217f2e3b6e4c83a92d0af28651185ad32d6623b":"The title identifies EEG emotion recognition, a neural-signal task rather than spoken speech.",
"4502f41071c5e2963cdc5a63ce0d554b8f39b66e":"DOA estimation for mm-wave radar is radar sensing, not speech.",
"45f70bd232ce23e73bfc531f72eec67305047b10":"Sparse-array DOA recovery estimates source direction, not a spoken-speech property.",
"47864d9cf57343a08aac681bbb1864d3aea61664":"12-lead ECG classification is cardiac signal analysis, not speech.",
"4a5ae08f959795b498bd1b08bfcff231139ef6b0":"Multimodal depression detection is a clinical prediction task; the title does not identify spoken speech.",
"4b6caccc5ee860932213532f80bbeb3b3b21281c":"Linguistic steganalysis detects hidden information in language, but the title identifies no spoken-audio task.",
"4caba636cf60116b33fb47db47e7670fa7f194cb":"Cross-subject EEG emotion recognition is neural-signal analysis, not speech.",
"4f740c11121d7f83bf0e0427acd39649f267b30e":"Diffusion-based DOA estimation is spatial signal processing, not speech.",
"5002792cbebdb91d9efddf2ee7d65be597e43cc0":"ECG foundation-model fine-tuning is biomedical waveform analysis, not speech.",
"500f49639f1d1278f59b041f4e1e234d6d4ab5c4":"Sparse-array design for wideband DOA is array sensing, not speech.",
"5015295f08359af651920a1769f311293055e1d1":"OFDM waveform design for radar and communications is wireless engineering, not speech.",
"50bd88eb54949b14e2817fc4efeaa79955f66676":"Robust DOA estimation identifies spatial source direction, not spoken speech.",
"51864be435fed087e5cb8ad50acb482002295533":"Beamforming dimensionality reduction is array signal processing without a speech-specific object.",
"51f44c85173cb19a0175e7d1b34678f6a9e4a492":"Complexity-aware routing for multilingual translation is text or language modeling; no spoken-speech task is identified.",
"52166868110be145ac94f4017d0ebef3165db866":"Difference-coarray design is sparse-array signal processing, not speech.",
"53017c5ceec21133c07c8bddbc38385250dacb10":"Echocardiography segmentation is cardiac image analysis, not speech.",
"55c54fd0dd2f8782fe66ba1cbf8c199b9d0a15db":"In-bed pose and shape estimation from pressure images is human-sensing vision, not speech.",
"56037e5edd51bea1273fedd7f4916014903a777e":"Covariance estimation for array beamforming is spatial signal processing, not speech.",
"57a2fc3889b4e09597be9910a9786f5ee99c3de8":"Gait-emotion recognition uses movement and clinical signals, not spoken speech.",
"5824cf90b852362332293a65d957c14ca3725a7c":"Distributionally robust adaptive beamforming is array processing, not speech.",
"598cc15f637f5c0be05c872ec54139e6ced07044":"Multi-agent LLM debate for clinical question answering is text-based clinical reasoning, not speech.",
"5c3b5b5267f766820103ef89aa8b7534df72a00f":"Single-snapshot DOA estimation reconstructs spatial signal structure, not spoken speech.",
"5d6c4b2fc00ece8b94aaa16dd40b95b4b732d714":"Multilingual multi-hop question answering is text reasoning and does not identify spoken speech.",
"603358e8a0f82dc7c54f4a26017627ed55ea4036":"Histopathology prediction refinement is medical image analysis, not speech.",
"604fa1417989799f31ffc39a804443526f9c7c2d":"Medical image segmentation domain adaptation is visual biomedical analysis, not speech.",
"612b339b94c4a2def1564abf5a64ceceb0de2322":"Encrypted-traffic classification is network telemetry analysis, not speech.",
"65208f5ba108911b56020f57b0be487f10b21993":"A Ziv-Zakai bound for distributed-array DOA is a theoretical sensing result, not speech.",
"681c04ceaa9504e107ad985c2555a8d26395b083":"Fetal ultrasound-plane recognition is medical image analysis, not speech.",
"68b83127e6211a3a7c3757b626eb298052c41f5e":"THz massive-MIMO channel estimation is wireless communications, not speech.",
}
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
rows = []
for pid, reasoning in REASONS.items():
    candidate = next(r for r in queue["rows"] if r["paper_id"] == pid)
    if candidate.get("review_state") == "analyst-reviewed":
        raise SystemExit(f"already reviewed: {pid}")
    p = papers[pid]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": pid, "title": p["title"], "decision": "unsupported", "confidence": f"analyst-reviewed-{depth}", "theme_id": None, "subtheme_id": None, "concept_id": None, "semantic_reasoning": reasoning, "evidence_excerpt": abstract[:1200] if abstract else p["title"], "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-080", "status": "analyst-reviewed-targeted-non-speech-technical-batch", "claim_boundary": "These decisions exclude explicit communications, array sensing, biomedical, vision, and text-only tasks from the spoken-speech taxonomy using preserved title/abstract evidence.", "reviewed_count": len(rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "unsupported": len(rows)}))

