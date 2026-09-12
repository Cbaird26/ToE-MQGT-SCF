#!/usr/bin/env python3
"""
Generate synthetic EMP-01 protocol data for testing the analyzer.
"""
import csv
import numpy as np

# Protocol parameters
GAMMA0 = 1000.0       # s^-1
T = 1e-4              # s
ETA = 0.5             # true eta (large for test)
DETAE = 0.1           # eV (large DeltaE for test)
Z = 5

# Model: alpha = 0.5 * GAMMA0 * T * eta * DeltaE (linearized)
# For N2: DeltaE = 0.1 eV, eta = 0.5 -> alpha = 0.5 * 1000 * 1e-4 * 0.5 * 0.1 = 2.5e-3
# Required N_tot for z=5: 4*z^2 / alpha^2 = 100 / 6.25e-6 = 1.6e7

def generate_block(block_idx, true_eta=0.1, noise=True):
    """Generate one block of N0/N1/N2/N3."""
    Gamma0 = 1000.0
    T = 1e-4
    
    # N0: monitor-off, baseline
    # N1: monitor-on, DeltaE=0 (null)
    # N2: monitor-on, DeltaE = 0.01 eV (signal)
    # N3: monitor-on, DeltaE=0, T_bath changed (bath calibration)
    
    DeltaE_N2 = 0.1  # eV
    eta_true = 0.5
    
    # True alpha values
    alpha_N0 = 0.0  # coupler off
    alpha_N1 = 0.0  # DeltaE=0
    alpha_N2 = 0.5 * 1000 * 1e-4 * 0.5 * 0.1  # = 2.5e-3
    alpha_N3 = 0.0  # DeltaE=0, bath change
    
    # Required N_tot for z=5
    z = 5
    alpha_signal = 0.5 * 1000 * 1e-4 * 0.5 * 0.1
    N_req = 4 * z**2 / (alpha_signal)**2  # ~1.6e7
    
    # Use N_tot that meets requirement (rounded up)
    N_tot = int(np.ceil(N_req))  # ~1.6e7
    
    sigma_stat = 1 / np.sqrt(N_tot)
    
    rows = []
    # N0: coupler off, baseline off
    V_N0 = 1.0
    V_N0_meas = V_N0 + np.random.normal(0, 1/np.sqrt(N_tot)) if noise else V_N0
    rows.append({
        'row_id': 'N0',
        'coupler': 0,
        'E_L': 0.0,
        'E_R': 0.0,
        'E_unit': 'eV',
        'T': 1e-4,
        'T_bath': 300.0,
        'N_tot': N_tot,
        'V_hat': V_N0_meas,
        'V_hat_err': 1/np.sqrt(N_tot),
        'baseline': 'off',
        'phase_scanned': 1
    })
    
    # N1: coupler on, DeltaE=0, baseline on
    V_N1 = 1.0
    V_N1_meas = V_N1 + np.random.normal(0, 1/np.sqrt(N_tot)) if noise else V_N1
    rows.append({
        'row_id': 'N1',
        'coupler': 1,
        'E_L': 0.0,
        'E_R': 0.0,
        'E_unit': 'eV',
        'T': 1e-4,
        'T_bath': 300.0,
        'N_tot': N_tot,
        'V_hat': V_N1_meas,
        'V_hat_err': 1/np.sqrt(N_tot),
        'baseline': 'on',
        'phase_scanned': 1
    })
    
    # N2: coupler on, DeltaE=0.1, baseline on
    alpha_N2 = 0.5 * 1000 * 1e-4 * 0.5 * 0.1  # 2.5e-3
    V_N2 = np.exp(-alpha_N2)
    V_N2_meas = V_N2 + np.random.normal(0, 1/np.sqrt(N_tot)) if noise else V_N2
    rows.append({
        'row_id': 'N2',
        'coupler': 1,
        'E_L': 0.1,
        'E_R': 0.0,
        'E_unit': 'eV',
        'T': 1e-4,
        'T_bath': 300.0,
        'N_tot': N_tot,
        'V_hat': V_N2_meas,
        'V_hat_err': 1/np.sqrt(N_tot),
        'baseline': 'on',
        'phase_scanned': 1
    })
    
    # N3: coupler on, DeltaE=0, T_bath changed
    V_N3 = 1.0
    V_N3_meas = V_N3 + np.random.normal(0, 1/np.sqrt(N_tot)) if noise else V_N3
    rows.append({
        'row_id': 'N3',
        'coupler': 1,
        'E_L': 0.1,   # common-mode E (non-zero, equal)
        'E_R': 0.1,   # DeltaE = 0
        'E_unit': 'eV',
        'T': 1e-4,
        'T_bath': 310.0,  # changed bath temp
        'N_tot': N_tot,
        'V_hat': V_N3_meas,
        'V_hat_err': 1/np.sqrt(N_tot),
        'baseline': 'on',
        'phase_scanned': 1
    })
    
    return rows

def main():
    np.random.seed(42)
    all_rows = []
    
    # Generate 3 interleaved blocks
    for i in range(3):
        block_rows = generate_block(i)
        for r in block_rows:
            r['block'] = i
        all_rows.extend(block_rows)
    
    # Write CSV
    fieldnames = ['row_id', 'coupler', 'E_L', 'E_R', 'E_unit', 'T', 'T_bath',
                  'N_tot', 'V_hat', 'V_hat_err', 'baseline', 'phase_scanned', 'block']
    
    with open('emp01_synthetic.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print("Generated emp01_synthetic.csv with 3 blocks (12 rows)")
    print("Columns:", list(all_rows[0].keys()))

if __name__ == '__main__':
    main()