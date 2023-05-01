#  A PROGRAM THAT COMPUTES THE WIND CHILL INDEX
print('''A PROGRAM THAT COMPUTES THE WIND CHILL INDEX
WCI = 13.12 + 0.6215*Ta - 11.37 * V**0.16 + 0.3965 * Ta * V**0.16
\t\tWhere Ta = Temperature and V = windspeed''')
Ta = float(input('Enter the temperature in degrees celsius: '))
V = float(input('Enter the wind speed in km/hr: '))
WCI = 13.12 + 0.6215*Ta - 11.37 * V**0.16 + 0.3965 * Ta * V**0.16
print('The Wind Chill Index is {:.0f}'.format(WCI))