# Script for Three Regions
# This script runs a PRISM model simulation to analyze the extinction probabilities of goats and tigers
# as a function of migration rates. It generates plots for the extinction probabilities of both species
# and saves the results to a CSV file.

# Simulation Parameters
# Goats1: 300
# Tigers1: 0
# Goats2: 0
# Tigers2: 0
# Goats3: 0
# Tigers3: 300


import subprocess
import os
import re

import numpy as np
import pandas as pd

# ─── CONFIG ────────────────────────────────────────────────────────────────────
PRISM_EXE = "/home/mohamed/Documents/prism-4.8.1-linux64-x86/bin/prism"
MODEL_FILE = "/home/mohamed/Documents/mg_3.prism"
# number of simulation samples per PRISM call
SIM_SAMPLES = 100
# range of migration rates to sweep
mig_rates = np.arange(0.001, 0.05, 0.00145)
# output directory for plots & CSV
OUT_DIR = "/home/mohamed/PycharmProjects/PythonProject/Results/3_extinction_vs_migration_rate"
os.makedirs(OUT_DIR, exist_ok=True)


# ────────────────────────────────────────────────────────────────────────────────


def run_prism_query(prism_exe, model_file, props_file, const_str, simsamp):
    cmd = [
        prism_exe,
        model_file,
        props_file,
        "-sim",
        "-simsamples", str(simsamp),
        "-const", const_str
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    out = proc.stdout.splitlines()

    # Regex to capture all result details
    # Example: Result: 1.0 (+/- 0.0 with probability 0.99; rel err 0.0)
    result_pattern = re.compile(r"Result:\s*([0-9.]+) \(\+/- ([0-9.]+) with probability ([0-9.]+); rel err ([0-9.]+)\)")
    results = []
    for line in out:
        m = result_pattern.search(line)
        if m:
            results.append({
                "value": float(m.group(1)),
                "error": float(m.group(2)),
                "probability": float(m.group(3)),
                "rel_err": float(m.group(4))
            })

    if len(results) != 2:
        raise RuntimeError(f"Expected 2 results, got {results}\nFull PRISM output:\n" + "\n".join(out))
    return results  # [{goats_result_dict}, {tigers_result_dict}]


def main():
    props_file = '/home/mohamed/PycharmProjects/PythonProject/Results/3_extinction_vs_migration_rate/ex.props'

    records = []
    for m in mig_rates:
        const_override = f"migrate_g={m:.6f},migrate_t={m:.6f}"
        print(f"→ running PRISM for migrate = {m:.6f} ...", end=" ")
        try:
            res_goats, res_tigers = run_prism_query(
                PRISM_EXE, MODEL_FILE, props_file, const_override, SIM_SAMPLES
            )
        except Exception as e:
            print("ERROR:", e)
            break
        print(f"  P_goats={res_goats['value']:.4f}, P_tigers={res_tigers['value']:.4f}")

        records.append({
            "migrate": m,
            "P_extinct_goats": res_goats['value'],
            "P_extinct_tigers": res_tigers['value'],
            "goats_error": res_goats['error'],
            "goats_probability": res_goats['probability'],
            "goats_rel_err": res_goats['rel_err'],
            "tigers_error": res_tigers['error'],
            "tigers_probability": res_tigers['probability'],
            "tigers_rel_err": res_tigers['rel_err']
        })

    # put into a DataFrame & save
    df = pd.DataFrame(records)
    df.to_csv(os.path.join(OUT_DIR, "extinction_vs_migration2.csv"), index=False)

if __name__ == "__main__":
    main()