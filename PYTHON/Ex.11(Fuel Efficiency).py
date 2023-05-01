#  CONVERSION OF FUEL EFFICIENCY FROM AMERICAN UNIT TO CANADIAN UNIT
print('1MPG = 235.215l/100km')
value = float(input('How much fuel in miles_per_gallon would you like to purchase? '))
canadian_unit = value * 235.215
print(canadian_unit,'l/100km is your equivalent in Canadian units.')