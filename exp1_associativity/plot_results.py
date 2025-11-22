import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Data
df = pd.read_csv('final_results.csv')

# Convert Size strings (16KB) to Numbers for sorting, then back to labels
size_map = {'16KB': 16, '32KB': 32, '64KB': 64, '128KB': 128, 
            '256KB': 256, '512KB': 512, '1MB': 1024, '2MB': 2048}
df['Size_Val'] = df['Size'].map(size_map)
df = df.sort_values(by=['Size_Val', 'Associativity'])

# Set the visual style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12, 'font.family': 'sans-serif'})

# Function to create a plot
def create_plot(y_col, y_label, title, filename):
    plt.figure(figsize=(10, 6))
    
    # Create the line plot
    sns.lineplot(data=df, x='Size', y=y_col, hue='Associativity', 
                 palette='tab10', marker='o', linewidth=2.5)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.ylabel(y_label, fontsize=14)
    plt.xlabel("Cache Size", fontsize=14)
    plt.legend(title='Associativity', title_fontsize=12)
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Save
    plt.savefig(filename, dpi=300)
    print(f"Saved {filename}")
    plt.close()

# 2. Generate the 3 Charts
print("Generating plots...")

# Plot 1: Access Time
create_plot('Access_Time(ns)', 'Access Time (ns)', 
            'Impact of Associativity on Cache Latency', 'plot_latency.png')

# Plot 2: Energy
create_plot('Read_Energy(nJ)', 'Read Energy per Access (nJ)', 
            'Impact of Associativity on Dynamic Energy', 'plot_energy.png')

# Plot 3: Area
create_plot('Area(mm2)', 'Area (mm^2)', 
            'Impact of Associativity on Silicon Area', 'plot_area.png')

print("Done! Check your folder for 3 PNG files.")