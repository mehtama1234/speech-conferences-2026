#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "huang25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly attack a deep speech classifier through stealthy compression-based triggers and measure attack robustness. The evidence supports speech security and spoofing misuse, without claiming deepfake attribution.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "huang25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly edit speech under background audio while addressing hallucination-like content and evaluating objective and subjective quality. The evidence supports perceptual enhancement, without proving faithful editing in all contexts.", ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "huang25d_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly track intent and slot information across multi-turn spoken-language understanding while selecting relevant history. The evidence supports dialogue state, without proving all real-world conversation shifts.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "huang25e_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study generalization of speech-deepfake detection under domain shifts and unseen test sets. The evidence supports spoofing and synthetic-voice misuse, without proving universal attack robustness.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "huang25f_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly measure tongue configurations and their acoustic consequences in Southwestern Mandarin apical vowels. The evidence supports articulatory coordination, without generalizing from seven speakers.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "huang25g_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly provide a toolkit for predicting human speech-quality scores and compare it across subjective-quality datasets and models. The evidence supports quality and naturalness, without replacing human judgment in every use.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "huang25h_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly relate accent-strength measures to inferred articulatory features across American and British English. The evidence supports accent robustness and analysis, without making the proxy a universal accent scale.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "huang25i_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly jointly recognize stuttering speech and detect stuttering events while preserving the spoken content. This belongs under disfluency and event preservation, not atypical articulation alone.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": sections, "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
