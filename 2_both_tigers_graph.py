# Script for Two regions
# This script reads population data from a file and plots the populations of two tiger groups over time.
# The populations are plotted in a single graph, and the resulting figure is saved as a PDF file.

import pandas as pd
import matplotlib.pyplot as plt

# Load data from the file
df = pd.read_csv("/home/mohamed/PycharmProjects/PythonProject/populations.txt", delim_whitespace=True)

# Plot all populations in a single graph
plt.figure(figsize=(10, 6))
plt.plot(df["time"], df["t1"], label="Tigers 1", color="green")
plt.plot(df["time"], df["t2"], label="Tigers 2", color="red")

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Tigers in Both Regions Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("tigers.pdf", format="pdf")
plt.show()
