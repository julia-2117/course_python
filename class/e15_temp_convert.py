"""
Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns.
The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the Internet.
"""
print('Celcius  Farenheit')
for g in range(0, 101, 10):
    f = g*(9/5)+32
    print(g, f, sep='       ')




