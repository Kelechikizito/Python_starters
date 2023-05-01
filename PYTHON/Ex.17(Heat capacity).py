#  A PROGRAM THAT COMPUTES THE COST OF HEATING WATER
# CALCULATING THE TOTAL AMOUNT OF ENERGY
C = 4.186
m = float(input('What is the mass of water in millimeteres? '))  
T = int(input('What is the temperature change? '))
q = m*C*T
# COMPUTING THE COST OF HEATING THE WATER
one_joule = 2.778 * (10 ** -7)
kw_per_hour = q * one_joule
print('{:.2f}'.format(kw_per_hour),'kilowatt-hour is the energy added or removed to achieve the desired temp. change in kw-hr.')
cost_of_heating_water = kw_per_hour * 8.9 
print('{:.2f}'.format(cost_of_heating_water),'cents is the cost of boiling a cup of coffee.')


