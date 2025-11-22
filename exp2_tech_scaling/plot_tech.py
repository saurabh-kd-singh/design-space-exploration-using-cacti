import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
try:
    df = pd.read_csv('results_tech.csv')
except FileNotFoundError:
    print("Error: results_tech.csv not found!")
    exit()

# 2. Sort by Tech Node (Large to Small) to show history moving forward
# We create a mapping to sort correctly: 90nm -> ... -> 22nm
tech_order = ['90nm', '65nm', '45nm', '32nm', '22nm']
df['Tech_Val'] = pd.Categorical(df['Tech_Node'], categories=tech_order, ordered=True)
df = df.sort_values('Tech_Val')

# 3. Plotting Setup
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12, 'font.family': 'sans-serif'})

def create_plot(y_col, y_label, title, filename, color):
    plt.figure(figsize=(10, 6))
    
    # Plot line
    sns.lineplot(data=df, x='Tech_Node', y=y_col, marker='o', 
                 linewidth=3, color=color, sort=False)
    
    # Add labels
    plt.title(title, fontsize=16, fontweight='bold')
    plt.ylabel(y_label, fontsize=14)
    plt.xlabel("Technology Node (Process Size)", fontsize=14)
    
    # Invert X axis to show time progression (Left=Old, Right=New)
    # Actually, standard is usually High to Low nm. The sort above handles it.
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f"Saved {filename}")
    plt.close()

# 4. Generate the 3 Plots
print("Generating Moore's Law Plots...")

# Area (The most famous one)
create_plot('Area(mm2)', 'Area (mm^2)', 
            'Moore\'s Law: Area Scaling (90nm to 22nm)', 'plot_tech_area.png', 'tab:green')

# Energy (Dennard Scaling)
create_plot('Read_Energy(nJ)', 'Read Energy (nJ)', 
            'Energy Efficiency Scaling', 'plot_tech_energy.png', 'tab:red')

# Latency
create_plot('Access_Time(ns)', 'Access Time (ns)', 
            'Performance Scaling (Latency)', 'plot_tech_latency.png', 'tab:blue')

print("Done!")