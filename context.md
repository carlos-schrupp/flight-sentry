# Flight Sentry — Portfolio Translation Context (from `index.html`)

This repo contains a Databricks-notebook-to-HTML export (`index.html`). The notebook reads like an internal project report: it is highly detailed, references section numbers, includes notebook artifacts (e.g., `%md`), and contains team emails + Slack-hosted photos.  
Goal: keep the page technical and credible for technical recruiters, but make it self-contained and readable for someone who did not work on the project.

Output files:
- **Source**: `index.html` (full technical report export)
- **Target**: `portfolio.html` (recruiter-friendly narrative + key figures + key results)

---

## Audience & framing

Recruiters/hiring managers typically scan in ~2–5 minutes. The portfolio version should:
- Lead with **what the system does**, **why it matters**, and **proof it works** (metrics + scale).
- Explain core technical decisions in plain language (esp. **T-2h cutoff**, **leakage control**, **time-aware validation**).
- Keep the deep-dive material accessible via **optional details/appendix**, not as the main reading path.

---

## Project facts worth surfacing early (from `index.html`)

- **Task**: predict whether a domestic U.S. flight will depart **≥ 15 minutes late** (`DEP_DEL15`), using only features available **2 hours before scheduled departure** (T-2h).
- **Data scale**: **31.1M flights** (2015–2019) using DOT on-time performance + NOAA weather; enriched with airport/station metadata.
- **Class imbalance**: about **18.15% delayed** (~82:18).
- **Engineering**: Spark-based, checkpointed multi-stage pipeline; strict temporal ordering and leakage prevention.
- **Feature set**: **112 leakage-free features** spanning temporal patterns, rolling delay aggregates, weather, congestion, carrier history, and network (graph) signals.
- **Top-end results (best reported summary)**:
  - **XGBoost ensemble (regression → threshold)**: **F2 ≈ 0.697**, **Recall ≈ 0.725**, **AUC‑PR ≈ 0.723**.
  - **Best direct classifier (CNN)**: **F2 ≈ 0.680**, **Recall ≈ 0.843**, **AUC‑PR ≈ 0.664**.
  - **Best regression metrics (ensemble)**: **RMSE ≈ 41.69 min**, **MAE ≈ 11.92 min**.

---

## What to de-projectify (make general + portfolio-safe)

Remove or replace:
- **Team emails** and **Slack-hosted headshots** (privacy + link rot).
- Internal storage paths like `dbfs:/...` (replace with “cloud object storage / data lake”).
- Notebook artifacts (`%md`, “Phase X extra points”, grading language).
- Overlong “Report Structure” lists that reference section numbers (replace with narrative sections).

Keep (but explain):
- “Phases” only as **iterations** (v1 baseline → v2 scale-up → v3 tuning), not course logistics.
- Technical details that signal maturity: leakage prevention, time-series split, distributed pipeline design, calibration/thresholding strategy.

---

## Section translation map (index → portfolio)

### 1) Project overview
**Index sections**: `1. Introduction`, `3.1 Project Abstract`  
**Portfolio translation**:
- Start with a 3–5 sentence “TL;DR”: what, why, and how well.
- Include a compact “quick facts” panel (data size, prediction window, best metric).

### 2) Problem & user value
**Index sections**: intro + scattered “Business Implications”  
**Portfolio translation**:
- Explain the operational use-case: early warning enables gate/crew planning and proactive comms.
- Clarify tradeoffs: “false alarm” vs “missed delay” → why **F2** (recall-weighted).

### 3) Data & leakage control
**Index sections**: `3.3 The Data` + join + leakage strategy (ER model, as-of join figures)  
**Portfolio translation**:
- Name the sources in plain language (DOT + NOAA), and why each matters.
- Explain *leakage* with one concrete example: “don’t use post-departure timestamps”.
- Explain the **T-2h join** and “as-of” weather alignment.
- Keep 1–3 key figures (pipeline diagram, leakage strategy figure).

### 4) Feature engineering (what signals matter)
**Index sections**: feature families + top importance paragraph  
**Portfolio translation**:
- Summarize feature families with examples (rolling origin delay rate, prior-leg delay, congestion proxies, network centrality).
- Add 1 paragraph on interpretability: “which signals dominated and why it makes sense operationally”.

### 5) Modeling strategy (time-aware validation)
**Index sections**: `5.*` + cross-validation + experiment summaries  
**Portfolio translation**:
- Present two tracks:
  1) direct classification (LR/RF/GBT/MLP/CNN)
  2) regression → threshold (XGBoost ensemble)
- Explain why time-series splitting matters and how it was done (train earlier, test later; blind 2019 holdout).
- Highlight the learning: regression-to-binary can outperform direct classification on F2/AUC‑PR.

### 6) Results (make it skimmable)
**Index sections**: `5.7 Summary of all ML Experiments` + selected plots  
**Portfolio translation**:
- Put best numbers in a small table (top 4–6 rows).
- Add 2 bullets: “best for recall”, “best for F2/AUC‑PR”.
- If including training time, label it as environment-dependent.

### 7) Engineering & scalability
**Index sections**: pipeline stages, parquet/compression benchmarking, cluster notes  
**Portfolio translation**:
- State what was required to make 31M rows feasible: checkpoints, caching, careful persistence, partitioning.
- Keep it tool-agnostic: “Spark on a cloud cluster” rather than vendor-specific paths.

### 8) What’s next (production considerations)
**Index sections**: “Open Issues and Next Steps”  
**Portfolio translation**:
- Real-time feature computation
- Monitoring and drift
- Threshold calibration by carrier/airport
- Testing robustness on later years (e.g., post-2019 regime shifts)

### 9) Credits
**Index sections**: team members  
**Portfolio translation**:
- List team members without emails; optionally add “my role” placeholders for you to personalize.

---

## Glossary (add to portfolio page)

- **DEP_DEL15**: binary label for departure delay ≥ 15 minutes.
- **T-2h**: prediction uses only data available 2 hours prior to scheduled departure.
- **Leakage**: features that “peek into the future” (post-departure info).
- **F2 score**: like F1 but weights recall higher (β=2), aligned to catching at-risk flights.
- **AUC‑PR / AuPRC**: precision–recall area; better than ROC-AUC when the positive class is rare.

---

## Talking points (interview-ready)

- “We treated this as an **operational early-warning** problem, so we optimized for recall-weighted metrics and enforced a strict **T-2h feature cutoff**.”
- “Most of the work was data engineering: rebuilding a **leakage-safe** join at 31M-row scale and checkpointing each stage for reproducibility.”
- “We compared direct classifiers vs regression-to-binary. The **XGBoost ensemble** had the best F2/AUC‑PR, while the **CNN** gave the best recall.”
- “Next steps are production concerns: near-real-time features, drift monitoring, and threshold calibration by context.”

