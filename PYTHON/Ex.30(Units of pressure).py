# A PROGRAM THAT CONVERTS TO VARIOUS UNITS OF PRESSURE
kp = float(input('Enter the pressure in kilo-pascal: '))
psi = kp * 0.145
atm = kp * 0.00986923
milli_of_merc = kp * 7.501
print('The equivalent in per-square-inch is {:.3f}.'.format(psi))
print('The equivalent in standard atmosphere is {:.3f}.'.format(atm))
print('The equivalent in millimetres of mercury is {:.3f}.'.format(milli_of_merc))