# EXP-003 — Multi-Outbreak Generalization Benchmark

## Objective

Evaluate whether the TableSafe AI signal-fusion architecture generalizes across multiple food contamination outbreaks using only public weak-signal sources.

---

# Hypothesis

Public weak-signal escalation patterns from Google Trends, Reddit complaints, FDA recall activity, and news severity indicators can identify contamination risk escalation at least 14 days before formal recall announcements across multiple pathogens and food categories.

---

# Events Evaluated

| Event | Pathogen | Product |
|---|---|---|
| McDonald’s Onion Outbreak | E. coli O157:H7 | Onions |
| Boar’s Head Recall | Listeria monocytogenes | Deli meats |
| Cucumber Recall | Salmonella | Cucumbers |

---

# AI Components Used

- TF-IDF signal extraction
- VADER sentiment analysis
- IsolationForest anomaly detection
- GradientBoosting risk scoring
- Composite weighted signal fusion

---

# Validation Design

- Walk-forward weekly validation windows
- Frozen thresholds and weights prior to execution
- Multi-event benchmarking
- Composite risk escalation scoring
- Recall Lead-Time Advantage (RLTA) analysis

---

# Evidence Collected

Artifacts stored under:

```text
evidence/exp003/

---

# Benchmark Results

| Metric | Result |
|---|---|
| F1 Score | 0.933 |
| AUPRC | 1.000 |
| Brier Score | 0.067 |

Prototype benchmark testing demonstrated strong separability between outbreak escalation periods and baseline periods using public weak-signal fusion.
