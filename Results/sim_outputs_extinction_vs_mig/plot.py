import matplotlib.pyplot as plt
import pandas as pd
import os
# Define the output directory
OUT_DIR = "./"
#reading the data from the file
df = pd.read_csv(os.path.join(OUT_DIR, "extinction_vs_migration.csv"))

# ─── Plot 1: goats ───────────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
plt.plot(df["migrate"], df["P_extinct_goats"], marker='o', linestyle='-')
plt.xlabel("Migration rate (migrate_g = migrate_t)")
plt.ylabel("P(goats extinct)")
plt.title("Goat Extinction Probability vs. Migration Rate")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "goats_extinction_vs_mig2.pdf"), format='pdf')
plt.show()

# ─── Plot 2: tigers ──────────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
plt.plot(df["migrate"], df["P_extinct_tigers"], marker='o', linestyle='-')
plt.xlabel("Migration rate")
plt.ylabel("Probability of Tigers Extinction")
plt.ylim(0.01, 1.01)  # Ensure y-axis is between 0 and 1
plt.xlim(left=0)  # Ensure x-axis is between
plt.title("Tiger Extinction Probability vs. Migration Rate")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "tigers_extinction_vs_mig2.pdf"), format='pdf')
plt.show()