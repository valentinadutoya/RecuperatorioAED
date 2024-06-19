cold_days = 0

# Ask the user for the temperature of each day.
for i in range(6):
  temperature = float(input(f"Enter the temperature for day {i+1}: "))

  # Check if the temperature is between -10 and 5 degrees inclusive.
  if -10 <= temperature <= 5:
    cold_days += 1

# Print the number of cold days.
print(f"There were {cold_days} cold days.")