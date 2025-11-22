import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
try:
    df = pd.read_csv('results_comparison.csv')
except FileNotFoundError:
    print("Error: File not found!")
    exit()

# 2. Sort Logic
tech_order = ['90nm', '65nm', '45nm', '32nm', '22nm']
df['Tech_Val'] = pd.Categorical(df['Tech'], categories=tech_order, ordered=True)
df = df.sort_values('Tech_Val')

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

# 3. Plot Function
def create_dual_plot(y_col, y_label, title, filename, log_scale=False):
    plt.figure(figsize=(10, 6))
    
    # Plot with 'hue' to separate HP vs LSTP
    sns.lineplot(data=df, x='Tech', y=y_col, hue='Type', style='Type',
                 markers=True, dashes=False, linewidth=3, palette=['#D62728', '#1F77B4'])
    
    if log_scale:
        plt.yscale('log') # Leakage changes exponentially!
        
    plt.title(title, fontsize=16, fontweight='bold')
    plt.ylabel(y_label, fontsize=14)
    plt.xlabel("Technology Node", fontsize=14)
    plt.legend(title='Transistor Type')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f"Saved {filename}")
    plt.close()

print("Generating Comparison Plots...")

# Plot 1: Leakage Power (The most important one)
# We use LOG SCALE because leakage explodes by 10x-100x
create_dual_plot('Leakage_Power(mW)', 'Leakage Power (mW) [Log Scale]', 
                 'The Leakage Crisis: HP vs. LSTP', 'plot_leakage_crisis.png', log_scale=True)

# Plot 2: Latency (The Trade-off)
create_dual_plot('Latency(ns)', 'Access Time (ns)', 
                 'Performance Cost: HP vs. LSTP', 'plot_latency_tradeoff.png')

print("Done!")