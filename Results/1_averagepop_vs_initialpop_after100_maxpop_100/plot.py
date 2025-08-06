import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# --- Step 1: Parse the file ---

initial_goats = []
initial_tigers = []
avg_goats = []
avg_tigers = []

with open("/Results/1_averagepop_vs_initialpop_after100_maxpop_100/data_nosim_ss.txt", "r") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    if "goats=" in lines[i] and "tigers=" in lines[i]:
        init_match = re.search(r"goats=(\d+)\s+tigers=(\d+)", lines[i])
        goat_match = re.search(r"Result:\s+([\d.]+)", lines[i])
        tiger_match = re.search(r"Result:\s+([\d.]+)", lines[i+1]) if i+1 < len(lines) else None

        if init_match and goat_match and tiger_match:
            g0 = int(init_match.group(1))
            t0 = int(init_match.group(2))
            goat_val = float(goat_match.group(1))
            tiger_val = float(tiger_match.group(1))

            initial_goats.append(g0)
            initial_tigers.append(t0)
            avg_goats.append(goat_val)
            avg_tigers.append(tiger_val)

        i += 2
    else:
        i += 1

# Convert to DataFrame
df = pd.DataFrame({
    "initial_goats": initial_goats,
    "initial_tigers": initial_tigers,
    "avg_goats": avg_goats,
    "avg_tigers": avg_tigers
})

# Avg Goat Population vs Initial Goats (averaging over initial_tigers)
grouped_goats = df.groupby('initial_goats')['avg_goats'].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.plot(grouped_goats['initial_goats'], grouped_goats['avg_goats'], marker='o', label='Avg Goats', color='green')
plt.xlabel("Initial Goats")
plt.ylabel("Average Goat Population")
plt.title("Avg Goat Population vs Initial Goats (averaged over Initial Tigers)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("avg_goat_population_vs_initial_goats.pdf", format='pdf')
plt.show()

# Avg Goat Population vs Initial Tigers (averaging over initial_goats)
grouped_goats_t = df.groupby('initial_tigers')['avg_goats'].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.plot(grouped_goats_t['initial_tigers'], grouped_goats_t['avg_goats'], marker='o', label='Avg Goats', color='green')
plt.xlabel("Initial Tigers")
plt.ylabel("Average Goat Population")
plt.title("Avg Goat Population vs Initial Tigers (averaged over Initial Goats)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("avg_goat_population_vs_initial_tigers.pdf", format='pdf')
plt.show()

# Avg Tiger Population vs Initial Goats (averaging over initial_tigers)
grouped_tigers = df.groupby('initial_goats')['avg_tigers'].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.plot(grouped_tigers['initial_goats'], grouped_tigers['avg_tigers'], marker='s', label='Avg Tigers', color='red')
plt.xlabel("Initial Goats")
plt.ylabel("Average Tiger Population")
plt.title("Avg Tiger Population vs Initial Goats (averaged over Initial Tigers)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("avg_tiger_population_vs_initial_goats.pdf", format='pdf')
plt.show()

# Avg Tiger Population vs Initial Tigers (averaging over initial_goats)
grouped_tigers_t = df.groupby('initial_tigers')['avg_tigers'].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.plot(grouped_tigers_t['initial_tigers'], grouped_tigers_t['avg_tigers'], marker='s', label='Avg Tigers', color='red')
plt.xlabel("Initial Tigers")
plt.ylabel("Average Tiger Population")
plt.title("Avg Tiger Population vs Initial Tigers (averaged over Initial Goats)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("avg_tiger_population_vs_initial_tigers.pdf", format='pdf')
plt.show()