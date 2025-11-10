temperature = [30, 28, 32, 35, 33, 25, 20]
humidity = [60, 65, 70, 55, 50, 75, 80]
Tmin = [15, 14, 16, 18, 10, 2, -1]  

THI_values = [] 
frost_days = 0

#Calculate THI and Frost Probability 
for i in range(len(temperature)):
    # THI calculation
    THI = temperature[i] - (0.55 - 0.0055 * humidity[i]) * (temperature[i] - 14.5)
    THI_values.append(THI)

#Frost check (if Tmin ≤ 0°C)
    if Tmin[i] <= 0:
        frost_days += 1

#Frost probability
frost_probability = (frost_days / len(Tmin)) * 100

#Result
print("=== Temperature-Humidity Index (THI) ===")
for i in range(len(temperature)):
    print(f"Day {i+1}: Temp={temperature[i]}°C, Humidity={humidity[i]}%, THI={THI_values[i]:.2f}")

print("\n=== Frost Probability ===")
print(f"Frost Days: {frost_days}/{len(Tmin)}")
print(f"Frost Probability: {frost_probability:.1f}%")