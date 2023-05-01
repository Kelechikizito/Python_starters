#  BOTTLE DEPOSITS
one_litre_or_less = 0.10
more_than_one_litre = 0.25
first_container = int(input('How many containers of 1 litre or less would you like?'))
second_container = int(input('How many litres of more than 1 litre would you like?'))
refund = one_litre_or_less * first_container + more_than_one_litre * second_container
print('Your refund will be $%.0f' % refund)