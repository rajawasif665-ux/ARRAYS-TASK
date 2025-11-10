high_temp = [36, 37, 38, 39, 36, 34, 37]   
low_temp = [26, 27, 26, 28, 27, 24, 26]
# CALCULTAE AVERAGE TEMPERATURE
avg_temp=[]
for i in range(len(high_temp)):
    avg=(high_temp[i]+low_temp[i])/2
    avg_temp.append(avg)
# DETECT HEATWAVE
count=0
heatwave=False
for i in range(len(high_temp)):
    if high_temp[i]>35 and low_temp[i]>25 and avg_temp[1]>30:
        count+=1
        if count>=5:
            heatwave=True
            break
    else:
        count=0
# RESULT
if heatwave:
    print("HEATWAVE DETECTED ")
else:
    ("NO HEATWAVE")

# COLD SNAP
high_tempc=[12, 8, 9, 7, 6, 11, 5]  
low_tempc = [2, -1, -2, -3, -1, 1, -4]
count=0
cold_snap=False
# CHECK 3+ COLD DAYS
for i in range(len(high_tempc)):
    if high_tempc[i]>10 and low_tempc[i]>0:
        count+=1
        if count>=3:
            cold_snap=True
            break
    else:
        count=0
# RESULT
if cold_snap:
    print("COLD_SNAP DETECTED")
else:
    print("NO COLD_SNAP")

# PRESSURE SYSTEM ANAYLSIS    
pressure = [1015, 1022, 1025, 1023, 1018, 999, 995, 998, 1002, 1010]
high_count=0
low_count=0
high_system=0
low_system=0
for i in range(len(pressure)):
    if pressure[i]>1020:
        count+=1
        if count>=3:
            high_system=True
    else:
        high_count=0
# CHECK LOW PRESSURE
for i in range(len(pressure)):
    if pressure[i]<1000:
        count+=1
        if count>=3:
            low_system=True
    else:
        low_count=0

# CLIMATE CALCULATIONS
avg_pressure=sum(pressure)/len(pressure)
highest_pressure=max(pressure)
lowest_pressure=min(pressure)
# RESULT
print("PRESSURE SYSTEM ANAYLSIS")
print(f"DAILY PRESSURE: {pressure}")
print(f"AVG_PRESSURE: {avg_pressure:.2f}hpa")
print(f"HIGHEST_PRESSURE: {highest_pressure}hpa")
print(f"LOWEST_PRESSURE:{lowest_pressure}hpa")
# RESULT
if high_system:
    print("HIGH PRESSURE SYSTEM DETECTED")
elif low_system:
    print("LOW PRESSURE SYSTEM DETECTED")
else:
    print("NO MAJOR PRESSURE SYSTEM DETECTED")

# GDD
Tmax = [25, 28, 30, 35, 33, 20, 18]
Tmin = [15, 16, 18, 20, 19, 10, 8]

Tbase = 10  
GDD_total = 0
HDD_total = 0
CDD_total = 0

for i in range(len(Tmax)):
    avg_temp = (Tmax[i] + Tmin[i]) / 2

#Growing Degree Days
    daily_GDD = avg_temp - Tbase
    if daily_GDD < 0:
        daily_GDD = 0
    GDD_total += daily_GDD
#Heating Degree Days
    if avg_temp < 18:
        HDD_total += (18 - avg_temp)
#Cooling Degree Days
    if avg_temp > 18:
        CDD_total += (avg_temp - 18)

# RESULT
print("Climate Calculations")
print(f"Total Growing Degree Days (GDD): {GDD_total:.2f}")
print(f"Total Heating Degree Days (HDD): {HDD_total:.2f}")
print(f"Total Cooling Degree Days (CDD): {CDD_total:.2f}")
