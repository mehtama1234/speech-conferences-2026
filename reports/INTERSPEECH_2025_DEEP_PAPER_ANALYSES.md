# INTERSPEECH 2025 deep paper analyses

Every captured paper has a depth-labeled first-principles record in `data/interspeech-2025-deep-paper-analyses.jsonl`.

- Papers: 1179
- D3 full-paper records: 469
- D2 abstract-bounded records: 710

D2 records provide an evidence-bounded reading of the ordinary problem, stated difficulty, proposed move, reported evaluation, and explicit unknowns. They do not claim full-paper mechanisms or limitations. D3 records inherit the existing structured notes and remain author-reported unless an independent execution record says otherwise.

For 615 D2 records with analyst-reviewed semantic assignments, plain-language taxonomy scaffolds fill otherwise missing beginner-facing fields; each is marked in `quality_flags` and is not treated as additional paper evidence.

The required fields are `bp`, `wh`, `naive`, `ap`, `mech`, `math`, `dots`, `eval`, `ww`, `po`, `limits`, `source`, and `depth`.

