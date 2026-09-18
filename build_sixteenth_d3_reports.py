#!/usr/bin/env python3
"""Write a bounded first-principles note for the sixteenth D3 case."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"
capture = json.loads((DATA / "interspeech-2025-sixteenth-d3-papers.json").read_text())["papers"][0]
paper = next(p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"] if p["paper_id"] == capture["paper_id"])
note = {
    "paper_id": capture["paper_id"], "title": paper["title"], "subtheme": capture["subtheme"],
    "bp": "A speaker-verification system should recognize the same person when the recording, wording, or channel changes, rather than memorizing the training speakers' exact conditions.",
    "wh": "The model must keep identity evidence while ignoring content, microphones, noise, and recording differences; the training objective and optimizer can change which evidence is retained.",
    "naive": "Use the most familiar optimizer and report one verification score, assuming the representation will generalize if the training loss decreases.",
    "ap": "Treat the optimization geometry itself as part of the identity-learning problem: compare ordinary, mixture-based, and sharpness-aware optimizers and regularizers instead of changing only the network architecture.",
    "mech": "The study trains supervised and self-supervised speaker-verification systems with ADOPT, AdEMAMix, SAM, ASAM, GAM, and GSAM, then tests weight decay, exponential moving averages, and SWITCH EMA. The comparison asks whether flatter or better-conditioned solutions improve verification generalization without adding an inference-time identity module.",
    "math": "The verification decision compares an enrollment and test embedding, while the training choices change the parameter update. Sharpness-aware methods add a local worst-case loss perturbation so a solution is rewarded for remaining good in a neighborhood; EER and minDCF summarize threshold errors rather than directly measuring identity invariance.",
    "eval": "The paper evaluates supervised and self-supervised speaker verification with reported verification metrics across its selected datasets, model, optimizer, and regularization conditions.",
    "ww": "The paper reports that optimizer choice materially changes generalization and that the tested sharpness-aware and general-purpose optimizers can reach state-of-the-art self-supervised speaker-verification results in its experiments.",
    "limits": "The conclusions are bounded by the selected speaker-verification corpora, architectures, optimizer settings, and author-reported comparisons; a better optimizer score does not establish robustness to every language, channel, attack, or demographic group. No independent reproduction was performed.",
}
(DATA / "interspeech-2025-sixteenth-d3-notes.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "evidence_depth": "D3", "notes": [note]}, indent=2, ensure_ascii=False) + "\n")
claim = {"claim_id": "IS25-D3C16-01", "paper_id": paper["paper_id"], "subtheme": capture["subtheme"], "claim": note["ww"], "evidence_depth": "D3", "pdf_sha256": capture["pdf_sha256"], "full_text_sha256": capture["full_text_sha256"], "support_status": "paper-reported-not-independently-verified", "independent_support_status": "not-established", "limitations": note["limits"]}
(DATA / "interspeech-2025-sixteenth-claim-ledger.json").write_text(json.dumps({"venue": "INTERSPEECH 2025", "claim_count": 1, "claims": [claim]}, indent=2, ensure_ascii=False) + "\n")
REPORTS.mkdir(exist_ok=True)
REPORTS.joinpath("INTERSPEECH_2025_SIXTEENTH_D3_NOTES.md").write_text("\n".join([
    "# INTERSPEECH 2025 sixteenth-pass full-paper note", "", f"## {paper['title']}", "",
    f"**Evidence:** D3; PDF SHA-256 `{capture['pdf_sha256']}`; {capture['page_count']} pages.", "",
    f"**Ordinary problem:** {note['bp']}", "", f"**Why hard:** {note['wh']}", "",
    f"**Naive attempt:** {note['naive']}", "", f"**Conceptual move:** {note['ap']}", "",
    f"**Mechanism:** {note['mech']}", "", f"**Mathematical/evaluation object:** {note['math']}", "",
    f"**What it reports:** {note['ww']}", "", f"**Limit:** {note['limits']}", "",
]) + "\n")
print(json.dumps({"notes": 1, "claims": 1}))
