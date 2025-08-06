import re
import matplotlib.pyplot as plt

# Lists for region 1 and 2 data
max_values = []
avg_goats_r1 = []
avg_goats_r2 = []
avg_tigers_r1 = []
avg_tigers_r2 = []

# Read and parse the file
with open("/Results/2_averagepop_vs_maxpop_after100_starthalf1_zero2/data.txt", "r") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    if "max=" in lines[i] and i + 3 < len(lines):
        max_match = re.search(r"max=(\d+)", lines[i])
        g1_match = re.search(r"Result:\s+([\d.]+)", lines[i])
        g2_match = re.search(r"Result:\s+([\d.]+)", lines[i + 1])
        t1_match = re.search(r"Result:\s+([\d.]+)", lines[i + 2])
        t2_match = re.search(r"Result:\s+([\d.]+)", lines[i + 3])

        if max_match and g1_match and g2_match and t1_match and t2_match:
            max_val = int(max_match.group(1))
            max_values.append(max_val)

            avg_goats_r1.append(float(g1_match.group(1)) / 100)
            avg_goats_r2.append(float(g2_match.group(1)) / 100)
            avg_tigers_r1.append(float(t1_match.group(1)) / 100)
            avg_tigers_r2.append(float(t2_match.group(1)) / 100)

        i += 4
    else:
        i += 1

print("Max Values:", max_values)
print("Average Goats Region 1:", avg_goats_r1)
print("Average Goats Region 2:", avg_goats_r2)
print("Average Tigers Region 1:", avg_tigers_r1)
print("Average Tigers Region 2:", avg_tigers_r2)

# Derived metrics
goat_pct_r1 = [g / m for g, m in zip(avg_goats_r1, max_values)]
goat_pct_r2 = [g / m for g, m in zip(avg_goats_r2, max_values)]
tiger_pct_r1 = [t / m for t, m in zip(avg_tigers_r1, max_values)]
tiger_pct_r2 = [t / m for t, m in zip(avg_tigers_r2, max_values)]

goat_to_tiger_ratio_r1 = [g / t if t > 0 else 0 for g, t in zip(avg_goats_r1, avg_tigers_r1)]
goat_to_tiger_ratio_r2 = [g / t if t > 0 else 0 for g, t in zip(avg_goats_r2, avg_tigers_r2)]

# --- PLOTTING ---

# 1. Average Goats
plt.figure(figsize=(8, 5))
plt.plot(max_values, avg_goats_r1, marker='o', label='Goats Region 1', color='green')
plt.plot(max_values, avg_goats_r2, marker='o', label='Goats Region 2', color='lightgreen')
plt.xlabel("Max Population")
plt.ylabel("Average Goats")
plt.title("Average Goat Population (Two Regions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("goats.pdf", format="pdf")
plt.show()

# 2. Average Tigers
plt.figure(figsize=(8, 5))
plt.plot(max_values, avg_tigers_r1, marker='s', label='Tigers Region 1', color='red')
plt.plot(max_values, avg_tigers_r2, marker='s', label='Tigers Region 2', color='tomato')
plt.xlabel("Max Population")
plt.ylabel("Average Tigers")
plt.title("Average Tiger Population (Two Regions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("tigers.pdf", format="pdf")
plt.show()

# 3. % of Max - Goats and Tigers
plt.figure(figsize=(8, 5))
plt.plot(max_values, goat_pct_r1, marker='o', label="Goats % Max R1", color='green')
plt.plot(max_values, goat_pct_r2, marker='o', label="Goats % Max R2", color='lightgreen')
plt.plot(max_values, tiger_pct_r1, marker='s', label="Tigers % Max R1", color='red')
plt.plot(max_values, tiger_pct_r2, marker='s', label="Tigers % Max R2", color='tomato')
plt.xlabel("Max Population")
plt.ylabel("Percentage of Max")
plt.ylim(0,0.5)
plt.title("Goats and Tigers as % of Max Population (Two Regions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("both.pdf", format="pdf")
plt.show()

# 4. Goats-to-Tigers Ratio
plt.figure(figsize=(8, 5))
plt.plot(max_values, goat_to_tiger_ratio_r1, marker='^', label="Goat/Tiger R1", color='purple')
plt.plot(max_values, goat_to_tiger_ratio_r2, marker='^', label="Goat/Tiger R2", color='violet')
plt.xlabel("Max Population")
plt.ylabel("Goat to Tiger Ratio")
plt.ylim(1, 2)
plt.title("Ratio of Goats to Tigers (Two Regions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("ratio.pdf", format="pdf")
plt.show()
