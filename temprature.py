hourly_temp = [20, 21, 23, 22, 21, 19, 25, 30, 31, 32, 28, 27, 26, 24, 23, 22, 20, 21, 23, 22, 24, 25, 26, 27]

threshold = 10  
hours_window = 6

print("=== Rapid Temperature Changes (>10°C in 6 hours) ===")
for i in range(len(hourly_temp) - hours_window):
    temp_change = max(hourly_temp[i:i+hours_window]) - min(hourly_temp[i:i+hours_window])
    if temp_change > threshold:
        print(f"Hours {i+1}-{i+hours_window}: Change={temp_change}°C")