#  A PROGRAM COMPUTES ON THE BASIS OF THE IDEAL GAS LAW
print('''Below is the formulae for the ideal gas law
\tPV = nRT''')
print('R = 8.314 J/molK')
R = 8.314
P = float(input('Enter the pressure of the gas in pascals: '))
V = float(input('Enter the volume of the gas in litres: '))
T1 = float(input('Enter the temperature in celsius: '))
T = T1 + 273.15
n = P*V/R*T
print('The amount of gas contained is {:.3f} moles'.format(n))