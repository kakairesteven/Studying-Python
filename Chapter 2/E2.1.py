"""
(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from
the console and converts it to Fahrenheit and displays the result. The formula for
the conversion is as follows:
fahrenheit = (9 / 5) * celsius + 32
"""

# Takes user input and converts it to integer.
# inputs are treated as strings. thus conversion
celsiusTemp = eval(input("Enter a degree in Celcius: "))
fahrenheitTemp = (9 / 5) * celsiusTemp + 32

print(celsiusTemp, 'is', fahrenheitTemp, "Fahrenheit")

# Run program and input a valid number.