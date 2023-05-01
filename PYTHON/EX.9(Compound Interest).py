#   A PROGRAM THAT COMPUTES COMPOUND INTEREST
print('Mr Ugwu just opened a new savings account at the rate of 4% per year')
Principal = float(input('How much will be deposited in the first year? '))
Rate = 0.04
First_year = round((Principal * Rate * 1 ) + Principal, 2)
Second_year = round((Principal * Rate * 2 ) + Principal, 2)
Third_year = round((Principal * Rate * 3 ) + Principal, 2)
print('The amount after the first year is N',First_year)
print('The amount after the second year is N',Second_year)
print('The amount after the third year is N',Third_year)

