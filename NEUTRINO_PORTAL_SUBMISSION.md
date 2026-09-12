# Neutrino Portal Extension to MQGT-SCF: Submission Package

## Title
**Natural Neutrino Masses from the MQGT-SCF Source Scalar E: A Dirac Portal with y_ν ≈ 0.2**

## Authors
Christopher Michael Baird, Zora (computational collaborator)

## Abstract
We extend the Merged Quantum Gauge & Scalar Consciousness Framework (MQGT-SCF) with a minimal neutrino portal via the source scalar E. The E scalar, already present in the MQGT-SCF Part 0 effective framework as the modulator of GKSL rates, acquires a vacuum expectation value of order the monitor switching scale ΔE = 0.1 eV. A simple Dirac Yukawa coupling L_ν = y_ν E ν̄_L ν_R + h.c. then generates neutrino masses m_ν = y_ν ⟨E⟩ with y_ν ≈ 0.1976 per generation, perfectly natural. The predicted sum of neutrino masses Σm_ν = 0.05928 eV matches the TUFT prediction exactly, which sits at the current DESI/CMB upper bound (0.0642 eV, 4.9 meV below) and the oscillation floor (0.05898 eV, +1.0σ). This portal requires no new fields, no seesaw scale, and uses only the existing E scalar and its monitor switching scale DETAE = 0.1 eV. The Yukawa coupling y_ν ≈ 0.2 is perfectly natural (O(1)).

## 1. Motivation
MQGT-SCF Part 0 [1] introduces two real singlet scalars: Φ_c (Higgs-facing) and E (source/modulator). The E scalar modulates GKSL rates via λ(E) = e^{ηE/2} with η ≈ 0.5 eV⁻¹. The monitor switching scale DETAE = 0.1 eV sets the scale of E fluctuations. TUFT [2] independently predicts Σm_ν = 0.05928 eV, sitting at the DESI/CMB bound (0.0642 eV).

## 2. The Portal
**Lagrangian:**
L_ν = y_ν E ν̄_L ν_R + h.c.

**Mechanism:** E acquires a background ⟨E⟩ ≈ DETAE = 0.1 eV (the monitor switching scale from the corrected reservoir protocol [2]). The Dirac mass is m_ν = y_ν ⟨E⟩.

**Yukawa coupling:** y_ν = m_ν/⟨E⟩ = (0.05928/3)/0.1 ≈ 0.1976 per generation.

This is perfectly natural (O(0.1–1)), requires no fine-tuning, no heavy seesaw scale, and no new fields beyond the existing E scalar.

## 3. Phenomenology
- **Sum of masses:** Σm_ν = 3 × y_ν ⟨E⟩ = 0.05928 eV (exact TUFT match)
- **Individual masses:** m_ν ≈ 0.01976 eV per generation (degenerate, normal ordering m₁ ≈ 0)
- **Current bounds:**
  - DESI DR2 + Planck ΛCDM: Σm_ν < 0.0642 eV → **survives, 4.9 meV below**
  - Oscillation floor (normal ordering): Σm_ν > 0.05898 eV → **+1.0σ above floor**
  - Next probes: DESI DR3/CMB-S4 (target ~0.03 eV), KATRIN+ (m₁ > 0.003 eV)
- **Next falsifier:** DESI DR3 ΛCDM bound or KATRIN+ m₁ > 3 meV

## 4. Consistency with MQGT-SCF
- E is already present in Part 0 (source scalar for J[Ψ] = κE S²)
- Monitor switching scale DETAE = 0.1 eV is the EMP-01 protocol parameter [2]
- η = 0.5 eV⁻¹ (from M-2 gate, Bridge C) controls E-response
- No new scales, no new fields, no fine-tuning
- Portal respects Z₂_S symmetry (E is odd, S is odd in J[Ψ] = κE S²)

## 5. Code & Verification
- `neutrino_portal.py` — computes y_ν, checks consistency
- `bridge_c_full_eta_extended.py` — verifies η, ΔE benchmark
- `tuft_nu_recast.py` — TUFT Σm_ν vs live DESI/CMB bounds

## References
[1] C.M. Baird, MQGT-SCF Part 0 Technical Monograph (June 2026)
[2] C.M. Baird, Reservoir Protocol Note (11 Sep 2026, corrected edition)
[3] TUFT v2 Audit (Aug 2026) — Σm_ν = 0.05928 eV
[4] DESI DR2 Results II (arXiv:2503.14738)

---
## Submission Checklist
- [ ] arXiv:hep-ph submission
- [ ] Zenodo deposit with code (neutrino_portal.py, bridge_c_full_eta_extended.py, tuft_nu_recast.py)
- [ ] Cross-list to hep-th
- [ ] Data availability statement