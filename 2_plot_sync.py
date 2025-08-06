# script for two regions
# This script reads goat population data from a file, computes the synchronization between two goat populations over time,
# and plots the correlation results with a sliding window approach.
# It uses Pearson correlation to measure the synchronization and visualizes the results with Matplotlib.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr

def read_data(file_path):
    # Read tabular data while skipping any header comments or blank lines
    df = pd.read_csv(file_path, delim_whitespace=True)
    return df

def sliding_sync(time, series1, series2, window_size=50, step=5):
    sync_times = []
    sync_corrs = []

    for start in range(0, len(time) - window_size, step):
        end = start + window_size
        t_win = time[start:end]
        s1_win = series1[start:end]
        s2_win = series2[start:end]

        if len(s1_win) < window_size or len(s2_win) < window_size:
            continue

        r, _ = pearsonr(s1_win, s2_win)
        sync_times.append(t_win[len(t_win) // 2])  # mid-time of window
        sync_corrs.append(r)

    return np.array(sync_times), np.array(sync_corrs)

def main():
    # Replace this with your actual file path
    file_path = "/home/mohamed/PycharmProjects/PythonProject/populations.txt"

    df = read_data(file_path)

    # Extract time and goat populations
    time = df["time"].values
    g1 = df["g1"].values
    g2 = df["g2"].values

    # Compute synchronization between goat populations
    sync_times, sync_corrs = sliding_sync(time, g1, g2, window_size=100000, step=10000)

    # Calculate Pearson correlation over the whole data
    pearson_corr, pearson_p = pearsonr(g1, g2)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(sync_times, sync_corrs, color='tab:blue', label='g1 vs g2 correlation (windowed)')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.axhline(pearson_corr, color='red', linestyle='--', linewidth=1.5, label=f'Correlation (global): {pearson_corr:.3f}')
    plt.xlabel("Time")
    plt.ylabel("Correlation")
    plt.title("Synchronization of Goat Populations (g1 vs g2) Over Time")
    plt.ylim(-1.05, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("goat_sync_over_time.pdf", format="pdf")
    plt.show()

if __name__ == "__main__":
    main()
