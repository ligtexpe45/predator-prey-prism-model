import re
import pandas as pd
import matplotlib.pyplot as plt

# File paths (adjust as needed)
goat_file = '/Results/Population_vs_systemParameters/goat_vs_rate'
tiger_file = '/Results/Population_vs_systemParameters/tiger_vs_rate'

# Regex to parse lines
pattern = re.compile(
    r"c1=(?P<c1>[\d.]+)\s+"
    r"c3=(?P<c3>[\d.]+)\s+→\s+Result:\s*(?P<res>[\d.]+)"
)

def load_and_normalize(file_path):
    records = []
    with open(file_path, 'r') as f:
        for line in f:
            m = pattern.search(line)
            if m and float(m.group('c1')) >= 0.5 and float(m.group('c3')) >= 0.4:
                records.append({
                    'c1': float(m.group('c1')),
                    'c3': float(m.group('c3')),
                    'value': float(m.group('res')) / 400.0
                })
    return pd.DataFrame(records)

# Load data
df_goat = load_and_normalize(goat_file)
df_tiger = load_and_normalize(tiger_file)

# Pivot to matrices
pivot_goat = df_goat.pivot(index='c1', columns='c3', values='value')
pivot_tiger = df_tiger.pivot(index='c1', columns='c3', values='value')
ratio = pivot_goat / pivot_tiger

# Improved plotting function with dynamic text color
from matplotlib.colors import Normalize

def plot_with_annotations(ax, data, title, cmap):
    norm = Normalize(vmin=data.min().min(), vmax=data.max().max())
    im = ax.imshow(data.values, origin='lower', aspect='auto', cmap=cmap, norm=norm)
    ax.set_title(title)
    ax.set_xlabel('Tiger death rate')
    ax.set_ylabel('Goat birth rate')
    # tick labels
    ax.set_xticks(range(len(data.columns)))
    ax.set_xticklabels([f"{v:.1f}" for v in data.columns], rotation=45)
    ax.set_yticks(range(len(data.index)))
    ax.set_yticklabels([f"{v:.1f}" for v in data.index])

    # annotate each cell with contrasting text
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            val = data.values[i, j]
            # choose white or black based on background luminance
            color = 'white' if norm(val) < 0.5 else 'black'
            ax.text(j, i, f"{val:.2f}",
                    ha='center', va='center', fontsize=8, color=color)
    return im

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
levels_cmap = 'viridis'  # perceptually uniform

# Goat
im0 = plot_with_annotations(axes[0], pivot_goat, 'Goat Population', levels_cmap)
plt.colorbar(im0, ax=axes[0], label='Goats')

# Tiger
im1 = plot_with_annotations(axes[1], pivot_tiger, 'Tiger Population', levels_cmap)
plt.colorbar(im1, ax=axes[1], label='Tigers')

# Ratio
im2 = plot_with_annotations(axes[2], ratio, 'Goat/Tiger Population Ratio', levels_cmap)
plt.colorbar(im2, ax=axes[2], label='Goat/Tiger')

plt.tight_layout()
plt.savefig('pop_vs_rate.pdf', format='pdf')
plt.show()
