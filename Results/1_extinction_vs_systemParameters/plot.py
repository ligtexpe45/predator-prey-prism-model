import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# Read and parse the data file
# Please ensure this file path is correct for your system.
file_path = '/Results/1_extinction_vs_systemParameters/ex_vs_rate.txt'
data = []
# This pattern will extract the c1, c3, and result values from each line.
pattern = re.compile(r"c1=(?P<c1>[\d.]+) c3=(?P<c3>[\d.]+).*Result:\s*(?P<res>[\d.]+)")

try:
    with open(file_path, 'r') as f:
        for line in f:
            m = pattern.search(line)
            if m:
                data.append({
                    'c1': float(m.group('c1')),
                    'c3': float(m.group('c3')),
                    'ext_prob': float(m.group('res'))
                })
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
    print("Using sample data to generate the plot.")
    # Generate sample data if the file is not found
    for c1_val in np.arange(0.1, 1.1, 0.1):
        for c3_val in np.arange(0.1, 1.1, 0.1):
            data.append({
                'c1': round(c1_val, 1),
                'c3': round(c3_val, 1),
                'ext_prob': round(np.random.rand(), 2)
            })


# Create DataFrame and pivot into matrix form
df = pd.DataFrame(data)
pivot = df.pivot(index='c1', columns='c3', values='ext_prob')

# --- Plotting Section ---
fig, ax = plt.subplots(figsize=(10, 8))

# Normalize data for color mapping and text color decisions
# This ensures the colors are scaled correctly between the min and max values.
norm = Normalize(vmin=pivot.min().min(), vmax=pivot.max().max())
cmap = 'viridis' # A perceptually uniform colormap

# Plot heatmap using imshow. We don't use 'extent' here.
# Instead, we'll manually set the tick labels later.
im = ax.imshow(
    pivot.values,
    origin='lower',
    aspect='auto',
    cmap=cmap,
    norm=norm
)

# Set axis labels and title
ax.set_xlabel('Tiger death rate', fontsize=12)
ax.set_ylabel('Goat birth rate', fontsize=12)
ax.set_title('Tiger Extinction Probability', fontsize=14, fontweight='bold')

# Set custom tick labels to match the data values
ax.set_xticks(np.arange(len(pivot.columns)))
ax.set_xticklabels([f"{v:.1f}" for v in pivot.columns])
ax.set_yticks(np.arange(len(pivot.index)))
ax.set_yticklabels([f"{v:.1f}" for v in pivot.index])

# Rotate the x-axis labels for better readability if they overlap
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
# This is the key part for centering the text in each cell.
# for i in range(len(pivot.index)):
#     for j in range(len(pivot.columns)):
#         value = pivot.values[i, j]
#         # Choose text color (white or black) based on the background
#         # cell color for better contrast and readability.
#         text_color = 'white' if norm(value) < 0.5 else 'black'
#         ax.text(
#             j, i, f"{value:.2f}",
#             ha="center", va="center",
#             color=text_color,
#             fontsize=8
#         )

# Add a colorbar to show the mapping of colors to values
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Extinction Probability', rotation=270, labelpad=15, fontsize=12)

# Adjust layout to prevent labels from being cut off
fig.tight_layout()

# Save the figure and show the plot
plt.savefig('ex_vs_rate_annotated.pdf', format='pdf')
plt.show()
