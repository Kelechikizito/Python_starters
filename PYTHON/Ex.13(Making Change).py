# A PROGRAM THAT MAKES CHANGE FROM USER IN VARIOUS DENOMINATIONS 
toonie_cents = 200
loonie_cents = 100
quarter_cents = 25
dime_cents = 10
nickel_cents = 5
penny_cents = 1
print('''A toonie reps 200 cents
A loonie reps 100 cents
A quarter reps 25 cents
A dime reps 10 cents
A nickel reps 5 units
A penny  reps 1 cent''')
cents = int(input('Enter the desired number of cents: '))
toonie = cents // toonie_cents
toonie_2 = cents % toonie_cents
toonie_statement = str(toonie) + ' toonie'
loonie = toonie_2 // loonie_cents
loonie_2 = toonie_2 % loonie_cents
loonie_statement = str(loonie) + ' loonie'
quarter = loonie_2 // quarter_cents
quarter_2 = loonie_2 % loonie_cents
quarter_statement = str(quarter) + ' quarter'
dime = quarter_2 // dime_cents
dime_2 = quarter_2 % dime_cents
dime_statement = str(dime) + ' dime'
nickel = dime_2 // nickel_cents
nickel_2 = dime_2 % nickel_cents
nickel_statement = str(nickel) + ' nickel'
penny = nickel_2 // penny_cents
penny_statement = str(penny) + ' penny'
print('You have',toonie_statement, loonie_statement, quarter_statement, dime_statement, nickel_statement, penny_statement,'as your change')