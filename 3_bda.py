# 3)Graphical Representation of Traditional and Big Data approaches for transferring 250 TB of data

import matplotlib.pyplot as plt
import pandas as pd

# Constants
TOTAL_DATA_TB = 250
NUM_SERVERS_TRADITIONAL = 1
NUM_SERVERS_BIG_DATA = 5
SPEED_MB_PER_SEC = 125
TB_TO_MB = 1024 * 1024

# Function
def calculate_time_days(num_servers, total_data_tb, speed_mb_s):
    total_data_mb = total_data_tb * TB_TO_MB
    effective_speed_mb_s = speed_mb_s * num_servers
    time_seconds = total_data_mb / effective_speed_mb_s
    time_days = time_seconds / (60 * 60 * 24)
    return time_days

# Calculations
days_traditional = calculate_time_days(
    NUM_SERVERS_TRADITIONAL, TOTAL_DATA_TB, SPEED_MB_PER_SEC
)
days_big_data = calculate_time_days(
    NUM_SERVERS_BIG_DATA, TOTAL_DATA_TB, SPEED_MB_PER_SEC
)

# DataFrame
data = {
    'Approach': ['Traditional', 'Big Data'],
    'Transfer Time (Days)': [round(days_traditional, 2), round(days_big_data, 2)]
}
df = pd.DataFrame(data)

# Show table
print(df)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Approach'], df['Transfer Time (Days)'])
plt.ylabel('Time Taken (Days)')
plt.title('Data Transfer Comparison (250 TB @ 1Gbps per server)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval}', ha='center')

# Show only (no saving)
plt.show()