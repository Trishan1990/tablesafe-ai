import pandas as pd
from sklearn.metrics import (
    precision_recall_curve,
    average_precision_score,
    f1_score,
    brier_score_loss
)
import matplotlib.pyplot as plt

# Load benchmark dataset
df = pd.read_csv("data/exp003_weekly_benchmark.csv")

# Ground truth labels
y_true = df["outbreak_label"]

# Predicted probabilities
y_scores = df["composite_risk_score"]

# Binary predictions using threshold
threshold = 0.65
y_pred = (y_scores >= threshold).astype(int)

# Metrics
f1 = f1_score(y_true, y_pred)
auprc = average_precision_score(y_true, y_scores)
brier = brier_score_loss(y_true, y_scores)

print("F1 Score:", round(f1, 3))
print("AUPRC:", round(auprc, 3))
print("Brier Score:", round(brier, 3))

# Precision Recall Curve
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)

plt.figure(figsize=(6,4))
plt.plot(recall, precision)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("EXP-003 Precision Recall Curve")
plt.grid(True)

plt.savefig("evidence/exp003/pr_curve.png")
print("Saved PR curve.")
