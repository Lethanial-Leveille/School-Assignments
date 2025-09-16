converting_from = input("Enter the unit you are converting from: ")
converting_to = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {converting_from}: "))

if converting_from == "Celsius":
    if converting_to == "Fahrenheit":
        temperature = (temperature * 1.8) + 32
    elif converting_to == "Kelvin":
        temperature += 273.15

elif converting_from == "Kelvin":
    if converting_to == "Fahrenheit":
        temperature = (temperature - 273.15) * 1.8 + 32
    elif converting_to == "Celsius":
        temperature -= 273.15

elif converting_from == "Fahrenheit":
    if converting_to == "Celsius":
        temperature = (temperature - 32) * (5/9)
    elif converting_to == "Kelvin":
        temperature = (temperature - 32) * (5/9) + 273.15

print(f"That is {round(temperature, 1)} degrees {converting_to}.")

