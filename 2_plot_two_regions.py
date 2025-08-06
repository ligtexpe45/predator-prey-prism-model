# Script for Two Regions
# This script reads population data from a file and plots the populations of goats and tigers in two different regions.

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("populations.txt", delim_whitespace=True)

# Set up two subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True)

# Plot for Region 1
axes[0].plot(df["time"], df["g1"], label="Goats 1", color="green")
axes[0].plot(df["time"], df["t1"], label="Tigers 1", color="red")
axes[0].set_title("Region 1")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Count")
axes[0].set_xlim(left=0)  # Set x-axis limit to start from 0
axes[0].legend()
axes[0].grid(True)

# Plot for Region 2
axes[1].plot(df["time"], df["g2"], label="Goats 2", color="green", linestyle="--")
axes[1].plot(df["time"], df["t2"], label="Tigers 2", color="red", linestyle="--")
axes[1].set_title("Region 2")
axes[1].set_xlabel("Time")
axes[1].set_xlim(left=0)  # Set x-axis limit to start from
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.suptitle("Population Dynamics in Two Regions", y=1.05)
plt.savefig("two_plots.pdf", format="pdf")
plt.show()
