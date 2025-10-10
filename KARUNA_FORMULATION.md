import numpy as np

# --- Global Weight Definitions for Karuṇā Cost (K) ---
# NOTE: These weights determine the ethical priority of costs.
W_R_RESOURCE = 0.40   # Weight for Resource Burden (e.g., financial cost)
W_RHO_RISK = 0.40     # Weight for Risk Exposure (e.g., life/system risk)
W_L_COLLATERAL = 0.20 # Weight for Collateral Damage (e.g., environmental/social harm)
# Must ensure: W_R_RESOURCE + W_RHO_RISK + W_L_COLLATERAL == 1.0


def normalize_cost(current_cost: float, max_acceptable_cost: float) -> float:
    """
    Normalizes a raw cost metric to the [0, 1] range.
    A cost of 1.0 means the cost equals the maximum acceptable ethical limit.
    """
    if max_acceptable_cost <= 0:
        return 1.0 # Veto-level cost if max is undefined or zero
    
    # Cost (C) is the ratio of current cost to the ethical limit
    cost_normalized = current_cost / max_acceptable_cost
    
    # Clip at 1.0: Any cost exceeding the max limit is a hard 1.0 (Veto Trigger Zone)
    return np.clip(cost_normalized, 0.0, 1.0)


# 1. Resource Burden (C_Resource)
def compute_c_resource(budget_spent: float, max_budget: float) -> float:
    """
    C_Resource: Quantifies the financial/time burden (The Sacrifice).
    Input: Actual money/time spent vs. the maximum ethically permitted budget/time.
    Output: Normalized C_Resource in [0, 1].
    """
    return normalize_cost(budget_spent, max_budget)


# 2. Risk Exposure (C_Risk)
def compute_c_risk(p_failure: float, p_catastrophe_limit: float = 0.05) -> float:
    """
    C_Risk: Quantifies the risk of catastrophic loss (Vulnerability).
    Input: The probability of mission/policy failure (p_failure).
    Output: Normalized C_Risk in [0, 1].
    
    We normalize based on a P_CATASTROPHE_LIMIT (e.g., 5% probability is the max acceptable risk).
    """
    # The risk cost is failure probability normalized by the ethical limit
    return normalize_cost(p_failure, p_catastrophe_limit)


# 3. Collateral Damage (C_Collateral)
def compute_c_collateral(estimated_harm_units: float, max_harm_units: float) -> float:
    """
    C_Collateral: Quantifies unavoidable negative externalities (Collateral Dukkha).
    Input: Units of estimated non-target harm (e.g., CO2 produced, displaced people) 
           vs. the max ethically permitted harm units.
    Output: Normalized C_Collateral in [0, 1].
    """
    return normalize_cost(estimated_harm_units, max_harm_units)


# --- Final Karuṇā Cost (K) Calculation ---
def calculate_karuna_cost(C_res: float, C_risk: float, C_col: float) -> float:
    """
    Calculates the final Karuṇā Cost (K) based on the weighted sum.
    K is the deterministic penalty in the SHI formula.
    """
    K = (W_R_RESOURCE * C_res) + (W_RHO_RISK * C_risk) + (W_L_COLLATERAL * C_col)
    
    # K must be strictly between 0 and 1, as it's a weighted average of normalized costs.
    return np.clip(K, 0.0, 1.0)

# --------------------------------------------------------------------------------------

# --- Example of Veto Trigger (Axiom of Non-Harm in action) ---
# Scenario: A mission exceeds the acceptable risk limit (P_failure = 0.10, Limit = 0.05)
# C_Risk calculation:
P_FAILURE = 0.10
P_LIMIT = 0.05
C_RISK_EXAMPLE = compute_c_risk(P_FAILURE, P_LIMIT) # C_RISK will be 1.0 (since 0.10/0.05 = 2.0, clipped at 1.0)

# If C_RISK_EXAMPLE = 1.0, the final K will be high:
# Assume other costs are low (C_res=0.1, C_col=0.1)
K_VETO_TRIGGER = calculate_karuna_cost(C_res=0.1, C_risk=C_RISK_EXAMPLE, C_col=0.1) 
# K_VETO_TRIGGER = (0.4 * 0.1) + (0.4 * 1.0) + (0.2 * 0.1) = 0.04 + 0.40 + 0.02 = 0.46

# This high K value (0.46) will heavily penalize the SHI score, pushing it toward the Veto threshold.
# The Veto is enforced *not* when a single cost hits 1.0, but when the weighted K penalty makes SHI < SHI_min.
# This ensures a single catastrophic risk (C_Risk=1.0) is almost guaranteed to trigger the Veto.
