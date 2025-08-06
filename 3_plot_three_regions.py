# Script for three regions
# This script reads population data from a file and plots the dynamics of goats and tigers in three different regions.
# The populations are plotted in three subplots, each representing a different region.
# The script saves the resulting figure as a PDF file.

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("populations.txt", delim_whitespace=True)

# Set up three subplots (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharex=True, sharey=True)

# Region 1
axes[0].plot(df["time"], df["g1"], label="Goats 1", linestyle="-")
axes[0].plot(df["time"], df["t1"], label="Tigers 1", linestyle="-")
axes[0].set_title("Region 1")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Count")
axes[0].legend()
axes[0].grid(True)

# Region 2
axes[1].plot(df["time"], df["g2"], label="Goats 2", linestyle="--")
axes[1].plot(df["time"], df["t2"], label="Tigers 2", linestyle="--")
axes[1].set_title("Region 2")
axes[1].set_xlabel("Time")
axes[1].legend()
axes[1].grid(True)

# Region 3
axes[2].plot(df["time"], df["g3"], label="Goats 3", linestyle=":")
axes[2].plot(df["time"], df["t3"], label="Tigers 3", linestyle=":")
axes[2].set_title("Region 3")
axes[2].set_xlabel("Time")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.suptitle("Population Dynamics in Three Regions", y=1.05)
plt.savefig("three_plots.pdf", format="pdf")
plt.show()
