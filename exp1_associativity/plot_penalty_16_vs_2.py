import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
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
df = df.sort_values(by=['Size_Val'])

# 3. Separate the 2-way (Baseline) and 16-way (High Complexity)
# We use 16-way to show the MAXIMUM penalty you can pay
base_df = df[df['Associativity'] == 2].set_index('Size')
high_df = df[df['Associativity'] == 16].set_index('Size')

# 4. Calculate the Ratios (The "Jump" Cost)
# Formula: (High Assoc Value) / (Low Assoc Value)
penalty_df = pd.DataFrame()
penalty_df['Size_Val'] = base_df['Size_Val'] # Keep size for sorting
penalty_df['Latency_Penalty'] = high_df['Access_Time(ns)'] / base_df['Access_Time(ns)']
penalty_df['Energy_Penalty'] = high_df['Read_Energy(nJ)'] / base_df['Read_Energy(nJ)']
penalty_df['Area_Penalty'] = high_df['Area(mm2)'] / base_df['Area(mm2)']

# Reset index to make 'Size' a column again for plotting
penalty_df = penalty_df.reset_index()
penalty_df = penalty_df.sort_values(by='Size_Val')

# 5. Create the "Single Plot"
plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")

# Plot Latency Line
sns.lineplot(data=penalty_df, x='Size', y='Latency_Penalty', marker='o', linewidth=3, 
             label='Latency Penalty', color='tab:blue')

# Plot Energy Line
sns.lineplot(data=penalty_df, x='Size', y='Energy_Penalty', marker='o', linewidth=3, 
             label='Energy Penalty', color='tab:red')

# Plot Area Line
sns.lineplot(data=penalty_df, x='Size', y='Area_Penalty', marker='o', linewidth=3, 
             label='Area Penalty', color='tab:green')

# 6. Formatting
plt.title('The Price of Complexity: 16-way vs. 2-way Overhead', fontsize=16, fontweight='bold')
plt.ylabel('Normalized Factor (1.0 = No Change)', fontsize=14)
plt.xlabel('Cache Size', fontsize=14)
plt.axhline(y=1.0, color='black', linestyle='--', linewidth=1) # The "Baseline" line
plt.xticks(rotation=45)
plt.legend(fontsize=12)
plt.tight_layout()

plt.savefig('plot_penalty_overview.png', dpi=300)
print("Saved plot_penalty_overview.png")