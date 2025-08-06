# Script for Two regions
# This script runs a series of simulations using Prism to analyze the effect of migration rates on synchronization between two populations.
# It runs multiple simulations for each migration rate, calculates the Pearson correlation between the two populations,
# and plots the average correlation against the migration rate. The results are saved to a CSV file.

import subprocess
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Configuration
prism_executable = "/home/mohamed/Documents/prism-4.8.1-linux64-x86/bin/prism"
model_file = "/home/mohamed/Documents/mg.prism"
sim_path = 900000
output_dir = "./sim_outputs_corr_vs_mig_allhalf2"
total_runs = 10  # replicates per parameter value

# Parameter range for migrate_g (and migrate_t will use the same value)
migrate_vals = np.arange(0.001, 0.041, 0.00145)  # 0.01 to 0.04015 inclusive, step 0.00145

# Prepare output list
results = []  # stores dicts: {'migrate': val, 'mean_corr': corr}

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

for m in migrate_vals:
    run_corrs = []
    # Build parameter override argument for Prism: both params together
    param_arg = f"migrate_g={m},migrate_t={m}"

    for run_id in range(1, total_runs + 1):
        out_file = os.path.join(output_dir, f"pop_m{m:.6f}_{run_id}.txt")
        cmd = [prism_executable,
               model_file,
               "-const", param_arg,
               "-simpath", str(sim_path),
               out_file]
        subprocess.run(cmd, check=True)

        # Read output and compute Pearson r
        df = pd.read_csv(out_file, delim_whitespace=True)
        corr, _ = pearsonr(df['g1'].values, df['g2'].values)
        run_corrs.append(corr)

    # Average correlation for this migrate value
    mean_corr = np.mean(run_corrs)
    results.append({'migrate': m, 'mean_corr': mean_corr})

# Convert to DataFrame
df_results = pd.DataFrame(results)

# Plot correlation vs migrate parameter
plt.figure(figsize=(8, 5))
plt.plot(df_results['migrate'], df_results['mean_corr'], 'o-')
plt.xlabel('migrate_g = migrate_t')
plt.ylabel('Mean Pearson r (g1 vs g2)')
plt.title('Synchronization vs Migration Rate')
plt.grid(True)
plt.tight_layout()
plt.show()

# Save results to CSV
df_results.to_csv(os.path.join(output_dir, 'corr_vs_migration.csv'), index=False)
