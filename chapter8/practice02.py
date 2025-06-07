def celciusToFahrenheit(C):
    return (C * (9/5)) + 32

celcius = int (input("Enter the celcius value: "))
fahrenheit = celciusToFahrenheit(celcius)

print(f"The fahrenhiet of {celcius} C is {fahrenheit} F ")