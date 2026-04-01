# 4) This program calculates the time required based on the number of nodes and network bandwidth.

import pandas as pd
def simulate_transfer():
    # Constants
    total_data_tb = 250
    server_capacity_tb = 4
    speed_gbps = 1  # 1 Gigabit per second
    speed_mb_s = (speed_gbps * 1024) / 8  # Convert Gbps to MB/s (125 MB/s)

    # Conversion: 1 TB = 1,048,576 MB
    total_data_mb = total_data_tb * 1024 * 1024

    # Calculation Logic
    def get_time_days(num_servers):
        # Total throughput increases with more servers in Big Data architecture
        effective_speed = speed_mb_s * num_servers
        seconds = total_data_mb / effective_speed
        return seconds / (60 * 60 * 24)

    # 1. Traditional Approach (1 Server)
    time_trad = get_time_days(1)

    # 2. Big Data Approach (5 Servers)
    time_big_data = get_time_days(5)

    print(f"--- Transfer Results (250 TB) ---")
    print(f"Traditional (1 Server): " f"{time_trad:.2f} Days")
    print(f"Big Data (5 Servers): " f"{time_big_data:.2f} Days")
    print(f"Time Saved: " f"{time_trad - time_big_data:.2f} Days")

if __name__ == "__main__":
    simulate_transfer()