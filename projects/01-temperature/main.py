def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:g}°C = {fahrenheit:g}°F")
    except ValueError:
        print("Please enter a valid number.")