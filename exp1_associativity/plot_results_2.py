import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Data
try:
    df = pd.read_csv('final_results.csv')
except FileNotFoundError:
    print("Error: final_results.csv not found!")
    exit()

# 2. Map labels to numbers for sorting
size_map = {
    '16KB': 16, '32KB': 32, '64KB': 64, '128KB': 128, 
    '256KB': 256, '512KB': 512, '1MB': 1024, '2MB': 2048,
    '4MB': 4096, '8MB': 8192, '16MB': 16384, '32MB': 32768
}

df['Size_Val'] = df['Size'].map(size_map)
df = df.sort_values(by=['Size_Val', 'Associativity'])

# 3. Plotting Configuration
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12, 'font.family': 'sans-serif'})

def create_plot(y_col, y_label, title, filename, log_scale=False):
    plt.figure(figsize=(12, 6))
    
    sns.lineplot(data=df, x='Size', y=y_col, hue='Associativity', 
                 palette='tab10', marker='o', linewidth=2.5)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.ylabel(y_label, fontsize=14)
    plt.xlabel("Cache Size", fontsize=14)
    plt.legend(title='Associativity', title_fontsize=12, loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save
    plt.savefig(filename, dpi=300)
    print(f"Saved {filename}")
    plt.close()

print("Generating plots for 16KB to 32MB...")

# Plot 1: Access Time
create_plot('Access_Time(ns)', 'Access Time (ns)', 
            'Global Latency Trend: The "Associativity Convergence"', 'plot_latency_full.png')

# Plot 2: Energy
create_plot('Read_Energy(nJ)', 'Read Energy (nJ)', 
            'Global Energy Trend: The Cost of Associativity', 'plot_energy_full.png')

# Plot 3: Area
create_plot('Area(mm2)', 'Area (mm^2)', 
            'Global Area Trend', 'plot_area_full.png')

print("Done! Open 'plot_latency_full.png' to see the magic.")