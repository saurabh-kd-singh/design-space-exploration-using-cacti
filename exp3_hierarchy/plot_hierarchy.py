import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
try:
    df = pd.read_csv('results_hierarchy.csv')
except FileNotFoundError:
    print("Error: File not found!")
    exit()

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

# 2. Function for Bar Plots
def create_bar_plot(y_col, y_label, title, filename, log_scale=False, color='tab:blue'):
    plt.figure(figsize=(8, 6))
    
    # Bar Plot
    sns.barplot(data=df, x='Level', y=y_col, palette=[color])
    
    if log_scale:
        plt.yscale('log')
        
    plt.title(title, fontsize=14, fontweight='bold')
    plt.ylabel(y_label, fontsize=12)
    plt.xlabel("") # No need for X label, the categories are clear
    
    # Add the numbers on top of the bars
    for index, row in df.iterrows():
        val = row[y_col]
        # Format text
        txt = f"{val:.3f}" if val < 10 else f"{val:.1f}"
        plt.text(index, val, txt, color='black', ha="center", va="bottom", fontweight='bold')

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f"Saved {filename}")
    plt.close()

print("Generating Hierarchy Plots...")

# Plot 1: Latency (Speed)
create_bar_plot('Latency(ns)', 'Access Time (ns)', 
                'Why we need L1: Latency Comparison', 'plot_hier_latency.png', color='#1f77b4')

# Plot 2: Leakage (The Heat Problem) - LOG SCALE
create_bar_plot('Leakage_Power(mW)', 'Leakage Power (mW) [Log Scale]', 
                'Why we need L2: The Leakage Fix', 'plot_hier_leakage.png', log_scale=True, color='#d62728')

# Plot 3: Area (The Cost)
create_bar_plot('Area(mm2)', 'Area (mm^2)', 
                'Why L3 is Expensive: Physical Size', 'plot_hier_area.png', color='#2ca02c')

print("Done!")