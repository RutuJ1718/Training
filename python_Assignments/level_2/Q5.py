#Function to analyze temperature readings:

def analyze_temperatures(temps):
    avg_temp = sum(temps) / len(temps)
    highest_temp = max(temps)
    lowest_temp = min(temps)
    return avg_temp, highest_temp, lowest_temp

temperature_readings = [25, 28, 21, 24, 27]
avg, high, low = analyze_temperatures(temperature_readings)
print(f"Average Temperature: {avg}")
print(f"Highest Temperature: {high}")
print(f"Lowest Temperature: {low}")
