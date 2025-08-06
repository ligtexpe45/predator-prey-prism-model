import pandas as pd
import matplotlib.pyplot as plt

# read csv file
df_results = pd.read_csv('2_synchronization_vs_migration/sim_outputs_corr_vs_mig/corr_vs_migration.csv')

# Plot correlation vs migrate parameter
plt.figure(figsize=(8, 5))
plt.plot(df_results['migrate'], df_results['mean_corr'], 'o-')
plt.xlabel('Migration Rate')
plt.ylabel('Mean Pearson r (g1 vs g2)')
plt.title('Synchronization vs Migration Rate')
plt.grid(True)
plt.tight_layout()
plt.savefig('/home/mohamed/PycharmProjects/PythonProject/sim_outputs_corr_vs_mig2/corr_vs_migration.pdf', format='pdf')
plt.show()