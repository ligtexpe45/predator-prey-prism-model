# Script for Two regions
# This script reads population data from a file and plots the populations of two goat groups over time.
# The populations are plotted in a single graph, and the resulting figure is saved as a PDF file.

import pandas as pd
import matplotlib.pyplot as plt

# Load data from the file
df = pd.read_csv("populations.txt", delim_whitespace=True)

# Plot all populations in a single graph
plt.figure(figsize=(10, 6))
plt.plot(df["time"], df["g1"], label="Goats 1", color="green")
plt.plot(df["time"], df["g2"], label="Goats 2", color="red")

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Goats in Both Regions Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xlim(left=0)
plt.savefig("goats.pdf", format="pdf")
plt.show()
