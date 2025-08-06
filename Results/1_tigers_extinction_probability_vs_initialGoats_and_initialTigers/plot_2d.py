import re
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plot
import numpy as np
import seaborn as sns


# Initialize lists
goats = []
tigers = []
results = []

# --- Read and extract data from the file ---
# IMPORTANT: Make sure this path points to your actual data file.
file_path = "/Results/1_tigers_extinction_probability_vs_initialGoats_and_initialTigers/Data.txt"

try:
    with open(file_path, "r") as file:
        for line in file:
            # This regular expression looks for the pattern: goats=NUMBER, tigers=NUMBER, Result=NUMBER
            match = re.search(r"goats=(\d+)\s+tigers=(\d+)\s+Result:\s+([\d.]+)", line)
            if match:
                g = int(match.group(1))
                t = int(match.group(2))
                r = float(match.group(3))
                goats.append(g)
                tigers.append(t)
                results.append(r)
except FileNotFoundError:
    print(f"Error: The file was not found at the path: {file_path}")
    print("Please update the 'file_path' variable with the correct location of your 'Data.txt' file.")
    # Exit or create empty lists so the rest of the script doesn't crash
    goats, tigers, results = [], [], []

# Check if any data was loaded before proceeding
if not goats:
    print("\nWarning: No data was loaded. The plots will be empty.")

# Create DataFrame
df = pd.DataFrame({
    'goats': goats,
    'tigers': tigers,
    'extinction_prob': results
})

# limit to goats < 200
df = df[df['goats'] < 220]

# Pivot & sort as before
heatmap_data = df.pivot(index='tigers', columns='goats', values='extinction_prob')
heatmap_data = heatmap_data.sort_index().sort_index(axis=1)


# --- PLOTTING METHOD using 'extent' ---
# This tells matplotlib the real-world coordinates for the corners of the data.
# extent=[left, right, bottom, top]
plt.figure(figsize=(12, 8))
plt.imshow(
    heatmap_data,
    aspect='auto',
    cmap='viridis',
    interpolation='bilinear',
    origin='lower',
    extent=[heatmap_data.columns.min(), heatmap_data.columns.max(),
            heatmap_data.index.min(), heatmap_data.index.max()]
)

cbar = plt.colorbar()
cbar.set_label('Extinction Probability')

plt.xlabel("Initial Goats")
plt.ylabel("Initial Tigers")
plt.title("Tiger Extinction Probability")


plt.xticks(rotation=45, ha='right')


plt.tight_layout()
plt.savefig("blended_heatmap.pdf", format="pdf")
plt.show()
