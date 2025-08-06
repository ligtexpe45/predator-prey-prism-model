import re
import matplotlib.pyplot as plt

# Lists to store extracted data
max_values = []
avg_goats = []
avg_tigers = []

# Read and parse the file
with open("/home/mohamed/PycharmProjects/PythonProject/Results/1_averagepop_vs_maxpop_after100_starthalf/data.txt", "r") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    if "max=" in lines[i]:
        max_match = re.search(r"max=(\d+)", lines[i])
        goat_match = re.search(r"Result:\s+([\d.]+)", lines[i])
        tiger_match = re.search(r"Result:\s+([\d.]+)", lines[i+1]) if i+1 < len(lines) else None

        if max_match and goat_match and tiger_match:
            max_val = int(max_match.group(1))
            goat_val = float(goat_match.group(1)) / 100
            tiger_val = float(tiger_match.group(1)) / 100

            max_values.append(max_val)
            avg_goats.append(goat_val)
            avg_tigers.append(tiger_val)

        i += 2
    else:
        i += 1

# Derived metrics
goat_pct = [g / m for g, m in zip(avg_goats, max_values)]
tiger_pct = [t / m for t, m in zip(avg_tigers, max_values)]
goat_to_tiger_ratio = [g / t if t > 0 else 0 for g, t in zip(avg_goats, avg_tigers)]

# --- PLOTTING ---

# 1. Average Goats
plt.figure(figsize=(8, 5))
plt.plot(max_values, avg_goats, marker='o', color='green')
plt.xlabel("Max Population")
plt.ylabel("Average Goats")
plt.title("Average Goat Population")
plt.grid(True)
plt.tight_layout()
plt.savefig("goats.pdf", format="pdf")
plt.show()

# 2. Average Tigers
plt.figure(figsize=(8, 5))
plt.plot(max_values, avg_tigers, marker='s', color='red')
plt.xlabel("Max Population")
plt.ylabel("Average Tigers")
plt.title("Average Tiger Population")
plt.grid(True)
plt.tight_layout()
plt.savefig("tigers.pdf", format="pdf")
plt.show()

# 3. % of Max - Goats and Tigers
plt.figure(figsize=(8, 5))
plt.plot(max_values, goat_pct, marker='o', label="Goats % of Max", color='green')
plt.plot(max_values, tiger_pct, marker='s', label="Tigers % of Max", color='red')
plt.xlabel("Max Population")
plt.ylabel("Percentage of Max")
plt.ylim(0, 0.5)
plt.title("Goats and Tigers as % of Max Population")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("both.pdf", format="pdf")
plt.show()

# 4. Goats-to-Tigers Ratio
plt.figure(figsize=(8, 5))
plt.plot(max_values, goat_to_tiger_ratio, marker='^', color='purple')
plt.xlabel("Max Population")
plt.ylabel("Goat to Tiger Ratio")
plt.ylim(1, 2)
plt.title("Ratio of Goats to Tigers")
plt.grid(True)
plt.tight_layout()
plt.savefig("ratio.pdf", format="pdf")
plt.show()
