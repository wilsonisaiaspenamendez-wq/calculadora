def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def meters_to_km(meters):
    kilometers = meters / 1000
    return kilometers

def units_conversion(value, unit_from, unit_to):
    if unit_from == 'C' and unit_to == 'F':
        return celsius_to_fahrenheit(value)
    elif unit_from == 'M' and unit_to == 'K':
        return meters_to_km(value)
    else:
        raise ValueError("Unsupported conversion")

# Get user input
value = float(input("Enter a value: "))
unit_from = input("Enter the unit (C or M): ").upper()
unit_to = input("Enter the target unit (F or K): ").upper()

# Perform conversion
result = units_conversion(value, unit_from, unit_to)

# Print result
print(f"{value} {unit_from} is equal to {result:.2f} {unit_to}")
