# A PROGRAM THAT CONVERTS CELSIUS TO FAHRENHEIT AND KELVIN
c = float(input('What is the temperature in degrees Celsius? '))
Fahrenheit = (c * 1.8) + 32
Kelvin = c + 273.15
print('The equivalent in degrees Fahrenheit is {:.2f}'.format(Fahrenheit))
print('The equivalent in degrees Kelvin is {:.2f}'.format(Kelvin))