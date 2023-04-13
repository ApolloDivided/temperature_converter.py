def celsius_to_fahrenheit(temp):
    """Convert temperature in Celsius to Fahrenheit"""
    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    """Convert temperature in Fahrenheit to Celsius"""
    return (temp - 32) * 5/9

while True:
    choice = input("Enter '1' to convert Celsius to Fahrenheit, or '2' to convert Fahrenheit to Celsius: ")
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F\n")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C\n")
    else:
        print("Invalid input. Try again.\n")
