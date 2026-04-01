# 2)  A sender wants to send 250TB of data and the server is 4TB each. calculate what is the time
# taken to transfer 250 TB to destination using one server and 4 servers(Assume your Network
# speed)

def calculate_transfer_time():
    total_data_tb = 250
    num_servers = 5
    transfer_speed_mbs = 100  # MB/s per server

    # Conversion: 1 TB = 1,000,000 MB
    total_data_mb = total_data_tb * 1_000_000

    # 1. Traditional Approach (1 Server)
    time_seconds_trad = total_data_mb / transfer_speed_mbs
    days_trad = time_seconds_trad / (3600 * 24)

    # 2. Big Data Approach (Multiple Servers)
    data_per_server_mb = total_data_mb / num_servers
    time_seconds_big_data = data_per_server_mb / transfer_speed_mbs
    days_big_data = time_seconds_big_data / (3600 * 24)

    efficiency_gain = ((days_trad - days_big_data) / days_trad) * 100

    print(f"--- Data Transfer Analysis ({total_data_tb}TB Total) ---")
    print(f"Traditional (1 Server): {days_trad:.2f} Days")
    print(f"Big Data ({num_servers} Servers): {days_big_data:.2f} Days")
    print(f"Efficiency Gain: {efficiency_gain:.2f}% faster")


if __name__ == "__main__":
    calculate_transfer_time()