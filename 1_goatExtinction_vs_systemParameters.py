# Script for One Region
# This script runs a PRISM model simulation in parallel for different parameter values.
# It sweeps through values of c1 and c3 from 0.1 to 1.0 in increments of 0.1,
# executing the PRISM model with these parameters and printing the results.
# It prints goat extinction probabilities for each combination of c1 and c3.

import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
def main():
    # PRISM model and property files
    PRISM_EXE = "/home/mohamed/Documents/prism-4.8.1-linux64-x86/bin/prism"
    model_file = "/home/mohamed/Documents/model.prism"
    prop_file = "/home/mohamed/Documents/m.props"
    # Number of simulation samples per run
    sim_samples = 100
    # Maximum parallel jobs
    max_workers = 12

    # Generate parameter values 0.1, 0.2, ..., 1.0
    c_values = [round(i * 0.1, 1) for i in range(1, 11)]

    def run_one(c1, c3):
        """
        Runs a single PRISM invocation for given c1 and c3,
        returns lines containing "Result".
        """
        cmd = [
            PRISM_EXE,
            model_file,
            prop_file,
            "-sim",
            f"-simsamples", str(sim_samples),
            "-const", f"c1={c1},c3={c3}"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output_lines = []
        for line in result.stdout.splitlines():
            if "Result" in line:
                output_lines.append(line)
        return c1, c3, output_lines

    # Use ThreadPoolExecutor to run in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_one, c1, c3)
                   for c1 in c_values for c3 in c_values]

        for future in as_completed(futures):
            c1, c3, lines = future.result()
            for line in lines:
                print(f"c1={c1} c3={c3} → {line}")

if __name__ == "__main__":
    main()
