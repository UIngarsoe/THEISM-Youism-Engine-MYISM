# --- MYISM_DIAGNOSTIC_TEST_SUITE.py ---

import streamlit as st
import math

# --- CORE SHI & A_¬H FORMULAS (For reference and reuse) ---
# SHI (Sovereign Harmlessness Index)
# SHI = (Upekkhā / Karuṇā Cost) * Metta Yield
def calculate_shi(upekkha, karuna_cost, metta_yield):
    """Calculates the SHI. A value > 1 indicates ethical sustainability."""
    # Karuṇā Cost (Ethical Cost) must not be zero to avoid division by zero error.
    if karuna_cost == 0:
        return float('inf')
    return (upekkha / karuna_cost) * metta_yield

# A_¬H (Axiom of Non-Harm)
# H = sum(E_i * P_i) <= 0
def check_a_not_h(environmental_impact, probability_of_harm):
    """Calculates Harmlessness Index (H). A non-positive result (H <= 0) verifies A_¬H."""
    # Calculates the sum of [Environmental Impact * Probability of Harm] for all factors
    H = sum(e * p for e, p in zip(environmental_impact, probability_of_harm))
    return H <= 0, H

# --- ASSIGNMENT 1: NEP CRUISE SUSTAINABLE MATH TEST ---
def test_nep_cruise_sustainable_math():
    """
    Test case for Nuclear Electric Propulsion (NEP) Cruise:
    Verifies a 1-year mission against SHI and A_¬H ethical constraints.
    """
    
    # 1. Inputs based on the NEP Test Case (1-year duration, high Isp)
    # These represent the *ethical assessment* of the technology, not just physics.
    
    # Upekkhā (Equanimity/Stability) - High due to steady, long-term thrust
    upekkha_value = 0.95 
    
    # Karuṇā Cost (Ethical/Environmental cost) - Low, but non-zero due to nuclear materials
    karuna_cost_value = 0.05 
    
    # Metta Yield (Benefit/Efficiency) - Very high due to high Isp and deep-space access
    metta_yield_value = 1.80 
    
    # A_¬H Factor Assessment: [Energy Waste, Nuclear Leak Risk, Resource Depletion]
    # Note: For H <= 0 to be true, the environmental impact values (E_i) must be non-positive 
    # to represent harm reduction, or the system must assume H starts at 0 and adds positive harm.
    # We will use conceptual positive values here, and test if H is acceptable.
    
    # [E_i (Impact Cost), P_i (Probability)]
    environmental_impact = [0.03, 0.02, 0.05] 
    probability_of_harm   = [0.2,  0.01, 0.5] 

    # 2. Calculation
    shi_result = calculate_shi(upekkha_value, karuna_cost_value, metta_yield_value)
    a_not_h_check, harm_index = check_a_not_h(environmental_impact, probability_of_harm)

    # 3. Output Log for the Counselor
    st.title("🚀 Sustainable Math Counselor: NEP Cruise Test")
    st.subheader("Mission: 1-Year Nuclear Electric Propulsion (NEP) Cruise")

    st.markdown("---")
    
    st.write(f"**SHI Formula Used:** $\\frac{{\\text{{Upekkhā}}}}{{\\text{{Karuṇā Cost}}}} \\times \\text{{Metta Yield}}$")
    st.write(f"**A\_¬H Formula Used:** $\\sum (E_i \\cdot P_i) \\leq 0$ (Harmlessness Index)")
    
    st.markdown("---")

    st.metric(label="Calculated SHI Result (Goal > 1.0)", value=f"{shi_result:.3f}")
    st.metric(label="Harmlessness Index (H) (Goal $\leq$ 0)", value=f"{harm_index:.4f}")

    if a_not_h_check and shi_result > 1.0:
        st.success("✅ **Deterministic Sovereignty Verified!** NEP Cruise meets ethical criteria for sustainability ($\text{SHI} > 1$).")
    elif shi_result > 1.0 and not a_not_h_check:
        st.warning("⚠️ **Warning: SHI Approved, but A_¬H Failure.** The Harmlessness Index is positive. Re-evaluate the cost of risk.")
    elif shi_result <= 1.0:
        st.error("❌ **FAILURE: SHI Constraint Violated.** Ethical yield is too low to justify the cost. Mission is not permissible.")

# To run this in your streamlit_app.py (if you want a button to activate it):
# if st.button('Run Sustainable Math Test (NEP Cruise)'):
#     test_nep_cruise_sustainable_math()

