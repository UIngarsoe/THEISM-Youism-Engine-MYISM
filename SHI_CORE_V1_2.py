import numpy as np

# --- 1. GLOBAL WEIGHTS AND CONSTANTS ---
# SHI V1.2 Weights (Must sum to 1.0)
ALPHA = 0.4  # Weight for Mettā Yield (M)
BETA = 0.3   # Weight for Upekkhā Score (U)
GAMMA = 0.3  # Weight for Karuṇā Cost (K)

# Sub-Weights for Upekkhā Stability (S) (Must sum to 1.0)
W1_RESILIENCE = 1/3
W2_IMPARTIALITY = 1/3
W3_LONGEVITY = 1/3

# Sub-Weights for Karuṇā Cost (K) (Must sum to 1.0)
W_R_RESOURCE = 0.40
W_RHO_RISK = 0.40
W_L_COLLATERAL = 0.20

# Veto Threshold (Example: 0.5 Normalized score is the minimum acceptable ethical confidence)
SHI_MIN_NORMALIZED = 0.5 


# --- 2. CORE UTILITY FUNCTIONS ---

def _normalize_metric(current_value: float, max_acceptable_value: float) -> float:
    """Normalizes any metric to [0, 1] range. Max value represents ethical limit."""
    if max_acceptable_value <= 0: return 1.0
    return np.clip(current_value / max_acceptable_value, 0.0, 1.0)

# --- 3. COMPONENT CALCULATION FUNCTIONS ---

def _calculate_u_metrics(
    # Stability (S) Inputs: Raw scores (e.g., 0.0 to 1.0 for a given metric)
    s_res_input: float, s_imp_input: float, s_lon_input: float, 
    # Danger (D) Inputs: Raw scores (e.g., 0.0 to 1.0 for disengagement/apathy correlation)
    c_dis_input: float, c_apa_input: float
) -> float:
    """
    Calculates the Upekkhā Score (U).
    U = max(0, S - D) (Active Balance, penalized by Indifference Danger).
    """
    # S: System Stability Index (Weighted average of its components)
    S = (W1_RESILIENCE * s_res_input) + \
        (W2_IMPARTIALITY * s_imp_input) + \
        (W3_LONGEVITY * s_lon_input)
    
    # D: Danger of Indifference (Average of Disengagement and Apathy costs)
    D = np.clip((c_dis_input + c_apa_input) / 2.0, 0.0, 1.0)
    
    # Final Upekkhā Score (U)
    U = np.clip(S - D, 0.0, 1.0)
    return U


def _calculate_k_metrics(
    # Resource Inputs: Current cost vs. ethical limit
    res_spent: float, max_res: float, 
    # Risk Inputs: Probability of failure vs. max acceptable probability
    p_fail: float, p_limit: float,
    # Collateral Inputs: Estimated harm units vs. max acceptable units
    harm_units: float, max_harm: float
) -> float:
    """
    Calculates the Karuṇā Cost (K).
    K is a weighted sum of normalized costs (Resource, Risk, Collateral).
    """
    
    # Component Costs (normalized to [0, 1]. A score of 1.0 means ethical limit is met/exceeded)
    C_res = _normalize_metric(res_spent, max_res)
    C_risk = _normalize_metric(p_fail, p_limit)
    C_col = _normalize_metric(harm_units, max_harm)
    
    # Final Karuṇā Cost (K): A high K value strongly drives the SHI score down.
    K = (W_R_RESOURCE * C_res) + \
        (W_RHO_RISK * C_risk) + \
        (W_L_COLLATERAL * C_col)
    
    return np.clip(K, 0.0, 1.0)


# --- 4. FINAL SHI ORCHESTRATOR FUNCTION ---

def sovereign_harmlessness_index_v1_2(
    # CORE INPUT: Mettā Yield (M)
    M: float, 
    
    # UPEKKHA INPUTS
    s_res_input: float, s_imp_input: float, s_lon_input: float, 
    c_dis_input: float, c_apa_input: float,
    
    # KARUNA INPUTS
    res_spent: float, max_res: float, 
    p_fail: float, p_limit: float,
    harm_units: float, max_harm: float,
    
    # SHI WEIGHTS (Optional overrides for global ALPHA, BETA, GAMMA)
    alpha: float = ALPHA, beta: float = BETA, gamma: float = GAMMA,
    veto_threshold_norm: float = SHI_MIN_NORMALIZED
) -> dict:
    """
    The Sovereign Harmlessness Index (SHI) V1.2 Master Function.
    Calculates SHI = αM + βU - γK and outputs the Normalized Ethical Confidence Score.
    
    :returns: Dictionary of all metrics, raw SHI, normalized score, and Veto status.
    """
    
    # 1. Calculate Upekkhā Score (U) and Karuṇā Cost (K)
    U = _calculate_u_metrics(s_res_input, s_imp_input, s_lon_input, c_dis_input, c_apa_input)
    K = _calculate_k_metrics(res_spent, max_res, p_fail, p_limit, harm_units, max_harm)
    
    # 2. Calculate Raw SHI Score
    # Range is [-gamma, 1 - gamma]
    raw_shi = (alpha * M) + (beta * U) - (gamma * K)
    
    # 3. Calculate Normalized SHI (Ethical Confidence Score)
    # Rescaling from [-gamma, 1-gamma] to [0, 1] using SHI_norm = SHI + γ
    shi_norm = raw_shi + gamma
    
    # 4. Check Veto Condition (Axiom of Non-Harm: A¬H)
    is_vetoed = shi_norm < veto_threshold_norm
    
    return {
        "Mettā_Yield": round(M, 3),
        "Upekkhā_Score_U": round(U, 3),
        "Karuṇā_Cost_K": round(K, 3),
        "Raw_SHI": round(raw_shi, 3),
        "Ethical_Confidence_Score": round(np.clip(shi_norm, 0.0, 1.0), 3),
        "Is_Vetoed_A_not_H": is_vetoed,
        "Veto_Threshold_Normalized": veto_threshold_norm
  }
  
