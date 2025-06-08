# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Ask the user for temperature
temperature_input = input("Enter the temperature to convert: ")

# Check if the input is a number
if temperature_input.replace('.', '', 1).isdigit():
    temperature = float(temperature_input)

    # Ask for the unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit.upper() == "F":
        result = convert_to_celsius(temperature)
        print(temperature, "°F is", result, "°C")

    elif unit.upper() == "C":
        result = convert_to_fahrenheit(temperature)
        print(temperature, "°C is", result, "°F")

    else:
        print("Invalid unit. Please enter C or F.")

else:
    print("Invalid temperature. Please enter a numeric value.")

