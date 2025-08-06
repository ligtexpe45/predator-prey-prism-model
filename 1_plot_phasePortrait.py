# Script for one region
# This script reads population data from a file and plots a phase portrait
# showing the relationship between goat and tiger populations over time.
# It saves the plot as a PDF file.

import pandas as pd
import matplotlib.pyplot as plt

# Read your data (assuming it's in a CSV or whitespace-separated file)
df = pd.read_csv("populations.txt", delim_whitespace=True)

goats = df['goats']
tigers = df['tigers']

# Plot phase portrait
plt.figure(figsize=(7, 6))
plt.plot(goats, tigers, '-o', markersize=2, linewidth=0.1, color='blue', alpha=0.3)

# Mark start point
plt.plot(goats.iloc[0], tigers.iloc[0], 'go', label='Start', markersize=6)
plt.plot(goats.iloc[-1], tigers.iloc[-1], 'ro', label='End', markersize=6)

plt.xlabel("Goat population")
plt.ylabel("Tiger population")
plt.title("Phase Portrait from Simulation Data")
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.tight_layout()
plt.savefig("phase_portrait.pdf", format="pdf")
plt.show()
