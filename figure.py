###
# File: ./dimergeco_figure/figure.py
# Created Date: Tuesday, June 10th 2025
# Author: Zihan
# -----
# Last Modified: Tuesday, 10th June 2025 4:19:44 pm
# Modified By: the developer formerly known as Zihan at <wzh4464@gmail.com>
# -----
# HISTORY:
# Date      		By   	Comments
# ----------		------	---------------------------------------------------------
###

# %%
import pandas as pd
import matplotlib.pyplot as plt

# Data from the user
data = {
    'nodes': [1, 4, 8, 16, 24],
    'Amazon 1000': [1, 0.67, 0.52, 0.44, 0.39],
    'Classic4': [1, 0.88, 0.76, 0.55, 0.52],
    'RCV1-Large': [1, 0.82, 0.66, 0.55, 0.47]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Updated color scheme, removing the first two colors
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

# Plotting the data with the updated color scheme, y-axis range, and evenly spaced x-axis ticks
plt.figure(figsize=(10, 6))
for i, column in enumerate(df.columns[1:]):
    plt.plot(df['nodes'], df[column], marker='o', label=column, color=colors[i])

# Adding title and labels
plt.title('Efficiency vs. Number of Nodes')
plt.xlabel('Number of Nodes')
plt.ylabel('Efficiency')
plt.ylim(0.0, 1.1)
plt.xticks(range(0, 26, 5))
plt.xlim(0, 26)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

## save to effiency.png
plt.savefig('efficiency.png')


# %%
import matplotlib.pyplot as plt
import pandas as pd

# Updated data from the user
data_updated = {
    'partition #': [25, 36, 49, 81, 100, 121],
    'repetition #': [2, 3, 4, 4, 4, 5],
    'time(s)': [3701, 2397, 1660, 721, 512, 665]
}

# colors
colors = ['#377eb8', '#ff7f00']

# Create a DataFrame
df_updated = pd.DataFrame(data_updated)

# Plotting the updated data with the same color scheme, y-axis range starting from 0, and aligned ticks
fig, ax1 = plt.subplots(figsize=(8, 5))

# Plotting repetition #
ax1.set_xlabel('Partition #')
ax1.set_ylabel('Repetition #')
ax1.plot(df_updated['partition #'], df_updated['repetition #'], marker='o', color=colors[0], label='Repetition #')
ax1.tick_params(axis='y')
ax1.axvline(x=100, color='red', linestyle='--', linewidth=1.5)  # Highlight partition 100 with a red dashed line
ax1.annotate('Partition 100', xy=(100, 1), xytext=(105, 2), 
             arrowprops=dict(facecolor='red', shrink=0.05), 
             fontsize=12, color='red', fontweight='bold')  # Add annotation

ax1.set_ylim(0, 8)
ax1.set_yticks(range(0, 9))

# Creating a second y-axis for time(s)
ax2 = ax1.twinx()
ax2.set_ylabel('Time(s)')
ax2.plot(df_updated['partition #'], df_updated['time(s)'], marker='o', color=colors[1], label='Time(s)')
ax2.tick_params(axis='y')
ax2.set_ylim(0, 4000)
ax2.set_yticks(range(0, 4500, 500))

# Adding title and grid
plt.title('Optimisation of Partition Setting')
fig.tight_layout()
ax1.grid(True)  # Ensure the x-axis grid is on

# Show the plot
plt.show()

# save to optimisation.png
plt.savefig('optimisation.png')



