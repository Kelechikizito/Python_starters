# A PROGRAM THAT DISPLAYS THE BETS THAT PAY OUT IN A ROULETTE SIMULATION
from random import randrange
value = randrange(0,38)
if (value == 0 ): 
    print('The spin resulted in 0...\nPay 0')
elif (value == 37):  #USE 37 TO REP 00
    print('The spin resulted in 00...\nPay 00')
# SINGLE NUMBER
else:
    print('The spin resulted in {}...\nPay {}'.format(value, value))
# RED SPACES
if ((value == 1) or (value == 3) or (value == 5) or (value == 7) or (value == 9) or (value == 12)
    or (value == 14) or (value == 16) or (value == 18) or (value == 19) or (value == 21) or
    (value == 23) or (value == 25) or (value == 27) or (value == 30) or (value == 32) or (value == 34)
    or (value == 36)):
    print('Pay Red')
# BLACK SPACES
if not((value == 1) or (value == 3) or (value == 5) or (value == 7) or (value == 9) or (value == 12)
    or (value == 14) or (value == 16) or (value == 18) or (value == 19) or (value == 21) or
    (value == 23) or (value == 25) or (value == 27) or (value == 30) or (value == 32) or (value == 34)
    or (value == 36) or (value == 37) or (value == 0)):
    print('Pay Black')
if (value % 2 == 1) and not(value == 37):
    print('Pay Odd')
elif (value % 2 == 0) and not(value == 0):
    print('Pay Even')
if (value >= 1) and (value <= 18):
    print('Pay 1 to 18')
elif (value > 18) and (value <= 36):
    print('Pay 19 to 36')