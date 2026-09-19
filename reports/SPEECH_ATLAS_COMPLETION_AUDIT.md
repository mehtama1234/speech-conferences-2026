# Speech atlas completion audit

**Status:** `organic-taxonomy-release-in-progress-with-explicit-boundaries`

The paper-grounded atlas has been rebuilt around an organically derived taxonomy proposal: its semantic layers, syntheses, provenance, artifact audit, reader path, rebuild, and validator are internally consistent. The new boundaries still require analyst review of rejected splits, rejected merges, and unresolved cases before the conceptual goal can be called complete.

| Requirement | Status | Evidence |
|---|---|---|
| baseline-first-principles-source | `verified-with-boundaries` | Fant, Gunnar. Sound, features, and perception. STL-QPSR 8(2-3), 1967, pp. 1-14.; 6 page-anchored principles are recorded. The source provides a conceptual chain, not a complete taxonomy or proof of current paper claims. |
| corpus-provenance | `verified-with-boundaries` | ICASSP preserved-input source manifest plus official ISCA archive manifest; 3739 official ICASSP accepted-paper title/paper-number matches are preserved, while the corpus remains discovery metadata for abstracts and full text. |
| full-paper-coverage-record | `verified-with-boundaries` | 1179 per-paper D2/D3 records; 469 D3 and 710 D2. |
| icassp-paper-evidence | `verified-with-boundaries` | 3864 ICASSP D1/D2 per-paper evidence records now preserve title-only versus abstract-backed boundaries; full-paper access remains unavailable for the corpus. |
| conceptual-taxonomy | `verified-with-boundaries` | The bounded taxonomy has 8 themes, 34 subthemes, and 72 concepts; 72/72 concepts have explicit definitions, boundaries, positive/negative membership examples, and D1/D2/D3 evidence rules. All 1179 INTERSPEECH and 3864 ICASSP records have explicit reviewed membership; the taxonomy remains an analytic model, not a claim about all speech research. |
| semantic-review-closure | `verified-with-boundaries` | An explainable proposal queue covers 1179 INTERSPEECH papers; 1179 have analyst-reviewed D2/D3 dispositions, with no provisional or unresolved INTERSPEECH rows. |
| corpus-wide-semantic-dispositions | `verified-with-boundaries` | Every INTERSPEECH and ICASSP record has an explicit disposition with preserved evidence and unresolved reason: INTERSPEECH {'analyst-confirmed': 1076, 'analyst-rejected': 103}, ICASSP {'analyst-rejected': 3429, 'analyst-confirmed': 434, 'analyst-unresolved': 1}. Provisional candidates are visibly not counted as analyst-confirmed. |
| icassp-semantic-boundary | `verified-with-boundaries` | An explicit queue covers 3864 ICASSP records with D1/D2 depth; 3864 have analyst-reviewed dispositions, including 1 explicitly insufficient-evidence case(s). This closes membership adjudication at the available metadata boundary; it does not make title-only records full-paper evidence. |
| deep-paper-analysis | `verified-with-boundaries` | 1179 papers have required first-principles fields at explicit D2/D3 depth; 469 have full-paper evidence. D2 records remain explicitly bounded, and D3 claims remain author-reported. |
| seed-family-synthesis | `verified-with-boundaries` | The bounded seed synthesis covers 8 themes from 456 reviewed D3 papers; it is not a venue-wide prevalence or independent scientific conclusion. |
| subtheme-synthesis | `verified-with-boundaries` | All 34 taxonomy subthemes have explicit synthesis records; 34 contain analyst-reviewed D2/D3 evidence and 34 contain D3 evidence. The taxonomy-valid D3 minimum is 3 papers across 34 subthemes, with concept boundaries and tradeoffs preserved. |
| first-principles-writeups | `verified-with-boundaries` | The writeup gate finds 34 of 34 subthemes complete against the required plain-language fields. This checks presence and evidence links; human review is still required for conceptual correctness. |
| per-paper-depth-and-provenance | `verified-with-boundaries` | The paper audit checks 1179 of 1179 records: D3 rows require captured PDF/text and D2 rows require an explicit abstract-only boundary. This does not certify interpretation or independent reproduction. |
| current-taxonomy-membership-adjudication | `in-progress` | The current taxonomy has 345 supported memberships still awaiting re-adjudication and 1394 adjudicated in the current queue. Prior semantic review and mechanical normalization are preserved, but they are not treated as final current-boundary decisions. |
| unified-theme-subtheme-teaching-report | `verified-with-boundaries` | A unified report covers every taxonomy theme and subtheme with baseline link, ordinary pressure, failed shortcut, recurring move, named evidence, boundaries, and open questions. It remains an analyst-authored synthesis and does not replace paper-level review. |
| reader-navigation | `verified-with-boundaries` | First-principles reading paths connect ordinary problems, failed shortcuts, conceptual moves, subthemes, papers, and evidence limits; the paths remain bounded by the reviewed D3 seed. |
| atlas-index | `verified-with-boundaries` | A plain-language index points readers to the taxonomy, reading paths, subtheme syntheses, paper analyses, gaps, and cross-venue comparison while preserving the incomplete-review boundary. |
| unresolved-case-visibility | `verified-with-boundaries` | A human-readable semantic-gap report separates ambiguous, insufficient-evidence, and ICASSP out-of-scope rows with examples and next actions; unresolved cases remain open. |
| claim-provenance | `verified-with-boundaries` | 456 reviewed-paper claims link to captured PDF/text hashes; independent support remains not-established. |
| artifact-reproducibility | `verified-with-boundaries` | Artifact links and reachability are recorded; idiap/RnV syntax-pass at ad9ce5c42c12dae05054bf2db6af2e4b3a89c0ea; lee-jhwn/IS25-emg-ema syntax-pass at d8bd5cfe1722ac58f0e612582e6ae4b30fdac29d; techsword/reliability-speech-feat-attr syntax-pass at 37990e842ae8c59463b75f394c0e91deebcbc198; luferrer/ConfidenceIntervals syntax-pass at 4c320a10686c3b0472d93e17ab6315081d6f6738; luferrer/ConfidenceIntervals check-error at 4c320a10686c3b0472d93e17ab6315081d6f6738; luferrer/ConfidenceIntervals smoke-pass at 4c320a10686c3b0472d93e17ab6315081d6f6738; aizhiqi-work/voxaging syntax-pass at 84f4dae15e1dac56ed46fddeec2abef472ebe822; modelscope/3D-Speaker syntax-pass at 065629c313eaf1a01c65c640c46d77e61e9607b4; seblemaguer/replikant package-build-pass at 81e308a079cb8e616929083e332ab4546174dbfa; langtech-bsc/commonphone-se syntax-pass at 2033c235e5c27ff5ecea1957d537be29bf11654d. These are bounded syntax/toy-smoke checks only; data-dependent training and scientific reproduction remain not-attempted. |
| cross-venue-synthesis | `verified-with-boundaries` | ICASSP/INTERSPEECH crosswalk includes denominators and warns that title-only versus abstract evidence and mixed scope prevent direct prevalence comparison. |
| deterministic-rebuild | `verified` | rebuild_speech_atlas.py completed and verify_speech_atlas.py returned zero errors; release manifest contains derived artifacts and evidence inputs. |
| unsupported-claims | `verified` | Reports and ledgers explicitly reject unsupported causal, prevalence, reproduction, clinical, and scientific-completeness claims. |

## Remaining bounded work

- Complete and human-review every theme and subtheme writeup, then confirm or revise each proposed split, merge, and unresolved boundary against the baseline account and named paper evidence before declaring the conceptual taxonomy final.

## Open evidence boundaries

- Additional D3 readings beyond the current 469-paper seed are optional expansion, not a closure defect.
- The artifact audit contains bounded syntax/package/smoke checks; data-dependent training and independent scientific reproduction remain unestablished.
- The ICASSP official supplement matches 3739 discovery records; 125 discovery records remain unmatched and are retained with their source boundary.
