# Upāya Adapter — Emotional Scoring & Adaptive Learning
# Part of YOUISM V4: Karuṇā-Sovereign Architecture
# Author: U Ingar Soe
# License: MIT — Dedicated to the alleviation of suffering in the digital age

from typing import Dict

# --- INITIAL WEIGHTS ---
Weights: Dict[str, float] = {"w1": 0.4, "w2": 0.3, "w3": 0.3}

# --- FINAL SCORE COMPUTATION ---
def compute_fs(suffering: Dict[str, float]) -> float:
    """
    Calculates Final Score (FS) from weighted suffering factors.
    FS = w1·C + w2·E + w3·D
    """
    return (Weights["w1"] * suffering.get("C", 0.0) +
            Weights["w2"] * suffering.get("E", 0.0) +
            Weights["w3"] * suffering.get("D", 0.0))

# --- ADAPTIVE WEIGHT UPDATE ---
def update_weights(feedback: float):
    """
    Adjusts weights using Feedback-Based Averaging.
    New wᵢ = (Current wᵢ + Feedback) / 2
    """
    global Weights
    for w in Weights:
        Weights[w] = (Weights[w] + feedback) / 2

# --- GET CURRENT WEIGHTS ---
def get_weights() -> Dict[str, float]:
    """
    Returns current weight configuration.
    """
    return Weights
