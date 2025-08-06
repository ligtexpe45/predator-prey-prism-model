# This script analyzes the oscillations in goat and tiger populations over time,
# identifies periods of oscillation, and calculates statistics for each period.
# It uses the `find_peaks` function from `scipy.signal` to detect peaks
# in the goat population data, and then computes average populations and durations for each period.
# The results are printed and plotted for visualization.

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load your data
df = pd.read_csv("populations.txt", delim_whitespace=True)

time = df["time"]
goats = df["goats"]
tigers = df["tigers"]

# --- Find peaks in goat population (can also try tigers) ---
peaks, _ = find_peaks(goats, prominence=40, distance=2000)  # Adjust `distance` based on your data

# Calculate periods
periods = time.iloc[peaks].diff().dropna().values  # time between peaks

# Collect stats per period
period_stats = []

for i in range(len(peaks) - 1):
    start_idx = peaks[i]
    end_idx = peaks[i + 1]

    avg_goats = goats.iloc[start_idx:end_idx + 1].mean()
    avg_tigers = tigers.iloc[start_idx:end_idx + 1].mean()
    start_time = time.iloc[start_idx]
    end_time = time.iloc[end_idx]
    duration = end_time - start_time

    period_stats.append({
        "period_index": i + 1,
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "avg_goats": avg_goats,
        "avg_tigers": avg_tigers
    })

# Optional: print summary
for stat in period_stats:
    print(f"Period {stat['period_index']}:")
    print(f"  Time: {stat['start_time']:.2f}–{stat['end_time']:.2f}, Duration: {stat['duration']:.2f}")
    print(f"  Avg Goats: {stat['avg_goats']:.2f}, Avg Tigers: {stat['avg_tigers']:.2f}\n")
    # print goat to tiger ratio
    print(f"  Goat to Tiger Ratio: {stat['avg_goats'] / stat['avg_tigers']:.2f}\n")

# calculate period_stats averages
avg_period_stats = {
    "avg_duration": sum(stat["duration"] for stat in period_stats) / len(period_stats),
    "avg_goats": sum(stat["avg_goats"] for stat in period_stats) / len(period_stats),
    "avg_tigers": sum(stat["avg_tigers"] for stat in period_stats) / len(period_stats)
}
print("Average Period Stats:")
print(f"  Avg Duration: {avg_period_stats['avg_duration']:.2f}")
print(f"  Avg Goats: {avg_period_stats['avg_goats']:.2f}")
print(f"  Avg Tigers: {avg_period_stats['avg_tigers']:.2f}")
print(f"  Avg Goat to Tiger Ratio: {avg_period_stats['avg_goats'] / avg_period_stats['avg_tigers']:.2f}\n")


# Plot population and detected peaks
plt.figure(figsize=(10, 5))
plt.plot(time, goats, label="Goats")
plt.plot(time, tigers, label="Tigers")
plt.plot(time.iloc[peaks], goats.iloc[peaks], 'go', label="Goat Peaks")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.title("Oscillations and Detected Periods")
plt.tight_layout()
plt.show()
