# Predator-Prey Prism Model

This repository contains Python scripts and simulation results for modeling and analyzing predator-prey dynamics (goats and tigers) in one, two, or three regions. The project focuses on population dynamics, extinction probabilities, and synchronization between regions using statistical and visualization tools.

**Naming convention:** Files and folders starting with **1_** are for one region, **2_** for two regions, and **3_** for three regions.

## Features
- Simulate population dynamics of goats and tigers in multiple regions
- Analyze extinction probabilities and population averages
- Compute synchronization (Pearson correlation) between regions
- Visualize results with publication-ready plots

## Installation
1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd PythonProject
   ```
2. Install required Python packages:
   ```bash
   pip install pandas matplotlib scipy
   ```

## Usage
Run the analysis scripts from the project root. Example:
```bash
python 1_plot.py
python 2_plot_sync.py
python 3_plot_three_regions.py
```

Each script reads simulation data (e.g., `populations.txt`) and generates plots in the Results directory.

## Main Scripts

### One Region
- **1_plot.py**: Plots goat and tiger populations over time for a single region.
- **1_plot_period.py**: Analyzes and plots population periods for one region.
- **1_plot_phasePortrait.py**: Plots phase portraits for one region.

### Two Regions
- **2_plot_sync.py**: Computes and plots synchronization (Pearson correlation) between goat populations in two regions using a sliding window.
- **2_calculate_sync_pearson.py**: Calculates overall Pearson correlation between two goat populations.
- **2_both_goats_graph.py**: Plots goat populations for two regions.
- **2_both_tigers_graph.py**: Plots tiger populations for two regions.
- **2_plot_two_regions.py**: Plots population dynamics for two regions.

### Three Regions
- **3_plot_three_regions.py**: Visualizes population dynamics for goats and tigers in three regions using subplots.

Other scripts in the repository provide additional analysis and plotting capabilities. Refer to each script for its specific functionality and usage.

## Results Directory Structure

### One Region
- **1_averagepop_vs_initialpop_after100_maxpop_100/**: Plots and data for average populations vs initial populations.
- **1_averagepop_vs_maxpop_after100_starthalf/**: Plots and data for average populations vs max population (start half of max population).
- **1_extinction_vs_systemParameters/**: Extinction probability analysis and plots.
- **1_One Region Simulation/**: Simulation outputs and plots for one region.
- **1_Population_vs_systemParameters/**: Population vs system parameter analysis and plots.
- **1_tigers_extinction_probability_vs_initialGoats_and_initialTigers/**: Extinction probability heatmaps and data.
- **1_Goats and Tigers extinction probability vs maxPop/**: Extinction probability vs max population for goats and tigers.

### Two Regions
- **2_averagepop_vs_maxpop_after100_starthalf1_zero2/**: Plots and data for average populations vs max population region 1 start at half of max population, region 2 starts at zero).
- **2_synchronization_vs_migration/**: Synchronization analysis and plots for migration scenarios.
- **2_Two Regions Simulations/**: Simulation outputs and plots for two regions.
- **2_Goats and Tigers extinction probability vs maxPop/**: Extinction probability vs max population for goats and tigers in two regions.

### Three Regions
- **3_extinction_vs_migration_rate/**: Extinction probability vs migration rate analysis and plots for three regions.

Other subfolders contain PDF plots, data files, and additional scripts for each scenario. Refer to each folder for its specific results and analysis.

## PRISM Model Files and Properties

The following PRISM model files define the system dynamics for different region scenarios:

- **model.prism**: PRISM model for one region.
- **mg.prism**: PRISM model for two regions.
- **mg_3.prism**: PRISM model for three regions.

The main properties used for analysis are defined in **prop.props**. Additional or scenario-specific properties can be found in other `.props` files or in data files within the Results subdirectories.

## License
This project is for academic and research purposes. Please cite appropriately if used in publications.

## Contact
For questions or collaboration, please contact the repository owner.
