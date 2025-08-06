# Script for Two regions
# Calculate synchronization between two goat populations using Pearson correlation

import pandas as pd
from scipy.stats import pearsonr

def read_data(file_path):
    # Read tabular data while skipping any header comments or blank lines
    df = pd.read_csv(file_path, delim_whitespace=True)
    return df

def main():
    # Replace this with your actual file path
    file_path = "populations.txt"

    df = read_data(file_path)

    # Extract time and goat populations
    time = df["time"].values
    g1 = df["g1"].values
    g2 = df["g2"].values

    # Compute synchronization between goat populations
    coor = pearsonr(g1, g2)

    print(f"Pearson correlation between g1 and g2: {coor[0]:.4f}")

if __name__ == "__main__":
    main()
