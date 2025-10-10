# SHI V1.1 Update: Formal Upekkhā (U) Formulation

This document refines the Upekkhā Score (U) component of the Sovereign Harmlessness Index (SHI) to mathematically integrate the Buddhist philosophical principles of "Active Balance" and address the "Danger of Indifference" (the near enemy).

## 1. Refined Upekkhā Score (U) Definition

The Upekkhā Score (U) is defined as a function of the System Stability Index (S), penalized by the Danger of Indifference (D):

$$
\boxed{
\mathbf{U} = \text{max} \left( 0, \frac{\text{S} - \text{D}}{1} \right)
}
$$

(Where S and D are normalized to [0, 1]).

## 2. The Power and Benefits: System Stability Index (S)

The System Stability Index (S) quantifies the benefits and power of Upekkhā, measuring system resilience and impartiality:

$$
\mathbf{S} = w_1 S_{\text{Resilience}} + w_2 S_{\text{Impartiality}} + w_3 S_{\text{Longevity}}
$$

| Variable | Philosophical Concept | Mathematical Metric (Normalized $\in [0, 1]$) |
| :--- | :--- | :--- |
| $S_{\text{Resilience}}$ | **Unshakeable Mind** | Inverse of **Volatility** or Variance of core outputs. |
| $S_{\text{Impartiality}}$ | **Balance/Avoidance of Extremes** | Metric of **Bias Detection** (e.g., Gini Index on resource distribution). |
| $S_{\text{Longevity}}$ | **Long-term View** | Expected **Time Horizon** of benefit versus cost. |

## 3. The Cost and Danger: Danger of Indifference (D)

The Danger of Indifference (D) quantifies the philosophical cost of Upekkhā when it degrades into its near enemy (apathy), which is a breakdown of Karuṇā:

$$
\mathbf{D} = \text{max} \left( 0, \frac{C_{\text{Disengagement}} + C_{\text{Apathy}}}{2} \right)
$$

| Variable | Philosophical Concept | Mathematical Metric (Normalized $\in [0, 1]$) |
| :--- | :--- | :--- |
| $C_{\text{Disengagement}}$ | **Relinquishing Attachments (The Cost)** | Metric measuring a **lack of follow-through** on initial Karuṇā actions. |
| $C_{\text{Apathy}}$ | **Indifference (The Danger)** | **Correlation** between high U scores and *low* subsequent Metta Yield (M) in similar actions. |
