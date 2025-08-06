# # Script for One region
# This script reads a data file containing populations of goats and tigers over time,
# and generates a plot showing the counts of both species over time.
# The plot is saved as a PDF file.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('populations.txt', delim_whitespace=True)

xLabel = 'time'

plt.figure(figsize=(8,5))
plt.plot(df[xLabel], df['goats'],
         lw=0.8, alpha=0.6,
         label='Goats')
plt.plot(df[xLabel], df['tigers'],
         lw=0.8, alpha=0.6,
         label='Tigers')
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('Goats and Tigers Counts Over Time')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.savefig('plot.pdf', format='pdf')
plt.show()
