# A PROGRAM THAT GIVES AN ASSESSMENT ON EMPLOYEES AND CALCULATES THIER RESPECTIVE RAISES

Raise = 2400.00
rating = float(input('What is your rating? ')) 
rate = rating

# IF-ELSE STATEMENTS
if rating == 0.0:
    print('This is an Unacceptable Perfomance.\nYou have no raise.')
elif rating == 0.4:
    print('This is an Acceptable Perfomance.\nYou have ${} has a raise.'.format(Raise * 0.4))
elif rating >= 0.6:
    print('This is a Meritorious Performance.\nYou have ${} has a raise.'.format(Raise * rate))
else:
    print('INVALID RATING!')