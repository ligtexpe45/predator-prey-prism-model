import re
import matplotlib.pyplot as plt

# Path to your file containing the data
file_path = "data.txt"

# Regex patterns
pattern = re.compile(
    r"max=(?P<max>\d+)\s+Result:\s+(?P<result>[\d.]+)"
)

# Containers for parsed data
tigers_max, tigers_res = [], []
goats_max, goats_res = [], []

current_section = None

with open(file_path, "r") as f:
    for line in f:
        # Detect which section we are in
        if "P=? [ F<=100 (t1 + t2 = 0) ]" in line:
            current_section = "tigers"
            continue
        elif "P=? [ F<=100 (g1 + g2 = 0) ]" in line:
            current_section = "goats"
            continue

        match = pattern.search(line)
        if match and current_section:
            max_val = int(match.group("max"))
            res_val = float(match.group("result"))
            if current_section == "tigers":
                tigers_max.append(max_val)
                tigers_res.append(res_val)
            elif current_section == "goats":
                goats_max.append(max_val)
                goats_res.append(res_val)

# --- Plotting ---

plt.figure(figsize=(8, 5))
plt.plot(tigers_max, tigers_res, marker="o", color="red")
plt.title("Tigers Extinction Probability vs Max Population")
plt.xlabel("Max Population")
plt.ylabel("Probability")
plt.ylim(0, 1)
plt.grid(True)
plt.savefig("tigers.pdf", format='pdf')

plt.figure(figsize=(8, 5))
plt.plot(goats_max, goats_res, marker="o", color="blue")
plt.title("Goats Extinction Probability vs Max Population")
plt.xlabel("Max Population")
plt.ylabel("Probability")
plt.ylim(0, 1)
plt.grid(True)
plt.savefig("goats.pdf", format='pdf')

plt.show()
