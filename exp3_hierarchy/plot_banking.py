import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('results_banking.csv')

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

# Create a Dual-Axis Plot (The Pro Move)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Access Time (Blue)
color = 'tab:blue'
ax1.set_xlabel('Number of Banks (Parallelism)', fontsize=14)
ax1.set_ylabel('Access Time (ns)', color=color, fontsize=14)
sns.lineplot(data=df, x='Banks', y='Access_Time(ns)', marker='o', color=color, ax=ax1, linewidth=3)
ax1.tick_params(axis='y', labelcolor=color)

# Plot Area (Red) on the Second Y-Axis
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Total Area (mm^2)', color=color, fontsize=14)
sns.lineplot(data=df, x='Banks', y='Area(mm2)', marker='s', color=color, ax=ax2, linewidth=3, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('The Banking Trade-off: Speed vs. Cost', fontsize=16, fontweight='bold')
plt.xscale('log', base=2) # Log scale X because banks are 1, 2, 4, 8...
plt.tight_layout()

plt.savefig('plot_banking_tradeoff.png', dpi=300)
print("Saved plot_banking_tradeoff.png")