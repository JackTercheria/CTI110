# A brief description of the project
# 9/11/2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter
# Jack Tercheria
#
# Get the temperature in degrees Celsius
# Convert the temperature with the formula
# Print the converted temperature
#
# Get the temperature in degrees Celsius
string_value = input('Temperature in degrees Celsius:  ')
Temperature = int(string_value)

# Convert the temperature to degrees Fahrenheit
F = (9/5)* Temperature + 32

# Display the temperature
print(F)
